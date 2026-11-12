"""Build coverage without promoting source collection into completed research."""
import csv
import json
from pathlib import Path

P = Path(__file__).resolve().parent
ROOT = P.parents[2]
# Preserve the curated registry and later user additions.
if (P / 'COVERAGE.csv').exists():
    raise SystemExit('COVERAGE.csv is curated; update rows in place, do not rebuild from the historical snapshot.')
d = json.loads((P / 'public_snapshot.json').read_text())
q = json.loads((P / 'primary_refresh.json').read_text())
groups = {
    'compute_ip': 'NVDA AVGO MRVL ALAB AIP',
    'memory_storage': 'MU SKHY RMBS ESMT WDC STX',
    'photonics_materials': 'TSEM CRDO AAOI COHR LITE CIEN FN POET AXTI SOI IQE SIVE LWLG NOK LASR',
    'packaging_test': 'FORM AEHR CAMT ONTO AMKR ASX TER ASMPT',
    'equipment_foundry': 'ASML AMAT LRCX KLAC ACMR ENTG TSM GFS INTC ON',
    'power_turbines_storage': 'GEV HWM DPC GNRC PWR ETN FLNC',
    'cooling_servers': 'MOD AAON NVT VRT CLS SMCI DELL HPE Lenovo',
    'network_cloud': 'ANET AMZN NBIS',
    'medical_auto_other': 'RXRX SCTX TSLA TEM CCXI',
}
sector = {t: k for k, v in groups.items() for t in v.split()}
assert set(sector) == set(d['universe'])
hold = dict(TSLA=1, NVDA=2, TSM=1, RXRX=50, CLS=1, NVT=2, CAMT=1, DPC=3, SCTX=2, POET=20)
fixed = set('FORM AEHR AXTI SOI IQE ESMT SIVE GEV HWM'.split())
fields = ['ticker', 'company_from_sec', 'sector', 'scope_source', 'fixed_nine', 'user_reported_shares', 'primary_source', 'primary_status', 'valuation_status', 'trend_status', 'events_status', 'invalidation_status', 'remaining_work', 'final_status', 'owner']
with (P / 'COVERAGE.csv').open('w') as f:
    w = csv.DictWriter(f, fieldnames=fields)
    w.writeheader()
    for i, t in enumerate(d['universe']):
        sec = d['sec'].get(t, {})
        ev = q.get(t, {})
        px = d['prices'].get(t, {})
        w.writerow(dict(
            ticker=t, company_from_sec=sec.get('name', 'UNKNOWN'), sector=sector[t],
            scope_source='merged_matrix_30' if i < 30 else 'historical_sectors_fixed_pool_user_updates',
            fixed_nine=t in fixed, user_reported_shares=hold.get(t, 0 if t in ['FORM', 'AMZN'] else 'UNKNOWN'),
            primary_source=ev.get('source', sec.get('source', 'PENDING')),
            primary_status='partial_facts_or_locator_only' if ev else 'SEC_index_only' if sec else 'PENDING',
            valuation_status='PENDING_current_scenarios_old_models_not_carried_forward',
            trend_status='OHLC_collected_corporate_actions_and_relative_strength_pending' if 'metrics' in px else 'PENDING_not_excluded',
            events_status='SEC_index_checked_IR_and_full_text_pending' if sec else 'PENDING_exchange_and_IR',
            invalidation_status='delivery_thesis_contradicted_by_Sept16_guidance' if t == 'FLNC' else 'PENDING_economic_thresholds',
            remaining_work=ev.get('remaining_work', 'fundamentals; valuation; trend verification; events; economic invalidation'),
            final_status='EXCLUDED' if t == 'FLNC' else 'RESEARCH_INCOMPLETE', owner='current_thread_direct',
        ))
sources = list(ROOT.glob('research_reports/*20260716/*20260716.csv'))
social = next(x for x in sources if '全清单' in x.name)
rows = list(csv.DictReader(social.open(encoding='utf-8-sig')))
with (P / 'HISTORICAL_SOCIAL_COVERAGE.csv').open('w') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0]) + ['current_pool_mapping', 'evidence_status'])
    w.writeheader()
    for row in rows:
        code = row['代码']
        row['current_pool_mapping'] = code if code in d['universe'] else 'retained_lead_identity_alias_pending'
        row['evidence_status'] = 'historical_social_lead_not_primary_evidence'
        w.writerow(row)
assert len(d['universe']) == 68 and len(rows) == 85
print({'formal_pool': 68, 'social_rows': 85, 'user_holdings': len(hold), 'fixed_pool': len(fixed)})
