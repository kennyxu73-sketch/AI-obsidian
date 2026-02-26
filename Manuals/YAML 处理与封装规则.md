---
title: 内阁资产：YAML 处理与封装规则
date: 2026-02-15
deadline: 2026-02-23
本文件版本: 1.6.1
primary_agent: 小酷
file_type: doc/standard
project_ref: "[[000_Cabinet_System/AI obsidian]]"
importance: 5
review_status: Approved
tags:
  - "#内阁基建/协议"
audit_status: 🚀 V1.6.1 逻辑全量封顶
audit_summary: |
  [V1.6.1 全量滚动审计报告]:
  - 基因继承：复核通过。已完整迁移 V1.6 历史链路。
  - 差异沉淀：已将原 audit_weights 等非标字段存证于 Legacy 模块。
  - weights: "小黑: 0.7, 小酷: 1" 
  [Legacy Metadata]:
    - old_alias: "内阁数字化治理大纲 (旧)"
audit_keywords:
  - "[[基因继承原则]]"
  - "[[滚动审计机制]]"
  - "[[Legacy_Metadata]]"
system_meta:
  file_id: CABINET-STRATEGY-001
  parent_doc: "[[内阁数字化治理大纲]]"
  protocol_v: yaml 版本:1.6.1
  kenny_notes: |
    [2026-02-23]: Kenny 终审 V1.6.1。补全全量历史链路。
    [升级核心]: 确立“旧元数据沉淀逻辑”，非标字段统一进摘要 Legacy 模块，确保 YAML 核心区洁净。
  history_logs:
    - V1.6.1 | 2026-02-23 | 架构升级：引入“滚动审计”与“基因解析”逻辑。确立非标元数据沉淀至摘要模块的规则。
    - V1.6 | 2026-02-23 | 时间主权：引入时间二元论（Created/Deadline）。纠正 Tag 与 Keywords 逻辑错误。强制 history_logs 首条对齐 date 字段。
    - V1.5.3 | 2026-02-23 | 架构优化：将 protocol_v 移入 System Meta。确立“格式自动换装，内容人工把关”逻辑。
    - V1.5.2 | 2026-02-23 | 约束闭环：确立字段约束等级，完善资产重塑红线。
    - V1.5.1 | 2026-02-23 | 维护优化：执行“去版本化”策略，简化维护负担。
    - V1.5 | 2026-02-23 | 全息感应：引入整体设计原则，确立元数据全景感应机制。
    - V1.4 | 2026-02-23 | 纵横闭环：引入 project_ref 字段。
    - V1.3 | 2026-02-21 | 架构分层：确立 Core View / Audit Layer / System Meta 三层解耦结构。
    - V1.2 | 2026-02-19 | 分类扩容：定义 doc/* 与 card/* 族群分类规范。
    - V1.1 | 2026-02-15 | 字段标准化：初步确定 title, date 等基础字段。
    - V1.0 | 2026-02-15 | 协议诞生：确立内阁数字化重塑元数据封装理念。
---

# 内阁资产：YAML 处理与封装全量规范 (V1.6.1 终极版)

## 一、 整体设计原则 (General Design Principles)

1. **资产全息化 (Holographic Assets)**：元数据通过 `[[双链]]` 成为逻辑节点。
    
2. **纵横坐标系 (Matrix Coordinate)**：通过 `file_type` 与 `project_ref` 确立唯一坐标。
    
3. **血缘守恒 (Ancestry Conservation)**：通过 `parent_doc` 杜绝孤儿文件。
    
4. **后台静默重塑 (Silent Background Refactoring)**：AI 自动遍历并静默更新协议版本。
    
5. **约束等级制 (Constraint Grading)**：明确区分必填（🔴）、推荐（🟡）与可选（🟢）字段。
    
6. **内容终审权 (Final Review Authority)**：涉及实质变更必须通过 `Pending` 触发人工审核。
    
7. **时间戳主权 (Timestamp Sovereignty)**：`date` 锁定资产真实的物理起源。
    
8. **时间二元论 (Dual-Date Theory)**：严格区分 `date` (出生) 与 `deadline` (截止)。
    
9. **基因继承原则 (V1.6.1 新增)**：新 YAML 必须是旧 YAML 的增量升级。AI 必须先扫描原文件旧元数据，确保原始标签与核心属性不丢失。
    
10. **滚动审计原则 (V1.6.1 新增)**：`audit_summary` 不再是简单的覆盖，而是包含对前代版本结论的复核，形成有厚度的信用链条。
    

---

## 二、 YAML 全量字段规范与约束等级 (V1.6.1)

### 1. 核心展示层 (Core View) - 纵横定位与时间主权

|**字段名**|**约束等级**|**执行逻辑与红线要求 (Redline)**|
|---|---|---|
|**`title`**|**🔴 必填**|资产逻辑名。AI 跨文件感应的核心标识。|
|**`date`**|**🔴 必填**|**Created Date**。锁定诞生日期。**[1.6.1 红线]**：禁止臆断！若正文模糊，必须寻找物理证据并在 `kenny_notes` 声明推算逻辑。|
|**`deadline`**|**🟢 可选**|**Finish Date**。锁定任务/日志截止点。|
|**`本文件版本`**|**🔴 必填**|**内容演进版本**。**[1.6.1 红线]**：遵循物理递进（如 1.6.0 -> 1.6.1）。4G 遗产封装初始为 `1.0.0`。|
|**`primary_agent`**|**🔴 必填**|责任人。**[1.6.1 逻辑]**：权重 < 0.3 的 Agent 自动剔除。|
|**`file_type`**|**🔴 必填**|**[1.6.1 复合模式]**：支持 `doc/mindmap` 或 `doc/standard`，保留插件形态主权。|
|**`project_ref`**|**🟡 推荐**|**强制双链** `[[ ]]`。关联横向项目看板。|
|**`review_status`**|**🔴 必填**|**状态闸门**：`Approved` 或 `Pending` (涉及年份推算或内容重塑必选)。|
|`importance`|**🟡 推荐**|资产权重 (1-5)。4-5 分触发“施工-审计分离”的二次确认逻辑。|

### 2. 深度审计层 (Audit Layer) - 全息感应

| **字段名**              | **约束等级**  | **执行逻辑与红线要求 (Redline)**                                                       |
| -------------------- | --------- | ----------------------------------------------------------------------------- |
| **`audit_summary`**  | **🔴 必填** | **全息滚动审计**。**[1.6.1 补丁]**：不准覆盖！必须包含 **[Legacy Metadata]** 区块，存放旧别名、旧权重等非标元数据。 |
| **`audit_keywords`** | **🟡 推荐** | **推荐双链** `[[ ]]`。实现逻辑感应。                                                      |
| `audit_status`       | 🟢 可选     | 演进标志（如：🚀 V1.6.1 逻辑全量封顶）。                                                     |
| audit_weights:       | **🔴 必填** | 对关联的agent 做相关性评估, 低于 0.5的不列出                                                  |

### 3. 系统追踪层 (System Meta) - 自动化维护

|**字段名**|**约束等级**|**执行逻辑与红线要求 (Redline)**|
|---|---|---|
|**`file_id`**|**🔴 必填**|**唯一识别码**。严禁人工修改。|
|**`protocol_v`**|**🔴 必填**|**技术协议水位**：`"yaml 版本:1.6.1"`。|
|**`history_logs`**|**🔴 必填**|**编年史**。**[1.6.1 红线]**：格式升级不记入业务 Log；首条必须对齐 `date` 字段。|
|`parent_doc`|**🟡 推荐**|**强制双链** `[[ ]]`。锁定纵向归属。|
|`kenny_notes`|🟢 可选|**[1.6.1 声明区]**：记录年份推算逻辑、审计冲突或统帅特殊指示。|

---

## 三、 自动维护与重塑协议 (Automation Protocols)

1. **基因继承与差异沉淀**：AI 必须提取旧 YAML 字段。标准字段全量融入；非标字段（如旧 Alias）沉淀至 `audit_summary` 的 `[Legacy Metadata]`。
    
2. **形态主权保护**：严禁抹除 `mindmap-plugin` 等标记。施工态生成“原文件名+旧标识”备份，重塑后保持原名以保护双链。
    
3. **V1.0 溯源原则**：AI 重塑遗产时，第一条 history log 必须锁定为 V1.0，日期与顶层 `date` 一致。
    
4. **滚动复核机制**：每一次版本递进，AI 必须对全量字段进行“体检”，确保新旧逻辑无冲突。
    
5. **静默对齐**：当协议水位过低时，AI 自动补全红线字段，保持资产自愈。
    

---

## 四、 本规范官方封装样板 (V1.6.1 终极版)

YAML

```
---
# --- 1. Core View (核心定位区) ---
title: 内阁资产：YAML 处理与封装规则
date: 2026-02-15
deadline: 2026-02-23
本文件版本: 1.6.1
primary_agent: 小酷
file_type: doc/standard
project_ref: "[[AI obsidian]]"
importance: 5
review_status: Approved
tags:
  - "#内阁基建/协议"
  - "#治理/V1.6.1升级"

# --- 2. Audit Layer (深度审计区) ---
audit_status: 🚀 V1.6.1 逻辑全量封顶
audit_summary: |
  [V1.6.1 全量滚动审计报告]:
  - 基因继承：复核通过。已完整迁移 V1.6 历史链路。
  - 差异沉淀：已将原 audit_weights 等非标字段存证于 Legacy 模块。
  [Legacy Metadata]:
    - old_alias: "内阁数字化治理大纲 (旧)"
    - old_weights: "小黑: 0.7, 小酷: 1"
audit_keywords:
  - "[[基因继承原则]]"
  - "[[滚动审计机制]]"
  - "[[Legacy_Metadata]]"

# --- 3. System Meta (系统追踪区) ---
system_meta:
  file_id: CABINET-STRATEGY-001
  parent_doc: "[[内阁数字化治理大纲]]"
  protocol_v: "yaml 版本:1.6.1"
  kenny_notes: |
    [2026-02-23]: Kenny 终审 V1.6.1。补全全量历史链路。
    [升级核心]: 确立“旧元数据沉淀逻辑”，非标字段统一进摘要 Legacy 模块，确保 YAML 核心区洁净。
  history_logs:
    - V1.6.1 | 2026-02-23 | 架构升级：引入“滚动审计”与“基因解析”逻辑。确立非标元数据沉淀至摘要模块的规则。
    - V1.6 | 2026-02-23 | 时间主权：引入时间二元论（Created/Deadline）。纠正 Tag 与 Keywords 逻辑错误。强制 history_logs 首条对齐 date 字段。
    - V1.5.3 | 2026-02-23 | 架构优化：将 protocol_v 移入 System Meta。确立“格式自动换装，内容人工把关”逻辑。
    - V1.5.2 | 2026-02-23 | 约束闭环：确立字段约束等级，完善资产重塑红线。
    - V1.5.1 | 2026-02-23 | 维护优化：执行“去版本化”策略，简化维护负担。
    - V1.5 | 2026-02-23 | 全息感应：引入整体设计原则，确立元数据全景感应机制。
    - V1.4 | 2026-02-23 | 纵横闭环：引入 project_ref 字段。
    - V1.3 | 2026-02-21 | 架构分层：确立 Core View / Audit Layer / System Meta 三层解耦结构。
    - V1.2 | 2026-02-19 | 分类扩容：定义 doc/* 与 card/* 族群分类规范。
    - V1.1 | 2026-02-15 | 字段标准化：初步确定 title, date 等基础字段。
    - V1.0 | 2026-02-15 | 协议诞生：确立内阁数字化重塑元数据封装理念。
---
```