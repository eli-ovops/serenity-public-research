"""As-of diagnostics on already retrieved public bars; no orders or backtest."""
import csv
import io
import json
import math
from datetime import datetime
from pathlib import Path

B = Path(__file__).resolve().parents[1]
P = B / 'public'
ASOF = '2026-10-19'


def number(v):
    if v is None or str(v).strip().lower() in ['n/a', '--', '-', '']:
        return None
    return float(str(v).replace('$', '').replace(',', ''))


def bars(t):
    x = json.loads((P / ('HISTORY_' + t + '.json')).read_text())
    rows = x['data']['tradesTable']['rows']
    result = []
    for row in rows:
        d = datetime.strptime(row['date'], '%m/%d/%Y').strftime('%Y-%m-%d')
        if d > ASOF:
            continue
        result.append(dict(date=d, **{k: number(row[k]) for k in ['open', 'high', 'low', 'close', 'volume']}))
    return sorted(result, key=lambda r: r['date'])


def stats(rows, cutoff=ASOF):
    rows = [r for r in rows if r['date'] <= cutoff]
    c = [r['close'] for r in rows]
    r = dict(asof=rows[-1]['date'], bars=len(rows), close=c[-1], open=rows[-1]['open'],
             high=rows[-1]['high'], low=rows[-1]['low'], volume=rows[-1]['volume'],
             intraday_close_location=(c[-1]-rows[-1]['low'])/(rows[-1]['high']-rows[-1]['low']) if rows[-1]['high'] > rows[-1]['low'] else None)
    for n in [1, 5, 20, 60]:
        r['return_' + str(n) + 'd_pct'] = (c[-1]/c[-n-1]-1)*100 if len(c) > n else None
    for n in [20, 50, 150]:
        avg = sum(c[-n:])/n if len(c) >= n else None
        r['sma_' + str(n)] = avg
        r['deviation_sma_' + str(n) + '_pct'] = (c[-1]/avg-1)*100 if avg else None
    r['drawdown_from_prior_20d_close_high_pct'] = (c[-1]/max(c[-20:])-1)*100
    prior_volumes = [x['volume'] for x in rows[-21:-1]]
    r['volume_vs_prior_20d_avg'] = rows[-1]['volume']/(sum(prior_volumes)/20) if len(prior_volumes)==20 and all(v is not None for v in prior_volumes) and rows[-1]['volume'] is not None else None
    r['missing_volume_dates'] = [x['date'] for x in rows if x['volume'] is None]
    return r


tickers = ['QQQ','SPY','RSP','SOXX','XBI','NVDA','TSLA','TSM','CLS','NVT','CAMT','POET','INOD','DPC','SCTX','RXRX']
series = {}
failures = {}
for t in tickers:
    try:
        series[t] = bars(t)
    except Exception as e:
        failures[t] = str(e)
out = {'asof':ASOF,'scope':'public unadjusted daily-bar diagnostics, not recommendations or performance',
       'limits':['No verified split/dividend adjustment or consolidated breadth series; RSP/SPY is only a breadth proxy.',
                 'No intraday tape, options book, order-book depth, or fill inference.',
                 'DPC and SCTX have short listing history; unavailable 150-day averages remain null.'],
       'latest':{},'historical_asof_checks':{},'failed_series':failures}
for t, rows in series.items():
    r=stats(rows)
    bench='XBI' if t in ['RXRX','SCTX'] else ('SOXX' if t in ['NVDA','TSM','CLS','CAMT','POET'] else ('SPY' if t in ['NVT','DPC','TSLA'] else 'QQQ'))
    b=stats(series[bench])
    r['comparison_benchmark']=bench
    r['relative_return_20d_pp'] = r['return_20d_pct']-b['return_20d_pct'] if r['return_20d_pct'] is not None and b['return_20d_pct'] is not None else None
    out['latest'][t]=r
    if t in ['CLS','NVT','DPC','INOD','SCTX','QQQ','SOXX']:
        out['historical_asof_checks'][t]={d:stats(rows,d) for d in ['2026-10-06','2026-10-08','2026-10-13']}
vix=[]
for row in csv.DictReader(io.StringIO((P/'CBOE_VIX_CSV.raw').read_text())):
    d=datetime.strptime(row['DATE'],'%m/%d/%Y').strftime('%Y-%m-%d')
    if d<=ASOF:vix.append(dict(date=d,**{k.lower():float(row[k]) for k in ['OPEN','HIGH','LOW','CLOSE']}))
out['vix_recent']=vix[-6:]
out['vix_last_return_pct']=(vix[-1]['close']/vix[-2]['close']-1)*100
(B/'root/market_diagnostics.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
for t,r in out['latest'].items():
    print(t, {k:round(v,3) if isinstance(v,float) else v for k,v in r.items() if k in ['asof','bars','close','return_1d_pct','return_20d_pct','deviation_sma_50_pct','deviation_sma_150_pct','relative_return_20d_pp','volume_vs_prior_20d_avg']})
print('VIX',out['vix_recent'][-1],out['vix_last_return_pct'],'missing',failures)
