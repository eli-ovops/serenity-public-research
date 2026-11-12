# SERENITY R7 GOVERNANCE THRESHOLD RECALIBRATION

Generated: 2026-06-04T12:48:15+08:00
Project: Serenity Alpha Research
Task: SERENITY_R7_GOVERNANCE_THRESHOLD_RECALIBRATION_MULTI_AGENT
Mode: research-only governance recalibration; public/local evidence only; no brokerage, secrets, scheduler, cron, service, monitor, trade output, target price, position sizing, entry point, or current buy list.

Mandatory statement: None of these categories is a buy recommendation.

## Final Decision

R7 is recalibrated from a near-perfect underwriting gate into a research-governance watchlist gate. R7 can include risk-flag watchlist candidates if P0 hard stops are absent, evidence is real, risks are named, and confirmation/invalidation paths are explicit.

New R7 outcome under this recalibration:

- R7_CLEAN_WATCHLIST: none.
- R7_RISK_FLAG_WATCHLIST: TSEM, FORM.
- R7_SPECULATIVE_RIGHT_TAIL: none.
- R6_PRIORITY_MEMO_CONTINUE: ONTO, CAMT.
- BLOCKED / NO-GO: LWLG remains BLOCKED; POET remains NO-GO.

This is not a current buy list, not investment advice, and not a trade plan.

## What Is Hard STOP Versus Watchlist Risk Flag

Hard STOP means the evidence base is not reliable enough for R7 governance: no material commercial revenue path, demo-only thesis, social-hype-driven thesis, weak thesis linkage, going-concern risk, or governance/accounting impairment.

Watchlist risk flag means the evidence base is real but unresolved risks remain. Customer concentration, customer opacity, prepayment not revenue, unknown contract cancellability, capacity execution, geo/export exposure, valuation/crowding, dilution complexity, and shareholder-capture uncertainty can enter R7 only as R7_RISK_FLAG_WATCHLIST, not as clean R7.

## Allowed Uncertainty In R7

R7 may allow:

- named or governed customer concentration;
- anonymous customer risk when filed contracts/revenue/prepayments are real and tracked;
- contract-quality uncertainty if the memo does not treat contract headlines as recognized revenue;
- capacity execution uncertainty when it is the actual bottleneck being monitored;
- valuation/crowding risk as a qualitative risk-only review;
- dilution or capital-structure complexity if survival and shareholder capture are not structurally impaired;
- geo/export exposure if it is monitorable and not sanction-linked or thesis-severing.

## Uncertainty That Blocks R7

R7 remains blocked by:

- going concern or acute liquidity stress;
- unreliable filings, accounting, audit, internal-control, or governance concerns;
- thesis linkage that stays indirect or speculative;
- demo/platform/MoU evidence without production revenue or credible material revenue path;
- social-media or price-momentum evidence used as positive support;
- no material operating revenue path tied to the thesis;
- financing/dilution that overwhelms common-shareholder capture;
- export/sanction/geopolitical risk that materially impairs operations or evidence reliability.

## New Classification System

1. R7_CLEAN_WATCHLIST: Evidence strong, no unresolved critical risk flags, suitable for governance watchlist.
2. R7_RISK_FLAG_WATCHLIST: Evidence strong enough for watchlist, but material risks remain. Not clean. Must be monitored.
3. R7_SPECULATIVE_RIGHT_TAIL: Right-tail setup exists, evidence incomplete, but not demo-only, hype-only, or no-revenue without credible path. Must be explicitly speculative.
4. R6_PRIORITY_MEMO_CONTINUE: Research quality high but not ready for R7 even with risk flags.
5. R6_BACKLOG: Evidence incomplete; wait for future filings, events, or customer disclosure.
6. BLOCKED: A critical blocker prevents advancement, but future evidence may reopen.
7. NO-GO: Permanent or near-permanent caution under current framework.

None of these categories is a buy recommendation.

## Gate Reclassification

| gate | old_type | new_type_P0_P1_P2 | blocks_R7_yes_no_conditional |
| --- | --- | --- | --- |
| STOP-REV0 | Hard STOP / blocks high evidence status | P0_HARD_STOP when no paid customer, no material operating revenue, or no credible material revenue path tied to the thesis; otherwise P1 if thesis revenue mix is unclear | CONDITIONAL |
| STOP-DEMO-NOT-PRODUCTION | Hard STOP / cannot receive high evidence status | P0_HARD_STOP if thesis is mainly demo/platform/MoU; P1_WATCHLIST_RISK_FLAG if demos are only supplemental to filed revenue/customer evidence | CONDITIONAL |
| STOP-CUSTOMER-UNCLEAR | Blocks R5/R7 readiness when uncleared | P1_WATCHLIST_RISK_FLAG | NO, unless opacity prevents basic commercial validation |
| STOP-DILUTION | Severe survivability/shareholder-capture penalty | P1_WATCHLIST_RISK_FLAG; escalates to P0_HARD_STOP if dilution or financing threatens survival or common-shareholder capture | CONDITIONAL |
| STOP-SOCIAL-HYPE | Social heat can only be crowding risk | P0_HARD_STOP if positive thesis relies on social-media heat; P2_MONITORING_ITEM if social heat is only crowding risk | CONDITIONAL |
| STOP-CUSTOMER-CONCENTRATION | Often treated as hard block | P1_WATCHLIST_RISK_FLAG | NO for R7_RISK_FLAG_WATCHLIST; YES for R7_CLEAN_WATCHLIST if material and unresolved |
| STOP-CHINA-GEO | Penalize or block if exposure uncontrollable | P1_WATCHLIST_RISK_FLAG; P0_HARD_STOP only for sanction-linked, export-control-impaired, or structurally uncontrollable exposure | CONDITIONAL |
| STOP-VALUATION-OVERHEAT | Research priority cap | P1_WATCHLIST_RISK_FLAG | NO for risk-flag R7; YES for clean R7 if evidence is thin and expectations dominate |
| STOP-GOING-CONCERN | Blocked until resolved by filings | P0_HARD_STOP | YES |
| STOP-SHAREHOLDER-NOT-CAPTURED | Score cap/downgrade | P1_WATCHLIST_RISK_FLAG | NO for risk-flag R7; YES if economics demonstrably bypass common shareholders |
| STOP-GOVERNANCE-ACCOUNTING | Blocked or heavily penalized | P0_HARD_STOP when evidence reliability is impaired; P1 if ordinary governance risk only | CONDITIONAL, usually YES when triggered |
| STOP-LINKAGE-WEAK | Cannot remain priority status | P0_HARD_STOP | YES |
| STOP-CONTRACT-CANCELLABILITY-UNKNOWN | Treated as hard unresolved contract-quality gate in TSEM R6 | P1_WATCHLIST_RISK_FLAG | NO for R7_RISK_FLAG_WATCHLIST; YES for R7_CLEAN_WATCHLIST |
| STOP-PREPAYMENT-NOT-REVENUE | Prevented R7 conversion of headline into revenue-quality proof | P1_WATCHLIST_RISK_FLAG | NO for risk-flag R7; YES if memo treats prepayment as recognized revenue |
| STOP-CAPACITY-EXECUTION-UNPROVEN | Critical unresolved execution gate | P1_WATCHLIST_RISK_FLAG | NO for risk-flag R7; YES for clean R7 or if capacity failure is evidenced |

## Candidate Reclassification

| ticker | old_classification | new_classification | reason | does_this_mean_buy_yes_no |
| --- | --- | --- | --- | --- |
| TSEM | R6_PRIORITY_MEMO_CONTINUE; S-A-B-C downgraded S to A / Medium; no R7 candidate under prior strict gate | R7_RISK_FLAG_WATCHLIST | Filed operating revenue, direct SiPho contract/prepayment evidence, and clear AI optical-interconnect bottleneck linkage are strong enough for governance watchlist status. It is not clean because prepayment is not revenue, contract terms are undisclosed, SiPho customer concentration is anonymous, capacity execution is unproven, valuation/crowding is high, and GF litigation remains a monitor. | NO |
| FORM | BLOCKED after R6-R1 due explicit customer concentration; S-A-B-C A / Medium-High | R7_RISK_FLAG_WATCHLIST | Customer concentration is explicit and material, but it is named, filing-backed, and paired with real revenue, HBM/probe-card/test-interface evidence, operating cash flow, and clear bottleneck relevance. Under the recalibrated framework it blocks clean R7, not risk-flag R7. | NO |
| ONTO | R6_RESEARCH_BACKLOG after R6-R1; S-A-B-C B / Medium | R6_PRIORITY_MEMO_CONTINUE | ONTO has real process-control/metrology evidence, revenue, and advanced-packaging/HBM linkage, but multiple unresolved P1 flags stack at once: anonymous customer concentration, convertible/debt/capped-call complexity, China/Taiwan/Korea/export exposure, Rigaku/capital-allocation uncertainty, shareholder-capture bridge, and valuation crowding. It is improved from generic backlog but not yet R7 even as risk-flag. | NO |
| CAMT | R5_PRIORITY_UNDERWRITING_CONTINUE; S-A-B-C A / Medium; no full R6 memo yet | R6_PRIORITY_MEMO_CONTINUE | CAMT has strong advanced-packaging inspection/metrology evidence and order momentum, but R7 cannot be assigned before a full R6 memo. Customer identity/concentration, Israel/geopolitical exposure, order durability, thesis-revenue separation, and valuation/crowding still need R6-level underwriting. | NO |
| POET | NO-GO / permanent caution | NO-GO | No-Go library treats POET as a false-positive caution reference. Demo/platform narrative and production-revenue uncertainty remain hard blockers unless materially different public evidence appears. | NO |
| LWLG | BLOCKED / near NO-GO | BLOCKED | No-Go library marks LWLG as blocked/near NO-GO. Production revenue and customer validation uncertainty remain critical blockers; risk-flag R7 cannot be used for a thesis without production-customer evidence. | NO |

## Candidate Panel Notes

### TSEM

TSEM moves to R7_RISK_FLAG_WATCHLIST. The positive case is no longer just a speculative photonics narrative: local R6 evidence showed filed operating revenue, SiPho contracts, customer prepayments, and direct AI optical-interconnect linkage. It is still not clean because prepayments are not revenue, contract cancellability is not public, SiPho customer identity/concentration is undisclosed, capacity execution is unproven, valuation/crowding is high, and GF litigation remains a monitor.

### FORM

FORM moves from BLOCKED to R7_RISK_FLAG_WATCHLIST. The old R6-R1 customer concentration block was too strict for governance watchlist purposes. The concentration is material and explicit, but named and monitorable. It blocks R7_CLEAN_WATCHLIST, not risk-flag R7.

### ONTO

ONTO moves from generic R6_RESEARCH_BACKLOG to R6_PRIORITY_MEMO_CONTINUE. It has real process-control/metrology evidence, but anonymous customer concentration, convertible financing, Rigaku capital allocation, China/Taiwan/Korea/export exposure, valuation/crowding, and shareholder-capture uncertainty stack too heavily for R7 today.

### CAMT

CAMT moves to R6_PRIORITY_MEMO_CONTINUE. It should not be classified as R7 before a full R6 memo because customer identity/concentration, Israel/geopolitical exposure, order durability, thesis-revenue separation, and crowding remain unresolved.

### POET

POET remains NO-GO / permanent caution. It should not reopen without materially different public production-revenue and customer evidence.

### LWLG

LWLG remains BLOCKED / near NO-GO. It cannot use speculative R7 unless production revenue and customer validation evidence materially change.

## Agent Debate Summary

See AGENT_DEBATE_SUMMARY.md for the coordinated multi-agent-style sections.

## Monitoring, Downgrade, And Upgrade Rules

| rule_id | rule_name | applies_to | required_action | downgrade_trigger | upgrade_trigger |
| --- | --- | --- | --- | --- | --- |
| R7-001 | No Trade Meaning | All R7 categories | Repeat the no-trade disclaimer in every R7 package and tracker. | Any output converts rating/watchlist status into a trade decision. | N/A |
| R7-002 | P0 Before R7 | All candidates | Block R7 if going concern, governance/accounting impairment, weak thesis linkage, demo-only thesis, social-hype thesis, or revenue-zero/no-path evidence is active. | Any P0 becomes active after admission. | Filed or credible public evidence resolves the P0. |
| R7-003 | Clean Versus Risk Flag | R7_CLEAN_WATCHLIST; R7_RISK_FLAG_WATCHLIST | Assign clean only when customer, revenue, governance, contract, execution, shareholder-capture, and crowding risks are governed. | A clean item develops unresolved P1 risk or a risk-flag item fails its confirmation path. | P1 risks are cleared or downgraded to P2 monitoring items. |
| R7-004 | Speculative Label Discipline | R7_SPECULATIVE_RIGHT_TAIL | Mark the label explicitly speculative and include confirmation/invalidation checklist. | Speculation becomes narrative-only or fails production/customer evidence tests. | Production revenue, repeat customer evidence, or contract-quality evidence improves. |
| R7-005 | Evidence Separation | All R7 candidates | Maintain evidence table and source refresh rule. | Memo blends claims/inference with confirmed evidence. | Claims are confirmed by filings, recognized revenue, or credible customer evidence. |
| R7-006 | Customer Risk Governance | Customer-concentrated candidates | Track 10% customer disclosures, program durability, receivables concentration, renewal/order cadence, and customer bargaining risk. | Top customer loss, concentration rise without durability, anonymous customer cannot be governed, or receivables stress appears. | Concentration falls, renewals repeat, terms/durability improve, or customer base diversifies. |
| R7-007 | Contract And Prepayment Governance | Contract/prepayment candidates | Track revenue recognition, deferred revenue/customer advances, refund mechanics, non-cancellable/take-or-pay terms, amendments, and milestone receipts. | Refund, contract reduction, missed payment, failed conversion to revenue, or memo treats prepayment as recognized revenue. | Recognized revenue, non-cancellable terms, repeated shipments, or transparent deferred-revenue conversion appears. |
| R7-008 | Capacity Execution Review | Capacity/ramp candidates | Track capex, tool install, yield, customer qualification, shipment schedule, penalties/refunds, and capacity language. | Capacity slips, customer qualification fails, penalties/refunds appear, or recognized revenue misses path. | Capacity qualification, shipment ramp, and revenue conversion are publicly confirmed. |
| R7-009 | False Positive Defense | POET; LWLG; QUBT/QBTS-style quantum; LAZR/MVIS-style hype or listing stress; demo-only humanoids; other false-positive references | Use them as caution references only unless materially different public production evidence appears. | A candidate resembles these archetypes and lacks production revenue/customer evidence. | Materially different public filings show production revenue, repeat customer demand, and shareholder capture. |
| R7-010 | Review Cadence | All R7 categories | Maintain review cadence and source refresh dates in tracker. | Missed review, stale source base, or material event not incorporated. | Current filing/event evidence clears P1 flags. |
| R7-011 | Crowding And Valuation Risk | All R7 categories | Describe expectation risk qualitatively and separately from evidence. | Narrative/crowding becomes the main thesis or evidence cadence cannot support expectations. | Evidence cadence improves and crowding risk becomes secondary. |
| R7-012 | Shareholder Capture | All candidates | Track gross margin, operating leverage, FCF, dilution, debt, SBC, capital allocation, and customer pricing power. | Operating progress is absorbed by dilution, debt, capex, customer bargaining, or poor capital allocation. | Margins, FCF, capital allocation, and dilution control support capture. |

## Source And Evidence Base

This task used existing local Serenity evidence only. No new ticker screen was run and the candidate universe was not expanded.

Reviewed local evidence:

- migrated_sessions/.../project_context/serenity_project_context_bootstrap_20260531_145409/AGENTS.md
- migrated_sessions/.../SERENITY_PROJECT_STATE.md
- migrated_sessions/.../SERENITY_STOP_GATES.md
- migrated_sessions/.../SERENITY_SCORECARD_V1_2.md
- migrated_sessions/.../SERENITY_NO_GO_LIBRARY.md
- migrated_sessions/.../SERENITY_R3_CLASSIFICATION.csv
- research_reports/serenity_r6_tsem_20260604_123223/*
- research_reports/serenity_sabc_us_stock_research_20260604_084600/*
- research_reports/serenity_r6_r1_20260601_212318/*
- research_reports/serenity_r6_20260531_191654/*
- migrated_sessions/.../research_reports/serenity_r5_20260531_163832/*


## Limitations

- This is a governance-framework recalibration, not company-specific new underwriting.
- No fresh public-source screen or universe expansion was performed.
- Some source paths are migrated context paths because root Serenity context files were absent in this checkout.
- R7_RISK_FLAG_WATCHLIST is not clean status and requires ongoing public-source review.
- No category, rating, or watchlist label means buy recommendation, sell recommendation, target price, position sizing, entry point, or trade plan.
