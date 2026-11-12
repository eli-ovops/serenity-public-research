# AIP 实际试跑与人工复核

2026-09-30。结论：**Codex 驱动的 TradingAgents 原生分析流程跑通；投资研究尚未完成。**

## 运行验收

- 15 次模型调用全部完成，24 次真实研究工具调用；预算上限 20 次，未追加调用。
- 行情、基本面、新闻分析 → 多空论证 → 研究经理 → 交易方案 → 三方风险复核 → 最终报告均已返回。
- 工具通过原生 ToolNodes 读取本轮核验并冻结的公开资料。此结果证明工具请求与资料返回贯通，不证明默认实时数据供应商已接通。
- 使用现有 Codex 登录；调用消耗适用的 Codex 额度。请求模型为 gpt-6-sol / medium，实际返回模型标识 UNKNOWN。
- 未读取账户、持仓、密钥或 Cookie，未下单，未安装或修改全局配置。

## 有价值的发现

模型正确指出：AIP 上半年经营现金流为 214.8 万美元，而 ATM 股权融资净所得为 7,254.6 万美元，后者不能算经营造血。收入增长和订单相关指标向好，但收购贡献、收入兑现及稀释仍需分别验证。[公司二季度公告](https://ir.arteris.com/news-releases/news-release-details/arteris-announces-financial-results-second-quarter-and-0)

独立算术复核：经营现金流减资本开支为 125.8 万美元；上半年股权薪酬 / 收入约 25.19%。这些是历史财务事实与计算，不单独构成买卖结论。

## 未接受的判断与原因

原始程序输出 HOLD。本线程**不把它接受为持有、停止加仓或卖出建议**，正式证据状态为「研究未完成」。

1. 配置仅允许两轮工具请求。行情节点先取日线，再请求七项指标，未轮到提示词要求的 get_verified_market_snapshot，就耗尽轮次。因此输入虽然有带日期的价格，报告仍将精确行情标为未知，该缺口又传到后续决策。这是流程配置问题，不是公司利空。
2. 当前充分稀释股数、可复算估值与价格地图尚未闭合；公司事件缺 SEC 直接交叉核对；市场宽度、SOXX 以及 VIX 日变动亦未完整核实。
3. 讨论节点大多重复同一份证据。多个角色一致输出 HOLD，不等于多个独立来源验证；缺证不能自动推导已有持仓应维持不变。

修复优先级：在模型分析前先提供必需的行情核验结果，避免依赖可耗尽的工具轮次；再补股数、估值与事件证据。此次试跑已结束，不为取得更漂亮的标签追加模型调用。

## 资料截点与来源

资料截点：2026-09-30 05:20 UTC；最新已完成美股常规交易日为 9 月 29 日。不同供应商的日变动与日内数据有差异，本轮日线计算采用同一来源，不混用盘后价格。

- [AIP 日线](https://stockanalysis.com/stocks/aip/history/)：9 月 29 日收盘 23.26 美元，+0.61%；20 日均价 22.4135。9 月 21 日至 29 日约 -3.73%。
- [QQQ 日线](https://stockanalysis.com/etf/qqq/history/)：9 月 29 日收盘 737.93，+0.19%；同区间约 -0.48%。
- [Cboe VIX](https://www.cboe.com/tradable-products/vix/)：页面日期 9 月 29 日，16.04；日变动与完整日内结构未独立确认。
- [公司新闻](https://ir.arteris.com/news-events/news-releases)、[公司日历](https://ir.arteris.com/events-and-presentations)、[IR 申报列表](https://ir.arteris.com/financial-information/sec-filings)。未发现已排期事件仅限本轮已查来源，不能视为全部事件门完成。

## 原始证据

同目录 RUN_STATUS.json、state.json、tool_calls.jsonl、calls/*/status.json、public_evidence.json、independent_checks.json 与 RAW_REPORT.md。

本轮仅试跑 AIP，不是全池筛选，不输出账户股数或市场「没有机会」结论。
