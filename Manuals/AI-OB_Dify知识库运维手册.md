---
title: AI-OB · Dify 知识库运维手册
version: "0.1"
ref_id: INFRA-DIFY-KB-RUNBOOK-20260329
---

# AI-OB · Dify 知识库运维手册

**定位**：Obsidian → Dify Knowledge（Dataset）同步与绑定的 **日常 SOP 与排障**。**总索引与对账**见 [`Dify/Knowledge_Dataset_Registry.md`](../Dify/Knowledge_Dataset_Registry.md)（勿与本手册重复长表）。

**引用**：

- [`Manuals/Dify_应用开发规范.md`](Dify_%E5%BA%94%E7%94%A8%E5%BC%80%E5%8F%91%E8%A7%84%E8%8C%83.md) §4（API / 环境变量）、§6（同步与缓存）
- [`Manuals/主人画像分级建立与使用规范.md`](%E4%B8%BB%E4%BA%BA%E7%94%BB%E5%83%8F%E5%88%86%E7%BA%A7%E5%BB%BA%E7%AB%8B%E4%B8%8E%E4%BD%BF%E7%94%A8%E8%A7%84%E8%8C%83.md) Tier C 与 HTTP slug
- 工具：`Internal_Cabinet_Tools/sync_to_dify.py`（仓库根，与 `TOOLS_PATH` / `.cursorrules` L0.6.2 一致）

---

## 1. 环境准备

| 项 | 说明 |
|----|------|
| `DIFY_API_BASE` | 默认 `http://10.210.8.8:5001`（与内阁算力节点一致时可省略） |
| `DIFY_DATASET_API_KEY` | **推荐**：Dify Knowledge / Dataset 专用 Key |
| `DIFY_API_KEY` | 无 Dataset 专用 Key 时可回退（权限以实例为准） |
| Python 依赖 | `httpx`（见工具仓库 requirements） |
| 运行位置 | **推荐**：在 **Mac** 上 `cd` 至 `Internal_Cabinet_Tools` 执行；Linux 服务器需自备脚本副本与 **`--source` 绝对路径**（服务器上须存在同步源目录） |

**禁止**：将任何 API Key 写入 Vault Markdown 或 Git。

---

## 2. 标准流程（首次与例行）

1. **Dify 控制台**：新建 **Knowledge / Dataset**，记录 **UUID** 与显示名。  
2. **[`Dify/Knowledge_Dataset_Registry.md`](../Dify/Knowledge_Dataset_Registry.md)**：在 **表 A** 填 UUID、显示名；更新 **上次成功同步**（首次可为 `—`）。  
3. **编辑** `_kb_sources/<kb_slug>/` 下切片（遵守各目录 `README` 禁令）。  
4. **预检**：  
   ```bash
   cd /Volumes/Cabinet/cabinet/Cursor_Workspace/Internal_Cabinet_Tools
   export DIFY_API_BASE="http://10.210.8.8:5001"
   export DIFY_DATASET_API_KEY="你的密钥"
   python3 sync_to_dify.py \
     --dataset-id "你的UUID" \
     --source "/Volumes/Cabinet/cabinet/obsidian_vault/000_Cabinet_System/Dify/_kb_sources/kenny_portrait_tier_c" \
     --dry-run
   ```  
   （将 `--source` 换为当前机器上 **真实绝对路径**；镜像目录同步时与真库内容保持一致。）  
5. **正式同步**：去掉 `--dry-run` 再执行；成功后更新注册表 **上次成功同步** 与 **滚动更新摘要**。  
6. **（可选）工作流**：在 Dify 中为需要 RAG 的应用添加 **Knowledge** 节点，选中同一 Dataset；检索结果接入 **Context 变量**，**不替换** System 中 Tier A 相关指令。

---

## 3. 常见问题

| 现象 | 处理 |
|------|------|
| `can't open file ... sync_to_dify.py` | 当前目录不是 `Internal_Cabinet_Tools` 或仓库未克隆到该机器；改用 `cd` 到正确路径或使用脚本绝对路径。 |
| `--source` 找不到文件 | 使用 **绝对路径**；勿假设 `~/obsidian_vault` 在服务器上存在。 |
| 未设置 Key 报错 | 设置 `DIFY_DATASET_API_KEY` 或 `DIFY_API_KEY`；`--dry-run` 可不调用 API。 |
| `update` 返回 404 | 控制台手工删过文档导致缓存 `document_id` 失效；使用 `sync_to_dify.py --invalidate` 或清理 `--source/.sync_cache.json` 中对应项后重试（见规范 §6.4）。 |
| 部分文件未上传 | 路径含 `private`、`_temp`、`副本` 或幽灵卷时脚本 **故意跳过**（见 `sync_to_dify.py` 与规范 §4）。 |

---

## 4. 安全与合规

- Tier C 源树：**禁止**整份 Tier A 全文、`.audit.yaml` 侧车、未脱敏内容；见 [`_kb_sources/kenny_portrait_tier_c/README.md`](../Dify/_kb_sources/kenny_portrait_tier_c/README.md)。  
- 重大架构变更：除更新注册表摘要外，在 **`Internal_Cabinet_Tools/CHANGELOG.md`**（及真库 CHANGELOG，若适用）留 **影子索引**。

---

## 5. 可选预检

- Mac 侧网络：`Internal_Cabinet_Tools/preflight_dify_zt.py`（`DIFY_API_BASE`、可选 Ollama / workflow 探测，见脚本说明）。

---

`ref_id`：**INFRA-DIFY-KB-RUNBOOK-20260329**
