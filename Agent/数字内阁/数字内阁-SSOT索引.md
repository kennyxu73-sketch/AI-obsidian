# 数字内阁 · SSOT 索引

**作用**：标明「哪类信息以哪份笔记为唯一权威（SSOT）」，短上下文（`[[基础背景 prompt]]`、`[[Base_L0]]`）只摘要并双链至此，避免双写漂移。

**关联阅读顺序**：见 [[数字内阁-索引]]。

---

## 主题 × 权威文档矩阵

| 主题 | SSOT（权威） | 短摘要 / 只读入口 |
|------|----------------|-------------------|
| 愿景、算力拓扑、Dify/One-API | [[基础背景 prompt]] §1 | [[Base_L0]] 不重复愿景正文 |
| **分层架构、四库、角色职责全文、Triple-A、Kenny's Law** | [[数字内阁（Digital Cabinet）]] | [[基础背景 prompt]] §2；[[Base_L0]] 极短角色索引 |
| SOP 细则（各 Agent 模式与动作） | [[Agent SOP(工作流协议) 配置方案]] | [[基础背景 prompt]] §3 与表格 |
| 议事渠道、@ 规则、小忆见证 | [[内阁 Agent 互访与议事规则]] | — |
| 自由碰撞三阶段、内勤小报转译 | [[内阁-自由议事与安全执行方案]] | — |
| Prompt 目录（L0/L1/L2）、Dify 同步 | [[内阁 Agent Prompt 维护法典]] | [[Base_L0]]、`Agent/Prompts/` |
| Kenny 认知画像（工具链规范名） | `Agent/小忆/Kenny画像/Kenny_Cognitive_Profile.md` | [[基础背景 prompt]]、`owner_context` |
| 多源对话收件、PSR、工具命令 | 见下节「运维指针」 | Internal_Cabinet_Tools 手册 |
| **企微多 Bot、session_id、去重、防循环、L3 合并** | [[数字内阁-企微多Bot与会话策略]] | 运维指针；`dialog_inbox` 实现 |

**说明**：`AI-ob 数字内阁.canvas` 含 **小欧、小记** 等扩展节点；[[数字内阁（Digital Cabinet）]] v2.0 正文未列出的成员，以画布与各 `Agent/[名]/` 说明为准，与 v2.0 冲突时 **优先以本表 SSOT 列 + 全量架构文** 对齐后再改画布或正文。

---

## 与基础背景 / Base_L0 的关系

- **[[基础背景 prompt]]**：对外 Prompt / Dify 的「短上下文」入口；§2 组织名单须与 [[数字内阁（Digital Cabinet）]] §三 **子集一致**（含小憶、小画、小报、小黑、小酷、小镜、小康）。
- **[[Base_L0]]**：硬约束 + 极短内阁索引；不展开职责，链向基础背景与全量架构。

---

## 运维指针（链到工具链，不复制长文）

| 事项 | 说明 |
|------|------|
| **物理主权 PSR** | 写入 `CABINET_ROOT` / Vault / RUNTIME 前：`cabinet_sentinel`、`AIOB_SHIELD_TOKEN`（哨兵非空时）、`AIOB_PSR_DISABLED` 仅开发。详见 Tools：`Manuals/多源对话与PSR运维备忘.md`。 |
| **多源对话 inbox** | `RUNTIME_ROOT/ai_dialogue_inbox/`、`inbox_manifest.jsonl`、`sync_errors.log`；脚本 `dialog_inbox.py`。法典与 SSOT：`Infrastructure/多源对话收件法典.md`（若存在）。 |
| **健康巡检** | `health_check.py dialog-sync-errors`（可选 `--fail-on-recent`）。 |
| **晋升 SSOT** | Kenny 审批 + `enseal` / Triple-A 闭环；Prompt 层不宣称自动升格。对齐 [[Base_L0]] 宪法节。 |
| **Kenny 上下文加载** | `owner_context.py`、`cabinet.owner.load_context`；路径约定见 Cursor 工作区 `.cursorrules`。 |

Tools 仓库路径（本机）：`Cursor_Workspace/Internal_Cabinet_Tools/`。

---

## 季度自检清单（议事规则观察切点）

来源：[[内阁 Agent 互访与议事规则]] §权力边界与观察重点。每季度勾选并填日期。

- [ ] **群外私通**：各 Agent 产出是否出现「群内未讨论过」的突兀结论？（日期：________）
- [ ] **小忆插话时机**：火花正盛时粗暴打断，还是废话阶段再收拢？（日期：________）
- [ ] **民主真实感**：参谋 Agent 是否敢于推翻彼此假设？（日期：________）

---

## 修订记录

| 日期 | 变更摘要 |
|------|-----------|
| 2026-03-28 | 初版：SSOT 矩阵、运维指针、季度清单；《自由议事》文件更名为 `内阁-自由议事与安全执行方案.md`（去除前导空格）。 |
| 2026-03-28 | 矩阵增列：[[数字内阁-企微多Bot与会话策略]]（v1.1）。 |
