# 研究包：NVDA（NVIDIA Corporation）

> 数据抓取 2026-10-28T13:38:01Z · 连接器 v9.1.0 · 用时 3.51 秒。以下是数据底稿与机械线索，不是结论；判断写进 lens-draft.json 后用 `serenity_lens.py finish` 收尾。

## 1. 对比表（USD 用即期汇率，仅作横向比较）

| 代码 | 价格 | 市值(USD) | 52周回撤 | 1年涨跌 | TTM收入(USD) | 收入同比 | 收入环比 | 毛利率(期末) | 毛利率同比 | P/S | 股本变化 | 机械旗标 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `NVDA` | 219.13 USD | 5.28T | -10.0% | +8.2% | 302.97B | +105.8% | +17.9% | 75.0% (2026-07-26) | +2.6pp | 17.4x | -0.8% | acceleration, repeated_prospectus_takedowns, material_agreement_8k_1_01, beneficial_owner_filings, insider_form4_activity |

## 2. 主体要点

- 最新季度收入：96.22B USD（期末 2026-07-26）；营业利润率 66.2%；现金+短投 22.44B；FCF 跑道 — 季。
- 计算市值：5.28T USD（219.13 × 24,100,000,000 股，股本截至 2026-08-21）。
- 文件雷达 `repeated_prospectus_takedowns`（PB-FIN-02）：Serial 424B supplements: an 8-K item 1.01 within 2 days usually marks an underwritten follow-on (read the price vs today); without it, suspect an active ATM and size the overhang.
- 文件雷达 `material_agreement_8k_1_01`（PB-SIG-02）：Open the 8-K exhibit: customer/supply/financing agreement? counterparty quality?
- 文件雷达 `beneficial_owner_filings`（PB-SIG-09）：New 13G/13D filers = institutional discovery or activist; read filer name and %.
- 文件雷达 `insider_form4_activity`（PB-SIG-10）：Classify open-market buys (code P) vs sales/grants; buys after a run-up are rarer signals.
- SEC 全文检索命中（近 25 个月）：customer_concentration 1（主文档 0/1）；capacity_signal 13（主文档 4/6）

## 2c. 本地财务与公司体检


### 公司体检（通用框架 · company-check-v2）

- 类型路由：**一般经营企业**（依据：SEC SIC 3674 (Semiconductors & Related Devices)）
- 数据：sec_companyfacts，报告期 2026-07-26，币种 USD；证据 E-LIVE-FIN
- 阶段：**常规经营期**（常规口径）；该阶段看：收入增速、利润率、现金转换、估值
- 结果：🚩 0 · 👀 2 · ✅ 10 · ℹ️ 3 · — 0

| 项目 | 数值 | 状态 | 公式 / 说明 |
|---|---|---|---|
| G1 收入同比 | 105.85% | ✅ | 最新报告期累计收入同比（A/H 聚合源）或最新季度同比（SEC/Yahoo） |
| G2 归母净利同比 | 122.73% | ✅ | TTM 净利润 vs 一年前 TTM（SEC；上年为亏损时不计算） |
| P1 毛利率 | 74.98% | ℹ️ | 毛利 / 收入（最新期） |
| P1d 毛利率同比变化 | 2.56pp | ✅ | 最新季度毛利率 − 去年同季 |
| P2 净利率（TTM） | 63.66% | ℹ️ | TTM 净利润 / TTM 收入 |
| P3 ROE（TTM） | 84.23% | ✅ | TTM 归母净利润 / 期末归母权益（未取平均） |
| C1 经营现金流 / 净利润（TTM） | 0.70x | 👀 | TTM 经营活动现金流净额 / TTM 净利润；长期 <0.7 说明利润没有变成现金 |
| C3 股权激励费用 / 收入（TTM） | 2.39% | ✅ | TTM 股权激励费用 / TTM 收入；高 SBC 是隐性稀释 |
| B1 资产负债率 | 28.50% | ✅ | 总负债 / 总资产 |
| B2 商誉 / 归母权益 | 9.23% | ✅ | 期末商誉 / 期末归母权益；商誉大意味着减值风险 |
| B3 净现金（现金 − 有息负债） | -109.23亿 USD | ℹ️ | 现金及等价物(+短期存款/短投) − 短借 − 长借 − 应付债券 |
| W1 应收增速 − 收入增速 | 20.92pp | 👀 | 应收账款同比（2025-07-27→2026-07-26）− 收入同比 |
| W2 存货增速 − 收入增速 | 5.18pp | ✅ | 存货同比（2025-07-27→2026-07-26）− 收入同比 |
| W3 合同负债/预收同比 | 371.02% | ✅ | 期末合同负债 / 去年同期 − 1；上升=客户预付增加（需求领先信号）；大降需追问 |
| D1 股本变化（约一年） | -0.82% | ✅ | 最新股本 / 4 个观测点前 − 1；持续增发=稀释 |

**估值（USD 口径）**

- 市值 5.28万亿 USD · P/E(TTM) 27.4x · P/B 23.1x · P/S 17.4x · 股息率 0.13% · 回购收益率 1.05%
- 股本口径：latest reported shares (market_current)

**需核实清单（到定期报告/公告原文确认）**

- [ ] 瓶颈/主题业务占总收入的比例（分部披露；占比小=敞口被稀释）
- [ ] 近 12 个月融资：方式（ATM（持续、无上限，最差）< 溢价可转债 < 定增 < 客户预付/长约（最好））、规模/市值、用途、价格；未用完的 ATM/储架额度
- [ ] 前五大客户集中度与长约条款（期限、可取消比例、预付款）

> 机械体检：每项都附公式与阈值（RULES），状态只是“该去看什么”，不是买卖结论。

## 3. 一手文件关键词摘录

### 10-K（提交 2026-02-25，期末 2026-01-25）`E-LIVE-DOC-01`
来源：https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm

- **remaining_performance_obligations** ×1：…Consolidated Financial Statements (Continued) We recognized revenue of $974 million and $729 million in fiscal years 2026 and 2025, respectively, that were included in the prior year end deferred revenue balance. As of January 25, 2026, revenue related to remaining performance obligations from contracts greater than one year in length was $2.3 billion, which includes $1.9 billion from deferred revenue and $390 milli
- **customer_deposits** ×4：…ed expenses 1,146 848 Other 1,373 897 Total accrued and other current liabilities $ 21,352 $ 11,737 (1)In fiscal years 2026 and 2025, we recorded an expense of approximately $3.2 billion and $2.0 billion, respectively, in cost of revenue. (2)Includes customer advances and unearned revenue related to hardware and software support, cloud services, and license and development arrangements. The balance as of January 25,
- **capacity_reservation** ×3：…supply may be extended. We have previously experienced and may continue to experience extended lead times of more than 12 months. To secure future supply and capacity, we have paid premiums, provided deposits, and entered into long-term supply agreements and capacity commitments, which have increased our product costs and this may continue. We may still be unable to secure sufficient commitments for capacity to addr
- **long_term_supply_agreement** ×1：…hain, the lead times for certain supply may be extended. We have previously experienced and may continue to experience extended lead times of more than 12 months. To secure future supply and capacity, we have paid premiums, provided deposits, and entered into long-term supply agreements and capacity commitments, which have increased our product costs and this may continue. We may still be unable to secure sufficient
- **customer_concentration** ×2：…directly from NVIDIA as direct customers, such as AIBs, distributors, ODMs, OEMs, CSPs, AI model makers, and system integrators. Certain direct customers may use either internal resources or third-party system integrators to complete their build. Three direct customers accounted for 25%, 18%, and 13% of our accounts receivable balance as of January 25, 2026. Two direct customers accounted for 17% and 16% of our acco
- **material_weakness** ×3：…could impose substantial demands on management time. Failure to implement new or updated controls, or difficulties encountered in their implementation, could harm our operating results or cause us to fail to meet our reporting obligations. Identification of material weaknesses in our internal controls, even if quickly remediated once disclosed, may cause investors to lose confidence in our financial statements and o
- **export_controls** ×54：…ents. Government Regulations Our worldwide business activities are subject to various laws, rules, and regulations of the United States as well as of foreign governments. Over the past three years, we have been subject to a series of shifting and expanding export control restrictions, impacting our ability to serve customers outside the United States. 9 Table of Contents In August 2022, the U.S. government, or USG, 
- **default_covenant** ×1：…al arrangements, including guarantees with partners. We provided $3.5 billion in land, power, and shell guarantees to early‑stage companies, generally over multi‑year periods. If the escrow and the partners' operating activities are not sufficient to cover an event of default under these guarantees, we may elect to assume the underlying leases for internal use or sublease them to third parties. Macroeconomic factors

### 10-Q（提交 2026-08-26，期末 2026-07-26）`E-LIVE-DOC-02`
来源：https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm

- **remaining_performance_obligations** ×1：…ears 2027 and 2026, respectively. We recognized revenue of $758 million and $479 million in the first half of fiscal years 2027 and 2026, respectively, that was included in the prior year-end deferred revenue balance. As of July 26, 2026, revenue related to remaining performance obligations from contracts greater than one year in length was $3.2 billion, which included $3.0 billion from deferred revenue and $244 mil
- **customer_deposits** ×4：…7 Excess inventory purchase obligations (2) 2,138 2,739 Accrued payroll and related expenses 1,206 1,146 Accrued purchase consideration (3) 986 3,921 Other 2,479 1,373 Total accrued and other current liabilities $ 26,960 $ 21,352 (1) Included customer advances and unearned revenue primarily related to hardware and software support, and license and development arrangements. The balance as of July 26, 2026, and Januar
- **capacity_reservation** ×1：…in production, challenges in managing supply and demand, revenue volatility, quality issues, increased inventory provisions, decreases in product yields, higher material 25 costs, and increased warranty costs. We have significantly increased our supply and capacity commitments from $119 billion last quarter to $279 billion as of July 26, 2026 to meet future demand. Refer to Note 10 of the Notes to Condensed Consolid
- **customer_concentration** ×2：…s, or ODMs, original equipment manufacturers, or OEMs, cloud service providers, or CSPs, AI model makers, and system integrators. Certain direct customers may use either internal resources or third-party system integrators to complete their build. Five direct customers accounted for 22%, 14%, 13%, 11%, and 10% of our accounts receivable balance as of July 26, 2026. Three direct customers accounted for 25%, 18%, and 
- **export_controls** ×43：…ing the European Union, the United States, the United Kingdom, South Korea, Japan, and China. For example, the French Competition Authority is questioning whether gaming GPUs and data center GPUs are separate product categories, an inquiry that may impact the export controls applicable to gaming products sold in France and Europe. We have also received, and continue to receive, broad requests for information from co

## 4. 图谱位置与下一跳候选

- 链 `ai_photonics` / 节点 `photonic_platform`（光子 IP / 平台（CPO 交换、光计算），状态 coming，类型 demand）；同层：MRVL, AVGO
  - 图谱状态最后核验：2026-10-19（9 天前；超过 180 天需重新核验）。图谱状态只是线索，用本次实时数据主动质疑它。
  - 下一跳 `LITE` Lumentum — EML 激光（可插拔）（now，依据 serenity_lead）
  - 下一跳 `COHR` Coherent — EML 激光（可插拔）（now，依据 serenity_lead）
  - 下一跳 `AXTI` AXT Inc. — InP 衬底（now，依据 serenity_lead）
  - 下一跳 `5802.T` Sumitomo Electric — InP 衬底（now，依据 serenity_lead）
  - 下一跳 `5016.T` JX Advanced Metals — InP 衬底（now，依据 serenity_lead）

## 5. Serenity 公开言论记忆（时点）

- 状态：available；公开帖转述（不是原话，不含订阅内容），帖子编号可在 x.com 查原文。立场 = 当时公开表达的看法，不是持仓记录；2026-10-19 之后是否有新表态未知（沉默不等于卖出）。Serenity 的说法是线索，不是公司事实。
  - 2025-11-18 `1990815562558308858` REAFFIRM/bullish
  - 2026-03-14 `2032935125378543936` REAFFIRM/bullish
  - 2026-03-18 `2034074445711814981` BEARISH/bearish
  - 2026-03-31 `2038954532944875733` REAFFIRM/bullish
  - 2026-09-23 `2102763548715753927` REAFFIRM/bullish

## 6. 数据质量警告（写进 lens 的 live_data.warnings_addressed）

- `NVDA`：sec_stale_series_dropped:capex:last_end_2020-07-26_vs_newest_2026-07-26

## 7. 下一步（快速路径）

1. 只在 brief 不够时再读一手文件：`python connectors/live_data.py filing-text --ticker X --latest 10-Q --preset contracts`（≤2 份）。
2. 填写 `lens-draft.json` 中所有 `TODO:` 字段（判断、情景、证伪条件、红队）。
3. `python scripts/serenity_lens.py finish lens-draft.json --md report.md --html report.html` 一步完成计算、校验、渲染与核验。

---

框架声明：本 skill 根据 Serenity 公开发布的内容提炼研究框架，用于回测与研究分析；报告由框架生成，不代表 Serenity 本人观点，亦非投资建议。
