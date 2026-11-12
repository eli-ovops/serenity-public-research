# 研究包：ACMR（ACM Research, Inc.）

> 数据抓取 2026-10-28T13:41:34Z · 连接器 v9.1.0 · 用时 2.81 秒。以下是数据底稿与机械线索，不是结论；判断写进 lens-draft.json 后用 `serenity_lens.py finish` 收尾。

## 1. 对比表（USD 用即期汇率，仅作横向比较）

| 代码 | 价格 | 市值(USD) | 52周回撤 | 1年涨跌 | TTM收入(USD) | 收入同比 | 收入环比 | 毛利率(期末) | 毛利率同比 | P/S | 股本变化 | 机械旗标 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `ACMR` | 53.72 USD | 761.57M | -57.8% | +29.6% | 1.04B | +36.0% | +26.7% | 46.0% (2026-06-30) | -2.5pp | 0.7x | — | material_agreement_8k_1_01, beneficial_owner_filings, insider_form4_activity, customer_concentration, supply_concentration |

## 2. 主体要点

- 最新季度收入：292.92M USD（期末 2026-06-30）；营业利润率 17.0%；现金+短投 1.07B；FCF 跑道 36.2 季。
- 计算市值：761.57M USD（53.72 × 14,176,690 股，股本截至 2019-03-08）。
- 文件雷达 `material_agreement_8k_1_01`（PB-SIG-02）：Open the 8-K exhibit: customer/supply/financing agreement? counterparty quality?
- 文件雷达 `beneficial_owner_filings`（PB-SIG-09）：New 13G/13D filers = institutional discovery or activist; read filer name and %.
- 文件雷达 `insider_form4_activity`（PB-SIG-10）：Classify open-market buys (code P) vs sales/grants; buys after a run-up are rarer signals.
- SEC 全文检索命中（近 25 个月）：supply_concentration 2（主文档 2/2）；customer_concentration 5（主文档 5/5）；capacity_signal 9（主文档 3/6）

## 2c. 本地财务与公司体检


### 公司体检（通用框架 · company-check-v2）

- 类型路由：**一般经营企业**（依据：SEC SIC 3559 (Special Industry Machinery, NEC)）
- 数据：sec_companyfacts，报告期 2026-06-30，币种 USD；证据 E-LIVE-FIN
- 阶段：**常规经营期**（常规口径）；该阶段看：收入增速、利润率、现金转换、估值
- 结果：🚩 1 · 👀 2 · ✅ 10 · ℹ️ 3 · — 2

| 项目 | 数值 | 状态 | 公式 / 说明 |
|---|---|---|---|
| G1 收入同比 | 36.01% | ✅ | 最新报告期累计收入同比（A/H 聚合源）或最新季度同比（SEC/Yahoo） |
| G2 归母净利同比 | 33.98% | ✅ | TTM 净利润 vs 一年前 TTM（SEC；上年为亏损时不计算） |
| P1 毛利率 | 45.96% | ℹ️ | 毛利 / 收入（最新期） |
| P1d 毛利率同比变化 | -2.54pp | ✅ | 最新季度毛利率 − 去年同季 |
| P2 净利率（TTM） | 14.48% | ℹ️ | TTM 净利润 / TTM 收入 |
| P3 ROE（TTM） | 8.08% | ✅ | TTM 归母净利润 / 期末归母权益（未取平均） |
| C1 经营现金流 / 净利润（TTM） | -0.04x | 🚩 | TTM 经营活动现金流净额 / TTM 净利润；长期 <0.7 说明利润没有变成现金 |
| C2 自由现金流（TTM） | -1.19亿 USD | 👀 | TTM 经营现金流 − TTM 资本开支 |
| C3 股权激励费用 / 收入（TTM） | 2.52% | ✅ | TTM 股权激励费用 / TTM 收入；高 SBC 是隐性稀释 |
| B1 资产负债率 | 29.25% | ✅ | 总负债 / 总资产 |
| B2 商誉 / 归母权益 | — | — | 期末商誉 / 期末归母权益；商誉大意味着减值风险 |
| B3 净现金（现金 − 有息负债） | 8.41亿 USD | ℹ️ | 现金及等价物(+短期存款/短投) − 短借 − 长借 − 应付债券 |
| W1 应收增速 − 收入增速 | -11.86pp | ✅ | 应收账款同比（2025-06-30→2026-06-30）− 收入同比 |
| W2 存货增速 − 收入增速 | -15.21pp | ✅ | 存货同比（2025-06-30→2026-06-30）− 收入同比 |
| W3 合同负债/预收同比 | -25.23% | 👀 | 期末合同负债 / 去年同期 − 1；上升=客户预付增加（需求领先信号）；大降需追问 |
| D1 股本变化（约一年） | — | — | 最新股本 / 4 个观测点前 − 1；持续增发=稀释 |
| R1 现金跑道（月） | 108.60 月 | ✅ | 现金及短投 / (−TTM 自由现金流 / 12)；跑道短 = 近期必须融资；融资方式决定稀释好坏：ATM（持续、无上限，最差）< 溢价可转债 < 定增 < 客户预付/长约（最好） |
| V1 P/S（增速 < 40% 时） | 0.73x | ✅ | 市值 / TTM 收入，仅在收入增速 < 40% 时打分；好公司 ≠ 好价格：增速不够时高 P/S 需要更强的前瞻证据 |

**估值（USD 口径）**

- 市值 7.62亿 USD · P/E(TTM) 5.1x · P/B 0.4x · P/S 0.7x
- 股本口径：latest reported shares (market_current)

**需核实清单（到定期报告/公告原文确认）**

- [ ] 瓶颈/主题业务占总收入的比例（分部披露；占比小=敞口被稀释）
- [ ] 近 12 个月融资：方式（ATM（持续、无上限，最差）< 溢价可转债 < 定增 < 客户预付/长约（最好））、规模/市值、用途、价格；未用完的 ATM/储架额度
- [ ] 前五大客户集中度与长约条款（期限、可取消比例、预付款）
- [ ] C1 经营现金流 / 净利润（TTM）：到定期报告原文核对口径与一次性因素

> 机械体检：每项都附公式与阈值（RULES），状态只是“该去看什么”，不是买卖结论。

## 3. 一手文件关键词摘录

### 10-K（提交 2026-03-02，期末 2025-12-31）`E-LIVE-DOC-01`
来源：https://www.sec.gov/Archives/edgar/data/1680062/000162828026013231/acmr-20251231.htm

- **customer_deposits** ×14：…nges in operating asset and liability accounts during the year-ended December 31, 2025 included the following uses of cash: an increase in inventories of $108.2 million (note 5), an increase in accounts receivable of $116.1 million (note 4), and a decrease in customer advances of $60.8 million (note 3). As described under “—Key Components of Results of Operations—Mainland China Government Research and Development Fu
- **long_term_supply_agreement** ×3：…ier, regardless of product performance or features. If we are not able to compete successfully against existing or new competitors, our business, operating results and financial condition will be negatively affected. Our customers do not generally enter into long-term purchase commitments, and they may decrease, cancel or delay their projected purchases at any time. In accordance with industry practice, our sales ar
- **sole_source** ×4：…ilt to order at our Lingang development and production center. See “Item 2. Properties,” of Part I of this report. We purchase some of the components and assemblies that we subsequently integrate into our products from a range of suppliers, some of which are single-source suppliers, and/or U.S. based suppliers which can no longer supply ACM Shanghai, ACM Korea and related entities as a result of recently enacted reg
- **customer_concentration** ×8：…rse effect on our revenue and operating results. There are also a limited number of potential customers for our products. The chip manufacturing industry is highly concentrated, and we derive most of our revenue from a limited number of customers. A total of four customers accounted for 52.2% of our revenue in 2025, four customers accounted for 52.2% of our revenue in 2024, and three customers accounted for 45.5% of
- **export_controls** ×46：…subsidiary of ACM Shanghai, which is located in the Republic of Korea, and other related entities. In general terms, the new BIS Entity List designations prohibit any party worldwide from furnishing hardware, software, or technologies that are subject to U.S. export controls jurisdiction directly or indirectly to ACM Shanghai or ACM Korea without obtaining authorization. See “Item 1A. Risk Factors—Regulatory Risks—O

### 10-Q（提交 2026-08-07，期末 2026-06-30）`E-LIVE-DOC-02`
来源：https://www.sec.gov/Archives/edgar/data/1680062/000162828026054832/acmr-20260630.htm

- **customer_deposits** ×8：…lities and Equity Current liabilities: Short-term borrowings (note 7) $ 107,218 $ 74,041 Current portion of long-term borrowings (note 9) 40,787 35,082 Related parties accounts payable (note 12) 29,799 32,060 Accounts payable 220,601 215,440 Advances from customers (note 3) 165,566 187,809 Deferred revenue (note 3) 15,908 17,388 Income taxes payable (note 15) 3,626 991 FIN-48 payable (note 15) 28,908 27,719 Other pa
- **customer_concentration** ×7：…counts receivable. 15 Table of Contents ACM RESEARCH, INC. Notes to the Condensed Consolidated Financial Statements (In thousands, except share, percentage and per share data) •Revenue concentration. For the three months ended June 30, 2026 and 2025, three customers accounted for 43.5% and four customers accounted for 66.5% of revenue, respectively. For the six months ended June 30, 2026 and 2025, one customer accou
- **export_controls** ×1：…subsidiary of ACM Shanghai, which is located in the Republic of Korea, and other related entities. In general terms, the new BIS Entity List designations prohibit any party worldwide from furnishing hardware, software, or technologies that are subject to U.S. export controls jurisdiction, directly or indirectly to ACM Shanghai or ACM Korea without obtaining authorization. See “Item 1A. Risk Factors—Regulatory Risks—

## 4. 图谱位置与下一跳候选

- 未收录于卡点图谱：Not in atlas: map the chain manually (PB-HUNT-08) and consider adding a node.

## 5. Serenity 公开言论记忆（时点）

- 状态：available；公开帖转述（不是原话，不含订阅内容），帖子编号可在 x.com 查原文。立场 = 当时公开表达的看法，不是持仓记录；2026-10-19 之后是否有新表态未知（沉默不等于卖出）。Serenity 的说法是线索，不是公司事实。
  - 2026-06-18 `2067412467404398942` REAFFIRM/bullish

## 6. 数据质量警告（写进 lens 的 live_data.warnings_addressed）

- `ACMR`：share_count_older_than_200_days
- `ACMR`：sec_stale_series_dropped:buybacks:last_end_2020-12-31_vs_newest_2026-06-30

## 7. 下一步（快速路径）

1. 只在 brief 不够时再读一手文件：`python connectors/live_data.py filing-text --ticker X --latest 10-Q --preset contracts`（≤2 份）。
2. 填写 `lens-draft.json` 中所有 `TODO:` 字段（判断、情景、证伪条件、红队）。
3. `python scripts/serenity_lens.py finish lens-draft.json --md report.md --html report.html` 一步完成计算、校验、渲染与核验。

---

框架声明：本 skill 根据 Serenity 公开发布的内容提炼研究框架，用于回测与研究分析；报告由框架生成，不代表 Serenity 本人观点，亦非投资建议。
