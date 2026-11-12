"""Explicit primary-filing overrides; retain the immutable original mixed-period pack."""
import copy, json
from pathlib import Path
BASE=Path(__file__).resolve().parent
PROJECT=BASE.parents[2]
original=PROJECT/'docs/research/serenity-skill-integration-20261023/rmbs-live/snapshots/RMBS.json'
s=json.loads(original.read_text())
b=json.loads((BASE/'FINANCIAL_BRIDGE.json').read_text())
q=b['financial_periods']['Q2_2026'];ttm=b['financial_periods']['TTM_to_2026_06_30'];bs=b['balance_20260630']
f=s['fundamentals'];summary=f['summary'];series=f['series'];date='2026-06-30';filed='2026-07-28'
qvals={'revenue':q['revenue'],'gross_profit':b['q2_revenue_composition']['gross_profit'],
       'operating_income':b['q2_revenue_composition']['operating_income'],'net_income':q['net_income_gaap'],
       'operating_cash_flow':q['cfo'],'capex':q['cash_ppe_purchases'],'sbc':q['sbc'],
       'cash':bs['cash_equivalents'],'short_term_investments':bs['marketable_securities'],
       'inventory':bs['inventory'],'equity':bs['equity'],'total_assets':bs['total_assets'],
       'total_liabilities':bs['total_liabilities'],'receivables':bs['accounts_receivable'],
       'goodwill':bs['goodwill'],'contract_liabilities':bs['deferred_revenue']}
for k,v in qvals.items():
    series[k]=[r for r in series.get(k,[]) if r['end']!=date]+[{'end':date,'value':round(v*1e6),'unit':'USD','filed':filed,'source':'primary_10Q_table_or_H1_minus_Q1'}]
series['shares_outstanding_dei'].append({'end':date,'value':108461603,'filed':filed,'form':'10-Q'})
series['total_debt']=[{'end':date,'value':49_985_000,'unit':'USD','filed':filed,
    'definition':'conservative debt-like sensitivity: EDA installment28.182m + operating leases21.803m, no conventional funded debt reported'}]
summary.update(revenue_ttm=ttm['revenue']*1e6,net_income_ttm=ttm['net_income_gaap']*1e6,
    operating_cash_flow_ttm=ttm['cfo']*1e6,capex_ttm=ttm['cash_ppe_purchases']*1e6,
    sbc_ttm=ttm['sbc']*1e6,gross_profit_ttm=601_023_000,operating_income_ttm=268_570_000,
    revenue_yoy_pct=(207.385/172.209-1)*100,revenue_qoq_pct=(207.385/180.189-1)*100,
    revenue_ttm_year_ago=645_488_000,net_income_ttm_year_ago=229_105_000,
    shares_outstanding=108461603,shares_as_of=date,shares_filed=filed,
    share_count_change_pct_vs_4_obs_ago=(108461603/107593820-1)*100,
    financials_source='primary SEC 10-Q + 10-K period-matched repair',financials_source_url=b['sources'][0]['url'],
    cash_and_st_investments={'end':date,'value':824_948_000},
    total_debt_latest={'end':date,'value':49_985_000,'definition':'EDA + leases conservative sensitivity'},
    net_debt=-774_963_000,
    rnd_ttm=None,buybacks_ttm=None,
    sec_data_warnings=['post_ASR_actual_common_and_current_cash_not_disclosed','debt_includes_EDA_and_operating_lease_sensitivity'])
for field,key in [('equity','equity'),('total_assets','total_assets'),('total_liabilities','total_liabilities'),
                  ('receivables','accounts_receivable'),('inventory','inventory'),('goodwill','goodwill'),
                  ('contract_liabilities','deferred_revenue'),('cash','cash_equivalents')]:
    summary[field+'_latest']={'end':date,'value':bs[key]*1e6}
    old=[r for r in series.get(field,[]) if r.get('end')=='2025-06-30']
    summary[field+'_year_ago']={'end':'2025-06-30','value':old[-1]['value']} if old else None
summary['gross_margin_quarterly']=[r for r in summary['gross_margin_quarterly'] if r['as_of']!=date]+[{'as_of':date,'pct':165.412/207.385*100}]
summary['operating_margin_quarterly'].append({'end':date,'pct':72.731/207.385*100})
summary['fcf_last_4q']=[r for r in summary['fcf_last_4q'] if r['end']!='2025-06-30']+[{'end':date,'value':52_178_000}]
summary['gross_margin_change_yoy_pp']=(165.412/207.385-137.439/172.209)*100
s['market_current'].update(shares_outstanding=108461603,shares_as_of='2026-06-30T00:00:00Z',market_cap=85.73*108461603,
    basis='10/22 close x latest disclosed 6/30 common; not actual post-ASR real-time capitalization')
s['quote']['source_url']='https://api.nasdaq.com/api/quote/RMBS/info?assetclass=stocks'
s['repair']={'source_original':str(original),'financial_bridge':str(BASE/'FINANCIAL_BRIDGE.json'),
    'as_of':b['asof_utc'],'original_warnings':copy.deepcopy(s['warnings']),
    'original_summary_retained_only_in_original':True,
    'no_assumption_of_realtime_post_ASR_shares':True,
    'net_debt_definition':'EDA28.182m + operating leases21.803m - cash+securities824.948m; PE valuations do not add this cash',
    'CFO_capex_conventions':'PPE-only FCF299.535m; include installment13.090m ->286.445m; SBC55.990m economic sensitivity separately'}
s['warnings']=['post_ASR_actual_common_and_current_cash_not_disclosed','reported_share_date_differs_from_quote_date',
    'debt_includes_EDA_and_operating_lease_sensitivity','cash_conversion_H1_CFO_down15_9pct',
    'DOJ_investigation_known_since_Q1_unquantified_tail_risk']
for e in s['evidence']:
    if e['evidence_id']=='E-LIVE-SHARES':e.update(title='10-Q common outstanding108461603 as of6/30; not post-ASR',locator=b['sources'][0]['url'],published_at='2026-07-28T00:00:00Z',period_end='2026-06-30T00:00:00Z',source_type='filing')
    elif e['evidence_id']=='E-LIVE-FIN':e.update(title='SEC primary period-matched Q2/H1/TTM repair',locator=b['sources'][0]['url'],published_at='2026-07-28T00:00:00Z',period_end='2026-06-30T00:00:00Z',source_type='filing')
s['retrieved_at']=b['asof_utc'];s['fundamentals_fallback']['status']='superseded_by_primary_repair' if isinstance(s.get('fundamentals_fallback'),dict) else 'UNKNOWN'
out=BASE/'snapshots'/'RMBS.json';out.parent.mkdir(exist_ok=True);out.write_text(json.dumps(s,ensure_ascii=False,indent=2)+'\n')
assert abs(summary['net_income_ttm']-239_680_000)<.01
assert abs(s['market_current']['market_cap']-85.73*108461603)<.01
print(json.dumps({'snapshot':str(out),'market_cap':s['market_current']['market_cap'],'common':summary['shares_outstanding'],'TTM_NI':summary['net_income_ttm'],'TTM_CFO':summary['operating_cash_flow_ttm']}))
