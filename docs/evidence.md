# 证据库 · Evidence Base

> 伏羲框架的每一条方法主张，都应该在这里找到出处。
> **证据分级为本项目对现有证据的综合判断，非期刊官方评级。** 数字口径以所引论文原文为准；本库只转录摘要级结论。
> 核验日期：2026-10-03 ｜ 引用编号 `[C..]` 与 `docs/stages/`、`docs/myths.md` 完全一致。

## 怎么读这张表

- **A 强**：多项元分析/RCT 支持、方向一致；
- **B 中**：有对照研究支持，但结果受情境调节；
- **C 弱/条件**：理论基础好，实证有限或结论混合；
- **D 证伪/避免**：流行但被证据否定或夸大（会在 `myths.md` 展开）。

## 一表看懂：30 条核心结论

| # | 主张 | 代表研究 | 关键结论（口径） | 等级 | 边界与注意 |
|---|------|----------|------------------|------|------------|
| 1 | 检索练习（测试效应） | [C01][C02][C03][C71] | 一周后，重复检索组回忆约 80%，重复学习组约 35% [C01]；检索练习 > 概念图复习 [C71] | A | 检索后须核对纠错；简答优于选择题 |
| 2 | 分布/间隔练习 | [C04][C06][C62] | 254 项实验、约 1.4 万名被试，分布优于集中 [C04]；最佳间隔≈目标保持期的 10–20% [C06]；间隔-保持关系非单调 [C62] | A | 间隔长度跟「要记多久」挂钩 |
| 3 | 现代调度算法（FSRS / HLR） | [C26][C29][C61] | FSRS：2.2 亿条学习日志建模，较当时最优方法提升 12.6%，上线墨墨背单词 [C26] | A（工业级部署） | 参数要按个人日志优化；看延后测验，不看当场手感 |
| 4 | 交错练习 | [C07][C08] | 数学 RCT：延迟测验 61% vs 38%，d=0.83；另一研究 72% vs 38%，d=1.05 [C07]；59 项研究、238 个效应量 [C08] | A（受调节） | 材料越相似收益越大；初学阶段可先块状再交错 |
| 5 | 变式练习（变换情境/参数） | [C30] | 变化练习的长期保持与迁移优于固定练习 [C30] | B | 运动技能类证据更充分 |
| 6 | 重读与划线 | [C05] | 重读、划线等属「低效用」技术 [C05] | D（低效） | 只能当热身，不能当学习主力 |
| 7 | 自我解释 | [C19] | 元分析：诱导自我解释有中等偏上正效应 [C19] | A | 对复杂材料收益更大 |
| 8 | 精细提问（「为什么」） | [C05] | 中等效用 [C05] | B | 适合概念性材料 |
| 9 | 生成效应（先自答再看） | [C05] | 自己生成答案优于被动阅读 [C05] | B | 与检索练习配合 |
| 10 | 双重编码 / 多媒体原则 | [C20] | 语言+图像双通道编码优于单通道 [C20] | B | 图要相关，装饰图无益 |
| 11 | 示范题与脚手架淡出 | [C15] | 新手先学 worked example，随后逐步撤走脚手架（专长反转效应）[C15] | A | 对新手用示范，对老手换练习 |
| 12 | 引导式教学 vs 最小指导 | [C16] | 对新手，「最小指导」式教学无效甚至有害 [C16] | A | 与「干中学」按熟练度分工 |
| 13 | 元认知校准 | [C05][C50] | 「感觉会了」不可靠，需用测验校准 [C05][C50] | B | 先预测测后对答案 |
| 14 | 目标设定与执行意图 | [C36][C33] | 具体且有挑战的目标+反馈最有效 [C36]；if-then 计划对目标达成有稳健效应 [C33] | B | 目标要写成可检验结果 |
| 15 | 习惯成形 | [C38] | 自动化中位数 66 天（区间 18–254 天）[C38] | B | 个体差异极大，别用 21 天神话压自己 |
| 16 | 动机（自我决定/自我效能） | [C34][C35][C39] | 自主·胜任·联结支撑内在动机 [C34]；效能感与效用价值干预可提升投入 [C35][C39] | B | 动机是设计出来的，不是打鸡血 |
| 17 | 成长型思维 | [C21] | 两个元分析整体效应弱；仅在部分情境有小效应 [C21] | C（弱） | 有用但远非万能钥匙 |
| 18 | 刻意练习 | [C31][C32] | 解释力因领域差异极大：游戏 26%、音乐 21%、体育 18%、教育 4%、职业 <1%（以原文为准）[C32] | B | 练法对、反馈快，才叫刻意练习 |
| 19 | 反馈 | [C46][C47] | 反馈是强力变量但高度依赖形式；607 个效应量中相当比例为负 [C46][C47] | A | 具体、可行动、对事不对人 |
| 20 | 认知学徒制 | [C44] | 示范/辅导/脚手架/淡出/表达/反思/探索 [C44] | B | 找高手带，或把高手「录下来」 |
| 21 | 先失败后教学（productive failure） | [C09] | 元分析 g=0.36 [0.20, 0.51]；高保真实施 0.37–0.58 [C09] | B | 先尝试→再受教，适合概念学习 |
| 22 | 项目式学习（PBL） | [C45] | 技能与态度小幅优势，知识面可能略窄 [C45] | B | 与结构化复习配套使用 |
| 23 | 情境学习 / 社区参与 | [C48] | 学习嵌入真实共同体，合法边缘参与 [C48] | B | 先进社区做小事 |
| 24 | 教学效应 | [C25][C23] | 预期要教别人 → 学习组织与回忆更好 [C25]；生成式学习策略清单 [C23] | B | 费曼技巧的机制即在此 |
| 25 | 迁移 | [C10][C11][C12][C13] | 近迁移支持强、远迁移有限，需刻意设计 [C10][C12]；类比与变式可促进 [C11][C30] | B | 「学完自动会用」是幻觉 |
| 26 | 睡眠与记忆巩固 | [C73] | 睡眠参与记忆巩固（综述）[C73] | B | 熬夜是偷学习效率的债 |
| 27 | 辅导与 AI 导师 | [C63][C64][C65][C59][C60][C22] | 一对一辅导极具威力（2σ 问题）[C65]；ITS 平均约 0.66 [C63]；专门设计的 AI 导师 0.73–1.3 SD 且用时更少 [C59]；AI 辅助真人导师 +4pp [C60]；主动学习 +0.47 SD [C22] | A/B | 设计质量决定成败；「有 AI」不等于「学得好」 |
| 28 | AI 撤除后的表现 | [C56] | 练习期 +48%，撤除 AI 后考试 −17% [C56] | B（单一大型 RCT） | 护栏（只给提示不给答案）可缓解 [C56] |
| 29 | AI 依赖风险 | [C57][C58] | 生成式 AI 可能诱发依赖与「元认知懒惰」[C57]；EEG 预印本研究提示「认知债务」[C58] | C（含未评审预印本） | 当作风险提示，不作定论 |
| 30 | 无效/夸大清单 | [C51][C52][C53][C54] | 学习风格匹配无证据 [C51]；学习金字塔是神话 [C52]；速读宣称不成立 [C53]；脑训远迁移为零 [C54] | D | 详见 `myths.md` |

## 数字口径（写作与引用时允许出现的具体数字）

- 约 80% vs 约 35%（[C01]；以原文为准）
- 254 项实验 / ≈1.4 万人（[C04]）；最佳间隔 ≈ 保持期 10–20%（[C06]）
- 61% vs 38%（d=0.83）；72% vs 38%（d=1.05）（[C07]）；59 项研究 / 238 个效应量（[C08]）
- FSRS：2.2 亿日志、+12.6%（[C26]）
- 多元分析效应：productive failure g=0.36 [0.20, 0.51]，高保真 0.37–0.58（[C09]）
- 刻意练习解释力：26% / 21% / 18% / 4% / <1%（[C32]，以原文为准）
- 反馈：607 个效应量、23,663 个观测（[C47]）
- 习惯：中位数 66 天（18–254 天）（[C38]）
- 主动学习：+0.47 SD；挂科率 33.8% → 21.8%（[C22]）
- ITS 平均效应 ≈0.66（[C63]）；AI 导师 0.73–1.3 SD（[C59]）；Tutor CoPilot +4pp（[C60]）
- AI 风险：练习 +48% / 考试 −17%（[C56]）

## 完整引用列表

- [C01] Karpicke, J. D., & Roediger, H. L. (2008). The Critical Importance of Retrieval for Learning. *Science*, 319(5865), 966–968. https://doi.org/10.1126/science.1152408
- [C02] Roediger, H. L., & Karpicke, J. D. (2006). Test-Enhanced Learning. *Perspectives on Psychological Science*. https://journals.sagepub.com/doi/10.1111/j.1745-6916.2006.00012.x
- [C03] Adesope, O. O., Trevisan, D. A., & Sundararajan, N. (2017). Rethinking the Use of Tests: A Meta-Analysis of Practice Testing. *Review of Educational Research*. https://gwern.net/doc/psychology/spaced-repetition/2017-adesope.pdf
- [C04] Cepeda, N. J., Pashler, H., Vul, E., Wixted, J. T., & Rohrer, D. (2006). Distributed practice in verbal recall tasks: A review and quantitative synthesis. *Psychological Bulletin*, 132(3). https://pubmed.ncbi.nlm.nih.gov/16719566/
- [C05] Dunlosky, J., Rawson, K. A., Marsh, E. J., Nathan, M. J., & Willingham, D. T. (2013). Improving Students' Learning With Effective Learning Techniques. *Psychological Science in the Public Interest*. https://pubmed.ncbi.nlm.nih.gov/26173288/
- [C06] Cepeda, N. J., Vul, E., Rohrer, D., Wixted, J. T., & Pashler, H. (2008). Spacing Effects in Learning: A Temporal Ridgeline of Optimal Retention. *Psychological Science*, 19(11). https://doi.org/10.1111/j.1467-9280.2008.02209.x
- [C07] Rohrer, D., Dedrick, R. F., Hartwig, M. K., & Cheung, C.-N. (2020). A randomized controlled trial of interleaved mathematics practice. *JEP: General*. https://gwern.net/doc/psychology/spaced-repetition/2019-rohrer.pdf ｜ Rohrer, Dedrick & Stershic (2015). https://pubmed.ncbi.nlm.nih.gov/24578089/
- [C08] Brunmair, M., & Richter, T. (2019). Similarity matters: A meta-analysis of interleaved learning and its moderators. *Psychological Bulletin*, 145(11). https://psychologie.uni-wuerzburg.de/fileadmin/06020400/2019/Brunmair_Richter_in_press__2019_META-ANALYSIS_OF_INTERLEAVED_LEARNING.pdf
- [C09] Sinha, T., & Kapur, M. (2021). When Problem Solving Followed by Instruction Works: Evidence for Productive Failure. *Review of Educational Research*. https://journals.sagepub.com/doi/full/10.3102/00346543211019105
- [C10] Pan, S. C., & Rickard, T. C. (2018). Transfer of test-enhanced learning: Meta-analytic review and synthesis. https://pdf.retrievalpractice.org/transfer/Pan_Rickard_2018.pdf
- [C11] Gick, M. L., & Holyoak, K. J. (1983). Schema induction and analogical transfer. *Cognitive Psychology*. https://www.sciencedirect.com/science/article/pii/0010028583900026
- [C12] Barnett, S. M., & Ceci, S. J. (2002). When and where do we apply what we learn? A taxonomy for far transfer. *Psychological Bulletin*, 128(4). https://doi.org/10.1037/0033-2909.128.4.612
- [C13] Hatano, G., & Inagaki, K. (1986). Two courses of expertise. https://psycnet.apa.org/record/1986-97669-017
- [C14] Murre, J. M. J., & Dros, J. (2015). Replication and Analysis of Ebbinghaus' Forgetting Curve. *PLOS ONE*. https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0120644
- [C15] Sweller, J., van Merriënboer, J. J. G., & Paas, F. (2019). Cognitive Architecture and Instructional Design: 20 Years Later. *Educational Psychology Review*. https://link.springer.com/article/10.1007/s10648-019-09465-5
- [C16] Kirschner, P. A., Sweller, J., & Clark, R. E. (2006). Why Minimal Guidance During Instruction Does Not Work. *Educational Psychologist*. https://www.tandfonline.com/doi/abs/10.1207/s15326985ep4102_1
- [C17] Chase & Simon (1973)；Cowan (2001)。工作记忆限制与组块（文本引用）。
- [C18] Chi, M. T. H., & Wylie, R. (2014). The ICAP Framework: Linking Cognitive Engagement to Active Learning Outcomes. *Educational Psychologist*. https://doi.org/10.1080/00461520.2014.965823
- [C19] Bisra, K., Liu, Q., Nesbit, J. C., Salimi, F., & Winne, P. H. (2018). Inducing Self-Explanation: a Meta-Analysis. *Educational Psychology Review*. https://eric.ed.gov/?id=EJ1186664
- [C20] Paivio (1971) 双编码；Mayer (2009) 多媒体学习（文本引用）。
- [C21] Sisk, V. F., Burgoyne, A. P., Sun, J., Butler, J. L., & Macnamara, B. N. (2018). To What Extent and Under Which Circumstances Are Growth Mind-Sets Important to Academic Achievement? Two Meta-Analyses. *Psychological Science*. https://journals.sagepub.com/doi/10.1177/0956797617739704
- [C22] Freeman, S., et al. (2014). Active learning increases student performance in science, engineering, and mathematics. *PNAS*. https://doi.org/10.1073/pnas.1319030111
- [C23] Fiorella, L., & Mayer, R. E. (2016). Eight Ways to Promote Generative Learning. *Educational Psychology Review*, 28(4). https://eric.ed.gov/?id=EJ1120458
- [C24] Chase & Simon (1973)。专家以「组块」记忆棋局（文本引用）。
- [C25] Nestojko, J. F., Bui, D. C., Kornell, N., & Bjork, E. L. (2014). Expecting to teach enhances learning and organization of knowledge in free recall of text passages. https://source.wustl.edu/2014/07/expecting-to-teach-enhances-learning-recall
- [C26] Ye, J., Su, J., & Cao, Y. (2022). A Stochastic Shortest Path Algorithm for Optimizing Spaced Repetition Scheduling. *KDD '22*. https://dl.acm.org/doi/10.1145/3534678.3539081
- [C27] FSRS 生态：https://github.com/open-spaced-repetition/fsrs4anki ｜ https://github.com/open-spaced-repetition/free-spaced-repetition-scheduler
- [C28] Arthur et al. (1998)。技能衰减与保持的定量综述（文本引用）。
- [C29] Settles, B., & Meeder, B. (2016). A Trainable Spaced Repetition Model for Language Learning. *ACL*. https://research.duolingo.com/papers/settles.acl16.pdf
- [C30] Shea, J. B., & Morgan, R. L. (1979). Contextual interference effects on the acquisition, retention, and transfer of a motor skill. https://gwern.net/doc/psychology/spaced-repetition/1979-shea.pdf
- [C31] Ericsson, K. A., Krampe, R. T., & Tesch-Römer, C. (1993). The role of deliberate practice in the acquisition of expert performance. *Psychological Review*. https://psycnet.apa.org/doiLanding?doi=10.1037%2F0033-295X.100.3.363
- [C32] Macnamara, B. N., Hambrick, D. Z., & Oswald, F. L. (2014). Deliberate Practice and Performance in Music, Games, Sports, Education, and Professions: A Meta-Analysis. *Psychological Science*. https://pubmed.ncbi.nlm.nih.gov/24986855/
- [C33] Gollwitzer, P. M., & Sheeran, P. (2006). Implementation Intentions and Goal Achievement: A Meta-Analysis. https://www.researchgate.net/publication/37367696_Implementation_Intentions_and_Goal_Achievement_A_Meta-Analysis_of_Effects_and_Processes
- [C34] Ryan, R. M., & Deci, E. L. (2000). Self-Determination Theory and the Facilitation of Intrinsic Motivation. *American Psychologist*. https://selfdeterminationtheory.org/SDT/documents/2000_RyanDeci_SDT.pdf
- [C35] Bandura (1977)。自我效能四来源（文本引用）。
- [C36] Locke, E. A., & Latham, G. P. (2002). Building a practically useful theory of goal setting and task motivation. *American Psychologist*. https://psycnet.apa.org/doiLanding?doi=10.1037%2F0003-066X.57.9.705
- [C37] Zimmerman, B. J. (2002). Becoming a Self-Regulated Learner: An Overview. https://www.leiderschapsdomeinen.nl/wp-content/uploads/2016/12/Zimmerman-B.-2002-Becoming-Self-Regulated-Learner.pdf
- [C38] Lally, P., et al. (2010). How are habits formed: Modelling habit formation in the real world. *EJSP*。（文本引用；口径见上表）
- [C39] Hulleman & Harackiewicz (2009)。效用价值干预（文本引用）。
- [C40] Oettingen（心理对照 / WOOP，文本引用）。
- [C41] Ausubel (1960) 先行组织者；Novak 概念图（文本引用）。
- [C42] Meyer, J. H. F., & Land, R. (2003). Threshold concepts and troublesome knowledge. https://www.research.ed.ac.uk/en/publications/threshold-concepts-and-troublesome-knowledge-linkages-to-ways-of-/
- [C43] Gagné 学习层级（文本引用）。
- [C44] Collins, A., Brown, J. S., & Newman, S. E. (1989). Cognitive Apprenticeship. https://files.eric.ed.gov/fulltext/ED284181.pdf
- [C45] Dochy, F., et al. (2003). Effects of problem-based learning: A meta-analysis. *Learning and Instruction*. https://eric.ed.gov/?id=EJ678509
- [C46] Hattie, J., & Timperley, H. (2007). The Power of Feedback. *Review of Educational Research*. https://doi.org/10.3102/003465430298487
- [C47] Kluger, A. N., & DeNisi, A. (1996). The effects of feedback interventions on performance. *Psychological Bulletin*. https://psycnet.apa.org/record/1996-02773-003
- [C48] Lave, J., & Wenger, E. (1991). Situated Learning: Legitimate Peripheral Participation. https://www.cambridge.org/highereducation/books/situated-learning/6915ABD21C8E4619F750A4D4ACA616CD
- [C49] Ahrens, S. (2017). *How to Take Smart Notes*；Luhmann 卡片盒（文本引用）。
- [C50] Dunning & Kruger (1999)；Koriat & Bjork（学习判断，文本引用）。
- [C51] Pashler, H., McDaniel, M., Rohrer, D., & Bjork, R. (2008). Learning Styles: Concepts and Evidence. *PSPI*. https://journals.sagepub.com/doi/full/10.1111/j.1539-6053.2009.01038.x
- [C52] Letrud, K. (2012). A Rebuttal of NTL Institute's Learning Pyramid. https://eric.ed.gov/?id=EJ996977 ｜ Subramony et al. (2014). https://eric.ed.gov/?id=EJ1057239
- [C53] Rayner, K., et al. (2016). So Much to Read, So Little Time: How Do We Read, and Can Speed Reading Help? *PSPI*. https://pubmed.ncbi.nlm.nih.gov/26769745/
- [C54] Sala, G., & Gobet, F. (2019). Near and Far Transfer in Cognitive Training: A Second-Order Meta-Analysis. *Collabra*. https://online.ucpress.edu/collabra/article/5/1/18/113004/
- [C55] Kirschner, P. A. (2017). Stop propagating the learning styles myth. *Computers & Education*（文本引用）。
- [C56] Bastani, H., Bastani, O., Sungu, A., Ge, H., Kabakcı, Ö., & Mariman, R. (2025). Generative AI without guardrails can harm learning: Evidence from high school mathematics. *PNAS*. https://www.pnas.org/doi/10.1073/pnas.2422633122
- [C57] Fan, Y., et al. (2025). Beware of metacognitive laziness: Effects of generative artificial intelligence on learning motivation, processes, and performance. *BJET*. https://bera-journals.onlinelibrary.wiley.com/doi/10.1111/bjet.13544
- [C58] Kosmyna, N., et al. (2025). Your Brain on ChatGPT: Accumulation of Cognitive Debt... MIT Media Lab（预印本，未同行评审）. https://www.media.mit.edu/publications/your-brain-on-chatgpt/
- [C59] Kestin, G., Miller, K., Klales, A., Milbourne, T., & Ponti, G. (2025). AI tutoring outperforms in-class active learning: an RCT... *Scientific Reports*. https://doi.org/10.1038/s41598-025-97652-6
- [C60] Wang, R. E., et al. (2024). Tutor CoPilot: A Human-AI Approach for Scaling Real-Time Expertise. https://arxiv.org/abs/2410.03017
- [C61] Tabibian, B., et al. (2019). Enhancing human learning via spaced repetition optimization. *PNAS*. https://www.pnas.org/doi/10.1073/pnas.1815156116
- [C62] Mozer, M., Pashler, H., Cepeda, N., Lindsey, R., & Vul, E. (2009). Predicting the Optimal Spacing of Study. *NeurIPS*. https://papers.nips.cc/paper_files/paper/2009/file/6bc24fc1ab650b25b4114e93a98f1eba-Paper.pdf
- [C63] Kulik, J. A., & Fletcher, J. D. (2016). Effectiveness of Intelligent Tutoring Systems: A Meta-Analytic Review. *RER*. https://journals.sagepub.com/doi/10.3102/0034654315581420
- [C64] VanLehn, K. (2011). The Relative Effectiveness of Human Tutoring, Intelligent Tutoring Systems, and Other Tutoring Systems. *Educational Psychologist*. https://www.tandfonline.com/doi/full/10.1080/00461520.2011.611369
- [C65] Bloom, B. S. (1984). The 2 Sigma Problem（文本引用）。
- [C66] Ebbinghaus (1885)；Bjork & Bjork (2011) 合意困难；Craik & Lockhart (1972)（文本引用）。
- [C67] Fitts & Posner (1967)；Newell & Rosenbloom (1981) 练习幂律。https://iiif.library.cmu.edu/file/Newell_box00032_fld02190_doc0001/Newell_box00032_fld02190_doc0001.pdf
- [C68] Vygotsky (1978)；Wood, Bruner & Ross (1976)（文本引用）。
- [C69] Krashen (1982)；Nation (2006)（文本引用）。
- [C70] Csikszentmihalyi (1990)（文本引用）。
- [C71] Karpicke, J. D., & Blunt, J. R. (2011). Retrieval Practice Produces More Learning than Elaborative Studying with Concept Mapping. *Science*. https://doi.org/10.1126/science.1199327
- [C72] 延伸读物：Brown et al. (2014)《Make It Stick》；Ericsson & Pool (2016)《Peak》；Young (2019)《Ultralearning》；Newport (2016)《Deep Work》；Walker (2017)《Why We Sleep》；Oakley (2014)《A Mind for Numbers》；Adler (1940/1972)《How to Read a Book》。
- [C73] Rasch, B., & Born, J. (2013). About Sleep's Role in Memory. *Physiological Reviews*. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3768102

## 如何更新

发现新论文、错误引用或更好的数字口径？请按仓库 Issue 模板提交，附：论文链接、结论摘要、建议等级、替换理由。每次更新会在 CHANGELOG 记录。
