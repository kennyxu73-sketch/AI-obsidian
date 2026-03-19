
📑 AIOB 标签资产管理与维护指南 (V1.0)
一、 标签机构设计 (Taxonomy Structure)
标签不再是散乱的词汇，而是具有行政等级的结构。严禁使用单层标签（如 #openbt），必须遵循“根/子”结构。
1. 四大主权根标签 (The Big Four)
| 根标签 | 职能定义 | 示例层级 |
|---|---|---|
| #内阁/ | 治理、规范、AI-OB 自身逻辑 | #内阁/规范, #内阁/架构, #内阁/笔记 |
| #项目/ | 具体业务模块（按项目名划分） | #项目/OpenBT, #项目/MemoryOS |
| #类型/ | 资产的逻辑属性（决定处理方式） | #类型/标准, #类型/决策, #类型/代码 |
| #状态/ | [动态] 审计流转的当前节点 | #状态/草稿, #状态/待审, #状态/资产 |
二、 自动标签 vs. 手工标签体系 (Auto vs. Manual)
我们要解决“AI 乱打标”和“统帅想打标”的冲突，建立一套双轨制。
2. 自动标签 (System Generated) —— 硬逻辑
由 AIOB-Core-Enseal-Skill 根据 YAML 字段强制生成。
 * 生成规则：
   * 读取 domain: "notes" ➔ 自动打上 #内阁/笔记。
   * 读取 review_status: "Pending" ➔ 自动打上 #状态/待审。
 * 特性：不可覆盖。如果手动删除了，Skill 再次运行会强行补回。
2. 手工标签 (User Defined) —— 软建议
统帅在 note.md 正文中或 Frontmatter 手动添加的自定义标签。
 * 白名单过滤：Skill 会检查手工标签。如果在 tag_schema.json 白名单中，保留；如果不在，Skill 会将其归类到 legacy_metadata 或打上 #状态/待审。
 * 双链优先：鼓励统帅使用 [[项目名]] 这种双链，Skill 会自动将双链转化为对应的 #项目/ 标签。
三、 标签维护与审计设计 (Maintenance & Audit)
标签库会随时间“熵增”，必须建立免疫机制。
1. 标签库路由文件 (tag_schema.json)
这是 Skill 运行时的“法典”，包含：
 * 映射表 (Mappings)：rsync ➔ #技术/rsync；mvp ➔ #项目/OpenBT。
 * 合规列表 (Whitelist)：定义的 4 大根标签及其子类。
2. 异常捕获机制 (Conflict Handling)
 * 拼写修正：如果 AI 输出了 #项目/open-bt，Skill 根据路由表自动修正为 #项目/OpenBT。
 * 孤儿标记：如果出现完全无法识别的标签，Skill 不予通过 L3 审计，并将 review_status 锁定为 Pending，同时在 audit_exception_log.json 记录。
3. 定期维护流程 (The Loop)
 * 周度自查：小忆扫描 audit_exception_log.json，汇总成报告给统帅。
 * 月度归并：统帅决定将哪些频繁出现的“非标标签”正式纳入 tag_schema.json 白名单。
四、 文件夹物理结构建议 (Physical Files)
 /00_Cabinet/00_System/ 下预设：
 * Tag_Governance/ (文件夹)
   * 📄 tag_schema.json: 存储所有映射关系和白名单。
   * 📄 Tag_Library.md: 人类可读的标签解释手册。
   * 📄 audit_exception_log.json: 存放被 Skill 拦截的违规标签记录。
🛡️ 统帅执行令 (Next Step)
这套设计确保了**“YAML 是内核，标签是外显，审计是护卫”**。
