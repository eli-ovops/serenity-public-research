# SERENITY_CATALYST_WATCH

Generated: 2026-06-10

Final decision: 以下是未来 3-6 个月 Serenity research-only / governance-only 验证日历模板。它不是交易日历，不创建 scheduler / cron / service / monitor，也不是买入建议、卖出建议、目标价、仓位建议、入场价、退出价、交易计划或 current buy list。

## 使用规则

- due window 是人工研究窗口，不是自动提醒。
- confirmation 必须来自 public filings, company IR, earnings release, SEC / exchange filing, legal docket or reputable public news。
- Serenity X archive 和价格变化只能作线索、crowding 或 asymmetry context，不能清 STOP gate。
- 每条事件只回答一个问题: bottleneck thesis 是否被 primary-source evidence 强化、削弱或仍未验证。

## P1: R7 Risk-Flag Watchlist

| ticker | validation event | due window | evidence needed | confirmation path | invalidation path | primary source to check | current governance status | priority |
|---|---|---|---|---|---|---|---|---|
| TSEM | SiPho contract conversion to recognized revenue | 2026-Q3 to 2026-Q4 | recognized SiPho revenue, segment bridge, or customer-advance-to-revenue conversion | revenue bridge aligns with disclosed commitment path | conversion materially lags or remains undisclosed without credible timing | future 6-K / 20-F / earnings release / IR deck | R7_RISK_FLAG_WATCHLIST | P1 |
| TSEM | customer disclosure / concentration governance | 2026-Q3 to 2026-Q4 | named customer table, 10% customer disclosure, SiPho-specific concentration, receivables | customer base is disclosed, diversified, or repeat/durable | anonymous exposure cannot be governed or concentration worsens | 20-F, 6-K, customer concentration notes, earnings materials | R7_RISK_FLAG_WATCHLIST | P1 |
| TSEM | capacity execution and qualification | 2026-Q3 to 2026-Q4 | Fab/tool/yield/customer qualification milestones, shipment schedule, capex/ramp language | qualified capacity and shipment ramp become public | capacity slips, penalties/refunds, qualification failure, or missed shipment path | 6-K, 20-F, earnings release, capex/ramp commentary | R7_RISK_FLAG_WATCHLIST | P1 |
| TSEM | prepayment accounting and refund mechanics | 2026-Q3 to 2026-Q4 | customer advances/deferred revenue roll-forward, refund liability, payment timing | advances convert transparently without refund/cancellation stress | prepayment refund, delay, missed scheduled payment, or weak refund protection | cash-flow statement, deferred revenue/customer advances notes, 6-K | R7_RISK_FLAG_WATCHLIST | P1 |
| TSEM | GF litigation update | 2026-Q3 to 2026-Q4 | court/ITC status, settlement, injunction risk, damages/licensing impact | dismissal, favorable decision, or immaterial settlement | injunction, material damages/licensing burden, design-around or customer disruption | legal proceedings notes, SEC filings, ITC/court updates | R7_RISK_FLAG_WATCHLIST | P1 |
| FORM | HBM / probe-card demand cadence | 2026-Q3 to 2026-Q4 | DRAM/HBM, probe-card, Foundry & Logic revenue commentary and order cadence | multi-quarter cadence supports structural test-interface demand | demand reverses or appears cycle-pulled-forward | 10-Q / 10-K, earnings release, investor presentation | R7_RISK_FLAG_WATCHLIST | P1 |
| FORM | SK hynix / NVIDIA exposure durability | 2026-Q3 to 2026-Q4 | 10% customer table, customer revenue share, receivables, repeat program signs | named exposure persists with collection quality and repeat demand | major customer weakens, concentration rises, or receivables stress appears | 10-Q / 10-K customer concentration and AR notes | R7_RISK_FLAG_WATCHLIST | P1 |
| FORM | revenue cadence and thesis linkage | 2026-Q3 to 2026-Q4 | explicit HBM/probe-card/CPO/SiPh test revenue or product commentary | revenue growth links to bottleneck rather than generic semicap cycle | thesis revenue linkage remains indirect after refresh | earnings materials, segment/product commentary, acquisition updates | R7_RISK_FLAG_WATCHLIST | P1 |
| FORM | margin / cycle / cash-flow capture | 2026-Q3 to 2026-Q4 | gross margin, operating income, OCF, FCF, working capital | margin and OCF remain supportive while bottleneck revenue grows | margin/OCF deteriorates despite revenue growth | income statement, cash-flow statement, 10-Q / 10-K | R7_RISK_FLAG_WATCHLIST | P1 |

## P2: R6 Priority / Fast Follow-Up

| ticker | validation event | due window | evidence needed | confirmation path | invalidation path | primary source to check | current governance status | priority |
|---|---|---|---|---|---|---|---|---|
| CAMT | HBM / advanced packaging metrology orders | 2026-Q3 to 2026-Q4 | order/backlog detail tied to advanced packaging/HBM inspection | orders are material and repeatable | order momentum stalls or remains too mixed | 20-F / 6-K or equivalent filings, earnings release, IR deck | R6_PRIORITY_MEMO_CONTINUE | P2 |
| CAMT | customer mix and geo risk | 2026-Q3 to 2026-Q4 | customer concentration, geography, Israel/export exposure | concentration and geo risk are governable | concentration or geo/export risk becomes thesis-severing | annual/quarterly filings, risk factors, customer/geography notes | R6_PRIORITY_MEMO_CONTINUE | P2 |
| CAMT | revenue conversion and margin durability | 2026-Q3 to 2026-Q4 | order-to-revenue conversion, gross margin, OCF/FCF | revenue converts with margin/FCF support | orders fail to convert or margin/FCF weakens | earnings release, financial statements, IR deck | R6_PRIORITY_MEMO_CONTINUE | P2 |
| CAMT | full R6 memo readiness | 2026-Q3 | complete Serenity R6 evidence table and STOP-gate audit | R6 memo can support or reject future R7 vote | source gaps persist or STOP gates remain too unclear | local R6 memo package using public filings and IR | R6_PRIORITY_MEMO_CONTINUE | P2 |
| CRDO | AEC / DSP revenue ramp | 2026-Q3 to 2026-Q4 | AEC/DSP revenue, AI networking customer demand, backlog/order commentary | ramp is broad enough and tied to AI interconnect | ramp is narrow, delayed, or one-customer dependent | 10-Q / 10-K, earnings release, IR deck | R6_PRIORITY_MEMO_CONTINUE | P2 |
| CRDO | optical / SiPh / CPO expansion | 2026-Q3 to 2026-Q4 | optical revenue split, SiPh/CPO product traction, production evidence | optical optionality becomes revenue-backed | optical remains narrative or non-material | earnings materials, product revenue commentary, filings | R6_PRIORITY_MEMO_CONTINUE | P2 |
| CRDO | DustPhotonics integration | 2026-Q3 to 2026-Q4 | integration milestones, customer traction, revenue contribution | integration expands bottleneck exposure without margin damage | integration delays or fails to produce commercial evidence | company filings, IR updates, acquisition commentary | R6_PRIORITY_MEMO_CONTINUE | P2 |
| CRDO | customer diversification | 2026-Q3 to 2026-Q4 | customer concentration trend, receivables, top-customer durability | customer base diversifies or concentration is durable | concentration rises or top-customer cadence weakens | 10-Q / 10-K customer and AR disclosures | R6_PRIORITY_MEMO_CONTINUE | P2 |
| CRDO | gross margin durability | 2026-Q3 to 2026-Q4 | gross margin, operating leverage, OCF/FCF bridge | ramp preserves or improves shareholder capture | margin compresses as ramp scales | financial statements, earnings release | R6_PRIORITY_MEMO_CONTINUE | P2 |
| MOD | Airedale / data-center cooling LTA conversion | 2026-Q3 to 2026-Q4 | LTA/backlog conversion, data-center cooling revenue, customer detail | LTA converts into recognized high-quality revenue | LTA/backlog fails to convert or remains vague | 10-Q / 10-K, earnings release, IR deck | R6_PRIORITY_MEMO_CONTINUE | P2 |
| MOD | backlog to revenue | 2026-Q3 to 2026-Q4 | backlog roll-forward, orders, revenue conversion by segment | backlog translates into revenue at acceptable cadence | backlog delays or cancellations emerge | filings, earnings release, backlog/order commentary | R6_PRIORITY_MEMO_CONTINUE | P2 |
| MOD | margin quality | 2026-Q3 to 2026-Q4 | gross margin, segment margin, working capital, OCF | cooling growth supports margin and cash conversion | revenue grows but margin/working capital absorbs economics | income statement, cash-flow statement, segment data | R6_PRIORITY_MEMO_CONTINUE | P2 |
| MOD | capacity execution | 2026-Q3 to 2026-Q4 | manufacturing capacity, delivery cadence, customer acceptance | capacity scales without execution penalty | capacity bottleneck or delivery issue appears | filings, IR updates, earnings commentary | R6_PRIORITY_MEMO_CONTINUE | P2 |
| ONTO | Dragonfly / advanced packaging quality | 2026-Q3 to 2026-Q4 | advanced packaging/HBM revenue bridge, product traction, customer qualification | platform quality links to material revenue | thesis remains broad platform narrative | 10-Q / 10-K, earnings release, IR deck | R6_PRIORITY_MEMO_CONTINUE | P2 |
| ONTO | customer concentration | 2026-Q3 to 2026-Q4 | anonymous top-customer trend, concentration, AR notes | concentration is stable and economically governable | concentration worsens or customer opacity persists | customer concentration and AR disclosures | R6_PRIORITY_MEMO_CONTINUE | P2 |
| ONTO | Rigaku integration / capital allocation | 2026-Q3 to 2026-Q4 | pro forma debt/cash/share bridge, Rigaku ROI, integration updates | capital allocation does not impair shareholder capture | acquisition/financing absorbs economics | 8-K, 10-Q / 10-K, acquisition updates, IR deck | R6_PRIORITY_MEMO_CONTINUE | P2 |
| ONTO | convertible / shareholder-capture risk | 2026-Q3 to 2026-Q4 | convertible terms, capped calls, share count, SBC, FCF | dilution/capital structure remains governable | common-shareholder capture weakens | filings, notes, cash-flow statement, share-count data | R6_PRIORITY_MEMO_CONTINUE | P2 |

## P3: Secondary Watch / Follow-Up

| ticker | validation event | due window | evidence needed | confirmation path | invalidation path | primary source to check | current governance status | priority |
|---|---|---|---|---|---|---|---|---|
| AAOI | 800G ramp to margin | 2026-Q3 to 2026-Q4 | 800G shipments, revenue, gross margin, net income trend | ramp improves margin and customer diversification | ramp stays unprofitable or concentrated | 10-Q / 10-K, earnings release, IR deck | R6_BACKLOG | P3 |
| AAON | BASX / liquid-cooling backlog conversion | 2026-Q3 to 2026-Q4 | backlog conversion, liquid-cooling revenue, capacity ramp | backlog converts with margin quality | capacity/margin problems offset demand | 10-Q / 10-K, earnings release, backlog notes | R6_BACKLOG | P3 |
| NVT | liquid-cooling / systems protection evidence | 2026-Q3 to 2026-Q4 | orders/revenue, Systems Protection margin, data-center mix | data-center exposure is material and margin-accretive | reference design remains non-order proof | 10-Q / 10-K, segment data, earnings release | R6_BACKLOG | P3 |
| ANET | AI networking revenue durability | 2026-Q3 to 2026-Q4 | AI Ethernet revenue, cloud titan demand, margins | AI fabric demand remains durable with margin capture | competition/cycle compresses growth or margins | 10-Q / 10-K, earnings release, IR deck | R6_BACKLOG | P3 |
| CIEN | AI/DCI optical revenue bridge | 2026-Q3 to 2026-Q4 | datacenter interconnect exposure, order cadence, customer mix | AI/DCI optical linkage is material and not generic carrier cycle | linkage remains generic telecom cycle | 10-Q / 10-K, earnings release, IR deck | R6_BACKLOG | P3 |
| PWR | AI factory power backlog quality | 2026-Q3 to 2026-Q4 | data-center power backlog, margin, working capital | AI power demand maps to company economics | backlog is generic infrastructure or working capital-heavy | 10-Q / 10-K, earnings release, backlog commentary | R6_BACKLOG | P3 |

## P4: Blocked / NO-GO / Red-Team Evidence Required Before Upgrade

| ticker | validation event | due window | evidence needed | confirmation path | invalidation path | primary source to check | current governance status | priority |
|---|---|---|---|---|---|---|---|---|
| POET | production customer and revenue proof | only if new public evidence appears in 2026-Q3/Q4 | named production customer, recognized revenue, repeat orders, margin, cash runway | materially different production evidence appears | demo/platform narrative persists or financing dependence worsens | filings, company IR, exchange releases, audited financials | NO-GO | P4 |
| SIVE/SIVEF | named production PO / AI DC revenue split | only if new public evidence appears in 2026-Q3/Q4 | named production customer, production PO, AI data-center revenue split, margin | reference-design narrative becomes production economics | no named customer or no revenue/margin proof | filings, company IR, official releases | BLOCKED | P4 |
| FLNC | hyperscaler order and margin proof | 2026-Q3 to 2026-Q4 | first real hyperscaler order, backlog conversion, gross margin | MSA/reference design converts to orders and margin | no orders, poor margin, project losses persist | 10-Q / 10-K, earnings release, backlog/order disclosures | BLOCKED | P4 |
| SMCI | real orders / cash conversion / governance cleanliness | 2026-Q3 to 2026-Q4 | AI server orders, gross margin, cash conversion, customer acceptance, governance/accounting clarity | blueprint exposure converts into clean economics | order proof absent or governance/cash concerns worsen | SEC filings, earnings release, governance disclosures | BLOCKED | P4 |
| LWLG | production revenue / recurring shipment evidence | only if new public evidence appears in 2026-Q3/Q4 | production revenue, recurring shipments, named/economic customers | platform becomes production-revenue story | demo/materials-platform evidence remains primary | filings, audited financials, company IR | BLOCKED | P4 |
| NOK | company-specific AI infra revenue bridge | 2026-Q3 to 2026-Q4 | AI/DCI/datacenter order or revenue bridge, margin capture | linkage becomes material and company-specific | linkage remains generic telecom cycle | 20-F / 6-K equivalent, earnings release, IR deck | BLOCKED | P4 |

## Direction Anchors

| ticker | validation event | due window | evidence needed | usage |
|---|---|---|---|---|
| NVDA | AI system demand cadence | 2026-Q3 to 2026-Q4 | system demand, GPU/rack cadence, downstream supply stress | validate lane demand only |
| TSM | CoWoS / advanced packaging stress | 2026-Q3 to 2026-Q4 | packaging capacity, foundry demand, lead-time / capex signal | validate packaging lane only |
| AVGO | ASIC / networking pull-through | 2026-Q3 to 2026-Q4 | custom silicon and networking demand | validate networking lane only |
| MU | HBM supply/demand cadence | 2026-Q3 to 2026-Q4 | HBM demand, pricing/capacity, customer cadence | validate HBM lane only |
| ETN | data-center power demand | 2026-Q3 to 2026-Q4 | power equipment backlog/order quality | validate power lane only |
| VRT | power/cooling demand | 2026-Q3 to 2026-Q4 | thermal/power backlog, margin, capacity | validate cooling/power lane only |
| GEV | grid bottleneck demand | 2026-Q3 to 2026-Q4 | grid equipment demand and execution | validate grid lane only |
| COHR | optical component demand | 2026-Q3 to 2026-Q4 | optical components, lasers, transceiver supply stress | validate optical lane only |
| LITE | laser / CPO demand | 2026-Q3 to 2026-Q4 | laser/CPO product demand and margin | validate laser lane only |
| MRVL | DSP / networking silicon demand | 2026-Q3 to 2026-Q4 | AI interconnect silicon demand | validate silicon lane only |
| DELL | AI server deployment | 2026-Q3 to 2026-Q4 | AI server orders/backlog/margin | validate deployment lane only |
| HPE | AI server deployment | 2026-Q3 to 2026-Q4 | AI server orders/backlog/margin | validate deployment lane only |
