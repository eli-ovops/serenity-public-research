# 研究包：SOUN（SoundHound AI, Inc.）

> 数据抓取 2026-11-06T04:28:37Z · 连接器 v9.1.0 · 用时 2.69 秒。以下是数据底稿与机械线索，不是结论；判断写进 lens-draft.json 后用 `serenity_lens.py finish` 收尾。

## 1. 对比表（USD 用即期汇率，仅作横向比较）

| 代码 | 价格 | 市值(USD) | 52周回撤 | 1年涨跌 | TTM收入(USD) | 收入同比 | 收入环比 | 毛利率(期末) | 毛利率同比 | P/S | 股本变化 | 机械旗标 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `SOUN` | 4.26 USD | 74.38M | -72.8% | -70.4% | 203.20M | +45.0% | +40.0% | 45.1% (2026-06-30) | +6.1pp | 0.4x | +0.0% | pricing_power, shelf_registration_on_file, repeated_prospectus_takedowns, unregistered_equity_sale_8k_3_02, material_agreement_8k_1_01 |

## 2. 主体要点

- 最新季度收入：61.90M USD（期末 2026-06-30）；营业利润率 -70.0%；现金+短投 202.78M；FCF 跑道 7.0 季。
- 计算市值：74.38M USD（4.26 × 17,461,000 股，股本截至 2022-03-09）。
- 文件雷达 `shelf_registration_on_file`（PB-FIN-01）：Read the S-3/424B5 for size vs market cap and whether an ATM sales agreement exists.
- 文件雷达 `repeated_prospectus_takedowns`（PB-FIN-02）：Serial 424B supplements: an 8-K item 1.01 within 2 days usually marks an underwritten follow-on (read the price vs today); without it, suspect an active ATM and size the overhang.
- 文件雷达 `unregistered_equity_sale_8k_3_02`（PB-FIN-03）：Private placement/PIPE: who bought, price vs market, lockup, warrants.
- 文件雷达 `material_agreement_8k_1_01`（PB-SIG-02）：Open the 8-K exhibit: customer/supply/financing agreement? counterparty quality?
- 文件雷达 `beneficial_owner_filings`（PB-SIG-09）：New 13G/13D filers = institutional discovery or activist; read filer name and %.
- 文件雷达 `insider_form4_activity`（PB-SIG-10）：Classify open-market buys (code P) vs sales/grants; buys after a run-up are rarer signals.
- SEC 全文检索命中（近 25 个月）：customer_concentration 7（主文档 1/6）；atm_program 41（主文档 5/6）；capacity_signal 36（主文档 1/6）；going_concern 15（主文档 3/6）

## 2c. 本地财务与公司体检


### 公司体检（通用框架 · company-check-v2）

- 类型路由：**一般经营企业**（依据：SEC SIC 7372 (Services-Prepackaged Software)）
- 数据：sec_companyfacts，报告期 2026-06-30，币种 USD；证据 E-LIVE-FIN
- 阶段：**认证/放量期**（TTM 亏损且收入同比 45% ≥ 25%）；该阶段看：认证/客户导入进度、订单与长约（可取消比例）、产能与良率爬坡、现金跑道、融资方式
- 结果：🚩 1 · 👀 2 · ✅ 7 · ℹ️ 4 · — 3

| 项目 | 数值 | 状态 | 公式 / 说明 |
|---|---|---|---|
| G1 收入同比 | 45.02% | ✅ | 最新报告期累计收入同比（A/H 聚合源）或最新季度同比（SEC/Yahoo） |
| G2 归母净利同比 | — | — | TTM 净利润 vs 一年前 TTM（SEC；上年为亏损时不计算） |
| P1 毛利率 | 45.12% | ℹ️ | 毛利 / 收入（最新期） |
| P1d 毛利率同比变化 | 6.08pp | ✅ | 最新季度毛利率 − 去年同季 |
| P2 净利率（TTM） | -67.45% | ℹ️ | TTM 净利润 / TTM 收入 |
| P3 ROE（TTM） | -27.95% | ℹ️ | TTM 归母净利润 / 期末归母权益（未取平均）；认证/放量期：当期利润不是关键 KPI，改看订单、认证、产能、现金跑道与融资方式 |
| C1 经营现金流 / 净利润（TTM） | 0.84x | ℹ️ | TTM 经营活动现金流净额 / TTM 净利润；长期 <0.7 说明利润没有变成现金 |
| C2 自由现金流（TTM） | -1.16亿 USD | 👀 | TTM 经营现金流 − TTM 资本开支 |
| C3 股权激励费用 / 收入（TTM） | 38.65% | 🚩 | TTM 股权激励费用 / TTM 收入；高 SBC 是隐性稀释 |
| B1 资产负债率 | 26.57% | ✅ | 总负债 / 总资产 |
| B2 商誉 / 归母权益 | 24.93% | ✅ | 期末商誉 / 期末归母权益；商誉大意味着减值风险 |
| W1 应收增速 − 收入增速 | — | — | 应收账款同比（2025-06-30→2026-06-30）− 收入同比；应收账款不足 TTM 收入的 5%，只作参考 |
| W2 存货增速 − 收入增速 | — | — | 存货同比（2025-06-30→2026-06-30）− 收入同比；存货不足 TTM 收入的 5%，只作参考 |
| W3 合同负债/预收同比 | 0.10% | ✅ | 期末合同负债 / 去年同期 − 1；上升=客户预付增加（需求领先信号）；大降需追问 |
| D1 股本变化（约一年） | 0.00% | ✅ | 最新股本 / 4 个观测点前 − 1；持续增发=稀释 |
| R1 现金跑道（月） | 21.00 月 | 👀 | 现金及短投 / (−TTM 自由现金流 / 12)；跑道短 = 近期必须融资；融资方式决定稀释好坏：ATM（持续、无上限，最差）< 溢价可转债 < 定增 < 客户预付/长约（最好） |
| V1 P/S（认证/放量期） | 0.37x | ✅ | 市值 / TTM 收入；放量期阈值放宽，但极端倍数仍要求订单/长约能覆盖；放量期不看当期利润，但好公司 ≠ 好价格：倍数要能被已签订单和产能爬坡解释 |

**估值（USD 口径）**

- 市值 74,383,860.00 USD · P/B 0.1x · P/S 0.4x
- 股本口径：latest reported shares (market_current)
- 注：loss-making on a TTM basis: P/E not meaningful

**需核实清单（到定期报告/公告原文确认）**

- [ ] 瓶颈/主题业务占总收入的比例（分部披露；占比小=敞口被稀释）
- [ ] 近 12 个月融资：方式（ATM（持续、无上限，最差）< 溢价可转债 < 定增 < 客户预付/长约（最好））、规模/市值、用途、价格；未用完的 ATM/储架额度
- [ ] 前五大客户集中度与长约条款（期限、可取消比例、预付款）
- [ ] 认证阶段与时间表（样品→认证→小批量→量产），以公司原话为准
- [ ] C3 股权激励费用 / 收入（TTM）：到定期报告原文核对口径与一次性因素

> 机械体检：每项都附公式与阈值（RULES），状态只是“该去看什么”，不是买卖结论。

## 3. 一手文件关键词摘录

### 10-K（提交 2026-03-02，期末 2025-12-31）`E-LIVE-DOC-01`
来源：https://www.sec.gov/Archives/edgar/data/1840856/000184085626000006/soun-20251231.htm

- **remaining_performance_obligations** ×4：…rvices revenue. The revenues from Amelia Software Platform and Virtual Assistance are included within Service Subscriptions, and are recognized point in time or over time depending on the arrangement. We have and may continue to experience volatility for our remaining performance obligations and deferred revenue as a result of the timing for completing our performance obligations. We had remaining performance obliga
- **customer_concentration** ×18：…l to continue planned business operations but may not be able to obtain such capital when desired on favorable terms, if at all, or without dilution to our stockholders; •Our operating results could be materially and adversely affected if it loses any of its largest customers due to concentration risk; •The market in which we operate is highly competitive and rapidly changing and we may be unable to compete successf
- **material_weakness** ×16：…ctions and any potential future acquisitions or strategic transactions may not be accretive and may subject us to various risks that could adversely affect our business and for which we may not achieve the anticipated benefit of such a transaction; •We have identified material weaknesses in our internal control over financial reporting and may identify additional material weaknesses in the future, which may result i
- **export_controls** ×6：…nd retain employees who want or need more flexibility. Government Regulations We are subject to various laws, regulations, and permitting requirements of federal, state, and local authorities, related to health and safety, consumer privacy, anti-corruption, export controls and AI-related regulations. The foregoing may include the U.S. Foreign Corrupt Practices Act of 1977, the U.S. Export Administration Regulations,
- **at_the_market** ×44：…2025, 2024 and 2023. Accordingly, SoundHound may require additional capital to continue its planned business operations. SoundHound anticipates that current cash, cash equivalents, cash provided by operating activities and funds available through SoundHound’s at-the-market offering program ("ATM"), will not be sufficient to meet its long-term expected future capital needs. SoundHound will need additional financing t
- **default_covenant** ×1：…The Amelia Debt will accrue interest at an annual rate equal to the sum of (a) Adjusted Term SOFR and (b)(i) an applicable margin of 9.00% for the portion of interest paid in cash, and (ii) an additional 1.00% for the portion of interest paid in kind. Upon an event of default, the interest rate will automatically increase by an additional 2.00% per annum, and may result in the declaration that all outstanding princi

### 10-Q（提交 2026-08-10，期末 2026-06-30）`E-LIVE-DOC-02`
来源：https://www.sec.gov/Archives/edgar/data/1840856/000184085626000022/soun-20260630.htm

- **remaining_performance_obligations** ×4：…respectively, for the three and six months ended June 30, 2026 as compared to $10.9 million and $16.7 million, respectively for the three and six months ended June 30, 2025. As of June 30, 2026, the aggregate amount of the transaction price allocated to the remaining performance obligations related to customer contracts that were unsatisfied or partially unsatisfied was $60.0 million. Given the applicable contract t
- **customer_concentration** ×7：…ances of which frequently exceed federally insured limits. The Company regularly monitors its credit risk exposure and takes steps to mitigate the likelihood of these exposures resulting in actual loss. As of June 30, 2026 and December 31, 2025, there was no customer that accounted for more than 10% of the Company’s accounts receivable balance. As of June 30, 2026, unbilled receivables from Customer A, B, C, and D a
- **material_weakness** ×6：…iss the Complaint on December 12, 2025. On May 19, 2026, the court granted SoundHound’s motion in part and denied it in part. The court dismissed the claims based on the Amelia accounting statements, as well as several statements about SoundHound’s efforts to remediate material weaknesses in its internal controls. The court denied the motion, however, as to certain internal-control statements. The case is scheduled 
- **at_the_market** ×38：…Balance as of March 31, 2026 — $ — 393,742,421 $ 37 32,535,408 $ 3 $ 1,442,560 $ (982,094) $ 160 $ 460,666 Issuance of Class A common stock for equity incentive awards — — 3,311,779 — — — 3,527 — — 3,527 Issuance of Class A common stock under the Second Equity Distribution Agreement, net of issuance costs — — 6,232,900 1 — — 47,461 — — 47,462 Stock-based compensation — — — — — — 21,593 — — 21,593 Net loss — — — — — 

## 4. 图谱位置与下一跳候选

- 未收录于卡点图谱：Not in atlas: map the chain manually (PB-HUNT-08) and consider adding a node.

## 5. Serenity 公开言论记忆（时点）

- 状态：available；公开帖转述（不是原话，不含订阅内容），帖子编号可在 x.com 查原文。立场 = 当时公开表达的看法，不是持仓记录；2026-10-19 之后是否有新表态未知（沉默不等于卖出）。Serenity 的说法是线索，不是公司事实。
  - 2026-01-14 `2011330371464675631` MENTION/neutral

## 6. 数据质量警告（写进 lens 的 live_data.warnings_addressed）

- `SOUN`：share_count_older_than_200_days
- `SOUN`：sec_stale_series_dropped:total_debt:last_end_2024-12-31_vs_newest_2026-06-30

## 7. 下一步（快速路径）

1. 只在 brief 不够时再读一手文件：`python connectors/live_data.py filing-text --ticker X --latest 10-Q --preset contracts`（≤2 份）。
2. 填写 `lens-draft.json` 中所有 `TODO:` 字段（判断、情景、证伪条件、红队）。
3. `python scripts/serenity_lens.py finish lens-draft.json --md report.md --html report.html` 一步完成计算、校验、渲染与核验。

---

框架声明：本 skill 根据 Serenity 公开发布的内容提炼研究框架，用于回测与研究分析；报告由框架生成，不代表 Serenity 本人观点，亦非投资建议。
