# 研究包：CGNX（Cognex Corporation）

> 数据抓取 2026-11-06T04:34:29Z · 连接器 v9.1.0 · 用时 3.24 秒。以下是数据底稿与机械线索，不是结论；判断写进 lens-draft.json 后用 `serenity_lens.py finish` 收尾。

## 1. 对比表（USD 用即期汇率，仅作横向比较）

| 代码 | 价格 | 市值(USD) | 52周回撤 | 1年涨跌 | TTM收入(USD) | 收入同比 | 收入环比 | 毛利率(期末) | 毛利率同比 | P/S | 股本变化 | 机械旗标 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `CGNX` | 47.495 USD | 8.00B | -34.8% | +23.1% | 1.13B | +13.2% | +7.6% | 70.8% (2026-10-04) | +3.1pp | 7.1x | +0.5% | beneficial_owner_filings, insider_form4_activity, capacity_language |

## 2. 主体要点

- 最新季度收入：313.39M USD（期末 2026-10-04）；营业利润率 32.2%；现金+短投 695.69M；FCF 跑道 — 季。
- 计算市值：8.00B USD（47.495 × 168,378,060 股，股本截至 2026-11-01）。
- 文件雷达 `beneficial_owner_filings`（PB-SIG-09）：New 13G/13D filers = institutional discovery or activist; read filer name and %.
- 文件雷达 `insider_form4_activity`（PB-SIG-10）：Classify open-market buys (code P) vs sales/grants; buys after a run-up are rarer signals.
- SEC 全文检索命中（近 25 个月）：capacity_signal 9（主文档 2/6）

## 2c. 本地财务与公司体检


### 公司体检（通用框架 · company-check-v2）

- 类型路由：**一般经营企业**（依据：SEC SIC 3823 (Industrial Instruments For Measurement, Display, and Control)）
- 数据：sec_companyfacts，报告期 2026-10-04，币种 USD；证据 E-LIVE-FIN
- 阶段：**常规经营期**（常规口径）；该阶段看：收入增速、利润率、现金转换、估值
- 结果：🚩 0 · 👀 1 · ✅ 13 · ℹ️ 2 · — 0

| 项目 | 数值 | 状态 | 公式 / 说明 |
|---|---|---|---|
| G1 收入同比 | 13.18% | ✅ | 最新报告期累计收入同比（A/H 聚合源）或最新季度同比（SEC/Yahoo） |
| G2 归母净利同比 | 119.70% | ✅ | TTM 净利润 vs 一年前 TTM（SEC；上年为亏损时不计算） |
| P1 毛利率 | 70.76% | ℹ️ | 毛利 / 收入（最新期） |
| P1d 毛利率同比变化 | 3.12pp | ✅ | 最新季度毛利率 − 去年同季 |
| P2 净利率（TTM） | 21.50% | ℹ️ | TTM 净利润 / TTM 收入 |
| P3 ROE（TTM） | 14.05% | ✅ | TTM 归母净利润 / 期末归母权益（未取平均） |
| C1 经营现金流 / 净利润（TTM） | 1.22x | ✅ | TTM 经营活动现金流净额 / TTM 净利润；长期 <0.7 说明利润没有变成现金 |
| C2 自由现金流（TTM） | 2.86亿 USD | ✅ | TTM 经营现金流 − TTM 资本开支 |
| C3 股权激励费用 / 收入（TTM） | 4.28% | ✅ | TTM 股权激励费用 / TTM 收入；高 SBC 是隐性稀释 |
| B1 资产负债率 | 24.38% | ✅ | 总负债 / 总资产 |
| B2 商誉 / 归母权益 | 22.43% | ✅ | 期末商誉 / 期末归母权益；商誉大意味着减值风险 |
| W1 应收增速 − 收入增速 | 26.99pp | 👀 | 应收账款同比（2025-09-28→2026-10-04）− 收入同比 |
| W2 存货增速 − 收入增速 | -2.90pp | ✅ | 存货同比（2025-09-28→2026-10-04）− 收入同比 |
| W3 合同负债/预收同比 | 78.61% | ✅ | 期末合同负债 / 去年同期 − 1；上升=客户预付增加（需求领先信号）；大降需追问 |
| D1 股本变化（约一年） | 0.47% | ✅ | 最新股本 / 4 个观测点前 − 1；持续增发=稀释 |
| V1 P/S（增速 < 40% 时） | 7.11x | ✅ | 市值 / TTM 收入，仅在收入增速 < 40% 时打分；好公司 ≠ 好价格：增速不够时高 P/S 需要更强的前瞻证据 |

**估值（USD 口径）**

- 市值 79.97亿 USD · P/E(TTM) 33.0x · P/B 4.7x · P/S 7.1x · P/FCF 28.0x · 股息率 0.71% · 回购收益率 1.63%
- 股本口径：latest reported shares (market_current)

**需核实清单（到定期报告/公告原文确认）**

- [ ] 瓶颈/主题业务占总收入的比例（分部披露；占比小=敞口被稀释）
- [ ] 近 12 个月融资：方式（ATM（持续、无上限，最差）< 溢价可转债 < 定增 < 客户预付/长约（最好））、规模/市值、用途、价格；未用完的 ATM/储架额度
- [ ] 前五大客户集中度与长约条款（期限、可取消比例、预付款）

> 机械体检：每项都附公式与阈值（RULES），状态只是“该去看什么”，不是买卖结论。

## 3. 一手文件关键词摘录

### 10-K（提交 2026-02-12，期末 2025-12-31）`E-LIVE-DOC-01`
来源：https://www.sec.gov/Archives/edgar/data/851205/000085120526000012/cgnx-20251231.htm

- **customer_deposits** ×8：…Other assets 4,994 5,027 Total assets $ 2,016,555 $ 1,992,850 LIABILITIES AND SHAREHOLDERS’ EQUITY Current liabilities: Accounts payable $ 50,203 $ 38,046 Accrued expenses 91,397 71,760 Accrued income taxes 9,141 25,685 Deferred revenue and customer deposits 21,094 25,035 Operating lease liabilities 11,716 8,854 Total current liabilities 183,551 169,380 Non-current operating lease liabilities 64,870 61,363 Deferred 
- **prepayment** ×1：…is recognized when control of the license is transferred to the partner, and amounts recognized in advance of billing are recorded as unbilled revenue. Credit assessments are performed to determine payment terms, which vary by region, industry, and customer. Prepayment terms result in contract liabilities for customer deposits. When credit is granted to customers, payment is typically due 30 to 90 days from billing.
- **customer_concentration** ×1：…2 Year Ended December 31, 2023 Revenue $ 288,324 $ 220,665 $ 164,115 $ 164,443 $ 837,547 Long-lived assets 62,946 17,005 17,028 15,958 $ 112,937 Revenue is presented geographically based on the customer’s country of domicile. Revenue from a single customer accounted for 15% and 10% of total revenue in 2025 and 2024, respectively. Revenue from this customer was not greater than 10% of total revenue in 2023. Accounts 
- **export_controls** ×1：…n recent years, trade tariffs imposed by the United States on certain components imported from Chinese suppliers resulted in higher costs for our products, which, to date, have not been material to our total cost of revenue. In addition to trade tariffs, U.S. export controls that place restrictions on the exportation of our products or a subset of our products, including applicable regulations promulgated by the U.S

### 10-Q（提交 2026-11-05，期末 2026-10-04）`E-LIVE-DOC-02`
来源：https://www.sec.gov/Archives/edgar/data/851205/000085120526000082/cgnx-20261004.htm

- **customer_deposits** ×6：…2 Other assets 4,551 4,994 Total assets 2,276,467 2,016,555 LIABILITIES AND SHAREHOLDERS’ EQUITY Current liabilities: Accounts payable $ 74,708 $ 50,203 Accrued expenses 88,618 91,397 Accrued income taxes 10,627 9,141 Deferred revenue and customer deposits 42,450 21,094 Operating lease liabilities 12,314 11,716 Total current liabilities 228,717 183,551 Non-current operating lease liabilities 58,048 64,870 Deferred i

## 4. 图谱位置与下一跳候选

- 未收录于卡点图谱：Not in atlas: map the chain manually (PB-HUNT-08) and consider adding a node.

## 5. Serenity 公开言论记忆（时点）

- 状态：no_mentions；公开时间线里没有关于 CGNX 本身的表态（覆盖至 2026-10-19）。没提到不代表看空。

## 6. 数据质量警告（写进 lens 的 live_data.warnings_addressed）


## 7. 下一步（快速路径）

1. 只在 brief 不够时再读一手文件：`python connectors/live_data.py filing-text --ticker X --latest 10-Q --preset contracts`（≤2 份）。
2. 填写 `lens-draft.json` 中所有 `TODO:` 字段（判断、情景、证伪条件、红队）。
3. `python scripts/serenity_lens.py finish lens-draft.json --md report.md --html report.html` 一步完成计算、校验、渲染与核验。

---

框架声明：本 skill 根据 Serenity 公开发布的内容提炼研究框架，用于回测与研究分析；报告由框架生成，不代表 Serenity 本人观点，亦非投资建议。
