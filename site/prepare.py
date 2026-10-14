# -*- coding: utf-8 -*-
"""汇总仓库内容到 site/build（mkdocs 的 docs_dir，构建产物、已 gitignore）。

用法：python site/prepare.py

映射规则
- docs/**.md                -> 同路径（README.md -> index.md；docs/book/ 仅收精读手册精简版）
- docs/assets/**            -> assets/**
- templates/*.md            -> doc-templates/*.md（MkDocs 硬编码排除根级 templates/，故改名映射）
- README.md / CHANGELOG.md / CONTRIBUTING.md -> repo-readme.md / changelog.md / contributing.md

链接改写
- 相对链接按「原文件位置」解析 → 映射到 staged 路径 → 重算相对路径（保留 #锚点）；
- 无映射目标（LICENSE、generator/、book 全量稿等）→ 仓库 GitHub URL；
- docs/index.html（在线主页 SPA）→ 站点 URL。

校验
- staged 的全部 .md 必须与 mkdocs.yml 的 nav 一一覆盖，否则退出码非 0。
"""
import os
import re
import sys
import shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUILD = os.path.join(ROOT, "site", "build")
GH_BLOB = "https://github.com/HuanMoovo/fuxi/blob/main/"
GH_TREE = "https://github.com/HuanMoovo/fuxi/tree/main/"
SITE_URL = "https://HuanMoovo.github.io/fuxi/"
INCLUDE_BOOK = {"docs/book/fuxi-handbook-lite-zh.md"}


def staged_target(rel):
    """仓库相对路径 -> staged 相对路径；None 表示不收录。"""
    rel = rel.replace("\\", "/")
    if rel == "README.md":
        return "repo-readme.md"
    if rel == "CHANGELOG.md":
        return "changelog.md"
    if rel == "CONTRIBUTING.md":
        return "contributing.md"
    if rel.startswith("docs/assets/"):
        return "assets/" + rel[len("docs/assets/"):]
    if rel.startswith("docs/"):
        sub = rel[len("docs/"):]
        if sub.startswith("book/"):
            return "book/" + os.path.basename(sub) if rel in INCLUDE_BOOK else None
        if sub.endswith(".md"):
            if sub == "README.md":
                return "index.md"
            if sub.endswith("/README.md"):
                return sub[: -len("README.md")] + "index.md"
            return sub
    if rel.startswith("templates/") and rel.endswith(".md"):
        return "doc-templates/" + rel[len("templates/"):]
    return None


def collect_sources():
    out = []
    docs = os.path.join(ROOT, "docs")
    for dirpath, dirnames, filenames in os.walk(docs):
        dirnames[:] = [d for d in dirnames if d not in (".git",)]
        for fn in filenames:
            src = os.path.join(dirpath, fn)
            rel = os.path.relpath(src, ROOT).replace("\\", "/")
            if rel.startswith("docs/assets/"):
                out.append((rel, staged_target(rel)))
                continue
            if not fn.endswith(".md"):
                continue
            dest = staged_target(rel)
            if dest:
                out.append((rel, dest))
    for rel in ("README.md", "CHANGELOG.md", "CONTRIBUTING.md"):
        out.append((rel, staged_target(rel)))
    tdir = os.path.join(ROOT, "templates")
    if os.path.isdir(tdir):
        for fn in sorted(os.listdir(tdir)):
            if fn.endswith(".md"):
                out.append(("templates/" + fn, "doc-templates/" + fn))
    return out


LINK_RE = re.compile(r"\]\(\s*(<[^>]+>|[^)\s]+)(\s+\"[^\"]*\")?\s*\)")
# 原始 HTML 属性（<img src>、<a href>）也要改写，否则书里会 404
ATTR_RE = re.compile(r"""(?P<pre>\b(?:src|href)\s*=\s*)(?P<q>["'])(?P<url>[^"']+)(?P=q)""")


def page_url_dir(dest):
    """staged .md 路径 -> mkdocs 页面 URL 目录（use_directory_urls=true 时）。"""
    d = dest[:-3] if dest.endswith(".md") else dest
    if os.path.basename(d) == "index":
        d = os.path.dirname(d)
    return d.strip("/")


def rewrite_links(text, src_rel):
    src_dir = os.path.dirname(src_rel)
    staged_src = staged_target(src_rel)
    staged_dir = os.path.dirname(staged_src)
    stats = {"mapped": 0, "fallback": 0}
    fallen = []

    def resolve(t):
        """仓库相对目标 -> staged 目标（相对路径）或 GitHub 兜底；None 表示不改写。"""
        if re.match(r"^(https?:|mailto:|#|data:|tel:|//)", t):
            return None
        path, sep, frag = t.partition("#")
        if not path:
            return None
        is_dir = path.endswith("/")
        resolved = os.path.normpath(os.path.join(src_dir, path)).replace("\\", "/")
        if resolved == "docs/index.html":
            new = SITE_URL
        else:
            dest = staged_target(resolved)
            if dest:
                new = os.path.relpath(dest, staged_dir if staged_dir else ".").replace("\\", "/")
                stats["mapped"] += 1
            else:
                base = GH_TREE if is_dir else GH_BLOB
                new = base + resolved.rstrip("/")
                stats["fallback"] += 1
                fallen.append(t)
        if sep and frag:
            new += "#" + frag
        return new

    def repl(m):
        target, title = m.group(1), (m.group(2) or "")
        t = target[1:-1] if target.startswith("<") and target.endswith(">") else target
        new = resolve(t)
        if new is None:
            return m.group(0)
        return "](" + new + title + ")"

    out = LINK_RE.sub(repl, text)

    pdir = page_url_dir(staged_src)

    def resolve_attr(t):
        """原始 HTML 属性：mkdocs 不换算原始标签的相对路径，直接产出相对页面 URL 的最终路径。"""
        if re.match(r"^(https?:|mailto:|#|data:|tel:|//)", t):
            return None
        path, sep, frag = t.partition("#")
        if not path:
            return None
        is_dir = path.endswith("/")
        resolved = os.path.normpath(os.path.join(src_dir, path)).replace("\\", "/")
        if resolved == "docs/index.html":
            new = SITE_URL
        else:
            dest = staged_target(resolved)
            if dest is None:
                base = GH_TREE if is_dir else GH_BLOB
                new = base + resolved.rstrip("/")
                stats["fallback"] += 1
                fallen.append(t)
            elif dest.endswith(".md"):
                u = dest[:-3]
                if os.path.basename(u) == "index":
                    u = os.path.dirname(u)
                rel = os.path.relpath(u or ".", pdir or ".").replace("\\", "/")
                new = "./" if rel == "." else rel + "/"
                stats["mapped"] += 1
            else:
                new = os.path.relpath(dest, pdir or ".").replace("\\", "/")
                stats["mapped"] += 1
        if sep and frag:
            new += "#" + frag
        return new

    def attr_repl(m):
        new = resolve_attr(m.group("url"))
        if new is None:
            return m.group(0)
        return m.group("pre") + m.group("q") + new + m.group("q")

    out = ATTR_RE.sub(attr_repl, out)
    return out, stats, fallen


def book_transform(text):
    """repo-readme.md 的书籍版微调（只改 staged 副本，源 README 保持不动）。"""
    n = 0
    if '<div align="center">' in text:
        # 启用 md_in_html：否则整块 hero（标题/加粗/链接行）以源码形式裸露
        text = text.replace('<div align="center">', '<div align="center" markdown="1">', 1)
        n += 1
    if "[docs/README.md](index.md)" in text:
        text = text.replace("[docs/README.md](index.md)", "[文档总目录](index.md)")
        n += 1
    print("  书籍版微调（项目主页）：%d 处" % n)
    return text


def main():
    sources = collect_sources()
    if os.path.isdir(BUILD):
        shutil.rmtree(BUILD)
    os.makedirs(BUILD, exist_ok=True)
    md_written = []
    total = {"mapped": 0, "fallback": 0}
    fallbacks = []
    for rel, dest in sources:
        src = os.path.join(ROOT, rel)
        dst = os.path.join(BUILD, dest)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        if rel.startswith("docs/assets/"):
            shutil.copy2(src, dst)
            continue
        text = open(src, encoding="utf-8").read()
        text, stats, fallen = rewrite_links(text, rel)
        if dest == "repo-readme.md":
            text = book_transform(text)
        total["mapped"] += stats["mapped"]
        total["fallback"] += stats["fallback"]
        fallbacks += fallen
        open(dst, "w", encoding="utf-8").write(text)
        md_written.append(dest)
    # 样式目录（extra_css 指向 staged 内路径）
    styles_src = os.path.join(ROOT, "site", "styles")
    if os.path.isdir(styles_src):
        shutil.copytree(styles_src, os.path.join(BUILD, "styles"), dirs_exist_ok=True)
    print("staged md: %d | 链接映射 %d 处 | GitHub 兜底 %d 处" % (len(md_written), total["mapped"], total["fallback"]))
    uniq = sorted(set(fallbacks))
    for u in uniq[:40]:
        print("  fallback:", u)
    if len(uniq) > 40:
        print("  ... 另有 %d 种" % (len(uniq) - 40))

    # nav 覆盖校验（用 mkdocs 自带的 YAML 加载器，支持 !!python/... 标签）
    cfg_path = os.path.join(ROOT, "mkdocs.yml")
    try:
        from mkdocs.utils import yaml_load
        cfg = yaml_load(open(cfg_path, encoding="utf-8"))
    except ImportError:
        from mkdocs.config import load_config
        cfg = load_config(config_file=cfg_path)
    nav_paths = []

    def walk(node):
        if isinstance(node, str):
            if node.endswith(".md"):
                nav_paths.append(node)
        elif isinstance(node, dict):
            for v in node.values():
                walk(v)
        elif isinstance(node, list):
            for v in node:
                walk(v)

    walk(cfg.get("nav") or [])
    staged_set = set(md_written)
    nav_set = set(nav_paths)
    missing = sorted(staged_set - nav_set)
    extra = sorted(nav_set - staged_set)
    if missing:
        print("!! 未进 nav 的文件:", missing)
    if extra:
        print("!! nav 指向不存在的文件:", extra)
    if missing or extra:
        return 1
    print("nav 覆盖校验通过：%d 个页面全部挂号" % len(staged_set))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
