import unittest,json
from evidence_adapter import EvidenceAdapter,indicators
class EvidenceTests(unittest.TestCase):
 def setUp(self):
  self.rows=[{'date':f'2026-09-{i:02d}','open':10.,'high':11.,'low':9.,'close':10.,'volume':100 if i<25 else 200} for i in range(1,26)]
  self.p={'ticker':'FORM','as_of':'2026-09-25','retrieved_utc':'now','policy':'test','market':{'rows':self.rows,'source':'public','price_basis':'daily'},'statements':{x:{'identity':x} for x in ['get_balance_sheet','get_cashflow','get_income_statement']},'fundamentals':{},'benchmarks':{},'vix':{},'company_events':{'news':['company only']}}
  self.a=EvidenceAdapter(self.p)
 def get(self,n,*a):return json.loads(self.a.respond(n,*a))['data']
 def test_statements_distinct_and_annual_not_substituted(self):
  self.assertNotEqual(self.get('get_balance_sheet','FORM'),self.get('get_cashflow','FORM'))
  self.assertEqual(self.get('get_cashflow','FORM','annual')['status'],'UNKNOWN')
 def test_no_global_or_macro_substitution(self):
  self.assertEqual(self.get('get_global_news')['status'],'UNKNOWN')
  self.assertEqual(self.get('get_macro_indicators','core_pce')['status'],'UNKNOWN')
 def test_ticker_and_date_scope(self):
  self.assertEqual(self.get('get_stock_data','NVDA')['status'],'UNKNOWN')
  d=self.get('get_stock_data','FORM','2026-09-01','2026-09-10')
  self.assertEqual(len(d['rows']),10)
  self.assertEqual(self.get('get_indicators','FORM','close_20_sma','2026-09-10')['status'],'UNKNOWN')
 def test_constant_series_and_actual_day_volume_ratio(self):
  x=indicators(self.rows);self.assertEqual(x['close_20_sma'],10);self.assertEqual(x['atr'],2);self.assertEqual(x['rsi'],50)
  self.assertEqual(self.get('get_verified_market_snapshot','FORM','2026-09-25')['last_volume_over_prior20_mean'],2)
if __name__=='__main__':unittest.main()
