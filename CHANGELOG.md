# AI-OB 内阁系统变更日志 (CHANGELOG)

**版本**: v1.6.7-Pilot-Operational  
**维护者**: 小酷 (CTO)  
**协议**: 遵循 `.cursorrules` L0.7 要求  
**状态**: 🔄 活跃更新中

---

## 2026-03-28 | 物理主库合并（嵌套副本已删除）

### 变更概述
将误置于 `Cursor_Workspace/Volumes/Cabinet/cabinet/obsidian_vault/` 的运行期文件合并至唯一主库 `/Volumes/Cabinet/cabinet/obsidian_vault/`，并删除该嵌套目录树，避免双份编辑与分叉。

### 关键动作
1. 合并：`Active_Session.md`、`Cognitive_Patch_Draft.md`、`logs/path_conflict.log`、`本 CHANGELOG`。
2. 将嵌套路径下 `.../Internal_Cabinet_Tools/path_conflict.log` 片段追加至主库 `path_conflict.log`（带合并标记）。
3. 删除：`/Volumes/Cabinet/cabinet/Cursor_Workspace/Volumes/`（整树）。

### JSON（影子索引）
```json
{ "module": "path-merge", "status": "done", "risk_level": "low", "ref_id": "MERGE-20260328-VAULT" }
```

---

## 2026-03-28 | 系统基础设施对齐点火

### 变更概述
完成 AI-OB 系统 Canonical Path Map 与物理目录结构的全面对齐，消除路径冲突根源。

### 关键动作
1. **宪法更新**: 修订 `.cursorrules` L0.5 & L0.6，将路径锚定至现有 `obsidian_vault` 结构。
2. **目录补全**: 创建缺失的 `200_Operations/` 运行时目录及其子结构。
3. **文件初始化**: 创建本 CHANGELOG 及运行时关键文件。

### 技术详情
- **L0.5 新映射**:
  - `MEMOIR_PATH` = `$CABINET_ROOT/obsidian_vault/400_Chronicles/`
  - `RAW_PATH` = `$CABINET_ROOT/obsidian_vault/100_Inbox_Intelligence/`
  - `RUNTIME_ROOT` = `$CABINET_ROOT/obsidian_vault/200_Operations/`
  - `SSOT_ROOT` = `$CABINET_ROOT/obsidian_vault/000_Cabinet_System/`
  - `TOOLS_PATH` = `$CABINET_ROOT/Cursor_Workspace/Internal_Cabinet_Tools/`

### 审计痕迹
- **触发规则**: L0.7 (SSOT 结构护栏要求 CHANGELOG)
- **审批状态**: ✅ Kenny 直接指令执行
- **关联文件**: `$RUNTIME_ROOT/Cognitive_Patch_Draft.md`

### 下一步
- 处理 SSOT 结构白名单违规项
- 验证 3090 服务器端口连通性
- 推进 P0 点火具体技能开发

---
**变更日志结束** | 版本 v1.6.7 初始化完成