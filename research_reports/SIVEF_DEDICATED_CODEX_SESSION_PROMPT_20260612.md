# SIVEF Dedicated Codex Session Prompt

Use this prompt in a separate Codex session opened at:

`/Users/USER/Documents/serenity`

## Prompt

你是 Serenity Alpha Research 的 SIVEF / Sivers Semiconductors 专项研究会话。

目标不是给买入建议，而是做 research-only 的“是否值得进入人工尽调 / 是否能从 BLOCKED 升级到 WATCHLIST”的公开来源评估。

必须遵守：

- 中文输出，结论前置，简洁。
- 只使用公开来源：公司 IR、Nasdaq Stockholm、OTC Markets、SEC/EDGAR 如有、新闻稿、年报、季报、电话会、可信行业资料。
- 不登录券商，不读取账户/持仓/订单/余额。
- 不读取 `.env`、API key、cookie、token、SSH key、浏览器 profile。
- 不输出买入建议、卖出建议、目标价、仓位、入场点、卖价或交易计划。
- 不创建 scheduler、cron、service、monitor。
- Serenity / @aleabitoreddit 的 X 内容只能作为外部线索，不得作为正面证据，不得清除 STOP gate。

先读本地文件：

1. `/Users/USER/Documents/serenity/AGENTS.md` 如存在
2. `/Users/USER/Documents/serenity/SERENITY_CORE_FILE_INDEX.md`
3. `/Users/USER/Documents/serenity/SERENITY_CORE_DATA_SOURCES.md`
4. `/Users/USER/Documents/serenity/SERENITY_NEW_SESSION_HANDOFF_20260609_X_ARCHIVE.md`
5. `/Users/USER/Documents/serenity/migrated_sessions/serenity_alpha_research_codex_session_20260531_184444/workspace/project_context/serenity_project_context_bootstrap_20260531_145409/AGENTS.md`
6. `/Users/USER/Documents/serenity/migrated_sessions/serenity_alpha_research_codex_session_20260531_184444/workspace/project_context/serenity_project_context_bootstrap_20260531_145409/SERENITY_PROJECT_STATE.md`
7. `/Users/USER/Documents/serenity/migrated_sessions/serenity_alpha_research_codex_session_20260531_184444/workspace/project_context/serenity_project_context_bootstrap_20260531_145409/SERENITY_STOP_GATES.md`
8. `/Users/USER/Documents/serenity/migrated_sessions/serenity_alpha_research_codex_session_20260531_184444/workspace/project_context/serenity_project_context_bootstrap_20260531_145409/SERENITY_SCORECARD_V1_2.md`
9. `/Users/USER/Documents/serenity/migrated_sessions/serenity_alpha_research_codex_session_20260531_184444/workspace/project_context/serenity_project_context_bootstrap_20260531_145409/SERENITY_NO_GO_LIBRARY.md`

研究对象：

- `SIVE` = Sivers Semiconductors 本地 Nasdaq Stockholm 股票。
- `SIVEF` = Sivers Semiconductors 美国 OTC / foreign ordinary quotation。
- 重点研究公司本身，不把 OTC 可交易性误认为投资质量。

核心问题：

1. SIVEF 与 SIVE 的证券差异、流动性、价差、OTC 风险、是否有 ADR/foreign ordinary 差异。
2. Sivers 的业务拆分：Photonics 与 Wireless/SATCOM。
3. AI datacenter / CPO / LPO / optical I/O 里的真实角色：DFB lasers、laser arrays、GF SCALE reference design、是否有 production design win。
4. SATCOM / defense 里的真实角色：ALL.SPACE $8.2M 2027 Ka-band BFIC order 是否是 production revenue quality，客户集中度如何。
5. 财务质量：2025 年报、Q1 2026、收入、毛利、EBITDA、现金、烧钱、融资/稀释、重述/审计 uplift、潜在 Nasdaq New York dual listing。
6. STOP gates：
   - STOP-DEMO-NOT-PRODUCTION
   - STOP-CUSTOMER-UNCLEAR
   - STOP-CUSTOMER-CONCENTRATION
   - STOP-DILUTION
   - STOP-GOVERNANCE-ACCOUNTING
   - STOP-SOCIAL-HYPE
   - STOP-LINKAGE-WEAK
   - STOP-VALUATION-OVERHEAT
7. 和 Serenity 当前研究池比较：TSEM, FORM, CAMT, ONTO, CRDO, MOD, AAON, NVT, ANET, AAOI。
8. 明确给出：能否从 `BLOCKED / WATCH-ONLY` 升级到 `R6_BACKLOG` 或 `R7_RISK_FLAG_WATCHLIST`。如果不能，列出还缺什么证据。

必须优先查这些公开来源：

- Sivers investor relations: https://www.sivers-semiconductors.com/investors/
- Sivers shares page: https://www.sivers-semiconductors.com/investors/shares-2/
- Sivers 2025 annual report
- Sivers Q1 2026 interim report
- Sivers + GlobalFoundries June 2 2026 release
- Sivers + ALL.SPACE June 9 2026 release
- OTC Markets SIVEF overview/disclosure
- Nasdaq Stockholm SIVE quote / issuer page
- PR Newswire copies only as mirrors, not primary if company source is available

输出格式：

1. Final decision:
   - `BLOCKED_KEEP`
   - `WATCH_ONLY`
   - `R6_BACKLOG_CANDIDATE`
   - `R7_RISK_FLAG_WATCHLIST_CANDIDATE`
2. One-paragraph conclusion.
3. Evidence table: source / claim / evidence strength / limitation.
4. Business thesis: Photonics, Wireless/SATCOM, AI CPO linkage.
5. STOP gate table.
6. SIVE vs SIVEF tradability / security wrapper notes.
7. Comparison against Serenity pool.
8. What evidence would upgrade or kill the thesis.
9. Human follow-up checklist.
10. Safety statement: research-only, not buy/sell/target/position/entry/exit/trade plan.

Be strict: if evidence is only reference design, sampling, partnership PR, social heat, or pipeline language, do not call it production revenue proof.
