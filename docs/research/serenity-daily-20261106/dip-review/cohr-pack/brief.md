# 研究包：COHR（Coherent Corp.）

> 数据抓取 2026-11-06T03:16:15Z · 连接器 v9.1.0 · 用时 2.54 秒。以下是数据底稿与机械线索，不是结论；判断写进 lens-draft.json 后用 `serenity_lens.py finish` 收尾。

## 1. 对比表（USD 用即期汇率，仅作横向比较）

| 代码 | 价格 | 市值(USD) | 52周回撤 | 1年涨跌 | TTM收入(USD) | 收入同比 | 收入环比 | 毛利率(期末) | 毛利率同比 | P/S | 股本变化 | 机械旗标 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `COHR` | 169.76 USD | 33.44B | -61.4% | +1.8% | 7.91B | +49.9% | +15.9% | 39.1% (2026-09-30) | +2.5pp | 4.2x | +25.3% | dilution, shelf_registration_on_file, unregistered_equity_sale_8k_3_02, beneficial_owner_filings, insider_form4_activity |

## 2. 主体要点

- 最新季度收入：2.37B USD（期末 2026-09-30）；营业利润率 —；现金+短投 1.75B；FCF 跑道 3.8 季。
- 计算市值：33.44B USD（169.76 × 196,958,669 股，股本截至 2026-11-02）。
- 文件雷达 `shelf_registration_on_file`（PB-FIN-01）：Read the S-3/424B5 for size vs market cap and whether an ATM sales agreement exists.
- 文件雷达 `unregistered_equity_sale_8k_3_02`（PB-FIN-03）：Private placement/PIPE: who bought, price vs market, lockup, warrants.
- 文件雷达 `beneficial_owner_filings`（PB-SIG-09）：New 13G/13D filers = institutional discovery or activist; read filer name and %.
- 文件雷达 `insider_form4_activity`（PB-SIG-10）：Classify open-market buys (code P) vs sales/grants; buys after a run-up are rarer signals.
- SEC 全文检索命中（近 25 个月）：supply_concentration 5（主文档 2/5）；customer_concentration 4（主文档 2/4）；capacity_signal 23（主文档 1/6）；going_concern 3（主文档 0/3）

## 2c. 本地财务与公司体检


### 公司体检（通用框架 · company-check-v2）

- 类型路由：**一般经营企业**（依据：SEC SIC 3827 (Optical Instruments & Lenses)）
- 数据：sec_companyfacts，报告期 2026-09-30，币种 USD；证据 E-LIVE-FIN
- 阶段：**常规经营期**（常规口径）；该阶段看：收入增速、利润率、现金转换、估值
- 结果：🚩 4 · 👀 2 · ✅ 8 · ℹ️ 3 · — 0

| 项目 | 数值 | 状态 | 公式 / 说明 |
|---|---|---|---|
| G1 收入同比 | 49.89% | ✅ | 最新报告期累计收入同比（A/H 聚合源）或最新季度同比（SEC/Yahoo） |
| G2 归母净利同比 | 285.60% | ✅ | TTM 净利润 vs 一年前 TTM（SEC；上年为亏损时不计算） |
| P1 毛利率 | 39.14% | ℹ️ | 毛利 / 收入（最新期） |
| P1d 毛利率同比变化 | 2.51pp | ✅ | 最新季度毛利率 − 去年同季 |
| P2 净利率（TTM） | 12.18% | ℹ️ | TTM 净利润 / TTM 收入 |
| P3 ROE（TTM） | 8.50% | ✅ | TTM 归母净利润 / 期末归母权益（未取平均） |
| C1 经营现金流 / 净利润（TTM） | -0.06x | 🚩 | TTM 经营活动现金流净额 / TTM 净利润；长期 <0.7 说明利润没有变成现金 |
| C2 自由现金流（TTM） | -18.34亿 USD | 👀 | TTM 经营现金流 − TTM 资本开支 |
| C3 股权激励费用 / 收入（TTM） | 2.74% | ✅ | TTM 股权激励费用 / TTM 收入；高 SBC 是隐性稀释 |
| B1 资产负债率 | 42.40% | ✅ | 总负债 / 总资产 |
| B2 商誉 / 归母权益 | 39.26% | 👀 | 期末商誉 / 期末归母权益；商誉大意味着减值风险 |
| B3 净现金（现金 − 有息负债） | -22.48亿 USD | ℹ️ | 现金及等价物(+短期存款/短投) − 短借 − 长借 − 应付债券 |
| W1 应收增速 − 收入增速 | 6.28pp | ✅ | 应收账款同比（2025-09-30→2026-09-30）− 收入同比 |
| W2 存货增速 − 收入增速 | 54.78pp | 🚩 | 存货同比（2025-09-30→2026-09-30）− 收入同比 |
| W3 合同负债/预收同比 | 191.53% | ✅ | 期末合同负债 / 去年同期 − 1；上升=客户预付增加（需求领先信号）；大降需追问 |
| D1 股本变化（约一年） | 25.33% | 🚩 | 最新股本 / 4 个观测点前 − 1；每股收入同比 +19.6%；核实融资方式：ATM（持续、无上限，最差）< 溢价可转债 < 定增 < 客户预付/长约（最好） |
| R1 现金跑道（月） | 11.50 月 | 🚩 | 现金及短投 / (−TTM 自由现金流 / 12)；跑道短 = 近期必须融资；融资方式决定稀释好坏：ATM（持续、无上限，最差）< 溢价可转债 < 定增 < 客户预付/长约（最好） |

**估值（USD 口径）**

- 市值 334.36亿 USD · P/E(TTM) 34.7x · P/B 3.0x · P/S 4.2x
- 股本口径：latest reported shares (market_current)

**需核实清单（到定期报告/公告原文确认）**

- [ ] 瓶颈/主题业务占总收入的比例（分部披露；占比小=敞口被稀释）
- [ ] 近 12 个月融资：方式（ATM（持续、无上限，最差）< 溢价可转债 < 定增 < 客户预付/长约（最好））、规模/市值、用途、价格；未用完的 ATM/储架额度
- [ ] 前五大客户集中度与长约条款（期限、可取消比例、预付款）
- [ ] C1 经营现金流 / 净利润（TTM）：到定期报告原文核对口径与一次性因素
- [ ] W2 存货增速 − 收入增速：到定期报告原文核对口径与一次性因素
- [ ] D1 股本变化（约一年）：到定期报告原文核对口径与一次性因素
- [ ] R1 现金跑道（月）：到定期报告原文核对口径与一次性因素

> 机械体检：每项都附公式与阈值（RULES），状态只是“该去看什么”，不是买卖结论。

## 3. 一手文件关键词摘录

### 10-K（提交 2026-08-14，期末 2026-06-30）`E-LIVE-DOC-01`
来源：https://www.sec.gov/Archives/edgar/data/820318/000082031826000020/iivi-20260630.htm

- **customer_deposits** ×9：…y investment (73,998) — — Loss on debt extinguishment 3,056 — 1,978 Increase (decrease) in cash from changes in: Accounts receivable (367,631) (170,444) 60,581 Inventories (1,183,000) (202,728) (23,196) Accounts payable 748,533 217,357 205,044 Contract liabilities (9,307) 3,182 (72,818) Income taxes 18,175 (22,118) 12,251 Accrued compensation and benefits 99,397 62,960 36,894 Other operating net assets (liabilities)
- **sole_source** ×3：…manufacturing process are generally available from several sources. However, in the Industrial segment, we currently purchase several key components and materials used in the manufacture of our products, including exotic materials, crystals, and optics, from sole-source or limited-source suppliers. We also purchase assemblies and turnkey solutions from contract manufacturers, based on our proprietary designs. We rel
- **customer_concentration** ×3：…2026 2025 2024 North America $ 4,633,696 $ 3,564,846 $ 2,622,569 Europe 814,176 698,800 714,282 China 813,377 680,110 621,918 Japan 390,373 390,610 340,863 Rest of World 466,559 475,749 408,056 Total $ 7,118,181 $ 5,810,115 $ 4,707,688 Major Customers One major customer accounted for 20%, 10%, and 10% of consolidated revenue during fiscal 2026, 2025 and 2024, respectively. A second major customer accounted for 12% o
- **export_controls** ×18：…ment of the Treasury, Office of Foreign Assets Control, implementing economic sanctions against designated countries, governments, and persons based on U.S. foreign policy and national security considerations. Foreign governments also have similar import and export controls, sanctions, laws, and regulations. For additional discussion regarding our import, export, and sanctions compliance, see the discussion in Item 
- **default_covenant** ×1：…h maturity and (ii) an interest coverage ratio, as defined in the Credit Agreement, of at least 2.50 to 1.00. Our ability to comply with these provisions may be affected by events beyond our control. Failure to comply with these covenants could result in an event of default, which, if not cured or waived, could accelerate our repayment obligations under the Credit Agreement or the Indenture, as applicable. If such i

### 10-Q（提交 2026-11-04，期末 2026-09-30）`E-LIVE-DOC-02`
来源：https://www.sec.gov/Archives/edgar/data/820318/000082031826000023/iivi-20260930.htm

- **customer_deposits** ×8：…ss — (115,211) Gain on sale of equity investment — (6,726) Loss on debt extinguishment — 3,056 Increase (decrease) in cash from changes in: Accounts receivable (255,278) (66,628) Inventories (737,082) (219,120) Accounts payable 429,824 105,357 Contract liabilities 269,276 (8,022) Income taxes (32,959) 37,221 Accrued compensation and benefits (90,196) (48,206) Other operating net assets (liabilities) (227,111) 40,796
- **export_controls** ×3：…illion recorded within Gain on sale of business in the Condensed Consolidated Statements of Earnings in the third quarter of fiscal 2026. See Note 7. Assets Held-for-Sale and Sale of Businesses for further information. Macroeconomic Conditions - Tariffs and Export Controls In early 2025, the United States implemented significant new tariffs and export restrictions affecting a broad range of countries, commodities an

## 4. 图谱位置与下一跳候选

- 链 `ai_photonics` / 节点 `eml_laser`（EML 激光（可插拔），状态 now，类型 material）；同层：LITE
  - 图谱状态最后核验：2026-10-19（18 天前；超过 180 天需重新核验）。图谱状态只是线索，用本次实时数据主动质疑它。
  - 下一跳 `AXTI` AXT Inc. — InP 衬底（now，依据 serenity_lead）
  - 下一跳 `5802.T` Sumitomo Electric — InP 衬底（now，依据 serenity_lead）
  - 下一跳 `5016.T` JX Advanced Metals — InP 衬底（now，依据 serenity_lead）
  - 下一跳 `4092.T` Nippon Chemical Industrial — 高纯红磷 / 铟 / 6N-7N InP 多晶原料（now，依据 serenity_lead）
  - 下一跳 `5714.T` Dowa Holdings — 高纯红磷 / 铟 / 6N-7N InP 多晶原料（now，依据 serenity_lead）

## 5. Serenity 公开言论记忆（时点）

- 状态：available；公开帖转述（不是原话，不含订阅内容），帖子编号可在 x.com 查原文。立场 = 当时公开表达的看法，不是持仓记录；2026-10-19 之后是否有新表态未知（沉默不等于卖出）。Serenity 的说法是线索，不是公司事实。
  - 2026-02-19 `2024338612356354447` REAFFIRM/bullish
  - 2026-10-10 `2108916977616179207` REAFFIRM/bullish

## 6. 数据质量警告（写进 lens 的 live_data.warnings_addressed）

- `COHR`：sec_stale_series_dropped:operating_income:last_end_2024-06-30_vs_newest_2026-09-30
- `COHR`：sec_stale_series_dropped:buybacks:last_end_2021-06-30_vs_newest_2026-09-30

## 7. 下一步（快速路径）

1. 只在 brief 不够时再读一手文件：`python connectors/live_data.py filing-text --ticker X --latest 10-Q --preset contracts`（≤2 份）。
2. 填写 `lens-draft.json` 中所有 `TODO:` 字段（判断、情景、证伪条件、红队）。
3. `python scripts/serenity_lens.py finish lens-draft.json --md report.md --html report.html` 一步完成计算、校验、渲染与核验。

---

框架声明：本 skill 根据 Serenity 公开发布的内容提炼研究框架，用于回测与研究分析；报告由框架生成，不代表 Serenity 本人观点，亦非投资建议。
