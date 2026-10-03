#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""伏羲框架 SVG 图表生成器 v2。
运行: python generator/build_svgs.py
输出: docs/assets/fuxi-hero.svg / fuxi-engine.svg / fuxi-paths.svg / fuxi-spacing.svg / fuxi-loop.svg / fuxi-mark.svg
设计原则: 纯静态、无外部依赖、无 <style>、全内联属性（GitHub 渲染安全）。
v2 修复: 环形扇区角度 bug、英文与徽章重叠、证据分级固定配色、合流箭头、交错网格、表格对齐。
"""
import math, os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "docs", "assets")
os.makedirs(OUT, exist_ok=True)

FF = "'Segoe UI','Microsoft YaHei','PingFang SC','Noto Sans CJK SC',sans-serif"
BG = "#0B1020"
PANEL = "#121A2E"
PANEL2 = "#0E1526"
INK = "#E8ECF8"
MUT = "#93A0BF"
LINE = "#2A3550"
ERA = ["#8B5CF6", "#22D3EE", "#34D399", "#F59E0B", "#FB7185"]
GRADE = {"A": "#4ADE80", "B": "#60A5FA", "C": "#FBBF24", "D": "#F87171"}
ERA_NAMES = ["启程纪", "建构纪", "巩固纪", "淬炼纪", "传承纪"]
ERA_SUB = ["立志 · 建图", "拆解 · 编码", "检索 · 间隔", "精练 · 实战", "教学 · 维护"]

STAGES = [
    dict(num=1, name="立志", en="Orient", line="把「想学」变成可执行契约", chips=["学习契约", "执行意图"], grade="B", era=0),
    dict(num=2, name="建图", en="Map", line="先见森林：画出领域地图", chips=["知识树三进路", "门槛概念"], grade="B", era=0),
    dict(num=3, name="拆解", en="Decompose", line="拆到能一口吃下的原子", chips=["组块", "技能分解"], grade="B", era=1),
    dict(num=4, name="编码", en="Encode", line="用例子与解释织进旧知识", chips=["自我解释", "双重编码"], grade="A", era=1),
    dict(num=5, name="检索", en="Retrieve", line="合上书，从脑中取出来", chips=["测试效应", "自由回忆"], grade="A", era=2),
    dict(num=6, name="间隔", en="Space", line="在遗忘边缘科学复习", chips=["FSRS 调度", "交错练习"], grade="A", era=2),
    dict(num=7, name="精练", en="Drill", line="在能力边缘带反馈重复", chips=["刻意练习", "反馈环"], grade="B", era=3),
    dict(num=8, name="实战", en="Apply", line="直接做真事，缺啥补啥", chips=["干中学", "真实反馈"], grade="B", era=3),
    dict(num=9, name="教学", en="Teach", line="讲给别人听，迁移新场景", chips=["费曼技巧", "类比迁移"], grade="B", era=4),
    dict(num=10, name="维护", en="Maintain", line="低频保养，复利增值", chips=["最低剂量", "教学即维护"], grade="C", era=4),
]


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def tw(s, size):
    w = 0.0
    for ch in s:
        w += size * (1.0 if ord(ch) > 0x2E7F else 0.56)
    return w


def rect(x, y, w, h, fill, stroke=None, rx=14, sw=1.2, op=None):
    s = f'<rect x="{x:.0f}" y="{y:.0f}" width="{w:.0f}" height="{h:.0f}" rx="{rx}" fill="{fill}"'
    if stroke: s += f' stroke="{stroke}" stroke-width="{sw}"'
    if op is not None: s += f' opacity="{op}"'
    return s + "/>"


def text(x, y, s, size, fill, weight="400", anchor="start", op=None, ls=None):
    a = f'<text x="{x:.0f}" y="{y:.0f}" font-size="{size}" fill="{fill}" font-weight="{weight}" text-anchor="{anchor}"'
    if op is not None: a += f' opacity="{op}"'
    if ls: a += f' letter-spacing="{ls}"'
    return a + f' dominant-baseline="middle">{esc(s)}</text>'


def chip(x, y, s, size=16, fg=INK, bg="none", stroke=None, h=32, pad=12, weight="500"):
    w = tw(s, size) + pad * 2
    g = ""
    if bg != "none" or stroke:
        g += rect(x, y, w, h, bg if bg != "none" else "none", stroke, rx=h / 2, sw=1.1)
    g += text(x + w / 2, y + h / 2 + 1, s, size, fg, weight, "middle")
    return g, w


def polar(cx, cy, r, ang_deg):
    a = math.radians(ang_deg)
    return cx + r * math.cos(a), cy - r * math.sin(a)


def seg_path(mid, span, r_in, r_out, cx, cy):
    def P(r, ang):
        a = math.radians(ang)
        return (cx + r * math.cos(a), cy - r * math.sin(a))
    a0, a1 = mid - span / 2, mid + span / 2
    x0i, y0i = P(r_in, a0); x1i, y1i = P(r_in, a1)
    x0o, y0o = P(r_out, a0); x1o, y1o = P(r_out, a1)
    return (f'M {x0i:.1f} {y0i:.1f} A {r_in} {r_in} 0 0 1 {x1i:.1f} {y1i:.1f} '
            f'L {x1o:.1f} {y1o:.1f} A {r_out} {r_out} 0 0 0 {x0o:.1f} {y0o:.1f} Z')


def svg_open(w, h, title):
    m = "".join(
        f'<marker id="aE{i}" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto">'
        f'<path d="M0,1 L7,4.5 L0,8" fill="none" stroke="{ERA[i]}" stroke-width="1.8"/></marker>'
        for i in range(5))
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">'
            f'<title>{esc(title)}</title><defs>'
            f'<marker id="aN" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,1 L7,4.5 L0,8" fill="none" stroke="{MUT}" stroke-width="1.6"/></marker>'
            f'{m}'
            f'<radialGradient id="glowV" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="#8B5CF6" stop-opacity="0.22"/><stop offset="100%" stop-color="#8B5CF6" stop-opacity="0"/></radialGradient>'
            f'<radialGradient id="glowC" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="#22D3EE" stop-opacity="0.18"/><stop offset="100%" stop-color="#22D3EE" stop-opacity="0"/></radialGradient>'
            f'<linearGradient id="lgA" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#8B5CF6"/><stop offset="25%" stop-color="#22D3EE"/><stop offset="50%" stop-color="#34D399"/><stop offset="75%" stop-color="#F59E0B"/><stop offset="100%" stop-color="#FB7185"/></linearGradient>'
            f'</defs>')


# ---------------------------------------------------------------- hero
def build_hero():
    W, H = 1720, 940
    p = [svg_open(W, H, "伏羲框架：五纪十阶总览")]
    p.append(f'<rect width="{W}" height="{H}" fill="{BG}"/>')
    p.append(f'<circle cx="180" cy="120" r="420" fill="url(#glowV)"/>')
    p.append(f'<circle cx="1560" cy="820" r="460" fill="url(#glowC)"/>')

    p.append(text(70, 78, "伏羲框架 · 万物皆可学", 54, INK, "800"))
    p.append(text(72, 128, "The Fuxi Framework — Everything Can Be Learned", 22, MUT, "400", ls="0.5"))
    p.append(text(72, 172, "5 纪 10 阶时间线 · 每阶 = 最合适的方法 × 证据等级 × 开源工具 × 过关测试", 21, "#C7D2EA"))

    badges = [("十阶时间线", 17, INK, "#1B2440", "#33406B"),
              ("三轨适配：探索 / 实战 / 冲刺", 15, INK, "#1B2440", "#33406B"),
              ("证据分级 A/B/C/D", 17, "#22D3EE", "#0E2433", "#155E75"),
              ("先建图再填肉 · 先检索再重复 · 先做真事", 15, MUT, "none", "#33406B")]
    ys = [54, 98, 142, 186]
    for (s, size, fg, bg, stroke), y in zip(badges, ys):
        w = tw(s, size) + 24
        g, _ = chip(1652 - w, y, s, size, fg, bg, stroke, h=32)
        p.append(g)

    col_w, gap = 320, 16
    x0 = 60
    for i in range(5):
        cx = x0 + i * (col_w + gap)
        p.append(rect(cx, 230, col_w, 580, "#0F1729", ERA[i] + "55", rx=22, sw=1.4))
        p.append(rect(cx, 230, col_w, 58, ERA[i] + "26", ERA[i] + "66", rx=18, sw=1.1))
        p.append(text(cx + col_w / 2, 251, f"{ERA_NAMES[i]}", 23, ERA[i], "700", "middle"))
        p.append(text(cx + col_w / 2, 274, ERA_SUB[i], 15, MUT, "400", "middle"))
        for j in range(2):
            st = STAGES[i * 2 + j]
            cy = 306 + j * 258
            p.append(rect(cx + 14, cy, col_w - 28, 234, PANEL, "#232F4E", rx=16, sw=1.2))
            p.append(f'<circle cx="{cx + 14 + 40}" cy="{cy + 40}" r="21" fill="{ERA[st["era"]]}"/>')
            p.append(text(cx + 14 + 40, cy + 41, str(st["num"]), 21, "#0B1020", "800", "middle"))
            p.append(text(cx + 14 + 78, cy + 40, st["name"], 30, INK, "700"))
            p.append(text(cx + 14 + 78, cy + 68, st["en"], 14, MUT, "400", ls="1"))
            gq = f'证据 {st["grade"]}'
            wq = tw(gq, 15) + 20
            g, _ = chip(cx + col_w - 28 + 14 - wq - 12, cy + 22, gq, 15, "#0B1020", GRADE[st["grade"]], None, h=30, pad=10)
            p.append(g)
            p.append(text(cx + 14 + 30, cy + 108, st["line"], 20, "#C7D2EA"))
            cxx = cx + 14 + 16
            for c in st["chips"]:
                g2, w2 = chip(cxx, cy + 134, c, 16, ERA[st["era"]], "none", ERA[st["era"]] + "AA", h=32)
                p.append(g2)
                cxx += w2 + 10
            if j == 0:
                p.append(f'<line x1="{cx + col_w / 2}" y1="{cy + 234}" x2="{cx + col_w / 2}" y2="{cy + 256}" stroke="{MUT}" stroke-width="1.4" marker-end="url(#aN)"/>')

    by = 866
    p.append(rect(60, by - 26, W - 120, 64, PANEL2, "#232F4E", rx=18, sw=1.1))
    step = (W - 200) / 9
    for i in range(10):
        px = 100 + i * step
        col = ERA[STAGES[i]["era"]]
        p.append(f'<circle cx="{px:.0f}" cy="{by}" r="13" fill="{col}"/>')
        p.append(text(px, by + 1, str(i + 1), 13, "#0B1020", "800", "middle"))
        if i < 9:
            p.append(f'<line x1="{px + 18:.0f}" y1="{by}" x2="{px + step - 18:.0f}" y2="{by}" stroke="{LINE}" stroke-width="2" marker-end="url(#aN)"/>')
    p.append(text(W / 2, by - 44, "主干流向：上一阶的产出，是下一阶的输入", 17, MUT, "400", "middle"))
    p.append(text(W - 90, 46, "github.com/HuanMoovo/fuxi", 16, MUT, "400", "end"))
    p.append(text(W / 2, H - 18, "启发式路线图 · 经验权重 · 证据分级为本项目综合判断（详见 docs/evidence.md）", 15, "#5E6C8F", "400", "middle"))
    p.append("</svg>")
    return "".join(p)


# ---------------------------------------------------------------- engine
def build_engine():
    W, H = 1560, 1010
    p = [svg_open(W, H, "伏羲引擎：十阶环 · 三恒 · 两尺 · 一原则")]
    p.append(f'<rect width="{W}" height="{H}" fill="{BG}"/>')
    p.append(f'<circle cx="380" cy="300" r="380" fill="url(#glowV)"/>')
    p.append(text(64, 66, "伏羲引擎 · 十阶环", 40, INK, "800"))
    p.append(text(64, 104, "Learning OS：三恒约束 × 两把尺 × 一原则，套在十阶主干上", 19, MUT))

    cx, cy, r_out, r_in = 500, 580, 322, 234
    for i in range(10):
        mid = 90 - (i * 36 + 18)
        col = ERA[STAGES[i]["era"]]
        p.append(f'<path d="{seg_path(mid, 34, r_in, r_out, cx, cy)}" fill="{col}" opacity="0.9" stroke="{BG}" stroke-width="2"/>')
        lx, ly = polar(cx, cy, r_out + 54, mid)
        anchor = "start" if lx > cx + 30 else ("end" if lx < cx - 30 else "middle")
        st = STAGES[i]
        p.append(text(lx, ly - 9, f'{st["num"]} · {st["name"]}', 23, col, "700", anchor))
        p.append(text(lx, ly + 15, st["en"], 14, MUT, "400", anchor))
    p.append(f'<rect x="{cx - 62}" y="{cy - 62}" width="124" height="124" rx="14" fill="#D33A3A" transform="rotate(45 {cx} {cy})"/>')
    p.append(text(cx, cy + 1, "伏羲", 40, "#FFFFFF", "800", "middle"))
    for ang, label, col in [(152, "认知负荷预算", ERA[1]), (28, "动机与自我调节", ERA[0]), (270, "反馈回路", ERA[3])]:
        lx, ly = polar(cx, cy, 150, ang)
        w = tw(label, 15) + 24
        p.append(rect(lx - w / 2, ly - 16, w, 32, PANEL2, col, rx=16, sw=1.4))
        p.append(text(lx, ly + 1, label, 15, col, "600", "middle"))
    p.append(text(cx, cy + 118, "十阶主干：上一阶输出 = 下一阶输入", 15, "#C7D2EA", "400", "middle"))
    p.append(text(cx, 963, "① 立志 → ② 建图 → ③ 拆解 → ④ 编码 → ⑤ 检索 → ⑥ 间隔 → ⑦ 精练 → ⑧ 实战 → ⑨ 教学 → ⑩ 维护", 17, "#C7D2EA", "500", "middle"))

    px, pw = 980, 545
    y = 150
    p.append(rect(px, y, pw, 240, PANEL, "#232F4E", rx=18))
    p.append(text(px + 24, y + 34, "三恒 · 永远在线的约束", 24, INK, "700"))
    rows = [("认知负荷预算", "工作记忆有限；新手先给示范与引导 [C15][C16]", ERA[1]),
            ("动机与自我调节", "自主 · 胜任 · 联结；目标 + 计划 [C34][C36]", ERA[0]),
            ("反馈回路", "即时、具体、可行动；无反馈=无精练 [C46][C47]", ERA[3])]
    for i, (t1, t2, col) in enumerate(rows):
        yy = y + 78 + i * 52
        p.append(f'<circle cx="{px + 34}" cy="{yy}" r="7" fill="{col}"/>')
        p.append(text(px + 54, yy, t1, 19, INK, "600"))
        p.append(text(px + 54 + tw(t1, 19) + 14, yy + 1, t2, 15, MUT))
    y = 414
    p.append(rect(px, y, pw, 210, PANEL, "#232F4E", rx=18))
    p.append(text(px + 24, y + 34, "两把尺 · 测什么", 24, INK, "700"))
    p.append(text(px + 24, y + 74, "表现（当下手感）", 17, "#F59E0B"))
    p.append(rect(px + 24, y + 88, 260, 14, "#F59E0B", None, rx=7, op="0.35"))
    p.append(text(px + 300, y + 96, "→ 会骗人", 15, MUT))
    p.append(text(px + 24, y + 130, "学习（延迟检索仍会）", 17, "#34D399"))
    p.append(rect(px + 24, y + 144, 260, 14, "#34D399", None, rx=7, op="0.9"))
    p.append(text(px + 300, y + 152, "→ 才是裁判", 15, MUT))
    p.append(text(px + 24, y + 184, "流畅感是骗子；一周后再测才作数 [C01][C05]", 15, MUT))
    y = 648
    p.append(rect(px, y, pw, 240, PANEL, "#232F4E", rx=18))
    p.append(text(px + 24, y + 34, "一原则 · ICAP 主动参与", 24, INK, "700"))
    lv = [("I 交互", "与人/系统讨论、互教", 1.0, ERA[2]), ("C 建构", "自我解释、画图、生成", 0.78, ERA[1]),
          ("A 主动", "操作、标注、复制", 0.5, ERA[0]), ("P 被动", "看、听、划重点", 0.22, ERA[4])]
    for i, (t1, t2, f, col) in enumerate(lv):
        yy = y + 72 + i * 42
        bw = 260 * f
        p.append(rect(px + 24, yy - 12, bw, 24, col, None, rx=12, op="0.85"))
        p.append(text(px + 34, yy, t1, 16, "#0B1020", "700"))
        p.append(text(px + 24 + max(bw, 130) + 16, yy, t2, 15, MUT))
    y = 912
    p.append(text(px + 24, y + 4, "证据分级：", 16, MUT))
    xx = px + 24 + tw("证据分级：", 16)
    for gl_, gcol in [("A 强", GRADE["A"]), ("B 中", GRADE["B"]), ("C 弱/条件", GRADE["C"]), ("D 证伪", GRADE["D"])]:
        g, w = chip(xx, y - 14, gl_, 14, gcol, "none", gcol + "99", h=28, pad=10)
        p.append(g); xx += w + 8
    p.append(text(64, H - 22, "三恒为本项目综合框架，具体证据见 docs/evidence.md", 15, "#5E6C8F"))
    p.append("</svg>")
    return "".join(p)


# ---------------------------------------------------------------- paths
def build_paths():
    W, H = 1700, 950
    p = [svg_open(W, H, "三轨适配：探索 / 实战 / 冲刺")]
    p.append(f'<rect width="{W}" height="{H}" fill="{BG}"/>')
    p.append(f'<circle cx="1500" cy="140" r="360" fill="url(#glowC)"/>')
    p.append(text(64, 70, "三轨适配 · 先选路线，再分配阶段权重", 40, INK, "800"))
    p.append(text(64, 110, "同一个十阶主干，不同走法；权重为经验值，见 docs/paths.md", 19, MUT))
    y = 156
    qs = [("只是好奇 → 探索轨", ERA[1]), ("有交付目标 → 实战轨", ERA[3]), ("有截止日/考试 → 冲刺轨", ERA[4])]
    xx = 64
    for q, col in qs:
        g, w = chip(xx, y, q, 17, col, "none", col + "AA", h=36, pad=16)
        p.append(g); xx += w + 18

    lanes = [
        ("探索轨", "无目标 · 想了解", [0.16, 0.9, 0.9, 0.9, 0.9, 0.45, 0.16, 0.16, 0.45, 0.16], ERA[1]),
        ("实战轨", "有交付物 / 工作技能", [0.9, 0.3, 0.9, 0.45, 0.45, 0.45, 0.9, 0.9, 0.45, 0.16], ERA[3]),
        ("冲刺轨", "考试 / 证书 / 硬截止", [0.9, 0.45, 0.45, 0.45, 0.9, 0.9, 0.9, 0.45, 0.16, 0.16], ERA[4]),
    ]
    lx, lw = 64, 210
    gx, gw, ggap = 320, 112, 12
    lane_w = 1506
    ly = 280
    for i in range(10):
        x = gx + i * (gw + ggap)
        p.append(text(x + gw / 2, ly - 64, f'{i + 1}', 21, ERA[STAGES[i]["era"]], "700", "middle"))
        p.append(text(x + gw / 2, ly - 38, STAGES[i]["name"], 16, MUT, "400", "middle"))
    for li, (name, sub, weights, col) in enumerate(lanes):
        y = ly + li * 136
        p.append(rect(64, y, lane_w, 120, "#0F1729", LINE, rx=18, sw=1.1))
        p.append(text(lx + 24, y + 48, name, 26, col, "700"))
        p.append(text(lx + 24, y + 80, sub, 15, MUT))
        for i, wgt in enumerate(weights):
            x = gx + i * (gw + ggap)
            c = ERA[STAGES[i]["era"]]
            op = "0.88" if wgt >= 0.8 else ("0.42" if wgt >= 0.4 else "0.16")
            p.append(rect(x, y + 16, gw, 88, c, None, rx=12, op=op))
            tcol = "#0B1020" if wgt >= 0.8 else (INK if wgt >= 0.4 else "#8A94B5")
            lab = "重" if wgt >= 0.8 else ("中" if wgt >= 0.4 else "轻")
            p.append(text(x + gw / 2, y + 60, lab, 22, tcol, "700", "middle"))
    my = 708
    spine_x = 1608
    ys_mid = [ly + li * 136 + 60 for li in range(3)]
    for ym in ys_mid:
        p.append(f'<line x1="{1574}" y1="{ym}" x2="{spine_x - 4}" y2="{ym}" stroke="{MUT}" stroke-width="1.6" marker-end="url(#aN)" opacity="0.85"/>')
    p.append(f'<line x1="{spine_x}" y1="{ys_mid[0]}" x2="{spine_x}" y2="{my - 4}" stroke="{MUT}" stroke-width="1.6" marker-end="url(#aN)" opacity="0.85"/>')
    p.append(rect(64, my, 1586, 78, PANEL2, "#33406B", rx=20, sw=1.2))
    p.append(text(96, my + 30, "共用十阶主干", 22, INK, "700"))
    p.append(text(96 + tw("共用十阶主干", 22) + 20, my + 31, "①立志 → ②建图 → ③拆解 → ④编码 → ⑤检索 → ⑥间隔 → ⑦精练 → ⑧实战 → ⑨教学 → ⑩维护", 19, "#C7D2EA"))
    p.append(text(96, my + 58, "换乘：目标变化就换轨；考试结束降级为低剂量维护，防止技能衰减 [C28]", 15, MUT))
    lgx = 1180
    for wgt, lab_ in [("0.88", "重"), ("0.42", "中"), ("0.16", "轻")]:
        p.append(rect(lgx, my + 26, 16, 16, INK, None, rx=4, op=wgt))
        p.append(text(lgx + 24, my + 34, lab_, 15, MUT))
        lgx += 62
    p.append(text(lgx + 4, my + 34, "（底色 = 所属纪）", 14, "#5E6C8F"))
    p.append(text(W / 2, H - 20, "权重为经验值、非实验结论；方法与证据见 docs/stages 与 docs/evidence.md", 15, "#5E6C8F", "400", "middle"))
    p.append("</svg>")
    return "".join(p)


# ---------------------------------------------------------------- spacing
def build_spacing():
    W, H = 1560, 900
    p = [svg_open(W, H, "间隔：遗忘曲线与复习调度")]
    p.append(f'<rect width="{W}" height="{H}" fill="{BG}"/>')
    p.append(f'<circle cx="240" cy="200" r="330" fill="url(#glowV)"/>')
    p.append(text(64, 70, "间隔 · 在遗忘边缘复习", 40, INK, "800"))
    p.append(text(64, 110, "遗忘不是 bug；卡在 R≈0.9 复习，收益/成本最优", 19, MUT))
    p.append(text(100, 196, "R = e^(−t/S)　（S 越大，衰减越慢）", 16, "#C7D2EA", "500"))

    ox, oy, pw, ph = 120, 240, 740, 460
    p.append(f'<line x1="{ox}" y1="{oy + ph}" x2="{ox + pw}" y2="{oy + ph}" stroke="{LINE}" stroke-width="1.5"/>')
    p.append(f'<line x1="{ox}" y1="{oy}" x2="{ox}" y2="{oy + ph}" stroke="{LINE}" stroke-width="1.5"/>')
    p.append(text(ox + pw / 2, oy + ph + 42, "时间 →", 17, MUT, "400", "middle"))
    p.append(text(ox - 42, oy + ph / 2, "记忆强度 R", 17, MUT, "400", "middle"))

    def X(t): return ox + (t / 36.0) * pw
    def Y(r): return oy + ph - r * ph
    for tick, lab_ in [(1.0, "1.0"), (0.5, "0.5"), (0.0, "0")]:
        p.append(text(ox - 12, Y(tick), lab_, 14, MUT, "400", "end"))
    p.append(f'<line x1="{ox}" y1="{Y(0.9):.1f}" x2="{ox + pw}" y2="{Y(0.9):.1f}" stroke="#F59E0B" stroke-width="1.3" stroke-dasharray="6 6" opacity="0.75"/>')
    p.append(text(ox + pw - 8, Y(0.9) - 16, "R ≈ 0.9：最佳复习窗口", 15, "#F59E0B", "600", "end"))
    reviews = [(0.0, 1.0), (1.0, 3.0), (4.0, 8.0), (12.0, 20.0)]
    seg_colors = ["#22D3EE", "#34D399", "#8B5CF6", "#FB7185"]
    for k, (t_start, S) in enumerate(reviews):
        t_end = 36.0 if k == len(reviews) - 1 else reviews[k + 1][0]
        pts = []
        t = t_start
        while t <= t_end + 1e-9:
            r = math.exp(-(t - t_start) / S)
            pts.append(f"{X(t):.1f},{Y(r):.1f}")
            t += 0.25
        p.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{seg_colors[k]}" stroke-width="3" opacity="0.95"/>')
    for k, (t, S) in enumerate(reviews):
        px_, py_ = X(t), Y(1.0)
        p.append(f'<circle cx="{px_:.1f}" cy="{py_:.1f}" r="7" fill="{seg_colors[k]}" stroke="{BG}" stroke-width="3"/>')
        lab = ["学习", "复习①", "复习②", "复习③"][k]
        if k == 0:
            p.append(text(px_ + 12, py_ + 24, lab, 15, seg_colors[k], "600"))
        else:
            p.append(text(px_ + 10, py_ - 20, lab, 15, seg_colors[k], "600"))
    p.append(text(ox + pw - 8, oy + 16, "S 随复习增长 → 曲线越来越平", 15, MUT, "400", "end"))
    p.append(text(ox, oy + ph + 72, "口径：最佳间隔 ≈ 目标保持期的 10–20% [C06]；254 项实验支持分布练习 [C04]", 15, MUT))

    rx0 = 940
    ry0 = 240
    p.append(rect(rx0, ry0, 560, 268, PANEL, "#232F4E", rx=18))
    p.append(text(rx0 + 22, ry0 + 30, "交错练习 vs 块状练习", 22, INK, "700"))
    lx0 = rx0 + 22
    for j, (nm, col) in enumerate([("A", ERA[2]), ("B", ERA[0]), ("C", ERA[3])]):
        p.append(rect(lx0 + j * 66, ry0 + 50, 18, 18, col, None, rx=4, op="0.9"))
        p.append(text(lx0 + j * 66 + 24, ry0 + 59, f"{nm} 类题型", 14, MUT))

    def grid_row(yy, seq, label):
        p.append(text(rx0 + 22, yy + 22, label, 16, INK, "600"))
        for i, k in enumerate(seq):
            x = rx0 + 96 + i * 48
            p.append(rect(x, yy, 44, 44, [ERA[2], ERA[0], ERA[3]][k], None, rx=8, op="0.85"))
            p.append(text(x + 22, yy + 23, "ABC"[k], 20, "#0B1020", "800", "middle"))

    grid_row(ry0 + 84, [0, 0, 0, 1, 1, 1, 2, 2, 2], "块状")
    grid_row(ry0 + 142, [0, 1, 2, 0, 1, 2, 0, 1, 2], "交错")
    p.append(text(rx0 + 22, ry0 + 214, "块状：一类连做，手感顺。 交错：混着练，学得慢、记得牢。", 15, MUT))
    p.append(text(rx0 + 22, ry0 + 244, "延迟测验 61% vs 38%（d=0.83）；材料越相似收益越大 [C07][C08]", 15, "#F59E0B"))

    ry1 = 536
    p.append(rect(rx0, ry1, 560, 300, PANEL, "#232F4E", rx=18))
    p.append(text(rx0 + 22, ry1 + 32, "调度：SM-2 → FSRS", 22, INK, "700"))
    steps = ["每张卡有状态：难度 D · 稳定度 S · 可提取度 R",
             "你给评分（Again / Hard / Good / Easy）",
             "更新 D、S，计算下个复习间隔",
             "目标留存率（desired retention）由你设定，如 0.9"]
    for i, s in enumerate(steps):
        yy = ry1 + 74 + i * 44
        p.append(f'<circle cx="{rx0 + 36}" cy="{yy}" r="13" fill="#0E2433" stroke="#22D3EE" stroke-width="1.2"/>')
        p.append(text(rx0 + 36, yy + 1, str(i + 1), 13, "#22D3EE", "700", "middle"))
        p.append(text(rx0 + 62, yy, s, 16, "#C7D2EA"))
    p.append(text(rx0 + 22, ry1 + 262, "2.2 亿学习日志建模，较当时最优方法 +12.6% [C26]", 15, "#22D3EE"))
    p.append(text(rx0 + 22, ry1 + 286, "墨墨背单词线上部署；FSRS 已内置 Anki [C26][C27]", 15, MUT))
    p.append(text(W / 2, H - 20, "间隔 = 把时间变成盟友：复习点由算法安排，你只负责检索与评分", 15, "#5E6C8F", "400", "middle"))
    p.append("</svg>")
    return "".join(p)


# ---------------------------------------------------------------- loop
def build_loop():
    W, H = 1440, 920
    p = [svg_open(W, H, "刻意练习闭环：定靶-练-测-诊-修")]
    p.append(f'<rect width="{W}" height="{H}" fill="{BG}"/>')
    p.append(f'<circle cx="360" cy="480" r="360" fill="url(#glowV)"/>')
    p.append(text(64, 70, "精练 · 刻意练习闭环", 40, INK, "800"))
    p.append(text(64, 110, "无反馈 = 无精练：每一次循环都要闭合", 19, MUT))
    cx, cy, R = 420, 510, 250
    nodes = [("定靶", "选一个子技能", 0), ("全神练", "在能力边缘", 1), ("即时测", "证据 > 感觉", 2),
             ("诊断", "根因分类", 3), ("修正再练", "针对性重练", 4)]
    for i, (t1, t2, e) in enumerate(nodes):
        ang = 90 - i * 72
        nx, ny = polar(cx, cy, R, ang)
        col = ERA[e]
        p.append(f'<circle cx="{nx:.0f}" cy="{ny:.0f}" r="66" fill="{PANEL}" stroke="{col}" stroke-width="2"/>')
        p.append(text(nx, ny - 10, t1, 22, INK, "700", "middle"))
        p.append(text(nx, ny + 16, t2, 14, MUT, "400", "middle"))
        s_ang, e_ang = ang - 26, ang - 72 + 26
        sx_, sy_ = polar(cx, cy, R, s_ang)
        ex_, ey_ = polar(cx, cy, R, e_ang)
        p.append(f'<path d="M {sx_:.0f} {sy_:.0f} A {R} {R} 0 0 1 {ex_:.0f} {ey_:.0f}" fill="none" stroke="{col}" stroke-width="2.4" opacity="0.75" marker-end="url(#aE{e})"/>')
    p.append(text(cx, cy + 0, "闭环", 30, INK, "800", "middle"))
    p.append(text(cx, cy + 34, "缺一环 = 原地踏步", 15, MUT, "400", "middle"))

    rx0, ry0 = 800, 150
    p.append(rect(rx0, ry0, 590, 240, PANEL, "#232F4E", rx=18))
    p.append(text(rx0 + 24, ry0 + 34, "三速反馈", 24, INK, "700"))
    fr = [("即时（每个动作）", "对答案 / 引擎 / 导师批注", ERA[1]), ("每日（日志复盘）", "错题日志 + 根因分类", ERA[3]),
          ("每周（教练/检视）", "周检视 + 高手示范 [C44]", ERA[0])]
    for i, (t1, t2, col) in enumerate(fr):
        yy = ry0 + 78 + i * 52
        p.append(f'<circle cx="{rx0 + 36}" cy="{yy}" r="7" fill="{col}"/>')
        p.append(text(rx0 + 54, yy, t1, 18, INK, "600"))
        p.append(text(rx0 + 54 + tw(t1, 18) + 12, yy + 1, t2, 15, MUT))
    p.append(text(rx0 + 24, ry0 + 220, "具体、可行动、对事不对人；约 1/3 的反馈会反噬 [C46][C47]", 15, "#F59E0B"))

    ry1 = 420
    p.append(rect(rx0, ry1, 590, 300, PANEL, "#232F4E", rx=18))
    p.append(text(rx0 + 24, ry1 + 32, "错误日志（示例结构）", 22, INK, "700"))
    cols = [("日期", 24), ("错因类型", 94), ("修正动作", 214), ("复测", 440)]
    p.append(rect(rx0 + 18, ry1 + 52, 554, 36, PANEL2, None, rx=10))
    for h_, hx in cols:
        p.append(text(rx0 + hx, ry1 + 70, h_, 15, MUT, "600"))
    rows = [("10-01", "概念错", "重学前置概念，画反例", "10-04 ✓"),
            ("10-02", "程序错", "慢速分解，重练 2 组", "10-05 重练"),
            ("10-03", "粗心", "检查清单 + 限时 3 题", "10-06 ✓")]
    for i, r_ in enumerate(rows):
        yy = ry1 + 106 + i * 46
        if i > 0:
            p.append(f'<line x1="{rx0 + 18}" y1="{yy - 26}" x2="{rx0 + 572}" y2="{yy - 26}" stroke="{LINE}" stroke-width="1"/>')
        for cell, hx in zip(r_, [c[1] for c in cols]):
            p.append(text(rx0 + hx, yy - 6, cell, 15, "#C7D2EA"))
    p.append(text(rx0 + 24, ry1 + 258, "根因分类：概念错｜程序错｜粗心｜记忆缺失 —— 不同根因，不同药方", 15, MUT))
    p.append(text(rx0 + 24, ry1 + 284, "先自己提交版本，再请 AI 挑错（护栏用法）[C56]", 15, "#22D3EE"))
    p.append(text(W / 2, H - 20, "刻意练习 = 明确子目标 × 全神贯注 × 能力边缘 × 即时反馈与修正 [C31]", 15, "#5E6C8F", "400", "middle"))
    p.append("</svg>")
    return "".join(p)


# ---------------------------------------------------------------- mark
def build_mark():
    S = 240
    p = [svg_open(S, S, "伏羲框架标志")]
    p.append(f'<rect width="{S}" height="{S}" fill="{BG}"/>')
    cx, cy, R = 120, 120, 84
    pts = []
    for i in range(10):
        ang = 90 - i * 36
        x, y = polar(cx, cy, R, ang)
        pts.append((x, y, ERA[STAGES[i]["era"]]))
    for i, (x, y, col) in enumerate(pts):
        x2, y2, col2 = pts[(i + 1) % 10]
        p.append(f'<line x1="{x:.0f}" y1="{y:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="{col}" stroke-width="1.6" opacity="0.5"/>')
        p.append(f'<line x1="{x:.0f}" y1="{y:.0f}" x2="{cx}" y2="{cy}" stroke="#E8ECF8" stroke-width="1.1" opacity="0.35"/>')
    for x, y, col in pts:
        p.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="9" fill="{col}"/>')
    p.append(f'<circle cx="{cx}" cy="{cy}" r="17" fill="#E8ECF8"/>')
    p.append(f'<circle cx="{cx}" cy="{cy}" r="26" fill="none" stroke="#E8ECF8" stroke-width="1.2" opacity="0.5"/>')
    p.append("</svg>")
    return "".join(p)


def main():
    files = {
        "fuxi-hero.svg": build_hero(),
        "fuxi-engine.svg": build_engine(),
        "fuxi-paths.svg": build_paths(),
        "fuxi-spacing.svg": build_spacing(),
        "fuxi-loop.svg": build_loop(),
        "fuxi-mark.svg": build_mark(),
    }
    for name, content in files.items():
        path = os.path.join(OUT, name)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"OK {path} ({len(content.encode('utf-8'))} bytes)")


if __name__ == "__main__":
    main()
