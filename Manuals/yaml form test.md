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
