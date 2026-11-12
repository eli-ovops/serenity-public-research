# RXRX / TSM 一手来源与截点

本轮查询截点：2026-10-20 08:19—08:24 UTC（北京时间16:19—16:24，美东04:19—04:24，盘前）。以下为公开来源。本地 Nasdaq 原始报价由本轮 Owner 保存于 `../public/QUOTE_RXRX.json`、`../public/QUOTE_TSM.json`，本协作者只读复用。

| ID | 来源 | 实际核读事实与限制 |
| --- | --- | --- |
| R1 | [RXRX 10月15日8-K](https://www.sec.gov/Archives/edgar/data/1601830/000160183026000128/rxrx-20261015.htm) | 9/30预估现金及受限现金约$561m，含Q3 ATM净$86m；新发61.54m股、$3.25、预计10/16交割；预估现金未经审计/审阅。 |
| R2 | [RXRX 10月15日424B5](https://www.sec.gov/Archives/edgar/data/1601830/000160183026000134/rxrx-finalprosuppxoct2026o.htm) | 募资预计净$187.2m；募后594.731318m股的基数是6/30的533.191318m，明示排除其后ATM已售23.696330m股、RSU等；未来ATM余$213.3m，尚未售不可加到当前股数。招股说明书只写预计交割，不能当交割回执。 |
| R3 | [RXRX 10月15日临床与合作更新](https://ir.recursion.com/news-releases/news-release-details/recursion-announces-200-million-oversubscribed-follow-offering) | REC-4881成人FAP 12周息肉负荷中位下降47%，停药12周后85%维持低于基线；上消化道中位下降55%。REC-1245较高剂量12人中11人疾病控制、2例确认部分缓解；65mg有剂量限制毒性，选45mg扩展。Sanofi option触发$10m，后续里程碑/版税有条件。REC-4881更多数据定于11/2披露，注册性试验拟2027H2且待FDA讨论。小样本、单臂/早期数据不可当批准或确定收入。 |
| R4 | [RXRX Q2 10-Q](https://www.sec.gov/Archives/edgar/data/1601830/000160183026000098/rxrx-20260630.htm)、[Q2业绩附件](https://www.sec.gov/Archives/edgar/data/1601830/000160183026000097/exhibit991-q0226.htm) | H1经营现金净流出$187.048m；H1非GAAP cash operating expense $191m；2026该费用指引<$375m，定义排除合作现金流入和非经常交易成本，不能等同全年实际净烧钱。 |
| R5 | [RXRX IR新闻索引](https://ir.recursion.com/news-events/press-releases) | 本轮打开，页面最上方为10/15三则新闻；索引“未发现更新”只限其展示范围和查询截点，不证明不存在其他披露。未独立找到融资完成公告。 |
| T1 | [TSM Q3业绩入口与Q4指引](https://investor.tsmc.com/english/quarterly-results/2026/q3) | Q3收入$46.72bn；Q4指引收入$52.3–54.3bn、汇率31.8 NTD/USD、毛利65–67%、营业利润率56.5–58.5%。 |
| T2 | [TSM Q3管理报告](https://investor.tsmc.com/chinese/encrypt/files/encrypt_file/reports/2026-10/f83780000ddc0c3b48e57a87eab6814c4ab35058/3Q26%20ManagementReport.pdf) | Q3净利NT$763.06bn、稀释EPS NT$29.43/ADS $4.60，CFO NT$919.77bn、CapEx NT$443.21bn，净现金储备NT$2,985.40bn；季度而非累计。网页工具解析该官方PDF。早前直取另一官方财务PDF 403后未重试。 |
| T2a | [TSM Q3财务表](https://investor.tsmc.com/chinese/encrypt/files/encrypt_file/qr/phase4_reports/2026-10/e18db1d00f041c8d37a90dedbcb150518d8277d9/FS.pdf) | 官方公开页面由网页工具解析：Q3稀释加权普通股25,932m；1 ADS=5股；CFO NT$919,776m、购建固定资产NT$443,206m；与九个月累计列分开读取。该URL不同于先前403的PDF URL。 |
| T3 | [TSM Q3逐字稿](https://investor.tsmc.com/japanese/encrypt/files/encrypt_file/reports/2026-10/eba4fac72873bf546b669bd2b5d973df5c93215d/TSMC%203Q26%20Transcript.pdf) | 全年2026资本预算$60–64bn；2026美元收入增速管理层预期约44%；海外厂未来数年毛利稀释约3–4个百分点，消费/价格敏感领域承压。逐字稿含LSEG版权，仅提取短事实，不复制正文。 |
| T4 | [TSM Q4'25业绩](https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-01/3e49621566a3ca53bdf8aee2586929b666c17fd6/4Q25EarningsRelease.pdf)、[Q1'26业绩](https://pr.tsmc.com/schinese/news/3297)、[Q2'26业绩](https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-07/a80d7933be643644081584087731f73b22ea5a2c/2Q26%20EarningsRelease.pdf) | 每ADS美元EPS依次$3.14、$3.49、$4.31；加Q3 $4.60得TTM $15.54。 |
| T5 | [TSM ADS合同口径](https://investor.tsmc.com/sites/ir/sec-filings/2023%2020F.pdf)、[TSM最新新闻索引](https://pr.tsmc.com/english/latest-news) | 每ADS代表5普通股；本轮新闻索引最上方为10/15 Q3发布，未发现更近重大公司新闻，仅限索引展示和截点。 |
| P1 | [Nasdaq RXRX quote](https://api.nasdaq.com/api/quote/RXRX/info?assetclass=stocks)、[Nasdaq TSM quote](https://api.nasdaq.com/api/quote/TSM/info?assetclass=stocks) | Owner保存原体；RXRX $3.5923/04:10ET，TSM $417.20/04:19ET；盘前，分别昨收$3.61/$420.22。时间/时段不能视作常规盘确认。 |
| P2 | [本地公开日线诊断](../../serenity-optimization-prd-20261020/root/market_diagnostics.json) | 截止10/19常规盘：RXRX 20日-9.068%、相对XBI -2.514个百分点；TSM 20日-5.598%、相对SOXX +4.666个百分点。仅用作结构与匹配行业比较，不作机械止损，也不冒充10/20盘前或收盘。 |

本轮仅查询公开页面，不登录、不读账户或凭据，不运行交易系统。公司站/SEC索引的“最新”是查询范围内的未发现，不是全市场事件不存在的绝对证明。
