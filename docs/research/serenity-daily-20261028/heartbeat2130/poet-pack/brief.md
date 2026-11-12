# 研究包：POET（POET Technologies Inc.）

> 数据抓取 2026-10-28T13:38:15Z · 连接器 v9.1.0 · 用时 3.17 秒。以下是数据底稿与机械线索，不是结论；判断写进 lens-draft.json 后用 `serenity_lens.py finish` 收尾。

## 1. 对比表（USD 用即期汇率，仅作横向比较）

| 代码 | 价格 | 市值(USD) | 52周回撤 | 1年涨跌 | TTM收入(USD) | 收入同比 | 收入环比 | 毛利率(期末) | 毛利率同比 | P/S | 股本变化 | 机械旗标 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `POET` | 5.68 USD | — | -72.7% | -11.8% | 1.71M | +112.3% | +13.2% | — | — | — | +262.5% | acceleration, dilution, shelf_registration_on_file, repeated_prospectus_takedowns, beneficial_owner_filings |

## 2. 主体要点

- 最新季度收入：569,925 USD（期末 2026-06-30）；营业利润率 —；现金+短投 39.96M；FCF 跑道 — 季。
- ⚠️ 市值未计算：foreign private issuer: SEC cover shares are ordinary shares but the US quote is per ADS. Re-run with --adr-ratio <ordinary shares per ADS> (see the deposit agreement / 20-F Item 12).
- 文件雷达 `shelf_registration_on_file`（PB-FIN-01）：Read the S-3/424B5 for size vs market cap and whether an ATM sales agreement exists.
- 文件雷达 `repeated_prospectus_takedowns`（PB-FIN-02）：Serial 424B supplements: an 8-K item 1.01 within 2 days usually marks an underwritten follow-on (read the price vs today); without it, suspect an active ATM and size the overhang.
- 文件雷达 `beneficial_owner_filings`（PB-SIG-09）：New 13G/13D filers = institutional discovery or activist; read filer name and %.
- SEC 全文检索命中（近 25 个月）：supply_concentration 8（主文档 0/6）；atm_program 13（主文档 2/6）；capacity_signal 23（主文档 0/6）；going_concern 10（主文档 2/6）

## 2c. 本地财务与公司体检


### 公司体检（通用框架 · company-check-v2）

- 类型路由：**一般经营企业**（依据：SEC SIC 3674 (Semiconductors & Related Devices)）
- 数据：sec_companyfacts，报告期 2026-06-30，币种 USD；证据 E-LIVE-FIN
- 阶段：**常规经营期**（常规口径）；该阶段看：收入增速、利润率、现金转换、估值
- 结果：🚩 1 · 👀 0 · ✅ 2 · ℹ️ 1 · — 7

| 项目 | 数值 | 状态 | 公式 / 说明 |
|---|---|---|---|
| G1 收入同比 | 112.29% | ✅ | 最新报告期累计收入同比（A/H 聚合源）或最新季度同比（SEC/Yahoo） |
| G2 归母净利同比 | — | — | TTM 净利润 vs 一年前 TTM（SEC；上年为亏损时不计算） |
| P1 毛利率 | — | ℹ️ | 毛利 / 收入（最新期） |
| P2 净利率（TTM） | — | — | TTM 净利润 / TTM 收入 |
| P3 ROE（TTM） | — | — | TTM 归母净利润 / 期末归母权益（未取平均） |
| C1 经营现金流 / 净利润（TTM） | — | — | TTM 经营活动现金流净额 / TTM 净利润；长期 <0.7 说明利润没有变成现金 |
| B1 资产负债率 | 44.06% | ✅ | 总负债 / 总资产 |
| B2 商誉 / 归母权益 | — | — | 期末商誉 / 期末归母权益；商誉大意味着减值风险 |
| W1 应收增速 − 收入增速 | — | — | 应收账款同比（2024-12-31→2025-12-31）− 收入同比；应收账款不足 TTM 收入的 5%，只作参考 |
| W2 存货增速 − 收入增速 | — | — | 存货同比（2024-12-31→2025-12-31）− 收入同比；存货不足 TTM 收入的 5%，只作参考 |
| D1 股本变化（约一年） | 262.50% | 🚩 | 最新股本 / 4 个观测点前 − 1；每股收入同比 -41.4%；核实融资方式：ATM（持续、无上限，最差）< 溢价可转债 < 定增 < 客户预付/长约（最好） |

**估值（USD 口径）**

- 未计算：market cap withheld: foreign private issuer: SEC cover shares are ordinary shares but the US quote is per ADS. Re-run with --adr-ratio <ordinary shares per ADS> (see the deposit agreement / 20-F Item 12).

**需核实清单（到定期报告/公告原文确认）**

- [ ] 瓶颈/主题业务占总收入的比例（分部披露；占比小=敞口被稀释）
- [ ] 近 12 个月融资：方式（ATM（持续、无上限，最差）< 溢价可转债 < 定增 < 客户预付/长约（最好））、规模/市值、用途、价格；未用完的 ATM/储架额度
- [ ] 前五大客户集中度与长约条款（期限、可取消比例、预付款）
- [ ] D1 股本变化（约一年）：到定期报告原文核对口径与一次性因素

> 机械体检：每项都附公式与阈值（RULES），状态只是“该去看什么”，不是买卖结论。

## 3. 一手文件关键词摘录

### 20-F（提交 2026-03-31，期末 2025-12-31）`E-LIVE-DOC-01`
来源：https://www.sec.gov/Archives/edgar/data/1437424/000149315226014253/form20-f.htm

- **customer_deposits** ×4：…liability is recognized in profit or loss. The Company’s financial instruments include cash and cash equivalents, short-term investments, accounts receivable, deposit, accounts payable and accrued liabilities, convertible debt, derivative warrant liability, contract liabilities and Covid-19 government support loans. Derivative financial instruments The Company issued warrants exercisable in a currency other than the
- **sole_source** ×3：…products or manufacturing of our products. We depend on a limited number of suppliers of wafers and components for our integrated photonic solutions, and on contract manufacturers for our optical interposer production activities. Some of these suppliers are sole source suppliers. We typically have not entered into long-term agreements with our suppliers. As a result, these suppliers generally may stop supplying us m
- **going_concern** ×2：…to the audit report for the fiscal year ended December 31, 2023, to express an adverse opinion on the effectiveness of the Company’s internal control over financial reporting because of the existence of a material weakness and (ii) to indicate that there was substantial doubt about the Company’s ability to continue as a going concern. In connection with the audit of the Company’s financial statements for the fiscal 
- **material_weakness** ×4：…an attestation report on the effectiveness of the Company’s internal control over financial reporting as of December 31, 2025. (d) Management Remediation Initiatives As previously reported in the Company’s Form 20-F for the year ended December 31, 2024, a material weakness was identified in internal controls performed by management due to insufficient resources to properly execute the designed controls or perform an
- **export_controls** ×4：…ubjects us to a number of additional risks and challenges, including: ● periodic changes in a specific country’s or region’s economic conditions, such as recession; ● licenses, tariffs and other trade barriers; ● the provision of services may require export licenses; ● environmental regulations; ● certification requirements; ● fluctuations in foreign currency exchange rates; ● inadequate protection of intellectual p
- **at_the_market** ×3：…4.15 Share Sale Agreement for DenseLight Semiconductors PTE, Ltd dated August 20, 2019 (6) 4.16 Omnibus Incentive Plan (12) 4.18 Underwriting Agreement with Maxim Group LLC (10) 4.20 Form of Warrant Certificate, December 4, 2023 (10) 4.23 Equity Distribution Agreement Dated June 29, 2023 (10) 4.24 Equity Distribution Agreement Dated September 1, 2023 (10) 4.27 Warrant indenture with TSX Trust Company, dated February

## 4. 图谱位置与下一跳候选

- 链 `ai_photonics` / 节点 `cpo_packaging`（CPO / 硅光封装，状态 filling，类型 demand）；同层：6451.TW, ASX
  - 图谱状态最后核验：2026-10-19（9 天前；超过 180 天需重新核验）。图谱状态只是线索，用本次实时数据主动质疑它。
  - 下一跳 `AXTI` AXT Inc. — InP 衬底（now，依据 serenity_lead）
  - 下一跳 `5802.T` Sumitomo Electric — InP 衬底（now，依据 serenity_lead）
  - 下一跳 `5016.T` JX Advanced Metals — InP 衬底（now，依据 serenity_lead）
  - 下一跳 `4092.T` Nippon Chemical Industrial — 高纯红磷 / 铟 / 6N-7N InP 多晶原料（now，依据 serenity_lead）
  - 下一跳 `5714.T` Dowa Holdings — 高纯红磷 / 铟 / 6N-7N InP 多晶原料（now，依据 serenity_lead）

## 5. Serenity 公开言论记忆（时点）

- 状态：available；公开帖转述（不是原话，不含订阅内容），帖子编号可在 x.com 查原文。立场 = 当时公开表达的看法，不是持仓记录；2026-10-19 之后是否有新表态未知（沉默不等于卖出）。Serenity 的说法是线索，不是公司事实。
  - 2026-01-14 `2011335633445286396` WATCH/neutral
  - 2026-01-22 `2014444695821472218` REAFFIRM/bullish
  - 2026-03-13 `2032196145263587754` REAFFIRM/bullish
  - 2026-04-27 `2048785899610427809` BEARISH/bearish
  - 2026-04-28 `2049032343974007088` REAFFIRM/bullish
  - 2026-08-30 `2093988125144207710` REAFFIRM/bullish

## 6. 数据质量警告（写进 lens 的 live_data.warnings_addressed）

- `POET`：share_count_older_than_200_days
- `POET`：market_cap_withheld: foreign private issuer: SEC cover shares are ordinary shares but the US quote is per ADS. Re-run with --adr-ratio <ordinary shares per ADS> (see the deposit agreement / 20-F Item 12).
- `POET`：foreign_private_issuer: 20-F/6-K filer; quarterly XBRL may be missing and US quote may be an ADR
- `POET`：financials_from_fallback: yahoo_timeseries (SEC XBRL latest quarter missing)
- `POET`：sec_stale_series_dropped:inventory:last_end_2018-12-31_vs_newest_2025-12-31
- `POET`：sec_stale_series_dropped:goodwill:last_end_2018-12-31_vs_newest_2025-12-31

## 7. 下一步（快速路径）

1. 只在 brief 不够时再读一手文件：`python connectors/live_data.py filing-text --ticker X --latest 10-Q --preset contracts`（≤2 份）。
2. 填写 `lens-draft.json` 中所有 `TODO:` 字段（判断、情景、证伪条件、红队）。
3. `python scripts/serenity_lens.py finish lens-draft.json --md report.md --html report.html` 一步完成计算、校验、渲染与核验。

---

框架声明：本 skill 根据 Serenity 公开发布的内容提炼研究框架，用于回测与研究分析；报告由框架生成，不代表 Serenity 本人观点，亦非投资建议。
