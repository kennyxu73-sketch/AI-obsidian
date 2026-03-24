
# cursor 下 continue 插件的 config 
## 1,直连豆包:

name: "KennyCabinet"
version: "1.0.0"
schema: "v1"

models:
  - name: "内阁-豆包3090"
    provider: "openai"
    # 重点 1：这里直接填豆包的推理端点 ID (ep-xxx)
    model: "ep-20260222002351-fkp5r" 
    # 重点 2：这里的 URL 指向火山引擎官方地址（如果你的 Cursor 电脑能直接上网）
    # 如果你想通过 3090 转发，就填你的 Cloudflare 隧道地址
    apiBase: "https://ark.cn-beijing.volces.com/api/v3"
    # 重点 3：这里填你从火山引擎后台申请的真实 API Key (不是 One-API 的 sk)
    apiKey: "你的火山引擎-豆包API-Key"
    roles:
      - chat
      - edit
      - apply

context:
  - provider: "code"
  - provider: "file"

## 连one api
name: "KennyCabinet"
version: "1.0.0"
schema: "v1"

models:
  - name: "内阁-核心大脑"
    provider: "openai"
    model: "gpt-4o"
    apiBase: "https://revelation-opinion-delivering-enclosure.trycloudflare.com/v1"
    apiKey: "sk-6xV5RJJT23HiaeQMC03500471e3d47Fd85BeFbDcFf787498"
    roles:
      - chat
      - edit
      - apply
  - name: "内阁-代码补全"
    provider: "openai"
    model: "gpt-4o"
    apiBase: "https://revelation-opinion-delivering-enclosure.trycloudflare.com/v1"
    apiKey: "sk-6xV5RJJT23HiaeQMC03500471e3d47Fd85BeFbDcFf787498"
    roles:
      - autocomplete

context:
  - provider: "code"
  - provider: "file"

rules:
  - "请使用中文回答我"