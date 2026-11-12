# 研究包：UPST（Upstart Holdings, Inc.）

> 数据抓取 2026-11-06T04:39:40Z · 连接器 v9.1.0 · 用时 3.86 秒。以下是数据底稿与机械线索，不是结论；判断写进 lens-draft.json 后用 `serenity_lens.py finish` 收尾。

## 1. 对比表（USD 用即期汇率，仅作横向比较）

| 代码 | 价格 | 市值(USD) | 52周回撤 | 1年涨跌 | TTM收入(USD) | 收入同比 | 收入环比 | 毛利率(期末) | 毛利率同比 | P/S | 股本变化 | 机械旗标 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `UPST` | 22.14 USD | 2.19B | -57.5% | -42.9% | 1.34B | +33.7% | +1.6% | — | — | 1.6x | +1.7% | material_agreement_8k_1_01, beneficial_owner_filings, insider_form4_activity, capacity_language, atm_language |

## 2. 主体要点

- 最新季度收入：370.52M USD（期末 2026-09-30）；营业利润率 9.7%；现金+短投 461.48M；FCF 跑道 9.9 季。
- 计算市值：2.19B USD（22.14 × 98,908,658 股，股本截至 2026-10-27）。
- 文件雷达 `material_agreement_8k_1_01`（PB-SIG-02）：Open the 8-K exhibit: customer/supply/financing agreement? counterparty quality?
- 文件雷达 `beneficial_owner_filings`（PB-SIG-09）：New 13G/13D filers = institutional discovery or activist; read filer name and %.
- 文件雷达 `insider_form4_activity`（PB-SIG-10）：Classify open-market buys (code P) vs sales/grants; buys after a run-up are rarer signals.
- SEC 全文检索命中（近 25 个月）：atm_program 15（主文档 4/6）；capacity_signal 18（主文档 1/6）

## 2c. 本地财务与公司体检


### 公司体检（通用框架 · company-check-v2）

- 类型路由：**银行**（依据：SEC SIC 6199 (Finance Services)）
- 数据：sec_companyfacts，报告期 2026-09-30，币种 USD；证据 E-LIVE-FIN
- 阶段：**常规经营期**（financial company）；该阶段看：ROE、P/B、资产质量
- 结果：🚩 0 · 👀 2 · ✅ 5 · ℹ️ 1 · — 3

| 项目 | 数值 | 状态 | 公式 / 说明 |
|---|---|---|---|
| G1 收入同比 | 33.71% | ✅ | 最新报告期累计收入同比（A/H 聚合源）或最新季度同比（SEC/Yahoo） |
| G2 归母净利同比 | 102.13% | ✅ | TTM 净利润 vs 一年前 TTM（SEC；上年为亏损时不计算） |
| P2 净利率（TTM） | 4.86% | ℹ️ | TTM 净利润 / TTM 收入 |
| P3 ROE（TTM） | 7.34% | 👀 | TTM 归母净利润 / 期末归母权益（未取平均） |
| C3 股权激励费用 / 收入（TTM） | 11.32% | 👀 | TTM 股权激励费用 / TTM 收入；高 SBC 是隐性稀释 |
| B2 商誉 / 归母权益 | 7.56% | ✅ | 期末商誉 / 期末归母权益；商誉大意味着减值风险 |
| D1 股本变化（约一年） | 1.67% | ✅ | 最新股本 / 4 个观测点前 − 1；持续增发=稀释 |
| S1 不良贷款率 | — | — | 聚合源银行专项指标（最新报告期） |
| S2 拨备覆盖率 | — | — | 聚合源银行专项指标（最新报告期） |
| S3 核心一级资本充足率 | — | — | 聚合源银行专项指标（最新报告期） |
| V1 P/S（增速 < 40% 时） | 1.63x | ✅ | 市值 / TTM 收入，仅在收入增速 < 40% 时打分；好公司 ≠ 好价格：增速不够时高 P/S 需要更强的前瞻证据 |

**估值（USD 口径）**

- 市值 21.90亿 USD · P/E(TTM) 33.6x · P/B 2.5x · P/S 1.6x
- 股本口径：latest reported shares (market_current)

**需核实清单（到定期报告/公告原文确认）**

- [ ] 瓶颈/主题业务占总收入的比例（分部披露；占比小=敞口被稀释）
- [ ] 近 12 个月融资：方式（ATM（持续、无上限，最差）< 溢价可转债 < 定增 < 客户预付/长约（最好））、规模/市值、用途、价格；未用完的 ATM/储架额度
- [ ] 前五大客户集中度与长约条款（期限、可取消比例、预付款）

> 机械体检：每项都附公式与阈值（RULES），状态只是“该去看什么”，不是买卖结论。
> 金融类公司：毛利率、现金流、资产负债率不适用，改看 ROE、P/B 与（银行）资产质量指标。

## 3. 一手文件关键词摘录

### 10-K（提交 2026-02-10，期末 2025-12-31）`E-LIVE-DOC-01`
来源：https://www.sec.gov/Archives/edgar/data/1647639/000164763926000027/upst-20251231.htm

- **at_the_market** ×1：…s, to additional paid-in capital. During the year ended December 31, 2025, the Company made no repurchases of common stock. As of December 31, 2025, $222.1 million remains available for future purchases of our common stock under the share repurchase program. At-the-Market Program On February 14, 2025, in connection with the commencement of an “at the market” offering program, the Company entered into a sales agreeme
- **default_covenant** ×2：…ts and other requirements, and under certain circumstances lenders may reduce availability, require repayment of outstanding borrowings, impose additional conditions or terminate their commitments. If we fail to comply with these requirements or experience an event of default, we could be required to repay borrowings, post additional collateral, liquidate assets at unfavorable prices or seek alternative financing, w

### 10-Q（提交 2026-11-03，期末 2026-09-30）`E-LIVE-DOC-02`
来源：https://www.sec.gov/Archives/edgar/data/1647639/000164763926000084/upst-20260930.htm

- **at_the_market** ×1：…with the 2029 Notes 2032 Capped Calls: Capped call transactions entered into in connection with the 2032 Notes ACH: Automated Clearing House AI: Artificial Intelligence ASC: Accounting Standards Codification ASU: Accounting Standards Update ATM Program: At-the-Market offering program AWS: Amazon Web Services CFPB: Consumer Financial Protection Bureau CODM: Chief Operating Decision Maker DCF: Discounted Cash Flow ESP
- **default_covenant** ×3：…lion, (ii) the sum of consolidated eligible assets, plus liquidity in excess of $100.0 million, of not less than $300.0 million in the aggregate, and (iii) a maximum consolidated secured gross leverage ratio of not more than 2.50 to 1.00. The occurrence of an event of default under the Revolver could result in all loans and other obligations under the Revolver becoming immediately due and payable and the Revolver be

## 4. 图谱位置与下一跳候选

- 未收录于卡点图谱：Not in atlas: map the chain manually (PB-HUNT-08) and consider adding a node.

## 5. Serenity 公开言论记忆（时点）

- 状态：no_mentions；公开时间线里没有关于 UPST 本身的表态（覆盖至 2026-10-19）。没提到不代表看空。

## 6. 数据质量警告（写进 lens 的 live_data.warnings_addressed）


## 7. 下一步（快速路径）

1. 只在 brief 不够时再读一手文件：`python connectors/live_data.py filing-text --ticker X --latest 10-Q --preset contracts`（≤2 份）。
2. 填写 `lens-draft.json` 中所有 `TODO:` 字段（判断、情景、证伪条件、红队）。
3. `python scripts/serenity_lens.py finish lens-draft.json --md report.md --html report.html` 一步完成计算、校验、渲染与核验。

---

框架声明：本 skill 根据 Serenity 公开发布的内容提炼研究框架，用于回测与研究分析；报告由框架生成，不代表 Serenity 本人观点，亦非投资建议。
