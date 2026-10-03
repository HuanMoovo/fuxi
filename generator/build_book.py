# -*- coding: utf-8 -*-
"""构建《伏羲框架 · 精读手册（精简版）》PDF。
用法：python generator/build_book.py
流程：book md -> 打印版 HTML（笔记本风）-> headless Chrome --print-to-pdf
"""
import os, re, subprocess, html as _html, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MD = os.path.join(ROOT, "docs", "book", "fuxi-handbook-lite-zh.md")
OUT_HTML = os.path.join(ROOT, "docs", "book", "fuxi-handbook-lite-zh.html")
OUT_PDF = os.path.join(ROOT, "docs", "pdf", "fuxi-handbook-lite-zh.pdf")
CHROME = r"C:/Program Files/Google/Chrome/Application/chrome.exe"

def esc(s):
    return _html.escape(s, quote=False)

def inline(s):
    s = esc(s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\1（\2）", s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    return s

def convert(md):
    lines = md.split("\n")
    out, toc, i = [], [], 0
    list_buf, list_tag = [], None
    def flush_list():
        nonlocal list_buf, list_tag
        if list_buf:
            out.append("<%s>%s</%s>" % (list_tag, "".join("<li>%s</li>" % x for x in list_buf), list_tag))
            list_buf, list_tag = [], None
    while i < len(lines):
        ln = lines[i].rstrip()
        if list_buf and not re.match(r"^\s*([-*]|\d+\.) ", ln):
            flush_list()
        m = re.match(r"^(#{1,3}) (.+)$", ln)
        if m:
            lvl, txt = len(m.group(1)), m.group(2)
            if lvl == 1 and txt == "目录":
                out.append("__TOC__"); i += 1; continue
            cid = "h%d" % len(toc)
            if lvl == 1: toc.append((1, txt, cid)); out.append('<h1 id="%s">%s</h1>' % (cid, inline(txt)))
            elif lvl == 2: toc.append((2, txt, cid)); out.append('<h2 id="%s">%s</h2>' % (cid, inline(txt)))
            else: out.append("<h3>%s</h3>" % inline(txt))
            i += 1; continue
        if ln.startswith("|") and i + 1 < len(lines) and re.match(r"^\|[-| :]+\|", lines[i+1]):
            hdr = [c.strip() for c in ln.strip("|").split("|")]
            rows = []; i += 2
            while i < len(lines) and lines[i].startswith("|"):
                rows.append([c.strip() for c in lines[i].strip("|").split("|")]); i += 1
            th = "".join("<th>%s</th>" % inline(c) for c in hdr)
            trs = "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % inline(c) for c in r) for r in rows)
            out.append("<table><thead><tr>%s</tr></thead><tbody>%s</tbody></table>" % (th, trs))
            continue
        if ln.startswith("> "):
            buf = []
            while i < len(lines) and lines[i].startswith("> "):
                buf.append(lines[i][2:]); i += 1
            out.append("<blockquote>%s</blockquote>" % "<br>".join(inline(b) for b in buf))
            continue
        if re.match(r"^\s*([-*]) ", ln):
            if list_tag not in (None, "ul"): flush_list()
            list_tag = "ul"; list_buf.append(inline(re.sub(r"^\s*[-*] ", "", ln))); i += 1; continue
        if re.match(r"^\s*\d+\. ", ln):
            if list_tag not in (None, "ol"): flush_list()
            list_tag = "ol"; list_buf.append(inline(re.sub(r"^\s*\d+\. ", "", ln))); i += 1; continue
        if re.match(r"^-{3,}\s*$", ln):
            out.append("<hr>"); i += 1; continue
        mi = re.match(r"^!\[([^\]]*)\]\(([^)]+)\)$", ln)
        if mi:
            cap = mi.group(1)
            out.append('<figure><img src="%s" alt="%s">%s</figure>' % (mi.group(2), esc(cap), ("<figcaption>%s</figcaption>" % inline(cap)) if cap else ""))
            i += 1; continue
        if ln.strip() == "":
            i += 1; continue
        out.append("<p>%s</p>" % inline(ln))
        i += 1
    flush_list()
    toc_html = ["<div class='toc'><h2 class='toc-h'>目录</h2>"]
    for lvl, txt, cid in toc:
        toc_html.append("<div class='toc-l l%d'><a href='#%s'>%s</a></div>" % (lvl, cid, esc(txt)))
    toc_html.append("</div>")
    return "".join(out).replace("__TOC__", "".join(toc_html))

CSS = """
@page { size: A4; margin: 17mm 15mm 16mm; }
* { box-sizing: border-box; }
body { font-family: "Microsoft YaHei","PingFang SC",sans-serif; font-size: 10.5pt; color: #2B2B2B; line-height: 1.75; margin: 0; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
.cover { height: 247mm; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; page-break-after: always; border: 6px double #6E4E9E; border-radius: 6px; padding: 20mm; }
.cover .logo { width: 96px; height: 96px; margin-bottom: 10mm; }
.cover h1 { font-size: 30pt; letter-spacing: 2px; border: none; margin: 6mm 0 2mm; color: #3A3355; }
.cover .sub { font-size: 13pt; color: #6E4E9E; letter-spacing: 4px; }
.cover .meta { margin-top: 14mm; font-size: 9.5pt; color: #6B7280; line-height: 2.1; }
h1 { font-family: "KaiTi","Microsoft YaHei",serif; font-size: 21pt; color: #3A3355; margin: 0 0 5mm; padding-bottom: 2mm; border-bottom: 2.5px solid #C9B8E8; page-break-before: always; }
h1:first-of-type { page-break-before: avoid; }
h2 { font-size: 14pt; color: #4A4166; border-left: 5px solid #6E4E9E; padding-left: 3mm; margin: 7mm 0 3mm; page-break-after: avoid; }
h3 { font-size: 11.5pt; color: #4A4166; margin: 5mm 0 2mm; page-break-after: avoid; }
p { margin: 2mm 0; text-align: justify; }
table { width: 100%; border-collapse: collapse; margin: 3mm 0 5mm; font-size: 9pt; page-break-inside: auto; }
th { background: #F5EEDD; color: #3A3355; border: 1px solid #D8CFC0; padding: 1.6mm 2mm; text-align: left; }
td { border: 1px solid #D8CFC0; padding: 1.6mm 2mm; vertical-align: top; }
tr { page-break-inside: avoid; }
blockquote { background: #FBF7EC; border-left: 4px solid #C97A3D; margin: 3mm 0; padding: 2.5mm 4mm; color: #5A5245; font-size: 9.5pt; border-radius: 0 4px 4px 0; }
ul, ol { margin: 2mm 0 3mm; padding-left: 6mm; }
li { margin: 1mm 0; }
hr { border: none; border-top: 1.5px dashed #C9B8E8; margin: 5mm 0; }
code { background: #F1EDE2; padding: 0.5mm 1.5mm; border-radius: 3px; font-size: 9pt; }
figure { margin: 4mm 0; text-align: center; page-break-inside: avoid; }
figure img { max-width: 100%; max-height: 105mm; }
figcaption { font-size: 8.5pt; color: #8A8F7A; margin-top: 1.5mm; }
.toc { page-break-after: always; }
.toc-h { border-left: none; text-align: center; font-size: 18pt; color: #3A3355; border-bottom: 2.5px solid #C9B8E8; padding-bottom: 3mm; }
.toc-l { margin: 2.2mm 0; }
.toc-l a { color: #2B2B2B; text-decoration: none; }
.toc-l.l1 { font-weight: 700; font-size: 11.5pt; margin-top: 4mm; color: #4A4166; }
.toc-l.l2 { padding-left: 6mm; font-size: 10pt; color: #555; }
strong { color: #3A3355; }
a { color: #4A5F8F; }
"""

def main():
    md = open(MD, encoding="utf-8").read()
    md = md.split("\n", 1)[1]  # 去掉首行标题（封面单独生成）
    body = convert(md)
    cover = ('<div class="cover"><img class="logo" src="../assets/fuxi-logo.svg" alt="伏羲框架">'
             '<h1>伏羲框架 · 万物皆可学</h1><div class="sub">精读手册 · 精简版</div>'
             '<div class="meta">The Fuxi Framework — Everything Can Be Learned<br>'
             '十阶时间线 × 证据分级（A/B/C/D）× 开源工具链<br>'
             '在线版：https://HuanMoovo.github.io/fuxi/<br>'
             '许可：CC BY 4.0（文档）· MIT（代码）· 文献 C01–C286 全部可核验</div></div>')
    doc = "<!DOCTYPE html><html lang='zh-CN'><head><meta charset='utf-8'><title>伏羲框架 · 万物皆可学 —— 精读手册（精简版）</title><style>%s</style></head><body>%s%s</body></html>" % (CSS, cover, body)
    os.makedirs(os.path.dirname(OUT_HTML), exist_ok=True)
    open(OUT_HTML, "w", encoding="utf-8").write(doc)
    os.makedirs(os.path.dirname(OUT_PDF), exist_ok=True)
    r = subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer", "--virtual-time-budget=15000",
                        "--allow-file-access-from-files", "--print-to-pdf=" + OUT_PDF, "file:///" + OUT_HTML.replace("\\", "/")],
                       capture_output=True, text=True)
    ok = os.path.exists(OUT_PDF)
    print("PDF:", OUT_PDF, os.path.getsize(OUT_PDF) if ok else "MISSING")
    print("chrome rc:", r.returncode)
    return 0 if ok else 1

if __name__ == "__main__":
    raise SystemExit(main())
