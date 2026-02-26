---
title: 内阁资产：YAML 处理与封装规则
date: 2026-02-15
deadline: 2026-02-23
本文件版本: 1.6.0
primary_agent: 小酷
file_type: doc/standard
project_ref: "[[000_Cabinet_System/AI obsidian]]"
importance: 5
review_status: Approved
tags:
  - "#内阁基建/协议"
  - "#治理/资产重塑"
  - "#策略/时间主权"
audit_status: 🚀 V1.6 协议全量封顶
audit_summary: |
  本规范定义了内阁资产治理的终极 YAML 标准。V1.6 核心引入“时间二元论”，通过 Created Date 锁定物理起源，通过 Deadline 锁定任务目标。确立了 history_logs 的全量说明义务，严禁 AI 臆断历史，确保每一份资产的演进脉络清晰、真实、可审计。
audit_keywords:
  - "[[时间戳主权]]"
  - "[[时间二元论]]"
  - "[[V1.0 溯源原则]]"
  - "[[静默重塑]]"
  - "[[资产自愈]]"
audit_weights:
  小酷: 1
  小黑: 0.7
system_meta:
  file_id: CABINET-STRATEGY-001
  parent_doc: "[[内阁数字化治理大纲]]"
  protocol_v: yaml 版本:1.6
  kenny_notes: |
    [2026-02-23]: Kenny 终审 V1.6。
    [核心逻辑]: 确立 Created Date 为唯一真实起源，Deadline 为可选目标点。
    [操作红线]: history_logs 第一条必须对齐 date 字段。Tag 不允许带版本号，Keywords 必须双链。
  history_logs:
    - V1.6 | 2026-02-23 | 时间主权：引入时间二元论（Created/Deadline）。纠正 Tag 与 Keywords 逻辑错误。强制 history_logs 首条对齐 date 字段，实现全量历史说明封顶。
    - V1.5.3 | 2026-02-23 | 架构优化：将 protocol_v 移入 System Meta。确立“格式自动换装，内容人工把关”的静默更新逻辑。
    - V1.5.2 | 2026-02-23 | 约束闭环：确立字段约束等级（🔴必填/🟡推荐/🟢可选），完善资产重塑红线。
    - V1.5.1 | 2026-02-23 | 维护优化：执行“去版本化”策略，简化维护负担。
    - V1.5 | 2026-02-23 | 全息感应：引入整体设计原则，确立元数据全景感应机制。
    - V1.4 | 2026-02-23 | 纵横闭环：引入 project_ref 字段，实现资产与项目的坐标交汇。
    - V1.3 | 2026-02-21 | 架构分层：确立 Core View / Audit Layer / System Meta 三层解耦结构。
    - V1.2 | 2026-02-19 | 分类扩容：定义 doc/* 与 card/* 族群分类规范。
    - V1.1 | 2026-02-15 | 字段标准化：初步确定 title, date 等基础字段，剔除冗余字段。
    - V1.0 | 2026-02-15 | 协议诞生：确立内阁数字化重塑的元数据封装理念，开启主权资产治理。
---

# 内阁资产：YAML 处理与封装规则 (V1.5.3)

## 一、 整体设计原则 (General Design Principles)

_本原则是内阁数字化基建的底层宪法，是所有 Agent 处理资产的最高准则：_

1. **资产全息化 (Holographic Assets)**：元数据必须通过 `[[双链]]` 成为可跳转、可感应的逻辑节点。
    
2. **纵横坐标系 (Matrix Coordinate)**：通过 `file_type` (纵向族群) 与 `project_ref` (横向项目) 确立资产唯一坐标。
    
3. **血缘守恒 (Ancestry Conservation)**：通过 `parent_doc` 确保碎片资产不丢失体系语境，杜绝产生孤儿文件。
    
4. **后台静默重塑 (Silent Background Refactoring)**：**[V1.5.3 核心]** 当后台 YAML 规则升级时，AI 自动遍历并静默更新协议版本及格式，若无内容冲突则不打扰统帅。
    
5. **约束等级制 (Constraint Grading)**：明确区分必填（🔴）、推荐（🟡）与可选（🟢）字段。必填项缺失将导致资产被判定为“逻辑残损”。
    
6. **内容终审权 (Final Review Authority)**：**[V1.5.3 最高原则]** AI 仅负责格式对齐与合并提案。任何涉及内容实质变更、思路合并或逻辑冲突的操作，必须通过 `review_status: "Pending"` 触发人工审核。
7. **时间戳主权 (Timestamp Sovereignty)**：`date` 锁定资产真实的物理起源。
8. **时间二元论 (Dual-Date Theory)**：区分 `date` (出生日期) 与 `deadline` (结束日期)。    

---

## 二、 YAML 全量字段规范与约束等级 (V1.5.3)

### 1. 核心展示层 (Core View) - 纵横定位与时间主权

|**字段名**|**约束等级**|**执行逻辑与红线要求 (Redline)**|
|---|---|---|
|**`title`**|**🔴 必填**|资产逻辑名。AI 跨文件感应的核心标识。|
|**`date`**|**🔴 必填**|**Created Date**。锁定诞生日期。取值：正文日期 > 文件创建日期。|
|**`deadline`**|**🟢 可选**|**Finish Date**。锁定任务/日志截止点。若无明确期限则不填。|
|**`本文件版本`**|**🔴 必填**|**业务展示版本**。标记内容演进（如：1.6.0）。|
|**`primary_agent`**|**🔴 必填**|责任人（小酷/小康/小镜/小憶/小报）。|
|**`file_type`**|**🔴 必填**|族群：`doc/standard` (协议), `doc/report` (报告), `card/*` (碎片)。|
|**`project_ref`**|**🟡 推荐**|**强制双链** `[[ ]]`。关联横向项目看板。|
|**`review_status`**|**🔴 必填**|**状态闸门**：`Approved` (已对齐); `Pending` (需审核)。|
|`importance`|**🟡 推荐**|资产权重 (1-5)。|

### 2. 深度审计层 (Audit Layer) - 全息感应

|**字段名**|**约束等级**|**执行逻辑与红线要求 (Redline)**|
|---|---|---|
|**`audit_summary`**|**🔴 必填**|**全息总结**。内容重塑时由 AI 自动重提炼。摘要巨变需 Pending。|
|**`audit_keywords`**|**🟡 推荐**|**推荐双链** `[[ ]]`。实现逻辑感应。|
|`audit_status`|🟢 可选|演进标志（如：🚀 协议封顶）。|

### 3. 系统追踪层 (System Meta) - 自动化维护

|**字段名**|**约束等级**|**执行逻辑与红线要求 (Redline)**|
|---|---|---|
|**`file_id`**|**🔴 必填**|**唯一识别码**。用于逻辑自愈与追踪，严禁人工修改。|
|**`protocol_v`**|**🔴 必填**|**技术协议水位**。当前水位：`"yaml 版本:1.6"`。|
|**`history_logs`**|**🔴 必填**|**编年史**。**[V1.6 红线]**：第一条必须引用 `date` 值为 V1.0。|
|`parent_doc`|**🟡 推荐**|**强制双链** `[[ ]]`。锁定纵向归属。|
|`kenny_notes`|🟢 可选|统帅批复、特殊指示与偏好留痕。|

## 三 自动维护与重塑协议 (Automation & Refactoring Protocols)

**这是 AI 执行全库治理时的“操作手册”：**

1. **水位感应与触发 (Sensing)**：
    
    - **逻辑**：Agent 扫描时，对比文件的 `system_meta.protocol_v` 与系统当前法定版本（1.53）。
        
    - **触发**：若水位低于 1.53 或字段缺失，立即启动“静默对齐”程序。
        
2. **静默更新流程 (Silent Update)**：
    
    - **操作**：AI 补全 1.53 要求的红线字段（如 `file_id`, `review_status` 等）。
        
    - **判定**：若补全过程仅涉及格式规范化，不涉及 `audit_summary` 的大幅修改，则直接更新 `protocol_v` 并设为 `Approved`。
        
3. **重塑与合并提案 (Refactoring Proposal)**：
    
    - **场景**：当发现同 `title` 下有多个碎片文件，或旧内容无法直接适配新字段。
        
    - **操作**：AI 编写合并后的初稿，保留所有历史 log，但将 `review_status` 强制设为 `Pending`。
        
    - **提示**：在 `kenny_notes` 中留下：`[AI 重塑建议]: 发现逻辑冲突，已准备合并提案，请统帅阅示。`
        
4. **血缘自愈 (Healing)**：
    - AI 必须定期根据 `file_id` 扫描断连的 `parent_doc` 或 `project_ref`。若发现关联文件更名，AI 必须自动修复 YAML 中的 `[[双链]]` 引用。
5. **V1.0 溯源原则**：AI 重塑遗产时，第一条 history log 必须锁定为 V1.0，日期必须与顶层 `date` 一致。
    
6. **静默对齐**：当 `protocol_v` 低于 1.6 时，AI 自动补全 `deadline` (可选) 及其他红线字段。
    
7. **真实性审计**：严禁 AI 臆断 1.0 以前的历史

## 四、 本文件官方封装样板 (V1.5.3 终极版)

YAML

```
---
title: 内阁资产：YAML 处理与封装规则
date: 2026-02-15
deadline: 2026-02-23
本文件版本: 1.6.0
primary_agent: 小酷
file_type: doc/standard
project_ref: "[[AI obsidian]]"
importance: 5
review_status: Approved
tags:
  - "#内阁基建/协议"
  - "#治理/资产重塑"
  - "#策略/时间主权"
audit_status: 🚀 V1.6 协议全量封顶
audit_summary: |
  本规范定义了内阁资产治理的终极 YAML 标准。V1.6 核心引入“时间二元论”，通过 Created Date 锁定物理起源，通过 Deadline 锁定任务目标。确立了 history_logs 的全量说明义务，严禁 AI 臆断历史，确保每一份资产的演进脉络清晰、真实、可审计。
audit_keywords:
  - "[[时间戳主权]]"
  - "[[时间二元论]]"
  - "[[V1.0 溯源原则]]"
  - "[[静默重塑]]"
  - "[[资产自愈]]"
audit_weights:
  小酷: 1
  小黑: 0.7
system_meta:
  file_id: CABINET-STRATEGY-001
  parent_doc: "[[内阁数字化治理大纲]]"
  protocol_v: yaml 版本:1.6
  kenny_notes: |
    [2026-02-23]: Kenny 终审 V1.6。
    [核心逻辑]: 确立 Created Date 为唯一真实起源，Deadline 为可选目标点。
    [操作红线]: history_logs 第一条必须对齐 date 字段。Tag 不允许带版本号，Keywords 必须双链。
  history_logs:
    - V1.6 | 2026-02-23 | 时间主权：引入时间二元论（Created/Deadline）。纠正 Tag 与 Keywords 逻辑错误。强制 history_logs 首条对齐 date 字段，实现全量历史说明封顶。
    - V1.5.3 | 2026-02-23 | 架构优化：将 protocol_v 移入 System Meta。确立“格式自动换装，内容人工把关”的静默更新逻辑。
    - V1.5.2 | 2026-02-23 | 约束闭环：确立字段约束等级（🔴必填/🟡推荐/🟢可选），完善资产重塑红线。
    - V1.5.1 | 2026-02-23 | 维护优化：执行“去版本化”策略，简化维护负担。
    - V1.5 | 2026-02-23 | 全息感应：引入整体设计原则，确立元数据全景感应机制。
    - V1.4 | 2026-02-23 | 纵横闭环：引入 project_ref 字段，实现资产与项目的坐标交汇。
    - V1.3 | 2026-02-21 | 架构分层：确立 Core View / Audit Layer / System Meta 三层解耦结构。
    - V1.2 | 2026-02-19 | 分类扩容：定义 doc/* 与 card/* 族群分类规范。
    - V1.1 | 2026-02-15 | 字段标准化：初步确定 title, date 等基础字段，剔除冗余字段。
    - V1.0 | 2026-02-15 | 协议诞生：确立内阁数字化重塑的元数据封装理念，开启主权资产治理。
---

```