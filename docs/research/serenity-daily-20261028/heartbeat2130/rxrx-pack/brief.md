# 研究包：RXRX（Recursion Pharmaceuticals, Inc.）

> 数据抓取 2026-10-28T13:38:07Z · 连接器 v9.1.0 · 用时 4.46 秒。以下是数据底稿与机械线索，不是结论；判断写进 lens-draft.json 后用 `serenity_lens.py finish` 收尾。

## 1. 对比表（USD 用即期汇率，仅作横向比较）

| 代码 | 价格 | 市值(USD) | 52周回撤 | 1年涨跌 | TTM收入(USD) | 收入同比 | 收入环比 | 毛利率(期末) | 毛利率同比 | P/S | 股本变化 | 机械旗标 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `RXRX` | 4.16 USD | 2.23B | -31.8% | -24.6% | 54.85M | -60.1% | +18.5% | -49.8% (2026-06-30) | -44.9pp | 40.6x | — | pricing_power, gross_margin_negative, acceleration, repeated_prospectus_takedowns, material_agreement_8k_1_01 |

## 2. 主体要点

- 最新季度收入：7.67M USD（期末 2026-06-30）；营业利润率 -1759.7%；现金+短投 545.68M；FCF 跑道 6.2 季。
- 计算市值：2.23B USD（4.16 × 535,342,170 股，股本截至 2026-07-31）。
- 文件雷达 `repeated_prospectus_takedowns`（PB-FIN-02）：Serial 424B supplements: an 8-K item 1.01 within 2 days usually marks an underwritten follow-on (read the price vs today); without it, suspect an active ATM and size the overhang.
- 文件雷达 `material_agreement_8k_1_01`（PB-SIG-02）：Open the 8-K exhibit: customer/supply/financing agreement? counterparty quality?
- 文件雷达 `beneficial_owner_filings`（PB-SIG-09）：New 13G/13D filers = institutional discovery or activist; read filer name and %.
- 文件雷达 `insider_form4_activity`（PB-SIG-10）：Classify open-market buys (code P) vs sales/grants; buys after a run-up are rarer signals.
- SEC 全文检索命中（近 25 个月）：supply_concentration 4（主文档 2/4）；atm_program 28（主文档 5/6）；capacity_signal 22（主文档 3/6）；going_concern 2（主文档 0/2）

## 2c. 本地财务与公司体检


### 公司体检（通用框架 · company-check-v2）

- 类型路由：**一般经营企业**（依据：SEC SIC 2836 (Biological Products, (No Diagnostic Substances))）
- 数据：sec_companyfacts，报告期 2026-06-30，币种 USD；证据 E-LIVE-FIN
- 阶段：**亏损且不增长**（TTM 亏损且收入增速 < 10%）；该阶段看：现金跑道、融资方式与稀释、收入能否恢复增长
- 结果：🚩 5 · 👀 3 · ✅ 2 · ℹ️ 3 · — 4

| 项目 | 数值 | 状态 | 公式 / 说明 |
|---|---|---|---|
| G1 收入同比 | -60.10% | 🚩 | 最新报告期累计收入同比（A/H 聚合源）或最新季度同比（SEC/Yahoo） |
| G2 归母净利同比 | — | — | TTM 净利润 vs 一年前 TTM（SEC；上年为亏损时不计算） |
| P1 毛利率 | -49.82% | ℹ️ | 毛利 / 收入（最新期） |
| P1d 毛利率同比变化 | -44.94pp | 🚩 | 最新季度毛利率 − 去年同季 |
| P2 净利率（TTM） | -945.92% | ℹ️ | TTM 净利润 / TTM 收入 |
| P3 ROE（TTM） | -56.71% | 🚩 | TTM 归母净利润 / 期末归母权益（未取平均） |
| C1 经营现金流 / 净利润（TTM） | 0.68x | ℹ️ | TTM 经营活动现金流净额 / TTM 净利润；长期 <0.7 说明利润没有变成现金 |
| C2 自由现金流（TTM） | -3.52亿 USD | 👀 | TTM 经营现金流 − TTM 资本开支 |
| C3 股权激励费用 / 收入（TTM） | 165.38% | 🚩 | TTM 股权激励费用 / TTM 收入；高 SBC 是隐性稀释 |
| B1 资产负债率 | 24.55% | ✅ | 总负债 / 总资产 |
| B2 商誉 / 归母权益 | 17.52% | ✅ | 期末商誉 / 期末归母权益；商誉大意味着减值风险 |
| W1 应收增速 − 收入增速 | — | — | 应收账款同比（2025-06-30→2026-06-30）− 收入同比；应收账款不足 TTM 收入的 5%，只作参考 |
| W2 存货增速 − 收入增速 | — | — | 存货同比（2025-06-30→2026-06-30）− 收入同比；存货不足 TTM 收入的 5%，只作参考 |
| W3 合同负债/预收同比 | -30.50% | 👀 | 期末合同负债 / 去年同期 − 1；上升=客户预付增加（需求领先信号）；大降需追问 |
| D1 股本变化（约一年） | — | — | 最新股本 / 4 个观测点前 − 1；持续增发=稀释 |
| R1 现金跑道（月） | 18.60 月 | 👀 | 现金及短投 / (−TTM 自由现金流 / 12)；跑道短 = 近期必须融资；融资方式决定稀释好坏：ATM（持续、无上限，最差）< 溢价可转债 < 定增 < 客户预付/长约（最好） |
| V1 P/S（增速 < 40% 时） | 40.60x | 🚩 | 市值 / TTM 收入，仅在收入增速 < 40% 时打分；好公司 ≠ 好价格：增速不够时高 P/S 需要更强的前瞻证据 |

**估值（USD 口径）**

- 市值 22.27亿 USD · P/B 2.4x · P/S 40.6x
- 股本口径：latest reported shares (market_current)
- 注：loss-making on a TTM basis: P/E not meaningful

**需核实清单（到定期报告/公告原文确认）**

- [ ] 瓶颈/主题业务占总收入的比例（分部披露；占比小=敞口被稀释）
- [ ] 近 12 个月融资：方式（ATM（持续、无上限，最差）< 溢价可转债 < 定增 < 客户预付/长约（最好））、规模/市值、用途、价格；未用完的 ATM/储架额度
- [ ] 前五大客户集中度与长约条款（期限、可取消比例、预付款）
- [ ] G1 收入同比：到定期报告原文核对口径与一次性因素
- [ ] P1d 毛利率同比变化：到定期报告原文核对口径与一次性因素
- [ ] P3 ROE（TTM）：到定期报告原文核对口径与一次性因素
- [ ] C3 股权激励费用 / 收入（TTM）：到定期报告原文核对口径与一次性因素
- [ ] V1 P/S（增速 < 40% 时）：到定期报告原文核对口径与一次性因素

> 机械体检：每项都附公式与阈值（RULES），状态只是“该去看什么”，不是买卖结论。

## 3. 一手文件关键词摘录

### 10-K（提交 2026-02-25，期末 2025-12-31）`E-LIVE-DOC-01`
来源：https://www.sec.gov/Archives/edgar/data/1601830/000160183026000039/rxrx-20251231.htm

- **customer_deposits** ×3：…40,780) Lease liabilities (21,679) Deferred revenue (120,905) Deferred tax liability (23,077) Other liabilities (1,572) Total identifiable net assets $ 526,438 Goodwill 103,686 Total assets acquired and liabilities assumed $ 630,124 Acquired contract liabilities in the scope of ASC 606 are an exception to the ASC 805 fair value measurement principle and were measured as if Recursion had originated the acquired contr
- **sole_source** ×4：…n Act of 2022 (IRA), which includes prescription drug provisions that have significant implications for the pharmaceutical industry and Medicare beneficiaries, including allowing the federal government to negotiate a maximum fair price for certain high-priced single source Medicare drugs, imposing penalties and excise tax for manufacturers that fail to comply with the drug price negotiation requirements, requiring i
- **material_weakness** ×19：…elay, impair, or prevent our development or commercialization efforts. ◦We may not realize all of the anticipated outcomes and benefits of our Acquisitions. ◦Our future success depends on our ability to attract, retain, and motivate key personnel. ◦We have identified material weaknesses in our internal control over financial reporting. 5 Cautionary Note Regarding Forward-Looking Statements This Annual Report on Form
- **export_controls** ×3：…’s attention and resources and significant defense costs and other professional fees. The SEC also may suspend or bar issuers from trading securities on U.S. exchanges for violations of the FCPA’s accounting provisions. We are subject to various governmental export controls, trade and economic sanctions, and import laws and regulations that could impair our ability to compete in international markets and subject us 
- **at_the_market** ×5：…ple, we have from time to time raised capital through the issuance of shares of Class A common stock in public offerings, private placements, and “at-the-market” offerings and may do so in the future. In February 2026, we entered into a sales agreement for an at-the-market offering for the sale of up to $300 million in Class A common stock (see “Part II - Item 9B - Other Information” for further details). In additio

### 10-Q（提交 2026-08-05，期末 2026-06-30）`E-LIVE-DOC-02`
来源：https://www.sec.gov/Archives/edgar/data/1601830/000160183026000098/rxrx-20260630.htm

- **material_weakness** ×5：…f any current or future litigation, which may arise during the ordinary course of business and be costly to defend; •our ability to maintain effective internal control over financial reporting and disclosure controls and procedures, including our ability to remediate the material weaknesses in internal control over financial reporting; •our anticipated use of our existing resources and the net proceeds from our publ
- **at_the_market** ×2：…share on all matters submitted to a vote of the Company’s stockholders. Common stockholders are entitled to receive dividends, as may be declared by the Company’s Board of Directors. As of June 30, 2026 and December 31, 2025, no dividends had been declared. At-The-Market Offerings In February 2026, the Company entered into a Sales Agreement (the TD Cowen Sales Agreement) with TD Securities (USA), LLC (the TD Cowen S

## 4. 图谱位置与下一跳候选

- 未收录于卡点图谱：Not in atlas: map the chain manually (PB-HUNT-08) and consider adding a node.

## 5. Serenity 公开言论记忆（时点）

- 状态：no_mentions；公开时间线里没有关于 RXRX 本身的表态（覆盖至 2026-10-19）。没提到不代表看空。

## 6. 数据质量警告（写进 lens 的 live_data.warnings_addressed）

- `RXRX`：gross_margin_outlier_2026-03-31:-92.99% — check impairment/one-offs/data error
- `RXRX`：gross_margin_outlier_2026-06-30:-49.82% — check impairment/one-offs/data error
- `RXRX`：sec_stale_series_dropped:short_term_investments:last_end_2022-12-31_vs_newest_2026-06-30
- `RXRX`：sec_stale_series_dropped:total_debt:last_end_2021-12-31_vs_newest_2026-06-30
- `RXRX`：sec_stale_series_dropped:receivables:last_end_2022-12-31_vs_newest_2026-06-30

## 7. 下一步（快速路径）

1. 只在 brief 不够时再读一手文件：`python connectors/live_data.py filing-text --ticker X --latest 10-Q --preset contracts`（≤2 份）。
2. 填写 `lens-draft.json` 中所有 `TODO:` 字段（判断、情景、证伪条件、红队）。
3. `python scripts/serenity_lens.py finish lens-draft.json --md report.md --html report.html` 一步完成计算、校验、渲染与核验。

---

框架声明：本 skill 根据 Serenity 公开发布的内容提炼研究框架，用于回测与研究分析；报告由框架生成，不代表 Serenity 本人观点，亦非投资建议。
