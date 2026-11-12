# 研究包：VRT（Vertiv Holdings Co）

> 数据抓取 2026-10-28T13:41:52Z · 连接器 v9.1.0 · 用时 3.04 秒。以下是数据底稿与机械线索，不是结论；判断写进 lens-draft.json 后用 `serenity_lens.py finish` 收尾。

## 1. 对比表（USD 用即期汇率，仅作横向比较）

| 代码 | 价格 | 市值(USD) | 52周回撤 | 1年涨跌 | TTM收入(USD) | 收入同比 | 收入环比 | 毛利率(期末) | 毛利率同比 | P/S | 股本变化 | 机械旗标 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `VRT` | 236.2 USD | 90.93B | -37.8% | +22.5% | 11.48B | +24.1% | +23.6% | 37.7% (2026-06-30) | +3.7pp | 7.9x | +0.8% | shelf_registration_on_file, repeated_prospectus_takedowns, material_agreement_8k_1_01, beneficial_owner_filings, insider_form4_activity |

## 2. 主体要点

- 最新季度收入：3.27B USD（期末 2026-06-30）；营业利润率 19.5%；现金+短投 2.81B；FCF 跑道 — 季。
- 计算市值：90.93B USD（236.2 × 384,988,173 股，股本截至 2026-07-27）。
- 文件雷达 `shelf_registration_on_file`（PB-FIN-01）：Read the S-3/424B5 for size vs market cap and whether an ATM sales agreement exists.
- 文件雷达 `repeated_prospectus_takedowns`（PB-FIN-02）：Serial 424B supplements: an 8-K item 1.01 within 2 days usually marks an underwritten follow-on (read the price vs today); without it, suspect an active ATM and size the overhang.
- 文件雷达 `material_agreement_8k_1_01`（PB-SIG-02）：Open the 8-K exhibit: customer/supply/financing agreement? counterparty quality?
- 文件雷达 `beneficial_owner_filings`（PB-SIG-09）：New 13G/13D filers = institutional discovery or activist; read filer name and %.
- 文件雷达 `insider_form4_activity`（PB-SIG-10）：Classify open-market buys (code P) vs sales/grants; buys after a run-up are rarer signals.
- SEC 全文检索命中（近 25 个月）：supply_concentration 6（主文档 2/6）；capacity_signal 17（主文档 4/6）；going_concern 4（主文档 0/4）

## 2c. 本地财务与公司体检


### 公司体检（通用框架 · company-check-v2）

- 类型路由：**一般经营企业**（依据：SEC SIC 3679 (Electronic Components, NEC)）
- 数据：sec_companyfacts，报告期 2026-06-30，币种 USD；证据 E-LIVE-FIN
- 阶段：**常规经营期**（常规口径）；该阶段看：收入增速、利润率、现金转换、估值
- 结果：🚩 1 · 👀 2 · ✅ 11 · ℹ️ 3 · — 0

| 项目 | 数值 | 状态 | 公式 / 说明 |
|---|---|---|---|
| G1 收入同比 | 24.12% | ✅ | 最新报告期累计收入同比（A/H 聚合源）或最新季度同比（SEC/Yahoo） |
| G2 归母净利同比 | 113.22% | ✅ | TTM 净利润 vs 一年前 TTM（SEC；上年为亏损时不计算） |
| P1 毛利率 | 37.71% | ℹ️ | 毛利 / 收入（最新期） |
| P1d 毛利率同比变化 | 3.72pp | ✅ | 最新季度毛利率 − 去年同季 |
| P2 净利率（TTM） | 15.09% | ℹ️ | TTM 净利润 / TTM 收入 |
| P3 ROE（TTM） | 36.40% | ✅ | TTM 归母净利润 / 期末归母权益（未取平均） |
| C1 经营现金流 / 净利润（TTM） | 1.94x | ✅ | TTM 经营活动现金流净额 / TTM 净利润；长期 <0.7 说明利润没有变成现金 |
| C2 自由现金流（TTM） | 29.30亿 USD | ✅ | TTM 经营现金流 − TTM 资本开支 |
| C3 股权激励费用 / 收入（TTM） | 0.45% | ✅ | TTM 股权激励费用 / TTM 收入；高 SBC 是隐性稀释 |
| B1 资产负债率 | 70.08% | 👀 | 总负债 / 总资产 |
| B2 商誉 / 归母权益 | 47.99% | 👀 | 期末商誉 / 期末归母权益；商誉大意味着减值风险 |
| B3 净现金（现金 − 有息负债） | -1.29亿 USD | ℹ️ | 现金及等价物(+短期存款/短投) − 短借 − 长借 − 应付债券 |
| W1 应收增速 − 收入增速 | 8.35pp | ✅ | 应收账款同比（2025-06-30→2026-06-30）− 收入同比 |
| W2 存货增速 − 收入增速 | 54.38pp | 🚩 | 存货同比（2025-06-30→2026-06-30）− 收入同比 |
| W3 合同负债/预收同比 | 189.01% | ✅ | 期末合同负债 / 去年同期 − 1；上升=客户预付增加（需求领先信号）；大降需追问 |
| D1 股本变化（约一年） | 0.82% | ✅ | 最新股本 / 4 个观测点前 − 1；持续增发=稀释 |
| V1 P/S（增速 < 40% 时） | 7.92x | ✅ | 市值 / TTM 收入，仅在收入增速 < 40% 时打分；好公司 ≠ 好价格：增速不够时高 P/S 需要更强的前瞻证据 |

**估值（USD 口径）**

- 市值 909.34亿 USD · P/E(TTM) 52.5x · P/B 19.1x · P/S 7.9x · P/FCF 31.0x · 股息率 0.09%
- 股本口径：latest reported shares (market_current)

**需核实清单（到定期报告/公告原文确认）**

- [ ] 瓶颈/主题业务占总收入的比例（分部披露；占比小=敞口被稀释）
- [ ] 近 12 个月融资：方式（ATM（持续、无上限，最差）< 溢价可转债 < 定增 < 客户预付/长约（最好））、规模/市值、用途、价格；未用完的 ATM/储架额度
- [ ] 前五大客户集中度与长约条款（期限、可取消比例、预付款）
- [ ] W2 存货增速 − 收入增速：到定期报告原文核对口径与一次性因素

> 机械体检：每项都附公式与阈值（RULES），状态只是“该去看什么”，不是买卖结论。

## 3. 一手文件关键词摘录

### 10-K（提交 2026-02-13，期末 2025-12-31）`E-LIVE-DOC-01`
来源：https://www.sec.gov/Archives/edgar/data/1674101/000167410126000008/vrt-20251231.htm

- **sole_source** ×3：…subject to labor shortages, oversupply, or fixed contractual terms relating to the contingent workforce, and our ability to manage the size of, and costs for, such contingent workforce may be further constrained by local laws or future changes to such laws. •Single-source suppliers - We obtain certain materials or components from single-source suppliers due to technology, availability, price, quality or other consid
- **material_weakness** ×6：…es associated with environmental, health and safety matters; failure to achieve environmental, social and governance goals; failure to realize the value of goodwill and intangible assets; exposure to fluctuations in foreign currency exchange rates; failure to remediate material weaknesses in our internal controls over financial reporting; our level of indebtedness and our ability to comply with the covenants and res
- **export_controls** ×6：…not limited to, laws and regulations relating to data protection and data privacy; •Failure to properly address legal compliance issues, particularly those related to imports/exports, anti-corruption laws, and foreign operations; •The risks associated with export controls, import restrictions, and sanctions programs; •Risks associated with foreign trade policies, including tariffs or global trade conflicts; •Risks a

### 10-Q（提交 2026-07-29，期末 2026-06-30）`E-LIVE-DOC-02`
来源：https://www.sec.gov/Archives/edgar/data/1674101/000162828026050609/vrt-20260630.htm

- **material_weakness** ×1：…es associated with environmental, health and safety matters; failure to achieve environmental, social and governance goals; failure to realize the value of goodwill and intangible assets; exposure to fluctuations in foreign currency exchange rates; failure to remediate material weaknesses in our internal controls over financial reporting; our level of indebtedness and our ability to comply with the covenants and res
- **default_covenant** ×2：…rtain cases the ability of our subsidiaries to incur liens, consolidate or merge, incur additional indebtedness (only applicable to non-guarantor subsidiaries), and pay dividends and distribution in respect of the Borrower’s equity interests when a default or event of default has occurred and is continuing. As of June 30, 2026, the Borrower was in compliance with the financial covenant required by the Senior Unsecur

## 4. 图谱位置与下一跳候选

- 链 `power` / 节点 `power_gen`（独立发电 / 表后电力，状态 now，类型 material）；同层：LEU
  - 图谱状态最后核验：2026-10-19（9 天前；超过 180 天需重新核验）。图谱状态只是线索，用本次实时数据主动质疑它。
  - 下一跳 `HPS-A.TO` Hammond Power Solutions — 变压器（干式/配电）（now，依据 serenity_lead）

## 5. Serenity 公开言论记忆（时点）

- 状态：available；公开帖转述（不是原话，不含订阅内容），帖子编号可在 x.com 查原文。立场 = 当时公开表达的看法，不是持仓记录；2026-10-19 之后是否有新表态未知（沉默不等于卖出）。Serenity 的说法是线索，不是公司事实。
  - 2025-11-20 `1991506376342843438` REAFFIRM/bullish
  - 2026-02-15 `2023061769313542601` WATCH/neutral
  - 2026-03-06 `2030056728650469846` REAFFIRM/bullish
  - 2026-06-15 `2066331049605627951` REAFFIRM/bullish

## 6. 数据质量警告（写进 lens 的 live_data.warnings_addressed）


## 7. 下一步（快速路径）

1. 只在 brief 不够时再读一手文件：`python connectors/live_data.py filing-text --ticker X --latest 10-Q --preset contracts`（≤2 份）。
2. 填写 `lens-draft.json` 中所有 `TODO:` 字段（判断、情景、证伪条件、红队）。
3. `python scripts/serenity_lens.py finish lens-draft.json --md report.md --html report.html` 一步完成计算、校验、渲染与核验。

---

框架声明：本 skill 根据 Serenity 公开发布的内容提炼研究框架，用于回测与研究分析；报告由框架生成，不代表 Serenity 本人观点，亦非投资建议。
