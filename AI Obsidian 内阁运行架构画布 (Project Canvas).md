---
title: AI Obsidian 内阁运行架构画布 (V2.0)
date: 2026-02-24
primary_agent: 小酷
file_type: doc/standard
importance: 5
review_status: Pending
project_ref: "[[000_Cabinet_System/AI obsidian]]"
tags:
  - "#内阁基建/架构"
  - "#治理/外审体系"
  - "#架构/双层审计"
audit_status: 🚀 架构升维完成
audit_summary: |-
  封面金句：执行与监察分离——本地 3090 负责重体力施工，云端 Gemini 影子负责合规性审计。
  [审计报告]: 本画布已注入《外审规范 v3.0》逻辑，新增“云端影子审计层”与“Gatekeeper 决策关口”，确立了 Kenny-in-the-Loop 的物理拦截机制。实现了本地执行层与云端监察层的物理隔离。
audit_keywords:
  - "[[隐私熔断]]"
  - "[[影子审计]]"
  - "[[Gatekeeper]]"
  - "[[决策关口]]"
audit_weights:
  小酷: 1
  小忆: 0.8
system_meta:
  file_id: CABINET-CANVAS-V20
  protocol_v: yaml 版本:1.6.1
  kenny_notes: |
    [2026-02-24]: 架构大版本升级。正式引入 Google Cloud 作为审计隔离带，防止本地 Agent 产生非受控的自我迭代。
  history_logs:
    - V1.0.0 | 2026-02-12 | 基础四层架构（指挥/算力/存储/网络）。
    - V2.0.0 | 2026-02-24 | 升维：加入云端监察层与 Gatekeeper 协议。
---

# 🏛️ AI Obsidian 内阁运行架构画布 (V2.0)

## 一、 层级定义 (The 4+1 Infrastructure)

### 层级 0：影子审计层 (Auditor Layer - 云端)
- **物理环境**：Google Cloud Platform (GCP)
- **核心组件**：Gemini 1.5 Pro / Flash (影子智能体)
- **职责**：
  - **影子审计**：实时抽检本地 Dify 工作流逻辑与小酷的代码变更。
  - **合规拦截**：检测到逻辑漂移、非受控系统变更或安全红线时，强制挂起本地进程。

### 层级 1：核心指挥层 (Command Center - 本地端)
- **设备**：MacBook Pro (纯净系统)
- **全局 UI**：Obsidian
- **Gatekeeper (决策关口)**：
  - 核心动作拦截点：**[库准入]**、**[外发布]**、**[系统更]**。
  - **物理红线**：所有此类操作必须获取 Kenny 的 `Approved Token`。

### 层级 2：算力引擎层 (Compute Engine - 核心节点)
- **设备**：Ubuntu 3090 服务器
- **核心组件**：
  - **Dify/n8n**：Agent 编排与自动化流中心。
  - **小黑 (XiaoHei)**：4G 遗产物理分拣 (2-1/2-2)。
  - **执行 Agent**：小酷 (CTO)、小忆 (秘书长)、小报 (情报官) 的本地本体。

### 层级 3：存储资产层 (Storage & Assets)
- **设备**：QNAP NAS (192.168.0.2)
- **目录安全规范**：
  - `.system/`：不可篡改区（存放治理协议与核心 Prompt）。
  - `Archive/`：物理快照区（执行修改前的强制备份）。

### 层级 4：网络海关层 (Network & Gateway)
- **设备**：NAS 虚拟机 OpenWrt
- **功能**：ZeroTier 虚拟内网 + 加密流量分流（上云审计专用通道）。

---

## 二、 关键协议集成 (Critical Protocols)

1. **隐私熔断 (Privacy Firewall)**：
   - 2-1 检测到 `Private` 标记时，2-2 立即停止 AI 分析，强制移交 Kenny 手动处理。
2. **0.3 权重过滤 (Threshold Filter)**：
   - 资产分流时，计算关联度 < 0.3 的 Agent 自动从 `audit_weights` 移除，保持系统极简。
3. **时间确权 (Time Sovereignty)**：
   - 严格继承 `ctime` 基因，禁止在无证据下默认当前年份，确保 4G 遗产时间线准确。

---

## 三、 任务路由 (Task Routing)

- [ ] **@小酷** : 完成 GCP 影子审计接口的 API 对接压测。
- [ ] **@小忆** : 更新“决策关口”交互模版，确保 Kenny 拥有清晰的知情权。
- [ ] **@审计影子** : 对本画布 V2.0 进行合规性复核。