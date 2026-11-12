# 数据合同、计算与状态语义 v1.0

本文件为待实施接口设计，不是已运行数据库。Owner：未来实施Owner；研究规则由Serenity研究Owner验收。字段缺失用null+reason，不用0/空字符串隐藏。

## 1. 共同字段与身份

所有记录含`id, schema_version, created_at_utc, source_ids, supersedes_id, author_role`；修改以新记录替代，不覆盖历史。数值以decimal或可还原字符串存储，显示舍入不进入计算。UTC为计算基准，另保留交易所时区/IANA名称与原时区。

`Security`: `security_id, legal_name, ticker, exchange, currency, quote_unit, effective_from/to, corporate_actions_status, primary_source`。ESMT=台湾3006而非EngageSmart；IQE quote_unit=GBX，100 GBX=1 GBP；DPC/SCTX身份以对应一手记录核对；并购、重组、代码变更保持历史映射，私企/间接敞口单列。

`UniverseVersion`: `universe_id, frozen_at, valid_from, members[], category(formal/historical_lead/fixed_baseline/user_statement), inclusion_source, owner, completion_standard`。当前74家正式池不得与用户事实数量或九家基线相加冒充独立公司数量；同证券去重，覆盖维度另存。

## 2. 来源、事实与实际读取

`SourceDocument`:

| 字段 | 合同 |
|---|---|
| `url, publisher, source_class` | 公司/监管原文、媒体有源转述、作者自述、推测、传闻分开 |
| `published_at, edited_at, filed_at, accepted_at` | 各自原始时点，未知不得用报告期末代替 |
| `retrieved_at, first_seen_at, known_at` | 此流程何时实际可得；保守known_at不得早于证实可得时间 |
| `event_occurred_at, effective_at` | 事件发生与政策/交易生效可不同；不得混同新闻发布时间 |
| `http_status, semantic_status` | 200壳页/解析失败≠正文取得；下载403可与先前公开解析成功并存 |
| `content_hash, local_path, retrieval_method` | 原文件才有原文件hash；DOM人工摘要不是原网页下载hash；不编造 |
| `reading_coverage` | 章节/页/段、全文/片段、图片OCR/视觉、音视频时间段、未读分别存 |
| `revision_of, duplicate_event_key` | 原始、修订、转载与更正链；同源不能重复投票 |

`Fact`: `security_id, metric, value, unit, currency, scale, period_start/end, duration_type(quarter/YTD/FY/instant), accounting_basis, consolidated_or_segment, organic_or_acquired, source_locator, source_id, known_at, is_company_disclosure, interpretation, uncertainty`。

例：TSLA Q2 FCF−1.092bn美元，与H1 CFO8.634bn/资本开支8.282bn不同期间；TSM CFO919.776bn为新台币；NVT持续经营CFO278.7m不等于包含终止业务的268.7m。无法解释的差额保留reconciliation_gap，不凑平。

`CashBridge`: `reported_cash, restricted_cash, financing_net, customer_pass_through_or_advances, cash_available_assumption, CFO, working_capital_components, capex, SBC, debt, guarantees_gross, collateral, dilution, adjustment_sources`。INOD明确扣预付款后约134m可作另一口径，但不把应付/其他负债135.827m全部称同一预付款。NVDA担保名义敞口与抵押不同字段，不能自动净额抵销。

`SocialClaim`: `post_url, author_handle, published/edited/read_at, main_or_reply, claim_summary, evidence_type, primary_links, claimed_interests, uncertainty, counterclaim_ids, media_coverage, primary_verification_state`。只保存必要简短摘要/链接；互动量不作真实性权重，未独立核实的作者持仓只是自述。

## 3. 行情、宏观与事件

`Bar`: `security_id, trading_date, exchange_timezone, session, open/high/low/close, volume_nullable, provider, retrieved_at, available_at, adjusted_flag, adjustment_source, delayed_seconds_nullable`。不把盘后价算常规收盘；缺volume不填0。SCTX61根、DPC81根不够150，`SMA150=null/history_insufficient`，不能判跌破150日。

`MarketSnapshot`: QQQ和VIX分别含时点/时段/现值/日变动/日内结构；SPY/RSP、SOXX或医疗基准另列。`breadth_kind=proxy|full|missing`，RS与收益使用共同交易窗口，`relative_return_pp = stock_return_pct - benchmark_return_pct`，不能与比率型RS混称。复权未核的价格诊断不作总回报基准。

`MacroRelease`: `series, reference_period, release_at, actual, prior_as_released, revised_prior, consensus_nullable, consensus_source/known_at, units, policy_status, speaker_role_valid_at`。预期不可得时surprise=null，不猜。宏观日历不归入公司24小时二元事件。

`CompanyEventCheck`: `security_id, checked_at, SEC_latest_range, IR_news_range, IR_calendar_range, known_event_time, type, materiality_reason, status(PASS/FAIL/UNVERIFIED), residual_risk`。两条有限充分一手路径可用且未发现已知重大事件，PASS+未披露事件残余；任何网页失败不等于FAIL反证。

## 4. 用户事实、研究图和决定

`UserPositionStatement`: `security_id, quantity_nullable, avg_cost_nullable, currency, stated_at, effective_at_nullable, message_locator, certainty, correction_of`。只接受用户主动提供，状态UNKNOWN/explicit_zero/positive分别处理。不调用任何账户接口。建议、未成交限价、未确认卖出不写入此表。

`ResearchMap`: `map_id, security_id, mode, thesis, milestone/date, scenario_inputs, fair_value_range, high_margin_price, reasonable_participation_range, expensive_zone, original_invalidation, economic_invalidation, event_invalidation, profit_protection, prewarning_rule, valid_until, affected_by_fact_ids, status, owner, replacement_deadline`。

`Decision`: `decision_id, asof, known_facts_cutoff, position_statement_id, map_version, policy_version, research_gate, account_gate, fundamental_state, risk_state, action, target_remaining_nullable, target_basis, reasoning, strongest_counterevidence, assumptions, expires_at, replacement_of`。缺资金时research_gate可PASS、account_gate=UNVERIFIED；新买/加仓及预算计算型股数为null。按FR-07拟澄清的退出规则，用户已确认数量且冻结规则可确定目标时可给0至已知数量的研究目标，target_basis=existing_position_exit，不新增暴露；未完成治理统一前按当前有效边界给明确研究动作/计算式，不能编股数。数量也未知则target_remaining=null，问最小必要事实。

`profit_protection`每条包含`rationale_source, trigger_expression, confirmation_session, economic_tradeoff, planned_action, fixed_at, tolerance_basis, expires_on_new_facts`。入场时即预置适用保护和复核要求；盈利后在未触发前明确有效版本。任何使用未来价格随动的方案须在初始版本写清计算法，不能下跌后手工移动。

## 5. 风险公式与偏离处置

设多头数量n，原计划价E，实际用户确认成交价F，当前可用常规/指定时段价格P，固定失效L，用户主动提供且同币种的总资金C。先核价格/失效同复权口径与时点。

- 原计划损失：`n × (E−L)`，仅在E>L、条件未先触发时有效。
- 成交后入场损失：`n × (F−L)`；它用于判断成交是否偏离原风险，不因后来价格变化回写。
- 当前剩余价格风险：`n × (P−L)`，仅在P>L且失效条件尚未满足；它不包括已发生损失，也不保证跳空后实际损失。
- 计划账户损失：`risk/C`；首股金额占比`P/C`。C未知/过期或币种转换未核时比例UNKNOWN，不停止公司/市场判断。
- 如果P≤L或复合失效表达式已满足：`risk_state=TRIGGERED`，不能计算0风险当PASS。
- 交易费/滑点可明确加入计划，但不可从未知费用伪造实际净收益。价格失效位也不等于止损单/保证价。

**成交偏离默认处置（本版待实施规则）**：有有效L/C且尚未触发时，计算`n_budget=floor(0.005×C/(P−L))`。如果现有n>n_budget，默认研究动作REDUCE至不超过n_budget；若n_budget=0，默认EXIT。仅有用户对该具体交易的明确例外，或新事实完成独立重审且获得相应授权，才能标例外；“公司未坏”不能标例外。先看当前风险，保留原违规记录，不把原成本风险重复计为今天新增风险。

若预算现已满足但原预算曾违规，不机械追罚卖出；记录旧违规、当前依据并禁止未复核的继续加风险。经济失效不成立或旧图过期，公式不能兜底造L，转REUNDERWRITE并给临时决定/期限。数量/当轮C不可靠时禁止预算公式自动输出股数；基于已确认数量的退出目标与新增/预算股数按FR-07分开，仍须明确研究风险动作。

历史过程示例，非今天交易建议：

| 示例输入 | 可复算输出 | 应识别的故障 |
|---|---|---|
| INOD原67/52、2股、C3254.25 | 原风险30/C=0.922%；1股0.461% | 事前2改1提示真实存在 |
| 同例用于检验成交后P62.5/L52 | 当前2股21/C=0.645%；n_budget=1 | 成交后不能只停加仓或照旧持有2 |
| FORM F95.89/L79，C取2900作计算样例 | 1股16.89/2900=0.582%；若P仍95.89，n_budget=0 | 单股无法部分减；2900为示例，不冒充当时精确NAV |
| DPC39.5/35.5、3股、C2894 | 风险12/C=0.415% | 数量偏离≠证明预算超限，须单独复核原首日参与限制 |

## 6. 状态迁移

研究：`INCOMPLETE → PASS|OBSERVE|EXCLUDE`；OBSERVE只剩一个可定位缺口，到期必须迁移或DATA_PIPELINE_BLOCKED并改源/Owner。新事实只使受影响维度过期，不能把所有旧证据清零。`deadline`必须带execution_mode=request_driven|authorized_runtime：当前请求式模式在首次相关请求处理过期与同次处置，不声称两次请求间自动交付；未来运行模式才验下一常规盘前SLA。

持仓决定：`HOLD → RISK_REVIEW → REDUCE|EXIT|HOLD`；发生重大新事实可转`REUNDERWRITE`，但附独立`interim_action`。任何action都不是执行确认。

触发：`ARMED → PREWARNING|TRIGGERED → REASSESSED|SUPERSEDED|EXPIRED`。触发历史永久保留，市场反弹不删记录；新决定可更新当前动作，禁止已过期条件僵化执行。

送达（未来授权能力）：`QUEUED → EMITTED → DELIVERED → ACKED`，另有FAILED/UNKNOWN/SUPERSEDED。发送工具返回成功仅证明EMITTED，通道未提供回执则DELIVERED=UNKNOWN。ACKED只代表用户看到/确认，不代表交易。执行必须另有用户确认事件。

事务：事实入库与规则评估可幂等；建议写入和待发送事件同一事务(outbox)防丢，通知重发不重建新交易动作；规则新版本升格预警可发新状态变化。此设计未创建实际服务。

## 7. 回放与效果账

`ReplayDecision`固定source_cutoff/map/policy/model；decision_at之前可得的原始版本才可用。文本LLM可能含未来知识，历史回放只验证规则状态/因果时间，不用于证明LLM选股超额收益。

`HypotheticalExecution`与用户执行分库存储，显著标SIMULATED_POLICY，不冒充真实凭证。信号用常规收盘形成，最早下一可交易时点；限价未触及留UNFILLED；OHLC不能区分同日先止损后止盈则按不利顺序或标歧义，两种敏感性都报告。加入费用/滑点、休市、复权与资金约束，禁止收盘生成信号又用同一收盘完美成交。

`Outcome`分研究政策净结果、用户主动提供的实际结果、匹配基准；缺交易/费用/资金流实际账UNKNOWN。原历史政策不完整则标不可回放，不能补规则；前瞻从同一天冻结完整基线或明确buy-and-hold。请求式与持续运行策略分组，不能把请求时点的记录当全时段监测效果。指标比较同起点、同资金、同币种，现金占用和卖后机会损失一并计，不能只挑卖掉后的下跌。
