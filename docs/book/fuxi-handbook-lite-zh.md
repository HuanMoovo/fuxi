# 伏羲框架 · 万物皆可学
## 精读手册（精简版 v1.1）

> 把「学会一样东西」拆成一条十阶时间线：每一阶给出最合适的方法 × 证据等级 × 开源工具 × 过关测试。
> 在线版（持续迭代）：https://HuanMoovo.github.io/fuxi/ ｜ 文档总目录：docs/README.md
> 许可：文档 CC BY 4.0 · 代码 MIT ｜ 全部文献可核验（C01–C286）

# 目录

# 编者的话：为什么是这四十多页

这本书是「伏羲框架」的精读入口：把你从「收藏夹里 100 个技巧、却不知道该用哪个」带到「一条清晰的十阶路线 + 一张证据地图」。

三点说明：
1. **本书是精简版**：完整版包含 11 个阶段详解、53 个理论框架、50+ 个方法卡、24 条误区考证与 286 条文献——全部开源在 GitHub，可在线检索。
2. **每一句主张都可核验**：文中 [Cxx] 编号对应书末精选文献与线上全量文献库；任何数字都能追到原文。
3. **读法**：先读第一章建立「为什么」，第二章当总目录随时跳转；第三章是上手清单；第四至六章按兴趣深入。

# 第一章 为什么需要这个框架

## 1.1 三重不对称：这个时代的学习困境

**知识在膨胀**：科学文献以年复合约 +4.1% 的速度增长、约 17.3 年翻一番（战后阶段更快）[C203]；全球存储容量 1986–2007 年间以约 +23%/年增长 [C204]。没有任何人的学习带宽在同步变宽——「读完再上场」的策略已经破产：正确的应对不是读得更快，而是携带地图（顺序）与过滤器（证据分级）。

**教育在滞后**：2022 年 PISA 显示多国数学与阅读出现历史性下滑 [C209]；中低收入国家约 70% 的 10 岁儿童读不懂简单短文 [C206]；大规模开放在线课程的证书完成率长期停留在约 3% 的量级 [C205]——「开放」不等于「完成」。等待教育系统更新不足以应对个人处境，需要「自建学习系统」+「质量核验工具」的组合。

**AI 是双刃剑**：无护栏使用生成式 AI，练习期表现 +48%、撤掉后考试 −17% [C56]；而带护栏的 AI 导师实验让学习显著提速（学习增益 0.73–1.3 SD，用时更少）[C59]。差别不在 AI，而在使用协议。

![图 1 · 知识缺口与三重时代危机](../assets/fuxi-why.svg)

## 1.2 四个论点（对应四篇深度剖析）

1. **方法碎片化**：每个技巧都带条件、剂量与顺序，短视频剥掉这些只剩口号——解药是框架层认知（先知道「何时用哪个」，再谈执行）。
2. **伪科学横行**：学习金字塔、学习风格匹配、速读等六大神话仍在传播；真正高效的方法（检索练习、间隔重复）反而被冷落 [C05][C214][C215]。判断任何学习主张，先跑「60 秒鉴别 SOP」：一手来源？对照组？可复现？谁在卖？
3. **爽感陷阱**：重读、划线、看视频让人「感觉在学」，延迟测验一做就露馅——流畅感是骗子，测验才是裁判 [C01][C220]。
4. **AI 时代的新风险**：认知卸载、幻觉、自动化偏误、评价失效、认知分层五重风险——把「独立尝试 → AI 质询 → 脱稿复现」写进每一阶 [C56][C222][C224]。

## 1.3 设计四原则

**地图优先**（十阶时间线回答「何时用哪个」）· **证据分级**（每个方法标 A/B/C/D：A 强 / B 中 / C 弱-条件 / D 证伪）· **AI 有护栏**（三步协议）· **开源可纠错**（CC BY 4.0，错误公开修正）。

# 第二章 十阶时间线：完整地图

![图 2 · 五纪十阶总览](../assets/fuxi-hero.svg)

## 2.1 总览表

| 阶段 | 一句话目标 | 核心方法 | 证据 |
|---|---|---|---|
| ① 立志 | 一页学习契约 | 目标层级 · 执行意图 | B |
| ② 建图 | 一页领域地图 | 三进路（发展史/对比/顶点倒推） | B |
| ③ 拆解 | 原子清单 + 练习动作 | 组块化 · 技能分解 | B |
| ④ 编码 | 最简解释 + 第一批卡 | 自我解释 · 生成效应 | A/B |
| ⑤ 检索 | 合上书先回忆 | 检索练习 · 抽认卡 | A |
| ⑥ 间隔 | 有序复习计划 | FSRS 调度 · 扩展间隔 | A |
| ⑦ 精练 | 能力边缘反复练 | 刻意练习 · 合意困难 | B |
| ⑧ 应用 | 真实项目干中学 | 做→卡→查→回填 | B |
| ⑨ 教学 | 讲给别人听 | 费曼式讲解 · 同伴教学 | A/B |
| ⑩ 维护 | 长期运转的系统 | 习惯 · 睡眠 · 运动 | A |
| ⑪ 拓界 | 走到知识边界之后 | 科研方法 + 五大赛道 | B |

## 2.2 第①阶 · 立志：一页学习契约

**目标**：把「想学 X」变成可执行的承诺。**核心动作**：写下「学成什么样算成功」（可验证的产出）+ 期限 + 每周固定时段；用「如果〈情境〉，就〈动作〉」把计划挂到固定线索上（执行意图，元分析 A 级 [C253]）。**过关自测**：能一句话说出目标、验收标准与时间预算。**常见错用**：目标是「学好英语」这类无法验收的愿望；计划没挂在具体时间地点上。

## 2.3 第②阶 · 建图：一页领域地图

**目标**：先知道森林在哪，再进树。**核心动作**：用三种进路任一画出骨架——发展史（时间线）、对比（同类并列）、顶点倒推（从高手在做什么反推知识树）；标出 5–9 个组块与前置关系。**过关自测**：合上资料，能向别人讲出这个领域的 5 个核心概念及其关系。**常见错用**：直接钻进第一个教程就开始学；地图追求完美而不开始。

## 2.4 第③阶 · 拆解：原子清单 + 练习动作

**目标**：把大技能拆到「一次练得动」。**核心动作**：拆成 15–60 分钟可完成一次的原子动作，按依赖排序；每个原子动作配一个明确练习。**过关自测**：清单里每一项都能在一小时内完成一次完整练习并知道对错。**常见错用**：拆得太粗（「练口语」）或太细（无法拼装）。

## 2.5 第④阶 · 编码：最简解释 + 第一批卡片

**目标**：把新知识编码成「可提取」的形式。**核心动作**：对每个概念写最简解释（用自己话讲给外行）；主动问「为什么成立 / 和什么相似 / 怎么不同」（精细提问）；先自己写答案再对照（生成效应 [C02]）；图文对照（双重编码 [C20]）。**过关自测**：能给外行讲懂 3 个核心概念。**常见错用**：抄书当编码；把「看过」当「编过」——检验标准是能否脱稿讲出来。

## 2.6 第⑤阶 · 检索：合上书先回忆

**目标**：用「取出」代替「再存入」。**核心动作**：学完立即合上材料，空白纸写/说全部能回忆的内容，再对照补缺；卡片一题一面（正面问题、背面答案）。**过关自测**：当天内容通过「空白纸回忆」测试（能写出 ≥70% 要点）。**常见错用**：只重读不复述；卡片越做越厚、复习只浏览不测验。[C01][C02]

## 2.7 第⑥阶 · 间隔：在快忘记时复习

**目标**：让记忆以最小成本存留最久。**核心动作**：把复习时点交给调度算法（如 FSRS），间隔随记忆强度扩展；考前分散到多天而非最后两晚猛攻。**过关自测**：连续 2 周按计划复习，完成率 > 80%。**常见错用**：每天固定复习全部卡片（低效）；临时抱佛脚（集中学习长期保持差）。[C04]

## 2.8 第⑦阶 · 精练：能力边缘反复练

**目标**：把「会」推到「熟」与「准」。**核心动作**：刻意练习四要素——明确子目标、在能力边缘、即时反馈、重复修正 [C31][C32]；混合题型与变式练习（交错，元分析支持 [C263]）；主动制造「合意困难」（拉长间隔、减少提示），但困难必须服务于检索与区辨 [C219]。**过关自测**：弱项在延迟测试中提升可观察。**常见错用**：舒适区重复一万小时；把「难受」当有效。

## 2.9 第⑧阶 · 应用：真实项目干中学

**目标**：让知识在真实场景中「长住」。**核心动作**：做真实项目，「做 → 卡 → 定向查学 → 回填」循环；任务尽量贴近真实使用场景（情境认知）；给新手保留保底脚手架，随熟练撤掉（示范淡出 [C81]）。**过关自测**：产出一个可展示的作品/交付物。**常见错用**：等「学完」再动手（无限期拖延）；只做教程题不做真项目。

## 2.10 第⑨阶 · 教学：教是最高级的学

**目标**：用输出倒逼输入。**核心动作**：脱稿讲给别人（或录音自讲），卡壳处即漏洞，补上再讲一遍 [C25][C19]；同伴教学：概念题先各自作答 → 讨论 → 再作答（收益显著 [C256]）。**过关自测**：完成一次 ≥10 分钟脱稿讲解并回复他人提问。**常见错用**：照着稿念；只讲给自己听从不接受提问。

## 2.11 第⑩阶 · 维护：让系统长期运转

**目标**：把学习变成可持续的日常。**核心动作**：固定线索 + 最小启动动作养成习惯 [C260]；睡眠 7–9 小时规律（学习环节而非奢侈品 [C261]）；每周 150 分钟运动 + 2 次力量（认知投资 [C262]）；每周 10 分钟复盘：完成率 / 卡点 / 下周调整。**过关自测**：连续 4 周系统未断链。**常见错用**：靠意志力硬撑；熬夜换时长。

## 2.12 第⑪阶 · 拓界：知识边界之后

**目标**：从「学人类已知」进入「探索人类未知」。**核心动作**：先写「无知清单」（你不知道自己不知道的东西 → 通过综述与专家访谈挖出）；用四矿脉找真问题（争议 / 断裂 / 工具 / 迁移）；证伪优先于证实。**过关自测**：提出一个可检验的新问题，并给出第一版实验设计。**常见错用**：追热点不做文献；问题大到无法检验。

# 第三章 十二张方法卡（先学这十二个）

**① 检索练习（A）**：合上材料写/说出全部能回忆的内容，再对照补缺。原理：提取本身会加固记忆 [C01]。常见错用：只重读不复述。

**② 间隔重复（A）**：把复习交给调度算法（FSRS），间隔随记忆强度扩展；目标保持越久、间隔越长 [C04]。常见错用：每天固定复习全部。

**③ 自我解释（A）**：学每一步时自问「为什么成立」并写下答案 [C19]。常见错用：只看不想，把「看懂」当「学会」。

**④ 生成效应（A）**：先自己写出答案再看解析，让大脑先「生成」再校对 [C02]。常见错用：先看答案再假装自己也会。

**⑤ 精细提问（B）**：对每条新知识主动问「为什么」（elaborative interrogation）与「和什么相似/不同」[C05]。常见错用：只求记住原文措辞。

**⑥ 双重编码（B）**：文字配结构图，图上必须有关系标注（不是装饰画）[C20]。常见错用：画漂亮的思维导图但从不回看。

**⑦ 示范题与淡出（B）**：新手先完整看一个样例，再逐步撤掉辅助自己做 [C81]。常见错用：一上来就硬做题、卡死崩溃。

**⑧ 刻意练习（B）**：明确子目标 + 在能力边缘 + 即时反馈 + 重复修正；领域不同效应不同（教育领域约 4% 方差）[C32]。常见错用：舒适区重复、无反馈硬练。

**⑨ 合意困难（B）**：让提取「稍微费力」——拉长间隔、交错题型、减少提示；困难必须服务于检索与区辨 [C219]。常见错用：把任何痛苦都当有效。

**⑩ 迁移设计（B）**：练习覆盖变式与跨情境；近迁移易、远迁移难，需要刻意设计 [C244]。常见错用：同一题型刷到熟，换个场景就废。

**⑪ 同伴教学（A）**：概念题先各自作答 → 同伴讨论 → 再作答；讨论前必须先独立思考 [C256]。常见错用：直接抄别人的答案参与讨论。

**⑫ AI 护栏三协议（强制）**：先独立尝试（哪怕错）→ 再让 AI 质询/找错/出题 → 最后脱稿复现才算学会 [C56][C59]。常见错用：直接要答案、把 AI 当代笔。

# 第四章 拓界篇：知识边界之后

科研不是终点而是起点：当你把「无知清单」写得足够具体，课题自会浮现。五个方向共用同一条创造循环——无知 → 问题 → 实验 → 证据 → 创造 → 传播。

![图 3 · 拓界循环整合图](../assets/fuxi-integration.svg)

## 4.1 科研：把未知变成公共知识

- 从「无知清单」到「四矿脉」找真问题：争议点 / 断裂带 / 新工具能解的老题 / 跨领域迁移 [C113][C114]。
- 组队是默认策略：高影响论文中团队署名占比持续上升 [C185]；非常规组合出高影响——新颖度要配比适度 [C186]。
- 提交与传播：预注册、开放数据、主动寻找反例与复现 [C285]。

## 4.2 创业：把创造变成产品与组织

- Mom Test 三原则：只问过去行为、问生活不问点子、少说多听 [C123 系]；MVP 的使命是「证伪一个关键假设」。
- PMF 判据看留存与口碑；「40% 非常失望」可作量化红线（Sean Ellis 测试）[C158 区域]。
- 创始人不年轻：高增长公司创始人平均 40+ 岁 [C125]；创业者承担不可分散风险，先定「可承受损失」[C190]。
- 双轨战略：需求可辨用「预测法」，高度不确定用「创造法」（试错、联盟、控制损失）[C188]。

## 4.3 人际：把关系当系统经营

- 四类经典模型：成人依恋四类型 / 爱情三角 / 强弱连接 / 互惠博弈 [C130][C131][C132][C133]。
- 「末日四骑士」（批评/鄙视/辩护/冷战）预测关系解体；**修复尝试**是关键变量 [C135]。
- 社会连接是健康因子：148 项研究，社会关系强的人存活率高约 50% 量级 [C136]。
- 弱连接给机会、强连接给信任：刻意经营「桥」的位置（结构洞）[C132][C164]。

## 4.4 长寿：把身体当基础设施

- 衰老有十二大标志（2023 扩展版）[C138]；把筹码押在 A 级因素：不吸烟、运动（死亡风险 −30~40% [C139]）、睡眠 7–9 小时（短睡风险 +12% 量级 [C140]）、地中海饮食（PREDIMED RCT 心血管事件显著下降 [C141]）、社交连接 [C136]。
- 「蓝区」极端长寿叙事有记录质量争议 [C142]；抗衰补剂与换血疗法证据等级 C/D——别做。
- 规律性 > 时长：睡眠规律与死亡风险的关联强于睡眠时长 [C197]。

## 4.5 未来：把世界地图更新到 2045

- 先学「怎么判断预测」：超级预测三件套——分层校准 + 基础率 + 频繁小步更新 [C151]；情景规划找「无后悔动作」。
- 六大前沿科学雷达（2026–2045）：人工智能 [C144] / 生物技术 [C145] / 聚变能源 [C146] / 健康老龄化 [C150] / 气候系统 [C148] / 空间制造。
- 宏观基础率：人口 2080 年代达峰约 103 亿 [C147]；每 +0.5°C 风险上台阶 [C148]；治理走向「竞争性共存」[C149]。

# 第五章 理论框架与方法全景（速查）

## 5.1 三十个核心框架（全量 53 个在线）

| 框架 | 一句话 | 文献 |
|---|---|---|
| 认知负荷理论 | 管理内在/外在/相关三类负荷 | C81·C15 |
| 工作记忆容量 | 同时处理的新信息只有几个组块 | C238 |
| 间隔效应 | 分散学习稳健优于集中 | C04 |
| 检索练习 | 「取出」比「存入」更能加固 | C01·C02 |
| 合意困难 | 特定困难提升长期保持 | C219 |
| 迁移 | 近迁移易、远迁移难 | C244 |
| 生成学习 | 主动生成意义而非接收 | C241·C23 |
| 自我解释 | 解释「为什么」是高效加工 | C19 |
| 双重编码 | 言语+图像双通道更牢 | C20 |
| 示范题与淡出 | 新手先看样例再撤辅助 | C81·C15 |
| 掌握学习 | 达标再进阶（2σ 方向） | C65 |
| 智能辅导系统 | 一对一机器导师接近人类 | C248 |
| 主动学习 | 课堂主动环节显著提升 | C249 |
| 反馈理论 | 任务/过程层反馈最有效 | C258·C259 |
| 刻意练习 | 目标+边缘+反馈+修正 | C31·C32 |
| 认知学徒/项目式 | 真实任务中师傅带 | C44·C45 |
| 自我调节学习 | 计划→执行→监控→反思 | C210 |
| 元认知 | 校准与监控自己的理解 | C242·C220 |
| 自我决定理论 | 自主/胜任/联结三需求 | C250 |
| 期望-价值 | 动机=期望×价值 | C251 |
| 目标设定 | 具体有难度优于尽力而为 | C252 |
| 执行意图 | 「如果X就做Y」转化行动 | C253 |
| 习惯回路 | 线索驱动的自动化 | C260 |
| 第一性原理 | 从深层原理推导而非类比 | C264·C265 |
| 类比推理 | 关系结构对齐而非表面相似 | C266 |
| 双加工 | 高风险判断强制慢通道 | C269·C270 |
| 批判性思维 | 对话式教学效果最优 | C271 |
| 贝叶斯推理 | 自然频率提升判断正确率 | C276 |
| 系统思维 | 反馈延迟骗过直觉 | C279 |
| 去偏差训练 | 单次训练可改善且持久 | C287 |

## 5.2 方法速查（按阶段，全量 50+ 在线）

| 阶段 | 方法 | 等级 | 文献 |
|---|---|---|---|
| 定向 | 具体目标设定 | A | C252 |
| 定向 | 执行意图 | A | C253 |
| 建图 | 领域地图三进路 | B | 本项目整理 |
| 拆解 | 组块化 | B | C17 |
| 编码 | 自我解释 | A | C19 |
| 编码 | 精细提问 | B | C05 |
| 编码 | 生成效应 | A | C02 |
| 编码 | 双重编码 | B | C20 |
| 编码 | 示范题淡出 | B | C81·C15 |
| 编码 | 概念图 | B | C41 |
| 检索 | 自由回忆 | A | C01 |
| 检索 | 抽认卡+调度 | A | C02·C04 |
| 检索 | 交错练习 | A | C263 |
| 检索 | 延迟判断 | B | C220 |
| 间隔 | 间隔重复 | A | C04 |
| 间隔 | 与睡眠对齐 | B | C261 |
| 精练 | 刻意练习 | B | C31·C32 |
| 精练 | 变式练习 | A | C263 |
| 精练 | 反馈循环 | A | C258·C259 |
| 应用 | 真实任务干中学 | B | C44 |
| 应用 | 项目式学习 | B | C45 |
| 应用 | 主动式工作坊 | A | C249 |
| 教学 | 教中学/费曼式 | B | C25·C19 |
| 教学 | 同伴教学 | A | C256 |
| 教学 | 导师/智能辅导 | A | C65·C248 |
| 维护 | 习惯设计 | B | C260 |
| 维护 | 睡眠 | A | C261 |
| 维护 | 运动 | A | C262 |
| 横切 | 原理推导练习 | B | C264·C265 |
| 横切 | 贝叶斯自然频率 | B | C276 |
| 横切 | 统计素养三问 | B | C283·C284 |

# 第六章 误区 24 条速查 + 六条详解

## 6.1 速查表

| 说法 | 真相 | 等级 |
|---|---|---|
| 学习风格匹配 | 无证据支持匹配增益 | D |
| 学习金字塔 | 数字无原始出处 | D |
| 重读/划线有用 | 低效用，只能热身 | D |
| 速读（高速+高理解） | 与阅读科学不符 | D |
| 一万小时定律 | 质量×反馈的函数 | D |
| 脑训练游戏提升智力 | 远迁移为零 | D |
| 成长型思维万能 | 证据支持条件性小效应 | C |
| 考前突击 | 集中学习长期保持差 | D |
| 边睡边学 | 编码需要清醒 | D |
| 遗忘=失败 | 遗忘是正常规律 | C |
| 多任务并行 | 切换代价+干扰同伴 | D |
| AI 全托管 | 撤离后表现下降 | D |
| 思维导图万能 | 证据有限、被营销夸大 | C |
| 先学完基础再动手 | 「学完」是无限期拖延 | C |
| 费曼技巧有原论文 | 后人的整理与命名 | C |
| 莫扎特效应 | 效应极小且可归因于唤醒 | D |
| 左右脑/10% 大脑 | 神经神话，无科学支持 | D |
| 关键期绝对化 | 渐变的敏感期非开关 | B |
| 手写必然优于打字 | 直接复现未发现优势 | C |
| 抽认卡只配死记 | 测试效应可迁移 | B |
| 补脑保健品 | 健康人无可靠证据 | C |
| 阅读障碍=看反字 | 神经发育性障碍 | D |
| 男生理科脑 | 性别差异极小且波动 | D |
| 合意困难=越难受越好 | 困难必须服务检索/区辨 | C |

## 6.2 六条详解

**学习金字塔（D）**：那张「听讲记住 5%、教别人记住 90%」的图，全部数字找不到原始出处——属以讹传讹 [C52]。要排序就用有证据的结论：检索练习与分散练习属高效用 [C05]。

**成长型思维（C）**：先承认合理部分——相信能力可发展有正面价值；但边界明确：两次元分析显示总效应很小，主要在有支持环境的中低成就学生中可见 [C21 区域]。当低成本补充可以，当万能钥匙不行。

**关键期（B）**：敏感期真实存在——第二语言语法能力约 17.9 岁前保持高位后开始下降 [C230]；但它是渐变的斜坡而不是开关，成人仍可以达到高水平（只是达标率下降）。

**手写 vs 打字（C）**：原始研究提示手写促进概括；但直接复现未发现手写优势，小元分析效应也极小 [C231]。决定因素是「你做了多少生成性加工」，不是工具本身。

**抽认卡只配死记（B）**：测试效应可迁移到新情境与新题型（虽小于直接效应）[C232]；把卡片升级为「应用卡/为什么卡」，理解类目标同样受益 [C233]。

**合意困难≠越难受越好（C）**：合意困难指特定设计——提取费力、间隔、交错、变式——服务「检索」与「区辨」两类加工；缺输入、烂材料、无序练习只会伤害学习 [C219]。

## 6.3 自查八问

① 上次学习结束有做空白纸回忆吗？② 用「我是视觉型」做过决定吗？③ 复习由工具调度还是心情？④ 撤掉 AI 能独立复现吗？⑤ 「等基础学完」说了多久？⑥ 判断「困难」看它练什么还是多难受？⑦ 用莫扎特/右脑类说法指导过学习投资吗？⑧ 校验过自己的 AI 用法符合三步协议吗？

# 第七章 证据与文献

## 7.1 证据分级标准

**A 强**（多项元分析/RCT 方向一致）· **B 中**（有对照研究，受情境调节）· **C 弱/条件**（理论好、实证有限）· **D 证伪**（流行但被证据否定）。等级为本项目对证据的综合判断，非期刊官方评级；所有数字照转文献报告口径。

## 7.2 精选文献（全量 C01–C286 见线上文献库）

- - [C01] Karpicke, J. D., & Roediger, H. L. (2008). The Critical Importance of Retrieval for Learning. *Science*, 319(5865), 966–968. ；<http
- - [C02] Roediger, H. L., & Karpicke, J. D. (2006). Test-Enhanced Learning. *Perspectives on Psychological Science*. ；<
- - [C03] Adesope, O. O., Trevisan, D. A., & Sundararajan, N. (2017). Rethinking the Use of Tests: A Meta-Analysis of Practice Testing. *Review of Educational Research*. <
- - [C04] Cepeda, N. J., et al. (2006). Distributed practice in verbal recall tasks. *Psychological Bulletin*, 132(3). ；
- - [C05] Dunlosky, J., et al. (2013). Improving Students' Learning With Effective Learning Techniques. *PSPI*.
- - [C09] Sinha, T., & Kapur, M. (2021). When Problem Solving Followed by Instruction Works: Evidence for Productive Failure. *RER*.
- - [C15] Sweller, J., van Merriënboer, J. J. G., & Paas, F. (2019). Cognitive Architecture and Instructional Design: 20 Years Later. *EPR*.
- - [C17] Chase & Simon (1973) Perception in chess；Cowan (2001) The magical number 4. ；
- - [C19] Bisra, K., et al. (2018). Inducing Self-Explanation: a Meta-Analysis. *EPR*.
- - [C20] Paivio, A. (1971). Imagery and Verbal Processes（书）；Mayer, R. E. (2009). Multimedia Learning（书）. ；
- - [C23] Fiorella, L., & Mayer, R. E. (2016). Eight Ways to Promote Generative Learning. *EPR*, 28(4).
- - [C25] Nestojko, J. F., et al. (2014). Expecting to teach enhances learning.
- - [C31] Ericsson, K. A., Krampe, R. T., & Tesch-Römer, C. (1993). The role of deliberate practice. *Psychological Review*.
- - [C32] Macnamara, B. N., Hambrick, D. Z., & Oswald, F. L. (2014). Deliberate Practice and Performance: A Meta-Analysis. *Psychological Science*.
- - [C41] Ausubel, D. P. (1960). Advance organizers；Novak & Cañas 概念图理论。 ；
- - [C44] Collins, A., Brown, J. S., & Newman, S. E. (1989). Cognitive Apprenticeship.
- - [C45] Dochy, F., et al. (2003). Effects of problem-based learning: A meta-analysis. *Learning and Instruction*.
- - [C51] Pashler, H., et al. (2008). Learning Styles: Concepts and Evidence. *PSPI*.
- - [C52] Letrud (2012) 与 Subramony et al. (2014)：学习金字塔/保持率锥系神话。 ；
- - [C53] Rayner, K., et al. (2016). So Much to Read, So Little Time. *PSPI*.
- - [C54] Sala, G., & Gobet, F. (2019). Near and Far Transfer in Cognitive Training. *Collabra*.
- - [C56] Bastani, H., et al. (2025). Generative AI without guardrails can harm learning. *PNAS*.
- - [C57] Fan, Y., et al. (2025). Beware of metacognitive laziness. *BJET*.
- - [C59] Kestin, G., et al. (2025). AI tutoring outperforms in-class active learning. *Scientific Reports*.
- - [C65] Bloom, B. S. (1984). The 2 Sigma Problem.
- - [C75] Roediger & Butler (2011) 检索练习的批判性回顾（TiCS）。
- - [C81] Sweller (1988) 认知负荷与示范题效应（原始论文）。
- - [C113] Kuhn, T. — The Structure of Scientific Revolutions（范式与反常）:
- - [C114] Popper, K. — 可证伪性与批判理性主义:
- - [C123] Camuffo et al. (2020). A Scientific Approach to Entrepreneurial Decision Making:
- - [C125] Azoulay et al. (2020). Age and High-Growth Entrepreneurship:
- - [C130] Hazan & Shaver (1987). Romantic love as attachment:
- - [C132] Granovetter (1973). The Strength of Weak Ties:
- - [C133] Nowak & Sigmund (2005). Evolution of indirect reciprocity:
- - [C135] Gottman Institute — Research:
- - [C136] Holt-Lunstad et al. (2010). Social Relationships and Mortality Risk:
- - [C138] López-Otín et al. (2023). Hallmarks of aging:
- - [C139] Moore et al. (2012). Physical activity and mortality:
- - [C141] Estruch et al. (2013). PREDIMED:
- - [C144] Stanford AI Index:
- - [C146] LLNL Fusion Ignition:
- - [C147] UN World Population Prospects:
- - [C148] IPCC AR6 SYR:
- - [C151] Tetlock et al. — Superforecasters:
- - [C203] Bornmann & Mutz (2015). Growth rates of modern science:
- - [C204] Hilbert & López (2011). The World's Technological Capacity:
- - [C205] Reich & Ruipérez-Valiente (2019). The MOOC Pivot（Science）:
- - [C206] World Bank — Learning Poverty:
- - [C207] WHO — Commission on Social Connection:
- - [C208] U.S. Surgeon General (2023). Our Epidemic of Loneliness and Isolation:
- - [C209] OECD (2023). PISA 2022 Results:
- - [C210] Zimmerman (2002). Becoming a Self-Regulated Learner:
- - [C214] Pashler et al. (2008). Learning Styles: Concepts and Evidence:
- - [C215] Rayner et al. (2016). So Much to Read, So Little Time:
- - [C216] Dekker et al. (2012). Neuromyths in Education:
- - [C217] Weisberg et al. (2008). The Seductive Allure of Neuroscience Explanations:
- - [C219] Bjork & Bjork (2011). Making Things Hard on Yourself, But in a Good Way:
- - [C220] Koriat & Bjork (2005). Illusions of Competence:
- - [C222] Ji et al. (2023). Survey of Hallucination in NLG:
- - [C224] Dell'Acqua et al. (2023). Navigating the Jagged Technological Frontier:
- - [C225] UNESCO (2023). Guidance for Generative AI in Education and Research:
- - [C226] Gerlich (2025). AI Tools in Society:
- - [C227] OpenAI et al. (2023). GPT-4 Technical Report:
- - [C228] Pietschnig, Voracek & Formann (2010). Mozart effect–Shmozart effect: A Meta-analysis:
- - [C230] Hartshorne, Tenenbaum & Pinker (2018). A Critical Period for Second Language Acquisition（Cognition）:
- - [C231] Urry et al. (2021). Don't Ditch the Laptop Just Yet: A Direct Replication（Psych Science）:
- - [C232] Pan & Rickard (2018). Transfer of Test-Enhanced Learning: Meta-Analytic Review（Psych Bulletin）:
- - [C233] Butler (2010). Repeated Testing Produces Superior Transfer of Learning（JEP:LMC）:
- - [C238] Cowan (2001). The Magical Number 4 in Short-Term Memory:
- - [C239] Baddeley (2012). Working Memory: Theories, Models, and Controversies（Annu Rev Psychol）:
- - [C240] van Kesteren et al. (2012). How Schema and Novelty Augment Memory Formation（TiCS）:
- - [C241] Wittrock (1974). Learning as a Generative Process:
- - [C244] Barnett & Ceci (2002). When and Where Do We Apply What We Learn?（迁移分类学）:
- - [C249] Freeman et al. (2014). Active Learning Increases Student Performance（PNAS）:
- - [C253] Gollwitzer & Sheeran (2006). Implementation Intentions and Goal Achievement（元分析）:
- - [C256] Smith et al. (2009). Why Peer Discussion Improves Student Performance（Science）:
- - [C258] Hattie & Timperley (2007). The Power of Feedback:
- - [C259] Wisniewski et al. (2020). The Power of Feedback Revisited（Frontiers）:
- - [C260] Wood & Neal (2007). A New Look at Habits and the Habit–Goal Interface:
- - [C261] Rasch & Born (2013). About Sleep's Role in Memory（Physiol Rev）:
- - [C262] Hillman, Erickson & Kramer (2008). Be Smart, Exercise Your Heart（Nat Rev Neurosci）:
- - [C263] Brunmair & Richter (2019). Similarity Matters: A Meta-Analysis on Interleaved Learning:
- - [C264] Chi, Feltovich & Glaser (1981). Categorization and Representation of Physics Problems:
- - [C265] Larkin et al. (1980). Expert and Novice Performance in Solving Physics Problems（Science）:
- - [C266] Gentner (1983). Structure-Mapping: A Theoretical Framework for Analogy:
- - [C269] Kahneman (2003). Maps of Bounded Rationality:
- - [C270] Evans & Stanovich (2013). Dual-Process Theories of Higher Cognition:
- - [C271] Abrami et al. (2015). Strategies for Teaching Students to Think Critically:
- - [C276] Gigerenzer & Hoffrage (1995). Bayesian Reasoning Without Instruction:
- - [C279] Sterman (2006). Learning from Evidence in a Complex World:
- - [C283] Amrhein et al. (2019). Scientists Rise Up Against Statistical Significance:
- - [C284] Wasserstein & Lazar (2016). ASA Statement on p-Values:
- - [C287] Morewedge et al. (2015). Debiasing Decisions:

# 结语：从这里出发

- 在线主页：https://HuanMoovo.github.io/fuxi/
- 文档总目录：https://github.com/HuanMoovo/fuxi/blob/main/docs/README.md
- 全量文献库：https://github.com/HuanMoovo/fuxi/blob/main/docs/references.md
- 图表生成器（可复现）：generator/build_svgs.py ｜ 本书生成器：generator/build_book.py

框架自己接受评判：发现错误欢迎提 Issue——错误被公开修正，本身就是这套方法的演示。
