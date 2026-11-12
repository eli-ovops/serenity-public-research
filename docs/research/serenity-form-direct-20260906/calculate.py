"""Research scenarios, USD millions except per-share prices; no dependencies."""
import json
from pathlib import Path

ROOT = Path(__file__).parent
SHARES = 80.0
EXCESS_CASH = 200.0
PRICE = 103.90

def value(fcf1, growth, discount, terminal, shares=SHARES, cash=EXCESS_CASH):
    assert discount > terminal
    flows = [fcf1 * (1 + growth) ** i for i in range(5)]
    explicit = sum(cf / (1 + discount) ** (i + 1) for i, cf in enumerate(flows))
    terminal_pv = flows[-1] * (1 + terminal) / (discount - terminal) / (1 + discount) ** 5
    return dict(flows=flows, explicit_pv=explicit, terminal_pv=terminal_pv,
                terminal_weight=terminal_pv / (explicit + terminal_pv),
                price=(explicit + terminal_pv + cash) / shares)

assumptions = {
    'stress': [140, .10, .12, .03],
    'base': [180.2, .20, .10, .035],
    'strong': [220, .20, .10, .035],
    'optimistic': [250, .25, .09, .04],
}
results = {k: dict(inputs=v, **value(*v)) for k, v in assumptions.items()}
lo, hi = 0., 1.
for _ in range(80):
    mid = (lo + hi) / 2
    if value(180.2, mid, .10, .035)['price'] < PRICE:
        lo = mid
    else:
        hi = mid
reverse = value(180.2, mid, .10, .035)
assert abs(reverse['price'] - PRICE) < 1e-8
assert abs(1100 * .24 * .80 + 35 - 50 - 16 - 180.2) < 1e-8
assert results['stress']['price'] < results['base']['price'] < results['strong']['price'] < results['optimistic']['price']
sensitivity = [{'discount': r, 'terminal': t, **value(180.2, .20, r, t)}
               for r in [.09, .10, .11, .12] for t in [.025, .035, .04]]
out = dict(unit='USD millions except per-share USD', shares_m=SHARES,
           excess_cash_m=EXCESS_CASH, scenarios=results, sensitivity=sensitivity,
           reverse_growth_years_2_to_5=mid, reverse=reverse,
           fcf_h1_standard=106.764-24.791,
           fcf_h1_after_sbc=106.764-24.791-16.721,
           book_net_cash=345.640-11.644,
           base_with_full_book_net_cash=value(180.2,.20,.10,.035,cash=345.640-11.644),
           base_with_85m_shares=value(180.2,.20,.10,.035,shares=85),
           checks='formula, monotonicity, reverse-price residual passed')
if __name__ == '__main__':
    (ROOT/'calculations.json').write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps({k: round(v['price'],2) for k,v in results.items()}))
