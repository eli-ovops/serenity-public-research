# Serenity 研究实验卡

更新：2026-07-16

用途：把研究视为可连续复盘、可证伪的实验。本文只管理研究过程，不是交易系统，不输出买卖建议、目标价、仓位、入场/退出点或当前买入名单。

本机制不替代现有治理：

- 先按 [SERENITY_TOTAL_CONTROL.md](SERENITY_TOTAL_CONTROL.md) 从瓶颈环节出发，再映射候选。
- 先检查 [SERENITY_STOP_GATES.md](migrated_sessions/serenity_alpha_research_codex_session_20260531_184444/workspace/project_context/serenity_project_context_bootstrap_20260531_145409/SERENITY_STOP_GATES.md)，再使用 [SERENITY_SCORECARD_V1_2.md](migrated_sessions/serenity_alpha_research_codex_session_20260531_184444/workspace/project_context/serenity_project_context_bootstrap_20260531_145409/SERENITY_SCORECARD_V1_2.md)。
- [SERENITY_NO_GO_LIBRARY.md](migrated_sessions/serenity_alpha_research_codex_session_20260531_184444/workspace/project_context/serenity_project_context_bootstrap_20260531_145409/SERENITY_NO_GO_LIBRARY.md)、R6/R7、`BLOCKED`、`NO-GO` 等候选治理状态仍是最终约束。
- 本文的实验状态只描述一条研究假设的生命周期，不得用于绕过 STOP gate、NO-GO 或提高候选等级。

## 1. 研究实验卡模板

每张卡使用稳定 ID，例如 `EXP-YYYYMMDD-主题-01`。新证据更新同一卡的版本和复盘记录；假设实质改变时必须新建卡，不得改写旧假设来制造“仍然正确”。

```text
实验 ID / 版本：
研究问题：
研究假设：一句可被公开证据证伪的陈述
瓶颈环节：容量 / 良率 / 资格认证 / 工具 / 材料 / 电力 / 散热 / 其他
环境条件：假设成立所依赖的需求、技术、供应、监管和时间窗口
研究对象范围：lane / stack layer / candidate subset；不得从 ticker-first 开始

一手证据：逐条记录 filing、IR、正式产品/订单/收入/客户/产能披露及定位；没有则写“缺失”
证据分层：
- Confirmed：filing、IR、正式产品/订单/收入/客户/产能披露
- Management claim：公司正式陈述但尚未被收入或生产事实验证
- Inferred：由多源证据推导，必须写明推导链
- Weak：社交、论坛、KOL 或未核验截图，只能作为线索/拥挤风险
- Needs verification：关键缺口及所需一手来源

证据强度：当前最强标签 + 最弱关键假设
可观察预测：对象 + 指标/事件 + 时间窗口 + 预期方向
确认条件：哪些公开事实出现后，假设得到加强
失效条件：哪些公开事实出现后，假设被证伪或必须降级
当前实验状态：OPEN / NOT_READY / INVALIDATED / REOPEN_TRIGGER
候选治理状态：沿用 R6/R7/BLOCKED/NO-GO/anchor-only 等；不得由实验状态自动改变
重开条件：INVALIDATED 后，必须出现的 materially different public evidence
最强反证：当前最能推翻假设的证据或替代解释
开放 STOP gates：逐项列出 STOP-*；未检查不得评分
NO-GO 核对：命中 / 未命中 / 不适用；命中时记录权威条款
Scorecard 快照：只记录现有 Opportunity / Evidence / Survivability / Penalty 维度及理由
风险：证据、执行、替代、客户、地缘、治理、财务与 shareholder capture
下一复盘触发：公开 filing / IR / 资格认证 / 产能 / 收入转换等事件；不得创建 scheduler
来源：文件或公开来源标题、日期、定位
Owner / 复核者：
```

## 2. 实验状态与转换

| 状态 | 含义 | 允许进入 | 允许离开 | 禁止事项 |
| --- | --- | --- | --- | --- |
| `OPEN` | 假设可证伪，预测、确认/失效条件和来源已写明，正在等待或吸收证据 | 新卡完成最低字段；或 `REOPEN_TRIGGER` 经重新审查后成立 | 到 `NOT_READY` 或 `INVALIDATED` | 不等于候选升级、评分通过或结论成立 |
| `NOT_READY` | 证据不足、预测不可观察、关键环境条件不清，或 STOP gate 尚未完成 | 新卡不完整；`OPEN` 出现关键缺口；重开证据不足 | 补齐后到 `OPEN`；出现反证到 `INVALIDATED` | 不得用叙事、价格变化或社交热度补足证据 |
| `INVALIDATED` | 已记录的失效条件发生，或最强反证足以推翻关键因果链 | `OPEN` / `NOT_READY` 经证据复核 | 只能到 `REOPEN_TRIGGER` | 不得直接回到 `OPEN`，不得删除旧失效记录或改写原假设 |
| `REOPEN_TRIGGER` | 出现预先写明的 materially different public evidence，具备重新审查资格 | 只能从 `INVALIDATED` 进入 | 重跑 STOP gate、NO-GO、scorecard 和反证审查后，到新版本 `OPEN` 或 `NOT_READY`；证据不成立则回 `INVALIDATED` | 不是“已重开”或“恢复原结论”，不得自动恢复旧候选等级 |

强制转换规则：

1. `OPEN -> INVALIDATED` 必须引用命中的失效条件和对应证据。
2. `INVALIDATED -> REOPEN_TRIGGER` 必须逐字引用原卡的重开条件，并证明新证据与旧叙事有实质差异。
3. `REOPEN_TRIGGER` 评审必须建立新版本，保留旧版本、旧证据曲线和最强反证。
4. NO-GO 项即使进入 `REOPEN_TRIGGER`，也仍保持 NO-GO，直到现有权威规则按 materially different public evidence 明确改判。

## 3. 最小复盘：证据曲线

证据曲线记录“证据是否越来越硬”，不记录价格表现，也不另造候选分数。每次实质更新追加一行：

| 日期/版本 | 新证据及来源 | 标签 | 对预测的方向 | 影响的 STOP gate / Scorecard 维度 | 曲线 | 说明 |
| --- | --- | --- | --- | --- | --- | --- |
| YYYY-MM-DD / vN | 可定位的一手或二手材料 | Confirmed / Management claim / Inferred / Weak / Needs verification | 支持 / 中性 / 反证 | STOP-*；现有 scorecard 字段 | `↑` / `→` / `↓` | 为什么改变或不改变 |

解释：

- `↑`：出现更直接的一手证据、跨链确认、生产/收入转换或重复验证。
- `→`：只有重复叙事、同源转述，或证据未触及关键预测。
- `↓`：预测落空、出现直接反证、来源可靠性下降，或 STOP gate 加重。
- 单条管理层陈述或社交信息不得单独形成 `↑`；价格变化永远不是确认条件。

## 4. 最小复盘：研究可信度曲线

研究可信度曲线只评价过程质量，不能抵消 STOP gate 或提高候选等级。每次复盘对五项标记 `完整 / 部分 / 缺失`，并记录趋势 `↑ / → / ↓`：

1. 来源可追溯：关键陈述能定位到日期、文件和原文位置。
2. 分层清楚：Confirmed、Management claim、Inferred、Weak、Needs verification 未混写。
3. 可证伪：预测、确认、失效与重开条件具体且可观察。
4. 反证优先：记录最强反证和至少一个替代解释，不只收集支持材料。
5. 治理完整：已先检查 STOP gate / NO-GO，再记录现有 scorecard 快照。

若任一关键结论缺少来源、失效条件或最强反证，可信度不得标记为上升。研究可信度上升也不代表研究假设成立。

## 5. 接入现有研究队列

研究队列中的任务执行时，至少补充：

- `实验 ID`
- 当前实验状态
- 本轮要观察的预测/事件
- 开放 STOP gates
- 下一证据触发或重开条件

队列优先级仍由既有 P1-P4、R6/R7 与 PMO 判断决定。P4 / fail-closed 项只有在满足卡内预登记的重开条件时才进入 `REOPEN_TRIGGER` 复核；否则不消耗优先研究资源。

## 6. 示例卡（仅演示，不是项目结论）

```text
实验 ID / 版本：EXP-DEMO-LIQUID-COOLING-01 / v1
研究问题：AI factory 扩张时，液冷部件的资格认证是否会比名义产能更早成为交付瓶颈？
研究假设：在示例观察窗口内，若高密度机柜部署继续扩张，已通过客户资格认证的液冷部件供应将比通用制造产能更稀缺。
瓶颈环节：资格认证 / 可靠性验证 / 产能爬坡
环境条件：高密度机柜部署继续；散热规格没有被替代架构显著降低；认证周期未明显缩短。
研究对象范围：液冷资格认证 lane；不映射具体证券。
一手证据：缺失；需核对公开的认证周期、量产出货、产能与收入转换披露。
证据分层：Needs verification。
证据强度：Needs verification；最弱假设是“认证周期而非项目施工或终端需求才是首要约束”。
可观察预测：后续公开材料同时出现认证周期延长、合格供应商数量受限，并有量产/收入转换证据。
确认条件：至少一项直接一手披露加一项跨链独立确认，且不是 demo、MoU 或 reference design。
失效条件：交付延迟主要由终端需求、项目施工或通用产能造成；认证供应快速扩张且未形成约束。
当前实验状态：NOT_READY
候选治理状态：不适用
重开条件：若本卡因“认证不是瓶颈”而 INVALIDATED，只有新的公开量产延迟与认证受限证据同时出现才可触发复核。
最强反证：名义产能和认证供应均充足，实际部署瓶颈位于电力接入或现场施工。
开放 STOP gates：STOP-LINKAGE-WEAK；STOP-DEMO-NOT-PRODUCTION。
NO-GO 核对：不适用。
风险：把行业增长误当资格认证瓶颈；把管理层 pipeline 当成生产事实。
下一复盘触发：公开 filing / IR 中出现认证、量产和收入转换的可核验证据。
来源：示例占位，不构成证据。
```
