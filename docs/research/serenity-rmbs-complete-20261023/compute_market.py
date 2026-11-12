"""Deterministic public-data arithmetic; no network or account state."""
import json
from datetime import datetime, timezone
from pathlib import Path

BASE = Path(__file__).resolve().parent
def read(name):
    return json.loads((BASE/'public'/name).read_text())
def num(v):
    return float(str(v).replace('$','').replace(',',''))
hist = {}
stats = {}
for ticker in ['RMBS','QQQ','SOXX']:
    rows = read('HISTORY_FULL_'+ticker+'.json')['data']['tradesTable']['rows']
    bars = sorted([{'date':datetime.strptime(r['date'],'%m/%d/%Y').date().isoformat(),
                    **{k:num(r[k]) for k in ['open','high','low','close','volume']}}
                   for r in rows], key=lambda x:x['date'])
    assert bars[-1]['date']=='2026-10-22' and len(bars)>=61
    hist[ticker]=bars
    prices=[r['close'] for r in bars]
    stats[ticker]={'last_completed_session':bars[-1],
        'returns_pct':{str(n):(prices[-1]/prices[-1-n]-1)*100 for n in [1,5,20,60]},
        'SMA20':sum(prices[-20:])/20,'SMA50':sum(prices[-50:])/50,
        'volume_vs_previous20_avg':bars[-1]['volume']/(sum(r['volume'] for r in bars[-21:-1])/20),
        'close_range_position_pct':100*(bars[-1]['close']-bars[-1]['low'])/(bars[-1]['high']-bars[-1]['low']),
        'source':str(BASE/'public'/('HISTORY_FULL_'+ticker+'.json'))}
stats['RMBS']['RS20_vs_QQQ_pp']=stats['RMBS']['returns_pct']['20']-stats['QQQ']['returns_pct']['20']
stats['RMBS']['RS20_vs_SOXX_pp']=stats['RMBS']['returns_pct']['20']-stats['SOXX']['returns_pct']['20']
stats['RMBS']['RS1_vs_SOXX_pp']=stats['RMBS']['returns_pct']['1']-stats['SOXX']['returns_pct']['1']
stats['RMBS']['entry_confirmed_price']=86.52
stats['RMBS']['one_share_mark_to_close_pnl_before_fees']=85.73-86.52
stats['RMBS']['original85_regular_session_trigger']={
    'observed_completed_session_low':85.01, 'trigger_seen':False,
    'first_real_tick_time':'UNKNOWN',
    'coverage':'10/22 complete regular daily bar, independently Nasdaq and Yahoo; not tick replay or continuous monitoring',
    'after_hours_not_regular_trigger':True}
out={'calculated_at_utc':datetime.now(timezone.utc).isoformat(),'kind':'completed_session_not_live',
     'technical':stats,'breadth_proxy':{
       'SPY':read('INFO_SPY.json')['data']['primaryData'],
       'RSP':read('INFO_RSP.json')['data']['primaryData'],
       'limits':'ETF relative returns are a breadth proxy, not actual advance-decline counts'},
     'VIX':{**read('VIX.json'),'time_status':'provider fields do not include timezone; delayed reference, not synchronized Nasdaq tick'},
     'treasury':{'as_of':'2026-10-22 approx15:30 ET indicative par curve','two_year_pct':4.65,
       'ten_year_pct':4.96,'change_vs_1021_bp':{'two_year':-16,'ten_year':-17},
       'source':'https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?field_tdr_date_value=2026&type=daily_treasury_yield_curve'},
     'calendar':{'beijing_date':'2026-10-23','US_latest_completed_session':'2026-10-22',
       'regular_session_today_beijing':'2026-10-23 21:30 to 2026-10-24 04:00','US_timezone':'EDT UTC-4',
       'is_oct23_exchange_holiday':False,'source':'https://www.nyse.com/trade/hours-calendars'}}
(BASE/'MARKET.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(stats,ensure_ascii=False,indent=2))
