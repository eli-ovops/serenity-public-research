"""2026-09-15 public research scenarios. Forecasts are author assumptions.
No account data, network, trading, or third-party dependencies.
Run with python3 -B calculate.py. Money/shares in millions unless noted.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FADE = [.15, .12, .09, .06, .04]
CASES = ['stress', 'base', 'strong']

def dcf(cf, r, g, net, shares):
    cf = list(cf)
    for growth in FADE:
        cf.append(cf[-1] * (1 + growth))
    explicit = sum(c / (1+r)**t for t, c in enumerate(cf, 1))
    terminal = cf[-1]*(1+g)/(r-g)/(1+r)**len(cf)
    return dict(cash_flows=cf, discount_rate=r, terminal_growth=g,
                equity_bridge=net, diluted_shares=shares,
                value=(explicit+terminal+net)/shares,
                terminal_fraction=terminal/(explicit+terminal))

SPECS = {
 'FORM': [([140,154,169.4,186.34,204.974],.12,.03,200,80),
          ([180.2*1.2**i for i in range(5)],.10,.035,200,80),
          ([220*1.2**i for i in range(5)],.10,.035,200,80)],
 'AEHR': [([8,10,12,15,18],.13,.03,85,36),
          ([23,30,40,52,68],.11,.035,100,34),
          ([35,48,65,90,120],.10,.04,100,34)],
 'AXTI': [([-20,0,10,20,30],.13,.03,200,75),
          ([0,15,35,60,85],.105,.035,280,70),
          ([5,30,70,120,180],.10,.04,280,70)],
 'Soitec': [([0,30,60,90,120],.12,.03,-56,36),
            ([40,90,156,224,279],.10,.035,-56,36),
            ([60,125,210,300,380],.10,.035,-56,36)],
 'IQE': [([-8,-5,0,4,8],.14,.03,-15,1500),
         ([0,4,12,20,28],.12,.035,30.2,1450),
         ([2,10,25,40,60],.11,.04,30.2,1450)],
 # Extra USD30m capacity capex at assumed 10 SEK/USD, split over years 1-2.
 'Sivers': [([-330,-270,-50,10,60],.15,.03,500,400),
            ([-320,-230,30,120,250],.13,.035,600,375),
            ([-300,-180,100,300,550],.12,.04,600,375)],
 'GEV': [([3000,3500,4200,5000,6000],.105,.03,3000,275),
         ([4500,6000,7500,9500,11500],.09,.035,5000,270),
         ([5500,7500,10000,13000,16000],.09,.035,5000,270)],
 # Per-share FCFE after interest: do not subtract debt twice.
 'HWM': [([4,4.4,4.8,5.2,5.7],.11,.03,0,1),
         ([4.75,5.6,6.6,7.8,9.2],.095,.035,0,1),
         ([5,6.2,7.7,9.5,11.8],.09,.04,0,1)]
}

def earnings(revenue, margin, shares, pe, fx=1, reserve=0):
    return dict(revenue=revenue, normal_net_margin=margin, diluted_shares=shares,
                pe=pe, fx_assumption=fx, reserve=reserve,
                value=(revenue*margin*pe-reserve)/shares*fx)

def main():
    out = {'as_of':'2026-09-15', 'forecast_status':'author assumptions, not company guidance',
           'dcf_method':'5 explicit years + 5 fade years + terminal', 'models':{}}
    for name, cases in SPECS.items():
        out['models'][name] = {label:dcf(*case) for label,case in zip(CASES,cases)}
    inputs = {
      'ESMT': [(22000,.12,320,10),(30000,.22,320,14),(40000,.30,320,16)],
      'TSM': [(176000,.45,5200,20),(185000,.50,5200,24),(205000,.53,5200,26)],
      'NVDA': [(360000,.45,24500,20,1,121400),(440000,.52,24500,25,1,121400),(500000,.55,24500,28,1,121400)],
      'ASMPT': [(18000,.08,430,16),(23000,.12,430,22),(28000,.15,430,25)],
      'Lenovo': [(95000,.02,16500,10,7.8),(110000,.033,16500,14,7.8),(120000,.04,16500,16,7.8)]
    }
    for name,cases in inputs.items():
        out['models'][name] = {label:earnings(*case) for label,case in zip(CASES,cases)}
    out['cross_checks'] = {
      'ESMT_CB_max_incremental_shares_m':2000/308,
      'ESMT_basic_plus_CB_shares_m':298.1278+2000/308,
      'TSM_Q3_September_needed_TWD_bn_at_assumed_FX32':45.2*32-467.580-514.806,
      'TSM_H1_FCF_to_net_profit':(1482.33-846.76)/1279.04,
      'ASMPT_H1_cash_after_capex_interest_leases_and_SBC_HKD_m':727.255-131.216-5.518-75.070-109.088-77.759,
      'Lenovo_Q1_FCF_before_acquisitions_USD_m':382.301-91.009-115.183-168.018,
      'TSM_example_DAY_limit_NOT_account_approval':415,
      'TSM_stress_price_NOT_stop_or_max_loss':out['models']['TSM']['stress']['value'],
      'TSM_one_share_stress_decline_NOT_max_loss':415-out['models']['TSM']['stress']['value'],
      'TSM_10pct_capital_amount_only':415/.10,
      'TSM_8pct_capital_amount_only':415/.08,
    }
    assert len(out['models']) == 13
    for name,cases in out['models'].items():
        assert cases['stress']['value'] < cases['base']['value'] < cases['strong']['value'], name
    (ROOT/'calculations.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    for name,cases in out['models'].items():
        scale = 100 if name == 'IQE' else 1
        print(name, '/'.join(f'{cases[k]["value"]*scale:.2f}' for k in CASES))

if __name__ == '__main__':
    main()
