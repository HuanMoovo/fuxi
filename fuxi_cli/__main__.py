import argparse
from contextlib import ExitStack
from dataclasses import asdict, dataclass
import json
import os
from pathlib import Path
import re
import sys


PACKAGE_DIR = Path(__file__).resolve().parent
REPO_URL = "https://github.com/HuanMoovo/fuxi"
CHECKLIST = "stage-checklist.md"
CONTRACT = "learning-contract.md"
CORE_STAGES = range(1, 11)
STAGE_HEADING = re.compile(r"第\s+(\d+)\s+阶\s*·\s*(.+)")
TASK_BOX = re.compile(r"^ {0,3}[-+*][ \t]+\[([ xX])\][ \t]+\S", re.MULTILINE)
CODE_FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")


def content_dir(name: str, source: str) -> Path:
    packaged = PACKAGE_DIR / name
    return packaged if packaged.is_dir() else PACKAGE_DIR.parent / source


def stage_files() -> list[Path]:
    stages = sorted(content_dir("stages", "docs/stages").glob("[0-9][0-9]-*.md"))
    if not stages:
        raise ValueError("找不到伏羲阶段指南。请检查安装是否完整。")
    return stages


def list_stages(_args: argparse.Namespace) -> None:
    for path in stage_files():
        number, slug = path.stem.split("-", 1)
        with path.open(encoding="utf-8") as guide:
            heading = guide.readline().partition("<br")[0].strip()
        title = heading.partition("·")[2].strip()
        print(f"{number}  {slug:<10}  {title}")


def show_stage(args: argparse.Namespace) -> None:
    selector = args.stage.strip().lower()
    for path in stage_files():
        number, slug = path.stem.split("-", 1)
        if selector in (number, number.lstrip("0"), slug):
            sys.stdout.write(path.read_text(encoding="utf-8"))
            return
    args.command_parser.error(f"未知阶段 {args.stage!r}，可用 fuxi stages 查看阶段编号和名称。")


def init_project(args: argparse.Namespace) -> None:
    destination = args.directory.expanduser()
    topic = None
    if args.topic is not None:
        topic = args.topic.strip()
        if not topic or len(topic.splitlines()) != 1:
            raise ValueError("学习主题须为单行非空文本。")
        topic = re.sub(r"([\\`*_{}\[\]()<>#!|])", r"\\\1", topic)

    templates = {}
    for path in sorted(content_dir("templates", "templates").glob("*.md")):
        contents = path.read_text(encoding="utf-8")
        contents = contents.replace("(../docs/README.md)", f"({REPO_URL}/blob/main/docs/README.md)")
        contents = contents.replace("(../README.md)", f"({REPO_URL})")
        if path.name == CONTRACT and topic:
            field = "**领域**：________"
            if field not in contents:
                raise ValueError(f"{CONTRACT} 缺少学习领域字段。")
            contents = contents.replace(field, f"**领域**：{topic}", 1)
        templates[path.name] = (
            contents.rstrip() + "\n\n"
            f"模板来源：[伏羲框架]({REPO_URL})（HuanMoovo，[CC BY 4.0]"
            "(https://creativecommons.org/licenses/by/4.0/)）。此为 CLI 导出版。\n"
        )
    if CONTRACT not in templates or CHECKLIST not in templates:
        raise ValueError("找不到伏羲学习模板。请检查安装是否完整。")

    try:
        destination.mkdir()
    except FileExistsError:
        raise ValueError(f"目标已存在，请指定一个新目录：{destination}") from None

    with ExitStack() as rollback:
        rollback.callback(destination.rmdir)
        for name, contents in templates.items():
            path = destination / name
            with path.open("x", encoding="utf-8", newline="\n") as output:
                rollback.callback(path.unlink, missing_ok=True)
                output.write(contents)
        rollback.pop_all()
    print(f"已在 {destination} 创建 {len(templates)} 份学习模板。先填写 {CONTRACT}。")


@dataclass(frozen=True)
class StageProgress:
    number: int
    title: str
    checked: int
    total: int


def without_code_examples(text: str) -> str:
    lines = []
    opening = None
    for line in text.splitlines():
        fence = CODE_FENCE.match(line)
        if opening is None:
            if fence:
                opening = fence[1]
            else:
                lines.append(line)
        elif fence and fence[1].startswith(opening) and not fence[2].strip():
            opening = None
    return "\n".join(lines)


def read_progress(checklist: Path) -> list[StageProgress]:
    try:
        text = checklist.read_text(encoding="utf-8-sig")
    except FileNotFoundError:
        raise ValueError(f"未找到过关清单 {checklist}。请先运行 fuxi init。") from None

    stages: dict[int, StageProgress] = {}
    sections = re.split(r"^##[ \t]+", without_code_examples(text), flags=re.MULTILINE)
    for section in sections[1:]:
        heading, _, body = section.partition("\n")
        match = STAGE_HEADING.fullmatch(heading.strip())
        if match is None:
            continue
        number = int(match[1])
        if number not in CORE_STAGES:
            continue
        if number in stages:
            raise ValueError(f"过关清单重复出现第 {number} 阶。")
        tasks = TASK_BOX.findall(body)
        if not tasks:
            raise ValueError(f"过关清单第 {number} 阶没有可统计的任务。")
        stages[number] = StageProgress(number, match[2], len(tasks) - tasks.count(" "), len(tasks))

    missing = [str(number) for number in CORE_STAGES if number not in stages]
    if missing:
        raise ValueError(f"过关清单缺少阶段 {', '.join(missing)}。请保留模板的阶段标题。")
    return [stages[number] for number in CORE_STAGES]


def show_status(args: argparse.Namespace) -> None:
    stages = read_progress(args.directory.expanduser() / CHECKLIST)
    checked = sum(stage.checked for stage in stages)
    total = sum(stage.total for stage in stages)
    if args.json:
        print(json.dumps({
            "checked": checked,
            "total": total,
            "stages": [asdict(stage) for stage in stages],
        }, ensure_ascii=False, indent=2))
        return
    for stage in stages:
        print(f"{stage.number:02}  {stage.title}  {stage.checked}/{stage.total}")
    print(f"合计  {checked}/{total} 项已勾选")


def main(argv: list[str] | None = None) -> int:
    if sys.platform == "win32" and not os.environ.get("PYTHONIOENCODING"):
        for stream in (sys.stdout, sys.stderr):
            if hasattr(stream, "reconfigure"):
                stream.reconfigure(encoding="utf-8")

    parser = argparse.ArgumentParser(prog="fuxi", description="伏羲学习框架命令行工具")
    commands = parser.add_subparsers(dest="command", required=True)

    init = commands.add_parser("init", help="新建学习目录并导出模板")
    init.add_argument("directory", type=Path, metavar="目录", help="尚不存在的学习目录")
    init.add_argument("--topic", metavar="主题", help="预填学习契约的领域字段")
    init.set_defaults(handler=init_project)

    stages = commands.add_parser("stages", help="列出十阶与第 11 阶拓界")
    stages.set_defaults(handler=list_stages)

    stage = commands.add_parser("stage", help="输出指定阶段指南的 Markdown")
    stage.add_argument("stage", metavar="阶段", help="阶段编号或英文名称，例如 2 或 map")
    stage.set_defaults(handler=show_stage, command_parser=stage)

    status = commands.add_parser(
        "status",
        help="统计过关清单的勾选进度",
        description="统计 stage-checklist.md 中十阶的顶层勾选项。",
    )
    status.add_argument(
        "directory", type=Path, nargs="?", default=Path("."), metavar="目录",
        help="学习目录，默认为当前目录",
    )
    status.add_argument("--json", action="store_true", help="以 JSON 格式输出")
    status.set_defaults(handler=show_status)

    args = parser.parse_args(argv)
    try:
        args.handler(args)
    except (OSError, ValueError) as error:
        print(f"fuxi: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
