# AI-Obsidian 项目文档

优先级：高 日期：2026-02-14


## 1. 项目背景

利用 NVIDIA 3090 算力中心，构建以 Dify 为核心的本地知识库与语音交互系统，建立自己的笔记管理工作体系
  

## 2. 核心架构参数

• 算力节点：NVIDIA GeForce RTX 3090 (24GB VRAM)

  

• 推理后端：

  

  • AI 对话：`[http://localhost:8189/v1/chat/completions](http://localhost:8189/v1/chat/completions)` (OpenAI 标准)

  

  • 语音识别 (ASR)：`ws://localhost:8766/ws/asr/stream`

  

  • 备用引擎：Ollama (已安装，CUDA 12/13)

  

• 管理平台：Dify (Docker 部署)

  

• 文档存储：3090 本地目录 `/home/comfcare/my_obsidian_vault`

  

## 3. 待办事项 (Next Steps)

• Dify 连接：配置 OpenAI-like 供应商指向 `[可疑链接已删除]`

  

• 目录挂载：将 3090 的 Obsidian 文件夹映射至 Dify Docker 容器

  

• 语音调试：测试 ASR 接口与 Dify 的流式交互

  

• 插件安装：在 Obsidian 中安装 Smart Connections 插件

  

## 4. 风险记录

• 显存竞争：当前 8189 进程已占用大部分显存，需监控显存分配。

  

• 数据恢复：NAS 7.81T 卷组暂时封存，待系统跑通后通过 7.4K 元数据备份恢复。

  

---