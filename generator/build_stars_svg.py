# -*- coding: utf-8 -*-
"""由 data/stars.json 生成 docs/assets/fuxi-stars.svg（笔记本风 star 记录图）。"""
import os, json, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data", "stars.json")
OUT = os.path.join(ROOT, "docs", "assets", "fuxi-stars.svg")
PAPER, INK, INK2, RULE = "#F5EEDD", "#2B2B2B", "#6B7280", "#C9D6E8"
GOLD, GOLDF = "#C9971B", "#E4B95B"
W, H = 1240, 680

def el(s): return s
def load():
    return json.load(open(DATA, encoding="utf-8"))

def main():
    db = load()
    recs = db["records"]
    cur = recs[-1]["stars"] if recs else 0
    p = []
    A = p.append
    A('<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %d %d">' % (W, H, W, H))
    A('<rect width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
    for gy in range(60, H, 56):
        A('<line x1="0" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="1" opacity="0.55"/>' % (gy, W, gy, RULE))
    A('<text x="56" y="84" font-family="KaiTi,Microsoft YaHei" font-size="34" fill="%s" font-weight="700">Star 记录 · HuanMoovo/fuxi</text>' % INK)
    A('<text x="56" y="120" font-family="Microsoft YaHei" font-size="16" fill="%s">数据由 GitHub Actions 每日自动记录 · 生成器 generator/build_stars_svg.py</text>' % INK2)
    A('<text x="%d" y="96" text-anchor="end" font-family="Microsoft YaHei" font-size="60" fill="%s" font-weight="700">★ %d</text>' % (W - 56, GOLD, cur))
    A('<text x="%d" y="126" text-anchor="end" font-family="Microsoft YaHei" font-size="15" fill="%s">当前 star 总数</text>' % (W - 56, INK2))
    x0, x1, y0, y1 = 90, 1160, 220, 520
    A('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="2"/>' % (x0, y1, x1, y1, "#8A8F7A"))
    A('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="2"/>' % (x0, y0, x0, y1, "#8A8F7A"))
    maxv = max([r["stars"] for r in recs] + [1])
    dates = [datetime.date.fromisoformat(r["date"]) for r in recs]
    if len(recs) >= 2 and (dates[-1] - dates[0]).days > 0:
        span = (dates[-1] - dates[0]).days
        def X(d): return x0 + (d - dates[0]).days / span * (x1 - x0)
    else:
        def X(d): return x0
    def Y(v): return y1 - (v / maxv) * (y1 - y0 - 20)
    # 网格 y 标签
    for frac in (0, 0.5, 1):
        v = maxv * frac
        A('<line x1="%d" y1="%.0f" x2="%d" y2="%.0f" stroke="%s" stroke-width="1" opacity="0.5" stroke-dasharray="5 6"/>' % (x0, Y(v), x1, Y(v), RULE))
        A('<text x="%d" y="%.0f" text-anchor="end" font-family="Microsoft YaHei" font-size="14" fill="%s">%d</text>' % (x0 - 12, Y(v) + 5, INK2, round(v)))
    pts = [(X(dates[i]), Y(recs[i]["stars"])) for i in range(len(recs))]
    if len(pts) >= 2:
        A('<path d="M' + " L".join("%.1f %.1f" % pt for pt in pts) + '" fill="none" stroke="%s" stroke-width="3.5"/>' % GOLD)
        A('<path d="M%.1f %.1f %s L%.1f %.1f L%.1f %.1f Z" fill="%s" opacity="0.22"/>' % (pts[0][0], y1, " L".join("%.1f %.1f" % pt for pt in pts), pts[-1][0], y1, pts[0][0], y1, GOLDF))
    for pt in pts:
        A('<circle cx="%.1f" cy="%.1f" r="6" fill="%s"/>' % (pt[0], pt[1], GOLD))
    if len(pts) == 1:
        A('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-width="2" stroke-dasharray="6 8" opacity="0.6"/>' % (pts[0][0], pts[0][1], x1, pts[0][1], GOLD))
        A('<text x="%d" y="%.0f" text-anchor="end" font-family="Microsoft YaHei" font-size="16" fill="%s">持续记录中……每日自动更新</text>' % (x1, pts[0][1] - 16, INK2))
    # x 轴标签（最多4个）
    if dates:
        picks = sorted(set([0, len(dates) - 1, len(dates) // 2]))[:4]
        for i in picks:
            A('<text x="%.0f" y="%d" text-anchor="middle" font-family="Microsoft YaHei" font-size="14" fill="%s">%s</text>' % (X(dates[i]), y1 + 28, INK2, recs[i]["date"]))
    # 最近记录表
    ty = 570
    A('<text x="56" y="%d" font-family="KaiTi,Microsoft YaHei" font-size="20" fill="%s" font-weight="700">最近记录</text>' % (ty, INK))
    row = min(7, len(recs))
    show = recs[-row:]
    A('<text x="200" y="%d" font-family="Microsoft YaHei" font-size="15" fill="%s">日期</text>' % (ty, INK2))
    A('<text x="420" y="%d" font-family="Microsoft YaHei" font-size="15" fill="%s">★ stars</text>' % (ty, INK2))
    A('<text x="640" y="%d" font-family="Microsoft YaHei" font-size="15" fill="%s">变化</text>' % (ty, INK2))
    A('<text x="820" y="%d" font-family="Microsoft YaHei" font-size="15" fill="%s">forks</text>' % (ty, INK2))
    A('<line x1="56" y1="%d" x2="1060" y2="%d" stroke="%s" stroke-width="1.6"/>' % (ty + 10, ty + 10, "#8A8F7A"))
    for j, r in enumerate(show):
        yy = ty + 40 + j * 0
        pass
    # 平铺一行（最多7条，逗号分隔，避免多行溢出）
    cells = []
    for i, r in enumerate(show):
        prev = show[i - 1]["stars"] if i > 0 else (recs[len(recs) - row + i - 1]["stars"] if len(recs) - row + i - 1 >= 0 else r["stars"])
        delta = r["stars"] - (recs[recs.index(r) - 1]["stars"] if recs.index(r) > 0 else r["stars"])
        cells.append("%s · ★%d（%+d）· fork %d" % (r["date"][5:], r["stars"], delta, r["forks"]))
    A('<text x="56" y="%d" font-family="Microsoft YaHei" font-size="15" fill="%s">%s</text>' % (ty + 46, INK, "  ｜  ".join(cells)))
    A('<text x="56" y="%d" font-family="Microsoft YaHei" font-size="13" fill="%s">数据源：GitHub API（data/stars.json 原始记录，公开可审计）</text>' % (H - 26, INK2))
    A("</svg>")
    open(OUT, "w", encoding="utf-8").write("".join(p))
    print("OK:", OUT, len("".join(p)))

if __name__ == "__main__":
    main()
