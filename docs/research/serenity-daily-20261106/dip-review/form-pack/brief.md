# 研究包：FORM（FormFactor, Inc.）

> 数据抓取 2026-11-06T03:14:12Z · 连接器 v9.1.0 · 用时 3.13 秒。以下是数据底稿与机械线索，不是结论；判断写进 lens-draft.json 后用 `serenity_lens.py finish` 收尾。

## 1. 对比表（USD 用即期汇率，仅作横向比较）

| 代码 | 价格 | 市值(USD) | 52周回撤 | 1年涨跌 | TTM收入(USD) | 收入同比 | 收入环比 | 毛利率(期末) | 毛利率同比 | P/S | 股本变化 | 机械旗标 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `FORM` | 71.76 USD | 5.63B | -55.2% | +34.0% | 980.10M | +38.4% | +8.6% | 54.7% (2026-09-26) | +14.9pp | 5.7x | +1.1% | pricing_power, unregistered_equity_sale_8k_3_02, beneficial_owner_filings, insider_form4_activity, going_concern_exhibit_only |

## 2. 主体要点

- 最新季度收入：280.55M USD（期末 2026-09-26）；营业利润率 29.1%；现金+短投 395.41M；FCF 跑道 — 季。
- 计算市值：5.63B USD（71.76 × 78,403,115 股，股本截至 2026-10-28）。
- 文件雷达 `unregistered_equity_sale_8k_3_02`（PB-FIN-03）：Private placement/PIPE: who bought, price vs market, lockup, warrants.
- 文件雷达 `beneficial_owner_filings`（PB-SIG-09）：New 13G/13D filers = institutional discovery or activist; read filer name and %.
- 文件雷达 `insider_form4_activity`（PB-SIG-10）：Classify open-market buys (code P) vs sales/grants; buys after a run-up are rarer signals.
- SEC 全文检索命中（近 25 个月）：supply_concentration 10（主文档 6/6）；customer_concentration 8（主文档 5/6）；atm_program 1（主文档 0/1）；capacity_signal 12（主文档 4/6）；going_concern 2（主文档 0/2）

## 2c. 本地财务与公司体检


### 公司体检（通用框架 · company-check-v2）

- 类型路由：**一般经营企业**（依据：SEC SIC 3674 (Semiconductors & Related Devices)）
- 数据：sec_companyfacts，报告期 2026-09-26，币种 USD；证据 E-LIVE-FIN
- 阶段：**常规经营期**（常规口径）；该阶段看：收入增速、利润率、现金转换、估值
- 结果：🚩 0 · 👀 0 · ✅ 14 · ℹ️ 3 · — 0

| 项目 | 数值 | 状态 | 公式 / 说明 |
|---|---|---|---|
| G1 收入同比 | 38.42% | ✅ | 最新报告期累计收入同比（A/H 聚合源）或最新季度同比（SEC/Yahoo） |
| G2 归母净利同比 | 325.06% | ✅ | TTM 净利润 vs 一年前 TTM（SEC；上年为亏损时不计算） |
| P1 毛利率 | 54.68% | ℹ️ | 毛利 / 收入（最新期） |
| P1d 毛利率同比变化 | 14.90pp | ✅ | 最新季度毛利率 − 去年同季 |
| P2 净利率（TTM） | 17.72% | ℹ️ | TTM 净利润 / TTM 收入 |
| P3 ROE（TTM） | 14.70% | ✅ | TTM 归母净利润 / 期末归母权益（未取平均） |
| C1 经营现金流 / 净利润（TTM） | 1.48x | ✅ | TTM 经营活动现金流净额 / TTM 净利润；长期 <0.7 说明利润没有变成现金 |
| C2 自由现金流（TTM） | 1.81亿 USD | ✅ | TTM 经营现金流 − TTM 资本开支 |
| C3 股权激励费用 / 收入（TTM） | 3.61% | ✅ | TTM 股权激励费用 / TTM 收入；高 SBC 是隐性稀释 |
| B1 资产负债率 | 17.49% | ✅ | 总负债 / 总资产 |
| B2 商誉 / 归母权益 | 17.99% | ✅ | 期末商誉 / 期末归母权益；商誉大意味着减值风险 |
| B3 净现金（现金 − 有息负债） | 3.85亿 USD | ℹ️ | 现金及等价物(+短期存款/短投) − 短借 − 长借 − 应付债券 |
| W1 应收增速 − 收入增速 | -23.91pp | ✅ | 应收账款同比（2025-09-27→2026-09-26）− 收入同比 |
| W2 存货增速 − 收入增速 | -19.30pp | ✅ | 存货同比（2025-09-27→2026-09-26）− 收入同比 |
| W3 合同负债/预收同比 | 61.47% | ✅ | 期末合同负债 / 去年同期 − 1；上升=客户预付增加（需求领先信号）；大降需追问 |
| D1 股本变化（约一年） | 1.14% | ✅ | 最新股本 / 4 个观测点前 − 1；持续增发=稀释 |
| V1 P/S（增速 < 40% 时） | 5.74x | ✅ | 市值 / TTM 收入，仅在收入增速 < 40% 时打分；好公司 ≠ 好价格：增速不够时高 P/S 需要更强的前瞻证据 |

**估值（USD 口径）**

- 市值 56.26亿 USD · P/E(TTM) 32.4x · P/B 4.8x · P/S 5.7x · P/FCF 31.0x
- 股本口径：latest reported shares (market_current)

**需核实清单（到定期报告/公告原文确认）**

- [ ] 瓶颈/主题业务占总收入的比例（分部披露；占比小=敞口被稀释）
- [ ] 近 12 个月融资：方式（ATM（持续、无上限，最差）< 溢价可转债 < 定增 < 客户预付/长约（最好））、规模/市值、用途、价格；未用完的 ATM/储架额度
- [ ] 前五大客户集中度与长约条款（期限、可取消比例、预付款）

> 机械体检：每项都附公式与阈值（RULES），状态只是“该去看什么”，不是买卖结论。

## 3. 一手文件关键词摘录

### 10-K（提交 2026-02-20，期末 2025-12-27）`E-LIVE-DOC-01`
来源：https://www.sec.gov/Archives/edgar/data/1039399/000103939926000009/form-20251227.htm

- **remaining_performance_obligations** ×4：…g prices are determined based on observable prices, which are the prices at which we separately sell these products. For items which do not have observable prices, we use our best estimate of the stand-alone selling prices. Transaction price allocated to the remaining performance obligations: On December 27, 2025, we had $30.3 million of remaining performance obligations, which were comprised of deferred service con
- **customer_deposits** ×4：…g other than the passage of time. Contract assets as of December 27, 2025 and December 28, 2024 were $2.3 million and $6.9 million, respectively, and are reported on the Consolidated Balance Sheets as a component of Prepaid expenses and other current assets. Contract liabilities include payments received and payments due in advance of performance under a contract and are satisfied as the associated revenue is recogn
- **sole_source** ×3：…we do not achieve the benefits anticipated from any of these investments, or if the achievement any of these benefits is delayed, our operating results may be negatively impacted. We obtain some of the components and materials we use in our products from a sole source or a limited group of suppliers, and the partial or complete loss of one of these suppliers, or scarcity of raw materials from one of these suppliers,
- **customer_concentration** ×3：…he following customers represented 10% or more of our revenues: Fiscal Year Ended December 27, 2025 December 28, 2024 December 30, 2023 SK hynix Inc. 22.9 % 18.9 % * Intel Corporation * 14.6 % 17.1 % * Less than 10% of revenues. At December 27, 2025, two customers accounted for 15.8% and 10.8% of gross accounts receivable. At December 28, 2024, one customer accounted for 22.0% of gross accounts receivable. No other 
- **material_weakness** ×1：…provide reliable financial reports or prevent fraud, our business and reputation may be harmed. We regularly review and assess our internal controls over financial reporting and our disclosure controls and procedures. As part of that process, we may discover material weaknesses in our internal controls. If we fail to maintain effective controls or timely implement any necessary improvement of our internal and disclo
- **export_controls** ×6：…of operations or cash flows. We have received, and may receive in the future, notices of violations of environmental regulations, or otherwise learn of such violations. Environmental contamination or violations may negatively impact our business. Import and Export Control We manufacture, market and sell our products both inside and outside the U.S. Certain products are subject to export control regulations. Failure 

### 10-Q（提交 2026-11-03，期末 2026-09-26）`E-LIVE-DOC-02`
来源：https://www.sec.gov/Archives/edgar/data/1039399/000103939926000043/form-20260926.htm

- **remaining_performance_obligations** ×4：…Total minimum lease payments 18,746 Less: interest (2,344) Present value of net minimum lease payments 16,402 Less: current portion (8,126) Total long-term operating lease liabilities $ 8,276 Note 17 — Revenue Transaction price allocated to the remaining performance obligations: On September 26, 2026, we had $13.3 million of remaining performance obligations, which were comprised of deferred service contracts, exten
- **customer_deposits** ×4：…n the passage of time. Contract assets as of September 26, 2026 and December 27, 2025 were $3.2 million and $2.3 million, respectively, and are reported on the Condensed Consolidated Balance Sheets as a component of Prepaid expenses and other current assets. Contract liabilities include payments received and payments due in advance of performance under a contract and are satisfied as the associated revenue is recogn
- **sole_source** ×1：…ory adjustments (including write-downs for inventory obsolescence), and amortization of certain intangible assets. Our manufacturing operations rely on a limited number of suppliers to provide key components and materials for our products, some of which are a sole source. We order materials and supplies based on backlog and forecasted customer orders. Tooling and setup costs related to changing manufacturing lots at
- **customer_concentration** ×3：…tely from other accrued liabilities in Note 6, Accrued Liabilities. These reclassifications had no impact on previously reported results of operations, financial position, or cash flows. Note 2 — Concentration of Credit and Other Risks Each of the following customers accounted for 10% or more of our revenues for the periods indicated: Three Months Ended Nine Months Ended September 26, 2026 September 27, 2025 Septemb
- **export_controls** ×1：…estments, including our capital expenditures, our restructuring plans, including our production plans, our credit facilities, our supply chain, our tax burden, uncertainties related to public health-related crises, the interpretation and impacts of changes in export controls, tariffs and other trade barriers, military conflicts, political volatility, legislative changes and similar factors, our ability to execute ou

## 4. 图谱位置与下一跳候选

- 链 `ai_photonics` / 节点 `siph_test`（硅光/CPO 检测与良率，状态 coming，类型 demand）；同层：6830.TW, AEHR, VIAV
  - 图谱状态最后核验：2026-10-19（18 天前；超过 180 天需重新核验）。图谱状态只是线索，用本次实时数据主动质疑它。

## 5. Serenity 公开言论记忆（时点）

- 状态：available；公开帖转述（不是原话，不含订阅内容），帖子编号可在 x.com 查原文。立场 = 当时公开表达的看法，不是持仓记录；2026-10-19 之后是否有新表态未知（沉默不等于卖出）。Serenity 的说法是线索，不是公司事实。
  - 2026-04-05 `2040842953883840770` REAFFIRM/bullish
  - 2026-07-31 `2083274448845906083` REAFFIRM/bullish

## 6. 数据质量警告（写进 lens 的 live_data.warnings_addressed）


## 7. 下一步（快速路径）

1. 只在 brief 不够时再读一手文件：`python connectors/live_data.py filing-text --ticker X --latest 10-Q --preset contracts`（≤2 份）。
2. 填写 `lens-draft.json` 中所有 `TODO:` 字段（判断、情景、证伪条件、红队）。
3. `python scripts/serenity_lens.py finish lens-draft.json --md report.md --html report.html` 一步完成计算、校验、渲染与核验。

---

框架声明：本 skill 根据 Serenity 公开发布的内容提炼研究框架，用于回测与研究分析；报告由框架生成，不代表 Serenity 本人观点，亦非投资建议。
