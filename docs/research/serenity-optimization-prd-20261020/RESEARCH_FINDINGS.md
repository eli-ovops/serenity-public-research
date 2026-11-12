# 联网研究：会改变优化方案的事实

研究日2026-10-20。行情截止美国10月19日完整常规盘；公司披露和X读取延伸到10月20日北京时间下午。下列是PRD设计依据，不是重新完成74家选股、11家全部财报全文或最新账户复核。

## 1. GitHub：已有工具能做什么

独立核读7个公开仓库、29个固定commit文件，包含README、许可证与关键实现；原始来源和hash见[GitHub研究](github/GITHUB_RESEARCH.md)及 `github/sources.json`。

- **TradingAgents**：所读上游README标v0.6.0，已存在调用者提供的持仓上下文、输入指纹及固定持有窗口结算。故不能继续说它完全没有持仓能力。但固定窗口研究评级不等于用户实际成交或及时退出。本地README仍记录0.5.2快照试验，图运行完成而研究验收失败；本轮未运行或升级。应保留为有界二审，不能作为决策或绩效真值。[上游PortfolioContext](https://github.com/TauricResearch/TradingAgents/blob/e8f5503e9b86d5c2710b0c76b1f686703968c9df/tradingagents/portfolio.py)
- **edgartools**：财报/XBRL与8-K附件抽取值得作为SEC适配器候选，仍需核期间、单位、修订和原始附件。不能包办海外披露或把解析空值变为零。[财务实现](https://github.com/dgunning/edgartools/blob/c2987cc11090971256aa3c5ffd399eb9b07df470/edgar/financials.py)
- **backtrader / Lean**：订单时点、跳空、限价未成交、费用/滑点与开市状态的语义值得借鉴；不接入实盘。backtrader GPL许可使直接复制需额外评估，优先独立实现有限回放合同；Lean整套系统对当前需求过重。[Lean FillModel](https://github.com/QuantConnect/Lean/blob/61c598b66ed8051d156bba10001eab4f3e86bcb9/Common/Orders/Fills/FillModel.cs)
- **qlib / skfolio**：采用可得时点、连续时间切分、隔离训练和检验的思想；不引入大模型训练。PIT算子不能替我们知道一条新闻当时何时公开；回测没有账户成交也不能变成实际净收益。[qlib PIT](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/data/pit.py)、[skfolio WalkForward](https://github.com/skfolio/skfolio/blob/adc006909df43a854da8406ca5d79335e286f652/src/skfolio/model_selection/_walk_forward.py)
- **LangGraph**：现有TradingAgents已使用；checkpoint只证明流程可以续接，不能证明持仓正确或提醒已送达。暂不再加一层编排。

## 2. 公司财报/披露：11家重点章节及额外Sivers链路

“读取”分别标为原始文件、公开一手解析或仅导航。HTTP下载失败不等于没有公司事实；先前已正常获得的一手解析与原始下载状态分别记录。未把新闻稿当审计意见，未宣称以下11家全篇逐字审读。

| 公司 | 本轮实际读取与事实 | 对优化的直接要求 |
|---|---|---|
| NVDA | 原站10-Q PDF取得，61页文本可定位；重点读资产负债表、客户集中/账期、担保与承诺。应收63.059bn美元；五客户占应收22%/14%/13%/11%/10%，部分投资级客户账期90天至一年；AI云租赁相关担保最大总敞口约3.5bn美元。季度收入增长不能替代这些风险。[10-Q](https://investor.nvidia.com/files/doc_financials/2027/NVDA-2027-Q2-10Q-Final-including-exhibits.pdf) | 现金转换、客户集中、担保和生态融资联动单独建字段；经营增长与市场风险分别评估 |
| TSM | Q3财务表4页和逐字稿重点段落，一手网页/PDF解析可读，原始PDF直接下载403。Q3收入46.72bn美元，毛利66.4%；Q4指引52.3—54.3bn美元。Q3经营现金流919.776bn新台币、购建固定资产443.206bn新台币，不能错作美元。[季度入口](https://investor.tsmc.com/english/quarterly-results/2026/q3)、[财务表](https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-10/3a94d1034b9e6b22446b674f7aaf3d088a12a193/FS.pdf) | 新财报须替换估值版本；单位/币种与季度、累计期间不可混用；旧419参考不能自动重启 |
| CLS | 已读Q2公告及SEC财务表相关段落。Q2收入4.70bn美元，调整EPS2.54；半年CFO767.2m、净资本支出482.2m、FCF285.0m。营运资本中存货占用与应付增加都很大，需解释现金来源。[SEC附件](https://www.sec.gov/Archives/edgar/data/1030894/000103089426000043/cls-20260630prcondensedfs.htm) | EPS、营运资本、资本支出与股本桥同时进入估值；盈利持仓另有保护决定，不能经营强就跳过 |
| TSLA | Q2更新PDF原件取得、33页文本可定位，重点读摘要/财务表和现金流；另读SEC 10-Q现金流。Q2 FCF为-1.092bn美元；半年CFO8.634bn、资本开支8.282bn。季度与半年结论不同。[更新文件](https://assets-ir.tesla.com/tesla-contents/IR/TSLA-Q2-2026-Update.pdf)、[10-Q](https://www.sec.gov/Archives/edgar/data/1318605/000162828026049270/tsla-20260630.htm) | 明确期间、经营/投资/现金口径；10月21日财报事件须入日历，不能只看长期AI叙事 |
| NVT | 从本轮SEC索引定位真实Q2 10-Q后，读取合并销售、分部、有机/并购拆分和现金流。Q2销售1,471.3m美元、同比52.8%；半年持续经营CFO278.7m，包含终止经营后的总CFO268.7m，资本开支57.6m。[10-Q](https://www.sec.gov/Archives/edgar/data/1720635/000162828026051428/nvt-20260630.htm) | 持续/终止经营、并购、分部与总数不能混同；合作新闻不直接等于订单金额 |
| CAMT | Q2一手公告重点段落可读；直接下载有TLS故障，未降低证书校验。收入133.2m美元、同比8%；GAAP净利23.3m、同比-31%，非GAAP净利39.4m、同比+2%；季度CFO12.2m。[公告](https://www.camtek.com/news-and-events/camtek-announces-results-for-the-second-quarter-of-2026/) | 必须解释调整项、收购与收入兑现，不机械使用净利增30%筛掉所有阶段；经营与持仓回撤分开 |
| DPC | 已读官方Q2公告重点财务和IPO/债务口径。收入269m美元、同比34%；GAAP亏损131m，而调整净利6m；现金与IPO后债务清偿不能只抽一个“净现金”数。[Q2公告](https://ir.doncasters.com/news-and-events/news/news-details/2026/DPC-Holdings-Reports-Strong-Second-Quarter-2026-Results/default.aspx) | IPO/MIP/融资、金属成本转嫁、IGT敞口和调整利润桥分开；短上市历史不是错误填150日指标的理由 |
| RXRX | Q2公司披露及10月15日临床/融资一手材料重点读取。新发61.54m股、每股3.25美元，毛额约200m；合作/临床进展与稀释同时成立，预期现金支持到2029不是确定保证。[融资公告](https://ir.recursion.com/news-releases/news-release-details/recursion-announces-pricing-200-million-underwritten-offering)、[临床/合作更新](https://ir.recursion.com/news-releases/news-release-details/recursion-announces-200-million-oversubscribed-follow-offering) | 生物医药单独处理样本、疗效、安全性与读出；新事实不能让风险图无限暂停；融资前后每股模型必须桥接 |
| POET | Q2公告的一手公开解析可读；直接GET仅167字符壳页，不能据HTTP200说读完。收入569,925美元、同比112%，季度亏损11.3m；期末现金/短投796.3m含融资影响。[Q2公告](https://www.poet-technologies.com/news/poet-technologies-reports-second-quarter-2026-results-revenue-up-112-year-over-year-in-sixth-consecutive-quarter-of-sequential-growth) | 低基数增长、融资现金、客户认证/实际订单/收入确认分开；博客与产业合作不能直接升级为收入 |
| SCTX | 官方9月2日Q2公告原始HTML及正文已读。6月底现金/短投43.0m美元，7月IPO/私募净额约140.6m；公司预计支持到2029H1。STX-1150为初始人体阶段，初始临床数据预计2027H1。[公告](https://www.scribetx.com/newsroom/scribe-therapeutics-reports-second-quarter-2026-financial-results-and-recent-corporate-highlights) | 动物数据不当人体疗效；募资与当季现金不同日期；早期临床公司用资金/里程碑框架，不硬套成熟公司ROE与三年复合净利 |

INOD单独展开：Q2收入92.1m美元、同比58%；公司明确250.4m现金/短投包括转付成本相关客户预付款，扣除后约134m。半年CFO164.441m中，应付及其他负债变化贡献135.827m。两者是不同口径，不能简单把135.827m全部叫预付款，也不能把全部现金或半年CFO机械年化为可分配价值。[SEC原始附件](https://www.sec.gov/Archives/edgar/data/903651/000110465926092010/tm2621499d1_ex99-1.htm)、[10-Q](https://www.sec.gov/Archives/edgar/data/903651/000110465926092021/inod-20260630x10q.htm)。PRD必须保留原数、归属、调整及不能解释的余额。

## 3. 自行读取X：发现与核实分开

直接访问公开网页的研究抓取返回403；Chrome扩展通道不可用、原生浏览器出现用户控制变化后未继续输入。随后使用受支持的独立IAB页，**仅阅读公开帖子与公开回复**成功；未读取cookie、token或browser profile文件，未更改关注/通知/订阅/发布状态。网页抓取403仍保留为失败，不宣称修好了该工具。

已全文读取4条主帖：

1. [10月20日Sivers生产订单主帖](https://x.com/aleabitoreddit/status/2112429644033245666)，页面显示最后编辑2026-10-20 06:24:08 UTC。作者把LiDAR从design-win转生产视为商业验证，并推测客户及AI光源扩展。作者另有两条可见补充：客户与终端去向透明度不足；其中一条补充在列表仍截断，不能称全读。已读可见询问与质疑，其中[一条回复](https://x.com/TSR2100/status/2112444897420869871)质疑未给订单规模/条款。
2. [10月19日Sivers资金、资格认证与产能主帖](https://x.com/aleabitoreddit/status/2112102623721505098)，08:44:41 UTC。作者也承认产品/季度产能披露不足，无法精确建模；把700m SEK融资作为扩产资金支持。已展开[公开回复](https://x.com/Dmytro_Lebid/status/2112104699859996753)；回复将1.2bn美元称为积压订单，但公司Q2原文称机会管线。看多和质疑都可能错用数据，不能只给“反方”标签就当证据。
3. [10月19日Lumentum需求/融资风险主帖](https://x.com/aleabitoreddit/status/2112080246895976755)，07:15:46 UTC；07:39:45 UTC实际读取。全文读取其转述和论点，但采访原视频、图片未核，不把作者引语升级为已读采访或不可撤销订单审查。可见作者其他回复/AAOI远期推算有截断，未用于公司估值。

4. [10月19日MSFT/NScale主帖](https://x.com/aleabitoreddit/status/2112130322683072617)，10:34:45 UTC；10月20日07:46:18 UTC实际全文读取，另读5条可见回复。作者认为订单取消可能让已有电力的竞争者受益，但也指出合同执行风险；[一条回复](https://x.com/vonlide53572/status/2112220029584642283)追问替代商是否真有未预订、规格匹配的容量。这是应核的需求转移假说，本轮未取得取消合同及新采购的一手证据，不升级为公司结论。

具体读取范围在 `root/X_READ_LOG.json` 保存。未检索全X、未读完最近7天全部线程/所有回复、未代表全市场情绪。

**已经追到的一手新变化**：Sivers[10月20日公司公告](https://www.sivers-semiconductors.com/press/strategic-lidar-customer-initiates-production-orders-with-sivers-semiconductors/)确认战略LiDAR客户启动滚动生产订单，Q4开始发货，2027项目进入生产；53m—138m美元为客户产品生命周期的估计收入潜力，**不是本次披露的已签订单金额**，客户名字未点名。不得转写为Aeva已确认采购、CPO已规模收入或相同金额积压。

**一手反证/限制**：Sivers[2025年报](https://www.sivers-semiconductors.com/wp-content/uploads/2026/05/Sivers_annualreport_2025_2.pdf)原件取得，86页，重点读PDF76—77页瑞典文审计报告及相关英文风险段。审计未修改整体意见，但明确持续经营重大不确定性，且把财报内控缺陷/错误列作重点审计领域。[8月Q2 CEO信](https://www.sivers-semiconductors.com/2026/08/27/vickram-vathulyas-letter-to-shareholders-interim-report-q2-2026/)确认其后700m SEK融资及订单/认证进展。不能用5月旧风险忽略后来的融资，也不能以融资已完成抹去现金消耗、内控或认证兑现风险。

## 4. 盘面：从单价改为有时间范围的风险诊断

本轮从Nasdaq公开历史接口取得16条完整行情序列：11家公司加QQQ/SPY/RSP/SOXX/XBI。14条各200个日线，DPC81、SCTX61；精确条数见 `root/market_diagnostics.json`。CBOE官方VIX CSV取得。RXRX首次Python TLS EOF后，按已知受支持curl默认严格TLS的一次恢复成功，旧失败留存。

截至Oct19常规盘：QQQ718.36/+1.21%，SPY766.48/+0.42%，RSP213.40/-0.32%，SOXX501.93/+1.73%，XBI147.86/+2.45%；VIX18.44/-7.75%，当日高18.93、低17.39。QQQ距50日均线约-1.15%、距150日约+3.18%；SOXX近20日约-10.26%，距150日约-1.67%。这是反弹与行业压力并存，不支持只凭当天指数变绿就宣布风险解除。

个股近20日相对匹配基准的差异、OHLC收盘位置、量能与均线均已复算。DPC/SCTX没有150日历史，指标留null，不当“不符合所以排除”。SPY一条历史成交量N/A保留缺失，不补0。

Nasdaq接口为公开、未独立验证复权的日线；未核公司行为、全市场涨跌家数、分钟行情或订单簿。RSP/SPY只是宽度代理，不能冒充全市场宽度；均线/相对强度只用于本轮诊断，不直接形成新的买卖规则。源URL、原体与计算脚本均保留，计算完成不等于策略回测。

## 5. 宏观/政策：检验日期与角色，避免旧闻变新风险

- [BLS CPI首页](https://www.bls.gov/cpi/)当前显示9月总体环比0.6%、同比3.7%；核心环比0.3%、同比2.6%。同时列9月非农+29,000（初值）、失业率4.2%。这是实际发布值，不是市场预期；未取得同截点可靠预期时，不能编造“超预期多少”。具体新闻稿直接下载403与官网可见数据分别记。
- [FOMC日历](https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm)下一会议10月27—28日。[9月会议纪要](https://www.federalreserve.gov/monetarypolicy/fomcminutes20260916.htm)为历史正式政策依据，不能当今日新讲话。[2026讲话索引](https://www.federalreserve.gov/newsevents/2026-speeches.htm)本轮显示最新10月14日Bowman讲话；未发现更晚索引项不等于证明所有官员无新讲话。人物、职务和发布日需从当期官方记录核对，不能永久把某个人写死为主席。
- [美国财政部2026日收益率](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value=2026)原件取得；Oct19 2年4.77%、10年5.15%。最初路径404后从已验证正确路径取得；保留两者。
- [白宫简报](https://www.whitehouse.gov/briefings-statements/)和[事实清单](https://www.whitehouse.gov/fact-sheets/)实际检查当前列表。必须按政策相关性分流，不能把所有政治消息变成交易风险；旧日期的科学计划、贸易政策也不能冒充过去24小时的新宣布。PRD要求个人表态、提议、行政文件和生效细则分层。

## 6. 对方案的实质影响

1. 从“研究很多公司再说持有”改成“先维护有版本的决定，再由新证据改变它”；公司好坏、估值回报和仓位风险分别闭合。
2. 稀释、预付款、非GAAP调整、资本开支及现金消耗均是必需数据合同，不以增长和产业瓶颈替代股东每股兑现。
3. X必须保存作者自认的不确定性、来源类别、编辑时间和读取范围；原帖也不是公司结论。今天Sivers案例可以直接作为验收用例。
4. 市场/行业/个股用统一时点、正确基准；缺指标不伪装反证，单一VIX或均线不自动否决。
5. 真正要补的是建议/持仓/规则/触发/送达状态及点时回放。更多代理和工具只在这些模块之外提供有界反证。
