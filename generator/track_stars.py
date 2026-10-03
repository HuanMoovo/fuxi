# -*- coding: utf-8 -*-
"""记录 HuanMoovo/fuxi 的 star / fork / watcher 数（每日由 Actions 运行）。
本地运行自动走 127.0.0.1:7897 代理；CI 环境直连。
"""
import os, json, sys, urllib.request, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data", "stars.json")
REPO = "HuanMoovo/fuxi"

def load():
    if os.path.exists(DATA):
        return json.load(open(DATA, encoding="utf-8"))
    return {"repo": REPO, "records": []}

def fetch():
    url = "https://api.github.com/repos/" + REPO
    headers = {"User-Agent": "fuxi-star-tracker", "Accept": "application/vnd.github+json"}
    tok = os.environ.get("GITHUB_TOKEN")
    if tok:
        headers["Authorization"] = "Bearer " + tok
    last_err = None
    for proxies in ({"https": "http://127.0.0.1:7897"}, {}):
        op = urllib.request.build_opener(urllib.request.ProxyHandler(proxies))
        try:
            with op.open(urllib.request.Request(url, headers=headers), timeout=15) as r:
                return json.loads(r.read().decode())
        except Exception as e:
            last_err = e
    raise SystemExit("fetch failed: %s" % last_err)

def main():
    d = fetch()
    today = datetime.datetime.utcnow().strftime("%Y-%m-%d")
    db = load()
    rec = {"date": today,
           "stars": d["stargazers_count"],
           "forks": d["forks_count"],
           "watchers": d["subscribers_count"]}
    recs = [r for r in db["records"] if r["date"] != today]
    recs.append(rec)
    recs.sort(key=lambda r: r["date"])
    db["repo"] = REPO
    db["updated"] = today
    db["records"] = recs
    os.makedirs(os.path.dirname(DATA), exist_ok=True)
    json.dump(db, open(DATA, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("recorded:", rec, "| total records:", len(recs))

if __name__ == "__main__":
    main()
