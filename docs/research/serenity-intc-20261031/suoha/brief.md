# 研究包：INTC（Intel Corporation）

> 数据抓取 2026-10-31T05:25:32Z · 连接器 v9.1.0 · 用时 21.15 秒。以下是数据底稿与机械线索，不是结论；判断写进 lens-draft.json 后用 `serenity_lens.py finish` 收尾。

## 1. 对比表（USD 用即期汇率，仅作横向比较）

| 代码 | 价格 | 市值(USD) | 52周回撤 | 1年涨跌 | TTM收入(USD) | 收入同比 | 收入环比 | 毛利率(期末) | 毛利率同比 | P/S | 股本变化 | 机械旗标 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `INTC` | 65.76 USD | 349.51B | -53.8% | +66.5% | 59.89B | +20.9% | +2.4% | 43.0% (2026-09-26) | +4.8pp | 5.8x | +11.4% | dilution, shelf_registration_on_file, repeated_prospectus_takedowns, unregistered_equity_sale_8k_3_02, beneficial_owner_filings |

## 2. 主体要点

- 最新季度收入：16.51B USD（期末 2026-09-26）；营业利润率 15.3%；现金+短投 54.01B；FCF 跑道 — 季。
- 计算市值：349.51B USD（65.76 × 5,315,000,000 股，股本截至 2026-10-23）。
- 文件雷达 `shelf_registration_on_file`（PB-FIN-01）：Read the S-3/424B5 for size vs market cap and whether an ATM sales agreement exists.
- 文件雷达 `repeated_prospectus_takedowns`（PB-FIN-02）：Serial 424B supplements: an 8-K item 1.01 within 2 days usually marks an underwritten follow-on (read the price vs today); without it, suspect an active ATM and size the overhang.
- 文件雷达 `unregistered_equity_sale_8k_3_02`（PB-FIN-03）：Private placement/PIPE: who bought, price vs market, lockup, warrants.
- 文件雷达 `beneficial_owner_filings`（PB-SIG-09）：New 13G/13D filers = institutional discovery or activist; read filer name and %.
- 文件雷达 `insider_form4_activity`（PB-SIG-10）：Classify open-market buys (code P) vs sales/grants; buys after a run-up are rarer signals.
- SEC 全文检索命中（近 25 个月）：supply_concentration 3（主文档 2/3）；customer_concentration 32（主文档 1/6）；atm_program 1（主文档 0/1）；capacity_signal 24（主文档 2/6）；going_concern 1（主文档 0/1）

## 2c. 本地财务与公司体检


### 公司体检（通用框架 · company-check-v2）

- 类型路由：**一般经营企业**（依据：SEC SIC 3674 (Semiconductors & Related Devices)）
- 数据：sec_companyfacts，报告期 2026-09-26，币种 USD；证据 E-LIVE-FIN
- 阶段：**常规经营期**（常规口径）；该阶段看：收入增速、利润率、现金转换、估值
- 结果：🚩 3 · 👀 0 · ✅ 8 · ℹ️ 4 · — 1

| 项目 | 数值 | 状态 | 公式 / 说明 |
|---|---|---|---|
| G1 收入同比 | 20.95% | ✅ | 最新报告期累计收入同比（A/H 聚合源）或最新季度同比（SEC/Yahoo） |
| G2 归母净利同比 | -6,176.77% | 🚩 | TTM 净利润 vs 一年前 TTM（SEC；上年为亏损时不计算） |
| P1 毛利率 | 42.97% | ℹ️ | 毛利 / 收入（最新期） |
| P1d 毛利率同比变化 | 4.75pp | ✅ | 最新季度毛利率 − 去年同季 |
| P2 净利率（TTM） | -20.09% | ℹ️ | TTM 净利润 / TTM 收入 |
| P3 ROE（TTM） | -10.47% | 🚩 | TTM 归母净利润 / 期末归母权益（未取平均） |
| C1 经营现金流 / 净利润（TTM） | -1.45x | ℹ️ | TTM 经营活动现金流净额 / TTM 净利润；长期 <0.7 说明利润没有变成现金 |
| C2 自由现金流（TTM） | 37.68亿 USD | ✅ | TTM 经营现金流 − TTM 资本开支 |
| C3 股权激励费用 / 收入（TTM） | 4.06% | ✅ | TTM 股权激励费用 / TTM 收入；高 SBC 是隐性稀释 |
| B1 资产负债率 | — | — | 总负债 / 总资产 |
| B2 商誉 / 归母权益 | 17.81% | ✅ | 期末商誉 / 期末归母权益；商誉大意味着减值风险 |
| B3 净现金（现金 − 有息负债） | 76.88亿 USD | ℹ️ | 现金及等价物(+短期存款/短投) − 短借 − 长借 − 应付债券 |
| W1 应收增速 − 收入增速 | 6.88pp | ✅ | 应收账款同比（2025-09-27→2026-09-26）− 收入同比 |
| W2 存货增速 − 收入增速 | -7.21pp | ✅ | 存货同比（2025-09-27→2026-09-26）− 收入同比 |
| D1 股本变化（约一年） | 11.43% | 🚩 | 最新股本 / 4 个观测点前 − 1；每股收入同比 +8.5%；核实融资方式：ATM（持续、无上限，最差）< 溢价可转债 < 定增 < 客户预付/长约（最好） |
| V1 P/S（增速 < 40% 时） | 5.84x | ✅ | 市值 / TTM 收入，仅在收入增速 < 40% 时打分；好公司 ≠ 好价格：增速不够时高 P/S 需要更强的前瞻证据 |

**估值（USD 口径）**

- 市值 3,495.14亿 USD · P/B 3.0x · P/S 5.8x · P/FCF 92.8x
- 股本口径：latest reported shares (market_current)
- 注：loss-making on a TTM basis: P/E not meaningful

**需核实清单（到定期报告/公告原文确认）**

- [ ] 瓶颈/主题业务占总收入的比例（分部披露；占比小=敞口被稀释）
- [ ] 近 12 个月融资：方式（ATM（持续、无上限，最差）< 溢价可转债 < 定增 < 客户预付/长约（最好））、规模/市值、用途、价格；未用完的 ATM/储架额度
- [ ] 前五大客户集中度与长约条款（期限、可取消比例、预付款）
- [ ] G2 归母净利同比：到定期报告原文核对口径与一次性因素
- [ ] P3 ROE（TTM）：到定期报告原文核对口径与一次性因素
- [ ] D1 股本变化（约一年）：到定期报告原文核对口径与一次性因素

> 机械体检：每项都附公式与阈值（RULES），状态只是“该去看什么”，不是买卖结论。

## 3. 一手文件关键词摘录

### 10-K（提交 2026-01-23，期末 2025-12-27）`E-LIVE-DOC-01`
来源：https://www.sec.gov/Archives/edgar/data/50863/000005086326000011/intc-20251227.htm

- **prepayment** ×2：…l expenditures for worldwide manufacturing and assembly and test, including investments in our process technology roadmap; investments in our product roadmap; working capital requirements, including cash outlays associated with the 2025 Restructuring Plan and prepayments we may enter into to secure supply; partner distributions to our non-controlling interest holders; pending and potential acquisitions; and strategi
- **long_term_supply_agreement** ×2：…or delay product purchase commitments with little or no notice to us and without penalty. From time to time, we may enter into additional agreements with customers covering, for example, changes from our standard terms and conditions, new product development, long term supply arrangements and marketing and private-label branding. Our sales are routinely made using electronic and web-based processes that allow custom
- **sole_source** ×2：…encompassing thousands of suppliers worldwide. We source various critical semiconductor development and manufacturing tools and materials, including rare earth elements, minerals and metals, from multiple suppliers. In some cases, however, we are reliant upon sole-source providers, such as with the EUV lithography tools manufactured by ASML that are required for leading-edge process technologies, or providers that a
- **customer_concentration** ×4：…re to manage risks related to our use of distributors and other third parties may reduce sales, increase expenses and weaken our competitive position. We receive a significant portion of our revenue from a limited number of customers. Collectively, our three largest customers accounted for 43% of our net revenue in 2025, 45% of our net revenue in 2024 and 40% of our net revenue in 2023. We expect a small number of c
- **export_controls** ×8：…cies and priorities; ▪technology trends and developments, including with respect to AI; ▪macro environmental and economic conditions; ▪geopolitical tensions and conflicts, including with respect to international trade policies in areas such as tariffs and export controls, and their potential impact on our business; ▪tax- and accounting-related expectations; ▪expectations regarding our relationships with certain sanc

### 10-Q（提交 2026-10-30，期末 2026-09-26）`E-LIVE-DOC-02`
来源：https://www.sec.gov/Archives/edgar/data/50863/000005086326000191/intc-20260926.htm

- **customer_deposits** ×1：…er 27, 2025). Refer to "Note 4: Earnings (Loss) Per Share and Stockholders' Equity" within Notes to Consolidated Condensed Financial Statements. Other Long-term Liabilities Other long-term liabilities as of September 26, 2026 include $1.2 billion related to customer deposits received to secure product supply in future periods and $5.1 billion related to the fair value of the Escrowed Shares derivative liability ($1.
- **prepayment** ×2：…unding requirements include capital expenditures for worldwide manufacturing and assembly and test operations, including investments in our process technology roadmap, investments in our product roadmap, working capital requirements (including commitments and prepayments made to secure supply capacity), partner distributions to our non-controlling interest holder related to Arizona SCIP, reducing outstanding indebte
- **export_controls** ×2：…g, incentives, policies and priorities; ▪technology trends and developments, including with respect to AI; ▪macroeconomic conditions; ▪geopolitical tensions and conflicts, including with respect to international trade policies in areas such as tariffs and export controls, and their potential impact on our business; ▪tax- and accounting-related expectations; ▪expectations regarding our relationships with certain sanc

## 4. 图谱位置与下一跳候选

- 链 `ai_compute_neocloud` / 节点 `server_cpu`（服务器 CPU（AI 推理/Agent 带动 CPU:GPU 比例上升），状态 now，类型 material）；同层：AMD, ARM
  - 图谱状态最后核验：2026-10-19（12 天前；超过 180 天需重新核验）。图谱状态只是线索，用本次实时数据主动质疑它。

## 5. Serenity 公开言论记忆（时点）

- 状态：available；公开帖转述（不是原话，不含订阅内容），帖子编号可在 x.com 查原文。立场 = 当时公开表达的看法，不是持仓记录；2026-10-19 之后是否有新表态未知（沉默不等于卖出）。Serenity 的说法是线索，不是公司事实。
  - 2026-01-13 `2011006623893123154` REAFFIRM/bullish
  - 2026-09-22 `2102247915251224980` REAFFIRM/bullish

## 6. 数据质量警告（写进 lens 的 live_data.warnings_addressed）

- `INTC`：sec_stale_series_dropped:buybacks:last_end_2022-12-31_vs_newest_2026-09-26
- `INTC`：sec_stale_series_dropped:contract_liabilities:last_end_2021-12-25_vs_newest_2026-09-26

## 7. 下一步（快速路径）

1. 只在 brief 不够时再读一手文件：`python connectors/live_data.py filing-text --ticker X --latest 10-Q --preset contracts`（≤2 份）。
2. 填写 `lens-draft.json` 中所有 `TODO:` 字段（判断、情景、证伪条件、红队）。
3. `python scripts/serenity_lens.py finish lens-draft.json --md report.md --html report.html` 一步完成计算、校验、渲染与核验。

---

框架声明：本 skill 根据 Serenity 公开发布的内容提炼研究框架，用于回测与研究分析；报告由框架生成，不代表 Serenity 本人观点，亦非投资建议。
