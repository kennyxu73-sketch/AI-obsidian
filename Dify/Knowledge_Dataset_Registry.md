---
title: Dify Knowledge Dataset 注册表（内阁总索引）
version: "0.1"
ref_id: INFRA-DIFY-KB-REGISTRY-20260329
---

# Knowledge Dataset 注册表

本文件是 **Dify Knowledge / Dataset** 与 Obsidian **`_kb_sources`**、**工作流设计文档 §3.6** 之间的 **总索引**（有什么、连谁、上次同步）。**日常同步命令与排障**见 [`Manuals/AI-OB_Dify知识库运维手册.md`](../Manuals/AI-OB_Dify%E7%9F%A5%E8%AF%86%E5%BA%93%E8%BF%90%E7%BB%B4%E6%89%8B%E5%86%8C.md)。

**契约**：[`Manuals/Dify_应用开发规范.md`](../Manuals/Dify_%E5%BA%94%E7%94%A8%E5%BC%80%E5%8F%91%E8%A7%84%E8%8C%83.md) §3.6、§5.1、§6。各 Workflow 的 **Knowledge 绑定表**（按应用）仍以对应 `Dify/.../WF_*.md` 为准；本表 **不替代** 单应用 Frontmatter 中的 `dify_knowledge_dataset_ids` / `dify_kb_source_paths`。

**密钥**：Dataset UUID 可登记；**API Key 仅环境变量**，禁止写入本页或 Git。

---

## Dataset ID 备用池（逐步应用）

已在 Dify 控制台预留 **3** 个 Dataset；**槽位 B/C 未指派 `kb_slug` 前请勿向其中同步生产内容**，避免与表 A 漂移。不足时在控制台新建 Dataset，并在此表 **追加行**。

| 槽位 | Dataset ID | 当前用途 |
|------|------------|----------|
| **A（首选）** | `dataset-SLkcbzIPqlKfRjql3OH3JQKF` | 表 A **`kenny_portrait_tier_c`**：`sync_to_dify.py --dataset-id`、启用 RAG 时工作流 Knowledge 绑定 |
| **B** | `dataset-qG66BG3MRwykotn9Ua3TxTUl` | 预留（分配业务后填入表 A 新行并改本列） |
| **C** | `dataset-ZzKcXRFZsIp4UCkG4kUaF0MW` | 预留（分配业务后填入表 A 新行并改本列） |

`POST /v1/datasets/{dataset_id}/...` 中的 `dataset_id` **以你方实例 OpenAPI 为准**（整串常含 `dataset-` 前缀）；若 404，按控制台文档尝试仅 UUID 段。

---

## 表 A · Knowledge Dataset 注册

| kb_slug | Dify Dataset 显示名 | Dataset UUID | OB 同步根（库根相对） | 同步脚本 / 说明 | 默认绑定工作流 | 上次成功同步 | 责任人 / 备注 |
|---------|---------------------|--------------|----------------------|-----------------|----------------|--------------|----------------|
| `kenny_portrait_tier_c` | （控制台填写，如 Kenny_Portrait_TierC） | `dataset-SLkcbzIPqlKfRjql3OH3JQKF` | `000_Cabinet_System/Dify/_kb_sources/kenny_portrait_tier_c/` | [`README`](_kb_sources/kenny_portrait_tier_c/README.md) + `sync_to_dify.py`（`TOOLS_PATH`） | `WF_Inbox_L1_Summary` / `WF_InboxRefine_Patch`（**默认未绑** RAG；启用时见各 WF §3.6） | — | Tier C；备用池槽位 **A**；`INFRA-KENNY-TIERC-KB-20260329` |

> 新增 Dataset：在表末 **追加一行**；或从 **备用池** 槽位 B/C 指派后更新上表与备用池两表。

---

## 画像维护（Kenny 认知资产）

与 [`Manuals/主人画像分级建立与使用规范.md`](../Manuals/%E4%B8%BB%E4%BA%BA%E7%94%BB%E5%83%8F%E5%88%86%E7%BA%A7%E5%BB%BA%E7%AB%8B%E4%B8%8E%E4%BD%BF%E7%94%A8%E8%A7%84%E8%8C%83.md) 一致；此处仅 **索引级** 摘要。

| Tier | 载体 | 注入 / 同步方式 | 与本表关系 |
|------|------|-----------------|------------|
| **A (Sovereign)** | `Agent/小忆/Kenny画像/Kenny_Cognitive_Profile.md` | HTTP **`p_tier_a_main`**（`prompt_http_bridge`） | **非** RAG Dataset |
| **B (Context)** | `Agent/小忆/Kenny画像/Kenny_Profile_L1_Context.md` | HTTP **`p_tier_b_l1_ctx`** | **非** RAG Dataset |
| **C (RAG)** | 表 A 行 `kenny_portrait_tier_c` | 脱水切片于 `_kb_sources/...` → **`sync_to_dify.py`** | 见表 A |

**小酷提醒**：Dify 中 Tier C 检索结果 **仅作 Context 变量**，**严禁**覆盖 System Prompt 中的 Tier A 指令。

---

## API / 工具对齐

| 能力 | 环境变量 / 鉴权 | 锚点 |
|------|-----------------|------|
| Dataset 文档 create/update | `DIFY_API_BASE`、`DIFY_DATASET_API_KEY`（或回退 `DIFY_API_KEY`） | `Internal_Cabinet_Tools/sync_to_dify.py`：`/v1/datasets/{id}/document/create-by-text`、`.../documents/{id}/update-by-text` |
| 工作流运行 | `DIFY_API_KEY` | `Internal_Cabinet_Tools/dify_client.py`：`POST /v1/workflows/run` |
| 画像 Prompt 只读 | `CABINET_PROMPT_TOKEN`（Prompt HTTP 桥） | `Internal_Cabinet_Tools/prompt_http_bridge.py`；slug 见画像规范 §6 |

---

## 对齐进度（自检勾选）

- [ ] Tier C 对应 Dataset 已在 Dify 控制台创建  
- [ ] 表 A 中 `TBD` 已替换为真实 UUID  
- [ ] 已执行至少一次 **非 dry-run** 的 `sync_to_dify.py` 且成功  
- [ ] 已在注册表 **更新摘要** 与 **上次成功同步** 留痕  
- [ ] （按需）目标 Workflow 已挂 Knowledge，检索输出接入 **Context**

---

## 知识库更新摘要（滚动，建议 ≤10 行）

**不替代** `Internal_Cabinet_Tools/CHANGELOG.md`（影子索引）/ 真库 `000_Cabinet_System/CHANGELOG.md`；重大变更仍写影子索引。

| 日期 | kb_slug | 变动摘要 | 备注 |
|------|---------|----------|------|
| 2026-03-29 | kenny_portrait_tier_c | 注册表与运维手册 scaffold；Dataset 未绑生产 UUID | 待首次生产同步后更新表 A「上次成功同步」 |
| 2026-03-29 | — | 登记 Dataset 备用池 3 槽；`kenny_portrait_tier_c` 绑定槽位 A | 槽位 B/C 预留；`sync`/WF 绑定后更新「上次成功同步」 |

---

`ref_id`：**INFRA-DIFY-KB-REGISTRY-20260329**
