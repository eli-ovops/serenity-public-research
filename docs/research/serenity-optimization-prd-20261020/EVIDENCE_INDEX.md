# 证据索引与读取边界

本索引说明本轮实际取得和用于PRD的材料，不把下载、解析、重点阅读、完整研究和有效策略混为一层。

## 历史故障

唯一完整文本审计入口：[REPORT](../serenity-complete-advice-audit-20261020/REPORT.md)、[逐股链条](../serenity-complete-advice-audit-20261020/CASEBOOK.md)、[507条最终答复索引](../serenity-complete-advice-audit-20261020/ALL_FINALS_INDEX.md)、[原文](../serenity-complete-advice-audit-20261020/ALL_FINALS_TEXT.md)、[覆盖验收](../serenity-complete-advice-audit-20261020/VALIDATION.md)。本轮复用，不重新扫描所有会话。93线程/507最终/1186中间回复口径及未覆盖图像、非匹配目录、删除记录/未知原指令边界沿用该正式报告，不扩大为全账户审计。

## GitHub

[固定源码研究](github/GITHUB_RESEARCH.md)与[机器来源清单](github/sources.json)：7仓库29文件，固定commit、获取时间、许可证及SHA-256；`github/evidence/`为实际取得文件。仅静态阅读，没有运行/升级框架；`github/PRD_REVIEW.md`为独立审查而非投资效果背书。

## 公司披露

下面记录重点阅读定位；本次不是11家完整报表及全部附件逐字审核。所有URL及财务摘要见[联网发现](RESEARCH_FINDINGS.md)。`root/web_*.txt`是原生公开网页工具返回的解析/搜索文本，不是官方服务器原始HTTP正文；其内部引用ID只用于追踪，不作为用户网页链接。

| 公司 | 已读材料和定位 | 本地证据层与缺口 |
|---|---|---|
| NVDA | FY27Q2 10-Q财务、应收/客户、租赁担保与投资风险重点段；PDF第3、5、8、14、16、19页及相关检索段 | `public/NVDA_Q2_10Q.pdf`、`.pages.json`及`.txt`；全文件61页可定位≠61页全部精读；release原始GET403 |
| TSM | Q3财务表4页与逐字稿重点段，收入/指引/现金流及资本开支 | `root/web_primary_documents.txt`、`web_primary_financial_details.txt`、`web_financial_sections_review.txt`等原生一手解析；两个原始PDF GET403保留receipt，无本地原件 |
| CLS | Q2公告和SEC财务表，H1/Q2 CFO、capex、FCF与营运资本 | `web_financial_search_a/b.txt`、`web_primary_financial_details.txt`、`web_financial_sections_review.txt`等；原始公告/SEC GET403，无本地原件 |
| TSLA | Q2 Update摘要/财务表与现金流，SEC 10-Q现金流段；IR季度事件导航 | `public/TSLA_Q2_UPDATE.pdf`、`.pages.json/.txt`，33页可定位；`web_primary_financial_details.txt`/`web_target_search_c.txt`的SEC/IR一手解析；IR原始GET403 |
| NVT | 从SEC submissions确定最新10-Q，读分部/有机并购与持续/终止经营现金流 | `public/NVT_SEC_SUBMISSIONS.json`；`web_financial_sections_review.txt`和`web_primary_policy_and_quality.txt`等一手解析；曾猜错一条URL不可用，不使用；真实URL列在发现文件 |
| CAMT | Q2公司公告重点财务/GAAP与非GAAP | `web_financial_search_a.txt`等公司原文解析；直接GET TLS失败，无降低验证/伪称原件 |
| DPC | 官方Q2公告经营/IPO/MIP/债务口径 | `web_financial_search_b.txt`/`web_primary_open_a.txt`等官方正文解析；10-Q原件403，本轮不声称全文已读 |
| RXRX | Q2财务重点段、Oct15融资及临床/合作公告相关段 | `web_financial_search_b.txt`/`web_primary_open_a.txt`/`web_target_search_c.txt`等公司原文解析；多个原始GET403；临床原始患者数据未独立获取 |
| POET | Q2公告收入/亏损/融资现金重点段 | `web_missing_financial_primary.txt`/`web_financial_sections_review.txt`等一手解析；GET200但正文提取仅167字符壳页，原体不当已读完整公告 |
| SCTX | Q2公告管线、资金/IPO与数据预期正文 | `public/SCTX_Q2_RELEASE.raw/.txt`及receipt；公告主体已读，不等于额外完成其所有SEC附件 |
| INOD | Q2 SEC ex99现金/预付款，10-Q客户集中与CFO/营运资本重点段 | `public/INOD_SEC_SUBMISSIONS.json`定位；`web_primary_financial_details.txt`、`web_financial_sections_review.txt`、`web_primary_policy_and_quality.txt`等一手解析；ex99原始GET403 |
| Sivers额外样本 | Oct20生产订单公告全文、Q2 CEO信、2025年报风险/审计重点段（PDF76—77瑞典文） | `public/SIVE_OCT20_PRODUCTION.raw/.txt`、`SIVE_Q2_LETTER.raw/.txt`、`SIVE_ANNUAL_2025.pdf/.pages.json`；86页文件取得，不说年报全篇精读；融资后与旧警告分别记日期 |

## X

[精确读取日志](root/X_READ_LOG.json)：4条@aleabitoreddit主帖全文与选定公开回复；Sivers主帖有公司公告核实，Lumentum采访转述、MSFT/NScale取消与替代采购未获一手确认。续帖截断/未读图像视频单列；不是全部最近7天帖子或全X情绪。该日志为人工整理的实际DOM读取摘要，不冒充原X网页存档/hash。

`SERENITY_FAN_*`两份成功抓取只是二手导航/线索，**没有用于确认作者实际持仓或公司事实**。历史用户桌面附件本轮未取得，不能冒充已读该附件全文。独立浏览页仅公开读取，未读浏览器profile/cookie文件。

## 行情与宏观

- Nasdaq公开历史16序列：`public/HISTORY_*.json/.raw`（RXRX旧TLS失败和一次严格curl恢复receipt均保留）；14×200日线+DPC81/SCTX61，截止Oct19常规盘。RXRX恢复请求保留已解析JSON及原体hash，但原curl正文未留存，不能重新核原体hash；其他有原体的回执独立核对，未伪造恢复原文或重取择优。
- [计算输出](root/market_diagnostics.json)和[计算源码](root/analyze_market.py)：日收益/20日相对收益、SMA及量能。只做本轮未核复权的诊断，不是策略回测/分钟读盘。
- CBOE VIX官方`public/CBOE_VIX_CSV.raw`；Fed日历/Sept纪要原始文件及receipt；Treasury正确路径原始文件与原404均保留。
- BLS CPI/就业首页、Fed讲话和白宫索引本轮公开解析记录在`root/web_macro_search_a.txt`、`web_macro_policy_navigation.txt`、`web_primary_policy_and_quality.txt`等。具体BLS旧稿GET403不改变此前当前首页解析可见事实。
- RSP/SPY是宽度代理，未取全市场涨跌家数；没有共识预期就不报超预期；没有读取所有Fed官员讲话、原始演讲视频或全量特朗普发言。

## 完整性与局限

`root/source_inventory.json`逐条列公开HTTP回执/状态与正文是否语义可用；`root/validation.json`核GitHub29份hash、行情16条/日期/缺失处理、文档FR/NFR/AC编号和本地链接。`root/ARTIFACT_MANIFEST.json`对本次目录文件做封存hash，不把hash当内容真实/财务结论正确的证明。

没有声称：重做74家筛选、11家所有财报全文、4条以外所有X线程、实际收益归因、策略回测成功、新系统已实现或通知已生效。没有账户/券商/secret读取、交易、后台任务、新付费订阅或对外发送。
