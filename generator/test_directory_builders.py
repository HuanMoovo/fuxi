import io
import json
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from unittest.mock import patch
from urllib.error import HTTPError, URLError

from generator import build_awesome, build_lifespan


class DirectoryBuildTests(unittest.TestCase):
    def run_builder(self, builder, failed_lookup):
        if builder is build_awesome:
            filename = "awesome-learning.md"
            data = [("Books", [("Good", "example/good", "Book", "1"),
                               ("Missing", "example/missing", "Book", "1")])]
        else:
            filename = "awesome-lifespan.md"
            data = [("Books", "Focus", "Note", "1", [
                ("Good", "example/good", "Book"),
                ("Missing", "example/missing", "Book"),
            ])]

        def open_repository(request, timeout):
            if request.full_url.endswith("/missing"):
                raise failed_lookup
            return io.BytesIO(json.dumps({
                "stargazers_count": 20,
                "full_name": "example/good",
            }).encode())

        with tempfile.TemporaryDirectory() as root:
            destination = Path(root) / "docs" / filename
            destination.parent.mkdir()
            destination.write_text("Existing catalog", encoding="utf-8")
            with patch.object(builder, "ROOT", root), patch.object(builder, "DATA", data), \
                    patch.object(builder.OP, "open", side_effect=open_repository), \
                    redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
                status = builder.main()
            return status, destination.read_text(encoding="utf-8")

    def test_api_errors_preserve_existing_catalog(self):
        for builder in (build_awesome, build_lifespan):
            for code in (403, 429, 503, None):
                with self.subTest(builder=builder.__name__, status=code):
                    failure = (URLError("Connection refused") if code is None
                               else HTTPError("https://api.github.com", code, "API error", None, None))
                    status, catalog = self.run_builder(builder, failure)
                    self.assertEqual(catalog, "Existing catalog")
                    self.assertEqual(status, 1)

    def test_missing_repository_can_be_skipped(self):
        for builder in (build_awesome, build_lifespan):
            with self.subTest(builder=builder.__name__):
                missing = HTTPError("https://api.github.com", 404, "Not found", None, None)
                status, catalog = self.run_builder(builder, missing)
                self.assertIn("https://github.com/example/good", catalog)
                self.assertNotIn("https://github.com/example/missing", catalog)
                self.assertIn(status, (None, 0))
