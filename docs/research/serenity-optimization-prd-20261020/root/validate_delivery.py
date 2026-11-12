"""Validate this research delivery's provenance/structure, not trading logic or returns."""
from pathlib import Path
import json, hashlib, re, csv
from collections import Counter

BASE = Path(__file__).resolve().parent.parent
def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

checks = {}
gh = json.loads((BASE/'github/sources.json').read_text())['sources']
checks['github_files'] = len(gh)
checks['github_repos'] = len({s['repo'] for s in gh})
checks['github_hash_mismatches'] = [s['evidence_file'] for s in gh if sha(BASE/'github'/s['evidence_file']) != s['sha256']]
inventory = []
for f in sorted((BASE/'public').glob('*.receipt.json')):
    d = json.loads(f.read_text())
    raw = BASE/d['raw_path'] if d.get('raw_path') else None
    row = {'receipt':str(f.relative_to(BASE)), 'source_id':d.get('id', f.stem),
           'url':d.get('url'), 'http_status':d.get('http_status'),
           'retrieved_at':d.get('retrieved_at'), 'raw_path':d.get('raw_path'),
           'hash_matches':sha(raw)==d['sha256'] if raw and raw.exists() and d.get('sha256') else None,
           'semantic_state':'not automatically inferred from HTTP', 'retrieval_status':d.get('retrieval_status')}
    if f.name=='POET_Q2_RELEASE.receipt.json':
        row['semantic_state']='raw retrieved but extracted article body shell only; primary native parse used separately'
    if f.name=='HISTORY_RXRX_CURL_RECOVERY.receipt.json':
        row['semantic_state']='strict TLS curl recovery, original Python failure retained; see receipt fields'
        row['url']=d['source']
        row['raw_path']=None
        row['hash_matches']=None
        row['raw_retention_gap']='Original curl body hash recorded but body not retained; normalized parsed JSON retained; no reconstruction or refetch'
        row['parsed_json_path']='public/HISTORY_RXRX.json'
        row['parsed_json_sha256']=sha(BASE/row['parsed_json_path'])
    inventory.append(row)
(BASE/'root/source_inventory.json').write_text(json.dumps(inventory,ensure_ascii=False,indent=2)+'\n')
checks['http_receipts'] = len(inventory)
checks['raw_hash_mismatches'] = [r['receipt'] for r in inventory if r['hash_matches'] is False]
checks['raw_hashes_checked'] = sum(r['hash_matches'] is True for r in inventory)
checks['raw_retention_gaps'] = [r['receipt'] for r in inventory if r.get('raw_retention_gap')]
checks['receipt_status_counts'] = dict(Counter(str(r['http_status']) for r in inventory))
market = json.loads((BASE/'root/market_diagnostics.json').read_text())
checks['market_series'] = len(market['latest'])
checks['market_dates'] = sorted({d['asof'] for d in market['latest'].values()})
checks['market_bar_counts'] = dict(Counter(d['bars'] for d in market['latest'].values()))
checks['market_failed_series'] = market.get('failed_series')
checks['short_history_null_correct'] = all(market['latest'][s]['sma_150'] is None for s in ['DPC','SCTX'])
checks['SPY_missing_volume_retained'] = '2026-04-20' in market['latest']['SPY']['missing_volume_dates']
with (BASE/'public/CBOE_VIX_CSV.raw').open() as f:
    rows = list(csv.DictReader(f))
    asof = next(r for r in rows if r['DATE']=='10/19/2026')
checks['VIX_asof'] = asof
x = json.loads((BASE/'root/X_READ_LOG.json').read_text())
checks['x_main_posts_read'] = len(x['records'])
prd = (BASE/'PRD.md').read_text()
checks['FR_ids'] = sorted(set(re.findall(r'^FR-(\d+) \*\*',prd,re.M)))
checks['NFR_ids'] = sorted(set(re.findall(r'^NFR-(\d+) \*\*',prd,re.M)))
ac = (BASE/'ACCEPTANCE_CASES.md').read_text()
checks['AC_ids'] = sorted(set(re.findall(r'^\| AC-(\d+) \|',ac,re.M)))
checks['broken_local_links'] = []
for p in [BASE/n for n in ['PRD.md','RESEARCH_FINDINGS.md','EVIDENCE_INDEX.md','DATA_CONTRACT.md','ACCEPTANCE_CASES.md','COMPLETION_AUDIT.md'] if (BASE/n).exists()]:
    for target in re.findall(r'\]\(([^)]+)\)',p.read_text()):
        if '://' in target or target.startswith('#'): continue
        target = target.split('#')[0]
        if not (p.parent/target).exists(): checks['broken_local_links'].append({'file':p.name,'target':target})
checks['design_only_not_implementation'] = True
checks['passes'] = (checks['github_files']==29 and checks['github_repos']==7 and
    not checks['github_hash_mismatches'] and not checks['raw_hash_mismatches'] and
    checks['market_series']==16 and checks['market_dates']==['2026-10-19'] and not checks['market_failed_series'] and
    checks['market_bar_counts']=={200:14,81:1,61:1} and checks['short_history_null_correct'] and
    checks['SPY_missing_volume_retained'] and checks['x_main_posts_read']==4 and
    checks['FR_ids']==[f'{i:02d}' for i in range(1,31)] and
    checks['NFR_ids']==[f'{i:02d}' for i in range(1,8)] and
    checks['AC_ids']==[f'{i:02d}' for i in range(1,37)] and not checks['broken_local_links'])
(BASE/'root/validation.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2)+'\n')
manifest = [{'path':str(p.relative_to(BASE)), 'bytes':p.stat().st_size, 'sha256':sha(p)}
            for p in sorted(BASE.rglob('*')) if p.is_file() and p.name!='ARTIFACT_MANIFEST.json']
(BASE/'root/ARTIFACT_MANIFEST.json').write_text(json.dumps({'scope':'Research files; excludes manifest itself','files':manifest},ensure_ascii=False,indent=2)+'\n')
print(json.dumps(checks,ensure_ascii=False,indent=2))
raise SystemExit(0 if checks['passes'] else 1)
