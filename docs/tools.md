# 伏羲框架 · 学习工具目录（Tools）

> 另见：[**学习友链目录**](./awesome-learning.md) —— 248 个热门学习项目索引（11 大类，全部经核验）。

> 万物皆可学 · Everything Can Be Learned —— 十阶学习流程的开源工具链，逐链接核验。核验日期：2026-10-03。

收录标准有三条。一是开源或可免费使用优先：付费与订阅制工具只保留能明显提升某一阶效率的公认必备条目。二是与十阶流程有明确落点：每个工具都要能回答「它服务哪一阶、替代或增强什么动作」，无法对应到任何一阶动作的工具不收。三是避免死链：不收藏「以后可能有用」的地址，所有条目都经过实际访问核验。

核验方式与日期：2026-10-03 对每条地址发送 HTTP 请求并跟随跳转（curl -L），返回 200/301/302 等视为可访问并收录进正文；无法访问的条目（404 等）移入文末「待核」。条目若因访问频率限制（HTTP 429）未能最终确认，会在原处标注「限流，未最终确认」。链接状态会随时间变化，本页是核验时点的快照。

许可与条款声明：许可证与使用条款以各仓库为准。本目录只保证一件事——「链接在核验时点可达」；能否商用、能否再分发、署名要求如何，请自行核对目标仓库的 LICENSE 与官方文档。阶段编号（1–10）为使用建议，不是硬性规定；同一工具跨阶段复用是常态。

## 怎么读这一页

- 条目格式：`**名称** — 仓库地址 — 适用阶：N — 一句话用途`；多个阶段用「·」分隔。
- 适用阶编号：1 立志（Orient）、2 建图（Map）、3 拆解（Decompose）、4 编码（Encode）、5 检索（Retrieve）、6 间隔（Space）、7 精练（Drill）、8 实战（Apply）、9 教学（Teach）、10 维护（Maintain）；各阶详解见 `docs/stages/`。
- 选型原则：每阶先只上 1–2 件，跑通比配齐重要；工具服务于流程，反过来不成立。
- 收录范围：只收录与十阶动作直接相关的工具；评测、素材站与纯信息源不在本页。
- 状态：全部 60 条正文条目均于 2026-10-03 核验可访问。

## 核验统计

本次核验共 60 条链接：全部可访问（HTTP 200，核验日期 2026-10-03）。

| 类别 | 条目数 | 主要服务阶段 |
|------|--------|--------------|
| 记忆与间隔复习 | 13 | 5 · 6 · 10 |
| 笔记与知识库 | 7 | 2–4 · 9 · 10 |
| 绘图与可视化 | 5 | 2 · 4 · 9 |
| 课程与练习平台 | 15 | 2 · 4 · 7 · 8 |
| 语言学习 | 9 | 2 · 4 · 5 · 7 |
| 习惯与执行 | 4 | 1 · 7 · 10 |
| AI 学习助手 | 4 | 4 · 5 · 7 |
| 文献与引用 | 3 | 2 · 4 · 9 |
| 合计 | 60 | 全十阶均有落点 |

## 记忆与间隔复习

第 5 阶（检索）与第 6 阶（间隔）的主场：用间隔重复（spaced repetition）把「复习」变成可调度、可统计的系统；第 10 阶的低频维护也依赖这一组。

- **Anki** — https://github.com/ankitects/anki — 适用阶：5·6·10 — 桌面与移动端间隔重复标准客户端（内置 FSRS 调度）。
- **AnkiDroid** — https://github.com/ankidroid/Anki-Android — 适用阶：5·6 — Anki 的 Android 客户端，碎片时间复习。
- **FSRS4Anki** — https://github.com/open-spaced-repetition/fsrs4anki — 适用阶：6 — 在 Anki 中用上并调优 FSRS 调度器的集成仓库。
- **FSRS Helper** — https://github.com/open-spaced-repetition/fsrs4anki-helper — 适用阶：6 — 配套插件：参数优化、负载均衡与提前复习。
- **FSRS 算法说明库** — https://github.com/open-spaced-repetition/free-spaced-repetition-scheduler — 适用阶：6 — DSR 记忆模型的算法说明，想搞懂调度原理先读它。
- **fsrs-rs** — https://github.com/open-spaced-repetition/fsrs-rs — 适用阶：6 — FSRS 的 Rust 实现（含优化器），适合嵌入应用与本地训练。
- **ts-fsrs** — https://github.com/open-spaced-repetition/ts-fsrs — 适用阶：6 — FSRS 的 TypeScript 实现，用于 Web / Node 端调度。
- **py-fsrs** — https://github.com/open-spaced-repetition/py-fsrs — 适用阶：6 — FSRS 的 Python 实现，适合脚本与数据分析。
- **Awesome FSRS** — https://github.com/open-spaced-repetition/awesome-fsrs — 适用阶：6 — FSRS 生态索引：实现、工具与资料汇总。
- **org-fc** — https://github.com/l3kn/org-fc — 适用阶：5·6 — 在 Emacs org-mode 内做间隔重复。
- **Obsidian Spaced Repetition** — https://github.com/st3v3nmw/obsidian-spaced-repetition — 适用阶：5·6 — 把 Obsidian 笔记直接变成复习卡片，笔记与复习不分离。
- **AnkiConnect** — https://github.com/FooSoft/anki-connect — 适用阶：5·6 — Anki 的 HTTP 接口，供脚本自动化制卡、同步与统计。
- **genanki** — https://github.com/kerrickstaley/genanki — 适用阶：4·5 — 用 Python 生成 Anki 卡组，适合批量、程序化制卡。

*注：fsrs-rs、ts-fsrs、py-fsrs 已补充核验并收录于上方列表。*

## 笔记与知识库

第 2–4 阶的建图、拆解与编码主要发生在笔记系统里；第 9–10 阶的公开输出与维护也从这里长出来。先选一套用熟，再谈迁移。

- **Obsidian** — https://github.com/obsidianmd/obsidian-releases — 适用阶：2·3·4·5·10 — 本地优先的 Markdown 知识库；本仓库为官方桌面端发布页（桌面端免费、源码不开源），双向链接与插件生态是核心。
- **Logseq** — https://github.com/logseq/logseq — 适用阶：3·4·5·6·10 — 大纲式双向链接知识库，内置卡片式复习（SRS）。
- **Zettlr** — https://github.com/Zettlr/Zettlr — 适用阶：4 — 面向学术写作的 Markdown 编辑器，Zettelkasten 工作流友好。
- **SilverBullet** — https://github.com/silverbulletmd/silverbullet — 适用阶：4 — 可自托管的浏览器端 Markdown 笔记（页面 + 查询）。
- **Foam** — https://github.com/foambubble/foam — 适用阶：2·4 — 在 VS Code 里搭个人知识库（wikilink、关系图）。
- **Quartz** — https://github.com/jackyzha0/quartz — 适用阶：8·9·10 — 把 Markdown 笔记构建成静态网站的「数字花园」（digital garden）工具。
- **Xournal++** — https://github.com/xournalpp/xournalpp — 适用阶：4 — 手写笔记与 PDF 批注，适合推导过程与讲义。

## 绘图与可视化

第 2 阶建图的主力；第 4 阶双重编码（语言 + 图像）与第 9 阶讲稿配图也常用到。共同原则：图先服务于结构，再谈好看。

- **markmap** — https://github.com/markmap/markmap — 适用阶：2·3 — Markdown 大纲一键渲染成思维导图。
- **Excalidraw** — https://github.com/excalidraw/excalidraw — 适用阶：2·4 — 手绘风格白板，画概念图与知识结构。
- **draw.io** — https://github.com/jgraph/drawio — 适用阶：2 — 流程图与架构图工具，画领域结构与依赖顺序。
- **Mermaid** — https://github.com/mermaid-js/mermaid — 适用阶：2·9 — 用文本语法生成图表，可嵌入 Markdown 与讲稿。
- **tldraw** — https://github.com/tldraw/tldraw — 适用阶：2·4 — 无限画布白板，自由排布概念与素材。

## 课程与练习平台

第 7 阶精练与第 8 阶实战的练习场；部分平台兼作第 2 阶的素材源（课程大纲与路线图）。挑平台看两点：有没有反馈、能不能产出可展示的成果。

- **freeCodeCamp** — https://github.com/freeCodeCamp/freeCodeCamp — 适用阶：8 — 免费编程课程与认证，以项目练习为主。
- **Exercism** — https://github.com/exercism/exercism — 适用阶：7 — 编程练习平台，配真人导师反馈，反馈回路现成。
- **The Odin Project** — https://github.com/TheOdinProject/theodinproject — 适用阶：8 — 开源全栈课程，项目驱动。
- **roadmap.sh** — https://github.com/kamranahmedse/developer-roadmap — 适用阶：2 — 各技术方向的路线图合集，建图的现成底稿。
- **OSSU** — https://github.com/ossu/computer-science — 适用阶：2 — 计算机科学自学课程表（按依赖排序的样例）。
- **OpenStax** — https://github.com/openstax — 适用阶：2·4 — 免费开放教材项目（本链接为其 GitHub 组织页）。
- **Lean 4** — https://github.com/leanprover/lean4 — 适用阶：4·7 — 定理证明器：把数学推理写成可运行、可检查的代码。
- **Mathematics in Lean** — https://github.com/leanprover-community/mathematics_in_lean — 适用阶：4 — 用 Lean 4 学数学的开放教材。
- **lean4game** — https://github.com/leanprover-community/lean4game — 适用阶：7 — 把 Lean 证明做成游戏化关卡练习。
- **Lichess** — https://github.com/lichess-org/lila — 适用阶：8 — 开源在线国际象棋平台（对局、谜题与分析；本仓库为服务端代码）。
- **Stockfish** — https://github.com/official-stockfish/Stockfish — 适用阶：7 — 开源国际象棋引擎，用复盘找漏着。
- **KaTrain** — https://github.com/sanderland/katrain — 适用阶：7 — 围棋 AI 复盘训练工具（基于 KataGo）。
- **MuseScore** — https://github.com/musescore/MuseScore — 适用阶：4·7 — 乐谱制作与播放，练习时可对照比对。
- **Audacity** — https://github.com/audacity/audacity — 适用阶：7 — 录音与音频编辑，用录音自评建立即时反馈。
- **Blender** — https://github.com/blender/blender — 适用阶：8 — 三维创作套件，适合以完整作品驱动实战。

## 语言学习

第 4 阶编码与第 7 阶精练的语言专用工具链。核心思路：先保证可理解的输入，再把输入快速转成卡片，进入检索循环。

- **Yomitan** — https://github.com/yomidevs/yomitan — 适用阶：4·5 — 浏览器内即时词典（日语等），一键做词卡。
- **asbplayer** — https://github.com/killergerbah/asbplayer — 适用阶：4·7 — 用视频字幕学语言：字幕取词、导出制卡。
- **mpvacious** — https://github.com/Ajatt-Tools/mpvacious — 适用阶：4·5 — mpv 插件：从音视频截取句子（含音频）制卡。
- **GoldenDict-ng** — https://github.com/xiaoyifang/goldendict-ng — 适用阶：2·4 — 跨平台词典客户端，支持多种词典格式。
- **LanguageTool** — https://github.com/languagetool-org/languagetool — 适用阶：7 — 语法与写作检查，给出可执行的修改反馈。
- **Whisper** — https://github.com/openai/whisper — 适用阶：4·7 — 语音识别模型：把音频材料转成文本。
- **whisper.cpp** — https://github.com/ggml-org/whisper.cpp — 适用阶：4·7 — Whisper 的高效本地实现，可离线转写。
- **Argos Translate** — https://github.com/argosopentech/argos-translate — 适用阶：2·4 — 离线神经翻译库，辅助阅读外文材料。
- **LibreTranslate** — https://github.com/LibreTranslate/LibreTranslate — 适用阶：2·4 — 可自托管的翻译 API，支持离线部署。

## 习惯与执行

第 1 阶立志的时间与习惯基建：把「每周什么时候学」落成系统；第 7、10 阶复用同一套工具监控执行。

- **Habitica** — https://github.com/HabitRPG/habitica — 适用阶：1·10 — 把习惯与任务游戏化的开源应用。
- **Loop Habit Tracker** — https://github.com/iSoron/uhabits — 适用阶：1·10 — Android 习惯打卡与强度统计。
- **Super Productivity** — https://github.com/johannesjo/super-productivity — 适用阶：1·7 — 任务与时间块管理，跟踪练习时段。
- **ActivityWatch** — https://github.com/ActivityWatch/activitywatch — 适用阶：1·7·10 — 自动时间追踪，用真实数据校准时间预算。

## AI 学习助手

把 AI 当副驾，不当替身。原则：先自己想，再让 AI 追问、出题、挑错；撤掉 AI 后要能独立复现。以下工具只负责「角色扮演」与「本地运行」两件事，方法与风险证据见本节末尾。

- **Mr. Ranedeer AI Tutor** — https://github.com/JushBJJ/Mr.-Ranedeer-AI-Tutor — 适用阶：4·5 — 可配置的 AI 导师提示词框架（自定深度与风格）。
- **awesome-chatgpt-prompts** — https://github.com/f/awesome-chatgpt-prompts — 适用阶：4·5 — 提示词合集，可改造出考官、陪练与评审角色。
- **llama.cpp** — https://github.com/ggml-org/llama.cpp — 适用阶：4·7 — 本地推理引擎，离线跑开源模型当私教。
- **Ollama** — https://github.com/ollama/ollama — 适用阶：4·7 — 一键拉取与运行本地模型，数据不出本机。

*风险与用法证据：[C56] https://www.pnas.org/doi/10.1073/pnas.2422633122 —— 练习期依赖 AI，撤除后考试表现更差；带「不给答案、只提问」护栏的版本可缓解。[C57] https://bera-journals.onlinelibrary.wiley.com/doi/10.1111/bjet.13544 —— 生成式 AI 可能诱发依赖与「元认知懒惰」（metacognitive laziness）。撤掉 AI 后必须能独立复现，是使用任何「AI 学习助手」的底线。*

## 文献与引用

第 2 阶收集素材、第 4 阶做编码、第 9 阶教学输出引用：从采集到引用的完整链条。

- **Zotero** — https://github.com/zotero/zotero — 适用阶：2·4·9 — 文献收集、管理与 PDF 批注一条龙（浏览器抓取、引用输出）。
- **Better BibTeX** — https://github.com/retorquere/zotero-better-bibtex — 适用阶：9 — 为 Zotero 提供稳定的引用键与 BibTeX/LaTeX 导出。
- **Tesseract** — https://github.com/tesseract-ocr/tesseract — 适用阶：2·4 — OCR 引擎：把扫描书页与图片转成可检索文本。

## 按阶速查

不想按类别翻，就按阶段看。下表只列该阶最常用的工具（示例性收录，完整归属以各条目上的「适用阶」为准）：

| 阶 | 阶段 | 常用工具 |
|----|------|----------|
| 1 | 立志 | Super Productivity、Loop Habit Tracker、ActivityWatch、Habitica |
| 2 | 建图 | roadmap.sh、OSSU、Obsidian、markmap、Excalidraw、draw.io |
| 3 | 拆解 | Obsidian、Logseq、markmap |
| 4 | 编码 | Obsidian、Logseq、Zettlr、SilverBullet、Xournal++、genanki、Zotero |
| 5 | 检索 | Anki、AnkiDroid、Obsidian Spaced Repetition、org-fc、AnkiConnect、Yomitan |
| 6 | 间隔 | Anki、FSRS4Anki、FSRS Helper、Awesome FSRS、org-fc、AnkiDroid |
| 7 | 精练 | Exercism、LanguageTool、Stockfish、KaTrain、Audacity、lean4game |
| 8 | 实战 | freeCodeCamp、The Odin Project、Lichess、Blender、Quartz |
| 9 | 教学 | Quartz、Zotero、Better BibTeX、Mermaid、Obsidian |
| 10 | 维护 | Anki、Quartz、Obsidian、Logseq、ActivityWatch、Habitica |

## 三条路线的组合参考

三条路线（探索轨／实战轨／冲刺轨）的定义与权重见 `docs/paths.md`。若不想逐件挑选，可以按路线直接取用一组最小组合：

| 路线 | 最小组合 | 一句话理由 |
|------|----------|------------|
| 探索轨 | Obsidian + Anki + markmap | 随手建图、随手建卡，不做过度规划 |
| 实战轨 | Super Productivity + freeCodeCamp / The Odin Project + Quartz | 任务推进、项目练习、成果发布 |
| 冲刺轨 | Anki + FSRS4Anki + AnkiDroid | 调度交给算法，复习随身带 |

## 如何贡献工具

发现死链、更合适的替代品，或认为某个阶段缺工具，都欢迎提 Issue 或 PR。

- 入口一：仓库 Issue。请选用 `.github/ISSUE_TEMPLATE/` 下的 Issue 模板（模板尚在完善，占位说明即可，写清是「工具推荐」还是「链接失效」）；若无对应模板，直接开普通 Issue。
- 入口二：Pull Request。直接修改本文，保持「一行一条」的既有格式。

投稿建议附上三样：工具名称与仓库地址；适用阶（1–10）与一句话用途；你的实测访问状态（例如 `curl -s -o /dev/null -w "%{http_code}" -L <url>` 的结果）与核验日期。审阅口径与本文一致：开源或免费优先、与十阶流程有明确落点、链接实测可访问；许可证与运营主体由维护者在收录时统一核对，贡献者无需断言。
