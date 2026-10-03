# Changelog

本项目遵循 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/) 与语义化版本。

## [1.2.0] - 2026-10-03

### Added
- `docs/stages/11-expand.md`：**第 11 阶 · 拓界** —— 触到人类知识/认知边界后，如何发现新问题、炼化研究问题、构建新理论（结合 C111–C122 文献，含流程图、工具链与过关检验）。
- `docs/awesome-lifespan.md`：**人生时间线友链目录** —— 从出生到老年 8 个阶段的学习重点 × 开源工具 × 对应十阶；由 `generator/build_lifespan.py` 可复现生成（41 条全部经核验）。
- `docs/references.md` 增补拓界篇文献 C111–C122（全部可点击、经核验）。

## [1.1.1] - 2026-10-03

### Added
- `docs/awesome-learning.md`：学习友链目录 —— 2464 个学习项目（精选 12 类 + 自动采集国际项目与书籍 5 区；由 `generator/build_awesome.py` 与 `generator/harvest_awesome.py` 可复现生成）；README 顶部导航、仓库导航树、工具链文档与站点页脚均已接入。

## [1.1.0] - 2026-10-03

### Changed
- **README 顶部居中**：LOGO + 标题 + 徽章居中排版；新增横版组合标 `docs/assets/fuxi-logo.svg`。
- **图表重绘为「复古笔记本」手绘风**：纸张横格、红边线、装订孔、和纸胶带、手写体、红印章、荧光笔高亮；6+1 张 SVG 全部由 `generator/build_svgs.py` 可复现生成。
- **引用全面补链**：C01–C73 每条均附可查看来源（开放获取优先，替换 ResearchGate 等反爬链接）；清理不可加载链接。
- 站点：LOGO 入驻、区块标题居中、统计更新为 110+ 文献、新增扩展文献入口。

### Added
- `docs/references.md`：扩展文献库 C74–C110（37 条，按主题分类）。
- `LICENSE-DOCS.md`：文档与图表 CC BY 4.0 声明（LICENSE 保持纯 MIT，便于 GitHub 识别）。

## [1.0.0] - 2026-10-03

### Added
- **十阶时间线**（`docs/stages/`）：立志 → 建图 → 拆解 → 编码 → 检索 → 间隔 → 精练 → 实战 → 教学 → 维护，共 10 篇阶段详解，每篇含方法卡（证据等级）、工具、过关自测、误区与 AI 用法。
- **证据库**（`docs/evidence.md`）：30 条核心结论、A/B/C/D 四级证据分级、70+ 条引用与数字口径。
- **开源工具链**（`docs/tools.md`）：50+ 工具，按阶段索引、逐链接核验。
- **三轨适配**（`docs/paths.md`）：探索 / 实战 / 冲刺三条路线权重表、五大领域适配、30 天启动模板、每日节律与复习预算速查。
- **误区辟谣库**（`docs/myths.md`）：15 条常见伪科学与夸大说法，逐条给证据与替代做法。
- **学习模板**（`templates/`）：学习契约、周检视、错题日志、卡片规则、十阶过关清单。
- **FAQ**（`docs/faq.md`）：12 个高频问题。
- **SVG 图表**（`docs/assets/`）：总览、引擎、三轨、间隔调度、练习闭环、标志共 6 张；全部由 `generator/build_svgs.py` 可复现生成。
- **GitHub Pages 主页**（`docs/index.html`）：零依赖静态单页。
- **CI**：每周链接检查（lychee）；Issue 模板（文献 / 工具 / 纠错）。

### Notes
- 证据分级为本项目对现有证据的综合判断，非期刊官方评级；引用数字以所引论文原文为准（核验日期 2026-10-03）。
- 本框架受双路径思想（搭框架 / 干中学）启发，在此基础上扩展并科学化。
