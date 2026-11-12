# 研究包：TEM（Tempus AI, Inc.）

> 数据抓取 2026-11-06T04:28:37Z · 连接器 v9.1.0 · 用时 3.61 秒。以下是数据底稿与机械线索，不是结论；判断写进 lens-draft.json 后用 `serenity_lens.py finish` 收尾。

## 1. 对比表（USD 用即期汇率，仅作横向比较）

| 代码 | 价格 | 市值(USD) | 52周回撤 | 1年涨跌 | TTM收入(USD) | 收入同比 | 收入环比 | 毛利率(期末) | 毛利率同比 | P/S | 股本变化 | 机械旗标 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `TEM` | 70.43 USD | 12.83B | -20.9% | -1.9% | 1.51B | +23.1% | +7.6% | — | — | 8.5x | — | unregistered_equity_sale_8k_3_02, material_agreement_8k_1_01, beneficial_owner_filings, insider_form4_activity, going_concern_exhibit_only |

## 2. 主体要点

- 最新季度收入：411.54M USD（期末 2026-09-30）；营业利润率 -13.8%；现金+短投 590.48M；FCF 跑道 17.3 季。
- 计算市值：12.83B USD（70.43 × 182,225,851 股，股本截至 2026-09-30）。
- 文件雷达 `unregistered_equity_sale_8k_3_02`（PB-FIN-03）：Private placement/PIPE: who bought, price vs market, lockup, warrants.
- 文件雷达 `material_agreement_8k_1_01`（PB-SIG-02）：Open the 8-K exhibit: customer/supply/financing agreement? counterparty quality?
- 文件雷达 `beneficial_owner_filings`（PB-SIG-09）：New 13G/13D filers = institutional discovery or activist; read filer name and %.
- 文件雷达 `insider_form4_activity`（PB-SIG-10）：Classify open-market buys (code P) vs sales/grants; buys after a run-up are rarer signals.
- SEC 全文检索命中（近 25 个月）：supply_concentration 5（主文档 3/5）；customer_concentration 7（主文档 2/6）；atm_program 22（主文档 2/6）；capacity_signal 22（主文档 3/6）；going_concern 6（主文档 0/6）

## 2c. 本地财务与公司体检


### 公司体检（通用框架 · company-check-v2）

- 类型路由：**一般经营企业**（依据：SEC SIC 7370 (Services-Computer Programming, Data Processing, Etc.)）
- 数据：sec_companyfacts，报告期 2026-09-30，币种 USD；证据 E-LIVE-FIN
- 阶段：**常规经营期**（常规口径）；该阶段看：收入增速、利润率、现金转换、估值
- 结果：🚩 2 · 👀 3 · ✅ 5 · ℹ️ 4 · — 2

| 项目 | 数值 | 状态 | 公式 / 说明 |
|---|---|---|---|
| G1 收入同比 | 23.14% | ✅ | 最新报告期累计收入同比（A/H 聚合源）或最新季度同比（SEC/Yahoo） |
| G2 归母净利同比 | — | — | TTM 净利润 vs 一年前 TTM（SEC；上年为亏损时不计算） |
| P1 毛利率 | — | ℹ️ | 毛利 / 收入（最新期） |
| P2 净利率（TTM） | -12.54% | ℹ️ | TTM 净利润 / TTM 收入 |
| P3 ROE（TTM） | -37.83% | 🚩 | TTM 归母净利润 / 期末归母权益（未取平均） |
| C1 经营现金流 / 净利润（TTM） | 0.57x | ℹ️ | TTM 经营活动现金流净额 / TTM 净利润；长期 <0.7 说明利润没有变成现金 |
| C2 自由现金流（TTM） | -1.37亿 USD | 👀 | TTM 经营现金流 − TTM 资本开支 |
| C3 股权激励费用 / 收入（TTM） | 13.27% | 👀 | TTM 股权激励费用 / TTM 收入；高 SBC 是隐性稀释 |
| B1 资产负债率 | 79.59% | 👀 | 总负债 / 总资产 |
| B2 商誉 / 归母权益 | 97.55% | 🚩 | 期末商誉 / 期末归母权益；商誉大意味着减值风险 |
| W1 应收增速 − 收入增速 | 11.10pp | ✅ | 应收账款同比（2025-09-30→2026-09-30）− 收入同比 |
| W2 存货增速 − 收入增速 | -25.33pp | ℹ️ | 存货同比（2025-09-30→2026-09-30）− 收入同比；存货不足 TTM 收入的 5%，只作参考 |
| W3 合同负债/预收同比 | 1.43% | ✅ | 期末合同负债 / 去年同期 − 1；上升=客户预付增加（需求领先信号）；大降需追问 |
| D1 股本变化（约一年） | — | — | 最新股本 / 4 个观测点前 − 1；持续增发=稀释 |
| R1 现金跑道（月） | 51.80 月 | ✅ | 现金及短投 / (−TTM 自由现金流 / 12)；跑道短 = 近期必须融资；融资方式决定稀释好坏：ATM（持续、无上限，最差）< 溢价可转债 < 定增 < 客户预付/长约（最好） |
| V1 P/S（增速 < 40% 时） | 8.50x | ✅ | 市值 / TTM 收入，仅在收入增速 < 40% 时打分；好公司 ≠ 好价格：增速不够时高 P/S 需要更强的前瞻证据 |

**估值（USD 口径）**

- 市值 128.34亿 USD · P/B 25.6x · P/S 8.5x
- 股本口径：latest reported shares (market_current)
- 注：loss-making on a TTM basis: P/E not meaningful

**需核实清单（到定期报告/公告原文确认）**

- [ ] 瓶颈/主题业务占总收入的比例（分部披露；占比小=敞口被稀释）
- [ ] 近 12 个月融资：方式（ATM（持续、无上限，最差）< 溢价可转债 < 定增 < 客户预付/长约（最好））、规模/市值、用途、价格；未用完的 ATM/储架额度
- [ ] 前五大客户集中度与长约条款（期限、可取消比例、预付款）
- [ ] P3 ROE（TTM）：到定期报告原文核对口径与一次性因素
- [ ] B2 商誉 / 归母权益：到定期报告原文核对口径与一次性因素

> 机械体检：每项都附公式与阈值（RULES），状态只是“该去看什么”，不是买卖结论。

## 3. 一手文件关键词摘录

### 10-K（提交 2026-02-24，期末 2025-12-31）`E-LIVE-DOC-01`
来源：https://www.sec.gov/Archives/edgar/data/1717115/000119312526066961/tem-20251231.htm

- **remaining_performance_obligations** ×4：…0 days after the date of service. The Company has no significant obligations for refunds, warranties, or similar obligations for Data and applications product offerings. The Company has elected the practical expedient, which allows the Company to not disclose remaining performance obligations for contracts with original terms of twelve months or less. Cancelable contracted revenue is not considered a remaining perfo
- **sole_source** ×7：…Our systems, processes, and procedures are designed to scale, as evidenced by the fact that we have become one of the largest sequences of cancer patients in the United States in just a few years. We rely on a limited number of suppliers, or, in some cases, sole suppliers to provide our products and services. Illumina, Inc., is our primary supplier of sequencers and laboratory reagents; however, we purchase laborato
- **at_the_market** ×6：…oceeds from the Offering for general corporate purposes, which may include acquisitions or strategic investments in complementary businesses or technologies, working capital, operating expenses, capital expenditures and repayment of additional indebtedness. At the Market Sales Agreement On August 8, 2025, we entered into a Controlled Equity OfferingSM Sales Agreement, or the Sales Agreement, with Morgan Stanley & Co
- **default_covenant** ×5：…duct development, new enterprise relationships and other general corporate purposes; • requiring us to repay the principal and accrued interest on the Second Amended Note if we terminate our agreement with Google for use of Google Cloud or as a result of an event of default under the operating covenants in the Second Amended Note, or requiring us to repay the principal and accrued interest on the Additional Term Loa

### 10-Q（提交 2026-11-02，期末 2026-09-30）`E-LIVE-DOC-02`
来源：https://www.sec.gov/Archives/edgar/data/1717115/000119312526442624/tem-20260930.htm

- **remaining_performance_obligations** ×3：…0 days after the date of service. The Company has no significant obligations for refunds, warranties, or similar obligations for Data and applications product offerings. The Company has elected the practical expedient, which allows the Company to not disclose remaining performance obligations for contracts with original terms of twelve months or less. Cancelable contracted revenue is not considered a remaining perfo
- **at_the_market** ×6：…ses of capped call (31,234 ) (41,775 ) Proceeds from revolving credit facility, net of original issue discount — 98,000 Proceeds from long-term debt, net of original issue discount — 196,000 Proceeds from issuance of common stock in connection with at-the-market offering, net of commissions — 195,499 Payment of deferred financing fees (1,349 ) (1,255 ) Net cash provided by financing activities $ 96,135 $ 887,732 Eff
- **default_covenant** ×4：…fault either the 2032 Trustee or the holders of at least 25% in principal amount of the outstanding 2032 Notes may declare 100% of the principal of, and accrued and unpaid special interest, if any, on, all the 2032 Notes to be due and payable. If there is an event of default relating to failures by the Company to comply with certain reporting requirements, the Company may elect, at its option, that the sole remedy t

## 4. 图谱位置与下一跳候选

- 未收录于卡点图谱：Not in atlas: map the chain manually (PB-HUNT-08) and consider adding a node.

## 5. Serenity 公开言论记忆（时点）

- 状态：no_mentions；公开时间线里没有关于 TEM 本身的表态（覆盖至 2026-10-19）。另有 1 条只是和其他公司一起被列出，不算表态。没提到不代表看空。

## 6. 数据质量警告（写进 lens 的 live_data.warnings_addressed）


## 7. 下一步（快速路径）

1. 只在 brief 不够时再读一手文件：`python connectors/live_data.py filing-text --ticker X --latest 10-Q --preset contracts`（≤2 份）。
2. 填写 `lens-draft.json` 中所有 `TODO:` 字段（判断、情景、证伪条件、红队）。
3. `python scripts/serenity_lens.py finish lens-draft.json --md report.md --html report.html` 一步完成计算、校验、渲染与核验。

---

框架声明：本 skill 根据 Serenity 公开发布的内容提炼研究框架，用于回测与研究分析；报告由框架生成，不代表 Serenity 本人观点，亦非投资建议。
