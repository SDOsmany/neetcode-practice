"""Runs one problem's tests. Press Run on a problem file, or use track.py."""
import ast
import importlib.util
import io
import json
import linecache
import pathlib
import sys
import traceback

ROOT = pathlib.Path(__file__).resolve().parent


def eq(got, want):
    if got != want:
        raise AssertionError(f"got {got!r}, expected {want!r}")


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def run(path):
    path = pathlib.Path(path).resolve()
    tests = ROOT / "_tests" / path.name
    try:
        _load("_problem_tests", tests).check(_load("_solution", path), eq)
    except Exception as e:
        tb = traceback.extract_tb(e.__traceback__)
        test_lines = [f for f in tb if f.filename == str(tests)]
        print(f"FAIL  {path.stem}")
        if test_lines:
            print(f"  test: {test_lines[-1].line}")
        print(f"  {type(e).__name__}: {e}")
        if not isinstance(e, AssertionError):
            print(f"  at {tb[-1].filename.split('/')[-1]} line {tb[-1].lineno}")
        sys.exit(1)
    print(f"PASS  {path.stem}")


def _test_call(line):
    """Turns a test line like eq(s.f(1), 2) into just s.f(1) for display."""
    try:
        call = ast.parse(line).body[0].value
        if call.func.id == "eq":
            return ast.get_source_segment(line, call.args[0]).replace(",mod)", ")")
    except Exception:
        pass
    return line


def run_json(path):
    """Used by the website: reports every test case and anything the code printed."""
    path = pathlib.Path(path).resolve()
    tests = ROOT / "_tests" / path.name
    cases = []

    def record(got, want):
        frame = sys._getframe(1)
        cases.append({
            "test": linecache.getline(frame.f_code.co_filename, frame.f_lineno).strip(),
            "call": _test_call(linecache.getline(frame.f_code.co_filename, frame.f_lineno).strip()),
            "got": repr(got)[:2000],
            "want": repr(want)[:2000],
            "ok": bool(got == want),
        })

    printed = io.StringIO()
    error = None
    real_stdout = sys.stdout
    sys.stdout = printed
    try:
        _load("_problem_tests", tests).check(_load("_solution", path), record)
    except Exception as e:
        tb = traceback.extract_tb(e.__traceback__)
        in_code = [f for f in tb if f.filename == str(path)]
        in_test = [f for f in tb if f.filename == str(tests)]
        lineno = in_code[-1].lineno if in_code else None
        if isinstance(e, SyntaxError) and e.filename == str(path):
            lineno = e.lineno
        error = {
            "message": f"{type(e).__name__}: {e.msg if isinstance(e, SyntaxError) else e}",
            "lineno": lineno,
            "test": _test_call(in_test[-1].line) if in_test else None,
        }
    mine = run_my_tests(path, tests)
    sys.stdout = real_stdout
    print(json.dumps({"cases": cases, "error": error, "mine": mine, "printed": printed.getvalue()[:20000]}))


def run_my_tests(path, tests):
    """Runs the tests you added on the site. They don't affect Solved status."""
    saved = ROOT / "my_tests" / f"{path.stem}.json"
    if not saved.exists():
        return []
    results = []
    for t in json.loads(saved.read_text()):
        result = {"code": t["code"], "expected": t["expected"], "ok": False, "got": None, "error": None}
        try:
            mod = _load("_solution", path)
            ns = {"mod": mod}
            ns.update(vars(_load("_problem_tests", tests)))
            ns.update({k: v for k, v in vars(mod).items() if not k.startswith("__")})
            ns.pop("check", None)
            if hasattr(mod, "Solution"):
                ns["s"] = mod.Solution()
            ns["mk"] = (lambda mk: (lambda vals, m=mod: mk(vals, m)))(ns["mk"]) if "mk" in ns else None
            tree = ast.parse(t["code"])
            if not tree.body or not isinstance(tree.body[-1], ast.Expr):
                raise ValueError("The last line must be a value to check, such as s.twoSum([1, 2], 3)")
            setup, last = tree.body[:-1], tree.body[-1]
            exec(compile(ast.Module(setup, []), "<my test>", "exec"), ns)
            got = eval(compile(ast.Expression(last.value), "<my test>", "eval"), ns)
            want = eval(t["expected"], ns)
            result.update(got=repr(got)[:2000], want=repr(want)[:2000], ok=bool(got == want))
        except Exception as e:
            result["error"] = f"{type(e).__name__}: {e.msg if isinstance(e, SyntaxError) else e}"
        results.append(result)
    return results


def example_test(slug):
    """Builds a starting point for a new test from a problem's first built-in test."""
    source =(ROOT / "_tests" / f"{slug}.py").read_text()
    tree = ast.parse(source)
    check = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == "check")
    setup = []
    for node in check.body:
        call = node.value if isinstance(node, ast.Expr) else None
        if isinstance(call, ast.Call) and getattr(call.func, "id", "") == "eq":
            code = ast.get_source_segment(source, call.args[0])
            expected = ast.get_source_segment(source, call.args[1])
            return {"code": "\n".join(setup + [code]).replace(",mod)", ")"), "expected": expected}
        text = ast.get_source_segment(source, node)
        if text != "s = mod.Solution()":
            setup.append(text)
    return {"code": "", "expected": ""}


if __name__ == "__main__":
    if sys.argv[2:] == ["--json"]:
        run_json(sys.argv[1])
    else:
        run(sys.argv[1])
