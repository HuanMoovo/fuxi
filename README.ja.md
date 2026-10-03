[简体中文](./README.md) ｜ [English](./README.en.md) ｜ **日本語**

<div align="center">

<a href="docs/assets/fuxi-logo.svg" target="_blank"><img src="docs/assets/fuxi-logo.svg" alt="伏羲フレームワーク · LOGO" width="560"></a>

# 伏羲フレームワーク · 万物は学べる

**The Fuxi Framework — Everything Can Be Learned**

「何かを学ぶ」を **5 つの時代・10 段階のタイムライン**に分解し、各段階に「**最適な方法 × エビデンス等級 × OSS ツール × 合格テスト**」を用意する。

**[十段階の詳細](https://github.com/HuanMoovo/fuxi/blob/main/docs/stages/01-orient.md)** · **[エビデンス集](./docs/evidence.md)** · **[参考文献（110+）](./docs/references.md)** · **[学習リンク集（2464）](./docs/awesome-learning.md)** · **[人生タイムライン](./docs/awesome-lifespan.md)** · **[開拓編・第 11 段階](./docs/stages/11-expand.md)** · **[オンラインサイト](https://HuanMoovo.github.io/fuxi/)**

</div>

## これは何か

- 学習を「根性」ではなく**工学**として扱う：全主張は検証可能、全数字に出典あり（[エビデンス集](./docs/evidence.md)：30 の結論＋[参考文献](./docs/references.md) 110+）。
- 図表はスクリプトで**再現可能**（[generator/build_svgs.py](./generator/build_svgs.py)）。
- 「学び方」だけでなく「学び終わった後」も対象：[開拓編・第 11 段階](./docs/stages/11-expand.md) —— 既存知識の限界に達したとき、未知を既知に変える方法（無知リスト・四大鉱脈・問題の陶冶・新奇予測・公開検証）。

## 十段階

| # | 段階 | 一言 |
|---|---|---|
| 1 | 立志 Orient | 「学びたい」を実行可能な契約に変える |
| 2 | 地図づくり Map | まず森を見る：領域地図を描く |
| 3 | 分解 Decompose | 一口サイズの原子まで分解する |
| 4 | 符号化 Encode | 例と説明を既存知識に織り込む |
| 5 | 想起 Retrieve | 本を閉じて、記憶から取り出す |
| 6 | 間隔 Space | 忘却の縁で科学的に復習する |
| 7 | 錬磨 Drill | 能力の縁でフィードバック付き反復 |
| 8 | 実践 Apply | 実物をやる、足りない分は後から補う |
| 9 | 教える Teach | 人に説明し、新場面へ転移させる |
| 10 | 維持 Maintain | 低頻度の手入れ、複利で増やす |

各段階の完全版（中国語）：[docs/stages](./docs/stages/)

## 三つのルート（[paths.md](./docs/paths.md)）

- **探索ルート** —— 目標なし・知りたいだけ：地図 → 分解 → 符号化 → 想起
- **実践ルート** —— 成果物あり：立志 → 分解 → 錬磨 → 実践
- **スプリントルート** —— 試験・締切厳守：立志 → 想起 → 間隔 → 錬磨

## エビデンス等級

全手法に等級を付与：**A 強 / B 中 / C 弱・条件付き / D 否定済み**（本プロジェクトの総合判断であり、公式ランクではない）。代表例：検索練習（テスト効果）＝1 週間後 約 80% vs 約 35%（想起 vs 再読）、間隔反復＝254 研究・最適間隔 ≈ 保持期間の 10–20%、FSRS＝2.2 億ログで +12.6%。数字の口径を含め [docs/evidence.md](./docs/evidence.md) に。

## AI 副操縦士プロトコル（七条・要約）

1. 順序鉄則：まず自分で産出 → AI に誤りを探させる；
2. 想起フェーズでは AI は出題と質問のみ、答えを求めない；
3. 役割：練習相手・試験官・反論者・初心者（代筆は禁止）；
4. AI が示す数値・引用は原典で核験；
5. 定期的に「AI なし遅延テスト」（撤退テスト）；
6. 省脳監査：思考を外注した工程を記録（そこが補習対象）；
7. ツールはローカル/OSS 優先（Ollama、llama.cpp）。

根拠：Bastani 2025（PNAS）· Fan 2025（BJET）· Kestin 2025（Sci Rep）。

## 始め方（30 分）

1. ルートを選ぶ（探索 / 実践 / スプリント）；
2. 「学習契約」を書く：検証可能な成果 3 つだけ；
3. 領域地図の下書きを描く：構造＞見た目；
4. Anki + FSRS にカードを 3 枚；
5. 明日から 25 分/日のリズム、1 週間後に白紙想起。

## リポジトリ構成

- `docs/` —— 全ドキュメント（stages/ 十段階 · evidence · references · awesome-learning（2464 リンク）· awesome-lifespan（人生タイムライン）…）
- `generator/` —— 図表と目録のビルドスクリプト（再現可能）
- `templates/` —— 学習契約・週次レビュー・誤り日誌などのテンプレート
- オンラインサイト：<https://HuanMoovo.github.io/fuxi/>（中文・English・日本語 切替対応）

## ライセンス

コード：MIT（[LICENSE](./LICENSE)）／ 文書・図表：CC BY 4.0（[LICENSE-DOCS.md](./LICENSE-DOCS.md)）

> 完全な内容・最新情報は [中国語版 README](./README.md) と [English README](./README.en.md) を正とします。
