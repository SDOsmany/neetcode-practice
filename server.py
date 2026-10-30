#!/usr/bin/env python3
"""Local practice website. Run: python3 server.py"""
import json
import mimetypes
import os
import subprocess
import sys
import threading
import time
import urllib.request
import webbrowser
from concurrent.futures import ThreadPoolExecutor
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

import _harness as harness
import track

VERSION = 3
ROOT = track.ROOT
WEB = ROOT / "web"
BY_SLUG = {p["slug"]: p for p in track.META}
FOOTER = '\n\n\nif __name__ == "__main__":\n    import pathlib, sys\n'
MY_TESTS = ROOT / "my_tests"
PROGRESS = ROOT / "progress.json"
MAX_BODY = 1_000_000
PORTS = range(8765, 8785)

progress_lock = threading.Lock()
status_cache = {}


def split_file(text):
    """Split a problem file into its description, the editable code and its footer."""
    doc_end = text.find('"""\n\n', 3)
    head = text[:doc_end + 5] if text.startswith('"""') and doc_end != -1 else ""
    rest = text[len(head):]
    cut = rest.rfind(FOOTER)
    code, foot = (rest[:cut], rest[cut:]) if cut != -1 else (rest, "")
    return head, code, foot


def template_parts(p):
    head, _, foot = split_file(track.starter_of(p).read_text())
    return head, foot


def description(p):
    head, _ = template_parts(p)
    return head.strip().strip('"').strip().split("\n\n", 1)[1]


def read_code(p):
    return split_file(track.path_of(p).read_text())[1]


def save_code(p, code):
    head, foot = template_parts(p)
    path = track.path_of(p)
    tmp = path.with_suffix(".tmp")
    tmp.write_text(head + code.rstrip() + foot)
    os.replace(tmp, path)


def read_my_tests(p):
    path = MY_TESTS / f'{p["slug"]}.json'
    return json.loads(path.read_text()) if path.exists() else []


def save_my_tests(p, tests):
    MY_TESTS.mkdir(exist_ok=True)
    clean = [{"code": str(t["code"]), "expected": str(t["expected"])} for t in tests]
    (MY_TESTS / f'{p["slug"]}.json').write_text(json.dumps(clean, indent=1))


def read_progress():
    return json.loads(PROGRESS.read_text()) if PROGRESS.exists() else {}


def update_progress(slug, changes):
    """Stars and notes. Solved status always comes from the tests."""
    with progress_lock:
        data = read_progress()
        entry = data.setdefault(slug, {})
        if "star" in changes:
            entry["star"] = bool(changes["star"])
        if "notes" in changes:
            entry["notes"] = str(changes["notes"])
        tmp = PROGRESS.with_suffix(".tmp")
        tmp.write_text(json.dumps(data, indent=1))
        os.replace(tmp, PROGRESS)


def run_problem(p):
    path = track.path_of(p)
    started = time.perf_counter()
    try:
        result = subprocess.run([sys.executable, str(track.HARNESS), str(path), "--json"],
                                capture_output=True, text=True, timeout=track.TIMEOUT, cwd=ROOT)
    except subprocess.TimeoutExpired:
        return {"cases": [], "mine": [], "printed": "", "error": {
            "message": f"Time limit: still running after {track.TIMEOUT} seconds. Check for an infinite loop.",
            "lineno": None, "test": None}}
    try:
        out = json.loads(result.stdout)
    except ValueError:
        return {"cases": [], "mine": [], "printed": "", "error": {
            "message": (result.stderr or result.stdout or "The program stopped unexpectedly.")[-2000:],
            "lineno": None, "test": None}}
    out["ms"] = round((time.perf_counter() - started) * 1000)
    if out["error"] and out["error"]["lineno"]:
        # Line numbers in the editor don't include the description at the top of the file.
        offset = split_file(path.read_text())[0].count("\n")
        out["error"]["lineno"] -= offset
    return out


def cached_status(p):
    # Only re-run tests for files that changed since the last check.
    stat = track.path_of(p).stat()
    key = (stat.st_mtime_ns, stat.st_size)
    cached = status_cache.get(p["slug"])
    if cached and cached[0] == key:
        return cached[1]
    status = track.status_of(p)
    status_cache[p["slug"]] = (key, status)
    return status


def problem_list():
    with ThreadPoolExecutor(8) as pool:
        statuses = list(pool.map(cached_status, track.META))
    progress = read_progress()
    return [{"slug": p["slug"], "title": p["title"], "diff": p["diff"], "cat": p["cat"], "status": s,
             "star": progress.get(p["slug"], {}).get("star", False)}
            for p, s in zip(track.META, statuses)]


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *args):
        pass

    def allowed(self):
        # This server runs code, so only accept requests from its own page.
        port = self.server.server_address[1]
        own = {f"127.0.0.1:{port}", f"localhost:{port}"}
        if self.headers.get("Host") not in own:
            return False
        origin = self.headers.get("Origin")
        return origin is None or origin in {f"http://{h}" for h in own}

    def send_json(self, obj, code=200):
        body = json.dumps(obj).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if not self.allowed():
            return self.send_error(403)
        path = self.path.split("?")[0]
        if path == "/api/version":
            return self.send_json({"version": VERSION})
        if path == "/api/problems":
            return self.send_json(problem_list())
        if path.startswith("/api/problem/"):
            p = BY_SLUG.get(path.rsplit("/", 1)[1])
            if not p:
                return self.send_error(404)
            saved = read_progress().get(p["slug"], {})
            return self.send_json({"slug": p["slug"], "title": p["title"], "diff": p["diff"],
                                   "cat": p["cat"], "hint": p["hint"],
                                   "text": description(p), "code": read_code(p),
                                   "myTests": read_my_tests(p),
                                   "example": harness.example_test(p["slug"]),
                                   "star": saved.get("star", False), "notes": saved.get("notes", "")})
        if path.startswith("/api/answer/"):
            p = BY_SLUG.get(path.rsplit("/", 1)[1])
            if not p:
                return self.send_error(404)
            answer = (ROOT / "_answers" / f'{p["slug"]}.py').read_text()
            return self.send_json({"code": split_file(answer)[1]})
        self.send_static("index.html" if path == "/" else path.lstrip("/"))

    def send_static(self, rel):
        target = (WEB / rel).resolve()
        if WEB.resolve() not in target.parents or not target.is_file():
            return self.send_error(404)
        body = target.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", mimetypes.guess_type(target.name)[0] or "application/octet-stream")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def do_POST(self):
        if not self.allowed() or self.headers.get("Content-Type") != "application/json":
            return self.send_error(403)
        length = int(self.headers.get("Content-Length", 0))
        if length > MAX_BODY:
            return self.send_error(413)
        data = json.loads(self.rfile.read(length) or b"{}")
        if self.path == "/api/reset-all":
            saved = track.restore(track.META)
            return self.send_json({"backedUp": saved})
        p = BY_SLUG.get(data.get("slug"))
        if not p:
            return self.send_error(404)
        if self.path == "/api/save":
            save_code(p, data["code"])
            return self.send_json({"ok": True})
        if self.path == "/api/my-tests":
            save_my_tests(p, data["tests"])
            return self.send_json({"ok": True})
        if self.path == "/api/progress":
            update_progress(p["slug"], data)
            return self.send_json({"ok": True})
        if self.path == "/api/run":
            save_code(p, data["code"])
            save_my_tests(p, data.get("myTests", []))
            return self.send_json(run_problem(p))
        if self.path == "/api/reset":
            track.restore([p])
            return self.send_json({"code": read_code(p)})
        self.send_error(404)


def running_version(port):
    try:
        with urllib.request.urlopen(f"http://127.0.0.1:{port}/api/version", timeout=1) as res:
            return json.load(res).get("version")
    except Exception:
        return None


def main():
    open_browser = "--no-browser" not in sys.argv
    server = None
    for port in PORTS:
        try:
            server = ThreadingHTTPServer(("127.0.0.1", port), Handler)
            break
        except OSError:
            if running_version(port) == VERSION:
                url = f"http://127.0.0.1:{port}/"
                print(f"The practice site is already running at {url}")
                if open_browser:
                    webbrowser.open(url)
                return
    if server is None:
        sys.exit("Couldn't find a free port. Close other practice windows and try again.")
    url = f"http://127.0.0.1:{server.server_address[1]}/"
    print(f"Practice site running at {url}\nKeep this window open. Press Ctrl+C to stop.", flush=True)
    if open_browser:
        threading.Timer(0.3, webbrowser.open, [url]).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")


if __name__ == "__main__":
    main()
