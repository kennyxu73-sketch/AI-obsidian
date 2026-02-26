

## 1. 核心指挥层 (Command Center)

• 设备: MacBook Pro (已重装，纯净系统)
• 软件: Obsidian (作为全局 UI)
• 目标: 通过 Markdown 和 Canvas 可视化所有内阁资产，发布指令。

## 2. 算力引擎层 (Compute Engine)

• 设备: Ubuntu 3090 服务器

• 核心组件:
  • Docker: 容器化管理
  • Dify: AI Agent 编排平台
  • Local LLMs: 部署在 3090 上的大模型
• 连接: 通过 SSH 和 ZeroTier 接入。

## 3. 存储资产层 (Storage & Assets)

• 设备: QNAP NAS (IP: 192.168.0.2)

• 目录结构:

  

  • `/share/Cabinet/Obsidian`: 核心知识库 (Markdown)

  

  • `/share/Cabinet/Archive`: 历史备份与 Mindmap 旧资产

  

  • `/share/Cabinet/AI_Models`: 模型权重存储

  

• 协议: SMB/NFS 挂载至 3090 和 Mac。

  

## 4. 网络海关层 (Network & Gateway)

• 设备: NAS 虚拟机中的 OpenWrt

  

• 核心功能:

  

  • ZeroTier: 构建跨地域虚拟内网

  

  • 流量分流: 解决移动端 VPN 冲突 (iPad/iPhone)

  

  • 翻墙中转: 借道 OpenWrt 访问海外 AI 服务。

  

## 5. 移动端接入 (Remote Access)

• 设备: iPad / iPhone

  

• 软件: ZeroTier + Obsidian Mobile

  

• 场景: 在外随时调阅 Skill 笔记，监控 3090 任务进度。

  

---