import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
TEMPLATES = ROOT / "templates"


class CliTests(unittest.TestCase):
    def run_cli(self, *args, cwd=ROOT):
        env = dict(os.environ, PYTHONPATH=str(ROOT))
        env.pop("PYTHONIOENCODING", None)
        return subprocess.run(
            [sys.executable, "-m", "fuxi_cli", *args],
            cwd=cwd,
            env=env,
            capture_output=True,
            encoding="utf-8",
            timeout=10,
        )

    def test_list_stages_from_another_directory(self):
        with tempfile.TemporaryDirectory() as folder:
            result = self.run_cli("stages", cwd=folder)

        self.assertEqual(result.returncode, 0, result.stderr)
        lines = result.stdout.splitlines()
        self.assertEqual(len(lines), 11)
        self.assertIn("立志", lines[0])
        self.assertIn("拓界", lines[-1])

    def test_stage_accepts_number_or_slug(self):
        expected = (ROOT / "docs/stages/02-map.md").read_text(encoding="utf-8")
        for selector in ("2", "02", "map"):
            with self.subTest(selector=selector):
                result = self.run_cli("stage", selector)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(result.stdout, expected)

    def test_unknown_stage_returns_usage_error(self):
        result = self.run_cli("stage", "12")
        self.assertEqual(result.returncode, 2)
        self.assertIn("12", result.stderr)
        self.assertEqual(result.stdout, "")

    def test_init_exports_all_templates_without_overwriting(self):
        with tempfile.TemporaryDirectory() as folder:
            project = Path(folder) / "我的 学习计划"
            result = self.run_cli("init", str(project), "--topic", "数据分析")
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(
                {path.name for path in project.iterdir()},
                {path.name for path in TEMPLATES.glob("*.md")},
            )
            contract = project / "learning-contract.md"
            contents = contract.read_text(encoding="utf-8")
            self.assertIn("**领域**：数据分析", contents)
            self.assertIn("CC BY 4.0", contents)
            self.assertNotIn("(../docs/README.md)", contents)

            contract.write_text("我的记录", encoding="utf-8")
            duplicate = self.run_cli("init", str(project))
            self.assertEqual(duplicate.returncode, 1)
            self.assertEqual(contract.read_text(encoding="utf-8"), "我的记录")

    def test_status_tracks_checked_boxes_in_the_local_checklist(self):
        with tempfile.TemporaryDirectory() as folder:
            project = Path(folder) / "学习计划"
            created = self.run_cli("init", str(project))
            self.assertEqual(created.returncode, 0, created.stderr)
            checklist = project / "stage-checklist.md"
            original = checklist.read_text(encoding="utf-8")
            checklist.write_text(original.replace("- [ ]", "- [X]", 1), encoding="utf-8")

            result = self.run_cli("status", "--json", cwd=project)
            self.assertEqual(result.returncode, 0, result.stderr)
            progress = json.loads(result.stdout)
            self.assertEqual(progress["checked"], 1)
            self.assertEqual(progress["total"], original.count("- [ ]"))
            self.assertEqual(len(progress["stages"]), 10)
            self.assertEqual(progress["stages"][0]["checked"], 1)
            self.assertEqual(progress["stages"][1]["checked"], 0)

            summary = self.run_cli("status", str(project))
            self.assertEqual(summary.returncode, 0, summary.stderr)
            self.assertIn(f"1/{progress['total']}", summary.stdout)

    def test_status_rejects_missing_or_incomplete_checklist(self):
        with tempfile.TemporaryDirectory() as folder:
            missing = self.run_cli("status", folder)
            self.assertEqual(missing.returncode, 1)
            self.assertIn("stage-checklist.md", missing.stderr)

            checklist = Path(folder) / "stage-checklist.md"
            checklist.write_text("## 第 1 阶 · 立志\n- [x] 已通过\n", encoding="utf-8")
            incomplete = self.run_cli("status", folder)
            self.assertEqual(incomplete.returncode, 1)
            self.assertEqual(incomplete.stdout, "")

    def test_status_ignores_checkboxes_and_headings_in_code_examples(self):
        with tempfile.TemporaryDirectory() as folder:
            original = (TEMPLATES / "stage-checklist.md").read_text(encoding="utf-8")
            examples = (
                "````markdown\n```\n## 第 1 阶 · 示例\n- [x] 代码示例\n````\n\n"
                "~~~markdown\n- [X] 另一段代码示例\n~~~\n\n"
            )
            modified = original.replace("## 第 2 阶", examples + "## 第 2 阶", 1)
            (Path(folder) / "stage-checklist.md").write_text(modified, encoding="utf-8")

            result = self.run_cli("status", folder, "--json")

        self.assertEqual(result.returncode, 0, result.stderr)
        progress = json.loads(result.stdout)
        self.assertEqual(progress["checked"], 0)
        self.assertEqual(progress["total"], original.count("- [ ]"))
