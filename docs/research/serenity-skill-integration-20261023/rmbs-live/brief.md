# 研究包：RMBS（Rambus Inc.）

> 数据抓取 2026-10-23T01:47:51Z · 连接器 v9.1.0 · 用时 46.74 秒。以下是数据底稿与机械线索，不是结论；判断写进 lens-draft.json 后用 `serenity_lens.py finish` 收尾。

## 1. 对比表（USD 用即期汇率，仅作横向比较）

| 代码 | 价格 | 市值(USD) | 52周回撤 | 1年涨跌 | TTM收入(USD) | 收入同比 | 收入环比 | 毛利率(期末) | 毛利率同比 | P/S | 股本变化 | 机械旗标 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `RMBS` | 85.73 USD | 9.27B | -50.8% | -24.5% | 756.33M | +20.4% | +15.1% | 79.8% (2026-06-30) | -0.1pp | 12.3x | +0.7% | material_agreement_8k_1_01, beneficial_owner_filings, insider_form4_activity, supply_concentration, capacity_language |

## 2. 主体要点

- 最新季度收入：207.38M USD（期末 2026-06-30）；营业利润率 34.3%；现金+短投 786.14M；FCF 跑道 — 季。
- 计算市值：9.27B USD（85.73 × 108,136,967 股，股本截至 2026-03-31）。
- 文件雷达 `material_agreement_8k_1_01`（PB-SIG-02）：Open the 8-K exhibit: customer/supply/financing agreement? counterparty quality?
- 文件雷达 `beneficial_owner_filings`（PB-SIG-09）：New 13G/13D filers = institutional discovery or activist; read filer name and %.
- 文件雷达 `insider_form4_activity`（PB-SIG-10）：Classify open-market buys (code P) vs sales/grants; buys after a run-up are rarer signals.
- SEC 全文检索命中（近 25 个月）：supply_concentration 10（主文档 6/6）；capacity_signal 13（主文档 3/6）

## 2c. 本地财务与公司体检


### 公司体检（通用框架 · company-check-v2）

- 类型路由：**一般经营企业**（依据：SEC SIC 3674 (Semiconductors & Related Devices)）
- 数据：sec_companyfacts，报告期 2026-06-30，币种 USD；证据 E-LIVE-FIN
- 阶段：**常规经营期**（常规口径）；该阶段看：收入增速、利润率、现金转换、估值
- 结果：🚩 0 · 👀 0 · ✅ 14 · ℹ️ 2 · — 0

| 项目 | 数值 | 状态 | 公式 / 说明 |
|---|---|---|---|
| G1 收入同比 | 20.43% | ✅ | 最新报告期累计收入同比（A/H 聚合源）或最新季度同比（SEC/Yahoo） |
| G2 归母净利同比 | 10.99% | ✅ | TTM 净利润 vs 一年前 TTM（SEC；上年为亏损时不计算） |
| P1 毛利率 | 79.76% | ℹ️ | 毛利 / 收入（最新期） |
| P1d 毛利率同比变化 | -0.05pp | ✅ | 最新季度毛利率 − 去年同季 |
| P2 净利率（TTM） | 30.41% | ℹ️ | TTM 净利润 / TTM 收入 |
| P3 ROE（TTM） | 16.51% | ✅ | TTM 归母净利润 / 期末归母权益（未取平均） |
| C1 经营现金流 / 净利润（TTM） | 1.59x | ✅ | TTM 经营活动现金流净额 / TTM 净利润；长期 <0.7 说明利润没有变成现金 |
| C2 自由现金流（TTM） | 3.35亿 USD | ✅ | TTM 经营现金流 − TTM 资本开支 |
| C3 股权激励费用 / 收入（TTM） | 7.18% | ✅ | TTM 股权激励费用 / TTM 收入；高 SBC 是隐性稀释 |
| B1 资产负债率 | 9.13% | ✅ | 总负债 / 总资产 |
| B2 商誉 / 归母权益 | 20.59% | ✅ | 期末商誉 / 期末归母权益；商誉大意味着减值风险 |
| W1 应收增速 − 收入增速 | -28.69pp | ✅ | 应收账款同比（2025-03-31→2026-03-31）− 收入同比 |
| W2 存货增速 − 收入增速 | 10.27pp | ✅ | 存货同比（2025-03-31→2026-03-31）− 收入同比 |
| W3 合同负债/预收同比 | 16.64% | ✅ | 期末合同负债 / 去年同期 − 1；上升=客户预付增加（需求领先信号）；大降需追问 |
| D1 股本变化（约一年） | 0.68% | ✅ | 最新股本 / 4 个观测点前 − 1；持续增发=稀释 |
| V1 P/S（增速 < 40% 时） | 12.26x | ✅ | 市值 / TTM 收入，仅在收入增速 < 40% 时打分；好公司 ≠ 好价格：增速不够时高 P/S 需要更强的前瞻证据 |

**估值（USD 口径）**

- 市值 92.71亿 USD · P/E(TTM) 40.3x · P/B 6.7x · P/S 12.3x · P/FCF 27.7x · 回购收益率 0.08%
- 股本口径：latest reported shares (market_current)

**需核实清单（到定期报告/公告原文确认）**

- [ ] 瓶颈/主题业务占总收入的比例（分部披露；占比小=敞口被稀释）
- [ ] 近 12 个月融资：方式（ATM（持续、无上限，最差）< 溢价可转债 < 定增 < 客户预付/长约（最好））、规模/市值、用途、价格；未用完的 ATM/储架额度
- [ ] 前五大客户集中度与长约条款（期限、可取消比例、预付款）

> 机械体检：每项都附公式与阈值（RULES），状态只是“该去看什么”，不是买卖结论。

## 3. 一手文件关键词摘录

### 10-K（提交 2026-02-18，期末 2025-12-31）`E-LIVE-DOC-01`
来源：https://www.sec.gov/Archives/edgar/data/917273/000119312526057101/rmbs-20251231.htm

- **remaining_performance_obligations** ×2：…1,601 21,852 During the years ended December 31, 2025 and December 31, 2024, the Company recognized $19.7 million and $17.5 million, respectively, of revenue that was included in deferred revenue as of December 31, 2024 and December 31, 2023, respectively. Remaining Performance Obligations Revenue allocated to remaining performance obligations represents the transaction price allocated to the performance obligations
- **customer_deposits** ×1：…ceives the final related reports from its customers. Contract Balances Timing of revenue recognition may differ from the timing of invoicing to the Company’s customers. The Company records contract assets when revenue is recognized prior to invoicing, and a contract liability when revenue is recognized subsequent to invoicing. The contract assets are transferred to receivables when the billing occurs. Cost of Revenu
- **long_term_supply_agreement** ×1：…entory by product generation, which may negatively impact revenue and inventory reserves. Our business is dependent on distributors to service our end customers. We utilize distributors to sell our memory interface chips to certain customers. We do not have long-term purchase commitments from our distributors. If a key distributor were to experience financial difficulties, including bankruptcy, this could materially
- **sole_source** ×1：…ely affect our business. We rely on third parties for a variety of services, including our manufacturing supply chain partners and third parties within our sales and distribution channels. Some of these third parties are, and may be, our sole manufacturer or sole source of certain 20 Table of Contents production materials and may be located in regions subject to geopolitical uncertainty (e.g., tensions between China
- **export_controls** ×7：…s and financial condition. • We are subject to various government restrictions and regulations, including on the sale of products and services that use encryption and other technology, those related to privacy, other consumer protection matters, other import/export controls and national security matters. • Litigation and government proceedings could affect our business in materially negative ways. • If we are unable

### 10-Q（提交 2026-07-28，期末 2026-06-30）`E-LIVE-DOC-02`
来源：https://www.sec.gov/Archives/edgar/data/917273/000119312526321000/rmbs-20260630.htm

- **remaining_performance_obligations** ×2：…y recognized $21.9 million of revenue that was included in deferred revenue as of December 31, 2025. During the six months ended June 30, 2025, the Company recognized $14.7 million of revenue that was included in deferred revenue as of December 31, 2024. 12 Remaining Performance Obligations Revenue allocated to remaining performance obligations represents the transaction price allocated to the performance obligation
- **long_term_supply_agreement** ×1：…entory by product generation, which may negatively impact revenue and inventory reserves. Our business is dependent on distributors to service our end customers. We utilize distributors to sell our memory interface chips to certain customers. We do not have long-term purchase commitments from our distributors. If a key distributor were to experience financial difficulties, including bankruptcy, this could materially
- **sole_source** ×1：…ely affect our business. We rely on third parties for a variety of services, including our manufacturing supply chain partners and third parties within our sales and distribution channels. Some of these third parties are, and may be, our sole manufacturer or sole source of certain production materials and may be located in regions subject to increased geopolitical uncertainty and changes in global trade policies (e.
- **export_controls** ×7：…condition and cash flows. • We are subject to various government restrictions and regulations, including on the sale of products and services that use encryption and other technology, those related to privacy, other consumer protection matters, other import/export controls and national security matters. • Litigation and government proceedings could affect our business in materially negative ways. • If we are unable 

## 4. 图谱位置与下一跳候选

- 链 `memory` / 节点 `mem_equipment`（存储工序设备与 IP，状态 filling，类型 demand）；同层：VECO, ONTO
  - 图谱状态最后核验：2026-10-19（4 天前；超过 180 天需重新核验）。图谱状态只是线索，用本次实时数据主动质疑它。

## 5. Serenity 公开言论记忆（时点）

- 状态：available；公开帖转述（不是原话，不含订阅内容），帖子编号可在 x.com 查原文。立场 = 当时公开表达的看法，不是持仓记录；2026-10-19 之后是否有新表态未知（沉默不等于卖出）。Serenity 的说法是线索，不是公司事实。
  - 2026-01-22 `2014354847202681059` WATCH/neutral
  - 2026-02-16 `2023314364757934115` REAFFIRM/bullish

## 6. 数据质量警告（写进 lens 的 live_data.warnings_addressed）

- `RMBS`：share_count_older_than_200_days
- `RMBS`：financials_from_fallback: yahoo_timeseries (SEC XBRL latest quarter 2026-03-31)
- `RMBS`：sec_stale_series_dropped:total_debt:last_end_2023-09-30_vs_newest_2026-03-31

## 7. 下一步（快速路径）

1. 只在 brief 不够时再读一手文件：`python connectors/live_data.py filing-text --ticker X --latest 10-Q --preset contracts`（≤2 份）。
2. 填写 `lens-draft.json` 中所有 `TODO:` 字段（判断、情景、证伪条件、红队）。
3. `python scripts/serenity_lens.py finish lens-draft.json --md report.md --html report.html` 一步完成计算、校验、渲染与核验。

---

框架声明：本 skill 根据 Serenity 公开发布的内容提炼研究框架，用于回测与研究分析；报告由框架生成，不代表 Serenity 本人观点，亦非投资建议。
