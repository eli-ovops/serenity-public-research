# 研究包：PATH（UiPath, Inc.）

> 数据抓取 2026-11-06T04:39:40Z · 连接器 v9.1.0 · 用时 2.81 秒。以下是数据底稿与机械线索，不是结论；判断写进 lens-draft.json 后用 `serenity_lens.py finish` 收尾。

## 1. 对比表（USD 用即期汇率，仅作横向比较）

| 代码 | 价格 | 市值(USD) | 52周回撤 | 1年涨跌 | TTM收入(USD) | 收入同比 | 收入环比 | 毛利率(期末) | 毛利率同比 | P/S | 股本变化 | 机械旗标 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `PATH` | 13.01 USD | 6.78B | -34.4% | -8.4% | 1.72B | +13.4% | -1.9% | 80.4% (2026-07-31) | -1.8pp | 3.9x | — | beneficial_owner_filings, insider_form4_activity, customer_concentration, capacity_language |

## 2. 主体要点

- 最新季度收入：410.26M USD（期末 2026-07-31）；营业利润率 7.7%；现金+短投 1.28B；FCF 跑道 — 季。
- 计算市值：6.78B USD（13.01 × 520,989,706 股，股本截至 2026-07-31）。
- 文件雷达 `beneficial_owner_filings`（PB-SIG-09）：New 13G/13D filers = institutional discovery or activist; read filer name and %.
- 文件雷达 `insider_form4_activity`（PB-SIG-10）：Classify open-market buys (code P) vs sales/grants; buys after a run-up are rarer signals.
- SEC 全文检索命中（近 25 个月）：customer_concentration 4（主文档 3/4）；capacity_signal 8（主文档 6/6）

## 2c. 本地财务与公司体检


### 公司体检（通用框架 · company-check-v2）

- 类型路由：**一般经营企业**（依据：SEC SIC 7372 (Services-Prepackaged Software)）
- 数据：sec_companyfacts，报告期 2026-07-31，币种 USD；证据 E-LIVE-FIN
- 阶段：**常规经营期**（常规口径）；该阶段看：收入增速、利润率、现金转换、估值
- 结果：🚩 0 · 👀 1 · ✅ 11 · ℹ️ 2 · — 2

| 项目 | 数值 | 状态 | 公式 / 说明 |
|---|---|---|---|
| G1 收入同比 | 13.42% | ✅ | 最新报告期累计收入同比（A/H 聚合源）或最新季度同比（SEC/Yahoo） |
| G2 归母净利同比 | 1,694.50% | ✅ | TTM 净利润 vs 一年前 TTM（SEC；上年为亏损时不计算） |
| P1 毛利率 | 80.36% | ℹ️ | 毛利 / 收入（最新期） |
| P1d 毛利率同比变化 | -1.84pp | ✅ | 最新季度毛利率 − 去年同季 |
| P2 净利率（TTM） | 21.03% | ℹ️ | TTM 净利润 / TTM 收入 |
| P3 ROE（TTM） | 18.57% | ✅ | TTM 归母净利润 / 期末归母权益（未取平均） |
| C1 经营现金流 / 净利润（TTM） | 1.03x | ✅ | TTM 经营活动现金流净额 / TTM 净利润；长期 <0.7 说明利润没有变成现金 |
| C2 自由现金流（TTM） | 3.63亿 USD | ✅ | TTM 经营现金流 − TTM 资本开支 |
| C3 股权激励费用 / 收入（TTM） | 13.63% | 👀 | TTM 股权激励费用 / TTM 收入；高 SBC 是隐性稀释 |
| B1 资产负债率 | 32.98% | ✅ | 总负债 / 总资产 |
| B2 商誉 / 归母权益 | 9.21% | ✅ | 期末商誉 / 期末归母权益；商誉大意味着减值风险 |
| W1 应收增速 − 收入增速 | 0.41pp | ✅ | 应收账款同比（2025-07-31→2026-07-31）− 收入同比 |
| W2 存货增速 − 收入增速 | — | — | 存货同比（2025-07-31→2026-07-31）− 收入同比；存货不足 TTM 收入的 5%，只作参考 |
| W3 合同负债/预收同比 | 7.24% | ✅ | 期末合同负债 / 去年同期 − 1；上升=客户预付增加（需求领先信号）；大降需追问 |
| D1 股本变化（约一年） | — | — | 最新股本 / 4 个观测点前 − 1；持续增发=稀释 |
| V1 P/S（增速 < 40% 时） | 3.94x | ✅ | 市值 / TTM 收入，仅在收入增速 < 40% 时打分；好公司 ≠ 好价格：增速不够时高 P/S 需要更强的前瞻证据 |

**估值（USD 口径）**

- 市值 67.78亿 USD · P/E(TTM) 18.7x · P/B 3.5x · P/S 3.9x · P/FCF 18.7x · 回购收益率 3.96%
- 股本口径：latest reported shares (market_current)

**需核实清单（到定期报告/公告原文确认）**

- [ ] 瓶颈/主题业务占总收入的比例（分部披露；占比小=敞口被稀释）
- [ ] 近 12 个月融资：方式（ATM（持续、无上限，最差）< 溢价可转债 < 定增 < 客户预付/长约（最好））、规模/市值、用途、价格；未用完的 ATM/储架额度
- [ ] 前五大客户集中度与长约条款（期限、可取消比例、预付款）

> 机械体检：每项都附公式与阈值（RULES），状态只是“该去看什么”，不是买卖结论。

## 3. 一手文件关键词摘录

### 10-K（提交 2026-03-25，期末 2026-01-31）`E-LIVE-DOC-01`
来源：https://www.sec.gov/Archives/edgar/data/1734722/000173472226000012/path-20260131.htm

- **remaining_performance_obligations** ×4：…nning of the period (954,541) (855,330) Translation adjustments 4,535 (10,872) Ending balance $ 707,305 $ 705,307 Deferred revenue, current 603,737 569,464 Deferred revenue, non-current 103,568 135,843 Total deferred revenue $ 707,305 $ 705,307 Remaining Performance Obligations Our remaining performance obligations are comprised of licenses, subscription services, and professional services not yet delivered. As of J
- **customer_deposits** ×5：…Business Acquisitions Assets acquired and liabilities assumed in a business combination are recorded at their respective fair values at the date of the acquisition in accordance with ASC 805, Business Combinations (with the exception of contract assets and contract liabilities, which are measured according to ASC 606, Revenue from Contracts with Customers, discussed under the heading "Revenue Recognition," below). D
- **capacity_reservation** ×1：…udes introducing new functionalities and adapting and growing our inside sales team and enterprise sales force. These efforts are aimed at driving new customer adoption and expanding use cases and integrations. We have entered into non-cancellable multi-year capacity commitments with certain third-party cloud providers for cloud infrastructure services. These commitments require us to pay for such capacity irrespect
- **customer_concentration** ×5：…e and ARR from sales to our top 10% of customers. As a result, our revenue and ARR could fluctuate materially and could be materially and disproportionately impacted by the purchasing decisions of these customers or any other future large customer. Any of our largest customers may decide to purchase less than they have in the past, may alter their purchasing patterns at any time with limited notice, or may decide no
- **export_controls** ×3：…ng on software solutions or their spending levels generally; perceived security or data privacy risks from the use of our products; changes in regulatory regimes that affect our customers or our ability to sell our products, including changes to sanctions and export control regimes; or changes in the views of the industry and public with regard to our products and automation products generally, including as a result

### 10-Q（提交 2026-09-08，期末 2026-07-31）`E-LIVE-DOC-02`
来源：https://www.sec.gov/Archives/edgar/data/1734722/000173472226000050/path-20260731.htm

- **remaining_performance_obligations** ×4：…1, 2026 and 2025, respectively. Deferred Revenue During the six months ended July 31, 2026 and 2025, we recognized $369.2 million and $362.6 million of revenue that was included in the deferred revenue balance as of January 31, 2026 and 2025, respectively. Remaining Performance Obligations Our remaining performance obligations are comprised of licenses, subscription services, and professional services not yet delive
- **customer_concentration** ×3：…ying other credit risk monitoring procedures. Significant customers are those that represent 10% or more of our total revenue for the period or accounts receivable at the balance sheet date. For the three and six months ended July 31, 2026 and 2025, no single customer accounted for 10% or more of our total revenue. As of July 31, 2026, one customer accounted for approximately 15% of our accounts receivable. As of Ja

## 4. 图谱位置与下一跳候选

- 未收录于卡点图谱：Not in atlas: map the chain manually (PB-HUNT-08) and consider adding a node.

## 5. Serenity 公开言论记忆（时点）

- 状态：no_mentions；公开时间线里没有关于 PATH 本身的表态（覆盖至 2026-10-19）。没提到不代表看空。

## 6. 数据质量警告（写进 lens 的 live_data.warnings_addressed）


## 7. 下一步（快速路径）

1. 只在 brief 不够时再读一手文件：`python connectors/live_data.py filing-text --ticker X --latest 10-Q --preset contracts`（≤2 份）。
2. 填写 `lens-draft.json` 中所有 `TODO:` 字段（判断、情景、证伪条件、红队）。
3. `python scripts/serenity_lens.py finish lens-draft.json --md report.md --html report.html` 一步完成计算、校验、渲染与核验。

---

框架声明：本 skill 根据 Serenity 公开发布的内容提炼研究框架，用于回测与研究分析；报告由框架生成，不代表 Serenity 本人观点，亦非投资建议。
