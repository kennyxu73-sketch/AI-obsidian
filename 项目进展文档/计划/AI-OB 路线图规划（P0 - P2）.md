---
aliases:
  - AI-OB 路线图规划（P0 -> P2）
---

# AI-OB 路线图（P0 -> P2）

## 目标：从“可运行”到“可规模化”再到“可产品化”

| 阶段 | 步骤（Step） | 关键功能（Function） | 里程碑（Milestone） | 核心要点（Key Points） | 通过标准（Exit Criteria） |

| **阶段**                               | **步骤 (Step)**      | **关键功能 (Function)**                      | **里程碑 (Milestone)**                 | **核心要点 (Key Points)**  | **通过标准 (Exit Criteria)**       |
| ------------------------------------ | ------------------ | ---------------------------------------- | ----------------------------------- | ---------------------- | ------------------------------ |
| **P0 启动期**<br><br>  <br><br>(2-4周)   | **S1: 路径与规则锁定**    | Canonical Path、`.cursorrules` Full、生效校验  | 路径冲突可检测，Legacy 写入被彻底拦截              | 先“防错”，再“提效”；**禁止双写**   | Legacy 拦截率 100%，SSOT 未审批写入 = 0 |
|                                      | **S2: 画像与协议**      | `Kenny_Cognitive_Profile` 读取、Why->How 输出 | AI 回答稳定符合“主权优先/本地优先”                | 让系统先“**懂你**”，再“**帮你**” | 正反例测试通过（红线请求被拦截拒绝）             |
|                                      | **S3: 封装 MVP**     | `enseal_skill.py`、`tag_schema.json` 校验   | 输入文本可产出 Triple-A (Runtime/SSOT 双模式) | 先跑最小闭环，不做复杂自动化         | SSOT Triple-A 资产完整率 100%       |
|                                      | **S4: 审批与审计**      | Drafts 审批流、`CHANGELOG` JSON、Ref_ID       | Pending/Approved/Rejected 可追踪回放     | 审计链要“**能追责、能回滚**”      | 关键变更漏记率 = 0                    |
|                                      | **S5: 守卫与降级**      | SSOT 结构护栏、动态白名单、软超时、只读降级                 | Full -> Lite 演练通过                   | 先验证“**出故障也安全**”        | 8h/24h/72h 状态机演练全部通过           |
| **P1 稳定期**<br><br>  <br><br>(4-8周)   | **S1: 历史数据导入**     | 4G 笔记分批入库（A/B 级优先）                       | 每批具备导入报告与审计摘要                       | **不全量硬灌**，按批次处理，支持随时暂停 | 批次成功率稳定，冲突率随时间下降               |
|                                      | **S2: 流程产品化**      | 审批流 UI/UX 优化、积压提醒、恢复机制                   | 审批超时自动降级 + 恢复闭环                     | 防“长期挂起”与“人工遗忘”         | 超时后无任何违规写入 SSOT 的记录            |
|                                      | **S3: 检索 P1 版**    | Notes/System 两域检索（Summary->Chunk）        | 检索结果可直接辅助周决策                        | 先求“**稳准**”，再扩域到 Code 域 | 误召回率显著下降，回答可解释性提升              |
|                                      | **S4: 可视化运营**      | 审计/冲突/进度 Dashboard (看板)                  | 周维度可见系统健康状态指标                       | **指标驱动**，不靠感性体感        | 周报自动产出且具备可复盘的客观数据              |
|                                      | **S5: 周运营闭环**      | 周计划-日执行-周复盘-知识沉淀                         | 每周形成“**结论资产**”                      | 任务管理与信息管理一体化运营         | 周目标达成率建议值 >= 70%               |
| **P2 智能化期**<br><br>  <br><br>(8-16周) | **S1: 多 Agent 编排** | 小报/小黑/小酷/小忆标准接口与交接                       | 并行处理 + 失败自动回滚机制上线                   | 职责边界清晰，运行状态全程可观测       | 编排失败时系统可自动回退到稳定状态              |
|                                      | **S2: 三域 RAG 升级**  | Notes/System/Code 三域覆盖 + Rerank          | 检索质量与广度显著提升                         | 降低幻觉，提升**精确召回**率       | 问答正确率与稳定性指标持续爬升                |
|                                      | **S3: 主动智能**       | 自动任务建议、风险预警、偏航提醒                         | 系统可主动提供“下一步行动”建议                    | 从“被动工具”进化为“**主动助手**”   | 人工介入时长明显下降（目标 30%+）            |
|                                      | **S4: 回忆录引擎**      | AI 采访追问、章节化输出、风格一致性                      | 高质量回忆录文档持续规模化产出                     | **情感事实双轨沉淀**           | 周产出稳定，AI 生成内容的返工率下降            |
|                                      | **S5: 成本性能治理**     | 本地优先调度、Token/时延预算管理                      | 产出质量与运行成本达到动态平衡                     | 可持续运行，避免系统越跑越贵         | 成本波动可预测，服务可用性 (SLA) 达标         |

---

## 阶段切换闸门（Go/No-Go）

- **P0 -> P1**：路径与审计稳定、Triple-A 完整、守卫机制演练通过。

- **P1 -> P2**：分批导入稳定、审批积压可控、检索质量达标、周运营闭环稳定。

- **P2 持续优化**：多Agent可靠、主动智能有效、成本可控且无主权事故。

---

## 每周固定节奏（建议）

- 周一：周目标与里程碑对齐

- 周中：功能开发 + 审批处理 + 风险清单更新

- 周六：信息分级与去噪（A/B/C/D）

- 周日：周复盘（指标、偏差、下周策略）


~~~mermaid

gantt
    title AI-OB P0 战役：物理主权与规矩建立
    dateFormat  YYYY-MM-DD
    section S1: 路径锁定
    物理路径映射 (3090<->Mac)      :active, p0s1_1, 2026-03-23, 2d
    部署 .cursorrules-Full (v1.6.7) :p0s1_2, after p0s1_1, 2d
    section S2: 画像对齐
    Kenny_Cognitive_Profile 补全  :p0s2_1, 2026-03-27, 2d
    正反例指令对抗测试             :p0s2_2, after p0s2_1, 1d
    section S3: 工具封装
    enseal_skill.py (MVP开发)     :p0s3_1, 2026-03-30, 4d
    tag_schema.json 自动化校验接入  :p0s3_2, after p0s3_1, 2d
    section S4: 审计溯源
    CHANGELOG JSON 记账规则建立    :p0s4_1, 2026-04-05, 2d
    Drafts 审批流实战演练          :p0s4_2, after p0s4_1, 2d
    section S5: 韧性演练
    软超时与只读降级压力测试        :crit, p0s5, 2026-04-09, 4d
    P0 退出评审 (Go/No-Go)        :milestone, p0m, 2026-04-13, 1d
~~~


~~~mermaid

gantt
    title AI-OB P1 战役：资产炼化与业务建模
    dateFormat  YYYY-MM-DD
    section S1: 数据分迁
    4G 笔记 A/B 级分批清洗入库     :active, p1s1, 2026-04-14, 10d
    section S2: 流程治理
    审批流产品化 (自动化积压处理)   :p1s2, after p1s1, 6d
    section S3: 语义检索
    Notes/System 双域检索 P1 版    :p1s3, after p1s2, 7d
    section S4: 运营可视化
    内阁运行看板 (Dashboard) 搭建  :p1s4, after p1s3, 5d
    section S5: 闭环固化
    周计划-日执行-周复盘流程走通    :p1s5, after p1s4, 5d
    P1 退出评审 (Go/No-Go)        :milestone, p1m, 2026-05-17, 1d
~~~


~~~mermaid

gantt
    title AI-OB P2 战役：全自动驾驶与产品化（融合版）
    dateFormat  YYYY-MM-DD
    axisFormat  %m/%d
    excludes    weekends

    section S1: Agent 编排
    多 Agent 串联与失败回滚机制               :p2s1, 2026-05-18, 10d

    section S2: RAG 进化
    三域 RAG（含 Code 域）+ Rerank            :p2s2, after p2s1, 12d

    section S3: 主动智能（含 Gap Engine v2.0）
    Gap Engine v2.0 Shadow 模式（只报告）     :p2g1, after p2s2, 4d
    Gap Engine v2.0 Assist 模式（建议不执行） :p2g2, after p2g1, 4d
    任务建议与风险偏航预警（Controlled）      :p2s3, after p2g2, 8d
    主动->被动快速回滚（风险对冲）            :crit, p2s3r, after p2s3, 4d

    section S4: 回忆录引擎
    憶镜项目采访追问算法增强                  :p2s4, after p2s3r, 8d

    section S5: 效能治理
    成本/性能治理（GPU/Token 预算）           :p2s5, after p2s4, 7d
    超预警自动降级机制（风险对冲）            :crit, p2s5r, after p2s5, 4d

    section P2 验收
    P2 最终验收（Production Ready）           :milestone, p2m, 2026-07-20, 1d

~~~


