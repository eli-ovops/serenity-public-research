# SERENITY R6 FORM / ONTO RESEARCH MEMO

Scope: research-only R6 memo build for FORM and ONTO. This document does not contain buy/sell recommendations, target prices, position sizing, entry timing, trading plans, or current buy lists.

## Executive Summary

- FORM classification: R6_RESEARCH_BACKLOG.
- ONTO classification: R6_RESEARCH_BACKLOG.
- R7 candidates: None under strict R6 rules because unresolved STOP gates remain unclear.
- CAMT status: remains R5 priority / future memo; not part of this R6 full memo body.
- Main reason: both FORM and ONTO have strong R6-quality thesis evidence, but R7 governance requires clearance of customer concentration, valuation crowding, thesis-revenue separation, and for ONTO dilution/capital allocation risk.

## Context Verification

| file | exists_yes_no | path | usage | consequence_if_missing |
|---|---|---|---|---|
| AGENTS.md | YES | /Users/USER/Documents/Codex/2026-05-31/serenity-alpha-research-codex-bitlanglang-bit/project_context/serenity_project_context_bootstrap_20260531_145409/AGENTS.md | safety boundary and evidence discipline | limitation; do not fabricate missing context |
| SERENITY_PROJECT_STATE.md | YES | /Users/USER/Documents/Codex/2026-05-31/serenity-alpha-research-codex-bitlanglang-bit/project_context/serenity_project_context_bootstrap_20260531_145409/SERENITY_PROJECT_STATE.md | state flags and active stops | limitation; do not fabricate missing context |
| SERENITY_SCORECARD_V1_2.md | YES | /Users/USER/Documents/Codex/2026-05-31/serenity-alpha-research-codex-bitlanglang-bit/project_context/serenity_project_context_bootstrap_20260531_145409/SERENITY_SCORECARD_V1_2.md | R6 scorecard fields | limitation; do not fabricate missing context |
| SERENITY_STOP_GATES.md | YES | /Users/USER/Documents/Codex/2026-05-31/serenity-alpha-research-codex-bitlanglang-bit/project_context/serenity_project_context_bootstrap_20260531_145409/SERENITY_STOP_GATES.md | hard STOP gate definitions | limitation; do not fabricate missing context |
| SERENITY_R1_R2_R3_SUMMARY.md | YES | /Users/USER/Documents/Codex/2026-05-31/serenity-alpha-research-codex-bitlanglang-bit/project_context/serenity_project_context_bootstrap_20260531_145409/SERENITY_R1_R2_R3_SUMMARY.md | prior calibration summary | limitation; do not fabricate missing context |
| SERENITY_R3_CLASSIFICATION.csv | YES | /Users/USER/Documents/Codex/2026-05-31/serenity-alpha-research-codex-bitlanglang-bit/project_context/serenity_project_context_bootstrap_20260531_145409/SERENITY_R3_CLASSIFICATION.csv | candidate history and R3 grouping | limitation; do not fabricate missing context |
| SERENITY_R4A_SCOPE.md | YES | /Users/USER/Documents/Codex/2026-05-31/serenity-alpha-research-codex-bitlanglang-bit/project_context/serenity_project_context_bootstrap_20260531_145409/SERENITY_R4A_SCOPE.md | R4-A scope and prohibitions | limitation; do not fabricate missing context |
| R4-A report | YES | /Users/USER/Documents/Codex/2026-05-31/serenity-alpha-research-codex-bitlanglang-bit/research_reports/serenity_r4a_20260531_162546/SERENITY_R4A_DEEP_DIVE_REPORT.md | prior R4-A findings | limitation; do not fabricate missing context |
| R4-A ranking | YES | /Users/USER/Documents/Codex/2026-05-31/serenity-alpha-research-codex-bitlanglang-bit/research_reports/serenity_r4a_20260531_162546/serenity_r4a_ranking.csv | prior classification and scores | limitation; do not fabricate missing context |
| R4-A tracker | YES | /Users/USER/Documents/Codex/2026-05-31/serenity-alpha-research-codex-bitlanglang-bit/research_reports/serenity_r4a_20260531_162546/serenity_candidate_tracker_v2.json | prior evidence/STOP gate summary | limitation; do not fabricate missing context |
| R5 report | YES | /Users/USER/Documents/Codex/2026-05-31/serenity-alpha-research-codex-bitlanglang-bit/research_reports/serenity_r5_20260531_163832/SERENITY_R5_UNDERWRITING_REPORT.md | R5 underwriting findings | limitation; do not fabricate missing context |
| R5 ranking | YES | /Users/USER/Documents/Codex/2026-05-31/serenity-alpha-research-codex-bitlanglang-bit/research_reports/serenity_r5_20260531_163832/serenity_r5_underwriting_ranking.csv | R5 ranking and classification | limitation; do not fabricate missing context |
| R5 tracker | YES | /Users/USER/Documents/Codex/2026-05-31/serenity-alpha-research-codex-bitlanglang-bit/research_reports/serenity_r5_20260531_163832/serenity_candidate_tracker_v3.json | R5 tracker state | limitation; do not fabricate missing context |

## FORM Research Memo

### Basic Profile
- ticker: FORM
- company: FormFactor, Inc.
- business description: Provider of probe cards, probe systems and test/interface technologies across semiconductor characterization, qualification and production test.
- market cap bucket: mid-cap / approximate
- R4-A status: R5_THESIS_UNDERWRITING_CANDIDATE
- R5 status: R6_FULL_THESIS_MEMO_CANDIDATE
- why it reached R6: Narrowest production test bottleneck with explicit HBM/DRAM and networking demand evidence, record revenue and strong revenue-quality translation.
- core thesis: FORM is a narrow semiconductor test chokepoint candidate: if HBM, advanced packaging and networking chips increase wafer/probe complexity, probe-card and production test interface demand can become structurally more important rather than merely cyclical.

### Serenity-Style Thesis
- core chokepoint: probe card / wafer test / known-good-die production interface for HBM, DRAM, networking and advanced packaging.
- why the chokepoint matters: higher pin density, packaging complexity and yield sensitivity increase the cost of weak test infrastructure.
- why this company captures it: official releases cite record DRAM revenue, HBM application demand and Foundry & Logic networking strength.
- evidence supports it: Q1 2026 record revenue, FY2025 HBM-driven revenue, investor day materials, and production test positioning.
- evidence still missing: exact thesis revenue, customer concentration table extraction, recurring cadence, backlog/order terms, cancellability and full FCF bridge.

### Revenue Quality Decomposition
- total revenue: 226.1M USD (10-Q, end 2026-03-28, filed 2026-05-05, us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax)
- segment revenue: PARTIAL / requires full filing and IR table extraction.
- AI / HBM / advanced packaging / process-control thesis-related revenue if disclosed: THESIS_REVENUE_NOT_SEPARATELY_DISCLOSED.
- legacy revenue: not separately quantified in this run.
- one-time revenue: not fully extracted; do not assume repeatability.
- recurring / repeat revenue: qualitative support only; exact repeat cadence not proven.
- gross margin trend: 86.8M USD (10-Q, end 2026-03-28, filed 2026-05-05, us-gaap:GrossProfit)
- operating margin trend: operating income proxy 16.6M USD (10-Q, end 2026-03-28, filed 2026-05-05, us-gaap:OperatingIncomeLoss)
- operating cash flow: 45.0M USD (10-Q, end 2026-03-28, filed 2026-05-05, us-gaap:NetCashProvidedByUsedInOperatingActivities)
- free cash flow: PARTIAL / requires operating cash flow minus capex bridge.
- capex requirement: 15.2M USD (10-Q, end 2026-03-28, filed 2026-05-05, us-gaap:PaymentsToAcquirePropertyPlantAndEquipment)
- working capital pressure: requires inventory/receivables/payables note extraction.
- geographic exposure: requires full latest filing risk factor extraction.
- customer concentration: CUSTOMER_CONCENTRATION_UNKNOWN for R7 purposes.
- product concentration: likely relevant to HBM/advanced packaging, but not fully quantified.

### Customer / Production Validation
- customer logo: not sufficient unless tied to revenue/order terms.
- ecosystem relationship: confirmation only, not production revenue.
- sample: not production revenue.
- demo: not production revenue.
- qualification: meaningful confirmation but not recurring revenue by itself.
- design win: confirmation only unless tied to PO/shipments/revenue.
- purchase order: positive if disclosed with economic terms; not fully extracted.
- production shipment: supported qualitatively by company-level production revenue, but thesis revenue is not separately disclosed.
- recurring revenue: not proven at R7 governance standard.
- long-term supply agreement: ONTO has HBM VPA evidence; FORM requires further extraction.
- prepayment: not fully extracted.
- take-or-pay: not established.
- cancellability: CANCELLABILITY_UNKNOWN.
- backlog quality: BACKLOG_QUALITY_UNKNOWN.

### Competitive Position
- main competitors: large semicap/process-control vendors, probe/test specialists, internal customer alternatives and adjacent inspection/metrology suppliers.
- competition type: both large vendors and specialized peers.
- mission-critical: yes for yield/test/process-control workflows, but mission-critical status must be linked to specific products and customers.
- switching cost: likely medium to high after customer qualification, but exact product-level stickiness remains to be proven.
- pricing power: plausible where qualification and yield impact are strong; not assumed without margin evidence.
- margin compression: possible from customer bargaining, mix, utilization, competition and cycle downturn.

### Cycle vs Structural Growth
- structural_growth_score: 8/10
- cycle_beta_score: 6/10
- uncertainty: MEDIUM: HBM/test complexity is structural, but memory/foundry capex cycle can inflate current strength.

### Shareholder Capture
- shareholder_capture_score: 8/10
- main_capture_risk: Customer concentration and cycle/mix pressure could weaken capture despite cleaner dilution profile.
- dilution: ONTO unresolved due convertible notes; FORM no major issue found in automated pass.
- debt: requires latest balance sheet review.
- SBC: requires detailed proxy/10-K extraction.
- capex pressure: requires FCF bridge.
- margin/cash flow pressure: see revenue quality decomposition.

### Hard STOP Gate Audit Summary

| gate | triggered_yes_no_unclear | evidence | consequence | R6_status |
|---|---|---|---|---|
| STOP-REV0 | NO | Company has operating revenue from filed/public evidence. | Clear for continued scoring. | CLEAR |
| STOP-DEMO-NOT-PRODUCTION | NO | Primary thesis evidence is production revenue/order/qualification context, not demo/sample/MoU alone. | Clear for continued scoring. | CLEAR |
| STOP-CUSTOMER-UNCLEAR | NO | Customer/product relationships are supported by official releases, but details vary by ticker. | Clear for continued scoring. | CLEAR |
| STOP-DILUTION | NO | Check share issuance, convertible financing, and SBC impact. | Clear for continued scoring. | CLEAR |
| STOP-SOCIAL-HYPE | NO | No social-media evidence was used as positive support. | Clear for continued scoring. | CLEAR |
| STOP-CUSTOMER-CONCENTRATION | UNCLEAR | Full 10% customer and customer concentration tables remain necessary for R7 governance. FORM says customer >10% breakdown is posted on IR, but this run did not fully extract the table. | Cannot enter R7 directly under R6 rules; must remain R6 backlog/continue until cleared. | R6_RESEARCH_BACKLOG_REQUIRED |
| STOP-CHINA-GEO | UNCLEAR | Global semicap supply chain, China/Taiwan/export and manufacturing geography risk require full risk-factor extraction. | Cannot enter R7 directly under R6 rules; must remain R6 backlog/continue until cleared. | R6_RESEARCH_BACKLOG_REQUIRED |
| STOP-VALUATION-OVERHEAT | UNCLEAR | No target price or trading signal used; crowding/expectation risk remains unresolved. | Cannot enter R7 directly under R6 rules; must remain R6 backlog/continue until cleared. | R6_RESEARCH_BACKLOG_REQUIRED |
| STOP-GOING-CONCERN | NO | No going-concern issue found in automated pass. | Clear for continued scoring. | CLEAR |
| STOP-SHAREHOLDER-NOT-CAPTURED | NO | Requires margin, FCF, dilution/debt and capital allocation evidence. | Clear for continued scoring. | CLEAR |
| STOP-GOVERNANCE-ACCOUNTING | NO | No accounting/governance blocker found in automated pass. | Clear for continued scoring. | CLEAR |
| STOP-LINKAGE-WEAK | NO | FORM/ONTO have direct linkage to test/process-control complexity; thesis revenue still not fully separated. | Clear for continued scoring. | CLEAR |

### Scorecard Summary
- opportunity_score: 37
- evidence_score: 39
- survivability_score: 39
- penalty_score: 17
- final_research_score: 85.2
- confidence_level: MEDIUM_HIGH
- R6 classification: R6_RESEARCH_BACKLOG

### Red Team
- if thesis wrong: the likely error is confusing cyclical semicap strength with durable AI-specific bottleneck capture.
- semiconductor cycle vs AI-specific: mixed; thesis requires isolating HBM/advanced packaging/process-control revenue.
- fully priced: valuation crowding is unresolved; no target price used.
- customer concentrated: unresolved until full customer table extraction.
- gross margin pressure: possible from mix, utilization, customer bargaining and competition.
- geopolitical/export risk: requires full risk factor extraction across China/Taiwan/export chain exposure.
- inventory cycle risk: customer digestion can defer demand.
- equipment capex cycle risk: WFE/memory/foundry capex cycle can distort demand.
- competitive replacement risk: large equipment/test vendors and qualified alternatives may compete.
- shareholder capture unclear: unresolved details remain before R7 governance.
- R6 materials still insufficient: yes, because exact thesis revenue, concentration, terms/cancellability and FCF bridge remain incomplete.

## ONTO Research Memo

### Basic Profile
- ticker: ONTO
- company: Onto Innovation Inc.
- business description: Provider of process control, inspection, metrology and related systems across semiconductor manufacturing.
- market cap bucket: mid-cap to large-cap / approximate
- R4-A status: R5_THESIS_UNDERWRITING_CANDIDATE
- R5 status: R6_FULL_THESIS_MEMO_CANDIDATE
- why it reached R6: Best combination of explicit HBM/process-control evidence, customer qualification, volume purchase agreement evidence and broad platform relevance; convertible financing and valuation crowding remain R6 risks.
- core thesis: ONTO is a process-control platform candidate: AI/HBM, 2.5D logic, advanced nodes and heterogeneous integration increase metrology/inspection complexity, making yield/process-control capability more strategic.

### Serenity-Style Thesis
- core chokepoint: process control / metrology / inspection for HBM, 2.5D logic, gate-all-around and advanced-node manufacturing.
- why the chokepoint matters: tighter process windows and heterogeneous integration increase metrology, bump inspection and yield-control burden.
- why this company captures it: official releases cite Dragonfly G5 qualification at 2.5D logic and HBM customers, Atlas G6 selection and HBM VPA evidence.
- evidence supports it: Q1 2026 record revenue, FY2025 HBM VPA, Rigaku partnership and SEC-hosted earnings exhibit.
- evidence still missing: exact thesis revenue, customer concentration, purchase agreement terms/cancellability, post-convert dilution/capital allocation and full FCF bridge.

### Revenue Quality Decomposition
- total revenue: 291.9M USD (10-Q, end 2026-03-31, filed 2026-05-05, us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax)
- segment revenue: PARTIAL / requires full filing and IR table extraction.
- AI / HBM / advanced packaging / process-control thesis-related revenue if disclosed: THESIS_REVENUE_NOT_SEPARATELY_DISCLOSED.
- legacy revenue: not separately quantified in this run.
- one-time revenue: not fully extracted; do not assume repeatability.
- recurring / repeat revenue: qualitative support only; exact repeat cadence not proven.
- gross margin trend: 146.4M USD (10-Q, end 2026-03-31, filed 2026-05-05, us-gaap:GrossProfit)
- operating margin trend: operating income proxy 33.5M USD (10-Q, end 2026-03-31, filed 2026-05-05, us-gaap:OperatingIncomeLoss)
- operating cash flow: 26.3M USD (10-Q, end 2026-03-31, filed 2026-05-05, us-gaap:NetCashProvidedByUsedInOperatingActivities)
- free cash flow: PARTIAL / requires operating cash flow minus capex bridge.
- capex requirement: 3.6M USD (10-Q, end 2026-03-31, filed 2026-05-05, us-gaap:PaymentsToAcquirePropertyPlantAndEquipment)
- working capital pressure: requires inventory/receivables/payables note extraction.
- geographic exposure: requires full latest filing risk factor extraction.
- customer concentration: CUSTOMER_CONCENTRATION_UNKNOWN for R7 purposes.
- product concentration: likely relevant to HBM/advanced packaging, but not fully quantified.

### Customer / Production Validation
- customer logo: not sufficient unless tied to revenue/order terms.
- ecosystem relationship: confirmation only, not production revenue.
- sample: not production revenue.
- demo: not production revenue.
- qualification: meaningful confirmation but not recurring revenue by itself.
- design win: confirmation only unless tied to PO/shipments/revenue.
- purchase order: positive if disclosed with economic terms; not fully extracted.
- production shipment: supported qualitatively by company-level production revenue, but thesis revenue is not separately disclosed.
- recurring revenue: not proven at R7 governance standard.
- long-term supply agreement: ONTO has HBM VPA evidence; FORM requires further extraction.
- prepayment: not fully extracted.
- take-or-pay: not established.
- cancellability: CANCELLABILITY_UNKNOWN.
- backlog quality: BACKLOG_QUALITY_UNKNOWN.

### Competitive Position
- main competitors: large semicap/process-control vendors, probe/test specialists, internal customer alternatives and adjacent inspection/metrology suppliers.
- competition type: both large vendors and specialized peers.
- mission-critical: yes for yield/test/process-control workflows, but mission-critical status must be linked to specific products and customers.
- switching cost: likely medium to high after customer qualification, but exact product-level stickiness remains to be proven.
- pricing power: plausible where qualification and yield impact are strong; not assumed without margin evidence.
- margin compression: possible from customer bargaining, mix, utilization, competition and cycle downturn.

### Cycle vs Structural Growth
- structural_growth_score: 8/10
- cycle_beta_score: 7/10
- uncertainty: MEDIUM_HIGH: process-control complexity is structural, but WFE cycle and large capital allocation events cloud purity.

### Shareholder Capture
- shareholder_capture_score: 7/10
- main_capture_risk: Convertible notes and Rigaku investment require R7-level dilution/debt/capital allocation audit.
- dilution: ONTO unresolved due convertible notes; FORM no major issue found in automated pass.
- debt: requires latest balance sheet review.
- SBC: requires detailed proxy/10-K extraction.
- capex pressure: requires FCF bridge.
- margin/cash flow pressure: see revenue quality decomposition.

### Hard STOP Gate Audit Summary

| gate | triggered_yes_no_unclear | evidence | consequence | R6_status |
|---|---|---|---|---|
| STOP-REV0 | NO | Company has operating revenue from filed/public evidence. | Clear for continued scoring. | CLEAR |
| STOP-DEMO-NOT-PRODUCTION | NO | Primary thesis evidence is production revenue/order/qualification context, not demo/sample/MoU alone. | Clear for continued scoring. | CLEAR |
| STOP-CUSTOMER-UNCLEAR | NO | Customer/product relationships are supported by official releases, but details vary by ticker. | Clear for continued scoring. | CLEAR |
| STOP-DILUTION | UNCLEAR | Check share issuance, convertible financing, and SBC impact. ONTO announced upsized $1.3B 0.00% convertible notes due 2031, so dilution/debt audit remains unresolved. | Cannot enter R7 directly under R6 rules; must remain R6 backlog/continue until cleared. | R6_RESEARCH_BACKLOG_REQUIRED |
| STOP-SOCIAL-HYPE | NO | No social-media evidence was used as positive support. | Clear for continued scoring. | CLEAR |
| STOP-CUSTOMER-CONCENTRATION | UNCLEAR | Full 10% customer and customer concentration tables remain necessary for R7 governance. | Cannot enter R7 directly under R6 rules; must remain R6 backlog/continue until cleared. | R6_RESEARCH_BACKLOG_REQUIRED |
| STOP-CHINA-GEO | UNCLEAR | Global semicap supply chain, China/Taiwan/export and manufacturing geography risk require full risk-factor extraction. | Cannot enter R7 directly under R6 rules; must remain R6 backlog/continue until cleared. | R6_RESEARCH_BACKLOG_REQUIRED |
| STOP-VALUATION-OVERHEAT | UNCLEAR | No target price or trading signal used; crowding/expectation risk remains unresolved. | Cannot enter R7 directly under R6 rules; must remain R6 backlog/continue until cleared. | R6_RESEARCH_BACKLOG_REQUIRED |
| STOP-GOING-CONCERN | NO | No going-concern issue found in automated pass. | Clear for continued scoring. | CLEAR |
| STOP-SHAREHOLDER-NOT-CAPTURED | UNCLEAR | Requires margin, FCF, dilution/debt and capital allocation evidence. | Cannot enter R7 directly under R6 rules; must remain R6 backlog/continue until cleared. | R6_RESEARCH_BACKLOG_REQUIRED |
| STOP-GOVERNANCE-ACCOUNTING | NO | No accounting/governance blocker found in automated pass. | Clear for continued scoring. | CLEAR |
| STOP-LINKAGE-WEAK | NO | FORM/ONTO have direct linkage to test/process-control complexity; thesis revenue still not fully separated. | Clear for continued scoring. | CLEAR |

### Scorecard Summary
- opportunity_score: 35
- evidence_score: 41
- survivability_score: 35
- penalty_score: 18
- final_research_score: 81.6
- confidence_level: MEDIUM_HIGH
- R6 classification: R6_RESEARCH_BACKLOG

### Red Team
- if thesis wrong: the likely error is confusing cyclical semicap strength with durable AI-specific bottleneck capture.
- semiconductor cycle vs AI-specific: mixed; thesis requires isolating HBM/advanced packaging/process-control revenue.
- fully priced: valuation crowding is unresolved; no target price used.
- customer concentrated: unresolved until full customer table extraction.
- gross margin pressure: possible from mix, utilization, customer bargaining and competition.
- geopolitical/export risk: requires full risk factor extraction across China/Taiwan/export chain exposure.
- inventory cycle risk: customer digestion can defer demand.
- equipment capex cycle risk: WFE/memory/foundry capex cycle can distort demand.
- competitive replacement risk: large equipment/test vendors and qualified alternatives may compete.
- shareholder capture unclear: unresolved details remain before R7 governance.
- R6 materials still insufficient: yes, because exact thesis revenue, concentration, terms/cancellability and FCF bridge remain incomplete.

## FORM vs ONTO Pairwise Comparison

| comparison_dimension | FORM | ONTO | winner | confidence | notes |
|---|---|---|---|---|---|
| AI / HBM / advanced packaging exposure directness | Direct HBM/DRAM probe-card and networking test demand in official releases. | Direct HBM/2.5D logic/process-control qualification and VPA evidence. | TIE | MEDIUM_HIGH | FORM is narrower; ONTO is broader process-control platform. |
| thesis revenue separability | Better qualitative separation via DRAM/HBM and probe-card production language, but exact thesis revenue not disclosed. | HBM VPA helps, but platform revenue remains mixed with broader process control. | FORM | MEDIUM | Neither discloses clean thesis revenue; no forced estimate. |
| customer validation | Strong production demand evidence but full customer concentration table not extracted. | HBM manufacturer VPA and customer qualifications are strong, but named customer economics incomplete. | ONTO | MEDIUM | ONTO has stronger explicit customer-event evidence; terms still incomplete. |
| recurring / repeat revenue quality | Probe cards may have repeat/consumable-like production cadence, but not fully quantified. | Equipment/platform purchases and VPA suggest recurring opportunity, but equipment lumpiness remains. | FORM | MEDIUM | FORM likely cleaner repeat production cadence. |
| gross margin / cash flow steadiness | Record revenue and margin improvement evidence; still cycle-sensitive. | Strong revenue but large Rigaku investment/convertible financing complicates cash/capital view. | FORM | MEDIUM | Needs full FCF bridge in R7 governance. |
| semiconductor cycle beta contamination | Memory/foundry cycle can inflate HBM test demand. | WFE/process-control cycle can contaminate advanced-node growth. | TIE | MEDIUM | Both have structural plus cyclical mix. |
| valuation fully priced risk | Record revenue and HBM narrative can attract crowding. | HBM/process-control/Rigaku/convertible narrative can attract more crowding. | FORM | LOW_MEDIUM | Winner means lower contamination risk, not a valuation conclusion. |
| customer concentration transparency | Company says >10% customer breakdown is posted on IR, but not fully extracted here. | Customer references and VPA are strong, but concentration table still needed. | FORM | LOW_MEDIUM | Both remain unclear under R6 rules. |
| shareholder capture clarity | Cleaner due less visible dilution/debt issue and direct production test economics. | Strong business but convertible notes and Rigaku investment require capital allocation audit. | FORM | MEDIUM_HIGH | Shareholder capture drives FORM edge. |
| Serenity-style misclassified bottleneck | More likely narrow test bottleneck misclassified as generic semicap beta. | More visible process-control growth platform; still high quality. | FORM | MEDIUM | FORM is narrower and more falsifiable. |

## Final R6 Decision

### FORM
- R6 classification: R6_RESEARCH_BACKLOG
- main reason: Best narrow bottleneck evidence, but R6 rules block R7 while customer concentration/geography/valuation crowding remain unclear.
- main risk: HBM/probe-card strength may be cyclical or concentrated, with insufficient R7-grade customer concentration and recurrence evidence.
- next action: clear customer concentration, geography/export exposure, valuation crowding, repeat revenue and FCF bridge before R7 governance.

### ONTO
- R6 classification: R6_RESEARCH_BACKLOG
- main reason: Very strong process-control/HBM evidence, but convertible financing, customer concentration, thesis-revenue separation and valuation crowding remain unresolved.
- main risk: Strong platform thesis may be partially priced and shareholder capture is complicated by convertible financing and capital allocation needs.
- next action: clear convertible/dilution, Rigaku capital allocation, customer concentration, VPA terms/cancellability, valuation crowding and thesis-revenue split before R7 governance.

### CAMT
- status: keep as R5 priority / not part of R6 full memo.

## Limitations
- Some context or output file absence would be marked in the context table; current critical files were available.
- Public evidence was collected from SEC/EDGAR, company IR pages/releases and public transcript/index sources; full R7 governance still needs manual table extraction.
- Thesis revenue was not separately disclosed for FORM or ONTO; no forced estimates were made.
- Customer concentration, backlog/order terms, take-or-pay and cancellability remain unresolved.
- No buy/sell recommendation, target price, position sizing, entry timing, trading plan or current buy list was produced.
