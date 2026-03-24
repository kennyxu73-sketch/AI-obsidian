# 开发进度控制 Skill 设计说明（P0纳入版）

## Project: AI-OB Progress Control Skill

## Version: v0.1 (P0-MVP)

## Status: Draft for P0 Execution

---


根据: [[000_Cabinet_System/Manuals/cursor 开发人机协作原则.md|
]]## 1. 目标定义（Why）

### 1.1 核心目标

构建一个“**轻量、可审计、可回滚**”的开发进度控制 Skill，用于每周自动评估项目健康度，辅助 Kenny 做决策。

### 1.2 解决的问题

- 周计划执行中容易陷入细节，缺少统一节奏控制。

- 多规则并行后，人工难以持续判断“是否偏航”。

- 新想法频繁出现，缺少结构化筛选与排期机制。

### 1.3 角色定位

> 该 Skill 是“**项目节奏控制器**”，不是“自动决策器”。

- 输出建议，不自动拍板。

- 关键结论由 Kenny 最终确认。

- 与小忆配合：小忆记录证据，Skill给建议分。

---

## 2. 设计原则（Principles）

1. **主权优先**：默认本地运行，不依赖云端服务。

2. **证据优先**：所有评分都要有日志/任务状态支撑。

3. **最小可逆**：失败可回滚，不影响主流程。

4. **先稳后强**：P0只做最小闭环，P1再增强自动化。

5. **不越权**：不替代审批，不直接修改 SSOT 资产。

---

## 3. 功能范围（P0 版本）

### 3.1 必做（P0 MVP）

- 读取本周计划与任务清单

- 读取审计/冲突日志（如 `CHANGELOG`, `path_conflict.log`）

- 输出 10 项检查卡建议分（建议 ✓/✗）

- 输出周状态灯：`🟢 健康` / `🟠 预警` / `🔴 偏航`

- 输出 Top3 风险与“下周唯一关键动作（One Thing）”

### 3.2 不做（P0 禁止）

- 自动改规则文件

- 自动审批或自动写入 SSOT

- 复杂多Agent并行编排

- 云端依赖型复杂推理

---

## 4. 输入输出定义（I/O Schema）

### 4.1 输入（Input）

```json

{

"week_id": "2026-W13",

"plan_file": "path/to/weekly_plan.md",

"task_file": "path/to/tasks.json",

"changelog_file": "path/to/CHANGELOG.md",

"conflict_log": "path/to/path_conflict.log",

"mode": "p0_mvp"

}

### 4.2 输出（Output）

{

"week_id": "2026-W13",

"health": "yellow",

"score": 7,

"checklist_advice": [

{"item":"单一主目标", "suggest":"pass", "evidence":"..."},

{"item":"审批边界", "suggest":"fail", "evidence":"..."}

],

"top_risks": [

"审批 pending 超时风险",

"日志漏记风险",

"任务插队导致偏航风险"

],

"one_thing_next_week": "完成P0-S4审批流闭环验证",

"go_no_go": "no-go"

}
```

---

## 5. 评分逻辑（P0 简化版）

- 总分 10 分（对应每周 10 项检查卡）
- 每项：
    - `pass` = 1
    - `warn` = 0.5
    - `fail` = 0
- 健康灯规则：
    - `>=8` -> 🟢
    - `5~7.5` -> 🟠
    - `<5` -> 🔴
- Go/No-Go：
    - `score >= 8` 且无红线事件 -> Go
    - 否则 -> No-Go

---

## 6. 与现有体系的集成点

### 6.1 与 `.cursorrules v1.6.x` 对齐

- 不绕过审批边界
- 不触发未授权写入
- 保持 Trigger-Based 同步机制

### 6.2 与小忆协同

- Skill 给“建议分”
- 小忆写“证据备注”
- Kenny 做“最终评分与决策”

### 6.3 与 Gap Engine 关系

- 当发现偏航风险时，写入 `Cognitive_Patch_Draft.md` 建议项
- 不直接执行修复动作

---

## 7. P0 路线图（执行计划）

### Week 1（P0-S3 同步期）

- 定义输入输出 schema
- 实现基础读取（plan/task/changelog/log）
- 输出纯文本建议报告（不含评分）

### Week 2（P0-S4）

- 加入 10 项检查卡评分逻辑
- 输出健康灯 + Go/No-Go
- 加入证据字段（evidence）

### Week 3（P0-S5 演练）

- 接入 soft-timeout 事件识别
- 演练 Full -> Lite 规则切换场景
- 完成一次周复盘实战

### Week 4（P0 Exit）

- 连续 2 周稳定运行
- 误报可控
- 形成固定周报模板

---

## 8. 验收标准（P0 Exit Criteria）

1. 能稳定读取输入文件并输出结构化建议
2. 建议分与人工判断基本一致（主观偏差可解释）
3. 无越权行为（不自动写 SSOT，不自动审批）
4. 周复盘可复现（同输入得出同结论）
5. 至少完成 2 次真实周报运行

---

## 9. 风险与对策

### 风险 A：评分误判

- 对策：输出 evidence，保留人工复核权

### 风险 B：日志不全导致误判

- 对策：缺失输入时降级为 `warn`，并提示“证据不足”

### 风险 C：功能膨胀

- 对策：P0 只允许 MVP 范围，新增功能放 P1 backlog

---

## 10. P1 预留（非本阶段）

- 趋势分析（连续周评分曲线）
- 自动生成周报草稿
- 与 Dify Tool 集成
- 与 n8n 定时任务联动

---



## 11. 最终结论（P0 纳入建议）

该 Skill 建议纳入 P0，定位为“节奏控制中枢”：

- 不替代 Kenny 决策
- 显著降低偏航概率
- 为 P1/P2 的自动化能力打地基