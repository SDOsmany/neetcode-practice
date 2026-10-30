#!/usr/bin/env python3
"""Progress tracker. Progress comes from your files and their tests.

  python3 track.py               show progress
  python3 track.py next          show the next unsolved problem
  python3 track.py test two_sum  run one problem's tests
  python3 track.py hint two_sum  show a hint
  python3 track.py answer two_sum  show a reference answer
  python3 track.py reset two_sum   restore one problem to blank
  python3 track.py reset all       restore everything to blank
"""
import filecmp
import json
import pathlib
import shutil
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor

ROOT = pathlib.Path(__file__).resolve().parent
META = json.loads((ROOT / "_meta.json").read_text())
HARNESS = ROOT / "_harness.py"
TIMEOUT = 10


def path_of(p):
    return ROOT / "problems" / p["cat"] / f'{p["slug"]}.py'


def starter_of(p):
    return ROOT / "_starters" / f'{p["slug"]}.py'


def run_tests(p):
    try:
        return subprocess.run([sys.executable, str(HARNESS), str(path_of(p))],
                              capture_output=True, text=True, timeout=TIMEOUT)
    except subprocess.TimeoutExpired:
        return None


def status_of(p):
    path = path_of(p)
    if not path.exists() or filecmp.cmp(path, starter_of(p), shallow=False):
        return "todo"
    result = run_tests(p)
    return "solved" if result and result.returncode == 0 else "started"


def statuses():
    with ThreadPoolExecutor(8) as pool:
        return list(pool.map(status_of, META))


def find(slug):
    for p in META:
        if p["slug"] == slug:
            return p
    sys.exit(f"No problem called {slug!r}. Run: python3 track.py to see the names.")


def show():
    marks = {"todo": "[ ]", "started": "[~]", "solved": "[x]"}
    all_status = statuses()
    cat = None
    for p, s in zip(META, all_status):
        if p["cat"] != cat:
            cat = p["cat"]
            group = [x for q, x in zip(META, all_status) if q["cat"] == cat]
            name = cat[3:].replace("_", " ").title()
            print(f'\n{name} ({group.count("solved")}/{len(group)})')
        print(f'  {marks[s]} {p["slug"]:<38} {p["diff"]}')
    solved = all_status.count("solved")
    print(f"\nSolved {solved}/{len(META)}, started {all_status.count('started')}")
    print("[x] tests pass   [~] edited, tests not passing yet   [ ] untouched")


def next_problem():
    for p, s in zip(META, statuses()):
        if s != "solved":
            print(f'{p["title"]} ({p["diff"]})\n{path_of(p).relative_to(ROOT)}')
            return
    print("Everything is solved. Use: python3 track.py reset all")


def test(slug):
    p = find(slug)
    result = run_tests(p)
    if result is None:
        sys.exit(f"FAIL  {slug}\n  Still running after {TIMEOUT}s. Check for an infinite loop.")
    print((result.stdout + result.stderr).rstrip())
    sys.exit(result.returncode)


def restore(targets):
    """Blank the given problems, keeping a copy of any code in backups/. Returns how many were copied."""
    stamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    saved = 0
    for p in targets:
        path = path_of(p)
        if not filecmp.cmp(path, starter_of(p), shallow=False):
            folder = ROOT / "backups" / stamp
            folder.mkdir(parents=True, exist_ok=True)
            shutil.copy(path, folder / path.name)
            saved += 1
        shutil.copy(starter_of(p), path)
    return saved


def reset(target):
    if target == "all":
        edited = [p for p in META if status_of(p) != "todo"]
        if not edited:
            print("Everything is already blank.")
            return
        print(f"This blanks {len(edited)} problem file(s). A copy of your code goes to backups/.")
        if input('Type "yes" to continue: ').strip() != "yes":
            print("Nothing changed.")
            return
        targets = edited
    else:
        targets = [find(target)]
    restore(targets)
    print(f"Reset {len(targets)} problem(s).")


def main():
    args = sys.argv[1:]
    if not args:
        show()
    elif args == ["next"]:
        next_problem()
    elif len(args) == 2 and args[0] == "test":
        test(args[1])
    elif len(args) == 2 and args[0] == "hint":
        print(find(args[1])["hint"])
    elif len(args) == 2 and args[0] == "answer":
        print((ROOT / "_answers" / f'{find(args[1])["slug"]}.py').read_text())
    elif len(args) == 2 and args[0] == "reset":
        reset(args[1])
    else:
        print(__doc__)


if __name__ == "__main__":
    main()
