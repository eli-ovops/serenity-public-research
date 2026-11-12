"""Use common calendar dates and FX for overseas/US comparisons."""
import json,datetime
from pathlib import Path
from zoneinfo import ZoneInfo
P=Path(__file__).resolve().parent
stocks=json.loads((P/'OVERSEAS_TECHNICALS.json').read_text())
def series(key):
    r=json.loads((P/'public'/('BENCH_'+key+'.json')).read_text())['chart']['result'][0]
    z=ZoneInfo(r['meta']['exchangeTimezoneName']);q=r['indicators']['quote'][0]['close']
    return {datetime.datetime.fromtimestamp(t,z).strftime('%Y-%m-%d'):q[i] for i,t in enumerate(r['timestamp']) if q[i] is not None}
bench={k:series(k) for k in ['HSI','FCHI','FTSE','OMXSPI','TWII','EURUSD','GBPUSD','USDSEK','USDHKD','USDTWD']}
src=json.loads((P/'HISTORY_SOURCES.json').read_text())
nas={}
for k in ['SOXX','QQQ']:
    rows=json.loads(Path(src[k]).read_text())['data']['tradesTable']['rows']
    nas[k]={datetime.datetime.strptime(r['date'],'%m/%d/%Y').strftime('%Y-%m-%d'):float(r['close'].replace('$','').replace(',','')) for r in rows}
settings={'SOI':('FCHI','EURUSD',1,1),'IQE':('FTSE','GBPUSD',1,.01),'SIVE':('OMXSPI','USDSEK',-1,1),'ASMPT':('HSI','USDHKD',-1,1),'Lenovo':('HSI','USDHKD',-1,1),'ESMT':('TWII','USDTWD',-1,1)}
out={}
for t,(local,fk,direction,scale) in settings.items():
    stock={b['date']:b['close'] for b in stocks[t]['complete_bars']}
    common=sorted(set(stock)&set(bench[local])&set(bench[fk])&set(nas['SOXX'])&set(nas['QQQ']))
    dates=common[-21:];a,b=dates[0],dates[-1]
    fx=lambda date:bench[fk][date] if direction==1 else 1/bench[fk][date]
    sr=(stock[b]/stock[a]-1)*100;lr=(bench[local][b]/bench[local][a]-1)*100
    usd=(stock[b]*scale*fx(b)/(stock[a]*scale*fx(a))-1)*100
    out[t]={'common_window_start':a,'common_window_end':b,'shared_intervals':len(dates)-1,'local_benchmark':local,
        'stock_local_return_pct':sr,'benchmark_local_return_pct':lr,'local_relative_pp':sr-lr,
        'stock_USD_return_pct':usd,'FX_pair':fk,'quote_scale_to_base_currency':scale,
        'SOXX_return_same_dates_pct':(nas['SOXX'][b]/nas['SOXX'][a]-1)*100,
        'SOXX_relative_USD_pp':usd-(nas['SOXX'][b]/nas['SOXX'][a]-1)*100,
        'QQQ_relative_USD_pp':usd-(nas['QQQ'][b]/nas['QQQ'][a]-1)*100,
        'qualification':'price returns exclude dividends; FX and local/US closes are different intraday times; common-date comparison is context, not synchronous execution proof',
        'HK_board_lot_not_assumed':'minimum trade lot/channel must be verified separately; 1share USD rules do not establish HK odd-lot availability'}
(P/'OVERSEAS_RELATIVE.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(out,ensure_ascii=False))
