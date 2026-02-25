# Obsidian Skill 系统总览
> 小酷 (CTO) 技术方案 | 基于 Obsidian 的 Skill 管理系统

## 📋 方案概述

本方案实现了一个基于 Obsidian 双链结构的 Skill（技能）管理系统，允许在 Obsidian Vault 中以 Markdown 文件的形式定义、管理和执行可复用的功能模块。

### 核心特性

✅ **本地优先**：所有 Skill 存储在 Obsidian Vault 中，确保隐私  
✅ **双链结构**：利用 Obsidian 的 `[[链接]]` 组织 Skill 依赖关系  
✅ **类型安全**：严格的 YAML frontmatter 规范  
✅ **权限控制**：细粒度的权限管理（读/写/网络/系统）  
✅ **3090 集成**：无缝对接本地算力  
✅ **自动注册**：自动发现和注册所有 Skill  

## 📁 文件结构

```
Internal_Cabinet_Tools/
├── skill_specification.md      # Skill 规范文档（详细）
├── skill_manager.py            # Skill 管理器实现（核心）
├── SKILL_USAGE_GUIDE.md        # 使用指南（快速上手）
├── README_SKILLS.md           # 本文件（总览）
└── examples/                   # 示例 Skill
    ├── skill_note_auditor.md          # 笔记审计器
    ├── skill_note_harvester.md        # 笔记收割器
    ├── skill_xiaohei_integration.md   # 小黑集成器
    └── skill_note_linker.md           # 笔记双链生成器
```

## 🚀 快速开始

### 1. 阅读文档

- **新手**：先看 `SKILL_USAGE_GUIDE.md`
- **开发者**：查看 `skill_specification.md`
- **示例**：参考 `examples/` 目录下的 Skill

### 2. 配置环境

```python
# 编辑 skill_manager.py
CONFIG = {
    "VAULT_PATH": "/your/obsidian/vault/path",
    # ...
}
```

### 3. 创建第一个 Skill

参考 `examples/skill_note_auditor.md`，在 `Skills/Analysis/` 目录下创建你的 Skill。

### 4. 运行

```python
from skill_manager import SkillManager

manager = SkillManager()
manager.update_registry()
result = await manager.execute("skill_001", {...})
```

## 📚 文档索引

| 文档 | 用途 | 受众 |
|------|------|------|
| `skill_specification.md` | 完整规范 | 开发者 |
| `SKILL_USAGE_GUIDE.md` | 使用指南 | 所有用户 |
| `README_SKILLS.md` | 总览 | 所有人 |

## 🎯 Skill 类型

| 类型 | 目录 | 用途 | 示例 |
|------|------|------|------|
| **Core** | `Skills/Core/` | 系统级功能 | 文件操作、配置管理 |
| **Analysis** | `Skills/Analysis/` | 数据分析 | 笔记审计、内容分析 |
| **Automation** | `Skills/Automation/` | 自动化 | 批量处理、定时任务 |
| **Integration** | `Skills/Integration/` | 系统集成 | 对接小黑/小镜/小康 |
| **Custom** | `Skills/Custom/` | 自定义 | 用户自定义功能 |

## 🔗 与现有系统集成

### 对接小黑（审计员）
```python
# 小黑出 JSON 判决书 → 小酷执行收割
result = await manager.execute("skill_003", {
    "xiaohei_judgment": json_judgment,
    "note_path": note_path
})
```

### 对接 3090 算力
```python
# Skill 自动使用 3090 API
from skill_manager import call_3090
response = await call_3090(prompt="...")
```

### 对接 n8n/Dify
Skill 可以作为 n8n workflow 节点或 Dify Agent Tool 使用。

## 🛡️ 安全与权限

### 权限级别

- **read_vault**: 读取 Vault 文件
- **write_vault**: 写入/修改文件（需谨慎）
- **network_access**: 网络请求（需明确声明）
- **system_access**: 系统调用（高风险）

### 安全规则

1. ✅ 默认 `write_vault: false`
2. ✅ 网络访问必须明确声明
3. ✅ AI 生成的 Skill 必须标注 `#ai-generated`
4. ✅ 修改原始笔记必须标注 `#modifies-original`

## 📊 工作流程

```
创建 Skill → 验证 → 注册 → 执行 → 监控 → 归档
     ↓         ↓      ↓      ↓      ↓      ↓
  编写.md   格式检查  注册表  调用3090  日志  版本管理
```

## 🎨 示例 Skill

### 1. 笔记审计器 (`skill_001`)
- **功能**：审计笔记内容，输出结构化 JSON
- **类型**：Analysis
- **依赖**：3090 算力
- **用途**：对接小黑审计逻辑

### 2. 笔记收割器 (`skill_002`)
- **功能**：批量扫描和处理笔记
- **类型**：Automation
- **依赖**：skill_001
- **用途**：批量审计笔记

### 3. 小黑集成器 (`skill_003`)
- **功能**：执行小黑 JSON 判决书
- **类型**：Integration
- **依赖**：skill_001
- **用途**：SOP 流程：小黑出判决书 → 小酷执行

### 4. 笔记双链生成器 (`skill_004`)
- **功能**：自动生成 Obsidian 双链
- **类型**：Core
- **依赖**：3090 算力
- **用途**：增强笔记关联性

## 🔧 技术栈

- **Python 3.8+**
- **python-frontmatter**: 解析 YAML frontmatter
- **httpx**: 异步 HTTP 客户端（调用 3090）
- **asyncio**: 异步执行

## 📝 最佳实践

1. ✅ **命名规范**：`skill_<功能>_<版本>.md`
2. ✅ **版本管理**：语义化版本号
3. ✅ **依赖管理**：使用 Obsidian 双链 `[[skill_xxx]]`
4. ✅ **错误处理**：所有 Skill 必须包含异常处理
5. ✅ **测试覆盖**：提供测试用例
6. ✅ **文档完整**：清晰的功能描述和使用示例

## 🐛 故障排查

常见问题请参考 `SKILL_USAGE_GUIDE.md` 的"故障排查"章节。

## 📞 支持

- **规范问题**：查看 `skill_specification.md`
- **使用问题**：查看 `SKILL_USAGE_GUIDE.md`
- **示例参考**：查看 `examples/` 目录

---

**维护者**：小酷 (CTO)  
**版本**：1.0.0  
**最后更新**：2024-01-01

**符合 SOP**：小报 → 小黑 → **小酷（技术落地）** → Kenny（终审）
