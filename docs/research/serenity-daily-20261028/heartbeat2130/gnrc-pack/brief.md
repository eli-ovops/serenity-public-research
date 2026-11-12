# 研究包：GNRC（Generac Holdings Inc.）

> 数据抓取 2026-10-28T13:41:47Z · 连接器 v9.1.0 · 用时 2.94 秒。以下是数据底稿与机械线索，不是结论；判断写进 lens-draft.json 后用 `serenity_lens.py finish` 收尾。

## 1. 对比表（USD 用即期汇率，仅作横向比较）

| 代码 | 价格 | 市值(USD) | 52周回撤 | 1年涨跌 | TTM收入(USD) | 收入同比 | 收入环比 | 毛利率(期末) | 毛利率同比 | P/S | 股本变化 | 机械旗标 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `GNRC` | 182.65 USD | 10.78B | -38.4% | +8.7% | 4.44B | +10.6% | +10.8% | 44.5% (2026-06-30) | +5.2pp | 2.4x | +0.6% | pricing_power, unregistered_equity_sale_8k_3_02, material_agreement_8k_1_01, beneficial_owner_filings, insider_form4_activity |

## 2. 主体要点

- 最新季度收入：1.17B USD（期末 2026-06-30）；营业利润率 17.9%；现金+短投 264.92M；FCF 跑道 — 季。
- 计算市值：10.78B USD（182.65 × 59,006,361 股，股本截至 2026-07-31）。
- 文件雷达 `unregistered_equity_sale_8k_3_02`（PB-FIN-03）：Private placement/PIPE: who bought, price vs market, lockup, warrants.
- 文件雷达 `material_agreement_8k_1_01`（PB-SIG-02）：Open the 8-K exhibit: customer/supply/financing agreement? counterparty quality?
- 文件雷达 `beneficial_owner_filings`（PB-SIG-09）：New 13G/13D filers = institutional discovery or activist; read filer name and %.
- 文件雷达 `insider_form4_activity`（PB-SIG-10）：Classify open-market buys (code P) vs sales/grants; buys after a run-up are rarer signals.
- SEC 全文检索命中（近 25 个月）：supply_concentration 19（主文档 0/6）；customer_concentration 4（主文档 2/4）；atm_program 2（主文档 0/2）；capacity_signal 15（主文档 4/6）；going_concern 1（主文档 0/1）

## 2c. 本地财务与公司体检


### 公司体检（通用框架 · company-check-v2）

- 类型路由：**一般经营企业**（依据：SEC SIC 3621 (Motors & Generators)）
- 数据：sec_companyfacts，报告期 2026-06-30，币种 USD；证据 E-LIVE-FIN
- 阶段：**常规经营期**（常规口径）；该阶段看：收入增速、利润率、现金转换、估值
- 结果：🚩 2 · 👀 0 · ✅ 12 · ℹ️ 3 · — 0

| 项目 | 数值 | 状态 | 公式 / 说明 |
|---|---|---|---|
| G1 收入同比 | 10.59% | ✅ | 最新报告期累计收入同比（A/H 聚合源）或最新季度同比（SEC/Yahoo） |
| G2 归母净利同比 | -25.98% | 🚩 | TTM 净利润 vs 一年前 TTM（SEC；上年为亏损时不计算） |
| P1 毛利率 | 44.47% | ℹ️ | 毛利 / 收入（最新期） |
| P1d 毛利率同比变化 | 5.20pp | ✅ | 最新季度毛利率 − 去年同季 |
| P2 净利率（TTM） | 5.82% | ℹ️ | TTM 净利润 / TTM 收入 |
| P3 ROE（TTM） | 8.97% | ✅ | TTM 归母净利润 / 期末归母权益（未取平均） |
| C1 经营现金流 / 净利润（TTM） | 2.12x | ✅ | TTM 经营活动现金流净额 / TTM 净利润；长期 <0.7 说明利润没有变成现金 |
| C2 自由现金流（TTM） | 3.79亿 USD | ✅ | TTM 经营现金流 − TTM 资本开支 |
| C3 股权激励费用 / 收入（TTM） | 1.15% | ✅ | TTM 股权激励费用 / TTM 收入；高 SBC 是隐性稀释 |
| B1 资产负债率 | 50.14% | ✅ | 总负债 / 总资产 |
| B2 商誉 / 归母权益 | 57.40% | 🚩 | 期末商誉 / 期末归母权益；商誉大意味着减值风险 |
| B3 净现金（现金 − 有息负债） | -9.26亿 USD | ℹ️ | 现金及等价物(+短期存款/短投) − 短借 − 长借 − 应付债券 |
| W1 应收增速 − 收入增速 | -7.43pp | ✅ | 应收账款同比（2025-06-30→2026-06-30）− 收入同比 |
| W2 存货增速 − 收入增速 | -11.81pp | ✅ | 存货同比（2025-06-30→2026-06-30）− 收入同比 |
| W3 合同负债/预收同比 | 395.89% | ✅ | 期末合同负债 / 去年同期 − 1；上升=客户预付增加（需求领先信号）；大降需追问 |
| D1 股本变化（约一年） | 0.56% | ✅ | 最新股本 / 4 个观测点前 − 1；持续增发=稀释 |
| V1 P/S（增速 < 40% 时） | 2.43x | ✅ | 市值 / TTM 收入，仅在收入增速 < 40% 时打分；好公司 ≠ 好价格：增速不够时高 P/S 需要更强的前瞻证据 |

**估值（USD 口径）**

- 市值 107.78亿 USD · P/E(TTM) 41.7x · P/B 3.8x · P/S 2.4x · P/FCF 28.4x
- 股本口径：latest reported shares (market_current)

**需核实清单（到定期报告/公告原文确认）**

- [ ] 瓶颈/主题业务占总收入的比例（分部披露；占比小=敞口被稀释）
- [ ] 近 12 个月融资：方式（ATM（持续、无上限，最差）< 溢价可转债 < 定增 < 客户预付/长约（最好））、规模/市值、用途、价格；未用完的 ATM/储架额度
- [ ] 前五大客户集中度与长约条款（期限、可取消比例、预付款）
- [ ] G2 归母净利同比：到定期报告原文核对口径与一次性因素
- [ ] B2 商誉 / 归母权益：到定期报告原文核对口径与一次性因素

> 机械体检：每项都附公式与阈值（RULES），状态只是“该去看什么”，不是买卖结论。

## 3. 一手文件关键词摘录

### 10-K（提交 2026-02-18，期末 2025-12-31）`E-LIVE-DOC-01`
来源：https://www.sec.gov/Archives/edgar/data/1474735/000143774926004568/gnrc20251231_10k.htm

- **remaining_performance_obligations** ×2：…During the year ended December 31, 2024, the Company recognized revenue of $19,173 related to amounts included in the December 31, 2023 deferred revenue balance. As of December 31, 2025, the aggregate amount of revenue that the Company expects to recognize on remaining performance obligations (excluding extended warranty) was $378,782, of which 100% is expected to be recognized as revenue over the next two years. We
- **customer_deposits** ×3：…changes in estimated sales or costs and the resulting profit or loss on a cumulative basis in the period when the estimate changes. Total service revenues accounted for approximately 4% of net sales during the years ended December 31, 2025, 2024 and 2023. Contract Liabilities While the Company’s standard payment terms are less than one year, the specific payment terms and conditions in its customer contracts vary. I
- **long_term_supply_agreement** ×1：…nd our control. We have seen such trends significantly impact our business in the past resulting in higher costs and shortages in materials, components and labor, and such impacts may continue or arise again in the foreseeable future. We typically do not have long-term supply contracts in place to ensure the raw materials and components we use are available in necessary amounts or at fixed prices. In the short-term,
- **sole_source** ×4：…g demand for our products; ● fluctuations in cost, availability, and quality of raw materials, key components and labor required to manufacture our products; ● our dependence on a small number of contract manufacturers and component suppliers, including single-source suppliers; ● changes and volatility with respect to the trade policies of various countries, which may result in new or increased tariffs, trade restri
- **customer_concentration** ×2：…majority of its domestic cash in a few commercial banks in multiple operating and investment accounts. Balances on deposit are insured by the Federal Deposit Insurance Corporation (FDIC) up to specified limits. Balances in excess of FDIC limits are uninsured. One customer accounted for approximately 9% and 10% of accounts receivable as of December 31, 2025 and 2024, respectively. No one customer accounted for greate
- **export_controls** ×1：…federal and state laws and multiple foreign laws, regulations and policies. These laws and regulations are complex, change frequently, have become more stringent over time and increase our cost of doing business. These laws and regulations include import and export control, sanction and trade restriction laws, environmental, health and safety regulations, data privacy requirements, international labor laws and work 
- **default_covenant** ×2：…such default occurs, the lenders under our credit facilities may elect to declare all outstanding borrowings, together with accrued interest and other fees, to be immediately due and payable, or enforce their security interest, any of which would result in an event of default. The lenders will also have the right in these circumstances to terminate any commitments they have to provide further borrowings. We may need

### 10-Q（提交 2026-08-04，期末 2026-06-30）`E-LIVE-DOC-02`
来源：https://www.sec.gov/Archives/edgar/data/1474735/000143774926025669/gnrc20260630_10q.htm

- **remaining_performance_obligations** ×2：…ring the six months ended June 30, 2026, the Company recognized revenue of $90,360 related to amounts included in the December 31, 2025 contract liability balance. As of June 30, 2026, the aggregate amount of revenue that the Company expects to recognize on remaining performance obligations (excluding extended warranty) was approximately $143,000, of which approximately 80% is expected to be recognized as revenue ov
- **customer_deposits** ×8：…no market data, which require the reporting entity to develop its own assumptions. The Company believes the carrying amount of its financial instruments (cash and cash equivalents, accounts receivable, contract assets, accounts payable, accrued liabilities, contract liabilities, short-term borrowings, and revolving facility (Revolving Facility) borrowings), excluding Term Loan borrowings, approximates the fair value
- **sole_source** ×1：…g demand for our products; ● fluctuations in cost, availability, and quality of raw materials, key components and labor required to manufacture our products; ● our dependence on a small number of contract manufacturers and component suppliers, including single-source suppliers; ● changes and volatility with respect to the trade policies of various countries, which may result in new or increased tariffs, trade restri

## 4. 图谱位置与下一跳候选

- 未收录于卡点图谱：Not in atlas: map the chain manually (PB-HUNT-08) and consider adding a node.

## 5. Serenity 公开言论记忆（时点）

- 状态：available；公开帖转述（不是原话，不含订阅内容），帖子编号可在 x.com 查原文。立场 = 当时公开表达的看法，不是持仓记录；2026-10-19 之后是否有新表态未知（沉默不等于卖出）。Serenity 的说法是线索，不是公司事实。
  - 2026-09-08 `2097321349555306512` MENTION/neutral

## 6. 数据质量警告（写进 lens 的 live_data.warnings_addressed）


## 7. 下一步（快速路径）

1. 只在 brief 不够时再读一手文件：`python connectors/live_data.py filing-text --ticker X --latest 10-Q --preset contracts`（≤2 份）。
2. 填写 `lens-draft.json` 中所有 `TODO:` 字段（判断、情景、证伪条件、红队）。
3. `python scripts/serenity_lens.py finish lens-draft.json --md report.md --html report.html` 一步完成计算、校验、渲染与核验。

---

框架声明：本 skill 根据 Serenity 公开发布的内容提炼研究框架，用于回测与研究分析；报告由框架生成，不代表 Serenity 本人观点，亦非投资建议。
