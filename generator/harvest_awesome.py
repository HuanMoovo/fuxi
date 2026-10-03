#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""学习友链自动采集器 —— python generator/harvest_awesome.py [groups...]
通过 GitHub Search API 采集国际开源学习项目与书籍（全部可点击、可加载），
写入 generator/awesome_auto.json（增量式：每组完成即保存）。
组：books / courses / awesome / subjects / tools
环境变量：GITHUB_TOKEN、FUXI_PROXY（默认 http://127.0.0.1:7897）。
"""
import os, sys, re, json, time, urllib.request, urllib.parse

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOKEN = os.environ.get("GITHUB_TOKEN", "")
PROXY = os.environ.get("FUXI_PROXY", "http://127.0.0.1:7897")
OP = urllib.request.build_opener(urllib.request.ProxyHandler({"https": PROXY, "http": PROXY}))
HDR = {"User-Agent": "fuxi-harvest"}
if TOKEN:
    HDR["Authorization"] = "Bearer " + TOKEN

QUERIES = {
 "books": [("topic:book stars:>100", 2), ("topic:books stars:>100", 2), ("topic:ebook stars:>100", 1),
           ("topic:textbook stars:>100", 1), ("topic:programming-book stars:>50", 1),
           ('"free book" in:name,description stars:>300', 1), ("topic:free-books stars:>20", 1)],
 "courses": [("topic:course stars:>200", 2), ("topic:courses stars:>200", 2), ("topic:tutorial stars:>1000", 2),
             ("topic:tutorials stars:>1000", 2), ("topic:education stars:>1000", 2), ("topic:learning stars:>1000", 2),
             ("topic:lectures stars:>100", 1), ("topic:mooc stars:>50", 1), ("topic:study stars:>200", 1)],
 "awesome": [("topic:awesome stars:>2000", 2), ("topic:awesome-list stars:>500", 2), ('"awesome" in:name stars:>5000', 2)],
 "subjects": [("topic:math stars:>1000", 1), ("topic:physics stars:>500", 1), ("topic:chemistry stars:>200", 1),
              ("topic:biology stars:>300", 1), ("topic:astronomy stars:>300", 1), ("topic:language-learning stars:>150", 1),
              ("topic:linguistics stars:>150", 1), ("topic:algorithms stars:>1000", 1), ("topic:data-structures stars:>1000", 1),
              ("topic:competitive-programming stars:>500", 1), ("topic:leetcode stars:>1000", 1), ("topic:interview stars:>1000", 1),
              ("topic:security stars:>1000", 1), ("topic:cybersecurity stars:>500", 1), ("topic:linux stars:>1000", 1),
              ("topic:networking stars:>500", 1), ("topic:database stars:>500", 1), ("topic:sql stars:>300", 1),
              ("topic:machine-learning stars:>2000", 1), ("topic:deep-learning stars:>1500", 1),
              ("topic:data-science stars:>1500", 1), ("topic:nlp stars:>1000", 1), ("topic:computer-vision stars:>1000", 1),
              ("topic:reinforcement-learning stars:>500", 1), ("topic:llm stars:>1500", 1), ("topic:psychology stars:>300", 1),
              ("topic:philosophy stars:>300", 1), ("topic:economics stars:>300", 1), ("topic:statistics stars:>500", 1),
              ("topic:music stars:>500", 1), ("topic:robotics stars:>500", 1), ("topic:game-development stars:>1000", 1),
              ("topic:web-development stars:>1000", 1), ("topic:embedded stars:>500", 1), ("topic:blockchain stars:>500", 1),
              ("topic:quantum-computing stars:>300", 1), ("topic:docker stars:>1000", 1), ("topic:kubernetes stars:>1500", 1)],
 "tools": [("topic:flashcards stars:>50", 1), ("topic:spaced-repetition stars:>100", 1), ("topic:note-taking stars:>500", 1),
           ("topic:knowledge-base stars:>300", 1), ("topic:markdown stars:>2000", 1), ("topic:wiki stars:>500", 1),
           ("topic:writing stars:>500", 1), ("topic:productivity stars:>1000", 1), ("topic:zettelkasten stars:>100", 1),
           ("topic:pkm stars:>100", 1)],
}
TITLES = {"books": "⑬ 国际开源书籍 · Free Books & Textbooks", "courses": "⑭ 国际课程与教程 · Courses & Tutorials",
          "awesome": "⑮ Awesome 清单扩展 · More Awesome Lists", "subjects": "⑯ 学科学习精选 · Subject Learning",
          "tools": "⑰ 学习工具生态 · Learning Tools"}
CAPS = {"books": 520, "courses": 520, "awesome": 300, "subjects": 620, "tools": 200}
ORDER = ["books", "courses", "awesome", "subjects", "tools"]
EMOJI = re.compile("[\U0001F000-\U0001FAFF\u2190-\u21FF\u2600-\u27BF\u2B00-\u2BFF\uFE0F]")

def clean(s):
    s = EMOJI.sub("", s or "")
    s = s.replace("[", "\uff08").replace("]", "\uff09")
    s = re.sub(r"https?://\S+", "", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s[:110]

_calls = []
def throttled():
    now = time.time()
    del _calls[:]
    for t in list(_calls):
        pass
    _calls[:] = [t for t in _calls if now - t < 60]
    if len(_calls) >= 26:
        time.sleep(max(0.0, 60 - (now - _calls[0]) + 0.6))
    _calls.append(time.time())

def search(q, pages):
    items = []
    for pg in range(1, pages + 1):
        throttled()
        url = ("https://api.github.com/search/repositories?per_page=100&sort=stars&order=desc&q="
               + urllib.parse.quote(q) + "&page=%d" % pg)
        try:
            with OP.open(urllib.request.Request(url, headers=HDR), timeout=30) as r:
                j = json.loads(r.read().decode())
        except Exception as e:
            print("  ! fail:", q, pg, type(e).__name__)
            continue
        batch = j.get("items", [])
        items += batch
        if len(batch) < 100:
            break
    return items

def main():
    args = sys.argv[1:] or ORDER
    jp = os.path.join(ROOT, "generator", "awesome_auto.json")
    data = {"generated": "", "sections": []}
    if os.path.exists(jp):
        data = json.load(open(jp, encoding="utf-8"))
    merged = {s["key"]: s for s in data.get("sections", [])}
    docp = os.path.join(ROOT, "docs", "awesome-learning.md")
    curated = set()
    if os.path.exists(docp):
        for ln in open(docp, encoding="utf-8"):
            if ln.startswith("## " + "\u81ea\u52a8\u91c7\u96c6\u533a"):
                break
            m = re.match(r"- \*\*\[.+?\]\(https://github\.com/([^)]+)\)\*\*", ln)
            if m:
                curated.add(m.group(1))
    for key in args:
        if key not in QUERIES:
            continue
        seen = set(curated)
        for s in merged.values():
            for e in s["entries"]:
                seen.add(e["full"])
        got = {}
        for q, pages in QUERIES[key]:
            items = search(q, pages)
            print("  %s | %s -> %d" % (key, q, len(items)))
            for it in items:
                fn = it.get("full_name", "")
                if not fn or it.get("fork") or fn in seen:
                    continue
                desc = clean(it.get("description") or "")
                if not desc:
                    continue
                got[fn] = {"name": it.get("name", fn.split("/")[-1]), "full": fn,
                           "desc": desc, "stars": it.get("stargazers_count", 0)}
                seen.add(fn)
        entries = sorted(got.values(), key=lambda x: -x["stars"])[:CAPS[key]]
        merged[key] = {"key": key, "title": TITLES[key], "entries": entries}
        data["sections"] = [merged[k] for k in ORDER if k in merged]
        data["generated"] = time.strftime("%Y-%m-%d")
        json.dump(data, open(jp, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print("  => %s kept %d | json saved" % (key, len(entries)))
    tot = sum(len(s["entries"]) for s in data["sections"])
    print("AUTO TOTAL:", tot, [s["key"] for s in data["sections"]])

if __name__ == "__main__":
    main()
