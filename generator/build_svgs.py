#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""伏羲框架 SVG 图表生成器 v3 —— 复古笔记本手绘风。
运行: python generator/build_svgs.py
输出: docs/assets/fuxi-hero.svg / fuxi-engine.svg / fuxi-paths.svg / fuxi-spacing.svg / fuxi-loop.svg / fuxi-mark.svg / fuxi-logo.svg
风格: 米黄纸张 + 横格线 + 红边线 + 装订孔 + 白纸卡片 + 和纸胶带 + 手写体 + 红印章 + 高亮笔。
纯静态、无外部依赖、全内联属性（GitHub 渲染安全）。
"""
import math, os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "docs", "assets")
os.makedirs(OUT, exist_ok=True)

# —— 手写字体栈（拉丁优先手写字体，中文回退楷体）
FF = "'Segoe Print','Bradley Hand','Comic Sans MS','KaiTi','STKaiti','Kaiti SC','Noto Serif SC',serif"
# —— 纸张与墨水
PAPER = "#F5EEDD"; RULE = "#C9D6E8"; MARGINR = "#E4A9A0"
CARD = "#FFFDF6"; CARD_ST = "#D9CFB8"; SHADOW = "#00000014"
INK = "#2B2F36"; INK2 = "#6A6F7C"
BLUE = "#2F5496"; RED = "#C0392B"; GREEN = "#3E7C59"; ORANGE = "#C97A3D"; PURPLE = "#6E4E9E"
YELLOW = "#F6E27A"
TAPES = ["#E7DCF0", "#D9E7F2", "#DCEBE0", "#F3E6CE", "#F2DCDE"]  # 与五纪色相呼应
ERA = ["#6E4E9E", "#2E6E8E", "#3E7C59", "#C97A3D", "#B04A5A"]
GRADE = {"A": "#3E7C59", "B": "#2F5496", "C": "#C97A3D", "D": "#C0392B"}
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


def rect(x, y, w, h, fill, stroke=None, rx=8, sw=1.2, op=None, dash=None):
    s = f'<rect x="{x:.0f}" y="{y:.0f}" width="{w:.0f}" height="{h:.0f}" rx="{rx}" fill="{fill}"'
    if stroke: s += f' stroke="{stroke}" stroke-width="{sw}"'
    if op is not None: s += f' opacity="{op}"'
    if dash: s += f' stroke-dasharray="{dash}"'
    return s + "/>"


def text(x, y, s, size, fill, weight="400", anchor="start", op=None, ls=None, fs=FF):
    a = f'<text x="{x:.0f}" y="{y:.0f}" font-size="{size}" fill="{fill}" font-weight="{weight}" text-anchor="{anchor}" font-family="{fs}"'
    if op is not None: a += f' opacity="{op}"'
    if ls: a += f' letter-spacing="{ls}"'
    return a + f' dominant-baseline="middle">{esc(s)}</text>'


def chip(x, y, s, size=16, fg=INK, bg=CARD, stroke=CARD_ST, h=30, pad=12, weight="500", rx=None):
    w = tw(s, size) + pad * 2
    g = rect(x, y, w, h, bg, stroke, rx=rx if rx is not None else h / 2, sw=1.1)
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


def tape(cx, cy, color, deg, w=76, h=22, op=0.85):
    return (f'<rect x="{-w/2}" y="{-h/2}" width="{w}" height="{h}" fill="{color}" opacity="{op}" rx="3" '
            f'transform="translate({cx:.0f} {cy:.0f}) rotate({deg})"/>')


def paper_card(x, y, w, h, tape_specs=None, rx=10):
    g = rect(x + 3, y + 4, w, h, "#00000010", None, rx=rx)
    g += rect(x, y, w, h, CARD, CARD_ST, rx=rx, sw=1.3)
    for (tx, ty, ci, deg) in (tape_specs or []):
        g += tape(x + tx, y + ty, TAPES[ci], deg)
    return g


def doodle_arrow(x1, y1, x2, y2, color=INK2, sw=1.8, bend=8):
    dx, dy = x2 - x1, y2 - y1
    L = math.hypot(dx, dy) or 1
    nx, ny = -dy / L, dx / L
    mx, my = (x1 + x2) / 2 + nx * bend, (y1 + y2) / 2 + ny * bend
    ang = math.atan2(y2 - my, x2 - mx)
    a1 = ang + math.radians(152); a2 = ang - math.radians(152)
    hx1, hy1 = x2 + 13 * math.cos(a1), y2 + 13 * math.sin(a1)
    hx2, hy2 = x2 + 13 * math.cos(a2), y2 + 13 * math.sin(a2)
    return (f'<path d="M {x1:.0f} {y1:.0f} Q {mx:.0f} {my:.0f} {x2:.0f} {y2:.0f}" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="round"/>'
            f'<path d="M {hx1:.0f} {hy1:.0f} L {x2:.0f} {y2:.0f} L {hx2:.0f} {hy2:.0f}" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="round"/>')


def hand_circle(cx, cy, r, color, sw=2.2):
    """手绘感双线圆。"""
    return (f'<circle cx="{cx:.0f}" cy="{cy:.0f}" r="{r}" fill="{CARD}" stroke="{color}" stroke-width="{sw}"/>'
            f'<circle cx="{cx+2:.0f}" cy="{cy+1:.0f}" r="{r-3}" fill="none" stroke="{color}" stroke-width="0.8" opacity="0.45"/>')


def stamp(cx, cy, size=128, chars="伏羲", rot=-7, color=RED, txt="#FFFFFF", fill=None):
    g = f'<g transform="rotate({rot} {cx} {cy})">'
    if fill:
        g += rect(cx - size / 2, cy - size / 2, size, size, fill, None, rx=10)
    g += rect(cx - size / 2, cy - size / 2, size, size, "none", color, rx=10, sw=3)
    g += rect(cx - size / 2 + 7, cy - size / 2 + 7, size - 14, size - 14, "none", color, rx=7, sw=1, op=0.7)
    g += text(cx, cy + 1, chars, int(size * 0.36), txt, "800", "middle")
    g += "</g>"
    return g


def deco_page(w, h, no=1, count=6):
    """纸张背景 + 横格 + 红边线 + 装订孔 + 页眉页脚。"""
    p = [rect(0, 0, w, h, PAPER, None, rx=0)]
    y = 118
    while y < h - 46:
        p.append(f'<line x1="70" y1="{y}" x2="{w-52}" y2="{y}" stroke="{RULE}" stroke-width="1.6" opacity="1"/>')
        y += 38
    p.append(f'<line x1="88" y1="96" x2="88" y2="{h-40}" stroke="{MARGINR}" stroke-width="1.8" opacity="0.8"/>')
    for hy in [150, 360, 570, 780]:
        if hy < h - 60:
            p.append(f'<circle cx="44" cy="{hy}" r="13" fill="{PAPER}" stroke="#C9BFA8" stroke-width="1.4"/>')
    p.append(text(70, 56, "伏羲框架 · 学习笔记", 15, INK2))
    p.append(text(w - 64, 56, f"No.{no} / {count}　·　2026.10", 14, INK2, "400", "end"))
    p.append(f'<line x1="70" y1="76" x2="{w-52}" y2="76" stroke="{INK2}" stroke-width="1" stroke-dasharray="7 7" opacity="0.5"/>')
    return "".join(p)


def svg_open(w, h, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">'
            f'<title>{esc(title)}</title>')


# ---------------------------------------------------------------- hero
def build_hero():
    W, H = 1720, 960
    p = [svg_open(W, H, "伏羲框架：五纪十阶总览（复古笔记本风）")]
    p.append(deco_page(W, H, 1, 8))
    # 标题（黄色高亮 + 手写体）
    p.append(rect(58, 92, 560, 78, YELLOW, None, rx=8, op="0.5"))
    p.append(text(78, 132, "伏羲框架 · 万物皆可学", 52, INK, "700"))
    p.append(text(80, 184, "The Fuxi Framework — Everything Can Be Learned", 21, INK2))
    p.append(text(80, 222, "5 纪 10 阶时间线 · 每阶 = 最合适的方法 × 证据等级 × 开源工具 × 过关测试", 20, "#4A5160"))
    # 右侧标签（纸片）
    badges = [("十阶时间线", 16), ("三轨适配：探索 / 实战 / 冲刺", 14)]
    yy = 100
    for s, size in badges:
        g, w = chip(1664 - (tw(s, size) + 24), yy, s, size, INK, CARD, CARD_ST, h=32)
        p.append(g); yy += 46
    # 证据分级（圈字母）
    p.append(text(1664 - 296, 236, "证据分级", 14, INK2, "400", "start"))
    xx = 1664 - 296 + tw("证据分级", 14) + 10
    for letter, col in [("A", GRADE["A"]), ("B", GRADE["B"]), ("C", GRADE["C"]), ("D", GRADE["D"])]:
        p.append(f'<circle cx="{xx+13}" cy="236" r="13" fill="none" stroke="{col}" stroke-width="2"/>')
        p.append(text(xx + 13, 237, letter, 15, col, "700", "middle"))
        xx += 34
    # 五纪列
    col_w, gap = 320, 16
    x0 = 60
    for i in range(5):
        cx = x0 + i * (col_w + gap)
        p.append(rect(cx, 268, col_w, 560, "#FFFFFF55", ERA[i], rx=16, sw=1.6, dash="9 7"))
        p.append(tape(cx + col_w / 2, 282, ERA[i], -1.5 if i % 2 == 0 else 1.5, w=190, h=34, op=0.22))
        p.append(text(cx + col_w / 2, 276, f"{ERA_NAMES[i]}", 21, ERA[i], "700", "middle"))
        p.append(text(cx + col_w / 2, 294, ERA_SUB[i], 13, INK2, "400", "middle"))
        for j in range(2):
            st = STAGES[i * 2 + j]
            cy = 320 + j * 248
            cw = col_w - 28
            p.append(paper_card(cx + 14, cy, cw, 224, tape_specs=[(24, 0, st["era"], -14), (cw - 24, 2, st["era"], 12)]))
            p.append(hand_circle(cx + 14 + 40, cy + 42, 21, ERA[st["era"]]))
            p.append(text(cx + 14 + 40, cy + 43, str(st["num"]), 20, ERA[st["era"]], "700", "middle"))
            p.append(text(cx + 14 + 76, cy + 42, st["name"], 29, INK, "700"))
            p.append(text(cx + 14 + 76, cy + 68, st["en"], 13, INK2, "400", ls="1"))
            # 证据圈字母
            gx_ = cx + 14 + cw - 30
            p.append(f'<circle cx="{gx_}" cy="{cy+42}" r="19" fill="none" stroke="{GRADE[st["grade"]]}" stroke-width="2.4"/>')
            p.append(text(gx_, cy + 43, st["grade"], 19, GRADE[st["grade"]], "700", "middle"))
            p.append(text(gx_, cy + 72, "证据", 11, INK2, "400", "middle"))
            p.append(text(cx + 14 + 30, cy + 108, st["line"], 19, "#454C59"))
            cxx = cx + 14 + 18
            for c in st["chips"]:
                g2, w2 = chip(cxx, cy + 134, c, 15, ERA[st["era"]], CARD, ERA[st["era"]] + "88", h=30)
                p.append(g2)
                cxx += w2 + 9
            if j == 0:
                p.append(doodle_arrow(cx + col_w / 2, cy + 226, cx + col_w / 2, cy + 246, INK2, 1.8, 5))
    # 底部：索引卡主干
    by = 872
    p.append(paper_card(60, by - 32, W - 120, 76, tape_specs=[(90, 0, 0, -8), (W - 210, 74, 2, 8)]))
    step = (W - 280) / 9
    for i in range(10):
        px = 140 + i * step
        col = ERA[STAGES[i]["era"]]
        p.append(f'<circle cx="{px:.0f}" cy="{by+4}" r="13" fill="none" stroke="{col}" stroke-width="2"/>')
        p.append(text(px, by + 5, str(i + 1), 13, col, "700", "middle"))
        if i < 9:
            p.append(f'<line x1="{px + 18:.0f}" y1="{by+4}" x2="{px + step - 18:.0f}" y2="{by+4}" stroke="{INK2}" stroke-width="1.6" stroke-dasharray="1 0"/>')
            p.append(f'<path d="M {px+step-24:.0f} {by-1} L {px+step-16:.0f} {by+4} L {px+step-24:.0f} {by+9}" fill="none" stroke="{INK2}" stroke-width="1.6"/>')
    p.append(text(W / 2, by - 44, "主干流向：上一阶的产出，是下一阶的输入", 16, INK2, "400", "middle"))
    p.append(text(70, H - 18, "启发式路线图 · 经验权重 · 证据分级为本项目综合判断（详见 docs/evidence.md）", 14, "#8A8F7A"))
    p.append(text(W - 64, H - 18, "github.com/HuanMoovo/fuxi", 14, "#8A8F7A", "400", "end"))
    p.append("</svg>")
    return "".join(p)


# ---------------------------------------------------------------- engine
def build_engine():
    W, H = 1560, 1030
    p = [svg_open(W, H, "伏羲引擎：十阶环 · 三恒 · 两把尺 · 一原则（复古笔记本风）")]
    p.append(deco_page(W, H, 2, 8))
    p.append(rect(64, 96, 560, 46, YELLOW, None, rx=8, op="0.5"))
    p.append(text(78, 120, "伏羲引擎 · 十阶环", 36, INK, "700"))
    p.append(text(78, 168, "Learning OS：三恒约束 × 两把尺 × 一原则，套在十阶主干上", 18, INK2))

    cx, cy, r_out, r_in = 500, 600, 300, 218
    for i in range(10):
        mid = 90 - (i * 36 + 18)
        col = ERA[STAGES[i]["era"]]
        p.append(f'<path d="{seg_path(mid, 34, r_in, r_out, cx, cy)}" fill="{col}" opacity="0.92" stroke="{PAPER}" stroke-width="2.5"/>')
        lx, ly = polar(cx, cy, r_out + 52, mid)
        anchor = "start" if lx > cx + 30 else ("end" if lx < cx - 30 else "middle")
        st = STAGES[i]
        p.append(text(lx, ly - 9, f'{st["num"]} · {st["name"]}', 22, INK, "700", anchor))
        p.append(text(lx, ly + 14, st["en"], 13, INK2, "400", anchor))
    p.append(stamp(cx, cy, 110, "伏羲", -8, RED, "#FFFFFF", "#C0392B"))
    chips3 = [(152, "认知负荷预算", "#CFDFEA", "#2E6E8E"), (28, "动机与自我调节", "#DCCFE8", "#6E4E9E"), (270, "反馈回路", "#F0D3C0", "#C97A3D")]
    for ang, label, tcol, fcol in chips3:
        lx, ly = polar(cx, cy, 150, ang)
        w = tw(label, 14) + 26
        g = f'<rect x="{lx-w/2:.0f}" y="{ly-17:.0f}" width="{w:.0f}" height="34" fill="{tcol}" opacity="0.95" rx="4" transform="rotate({"2" if ang!=270 else "-2"} {lx:.0f} {ly:.0f})"/>'
        g += text(lx, ly + 1, label, 14, "#3A3A32", "600", "middle")
        p.append(g)
    p.append(text(cx, cy + 118, "十阶主干：上一阶输出 = 下一阶输入", 14, "#4A5160", "400", "middle"))
    p.append(text(cx, 963, "① 立志 → ② 建图 → ③ 拆解 → ④ 编码 → ⑤ 检索 → ⑥ 间隔 → ⑦ 精练 → ⑧ 实战 → ⑨ 教学 → ⑩ 维护", 16, "#4A5160", "500", "middle"))

    px, pw = 980, 528
    # 三恒
    y = 150
    p.append(paper_card(px, y, pw, 238, tape_specs=[(70, 0, 0, -10), (pw - 60, 2, 1, 9)]))
    p.append(text(px + 24, y + 36, "三恒 · 永远在线的约束", 22, INK, "700"))
    rows = [("认知负荷预算", "工作记忆有限；新手先给示范与引导 [C15][C16]", "#2E6E8E"),
            ("动机与自我调节", "自主 · 胜任 · 联结；目标 + 计划 [C34][C36]", "#6E4E9E"),
            ("反馈回路", "即时、具体、可行动；无反馈=无精练 [C46][C47]", "#C97A3D")]
    for i, (t1, t2, col) in enumerate(rows):
        yy = y + 82 + i * 50
        p.append(f'<circle cx="{px + 34}" cy="{yy}" r="7" fill="{col}"/>')
        p.append(text(px + 52, yy, t1, 18, INK, "600"))
        p.append(text(px + 52 + tw(t1, 18) + 12, yy + 1, t2, 14, INK2))
    # 两把尺
    y = 412
    p.append(paper_card(px, y, pw, 208, tape_specs=[(120, 0, 2, 10)]))
    p.append(text(px + 24, y + 36, "两把尺 · 测什么", 22, INK, "700"))
    p.append(text(px + 24, y + 76, "表现（当下手感）", 16, "#B06A2A"))
    p.append(rect(px + 24, y + 90, 250, 15, "#E8C48A", None, rx=4))
    p.append(text(px + 288, y + 98, "→ 会骗人", 14, INK2))
    p.append(text(px + 24, y + 132, "学习（延迟检索仍会）", 16, "#2E6E8E"))
    p.append(rect(px + 24, y + 146, 250, 15, "#7FB3D5", None, rx=4))
    p.append(text(px + 288, y + 154, "→ 才是裁判", 14, INK2))
    p.append(text(px + 24, y + 184, "流畅感是骗子；一周后再测才作数 [C01][C05]", 14, INK2))
    # 一原则
    y = 644
    p.append(paper_card(px, y, pw, 236, tape_specs=[(80, 0, 1, -9), (pw - 90, 234, 0, 8)]))
    p.append(text(px + 24, y + 36, "一原则 · ICAP 主动参与", 22, INK, "700"))
    lv = [("I 交互", "与人/系统讨论、互教", 1.0, "#9CC5A1"), ("C 建构", "自我解释、画图、生成", 0.78, "#A8C6E8"),
          ("A 主动", "操作、标注、复制", 0.5, "#C7B8E8"), ("P 被动", "看、听、划重点", 0.22, "#E8B4B4")]
    for i, (t1, t2, f, col) in enumerate(lv):
        yy = y + 76 + i * 40
        bw = 250 * f
        p.append(rect(px + 24, yy - 12, bw, 24, col, "#3A3A3A22", rx=4, sw=1))
        p.append(text(px + 34, yy, t1, 15, "#33392F", "700"))
        p.append(text(px + 24 + max(bw, 132) + 16, yy, t2, 14, INK2))
    # 分级图例
    p.append(text(px + 24, 928, "证据分级：", 15, INK2))
    xx = px + 24 + tw("证据分级：", 15)
    for letter, col, lab_ in [("A", GRADE["A"], " 强"), ("B", GRADE["B"], " 中"), ("C", GRADE["C"], " 弱/条件"), ("D", GRADE["D"], " 证伪")]:
        p.append(f'<circle cx="{xx+13}" cy="928" r="13" fill="none" stroke="{col}" stroke-width="2"/>')
        p.append(text(xx + 13, 929, letter, 15, col, "700", "middle"))
        p.append(text(xx + 30, 929, lab_, 13, INK2))
        xx += 30 + tw(lab_, 13) + 16
    p.append(text(70, H - 18, "三恒为本项目综合框架，具体证据见 docs/evidence.md", 14, "#8A8F7A"))
    p.append("</svg>")
    return "".join(p)


# ---------------------------------------------------------------- paths
def build_paths():
    W, H = 1700, 970
    p = [svg_open(W, H, "三轨适配：探索 / 实战 / 冲刺（复古笔记本风）")]
    p.append(deco_page(W, H, 3, 8))
    p.append(rect(64, 96, 680, 46, YELLOW, None, rx=8, op="0.5"))
    p.append(text(78, 120, "三轨适配 · 先选路线，再分配阶段权重", 36, INK, "700"))
    p.append(text(78, 168, "同一个十阶主干，不同走法；权重为经验值，见 docs/paths.md", 18, INK2))
    y = 200
    qs = [("只是好奇 → 探索轨", ERA[1]), ("有交付目标 → 实战轨", ERA[3]), ("有截止日/考试 → 冲刺轨", ERA[4])]
    xx = 78
    for q, col in qs:
        g, w = chip(xx, y, q, 16, col, CARD, col + "99", h=34, pad=15)
        p.append(g); xx += w + 16

    lanes = [
        ("探索轨", "无目标 · 想了解", [0.16, 0.9, 0.9, 0.9, 0.9, 0.45, 0.16, 0.16, 0.45, 0.16], ERA[1]),
        ("实战轨", "有交付物 / 工作技能", [0.9, 0.3, 0.9, 0.45, 0.45, 0.45, 0.9, 0.9, 0.45, 0.16], ERA[3]),
        ("冲刺轨", "考试 / 证书 / 硬截止", [0.9, 0.45, 0.45, 0.45, 0.9, 0.9, 0.9, 0.45, 0.16, 0.16], ERA[4]),
    ]
    gx, gw, ggap = 330, 108, 12
    ly = 330
    for i in range(10):
        x = gx + i * (gw + ggap)
        p.append(text(x + gw / 2, ly - 64, f'{i + 1}', 20, ERA[STAGES[i]["era"]], "700", "middle"))
        p.append(text(x + gw / 2, ly - 38, STAGES[i]["name"], 15, INK2, "400", "middle"))
    for li, (name, sub, weights, col) in enumerate(lanes):
        y = ly + li * 130
        p.append(paper_card(64, y, 1506, 114, tape_specs=[(64, 0, li % 3, -10)] if li == 0 else [(1506 - 60, 112, (li + 1) % 3, 9)]))
        p.append(text(88, y + 44, name, 24, col, "700"))
        p.append(text(88, y + 76, sub, 14, INK2))
        for i, wgt in enumerate(weights):
            x = gx + i * (gw + ggap)
            c = ERA[STAGES[i]["era"]]
            op = "0.85" if wgt >= 0.8 else ("0.40" if wgt >= 0.4 else "0.16")
            p.append(rect(x, y + 15, gw, 84, c, "#3A3A3A22", rx=6, sw=1, op=op))
            tcol = "#FFFFFF" if wgt >= 0.8 else (INK if wgt >= 0.4 else "#8A8F7A")
            lab = "重" if wgt >= 0.8 else ("中" if wgt >= 0.4 else "轻")
            p.append(text(x + gw / 2, y + 58, lab, 21, tcol, "700", "middle"))
    my = 752
    ys_mid = [ly + li * 130 + 57 for li in range(3)]
    for ym in ys_mid:
        p.append(doodle_arrow(1578, ym, 1622, my + 20, INK2, 1.6, 4))
    p.append(paper_card(64, my, 1586, 82, tape_specs=[(120, 0, 1, -8), (1586 - 130, 80, 2, 8)]))
    p.append(text(96, my + 32, "共用十阶主干", 21, INK, "700"))
    p.append(text(96 + tw("共用十阶主干", 21) + 18, my + 33, "①立志 → ②建图 → ③拆解 → ④编码 → ⑤检索 → ⑥间隔 → ⑦精练 → ⑧实战 → ⑨教学 → ⑩维护", 17, "#4A5160"))
    p.append(text(96, my + 60, "换乘：目标变化就换轨；考试结束降级为低剂量维护，防止技能衰减 [C28]", 14, INK2))
    lgx = 1230
    for wgt, lab_ in [("0.85", "重"), ("0.40", "中"), ("0.16", "轻")]:
        p.append(rect(lgx, my + 28, 16, 16, INK, None, rx=3, op=wgt))
        p.append(text(lgx + 24, my + 36, lab_, 14, INK2))
        lgx += 58
    p.append(text(lgx + 2, my + 36, "（底色调 = 所属纪）", 13, "#8A8F7A"))
    p.append(text(W / 2, H - 18, "权重为经验值、非实验结论；方法与证据见 docs/stages 与 docs/evidence.md", 14, "#8A8F7A", "400", "middle"))
    p.append("</svg>")
    return "".join(p)


# ---------------------------------------------------------------- spacing
def build_spacing():
    W, H = 1560, 920
    p = [svg_open(W, H, "间隔：遗忘曲线与复习调度（复古笔记本风）")]
    p.append(deco_page(W, H, 4, 8))
    p.append(rect(64, 96, 600, 46, YELLOW, None, rx=8, op="0.5"))
    p.append(text(78, 120, "间隔 · 在遗忘边缘复习", 36, INK, "700"))
    p.append(text(78, 168, "遗忘不是 bug；卡在 R≈0.9 复习，收益/成本最优", 18, INK2))
    # 左：坐标纸卡片
    ox, oy, pw, ph = 150, 300, 700, 360
    p.append(paper_card(96, 220, 830, 560, tape_specs=[(120, 0, 0, -8), (830 - 130, 558, 2, 8)]))
    p.append(text(116, 252, "R(t) = e^(−t/S)：每次复习后稳定度 S 增大 → 曲线更平、间隔更长（纵轴局部放大 0.8–1.0）", 14, "#4A5160", "500"))
    gx0, gy0, gx1, gy1 = ox, oy, ox + pw, oy + ph
    for gx in range(int(gx0), int(gx1) + 1, 35):
        p.append(f'<line x1="{gx}" y1="{gy0}" x2="{gx}" y2="{gy1}" stroke="#E1E9F4" stroke-width="1"/>')
    for gy in range(int(gy0), int(gy1) + 1, 35):
        p.append(f'<line x1="{gx0}" y1="{gy}" x2="{gx1}" y2="{gy}" stroke="#E1E9F4" stroke-width="1"/>')
    p.append(f'<line x1="{gx0}" y1="{gy1}" x2="{gx1}" y2="{gy1}" stroke="{INK}" stroke-width="2"/>')
    p.append(f'<line x1="{gx0}" y1="{gy0}" x2="{gx0}" y2="{gy1}" stroke="{INK}" stroke-width="2"/>')
    p.append(text(ox + pw / 2, oy + ph + 46, "时间（复习间隔逐次增大）→", 16, INK2, "400", "middle"))
    T_MAX = 15.0
    def X(t):
        return ox + (t / T_MAX) * pw
    def Y(r):
        return oy + ph * (1 - (r - 0.8) / 0.2)
    p.append(text(ox - 36, oy + 10, "R", 15, INK2, "600"))
    for tick in (1.0, 0.9, 0.8):
        p.append(text(ox - 12, Y(tick), f"{tick:.1f}", 14, INK2, "400", "end"))
    y09 = Y(0.9)
    p.append(f'<line x1="{ox}" y1="{y09:.1f}" x2="{ox + pw}" y2="{y09:.1f}" stroke="{RED}" stroke-width="1.4" stroke-dasharray="8 6" opacity="0.7"/>')
    p.append(text(ox + pw - 8, y09 - 16, "R ≈ 0.9：复习触发线", 15, RED, "600", "end"))
    times = [0.0, 1.0, 3.0, 7.0, 15.0]
    seg_colors = ["#2E6E8E", "#3E7C59", "#6E4E9E", "#B04A5A"]
    for k in range(4):
        t0, t1 = times[k], times[k + 1]
        S = (t1 - t0) / 0.10536
        n = 64
        pts = []
        for i in range(n + 1):
            tt = t0 + (t1 - t0) * i / n
            pts.append(f"{X(tt):.1f},{Y(math.exp(-(tt - t0) / S)):.1f}")
        p.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{seg_colors[k]}" stroke-width="3.4" stroke-linecap="round"/>')
        if k > 0:
            p.append(f'<line x1="{X(t0):.1f}" y1="{Y(1.0):.1f}" x2="{X(t0):.1f}" y2="{y09:.1f}" stroke="{seg_colors[k]}" stroke-width="2" opacity="0.5"/>')
        tmid = (t0 + t1) / 2
        p.append(text(X(tmid), Y(1.0) + 22, f"S{k+1}", 13, seg_colors[k], "600", "middle"))
    p.append(f'<circle cx="{X(0):.1f}" cy="{Y(1.0):.1f}" r="8" fill="{RED}" stroke="{CARD}" stroke-width="3"/>')
    p.append(text(X(0) + 14, Y(1.0) - 16, "R=1.0", 12, INK2))
    for k, tt in enumerate(times[1:]):
        px_, py_ = X(tt), y09
        if k == 3:
            p.append(f'<circle cx="{px_:.1f}" cy="{py_:.1f}" r="8" fill="{CARD}" stroke="{RED}" stroke-width="2.4" opacity="0.55"/>')
        else:
            p.append(f'<circle cx="{px_:.1f}" cy="{py_:.1f}" r="8" fill="{RED}" stroke="{CARD}" stroke-width="3"/>')
        lab = ["复习①", "复习②", "复习③", "下次复习"][k]
        p.append(f'<line x1="{px_:.1f}" y1="{py_ + 12:.1f}" x2="{px_:.1f}" y2="524" stroke="{RED}" stroke-width="1" opacity="0.3"/>')
        p.append(text(px_ + (10 if k == 0 else 0), 542, lab, 15, "#A03028" if k == 3 else RED, "600", "middle"))
    p.append(text(X(0) - 10, 542, "学习", 15, RED, "600", "middle"))
    p.append(f'<line x1="{X(0):.1f}" y1="{Y(1.0) + 12:.1f}" x2="{X(0):.1f}" y2="524" stroke="{RED}" stroke-width="1" opacity="0.3"/>')
    p.append(text(116, 806, "口径：最佳间隔 ≈ 目标保持期的 10–20% [C06]；254 项实验支持分布练习 [C04]", 14, INK2))
    p.append(text(W / 2, H - 18, "间隔 = 把时间变成盟友：复习点由算法安排，你只负责检索与评分", 14, "#8A8F7A", "400", "middle"))
    p.append("</svg>")
    return "".join(p)


# ---------------------------------------------------------------- loop
def build_loop():
    W, H = 1440, 940
    p = [svg_open(W, H, "刻意练习闭环：定靶-练-测-诊-修（复古笔记本风）")]
    p.append(deco_page(W, H, 5, 8))
    p.append(rect(64, 96, 560, 46, YELLOW, None, rx=8, op="0.5"))
    p.append(text(78, 120, "精练 · 刻意练习闭环", 36, INK, "700"))
    p.append(text(78, 168, "无反馈 = 无精练：每一次循环都要闭合", 18, INK2))
    cx, cy, R = 420, 540, 240
    nodes = [("定靶", "选一个子技能", 0), ("全神练", "在能力边缘", 1), ("即时测", "证据 > 感觉", 2),
             ("诊断", "根因分类", 3), ("修正再练", "针对性重练", 4)]
    for i, (t1, t2, e) in enumerate(nodes):
        ang = 90 - i * 72
        nx, ny = polar(cx, cy, R, ang)
        col = ERA[e]
        p.append(f'<circle cx="{nx:.0f}" cy="{ny:.0f}" r="64" fill="{CARD}" stroke="{col}" stroke-width="2.4"/>')
        p.append(f'<circle cx="{nx+2:.0f}" cy="{ny+1:.0f}" r="57" fill="none" stroke="{col}" stroke-width="0.9" opacity="0.45"/>')
        p.append(text(nx, ny - 10, t1, 21, INK, "700", "middle"))
        p.append(text(nx, ny + 16, t2, 13, INK2, "400", "middle"))
        s_ang, e_ang = ang - 26, ang - 72 + 26
        sx_, sy_ = polar(cx, cy, R, s_ang)
        ex_, ey_ = polar(cx, cy, R, e_ang)
        ang_t = math.atan2(ey_ - sy_, ex_ - sx_) if False else 0
        # 手绘弧线 + 手绘箭头
        mx_, my_ = polar(cx, cy, R + 14, (s_ang + e_ang) / 2)
        hx1 = ex_ - 12 * math.cos(math.radians(30)); hy1 = ey_ - 12 * math.sin(math.radians(30))
        p.append(f'<path d="M {sx_:.0f} {sy_:.0f} A {R} {R} 0 0 1 {ex_:.0f} {ey_:.0f}" fill="none" stroke="{col}" stroke-width="2.4" opacity="0.8" stroke-linecap="round"/>')
        a_head = math.atan2(ey_ - my_, ex_ - mx_)
        for da in (152, -152):
            hhx = ex_ + 12 * math.cos(a_head + math.radians(da)); hhy = ey_ + 12 * math.sin(a_head + math.radians(da))
            p.append(f'<line x1="{ex_:.0f}" y1="{ey_:.0f}" x2="{hhx:.0f}" y2="{hhy:.0f}" stroke="{col}" stroke-width="2.2" stroke-linecap="round"/>')
    p.append(stamp(cx, cy, 96, "闭环", -6, BLUE, "#FFFFFF", None))
    p.append(text(cx, cy + 78, "缺一环 = 原地踏步", 14, INK2, "400", "middle"))

    rx0 = 800
    p.append(paper_card(rx0, 150, 580, 236, tape_specs=[(90, 0, 0, -9)]))
    p.append(text(rx0 + 24, 186, "三速反馈", 22, INK, "700"))
    fr = [("即时（每个动作）", "对答案 / 引擎 / 导师批注", "#2E6E8E"), ("每日（日志复盘）", "错题日志 + 根因分类", "#C97A3D"),
          ("每周（教练/检视）", "周检视 + 高手示范 [C44]", "#6E4E9E")]
    for i, (t1, t2, col) in enumerate(fr):
        yy = 228 + i * 50
        p.append(f'<circle cx="{rx0 + 36}" cy="{yy}" r="7" fill="{col}"/>')
        p.append(text(rx0 + 54, yy, t1, 17, INK, "600"))
        p.append(text(rx0 + 54 + tw(t1, 17) + 12, yy + 1, t2, 14, INK2))
    p.append(text(rx0 + 24, 368, "具体、可行动、对事不对人；约 1/3 的反馈会反噬 [C46][C47]", 14, "#B06A2A"))
    ry1 = 420
    p.append(paper_card(rx0, ry1, 580, 296, tape_specs=[(120, 0, 2, 10), (580 - 120, 294, 1, -8)]))
    p.append(text(rx0 + 24, ry1 + 34, "错误日志（示例结构）", 21, INK, "700"))
    cols = [("日期", 24), ("错因类型", 92), ("修正动作", 208), ("复测", 430)]
    p.append(f'<line x1="{rx0+18}" y1="{ry1+58}" x2="{rx0+562}" y2="{ry1+58}" stroke="{INK}" stroke-width="1.4"/>')
    for h_, hx in cols:
        p.append(text(rx0 + hx, ry1 + 74, h_, 14, INK2, "600"))
    rows = [("10-01", "概念错", "重学前置概念，画反例", "10-04 ✓"),
            ("10-02", "程序错", "慢速分解，重练 2 组", "10-05 重练"),
            ("10-03", "粗心", "检查清单 + 限时 3 题", "10-06 ✓")]
    for i, r_ in enumerate(rows):
        yy = ry1 + 112 + i * 46
        p.append(f'<line x1="{rx0+18}" y1="{yy+22}" x2="{rx0+562}" y2="{yy+22}" stroke="{RULE}" stroke-width="1.2"/>')
        for cell, hx in zip(r_, [c[1] for c in cols]):
            p.append(text(rx0 + hx, yy, cell, 14, "#454C59"))
    p.append(text(rx0 + 24, ry1 + 258, "根因分类：概念错｜程序错｜粗心｜记忆缺失 —— 不同根因，不同药方", 14, INK2))
    p.append(text(rx0 + 24, ry1 + 282, "先自己提交版本，再请 AI 挑错（护栏用法）[C56]", 14, BLUE))
    p.append(text(W / 2, H - 18, "刻意练习 = 明确子目标 × 全神贯注 × 能力边缘 × 即时反馈与修正 [C31]", 14, "#8A8F7A", "400", "middle"))
    p.append("</svg>")
    return "".join(p)


# ---------------------------------------------------------------- mark & logo
def build_mark():
    S = 260
    p = [svg_open(S, S, "伏羲框架标志（复古笔记本风）")]
    cx, cy, R = 130, 130, 86
    # 手绘双圈
    p.append(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="{INK}" stroke-width="3"/>')
    p.append(f'<circle cx="{cx+2}" cy="{cy+1}" r="{R-5}" fill="none" stroke="{INK}" stroke-width="1" opacity="0.35"/>')
    p.append(f'<circle cx="{cx}" cy="{cy}" r="{R-30}" fill="none" stroke="{BLUE}" stroke-width="1.6" opacity="0.7"/>')
    pts = []
    for i in range(10):
        ang = 90 - i * 36
        x, y = polar(cx, cy, R, ang)
        pts.append((x, y, ERA[STAGES[i]["era"]]))
    for i, (x, y, col) in enumerate(pts):
        x2, y2, _ = pts[(i + 1) % 10]
        p.append(f'<line x1="{x:.0f}" y1="{y:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="{col}" stroke-width="1.6" opacity="0.6"/>')
    for x, y, col in pts:
        p.append(f'<line x1="{x:.0f}" y1="{y:.0f}" x2="{cx}" y2="{cy}" stroke="{INK}" stroke-width="1" opacity="0.3"/>')
        p.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="9.5" fill="{col}" stroke="{PAPER}" stroke-width="2"/>')
    # 中心绳结（红）
    k = 30
    p.append(f'<g transform="rotate(-8 {cx} {cy})">'
             f'<rect x="{cx-k/2}" y="{cy-k/2}" width="{k}" height="{k}" fill="{RED}" rx="6"/>'
             f'<rect x="{cx-k/2+4}" y="{cy-k/2+4}" width="{k-8}" height="{k-8}" fill="none" stroke="{PAPER}" stroke-width="1.2" opacity="0.85"/>'
             f'<line x1="{cx-k/2}" y1="{cy}" x2="{cx+k/2}" y2="{cy}" stroke="{PAPER}" stroke-width="1.6" opacity="0.85"/>'
             f'<line x1="{cx}" y1="{cy-k/2}" x2="{cx}" y2="{cy+k/2}" stroke="{PAPER}" stroke-width="1.6" opacity="0.85"/>'
             f'</g>')
    p.append("</svg>")
    return "".join(p)


def build_logo():
    # 横排组合标（图标 + 字标），用于 README 居中头部与站点
    W, H = 1280, 360
    p = [svg_open(W, H, "伏羲框架 · LOGO")]
    # 图标
    cx, cy, R = 190, 180, 128
    p.append(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="{CARD}" stroke="{INK}" stroke-width="4"/>')
    p.append(f'<circle cx="{cx+2}" cy="{cy+2}" r="{R-7}" fill="none" stroke="{INK}" stroke-width="1.2" opacity="0.35"/>')
    p.append(f'<circle cx="{cx}" cy="{cy}" r="{R-46}" fill="none" stroke="{BLUE}" stroke-width="2" opacity="0.65"/>')
    pts = []
    for i in range(10):
        ang = 90 - i * 36
        x, y = polar(cx, cy, R, ang)
        pts.append((x, y, ERA[STAGES[i]["era"]]))
    for i, (x, y, col) in enumerate(pts):
        x2, y2, _ = pts[(i + 1) % 10]
        p.append(f'<line x1="{x:.0f}" y1="{y:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="{col}" stroke-width="2.2" opacity="0.6"/>')
        p.append(f'<line x1="{x:.0f}" y1="{y:.0f}" x2="{cx}" y2="{cy}" stroke="{INK}" stroke-width="1.4" opacity="0.28"/>')
    for x, y, col in pts:
        p.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="13" fill="{col}" stroke="{CARD}" stroke-width="3"/>')
    k = 74
    p.append(f'<g transform="rotate(-8 {cx} {cy})">'
             f'<rect x="{cx-k/2}" y="{cy-k/2}" width="{k}" height="{k}" fill="none" stroke="{RED}" stroke-width="5" rx="10"/>'
             f'<rect x="{cx-k/2+8}" y="{cy-k/2+8}" width="{k-16}" height="{k-16}" fill="none" stroke="{RED}" stroke-width="1.6" opacity="0.8" rx="7"/>'
             f'<text x="{cx}" y="{cy+2}" font-size="30" fill="{RED}" font-weight="800" text-anchor="middle" dominant-baseline="middle" font-family="{FF}">伏羲</text>'
             f'</g>')
    # 字标（放大 + 浅色描边，深色背景同样可读）
    def logo_text(x, y, s, size, fill, weight):
        return (f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" font-weight="{weight}" '
                f'font-family="{FF}" dominant-baseline="middle" stroke="#FFFDF6" '
                f'stroke-width="{size * 0.10:.1f}" stroke-linejoin="round" paint-order="stroke">{esc(s)}</text>')
    p.append(logo_text(392, 150, "伏羲框架", 116, INK, "700"))
    p.append(rect(398, 218, 372, 13, YELLOW, None, rx=5, op="0.8"))
    p.append(logo_text(392, 262, "万物皆可学 · Everything Can Be Learned", 32, "#3A4048", "600"))
    p.append(logo_text(392, 312, "十阶时间线 × 证据分级 × 开源工具链", 25, "#4A5160", "500"))
    p.append("</svg>")
    return "".join(p)



# ---------------------------------------------------------------- expand / longevity / future
def _card(x, y, w, h, tapes=None):
    return paper_card(x, y, w, h, tape_specs=tapes or [(30, 0, 1, -10)])

def build_expand():
    W, H = 1560, 880
    p = [svg_open(W, H, "拓界篇 · 五大赛道（复古笔记本风）")]
    p.append(deco_page(W, H, 6, 8))
    p.append(rect(58, 92, 620, 78, YELLOW, None, rx=8, op="0.5"))
    p.append(text(78, 128, "拓界篇 · 五大赛道", 44, INK, "700"))
    p.append(text(80, 200, "十阶之后：从学到创造 —— 每条赛道都有自己的方法论与证据体系", 19, INK2))
    p.append(stamp(W - 150, 150, 116, "拓界", -8, RED, "#FFFFFF", "#C0392B"))
    courses = [
        ("科研", "Research", "把未知变成公共知识", ["无知清单", "四大矿脉", "证伪优先", "立新理论"], ERA[0]),
        ("创业", "Venture", "把创造变成产品与组织", ["Mom Test 访谈", "MVP 证伪假设", "PMF 看留存", "可承受损失"], ERA[3]),
        ("人际", "Relate", "把关系建模与经营", ["依恋四类型", "弱连接机会", "互惠博弈", "修复尝试"], ERA[2]),
        ("长寿", "Longevity", "把身体变成基础设施", ["证据分级表", "运动睡眠社交", "慢病管理", "拒绝补剂营销"], ERA[1]),
        ("未来", "Futures", "把地图更新到 2045", ["超级预测", "前沿雷达", "情景规划", "无后悔动作"], ERA[4]),
    ]
    cw, gap, x0, y0 = 278, 14, 58, 240
    for i, (name, en, line, keys, col) in enumerate(courses):
        cx = x0 + i * (cw + gap)
        p.append(_card(cx, y0, cw, 500, [(40, 0, i % 5, -12), (cw - 40, 2, i % 5, 10)]))
        p.append(hand_circle(cx + 46, y0 + 52, 24, col))
        p.append(text(cx + 46, y0 + 53, str(i + 1), 22, col, "700", "middle"))
        p.append(text(cx + 30, y0 + 112, name, 34, INK, "700"))
        p.append(text(cx + 30, y0 + 146, en, 15, INK2, ls="1"))
        p.append(text(cx + 30, y0 + 192, line, 16, "#454C59"))
        for j, k in enumerate(keys):
            p.append(f'<circle cx="{cx+38}" cy="{y0+250+j*48}" r="6" fill="{col}"/>')
            p.append(text(cx + 56, y0 + 251 + j * 48, k, 18, INK, "500"))
        p.append(text(cx + 30, y0 + 476, "详见 docs/expand/", 13, "#8A8F7A"))
    p.append(paper_card(58, 780, W - 120, 62))
    p.append(text(96, 812, "五赛道共用一个创造循环：无知 → 问题 → 实验 → 创造 → 传播（科研造知识 · 创业造价值 · 人际造信任 · 长寿保载体 · 未来定方向）", 18, "#454C59", "500"))
    p.append("</svg>")
    return "".join(p)

def build_longevity():
    W, H = 1560, 900
    p = [svg_open(W, H, "长寿 · 证据分级（复古笔记本风）")]
    p.append(deco_page(W, H, 7, 8))
    p.append(rect(58, 92, 640, 78, YELLOW, None, rx=8, op="0.5"))
    p.append(text(78, 128, "长寿 · 证据分级与关键数字", 42, INK, "700"))
    p.append(text(80, 200, "把筹码押在 A 级因素上：不伤害 × 运动 × 睡眠 × 饮食 × 社交", 19, INK2))
    rows = [
        ("不吸烟", "20 世纪最大单项寿命增益", "A", 470),
        ("运动：150 分/周 + 力量 2 次", "全因死亡风险 −30~40%", "A", 470),
        ("睡眠 7–9 小时（规律）", "短睡（<6h）死亡风险 +12% 量级", "A", 470),
        ("地中海饮食", "PREDIMED RCT：心血管事件显著下降", "A", 470),
        ("社交连接", "存活率 +50% 量级（148 研究）", "A", 470),
        ("乐观与意义感", "高乐观组寿命更长（队列）", "B", 300),
        ("限时进食 / 间歇禁食", "收益主要来自总热量", "B", 300),
        ("「蓝区」极端长寿叙事", "出生记录质量受质疑", "C", 165),
        ("抗衰补剂（NAD+ 等）", "无人体硬终点证据", "C", 165),
        ("换血 / 干细胞注射", "无证据 + 真实风险", "D", 80),
    ]
    col = {"A": "#3E7C59", "B": "#2F5496", "C": "#C97A3D", "D": "#C0392B"}
    y = 268
    for name, note, g, bw in rows:
        p.append(text(400, y + 16, name, 18, INK, "600", "end"))
        p.append(rect(420, y, bw, 26, col[g], "#3A3A3A22", rx=6, sw=1, op="0.85"))
        p.append(f'<circle cx="1060" cy="{y+13}" r="16" fill="{CARD}" stroke="{col[g]}" stroke-width="2.4"/>')
        p.append(text(1060, y + 14, g, 17, col[g], "700", "middle"))
        p.append(text(1096, y + 16, note, 16, "#454C59"))
        y += 52
    p.append(text(96, 820, "等级为本项目对证据的综合判断（详见 docs/expand/longevity.md）；抗衰补剂与换血疗法的 D 级是「别做」而不是「没看到」", 14, "#8A8F7A"))
    p.append("</svg>")
    return "".join(p)

def build_future():
    W, H = 1560, 920
    p = [svg_open(W, H, "未来纪元 · 前沿科学雷达与宏观趋势（复古笔记本风）")]
    p.append(deco_page(W, H, 8, 8))
    p.append(rect(58, 92, 700, 78, YELLOW, None, rx=8, op="0.5"))
    p.append(text(78, 128, "未来纪元 · 前沿科学雷达 × 宏观趋势", 40, INK, "700"))
    p.append(text(80, 200, "先学会判断预测（超级预测 / 情景 / 预测市场），再读雷达与趋势 —— 每季度更新", 19, INK2))
    fields = [
        ("人工智能", "Stanford AI Index [C144]", 4, ERA[0]),
        ("生物技术（CRISPR）", "2020 诺贝尔化学奖 [C145]", 3, ERA[2]),
        ("能源（聚变）", "NIF 点火净增益 [C146]", 2, ERA[3]),
        ("健康老龄化", "WHO 健康老龄化十年 [C150]", 3, ERA[1]),
        ("气候与地球系统", "IPCC AR6 综合报告 [C148]", 4, ERA[4]),
        ("空间与先进制造", "观察位：追踪 arXiv / 行业年报", 1, ERA[4]),
    ]
    cw, ch, gap = 466, 148, 12
    for i, (name, src, dots, col) in enumerate(fields):
        cx = 58 + (i % 3) * (cw + gap)
        cy = 236 + (i // 3) * (ch + gap)
        p.append(_card(cx, cy, cw, ch, [(50, 0, i % 5, -9)]))
        p.append(text(cx + 26, cy + 42, name, 24, INK, "700"))
        for k in range(4):
            fill = col if k < dots else "#DDD6C6"
            p.append(f'<circle cx="{cx+34+k*26}" cy="{cy+78}" r="9" fill="{fill}"/>')
        p.append(text(cx + 26, cy + 116, src, 14, INK2))
    tb = 236 + 2 * (ch + gap) + 16
    trends = [
        ("人口：2080s 峰值 ~103 亿", "UN WPP 2024 [C147]", ERA[1]),
        ("气候：每 +0.5°C 风险台阶", "IPCC AR6 [C148]", ERA[4]),
        ("治理：竞争性共存", "NIC Global Trends 2040 [C149]", ERA[0]),
    ]
    tw = (W - 120 - 24) // 3
    for i, (line, src, col) in enumerate(trends):
        tx = 58 + i * (tw + 12)
        p.append(_card(tx, tb, tw, 108, [(60, 0, (i + 2) % 5, -8)]))
        p.append(text(tx + 24, tb + 40, line, 20, INK, "700"))
        p.append(text(tx + 24, tb + 76, src, 14, INK2))
    p.append(text(96, H - 66, "2×2 情景（AI 快慢 × 全球化/碎片化）→ 找无后悔动作：健康 · 技能 · 社交 · 现金缓冲", 17, "#454C59", "500"))
    p.append(text(96, H - 34, "详见 docs/expand/futures.md · 数据基线 ourworldindata.org · 成熟度四格为项目综合判断", 14, "#8A8F7A"))
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
        "fuxi-logo.svg": build_logo(),
        "fuxi-expand.svg": build_expand(),
        "fuxi-longevity.svg": build_longevity(),
        "fuxi-future.svg": build_future(),
    }
    for name, content in files.items():
        path = os.path.join(OUT, name)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"OK {path} ({len(content.encode('utf-8'))} bytes)")


if __name__ == "__main__":
    main()
