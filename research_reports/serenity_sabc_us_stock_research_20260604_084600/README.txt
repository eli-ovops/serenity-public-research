SERENITY S-A-B-C US STOCK RESEARCH SNAPSHOT

Timestamp: 2026-06-04T08:46:00+08:00
Project: Serenity Alpha Research
Mode: research-only / public-source / no brokerage / no secrets / no trading actions
Candidate set: FORM, ONTO, CAMT, TSEM

Files:
- SERENITY_SABC_CLOSED_LOOP_REPORT.md: full reasoning and evidence classification
- serenity_sabc_rating_table.csv: required structured S-A-B-C table
- market_snapshot.csv: public market-data snapshot from web.finance
- evidence_sources.csv: source URLs used for public evidence
- MANIFEST.md: artifact inventory
- SELF_CHECK.md: safety and validation checklist
- SHA256SUMS.txt: file hashes

Data sources used:
- SEC EDGAR public filings and exhibits
- Public web quote pages for cross-check context
- web.finance public market snapshot accessible without authentication

Evidence classification:
- Confirmed: SEC filing / company-filed release / public market snapshot facts
- Inferred: bottleneck mapping and supply-chain thesis derived from confirmed facts
- Speculative: future contract durability, margin capture, customer breadth, and undisclosed program terms

Limitations and disclaimers:
- This package is not investment advice and contains no buy/sell recommendation, target price, position sizing, entry/exit point, or trade plan.
- No brokerage account, API key, secret, cookie, token, .env, private endpoint, scheduler, service, monitor, or order system was accessed.
- Intraday chart files were not generated because unauthenticated chart-series access failed locally; market_snapshot.csv is included instead.
