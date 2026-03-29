# Dify 导出归档

按 [`Manuals/Dify_应用开发规范.md`](../Manuals/Dify_%E5%BA%94%E7%94%A8%E5%BC%80%E5%8F%91%E8%A7%84%E8%8C%83.md) §5：从 Dify 控制台导出的 DSL / JSON **派生产物**放此目录，与设计 `.md` 的 `dify_artifact`、`dify_exported_at` 双链。

**本批次 Ref_ID**：`INFRA-DIFY-INBOX-20260329-01`（首个 `WF_InboxRefine_Patch` 导入后请将文件置于此并更新设计文档 Frontmatter）。

| 文件 | 应用 | 备注 |
|------|------|------|
| `wf_inbox_l1_summary_20260330.yml` | `WF_Inbox_L1_Summary` | 含 **Tier C** 知识库节点（query=`dialogue_excerpt`）；真源见 `WF_*.md` |
| `wf_inbox_refine_patch_20260330.yml` | `WF_InboxRefine_Patch` | 含 **Tier C** 知识库节点（query=`l1_summaries_bulk`）；同上 |
| `wf_inbox_l1_summary_20260329.yml` | （旧版 L1 MVP） | 保留对照，**当前**以 `20260330` 与 Frontmatter 为准 |

> 勿手搓整包 JSON：以 Dify 导出为准，再交小酷 diff。上表 **20260330** 由 `Internal_Cabinet_Tools/gen_dify_inbox_workflows.py` 从 Agent 真源 MD 生成，导入后若改画布请 **再导出** 覆盖。
