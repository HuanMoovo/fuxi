#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""人生时间线学习友链构建器 —— python generator/build_lifespan.py
按人生阶段（出生 → 老年）组织的学习友链目录；全部条目为 GitHub 开源项目并经 API 核验。
生成 docs/awesome-lifespan.md。环境变量：GITHUB_TOKEN、FUXI_PROXY。
"""
import os, json, sys, urllib.request, concurrent.futures as cf

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOKEN = os.environ.get("GITHUB_TOKEN", "")
PROXY = os.environ.get("FUXI_PROXY", "http://127.0.0.1:7897")
OP = urllib.request.build_opener(urllib.request.ProxyHandler({"https": PROXY, "http": PROXY}))
HDR = {"User-Agent": "fuxi-lifespan"}
if TOKEN:
    HDR["Authorization"] = "Bearer " + TOKEN

DATA = [
 ("0–3 岁 ｜ 婴幼儿期", "重点：真人对话、亲子共读、自由玩耍；让语言输入又多又暖。",
  "**此阶段几乎没有值得推荐的开源软件 —— 最好的「工具」是照护者本人。** 若一定要看，可把屏幕交给「听」而不是「看」。",
  "地基未开始（可先读 [第 1 阶 · 立志](./stages/01-orient.md) 的「环境设计」一节）", []),
 ("3–6 岁 ｜ 幼儿期", "重点：玩中学、前读写与数感、规则类游戏。",
  "屏幕时间受控（WHO 建议 3-4 岁 ≤1 小时/天，越少越好），优先亲子共玩。",
  "→ [② 建图](./stages/02-map.md) · [④ 编码](./stages/04-encode.md)（以游戏与实物为主）",
  [("GCompris", "KDE/gcompris", "2-10 岁互动益智活动合集（离线）"),
   ("Sugar", "sugarlabs/sugar", "OLPC 儿童学习桌面环境"),
   ("Kolibri", "learningequality/kolibri", "离线 K-12 课程库（低带宽地区广泛使用）")]),
 ("6–12 岁 ｜ 儿童期", "重点：读写算打底、好奇心保护、第一次「做成一个项目」。",
  "编程启蒙与汉字书写都可以从图形化 / 动画化工具开始。",
  "→ [③ 拆解](./stages/03-decompose.md) · [⑦ 精练](./stages/07-drill.md)",
  [("Blockly", "RaspberryPiFoundation/blockly", "积木式编程（教学标准件）"),
   ("Scratch GUI", "scratchfoundation/scratch-gui", "Scratch 图形化编程（作品社区）"),
   ("Code.org", "code-dot-org/code-dot-org", "K-12 计算机科学课程平台"),
   ("Hanzi Writer", "chanind/hanzi-writer", "汉字笔顺动画练习")]),
 ("12–18 岁 ｜ 少年期", "重点：学习方法升级（检索练习/间隔重复）、编程与学科入门、第一次公开作品。",
  "此阶段最大的杠杆是「学习方法的更换」，而不是刷更多题。",
  "→ [⑤ 检索](./stages/05-retrieve.md) · [⑥ 间隔](./stages/06-space.md)",
  [("Hello 算法", "krahets/hello-algo", "动画图解数据结构与算法（中文）"),
   ("freeCodeCamp", "freeCodeCamp/freeCodeCamp", "免费交互式编程课程"),
   ("Python-100-Days", "jackfrued/Python-100-Days", "Python 百日成体系教程（中文）"),
   ("The Odin Project", "TheOdinProject/theodinproject", "项目式全栈 Web 课程"),
   ("3Blue1Brown 视频源码", "3b1b/videos", "数学可视化视频（配 Manim 复现）"),
   ("Manim", "ManimCommunity/manim", "复现/创作数学动画"),
   ("代码随想录", "youngyangyang04/leetcode-master", "刷题顺序与题解体系（中文）")]),
 ("18–25 岁 ｜ 青年期", "重点：系统化学科训练、向「专业」的第一跳、建立自己的知识库。",
  "大学的核心竞争力不是课表，而是「自学引擎 + 检索/间隔系统」。",
  "→ [② 建图](./stages/02-map.md) · [⑦ 精练](./stages/07-drill.md) · [⑧ 实战](./stages/08-apply.md)",
  [("cs-self-learning", "PKUFlyingPig/cs-self-learning", "计算机自学指南（中文）"),
   ("OSSU", "ossu/computer-science", "开源自修计算机学位"),
   ("The Missing Semester", "missing-semester/missing-semester", "MIT：工具链与命令行"),
   ("CS-Notes", "CyC2018/CS-Notes", "技术面试知识笔记"),
   ("d2l-zh", "d2l-ai/d2l-zh", "《动手学深度学习》（中文）"),
   ("nn-zero-to-hero", "karpathy/nn-zero-to-hero", "从零手搓神经网络"),
   ("Anki", "ankitects/anki", "间隔重复系统（大学四年最划算的工具）"),
   ("FSRS4Anki", "open-spaced-repetition/fsrs4anki", "现代化复习调度")]),
 ("25–40 岁 ｜ 成年初期", "重点：职业纵深与 T 型扩展、刻意练习、从「会」到「强」。",
  "此阶段时间碎片化，最忌「从头学一门新课」；要在真实项目里补洞。",
  "→ [⑦ 精练](./stages/07-drill.md) · [⑧ 实战](./stages/08-apply.md)（干中学为主）",
  [("Build Your Own X", "codecrafters-io/build-your-own-x", "从零手搓系统（干中学典范）"),
   ("K8s the Hard Way", "kelseyhightower/kubernetes-the-hard-way", "硬核方式掌握 Kubernetes"),
   ("System Design Primer", "donnemartin/system-design-primer", "系统设计入门"),
   ("nanoGPT", "karpathy/nanoGPT", "从零训练 GPT（能力边缘项目）"),
   ("LLMs-from-scratch", "rasbt/LLMs-from-scratch", "从零构建大模型"),
   ("Zotero", "zotero/zotero", "文献与资料管理（研究型工作的地基）"),
   ("Coding Interview University", "jwasham/coding-interview-university", "转岗/晋升的系统复习")]),
 ("40–60 岁 ｜ 中年期", "重点：整合、传承与输出 —— 把经验变成可复用资产。",
  "此阶段的复利来自「讲清楚」：教学是最强维护（[⑨ 教学](./stages/09-teach.md)）。",
  "→ [⑨ 教学](./stages/09-teach.md) · [⑩ 维护](./stages/10-maintain.md)",
  [("Logseq", "logseq/logseq", "双链知识库（经验资产化）"),
   ("Obsidian Spaced Repetition", "st3v3nmw/obsidian-spaced-repetition", "笔记内科学复习"),
   ("Quartz", "jackyzha0/quartz", "把笔记发布成网站"),
   ("Marp", "marp-team/marp", "Markdown 做幻灯片（讲课）"),
   ("Slidev", "slidevjs/slidev", "面向开发者的幻灯片"),
   ("Quarto", "quarto-dev/quarto-cli", "学术/技术出版系统"),
   ("MuseScore", "musescore/MuseScore", "开源制谱（兴趣即复利）")]),
 ("60+ 岁 ｜ 老年期", "重点：认知维护、持续丰富的生活、乐学不辍。",
  "诚实结论：认知训练对「近迁移」有限（[Salthouse 2009](<https://journals.sagepub.com/doi/full/10.1111/j.1539-6053.2009.01038.x>)）；但持续丰富的环境、社交与身体活动与更好的认知老化相关（[Hertzog et al. 2008](<https://journals.sagepub.com/doi/full/10.1111/j.1539-6053.2009.01034.x>)）。学新技能的真实价值在于「用进废退 + 生活意义」。",
  "→ [⑩ 维护](./stages/10-maintain.md)",
  [("KOReader", "koreader/koreader", "电纸书阅读（低负担长阅读）"),
   ("Calibre", "kovidgoyal/calibre", "电子书管理"),
   ("Lichess", "lichess-org/lila", "国际象棋（社交+认知活动）"),
   ("wger", "wger-project/wger", "健身/活动记录（身体是认知的底座）"),
   ("Memos", "usememos/memos", "轻量记录，保持输出习惯")]),
]

def main():
    slugs = sorted({sl for _, _, _, _, items in DATA for (_, sl, _) in items})
    info = {}
    def f(sl):
        try:
            with OP.open(urllib.request.Request("https://api.github.com/repos/" + sl, headers=HDR), timeout=30) as r:
                j = json.loads(r.read().decode())
            return (sl, j.get("stargazers_count", 0), j.get("full_name", sl))
        except Exception as e:
            return (sl, -1, sl)
    with cf.ThreadPoolExecutor(8) as ex:
        for sl, st, fn in ex.map(f, slugs):
            info[sl] = (st, fn)
    fails = [(sl, st) for sl, (st, fn) in info.items() if st < 0]
    print("FAIL:", fails if fails else "NONE")
    def fmt(n):
        if n >= 10000: return "★%.1f万" % (n / 10000)
        if n >= 1000: return "★%.1fk" % (n / 1000)
        return "★%d" % n
    import time as _t
    out = ["# 人生时间线 · 学习友链目录 Lifespan Learning Directory\n",
           "> 按**人生阶段**排序的学习友链：从出生到老年，每个阶段 = 学习重点 × 最值得的开源工具 × 对应十阶。全部条目经 GitHub API 核验（%s），可点击、可加载。\n>" % _t.strftime("%Y-%m-%d"),
           "> 姊妹篇：分类版 [学习友链目录](./awesome-learning.md)（2464 条）。年龄分段是启发式参考，不是硬性规定 —— 成年后决定学习的不是年龄，而是「目标 × 领域 × 资源」。\n",
           "> 本目录由 [`generator/build_lifespan.py`](https://github.com/HuanMoovo/fuxi/blob/main/generator/build_lifespan.py) 可复现生成。\n"]
    for title, focus, note, mapping, items in DATA:
        out.append("\n## " + title + "\n")
        out.append("> " + focus + "\n")
        out.append(note + "\n")
        out.append("\n对应十阶：" + mapping + "\n")
        for name, sl, why in items:
            st, fn = info[sl]
            if st < 0: continue
            out.append("- **[" + name + "](https://github.com/" + fn + ")** " + fmt(st) + " — " + why)
    out.append("\n---\n")
    out.append("\n> 下一站：当你触到人类知识的边界 —— 见 [第 11 阶 · 拓界](../docs/stages/11-expand.md)（从学会到创造）。\n")
    p = os.path.join(ROOT, "docs", "awesome-lifespan.md")
    with open(p, "w", encoding="utf-8") as fh:
        fh.write("\n".join(out) + "\n")
    print("WRITTEN:", p, "| entries:", sum(len(i) for _, _, _, _, i in { }.keys() or [] for i in [None])) if False else None
    print("done")

if __name__ == "__main__":
    main()
