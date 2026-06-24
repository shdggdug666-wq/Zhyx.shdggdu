# AI Agent 应用工程师 · 学习路线图

> 目标岗位:**AI Agent 应用工程师(AI4Science / 生命科学方向)**
> 适用画像:会一些 Python、有生物/生信背景、9–12 个月碎片时间、实战项目驱动
> 编制日期:2026-06
> 阅读方式:先看 §1 技能矩阵和 §2 总览,再逐阶段展开;每周末对照 §7 的检查表。

---

## 0. 这份课程的底层逻辑

岗位本质 = **用 Agent 工程方法,把生命科学领域的"数据 / 知识 / 工具"做成可被大模型调用的服务**。

它要四样东西:
1. **工具服务化能力**(MCP / Skills / FastAPI)—— 把生信工具变成 Agent 能用的"手"
2. **数据管道能力**(ETL:获取→解析→清洗→标注→合成→质控)—— Agent 的"粮食"
3. **知识管道能力**(RAG / KG / GraphRAG)—— Agent 的"记忆与推理"
4. **AI 编程 + 可靠性**(Cursor / Claude Code + 测试评估)—— 你的"造物效率"

你的生信背景直接命中"工具"和"数据"两个主场,所以课程把这两个作为**优势放大点**,把"知识管道"和"Agent 工程"作为**主攻新技术**。全程所有练习和项目都绑定生命科学场景,最终产出一个能讲故事的旗舰项目 + 一组作品集 + (可选)一篇 AI4Science 文章/专利草稿。

---

## 1. 技能矩阵:岗位要求 → 学习模块映射

| 岗位条目 | 类型 | 对应阶段 | 落地项目(作品集) |
|---|---|---|---|
| 熟练 Python + FastAPI/MCP 服务化开发 | 必备 | 阶段 A | `bio-mcp-server`:序列工具封装成 MCP 服务 |
| 熟悉一种 Agent 框架(LangChain/LangGraph/Agno) | 必备 | 阶段 D | 用 LangGraph 编排生信分析工作流 |
| 熟练 AI 编程工具(Cursor/Claude Code)+ 测试保证可靠性 | 必备 | 阶段 E(贯穿) | 用 Claude Code 全程开发 + pytest 评估集 |
| 数据解析合成 / 工具 MCP 封装 / 工作流编排 / GraphRAG(任一实战) | 必备(四选一,建议全做) | B / D / D / C | 四个里程碑项目全覆盖 |
| Skills/MCP 构建 + 业务流编排 + 提示词优化 | 职责 | A+D | 旗舰项目核心 |
| 优化数据管道(获取/解析/清洗/标注/合成/质控) | 职责 | B | `sci-data-etl` |
| 优化知识管道(实体关系抽取/分块/RAG/KG) | 职责 | C | `biokg-rag` |
| 编写 AI4Science 学术文章或专利 | 职责 | 收尾 | 一篇技术文章/专利草稿 |
| **加分** 生信工具链(序列检索比对/引物设计/结构预测) | 加分→**你的主场** | B+D | 直接做成 MCP 工具 |
| **加分** RAG 痛点优化(chunk/召回/重排/评估) | 加分 | C | RAG 评估闭环 + 优化对比实验 |
| **加分** Agent 驱动数据 ETL | 加分 | B+D | ETL 流水线由 Agent 调度 |

✅ 结论:这张表是**检验标准**——课程结束时,右边每一栏的项目你都应该能演示、能讲清原理、能把代码放上 GitHub。

---

## 2. 课程总览(约 40 周,可伸缩)

| 阶段 | 主题 | 周数 | 核心交付物 | 对标 |
|---|---|---|---|---|
| **A** | Python 工程化地基 | 3–4 | FastAPI 服务 + 工程骨架 | 要求1 |
| **B** | 生命科学数据管道 / ETL | 6–8 | `sci-data-etl` 流水线 | 职责2 + 加分3 |
| **C** | 知识管道:RAG / KG / GraphRAG | 8–10 | `biokg-rag` + 评估闭环 | 职责3 + 加分2 |
| **D** | Agent 工程:MCP / 框架 / 工作流 | 8–10 | `bio-mcp-server` + LangGraph 工作流 | 要求2/4 + 职责1 + 加分1 |
| **E** | AI 编程工具 + 可靠性工程 | 贯穿 + 4 周集中 | 测试评估集 + CI | 要求3 |
| **旗舰** | 生命科学 Agent 产品 | 4–6(与 C/D 重叠) | 可演示的完整产品 | 全岗 |
| **收尾** | 论文/专利 + 作品集 + 求职 | 2–3 | 文章草稿 + 作品集站 | 职责4 |

> 碎片时间(6–10 小时/周)建议:每周 **1 个"学习块"(2–3h 看文档/教程)+ 2 个"动手块"(2–3h 写代码)**,周末做整合。

---

## 3. 阶段详解

### 阶段 A · Python 工程化地基(3–4 周)
> 目的:把"会一些 Python"升级到"能写出工业级服务"。这是 FastAPI/MCP 的前置。

**核心知识点**
- 现代工程工具链:`uv`(或 poetry)管依赖、虚拟环境、`.env` 配置、`ruff`/`black` 格式化、Git 工程化提交
- 类型注解 + `Pydantic v2`(数据校验,MCP/FastAPI 的灵魂)
- 异步基础:`async`/`await`、`asyncio`、为什么 LLM 调用都要异步
- **FastAPI**:路由、依赖注入、Pydantic 模型、异步端点、自动文档、异常处理
- `pytest` 基础:写第一个测试,理解"测试保证可靠性"

**实战项目(本阶段交付)**
- `bio-api`:用 FastAPI 写 3 个端点
  - `POST /translate` 输入 DNA 序列返回翻译蛋白(复习你的生信基础)
  - `GET /gc-content` 计算 GC 含量
  - `GET /blast` 包一层 NCBI BLAST 调用(用 Biopython)
- 配上 `pytest` 测试 + 一份 `README`

**资源(官方优先)**
- FastAPI 官方教程(逐章过,重点:路径参数/请求体/依赖注入/异步)
- Pydantic v2 官方文档
- `uv` 官方文档(替代 pip/venv 的现代方案)
- Real Python 上 pytest 入门

**检验标准(做到才算过关)**
- [ ] 能用 `uv` 从零搭一个项目并跑起来
- [ ] 能写出带类型注解 + Pydantic 模型的 FastAPI 服务
- [ ] 服务有 ≥3 个端点 + ≥3 个 pytest 用例
- [ ] 能讲清"为什么 LLM 应用要用异步"

---

### 阶段 B · 生命科学数据管道 / ETL(6–8 周)
> 目的:这是你的**主场**。目标是把"生命科学多类型数据的获取/解析/清洗/标注/合成/质控"做成一条可被 Agent 调度的 ETL 流水线。直接命中**职责2 + 加分项3**。

**核心知识点**
- 数据获取:NCBI Entrez(E-utilities)、UniProt REST API、PDB/RCSB API、PubMed 文献;异步并发抓取 + 限流 + 重试
- 数据解析:FASTA/GenBank(用 Biopython)、PDB 结构、PDF 文献(用 `pypdf`/`markitdown`/`unstructured`)、表格数据(`polars`/`pandas`)
- 数据清洗:去重、标准化(基因名/物种名归一)、异常值识别
- 数据标注与合成:用 LLM 做弱标注/合成数据(如生成问答对)、合成数据质量控制
- 质控(QC):覆盖率、完整性校验、统计画像
- 编排:用 `prefect` 或简单 DAG 把上述步骤串成流水线;**为后面 Agent 调度埋点**

**实战项目(本阶段交付):`sci-data-etl`**
- 一条流水线:从 PubMed 拉文献 → 解析正文/图表 → 抽取结构化字段 → 清洗归一 → 质控报告
- 一条流水线:从 NCBI 拉一批基因序列 → 解析 → GC/长度 QC → 落库
- 每步可独立测试,有日志和失败重试
- **加码**:用 LLM 把文献自动合成成"问答训练对",并做合成数据质控(命中加分项3的"数据合成、质控")

**资源**
- NCBI E-utilities 官方手册、Biopython 教程(`Entrez`、`SeqIO`)
- UniProt / RCSB PDB 官方 API 文档
- Prefect 官方入门(或轻量用自己写的状态机)

**检验标准**
- [ ] 能稳定异步抓取 ≥3 类生命数据源(文献/序列/结构)
- [ ] 有完整的解析→清洗→QC 流程,每步有测试
- [ ] 做过一次 LLM 合成数据 + 质控,能讲清合成数据的坑(幻觉、分布偏移)
- [ ] 流水线可被一个简单脚本/Agent 调用触发(为阶段D埋点)

---

### 阶段 C · 知识管道:RAG / KG / GraphRAG(8–10 周)
> 目的:**主攻新技术之一**。命中职责3(实体关系抽取/智能分块/RAG/KG)+ 加分项2(RAG 痛点优化)。这是最容易出彩、面试最爱问的部分。

**核心知识点(C1–C4 四块)**

- **C1 · RAG 基础**:Embedding 模型选择、向量库(Chroma/Qdrant/PGVector)、检索-生成链路、`LlamaIndex` 或 `LangChain` 的 retriever
- **C2 · 智能分块(chunking)**:固定/递归/语义/基于结构(按章节/表格/图注)分块;**生命科学文献的特殊分块**(摘要/方法/结果/表格图注分开处理)
- **C3 · 召回 + 重排(rerank)**:混合检索(向量+BM25)、交叉编码器重排(cross-encoder rerank)、召回率/精确率调优
- **C4 · 实体关系抽取 + 知识图谱(KG)**:用 LLM/NER 抽实体(基因/蛋白/疾病/药物)+ 关系;存入图库(Neo4j 或 NetworkX);**GraphRAG**(微软 GraphRAG 思路:社区检测 + 层次摘要)
- **贯穿 · 评估闭环**:RAGAS / 自建评估集,量化召回命中率、答案忠实度、上下文相关性——**这是加分项2的核心(RAG 痛点优化 = 能用数字说话)**

**实战项目(本阶段交付):`biokg-rag`**
- 在阶段 B 抓取的生命科学文献上,构建一个**可问答的知识库**
- 两套检索对比:① 纯向量 RAG;② GraphRAG(抽取实体关系建图 + 图增强检索)
- 建一个 ≥50 条的评估集,跑出基线指标,然后做 ≥3 轮优化实验(改分块/加重排/调召回数),画出指标对比表
- 产出一份**《RAG 痛点优化实验报告》**(这就是面试时最有杀伤力的作品)

**资源**
- LangChain / LlamaIndex 官方 RAG 教程(最新版,以官方为准)
- 微软 GraphRAG 项目(README + 论文)
- RAGAS 文档;cross-encoder rerank(`bge-reranker` / Cohere rerank)
- Neo4j 官方 + LLM 图谱构建(`GraphRAG` / `neo4j-graphrag`)

**检验标准**
- [ ] 能从零搭一个 RAG,并能讲清每一步在做什么
- [ ] 实现 ≥2 种分块策略并对比
- [ ] 实现混合检索 + 重排,指标有明显提升
- [ ] 用 LLM 抽过实体关系并建过 KG
- [ ] **有一份带数字的评估报告**(这是加分项2的硬证据)

---

### 阶段 D · Agent 工程:MCP / 框架 / 工作流(8–10 周)
> 目的:**主攻核心技术**。命中职责1(Skills/MCP 构建 + 业务流编排)+ 要求2(Agent 框架)+ 要求4(MCP封装/工作流编排)+ 加分项1(生信工具链)。这是岗位的"心脏"。

**核心知识点(D1–D3 三块)**

- **D1 · MCP(Model Context Protocol)**:MCP 是什么、server/client/resources/tools/prompts 五要素、用官方 SDK(Python)写 MCP server、在 Claude Desktop / Cursor 里挂载调试
- **D2 · Agent 框架**:选 **LangGraph** 作为主力(显式状态机,适合生信这种有明确步骤的分析流);了解 LangChain 基础组件、Agno 作为对比;ReAct / 工具调用 / 多步规划
- **D3 · 工作流编排**:用 LangGraph 把"检索→调用生信工具→分析→生成报告"编成有状态的图;人在回路(human-in-the-loop)、错误恢复、并行工具调用

**实战项目(本阶段交付)**
1. **`bio-mcp-server`(核心)**:把你的生信工具封装成一个 MCP server,至少包含:
   - `blast_search`(序列检索比对)
   - `primer_design`(引物设计)
   - `structure_predict`(结构预测——可包 ESMFold/ColabFold API)
   - `get_sequence`/`gc_content` 等基础工具
   - → 可在 Claude Desktop / Cursor 里直接被 Agent 调用演示
2. **`bio-agent-workflow`**:用 LangGraph 编排一个"分子生物学分析工作流":
   - 输入一个基因名 → Agent 自动:查序列 → 设计引物 → BLAST 验证 → 结构预测 → 汇总报告
   - 有状态、有错误处理、可人在回路确认

**资源**
- **MCP 官方文档**(modelcontextprotocol.io)+ Python SDK 示例(以官方最新为准)
- LangGraph 官方教程 + LangChain Academy(免费)
- ESMFold / ColabFold API 文档(结构预测封装)
- Primer3(PyPI `primer3-py`)用于引物设计封装

**检验标准**
- [ ] 能独立写一个 MCP server 并在 Claude Desktop 里跑通
- [ ] 生信工具被正确封装(参数校验/错误返回/文档齐全)
- [ ] 能用 LangGraph 画出并跑通一个多步工作流
- [ ] 工作流有错误处理和(至少一处)人在回路

---

### 阶段 E · AI 编程工具 + 可靠性工程(贯穿全程 + 4 周集中)
> 目的:命中要求3(熟练 Cursor/Claude Code,能提效并能测试保证可靠性)。这不是单独阶段,而是从 A 开始就要养成的工作方式,最后 4 周系统化提升。

**核心知识点**
- **Claude Code / Cursor 工作流**:项目上下文管理、`CLAUDE.md`、子代理(subagent)、规则文件、如何拆任务给 AI
- **用 AI 提效但保证可靠**:AI 写的代码必须配测试;评估驱动开发(Eval-Driven Development)——给 LLM 功能写评估集,改提示词看分数
- **LLM 应用的测试与评估**:单元测试 + 端到端评估 + 回归集;用 pytest + 自建评估跑分;CI(GitHub Actions)自动跑测试和评估
- **提示词工程系统化**:结构化提示、少样本、思维链、工具调用提示——命中职责1的"提示词优化"

**实践(本阶段交付)**
- 从阶段 A 起就用 Claude Code 主力开发,持续维护 `CLAUDE.md`
- 给阶段 C 的 RAG 和阶段 D 的 Agent 各建一套评估集
- 配 CI:每次提交自动跑 pytest + 关键评估指标

**资源**
- Claude Code 官方文档 / Cursor 官方文档
- Anthropic 提示词工程指南(prompt engineering + tool use)
- Eval-Driven Development 相关博客(搜 "eval driven development LLM")

**检验标准**
- [ ] 全程主力用 AI 编程工具,且能讲清怎么"提效又不失控"
- [ ] 每个核心模块有测试 + 评估集
- [ ] 有 CI 在跑(至少 pytest)

---

## 4. 旗舰项目 · 生命科学 Agent 产品(与 C/D 重叠 + 4–6 周集中打磨)
> 这是你的**王牌作品集**。把前面所有技能汇聚成一个能演示、能讲故事的完整产品。建议方向(选一个深入):

**候选方向(任选其一,挑你最熟的生信场景)**
- **A.「文献→假设」科研助手 Agent**:输入一个生物学问题 → Agent 检索文献(GraphRAG)→ 抽取实体关系(KG)→ 调用生信工具验证 → 生成带引用的研究假设报告
- **B.「序列→洞察」分子分析 Agent**:输入基因/蛋白 → 自动完成检索/比对/引物/结构预测/功能注释流水线 → 生成可交互分析报告
- **C.「数据 ETL」Agent 驾驶舱**:用 Agent 调度阶段 B 的 ETL,自然语言指挥"帮我拉某物种所有相关文献并质控",Agent 自动编排工具

**旗舰项目必须包含**
- 可演示的入口(CLI / 简单 Web 界面 / Claude Desktop 技能)
- ≥1 个自研 MCP server(生信工具)
- ≥1 套 RAG 或 GraphRAG 知识检索
- LangGraph 工作流编排
- 评估集 + 一份《效果与可靠性报告》
- GitHub 仓库 + README + 架构图 + 演示视频(2–3 分钟)

> 这个项目就是你面试时 80% 的谈资。它的深度直接决定你能否拿到 offer。

---

## 5. 收尾 · 论文/专利 + 作品集 + 求职(2–3 周)
> 命中职责4(编写 AI4Science 文章或专利)+ 把前面成果"包装"出去。

- **技术文章/专利草稿**:把旗舰项目里一个有新意的点(如"生命科学文献的 GraphRAG 分块策略"或"生信工具的 MCP 封装范式")写成一篇技术博客 / arXiv 预印本 / 专利交底书草稿。不必完美,要有。
- **作品集**:一个简单网站(GitHub Pages 即可),罗列 5 个项目(阶段 A/B/C/D + 旗舰),每个一段话讲清"解决了什么、用了什么、效果数字"。
- **简历改写**:把每个项目映射到岗位 JD 的具体条目(用 §1 的表格语言)。
- **求职准备**:准备 3 个能深聊的技术故事(RAG 优化、MCP 封装、工作流编排),每个能讲到代码细节。

---

## 6. 工具与资源清单

**语言与工程**:Python · `uv` · `ruff` · Pydantic v2 · FastAPI · pytest · Git · GitHub Actions
**数据/生信**:Biopython · NCBI E-utilities · UniProt API · RCSB PDB · `primer3-py` · ESMFold/ColabFold
**AI 编程**:Claude Code(主力,你已经在用)· Cursor
**Agent / MCP**:MCP Python SDK · LangGraph · LangChain ·(了解)Agno
**知识管道**:LlamaIndex · Chroma/Qdrant · Neo4j · RAGAS · `bge-reranker` · 微软 GraphRAG
**LLM**:Anthropic Claude API / OpenAI API(选一个主力,建议 Claude,与岗位工具一致)
**学习资源(优先官方文档)**
- DeepLearning.AI 短课(LangChain / RAG / MCP / Agent 系列,免费,质量高)
- LangChain Academy(LangGraph,免费)
- 李宏毅 生成式 AI / LLM 课程(B 站,中文,补理论)
- Anthropic 提示词工程 + Tool Use 官方指南
- 各框架官方文档(版本变化快,**一律以官方最新文档为准**)

---

## 7. 每周节奏与里程碑检查表

**典型一周(6–10h)**
- 工作日 2–3 个晚上 × 1.5h:看文档/教程,记笔记
- 周末 1 个 3–4h 大块:动手写项目代码,做整合
- 每天 10min:逛 AI Agent 新产品(命中要求5"喜欢体验各类 Agent 产品"——这也是硬性要求!)

**里程碑 Gate(每个阶段结束自测,过不了别硬推进)**
- [ ] Gate A:FastAPI 服务能跑 + 有测试(第 4 周)
- [ ] Gate B:ETL 流水线跑通一类数据 + QC(第 12 周)
- [ ] Gate C:RAG + 评估报告有数字(第 22 周)
- [ ] Gate D:MCP server 在 Claude Desktop 跑通 + LangGraph 工作流(第 32 周)
- [ ] Gate 旗舰:可演示产品 + 演示视频(第 38 周)
- [ ] Gate 收尾:文章草稿 + 作品集上线(第 40 周)

> 节奏可伸缩:全职可压缩到 3–4 个月;若某阶段卡住,允许延后 1–2 周,但**不要跳过测试和评估**——那是"可靠性"的命门。

---

## 8. 第一步:本周(第 1 周)立刻开始

别等"准备好"。这周只做三件事:
1. **装好工具链**:装 `uv`、Claude Code(你已有)、VS Code;用 `uv init` 建第一个项目仓库,提交到 GitHub。
2. **过 FastAPI 官方教程前 5 节**(路径参数、请求体、查询参数、Pydantic 模型、异步基础)。
3. **写第一个端点**:`POST /gc-content` 输入 DNA 序列返回 GC 含量,配 1 个 pytest。能跑通就算开工成功。

> 记住:你最大的优势是**生信背景**。当别人还在学"序列是什么"时,你已经在把它封装成 MCP 工具了。全程把生命科学当试验田,这是你区别于普通"AI 工程师"求职者的核心壁垒。
