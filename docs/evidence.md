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

> 每条引用均附可查看来源；开放获取优先。出版商页面（少数需正常浏览器打开）在链接核验时可能拒绝爬虫访问。

- [C01] Karpicke, J. D., & Roediger, H. L. (2008). The Critical Importance of Retrieval for Learning. *Science*, 319(5865), 966–968. <https://learninglab.psych.purdue.edu/downloads/2008/2008_Karpicke_Roediger_Science.pdf>；<https://doi.org/10.1126/science.1152408>
- [C02] Roediger, H. L., & Karpicke, J. D. (2006). Test-Enhanced Learning. *Perspectives on Psychological Science*. <https://learninglab.psych.purdue.edu/downloads/2006/2006_Roediger_Karpicke_PsychSci.pdf>；<https://journals.sagepub.com/doi/10.1111/j.1745-6916.2006.00012.x>
- [C03] Adesope, O. O., Trevisan, D. A., & Sundararajan, N. (2017). Rethinking the Use of Tests: A Meta-Analysis of Practice Testing. *Review of Educational Research*. <https://gwern.net/doc/psychology/spaced-repetition/2017-adesope.pdf>
- [C04] Cepeda, N. J., et al. (2006). Distributed practice in verbal recall tasks. *Psychological Bulletin*, 132(3). <https://escholarship.org/content/qt3rr6q10c/qt3rr6q10c.pdf>；<https://pubmed.ncbi.nlm.nih.gov/16719566/>
- [C05] Dunlosky, J., et al. (2013). Improving Students' Learning With Effective Learning Techniques. *PSPI*. <https://pubmed.ncbi.nlm.nih.gov/26173288/>
- [C06] Cepeda, N. J., et al. (2008). Spacing Effects in Learning: A Temporal Ridgeline of Optimal Retention. *Psychological Science*, 19(11). <https://doi.org/10.1111/j.1467-9280.2008.02209.x>
- [C07] Rohrer, D., Dedrick, R. F., Hartwig, M. K., & Cheung, C.-N. (2020). A randomized controlled trial of interleaved mathematics practice. *JEP: General*；另 Rohrer et al. (2015). <https://gwern.net/doc/psychology/spaced-repetition/2019-rohrer.pdf>；<https://pubmed.ncbi.nlm.nih.gov/24578089/>
- [C08] Brunmair, M., & Richter, T. (2019). Similarity matters: A meta-analysis of interleaved learning. *Psychological Bulletin*, 145(11). <https://psychologie.uni-wuerzburg.de/fileadmin/06020400/2019/Brunmair_Richter_in_press__2019_META-ANALYSIS_OF_INTERLEAVED_LEARNING.pdf>
- [C09] Sinha, T., & Kapur, M. (2021). When Problem Solving Followed by Instruction Works: Evidence for Productive Failure. *RER*. <https://journals.sagepub.com/doi/full/10.3102/00346543211019105>
- [C10] Pan, S. C., & Rickard, T. C. (2018). Transfer of test-enhanced learning: Meta-analytic review and synthesis. <https://pdf.retrievalpractice.org/transfer/Pan_Rickard_2018.pdf>
- [C11] Gick, M. L., & Holyoak, K. J. (1983). Schema induction and analogical transfer. *Cognitive Psychology*. <https://www.sciencedirect.com/science/article/pii/0010028583900026>
- [C12] Barnett, S. M., & Ceci, S. J. (2002). When and where do we apply what we learn? *Psychological Bulletin*, 128(4). <https://doi.org/10.1037/0033-2909.128.4.612>
- [C13] Hatano, G., & Inagaki, K. (1986). Two courses of expertise. <https://psycnet.apa.org/record/1986-97669-017>
- [C14] Murre, J. M. J., & Dros, J. (2015). Replication and Analysis of Ebbinghaus' Forgetting Curve. *PLOS ONE*. <https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0120644>
- [C15] Sweller, J., van Merriënboer, J. J. G., & Paas, F. (2019). Cognitive Architecture and Instructional Design: 20 Years Later. *EPR*. <https://link.springer.com/article/10.1007/s10648-019-09465-5>
- [C16] Kirschner, P. A., Sweller, J., & Clark, R. E. (2006). Why Minimal Guidance During Instruction Does Not Work. *Educational Psychologist*. <https://eric.ed.gov/?id=EJ736299>
- [C17] Chase & Simon (1973) Perception in chess；Cowan (2001) The magical number 4. <https://doi.org/10.1016/0010-0285(73)90004-2>；<https://pubmed.ncbi.nlm.nih.gov/11515286>
- [C18] Chi, M. T. H., & Wylie, R. (2014). The ICAP Framework. *Educational Psychologist*. <https://doi.org/10.1080/00461520.2014.965823>
- [C19] Bisra, K., et al. (2018). Inducing Self-Explanation: a Meta-Analysis. *EPR*. <https://eric.ed.gov/?id=EJ1186664>
- [C20] Paivio, A. (1971). Imagery and Verbal Processes（书）；Mayer, R. E. (2009). Multimedia Learning（书）.  <https://archive.org/details/imageryverbalpro0000paiv>；<https://eric.ed.gov/?id=ED530802>
- [C21] Sisk, V. F., et al. (2018). Growth Mind-Sets and Academic Achievement: Two Meta-Analyses. *Psychological Science*. <https://journals.sagepub.com/doi/10.1177/0956797617739704>
- [C22] Freeman, S., et al. (2014). Active learning increases student performance in STEM. *PNAS*. <https://doi.org/10.1073/pnas.1319030111>；<https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4018102/>
- [C23] Fiorella, L., & Mayer, R. E. (2016). Eight Ways to Promote Generative Learning. *EPR*, 28(4). <https://eric.ed.gov/?id=EJ1120458>
- [C24] Chase & Simon (1973). 专家以「组块」记忆棋局。 <https://doi.org/10.1016/0010-0285(73)90004-2>
- [C25] Nestojko, J. F., et al. (2014). Expecting to teach enhances learning.  <https://source.wustl.edu/2014/07/expecting-to-teach-enhances-learning-recall>
- [C26] Ye, J., Su, J., & Cao, Y. (2022). A Stochastic Shortest Path Algorithm for Optimizing Spaced Repetition Scheduling. *KDD*. <https://dl.acm.org/doi/10.1145/3534678.3539081>
- [C27] FSRS 生态：FSRS4Anki 主仓与算法 wiki。 <https://github.com/open-spaced-repetition/fsrs4anki>；<https://github.com/open-spaced-repetition/fsrs4anki/wiki>
- [C28] Arthur, W., et al. (1998). Factors that influence skill decay and retention. <https://doi.org/10.1207/s15327043hup1101_3>
- [C29] Settles, B., & Meeder, B. (2016). A Trainable Spaced Repetition Model for Language Learning. *ACL*. <https://research.duolingo.com/papers/settles.acl16.pdf>
- [C30] Shea, J. B., & Morgan, R. L. (1979). Contextual interference effects.  <https://gwern.net/doc/psychology/spaced-repetition/1979-shea.pdf>
- [C31] Ericsson, K. A., Krampe, R. T., & Tesch-Römer, C. (1993). The role of deliberate practice. *Psychological Review*. <https://psycnet.apa.org/doiLanding?doi=10.1037%2F0033-295X.100.3.363>
- [C32] Macnamara, B. N., Hambrick, D. Z., & Oswald, F. L. (2014). Deliberate Practice and Performance: A Meta-Analysis. *Psychological Science*. <https://pubmed.ncbi.nlm.nih.gov/24986855/>
- [C33] Gollwitzer, P. M., & Sheeran, P. (2006). Implementation Intentions and Goal Achievement: A Meta-Analysis.（NIH 存档 PDF） <https://cancercontrol.cancer.gov/sites/default/files/2020-06/goal_intent_attain.pdf>
- [C34] Ryan, R. M., & Deci, E. L. (2000). Self-Determination Theory. *American Psychologist*. <https://selfdeterminationtheory.org/SDT/documents/2000_RyanDeci_SDT.pdf>
- [C35] Bandura, A. (1977). Self-efficacy: Toward a unifying theory. *Psychological Review*. <https://pubmed.ncbi.nlm.nih.gov/847061>
- [C36] Locke, E. A., & Latham, G. P. (2002). Building a practically useful theory of goal setting. *American Psychologist*. <https://psycnet.apa.org/doiLanding?doi=10.1037%2F0003-066X.57.9.705>
- [C37] Zimmerman, B. J. (2002). Becoming a Self-Regulated Learner. <https://www.leiderschapsdomeinen.nl/wp-content/uploads/2016/12/Zimmerman-B.-2002-Becoming-Self-Regulated-Learner.pdf>
- [C38] Lally, P., et al. (2010). How are habits formed. *EJSP*. <https://doi.org/10.1002/ejsp.674>
- [C39] Hulleman, C. S., & Harackiewicz, J. M. (2009). Promoting Interest and Performance. *Science*. <https://doi.org/10.1126/science.1177067>
- [C40] Oettingen, G. (2012). Future thought and behaviour change. *ERSP*. <https://www.tandfonline.com/doi/full/10.1080/10463283.2011.643698>
- [C41] Ausubel, D. P. (1960). Advance organizers；Novak & Cañas 概念图理论。 <https://doi.org/10.1037/h0043805>；<https://cmap.ihmc.us/publications/researchpapers/theoryunderlyingconceptmaps.pdf>
- [C42] Meyer, J. H. F., & Land, R. (2003). Threshold concepts and troublesome knowledge. <https://www.research.ed.ac.uk/en/publications/threshold-concepts-and-troublesome-knowledge-linkages-to-ways-of-/>
- [C43] Gagné 九大教学事件（NIU 教学指南）。 <https://www.niu.edu/citl/resources/guides/instructional-guide/gagnes-nine-events-of-instruction.shtml>
- [C44] Collins, A., Brown, J. S., & Newman, S. E. (1989). Cognitive Apprenticeship. <https://files.eric.ed.gov/fulltext/ED284181.pdf>
- [C45] Dochy, F., et al. (2003). Effects of problem-based learning: A meta-analysis. *Learning and Instruction*. <https://eric.ed.gov/?id=EJ678509>
- [C46] Hattie, J., & Timperley, H. (2007). The Power of Feedback. *RER*. <https://doi.org/10.3102/003465430298487>
- [C47] Kluger, A. N., & DeNisi, A. (1996). The effects of feedback interventions. *Psychological Bulletin*. <https://psycnet.apa.org/record/1996-02773-003>
- [C48] Lave, J., & Wenger, E. (1991). Situated Learning. <https://www.cambridge.org/highereducation/books/situated-learning/6915ABD21C8E4619F750A4D4ACA616CD>
- [C49] Ahrens, S. (2017). How to Take Smart Notes；Luhmann 卡片盒。 <https://www.soenkeahrens.de/en/takesmartnotes>
- [C50] Dunning & Kruger (1999) 自我评估偏差；Koriat & Bjork (2005) 胜任错觉。 <https://doi.org/10.1037/0022-3514.77.6.1121>；<https://bjorklab.psych.ucla.edu/wp-content/uploads/sites/13/2016/07/Koriat_RBjork_2005.pdf>
- [C51] Pashler, H., et al. (2008). Learning Styles: Concepts and Evidence. *PSPI*. <https://journals.sagepub.com/doi/full/10.1111/j.1539-6053.2009.01038.x>
- [C52] Letrud (2012) 与 Subramony et al. (2014)：学习金字塔/保持率锥系神话。 <https://eric.ed.gov/?id=EJ996977>；<https://eric.ed.gov/?id=EJ1057239>
- [C53] Rayner, K., et al. (2016). So Much to Read, So Little Time. *PSPI*. <https://pubmed.ncbi.nlm.nih.gov/26769745/>
- [C54] Sala, G., & Gobet, F. (2019). Near and Far Transfer in Cognitive Training. *Collabra*. <https://online.ucpress.edu/collabra/article/5/1/18/113004/>
- [C55] Kirschner, P. A. (2017). Stop propagating the learning styles myth. *Computers & Education*. <https://doi.org/10.1016/j.compedu.2017.05.005>
- [C56] Bastani, H., et al. (2025). Generative AI without guardrails can harm learning. *PNAS*. <https://www.pnas.org/doi/10.1073/pnas.2422633122>
- [C57] Fan, Y., et al. (2025). Beware of metacognitive laziness. *BJET*. <https://bera-journals.onlinelibrary.wiley.com/doi/10.1111/bjet.13544>
- [C58] Kosmyna, N., et al. (2025). Your Brain on ChatGPT（预印本）. <https://www.media.mit.edu/publications/your-brain-on-chatgpt/>
- [C59] Kestin, G., et al. (2025). AI tutoring outperforms in-class active learning. *Scientific Reports*. <https://doi.org/10.1038/s41598-025-97652-6>
- [C60] Wang, R. E., et al. (2024). Tutor CoPilot. <https://arxiv.org/abs/2410.03017>
- [C61] Tabibian, B., et al. (2019). Enhancing human learning via spaced repetition optimization. *PNAS*. <https://www.pnas.org/doi/10.1073/pnas.1815156116>
- [C62] Mozer, M., et al. (2009). Predicting the Optimal Spacing of Study. *NeurIPS*. <https://papers.nips.cc/paper_files/paper/2009/file/6bc24fc1ab650b25b4114e93a98f1eba-Paper.pdf>
- [C63] Kulik, J. A., & Fletcher, J. D. (2016). Effectiveness of Intelligent Tutoring Systems. *RER*. <https://journals.sagepub.com/doi/10.3102/0034654315581420>
- [C64] VanLehn, K. (2011). Relative Effectiveness of Human Tutoring and ITS. *Educational Psychologist*. <https://www.tandfonline.com/doi/full/10.1080/00461520.2011.611369>；<https://asu.elsevierpure.com/en/publications/the-relative-effectiveness-of-human-tutoring-intelligent-tutoring/>
- [C65] Bloom, B. S. (1984). The 2 Sigma Problem. <https://gwern.net/doc/psychology/1984-bloom.pdf>
- [C66] Ebbinghaus (1885) 遗忘曲线（archive 原书）；Bjork & Bjork (2011) 合意困难；Craik & Lockhart (1972) 加工深度。 <https://archive.org/details/memorycontributi00ebbiuoft>；<https://bjorklab.psych.ucla.edu/publication/bjork-e-l-bjork-r-a-2014-making-things-hard-on-yourself-but-in-a-good-way-creating-desirable-difficulties-to-enhance-learning-in-m-a-gernsbacher-and-j-pomerantz-eds-psycholo/>
- [C67] Newell & Rosenbloom (1981) 练习幂律；Fitts & Posner (1967) 技能三阶段。 <https://iiif.library.cmu.edu/file/Newell_box00032_fld02190_doc0001/Newell_box00032_fld02190_doc0001.pdf>
- [C68] Vygotsky (1978) 最近发展区；Wood, Bruner & Ross (1976) 脚手架。 <https://archive.org/details/mindinsocietydev0000vygo>；<https://doi.org/10.1111/j.1469-7610.1976.tb00381.x>
- [C69] Krashen (1982) 输入假说；Nation (2006) 词汇覆盖率。 <https://www.sdkrashen.com/content/books/principles_and_practice.pdf>
- [C70] Csikszentmihalyi (1990) 心流（CUNY 开放 PDF）。 <https://files.blogs.baruch.cuny.edu/wp/blogs.dir/2418/files/2013/04/Mihaly-Csikszentmihalyi-Flow.pdf>
- [C71] Karpicke, J. D., & Blunt, J. R. (2011). Retrieval Practice Produces More Learning than Concept Mapping. *Science*. <https://learninglab.psych.purdue.edu/downloads/2011/2011_Karpicke_Blunt_Science.pdf>；<https://doi.org/10.1126/science.1199327>
- [C72] 延伸读物：Make It Stick / Peak / Ultralearning / Deep Work / Why We Sleep / A Mind for Numbers / How to Read a Book（各书官方页或书目页）。 <https://www.hup.harvard.edu/books/9780674729018>；<https://www.penguin.co.uk/books/421170/peak-by-anders-ericsson/9781473513143>；<https://www.scotthyoung.com/blog/ultralearning/>；<https://calnewport.com/books/deep-work/>；<https://www.penguinrandomhouse.com/books/550909/why-we-sleep-by-matthew-walker-phd/>；<https://www.penguinrandomhouse.com/books/314056/a-mind-for-numbers-by-barbara-oakley-phd/>；<https://archive.org/details/howtoreadabook1972edition>
- [C73] Rasch, B., & Born, J. (2013). About Sleep's Role in Memory. *Physiological Reviews*. <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3768102>

> ➕ 扩展文献库（[C74]–[C110]，37 条新增）见 [docs/references.md](./references.md)。

## 如何更新

发现新论文、错误引用或更好的数字口径？请按仓库 Issue 模板提交，附：论文链接、结论摘要、建议等级、替换理由。每次更新会在 CHANGELOG 记录。
