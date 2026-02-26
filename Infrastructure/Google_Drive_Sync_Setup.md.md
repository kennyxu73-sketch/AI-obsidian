# 内阁基建：Google Drive 与 3090 同步配置手册

## 1. 核心凭据 (Credentials)

> **注意：** 请手动填入你刚刚在 Google Cloud Console 获得的秘钥。

- **Client ID:** `429437817441-p6m33f7scubr9h8506p6195l16f6u41l.apps.googleusercontent.com`
    
- **Client Secret:** `[请填入你刚才复制的 GOCSPX 开头的字符串]`
    
- **权限范围 (Scope):** `Drive` (Full Access)
    

---

## 2. 目录映射关系 (Mapping)

为了保持 AI 审计的一致性，本地与云端采用镜像命名：

|**模块职能**|**本地路径 (3090 Ubuntu)**|**云端路径 (Google Drive)**|
|---|---|---|
|**工场 (代码/工具)**|`.../internal_cabinet_tools`|`Cabinet_Base/internal_cabinet_tools`|
|**档案室 (逻辑/宪法)**|`.../000_cabinet_system`|`Cabinet_Base/000_cabinet_system`|

---

## 3. 3090 哨兵脚本逻辑 (`cabinet_watchdog.sh`)

该脚本负责“存盘即同步”并生成“审计就绪”信号。

Bash

```
#!/bin/bash
# 自动同步脚本：监测变动并推送至 Google Drive

# 配置路径
CUR_DIR="/path/to/cursor_workspace/internal_cabinet_tools"
OBS_DIR="/path/to/obsidian/000_cabinet_system"
REMOTE_NAME="gdrive"
HEARTBEAT_FILE="$OBS_DIR/sync_status.json"

echo ">>> 哨兵已就位，正在监听内阁变动..."

# 启动监听
inotifywait -m -r -e modify,create,delete,move "$CUR_DIR" "$OBS_DIR" --exclude "(__pycache__|\.git|sync_status\.json)" | while read path action file
do
    TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
    
    # 1. 标记同步开始
    echo "{\"last_sync\": \"$TIMESTAMP\", \"status\": \"uploading\"}" > "$HEARTBEAT_FILE"

    # 2. 极速同步（排除无用文件）
    rclone sync "$CUR_DIR" "$REMOTE_NAME:Cabinet_Base/internal_cabinet_tools" --exclude "**/__pycache__/**" --exclude "**/.git/**"
    rclone sync "$OBS_DIR" "$REMOTE_NAME:Cabinet_Base/000_cabinet_system"

    # 3. 标记就绪
    if [ $? -eq 0 ]; then
        echo "{\"last_sync\": \"$TIMESTAMP\", \"status\": \"ready\"}" > "$HEARTBEAT_FILE"
        echo -e "\033[1;32m>>> [Audit Ready] 对齐完成，监察官可介入。\033[0m"
    fi
done
```

---

## 4. 监察官 (Gems) 握手协议

在 Gemini Gems 的系统指令中加入以下内容，实现“手动触发审计”：

> **握手逻辑：**
> 
> 1. 每次对话开始，首先读取 `000_cabinet_system/sync_status.json`。
>     
> 2. 核对 `last_sync` 时间。如果 `status` 为 `ready`，播报：“统帅，云端资产已对齐，当前版本 [时间戳]，是否开始审计？”
>     
> 3. 得到肯定答复后，结合 `internal_cabinet_tools` 的代码和 `000_cabinet_system` 的规范进行深度分析。
>     

---