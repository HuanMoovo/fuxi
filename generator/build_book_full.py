# -*- coding: utf-8 -*-
"""构建《伏羲框架 · 万物皆可学（完整版）》PDF。
阶段：--stage=prep（书稿 HTML + mermaid 渲染）/ pdf（Chrome 打印 + pypdf 页码书签）/ all
运行：venv python generator/build_book_full.py --stage=prep
"""
import os, re, sys, json, base64, hashlib, subprocess, urllib.request
from concurrent.futures import ThreadPoolExecutor

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHROME = r"C:/Program Files/Google/Chrome/Application/chrome.exe"
OUT_HTML = os.path.join(ROOT, "docs", "book", "fuxi-handbook-full-zh.html")
RAW_PDF = os.path.join(ROOT, "docs", "pdf", "_full_raw.pdf")
OUT_PDF = os.path.join(ROOT, "docs", "pdf", "fuxi-handbook-full-zh.pdf")
MMD_DIR = os.path.join(ROOT, "docs", "book", "full-assets", "mmd")
PROXIES = {"https": "http://127.0.0.1:7897", "http": "http://127.0.0.1:7897"}

PARTS = [
 ("第一部分 · 为什么与深度剖析", "世界的三重不对称，与四个被误解的学习真相", [
   ("为什么需要伏羲框架", "docs/why.md"),
   ("深度剖析① · 方法碎片化", "docs/why/fragmentation.md"),
   ("深度剖析② · 伪科学横行", "docs/why/pseudoscience.md"),
   ("深度剖析③ · 爽感陷阱", "docs/why/fluency-trap.md"),
   ("深度剖析④ · AI 时代的新风险", "docs/why/ai-risks.md"),
   ("姐妹篇（上）· 理论框架全景（53 个）", "docs/why/theories.md"),
   ("姐妹篇（下）· 学习方法全景（50+）", "docs/why/methods.md"),
 ]),
 ("第二部分 · 十阶时间线详解", "从「想学」到「学成」的十一个阶段", [
   ("第 1 阶 · 立志：一页学习契约", "docs/stages/01-orient.md"),
   ("第 2 阶 · 建图：一页领域地图", "docs/stages/02-map.md"),
   ("第 3 阶 · 拆解：原子清单与练习", "docs/stages/03-decompose.md"),
   ("第 4 阶 · 编码：最简解释与卡片", "docs/stages/04-encode.md"),
   ("第 5 阶 · 检索：合上书先回忆", "docs/stages/05-retrieve.md"),
   ("第 6 阶 · 间隔：有序复习", "docs/stages/06-space.md"),
   ("第 7 阶 · 精练：能力边缘反复练", "docs/stages/07-drill.md"),
   ("第 8 阶 · 应用：干中学", "docs/stages/08-apply.md"),
   ("第 9 阶 · 教学：讲给别人听", "docs/stages/09-teach.md"),
   ("第 10 阶 · 维护：让系统长期运转", "docs/stages/10-maintain.md"),
   ("第 11 阶 · 拓界：知识边界之后", "docs/stages/11-expand.md"),
 ]),
 ("第三部分 · 拓界篇 · 五大赛道", "一个循环 · 五条赛道 · 五大理论支柱", [
   ("拓界 · 理论整合", "docs/expand/integration.md"),
   ("赛道 · 创业", "docs/expand/entrepreneurship.md"),
   ("赛道 · 人际", "docs/expand/relationships.md"),
   ("赛道 · 长寿", "docs/expand/longevity.md"),
   ("赛道 · 未来纪元", "docs/expand/futures.md"),
 ]),
 ("第四部分 · 误区全景", "24 条高频误区的证据裁决", [("学习误区辟谣库（24 条）", "docs/myths.md")]),
 ("第五部分 · 路线、FAQ 与工具", "怎么走、遇到问题怎么办、用什么工具", [
   ("路线与领域", "docs/paths.md"),
   ("常见问题 FAQ", "docs/faq.md"),
   ("开源工具链", "docs/tools.md"),
 ]),
 ("第六部分 · 模板与行动附录", "即取即用：契约 / 检视 / 错题 / 卡片 / 清单", [
   ("学习契约（模板）", "templates/learning-contract.md"),
   ("周检视（模板）", "templates/weekly-review.md"),
   ("错题日志（模板）", "templates/error-log.md"),
   ("卡片规则（模板）", "templates/card-rules.md"),
   ("十阶过关清单（模板）", "templates/stage-checklist.md"),
 ]),
 ("第七部分 · 证据与文献", "每一条主张都可核验（放于最末）", [
   ("证据底座（30 条结论）", "docs/evidence.md"),
   ("全量文献库（C01–C286）", "docs/references.md"),
 ]),
]

def strip_nav(t):
    t = re.sub(r"\n\n---\n\n\*\*导航\*\*：[^\n]*\n?$", "", t.rstrip())
    return t

def strip_first_h1(t):
    lines = t.split("\n")
    for i, ln in enumerate(lines):
        if ln.startswith("# "):
            lines.pop(i); break
        if ln.strip() and not ln.startswith(("#", ">", "\ufeff")):
            break
    return "\n".join(lines)

def fix_img(src):
    m = re.match(r"https?://raw\.githubusercontent\.com/HuanMoovo/fuxi/main/(.+)$", src)
    if m:
        return os.path.relpath(os.path.join(ROOT, m.group(1)), os.path.join(ROOT, "docs", "book")).replace("\\", "/")
    if src.startswith("http"):
        return src
    return src

# ---------- mermaid ----------
def mmd_url(code, width=1400):
    b = base64.urlsafe_b64encode(json.dumps({"code": code, "mermaid": {"theme": "default"}}).encode()).decode()
    return "https://mermaid.ink/img/" + b + "?width=%d" % width

def fetch(url):
    for op in (urllib.request.build_opener(urllib.request.ProxyHandler(PROXIES)),
               urllib.request.build_opener()):
        try:
            with op.open(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=50) as r:
                if r.status == 200:
                    return r.read()
        except Exception:
            continue
    return None

def render_one(code):
    h = hashlib.sha1(code.encode()).hexdigest()[:16]
    fp = os.path.join(MMD_DIR, h + ".jpg")
    if os.path.exists(fp) and os.path.getsize(fp) > 500:
        return (h, True)
    data = fetch(mmd_url(code)) or fetch(mmd_url(code, 1000))
    if data and len(data) > 500:
        open(fp, "wb").write(data)
        return (h, True)
    return (h, False)

# ---------- converter ----------
def inline(s, pool):
    s = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"&lt;(https?://[^\s&]+)&gt;", r"\1", s)
    def link(m):
        txt, url = m.group(1), m.group(2)
        if url.endswith(".md"):
            return txt
        if url.startswith("http"):
            return "%s（%s）" % (txt, url)
        return txt
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", link, s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    return s

def convert(text, pool, mmd_map, hprefix):
    lines = strip_first_h1(strip_nav(text)).split("\n")
    out = []
    i = 0
    while i < len(lines):
        ln = lines[i].rstrip()
        fence = re.match(r"^```(\w*)\s*$", ln)
        if fence:
            lang = fence.group(1); buf = []; i += 1
            while i < len(lines) and not lines[i].startswith("```"):
                buf.append(lines[i]); i += 1
            i += 1
            code = "\n".join(buf)
            if lang == "mermaid":
                h = hashlib.sha1(code.encode()).hexdigest()[:16]
                if mmd_map.get(h):
                    out.append('<figure class="mmd"><img src="full-assets/mmd/%s.jpg" alt="流程图"><figcaption>流程图</figcaption></figure>' % h)
                else:
                    out.append('<div class="mmdfb">［流程图 · 见在线版或 PDF 目录附注］</div>')
            else:
                out.append("<pre>%s</pre>" % code.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))
            continue
        m = re.match(r"^(#{1,4}) (.+)$", ln)
        if m:
            lvl = min(len(m.group(1)) + 1, 4)
            out.append("<h%d>%s</h%d>" % (lvl, inline(m.group(2), pool), lvl))
            i += 1; continue
        if ln.startswith("|") and i + 1 < len(lines) and re.match(r"^\|[-| :]+\|", lines[i+1]):
            hdr = [c.strip() for c in ln.strip("|").split("|")]
            rows = []; i += 2
            while i < len(lines) and lines[i].startswith("|"):
                rows.append([c.strip() for c in lines[i].strip("|").split("|")]); i += 1
            th = "".join("<th>%s</th>" % inline(c, pool) for c in hdr)
            trs = "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % inline(c, pool) for c in r) for r in rows)
            out.append("<table><thead><tr>%s</tr></thead><tbody>%s</tbody></table>" % (th, trs))
            continue
        if ln.startswith("> "):
            buf = []
            while i < len(lines) and lines[i].startswith("> "):
                buf.append(lines[i][2:]); i += 1
            out.append("<blockquote>%s</blockquote>" % "<br>".join(inline(b, pool) for b in buf))
            continue
        if re.match(r"^\s*([-*]) ", ln):
            buf = []
            while i < len(lines) and re.match(r"^\s*([-*]) ", lines[i]):
                item = re.sub(r"^\s*[-*] ", "", lines[i])
                if item.startswith("[ ] "):
                    buf.append("<li class='todo'>☐ %s</li>" % inline(item[4:], pool))
                elif item.lower().startswith("[x] "):
                    buf.append("<li class='todo'>☑ %s</li>" % inline(item[4:], pool))
                else:
                    buf.append("<li>%s</li>" % inline(item, pool))
                i += 1
            out.append("<ul>%s</ul>" % "".join(buf))
            continue
        if re.match(r"^\s*\d+\. ", ln):
            buf = []
            while i < len(lines) and re.match(r"^\s*\d+\. ", lines[i]):
                buf.append("<li>%s</li>" % inline(re.sub(r"^\s*\d+\. ", "", lines[i]), pool)); i += 1
            out.append("<ol>%s</ol>" % "".join(buf))
            continue
        if re.match(r"^-{3,}\s*$", ln):
            out.append("<hr>"); i += 1; continue
        mi = re.match(r"^!\[([^\]]*)\]\(([^)]+)\)$", ln)
        if mi:
            src = fix_img(mi.group(2)); cap = mi.group(1)
            out.append('<figure><img src="%s" alt="%s">%s</figure>' % (src, cap, ("<figcaption>%s</figcaption>" % inline(cap, pool)) if cap else ""))
            i += 1; continue
        if ln.strip() == "":
            i += 1; continue
        out.append("<p>%s</p>" % inline(ln, pool))
        i += 1
    return "".join(out)

CSS = """
@page { size: A4; margin: 17mm 15mm 18mm; }
* { box-sizing: border-box; }
body { font-family: "Microsoft YaHei","PingFang SC",sans-serif; font-size: 11.5pt; color: #2B2B2B; line-height: 1.9; margin: 0; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
.cover { height: 246mm; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; page-break-after: always; border: 6px double #6E4E9E; border-radius: 6px; padding: 20mm; }
.cover .logo { width: 100px; height: 100px; margin-bottom: 10mm; }
.cover h1 { font-size: 31pt; letter-spacing: 2px; border: none; margin: 6mm 0 2mm; color: #3A3355; }
.cover .sub { font-size: 14pt; color: #6E4E9E; letter-spacing: 5px; }
.cover .meta { margin-top: 14mm; font-size: 10pt; color: #6B7280; line-height: 2.1; }
.partpage { page-break-before: always; height: 232mm; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; border: 5px double #6E4E9E; border-radius: 6px; }
.partpage .pn { font-size: 12pt; letter-spacing: 6px; color: #8A8F7A; }
.partpage .pt { font-size: 28pt; color: #3A3355; margin: 9mm 0 5mm; font-family: "KaiTi","Microsoft YaHei",serif; }
.partpage .pd { font-size: 11.5pt; color: #6B7280; }
h1 { font-family: "KaiTi","Microsoft YaHei",serif; font-size: 21pt; color: #3A3355; margin: 0 0 5mm; padding-bottom: 2mm; border-bottom: 2.5px solid #C9B8E8; page-break-before: always; }
h2 { font-size: 14pt; color: #4A4166; border-left: 5px solid #6E4E9E; padding-left: 3mm; margin: 7mm 0 3mm; page-break-after: avoid; }
h3 { font-size: 12pt; color: #4A4166; margin: 5mm 0 2mm; page-break-after: avoid; }
h4 { font-size: 11pt; color: #4A4166; margin: 4mm 0 2mm; }
p { margin: 2mm 0; text-align: justify; }
table { width: 100%; border-collapse: collapse; margin: 3mm 0 5mm; font-size: 9.6pt; }
th { background: #F5EEDD; color: #3A3355; border: 1px solid #D8CFC0; padding: 1.5mm 2mm; text-align: left; }
td { border: 1px solid #D8CFC0; padding: 1.5mm 2mm; vertical-align: top; }
tr { page-break-inside: avoid; }
blockquote { background: #FBF7EC; border-left: 4px solid #C97A3D; margin: 3mm 0; padding: 2.5mm 4mm; color: #5A5245; font-size: 10.5pt; border-radius: 0 4px 4px 0; }
ul, ol { margin: 2mm 0 3mm; padding-left: 6mm; }
li { margin: 1mm 0; }
li.todo { list-style: none; margin-left: -4mm; }
hr { border: none; border-top: 1.5px dashed #C9B8E8; margin: 5mm 0; }
code { background: #F1EDE2; padding: 0.5mm 1.5mm; border-radius: 3px; font-size: 9.5pt; }
pre { background: #F1EDE2; padding: 3mm; border-radius: 4px; font-size: 9.5pt; white-space: pre-wrap; }
figure { margin: 4mm 0; text-align: center; page-break-inside: avoid; }
figure img { max-width: 100%; max-height: 100mm; }
figure.mmd img { max-height: 130mm; border: 1px solid #E5DECE; border-radius: 4px; padding: 1.5mm; }
figcaption { font-size: 8.5pt; color: #8A8F7A; margin-top: 1.5mm; }
.toc { page-break-after: always; }
.toc-h { border-left: none; text-align: center; font-size: 19pt; color: #3A3355; border-bottom: 2.5px solid #C9B8E8; padding-bottom: 3mm; }
.toc-l0 { font-weight: 700; font-size: 12.5pt; color: #3A3355; margin: 4mm 0 1.5mm; }
.toc-l1 { font-size: 10.5pt; padding-left: 5mm; margin: 1.2mm 0; color: #444; }
strong { color: #3A3355; }
a { color: #4A5F8F; }
.mmdfb { border: 1px dashed #C9B8E8; padding: 2mm; color: #8A8F7A; font-size: 9pt; text-align: center; }
.note { background: #FBF7EC; border: 1px solid #E5DECE; border-radius: 6px; padding: 4mm 5mm; font-size: 10pt; color: #5A5245; }
"""

def build_html():
    pool = {}
    all_md = {}
    mmd_codes = []
    for pt, pd, chapters in PARTS:
        for title, rel in chapters:
            t = open(os.path.join(ROOT, rel), encoding="utf-8").read()
            all_md[rel] = t
            for m in re.finditer(r"```mermaid\n(.*?)```", t, re.S):
                mmd_codes.append(m.group(1))
    os.makedirs(MMD_DIR, exist_ok=True)
    mmd_map = {}
    with ThreadPoolExecutor(6) as ex:
        for (h, ok) in ex.map(render_one, mmd_codes):
            mmd_map[h] = ok
    print("MMD: %d blocks, %d rendered ok, %d failed" % (len(mmd_codes), sum(1 for v in mmd_map.values() if v), sum(1 for v in mmd_map.values() if not v)))

    toc = ['<div class="toc"><h2 class="toc-h" style="border-left:none">目录</h2>']
    body = []
    for pt, pd_, chapters in PARTS:
        toc.append('<div class="toc-l0">%s</div>' % pt)
        for title, rel in chapters:
            toc.append('<div class="toc-l1">%s</div>' % title)
        body.append('<div class="partpage"><div class="pn">PART</div><div class="pt">%s</div><div class="pd">%s</div></div>' % (pt, pd_))
        for title, rel in chapters:
            body.append("<h1>%s</h1>" % title)
            body.append(convert(all_md[rel], pool, mmd_map, "c"))
    toc.append("</div>")
    cover = ('<div class="cover"><img class="logo" src="../assets/fuxi-logo.svg" alt="伏羲框架">'
             '<h1>伏羲框架 · 万物皆可学</h1><div class="sub">完整版 · The Complete Edition</div>'
             '<div class="meta">十阶时间线 × 证据分级（A/B/C/D）× 开源工具链<br>'
             '含：深度剖析 · 理论/方法全景 · 十阶详解 · 拓界五赛道 · 误区 24 条 · 全量文献 C01–C286 · 模板附录<br>'
             '在线版：https://HuanMoovo.github.io/fuxi/<br>'
             '许可：文档 CC BY 4.0 · 代码 MIT ｜ 生成器：generator/build_book_full.py</div></div>')
    note = ('<div class="note"><b>关于本完整版</b><br>'
            '本册收录：为什么与四篇深度剖析、理论框架全景（53）与方法全景（50+）、十阶详解（11 篇）、拓界篇（整合 + 五大赛道）、'
            '误区库（24 条）、证据底座与全量文献库（C01–C286）、路线 / FAQ / 工具链，以及全部可打印模板。<br>'
            '未收录（见在线版）：学习友链目录（2600+ 链接库）、人生时间线目录与站点交互界面。<br>'
            '全部文献逐条核验；页码与书签由 pypdf 自动生成。错误修正记录见 CHANGELOG。</div><div style="page-break-after: always"></div>')
    doc = "<!DOCTYPE html><html lang='zh-CN'><head><meta charset='utf-8'><title>伏羲框架 · 万物皆可学（完整版）</title><style>%s</style></head><body>%s%s%s%s</body></html>" % (CSS, cover, note, "".join(toc), "".join(body))
    open(OUT_HTML, "w", encoding="utf-8").write(doc)
    print("HTML:", OUT_HTML, len(doc))

def build_pdf():
    os.makedirs(os.path.dirname(RAW_PDF), exist_ok=True)
    r = subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer", "--virtual-time-budget=30000",
                        "--allow-file-access-from-files", "--print-to-pdf=" + RAW_PDF, "file:///" + OUT_HTML.replace("\\", "/")],
                       capture_output=True, text=True)
    print("chrome rc:", r.returncode, "| raw:", os.path.getsize(RAW_PDF) if os.path.exists(RAW_PDF) else "MISSING")
    if r.returncode != 0 or not os.path.exists(RAW_PDF):
        return 1
    import pypdf
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import A4
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.cidfonts import UnicodeCIDFont
    pdfmetrics.registerFont(UnicodeCIDFont("STSong-Light"))
    reader = pypdf.PdfReader(RAW_PDF)
    N = len(reader.pages)
    norm = lambda s: re.sub(r"\s+", "", s or "")
    texts = [norm(pg.extract_text()) for pg in reader.pages]
    # 页码 overlay
    ov = os.path.join(os.path.dirname(RAW_PDF), "_ov.pdf")
    c = canvas.Canvas(ov, pagesize=A4)
    for i in range(N):
        c.setFont("STSong-Light", 8)
        c.setFillColorRGB(0.45, 0.47, 0.45)
        c.drawCentredString(A4[0] / 2, 11 * 2.83465, "— %d —" % (i + 1))
        c.drawRightString(A4[0] - 42, 11 * 2.83465, "伏羲框架 · 完整版")
        c.showPage()
    c.save()
    ovr = pypdf.PdfReader(ov)
    w = pypdf.PdfWriter()
    for i in range(N):
        pg = reader.pages[i]
        pg.merge_page(ovr.pages[i])
        w.add_page(pg)
    def find(title, start=0):
        key = norm(title)
        for i in range(start, N):
            if key and key in texts[i]:
                return i
        short = norm(title.split("·")[-1])
        for i in range(start, N):
            if short and short in texts[i]:
                return i
        return None
    pos = 0
    for pt, _pd, chapters in PARTS:
        pi = find(pt, pos) or pos
        part_item = w.add_outline_item(pt, pi)
        pos = pi
        for title, _rel in chapters:
            ci = find(title, pos) or pos
            w.add_outline_item(title, ci, parent=part_item)
            pos = ci
    w.add_metadata({"/Title": "伏羲框架 · 万物皆可学（完整版）", "/Author": "HuanMoovo",
                    "/Subject": "十阶时间线 x 证据分级 x 开源工具链", "/Keywords": "learning, evidence-based, Fuxi Framework"})
    with open(OUT_PDF, "wb") as f2:
        w.write(f2)
    print("PDF:", OUT_PDF, os.path.getsize(OUT_PDF), "| pages:", N)

if __name__ == "__main__":
    stage = "all"
    for a in sys.argv[1:]:
        if a.startswith("--stage="):
            stage = a.split("=", 1)[1]
    if stage in ("prep", "all"):
        build_html()
    if stage in ("pdf", "all"):
        build_pdf()
