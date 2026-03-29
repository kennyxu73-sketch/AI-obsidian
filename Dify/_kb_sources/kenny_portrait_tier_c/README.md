# Kenny 画像 · Tier C 知识库源（RAG）

契约真源：[`Manuals/主人画像分级建立与使用规范.md`](../../Manuals/%E4%B8%BB%E4%BA%BA%E7%94%BB%E5%83%8F%E5%88%86%E7%BA%A7%E5%BB%BA%E7%AB%8B%E4%B8%8E%E4%BD%BF%E7%94%A8%E8%A7%84%E8%8C%83.md)；[`Manuals/Dify_应用开发规范.md`](../../Manuals/Dify_%E5%BA%94%E7%94%A8%E5%BC%80%E5%8F%91%E8%A7%84%E8%8C%83.md) §6。

## 核心架构逻辑（Tier A / B / C）

- **Tier A (Sovereign)**：`p_tier_a_main`（HTTP 注入），**公理裁决**；**不可检索**、全量比对；**非**本 Dataset 职责。
- **Tier B (Context)**：`p_tier_b_l1_ctx`（HTTP 注入），对话锚定，短促。
- **Tier C (RAG)**：`sync_to_dify.py` → Dataset，辅助背景召回（海量、模糊匹配）；**仅**本目录同步内容。
- **小酷提醒**：Dify 控制台中 Tier C 检索结果 **仅作 Context 变量** 输入 LLM，**严禁**直接覆盖 System Prompt 中的 Tier A 指令。

## 禁令（同步前自检）

- 不得纳入含 **`.audit.yaml`**（及规范禁止的侧车）的文件正文或整文件拷贝。
- 不得将位于 **`private/`** 路径段下的原文件作为同步源；勿写入未脱敏敏感段落。
- **禁止**将整份 Tier A（如 `Kenny_Cognitive_Profile.md`）全文复制进本树作为 RAG 主真源；Tier C 仅为**脱水切片**。

取材：从 [`Agent/小忆/Kenny画像/`](../../Agent/%E5%B0%8F%E5%BF%86/Kenny%E7%94%BB%E5%83%8F/) **人工脱水**摘录写入本目录下各 `.md`。

## 同步至 Dify Dataset

1. 在 Dify 控制台创建 **Knowledge / Dataset**，复制 **UUID**。
2. 环境变量：`DIFY_API_BASE`（见 `.cursorrules` L0.6.2 / `Manuals/Dify_应用开发规范.md` §4）、`DIFY_DATASET_API_KEY`（或 `DIFY_API_KEY`）。
3. 在 `Internal_Cabinet_Tools` 仓库根执行（需 `httpx`）：

```bash
export DIFY_API_BASE="http://10.210.8.8:5001"
export DIFY_DATASET_API_KEY="你的密钥"

python3 sync_to_dify.py \
  --dataset-id "你的_Dataset_UUID" \
  --source "/Volumes/Cabinet/cabinet/obsidian_vault/000_Cabinet_System/Dify/_kb_sources/kenny_portrait_tier_c" \
  --dry-run
```

确认输出后去掉 `--dry-run` 再执行。若从 Cursor 镜像目录同步，将 `--source` 换为  
`.../Internal_Cabinet_Tools/000_Cabinet_System 1/Dify/_kb_sources/kenny_portrait_tier_c`（须与真库内容一致）。

`.sync_cache.json` 默认生成在 `--source` 目录内，**派生状态**，建议勿提交 Git。

## 本目录文件

| 文件 | 说明 |
|------|------|
| `Kenny_Projects_Index.md` | 项目表切片 |
| `Kenny_Tech_Stack_Glossary.md` | 术语表切片 |
| `Kenny_Habits_Reference.md` | 习惯参考切片 |

---

`ref_id`：**INFRA-KENNY-TIERC-KB-20260329**
