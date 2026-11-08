import io
import json
import subprocess
import sys
import tempfile
import time
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

from generator import harvest_awesome


def search_response(items, incomplete=False):
    return io.BytesIO(json.dumps({
        "total_count": len(items),
        "incomplete_results": incomplete,
        "items": items,
    }).encode())


class HarvestTests(unittest.TestCase):
    def setUp(self):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        root = Path(directory.name)
        self.catalog = root / "generator" / "awesome_auto.json"
        self.catalog.parent.mkdir()
        (root / "docs").mkdir()
        (root / "docs" / "awesome-learning.md").write_text(
            "- **[Curated](https://github.com/example/curated)**\n", encoding="utf-8"
        )
        self.original = {"generated": "2026-10-01", "sections": [
            {"key": "books", "title": harvest_awesome.TITLES["books"], "entries": [
                {"name": "previous", "full": "example/previous", "desc": "Cached book", "stars": 100},
            ]},
            {"key": "courses", "title": harvest_awesome.TITLES["courses"], "entries": [
                {"name": "course", "full": "example/course", "desc": "Another group", "stars": 200},
            ]},
        ]}
        self.catalog.write_text(json.dumps(self.original), encoding="utf-8")
        self.enter_patch(patch.object(harvest_awesome, "ROOT", directory.name))
        self.enter_patch(patch.object(harvest_awesome, "_calls", []))
        self.enter_patch(patch.object(harvest_awesome, "QUERIES", {"books": [("topic:books", 2)]}))
        self.enter_patch(patch.object(sys, "argv", ["harvest_awesome.py", "books"]))

    def enter_patch(self, patcher):
        patcher.start()
        self.addCleanup(patcher.stop)

    def run_harvest(self, responses):
        with patch.object(harvest_awesome.OP, "open", side_effect=responses), redirect_stdout(io.StringIO()):
            return harvest_awesome.main()

    def test_rerun_keeps_cached_entries_and_respects_other_groups(self):
        items = [
            {"name": name, "full_name": "example/" + name, "description": "Useful", "stargazers_count": 300}
            for name in ("new", "curated", "course")
        ]
        for _ in range(2):
            self.run_harvest([search_response(items)])
            sections = json.loads(self.catalog.read_text(encoding="utf-8"))["sections"]
            self.assertEqual(
                [entry["full"] for entry in sections[0]["entries"]],
                ["example/new", "example/previous"],
            )
            self.assertEqual(sections[1], self.original["sections"][1])

    def test_repository_names_are_compared_case_insensitively(self):
        self.run_harvest([search_response([
            {"full_name": "Example/Previous", "description": "Updated", "stargazers_count": 250},
            {"full_name": "Example/Course", "description": "Already grouped", "stargazers_count": 300},
            {"full_name": "Example/Curated", "description": "Already curated", "stargazers_count": 300},
        ])])
        entries = json.loads(self.catalog.read_text(encoding="utf-8"))["sections"][0]["entries"]
        self.assertEqual([entry["full"] for entry in entries], ["Example/Previous"])
        self.assertEqual(entries[0]["stars"], 250)

    def test_failed_or_incomplete_page_keeps_existing_file(self):
        before = self.catalog.read_bytes()
        for response in (OSError("page request failed"), search_response([], incomplete=True)):
            with self.subTest(response=response):
                self.catalog.write_bytes(before)
                first_page = search_response([
                    {"name": "new", "full_name": "example/new", "description": "Useful", "stargazers_count": 300},
                    *[{}] * 99,
                ])
                result = self.run_harvest([first_page, response])
                self.assertEqual(self.catalog.read_bytes(), before)
                self.assertEqual(result, 1)

    def test_failed_replace_keeps_existing_file(self):
        before = self.catalog.read_bytes()
        with patch.object(harvest_awesome.os, "replace", side_effect=PermissionError("Output is in use")):
            with self.assertRaises(PermissionError):
                self.run_harvest([search_response([])])
        self.assertEqual(self.catalog.read_bytes(), before)
        files = [path for path in self.catalog.parent.iterdir() if path.name != ".awesome_auto.lock"]
        self.assertEqual(files, [self.catalog])

    def test_concurrent_harvest_is_busy_and_crash_releases_lock(self):
        child = """
from pathlib import Path
import sys
from generator import harvest_awesome

root, group, hold = sys.argv[1:]
harvest_awesome.ROOT = root
harvest_awesome.QUERIES = {group: [("topic:" + group, 1)]}
sys.argv = ["harvest_awesome.py", group]

def fake_search(*args):
    if hold == "hold":
        (Path(root) / "ready").touch()
        sys.stdin.read(1)
    return [{"full_name": "example/new-" + group, "description": "New entry", "stargazers_count": 500}]

harvest_awesome.search = fake_search
sys.exit(harvest_awesome.main())
"""
        root = self.catalog.parent.parent
        command = [sys.executable, "-c", child, str(root)]
        repo = Path(harvest_awesome.__file__).resolve().parents[1]
        before = self.catalog.read_bytes()
        with subprocess.Popen(command + ["books", "hold"], cwd=repo, stdin=subprocess.PIPE) as holder:
            try:
                deadline = time.monotonic() + 10
                while not (root / "ready").exists() and holder.poll() is None and time.monotonic() < deadline:
                    time.sleep(0.01)
                self.assertTrue((root / "ready").exists(), "first harvest did not reach search")
                busy = subprocess.run(command + ["courses", "run"], cwd=repo, capture_output=True, timeout=10)
                self.assertEqual(busy.returncode, 1)
                self.assertIn(b"already running", busy.stderr)
                self.assertEqual(self.catalog.read_bytes(), before)
            finally:
                if holder.poll() is None:
                    holder.kill()
                holder.wait(timeout=10)

        retry = subprocess.run(command + ["courses", "run"], cwd=repo, capture_output=True, timeout=10)
        self.assertEqual(retry.returncode, 0, retry.stderr)
        sections = json.loads(self.catalog.read_text(encoding="utf-8"))["sections"]
        self.assertEqual(sections[0], self.original["sections"][0])
        self.assertEqual(sections[1]["entries"][0]["full"], "example/new-courses")

    def test_throttles_unauthenticated_searches(self):
        now = 0.0
        requested_at = []

        def advance(seconds):
            nonlocal now
            now += seconds

        def open_page(*args, **kwargs):
            requested_at.append(now)
            return search_response([{}] * 100)

        with patch.object(harvest_awesome, "TOKEN", ""), \
                patch.object(harvest_awesome.time, "monotonic", side_effect=lambda: now), \
                patch.object(harvest_awesome.time, "sleep", side_effect=advance), \
                patch.object(harvest_awesome.OP, "open", side_effect=open_page):
            harvest_awesome.search("topic:books", 11)

        self.assertEqual(requested_at[:10], [0.0] * 10)
        self.assertGreaterEqual(requested_at[10], 60.0)
