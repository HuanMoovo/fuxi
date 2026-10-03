# 深度剖析④ AI 时代的新风险：最危险的不是 AI 太强，而是「练习感」被偷走

> 五重风险 × 证据 → 机制 → 三步护栏协议 → 质量五问。本文是「[为什么需要伏羲框架](../why.md)」四论点的深度展开之四。
> 系列：[① 方法碎片化](fragmentation.md) · [② 伪科学横行](pseudoscience.md) · [③ 爽感陷阱](fluency-trap.md) · **④ AI 时代的新风险（本文）**

## 0. 症状自查

- [ ] 用 AI 写作业/代码/方案又快又好，但离开它写不出同等质量；
- [ ] 遇到问题的第一反应是「问 AI」，而不是先想 30 秒；
- [ ] 分不清 AI 输出里哪句是错的（它说得都很有道理）；
- [ ] 越用越依赖，独自推理的耐心明显下降。

## 1. 五重风险 × 证据

### ① 认知卸载：想得越少，越不会想
- **卸载理论**：人会把认知负担转移到外部载体（工具、他人、AI）；卸载即时省力，但有长期代价——被卸载的能力停止锻炼 [C221]；
- **随机实验（最硬的证据）**：无护栏使用生成式 AI 的学生，数学练习期表现提升约 **48%**，但撤掉 AI 后的考试**下降约 17%** [C56]；
- **调查证据（相关，非因果）**：2025 年一项研究显示 AI 工具使用频率与批判性思维得分负相关，认知卸载为中介变量 [C226]；
- **对照**：结构化、有护栏的 AI 导师实验则显著提升学习——差别不在 AI，而在**使用协议** [C59]。

### ② 幻觉：流畅的错误比生硬的错误更危险
- LLM 的幻觉是结构性特征而非零星 bug，任何「消除幻觉」的承诺都应打折听 [C222]；
- 经典实验早已证明：**无关的神经科学术语**能让坏解释被评为更可信 [C217]——AI 的流畅文风自带同一枚「可信滤镜」，且规模大了几个数量级。

### ③ 自动化偏误：越信，越不检查
- 系统综述（临床决策场景）：面对自动化建议，人会**系统性减少独立检查**，错误因此被放大 [C223]；
- 知识工作现场实验（「锯齿边界」）：在 AI 能力**之内**的任务上使用 AI 显著提速提质；在**边界之外**的任务上，用 AI 反而更容易做错——而边界常常不可见 [C224]。

### ④ 评价体系失效
- 前沿模型在各类标准化考试上的表现已接近或超过人类平均水平 [C227]——「考分」作为能力信号的可靠性在快速衰减；
- UNESCO 发布面向教育与研究的生成式 AI 指南，呼吁能力框架与伦理护栏 [C225]。

### ⑤ 认知分层加剧
- 岗位自动化争论仍在 9%–47% 的宽区间 [C182]；技术红利的分配并不均匀 [C201]；
- **推论（非证据）**：把 AI 当「代笔」和当「陪练」的两类人之间，能力差距将以复利方式扩大——这是本框架必须把「护栏」写进每一阶的原因。

## 2. 机制：AI 加速了「爽感陷阱」

```mermaid
flowchart LR
  A[答案直达<br/>零摩擦] --> B[无检索努力]
  B --> C[无合意困难]
  C --> D[遗忘加速 + 假自信]
  D --> E[更依赖 AI]
  E --> A
```

它与 [③ 爽感陷阱](fluency-trap.md) 的循环**同构**——AI 只是把循环的转速提高了十倍。

## 3. 三步护栏协议（本框架强制，已写入每一阶）

1. **独立尝试**：先自己答、自己写、自己推——哪怕错；
2. **质询与找错**：再让 AI 点评你的思路 / 找漏洞 / 出变式题（而不是要答案）；
3. **脱稿复现**：关掉 AI，重新独立完成一次，通过才算学会。

各阶示例：

| 阶段 | 正确用法示例 |
|---|---|
| ④ 编码 | 先写「最简解释」，再让 AI 指出解释里的漏洞 |
| ⑤ 检索 | 让 AI 当考官出题、评分、追问 |
| ⑦ 精练 | 让 AI 生成变式题（但要自己先做题再对答案） |
| ⑨ 教学 | 让 AI 扮演「听不懂的学生」来检验你的讲解 |

## 4. AI 输出质量五问（每次都要过一遍）

- [ ] 有出处吗？能点开核对原始来源吗？
- [ ] 我能独立验证这条信息吗（第二来源）？
- [ ] 这是我该练的技能，还是该外包的杂务？
- [ ] 我把它当导师（提问、找错），还是代笔（要成品）？
- [ ] 撤掉 AI，我能复现同等质量吗（或至少复现核心推理）？

## 检验清单

- [ ] 能说出无护栏 AI 实验的两个数字（+48% / −17%）；
- [ ] 自己的 AI 使用符合三步协议（有记录可查）；
- [ ] 用「五问」检查过至少一次 AI 输出；
- [ ] 能解释「锯齿边界」为什么让过度依赖特别危险。

## 参考（本文）

- [C56] Bastani et al. (2025). Generative AI without guardrails can harm learning（PNAS）
- [C59] Kestin et al. (2025). AI tutoring outperforms in-class active learning
- [C182][C201] 自动化与就业：[未来纪元](../expand/futures.md)
- [C221] Risko & Gilbert (2016). Cognitive Offloading（TiCS）: <https://pubmed.ncbi.nlm.nih.gov/27542527/>
- [C222] Ji et al. (2023). Survey of Hallucination in Natural Language Generation: <https://arxiv.org/abs/2202.03629>
- [C223] Goddard, Roudsari & Wyatt (2012). Automation Bias: A Systematic Review（JAMIA）: <https://pubmed.ncbi.nlm.nih.gov/21685142/>
- [C224] Dell'Acqua et al. (2023). Navigating the Jagged Technological Frontier: <https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4573321>
- [C225] UNESCO (2023). Guidance for Generative AI in Education and Research: <https://www.unesco.org/en/articles/guidance-generative-ai-education-and-research>
- [C226] Gerlich (2025). AI Tools in Society: Impacts on Cognitive Offloading and Critical Thinking: <https://www.mdpi.com/2075-4698/15/1/6>
- [C227] OpenAI et al. (2023). GPT-4 Technical Report: <https://arxiv.org/abs/2303.08774>

---

**导航**：[📚 文档总目录](../../README.md) ｜ [🏠 项目主页](../../README.md) ｜ [在线主页](https://HuanMoovo.github.io/fuxi/)
