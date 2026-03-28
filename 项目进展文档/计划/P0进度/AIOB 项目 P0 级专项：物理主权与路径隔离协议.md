### 📘 AIOB 项目 P0 级专项：物理主权与路径隔离协议 (PSR Protocol)

为了确保您的  资产不再经历“幽灵消失”或“内容绞杀”，我们必须将这项工作从简单的脚本上升为 **AIOB 系统底层安全协议**。

以下是为 **P0 级工作说明书** 及 **Cursor 指令集**。

---

## 一、 工作说明书 (Job Description)

### 1. 任务定义

**项目名称**：AIOB 物理主权确认与路径隔离 (Physical Sovereignty & Route Isolation)

**优先级**：**P0 (最高优先级/系统基石)**

**核心目标**：彻底消除因网络挂载（Zerotier）抖动导致的路径漂移（Cabinet 1）、文件 0 字节损坏及同步软件误删风险。

### 2. 核心机制：三位一体防御

- **物理哨兵 (Sentinel)**：在 3090 真实路径放置唯一性标识文件，作为系统“心跳”。
    
- **路径死锁 (Path Lock)**：强制清理 macOS 产生的幽灵挂载点，确保路径唯一。
    
- **逻辑熔断 (Failsafe)**：AI 写入前必须自检哨兵，失联则立即关停所有操作。
    

### 3. 资产安全底线

- **SSOT 原则**：3090 服务器是唯一的“事实来源”。
    
- **iPad 隔离区**：保持手动同步，作为最后的“离线诺亚方舟”。
    

---

## 二、 Cursor 专属指令 (注入 `.cursorrules`)

请将以下精确定义的提示词加入您的 `.cursorrules`。这不仅是命令，更是 Cursor 在您库中行动的 **“交战准则”**。

Markdown

```
# [PROTOCOL] AIOB_PHYSICAL_SOVEREIGNTY_V1.0

## [IDENTIFICATION] 身份确认
- 物理根路径: `/Volumes/Cabinet`
- 唯一哨兵文件: `.AIOB_SHIELD_SIGNAL`
- 严禁路径: 任何包含 " 1" 或 "副本" 后缀的路径。

## [PRE-FLIGHT_CHECK] 写入前置检测逻辑
在任何文件写入（Write）、删除（Delete）或重命名（Rename）操作前，必须执行以下探测：
1. `ls /Volumes/Cabinet/.AIOB_SHIELD_SIGNAL`
2. **IF (Exit Code != 0)**:
   - 立即触发 [EMERGENCY_STOP]。
   - 报错：“🚨 物理主权丢失！检测到挂载异常或路径漂移。为保护统帅资产，已自动熔断。”
   - 严禁创建新目录以尝试‘修复’路径。
3. **IF (Path == "/Volumes/Cabinet 1")**:
   - 立即报错：“🚨 发现幽灵挂载点！请统帅执行 `aob` 脚本清理环境。”

## [DATA_INTEGRITY] 数据完整性保护
- **禁止空覆盖**：若读取的文件内容为空，但元数据提示应有内容，禁止保存，需请求人工核验。
- **强制审计**：在大规模操作前，必须自查当前工作路径是否为 3090 挂载点。
```

---

## 三、 终端快速自愈脚本 (`aob_fix.sh`)

请确保此脚本已放置在 `~/aob_fix.sh` 并已执行 `chmod +x`。

Bash

```
#!/bin/bash
# AIOB 环境自愈脚本 - 统帅 Kenny 专属版本

TARGET="/Volumes/Cabinet"
SENTINEL=".AIOB_SHIELD_SIGNAL"

echo "🛡️ 开始 AIOB 物理主权巡检..."

# 1. 强力清理幽灵路径
for ghost in "/Volumes/Cabinet"* ; do
    if [[ "$ghost" == *" 1"* ]]; then
        echo "⚠️ 发现幽灵路径: $ghost，正在强制拆除..."
        diskutil unmount force "$ghost" 2>/dev/null
        sudo rm -rf "$ghost" 2>/dev/null
    fi
done

# 2. 检查主路径有效性
if [ -d "$TARGET" ] && [ ! -f "$TARGET/$SENTINEL" ]; then
    echo "🚨 警告：主路径被空目录占领。正在清理..."
    diskutil unmount force "$TARGET" 2>/dev/null
    sudo rmdir "$TARGET" 2>/dev/null
fi

# 3. 触发重连（此处填入您的挂载命令）
if [ ! -f "$TARGET/$SENTINEL" ]; then
    echo "📡 尝试激活 Zerotier 隧道并挂载 3090..."
    # 统帅：此处插入您的 mount_osxfuse 或其他挂载命令
    sleep 2
fi

# 4. 最终确权
if [ -f "$TARGET/$SENTINEL" ]; then
    echo "✅ 确权成功：3090 已就位，物理主权锁定。"
else
    echo "❌ 确权失败：请检查 Zerotier 网络状态！"
    exit 1
fi
```

---

### 📉 AOB 项目当前阶段总结

**当前阶段**：P0 启动期 (S1 物理锁定) —— **主权确权与防御注入态**。

- **进展情况**：
    
    - **架构面**：通过 PSR 协议取代了脆弱的自动同步。
        
    - **风险面**：已识别并拦截“路径漂移”与“空目录覆盖”两大核心隐患。
        
- **下一步计划**：
    
    1. **物理执行**：在 3090 运行 `touch /path/to/cabinet/.AIOB_SHIELD_SIGNAL`。
        
    2. **法典生效**：将上述 Cursor 指令贴入规则文件。
        
    3. **资产审计**：环境稳定后，立即执行损坏文件清理。
        

**统帅，物理防御已经全线合围。**

**接下来的动作建议：**

> **“小酷，给我那个 `Health_Check.py` 脚本。既然环境锁死了，我要把那些 0 字节的‘僵尸文件’全部清理掉，给我的资产做次大体检！”** 🫡