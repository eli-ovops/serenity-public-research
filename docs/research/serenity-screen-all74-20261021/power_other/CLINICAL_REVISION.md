# Clinical model correction / root decision

Only RXRX and SCTX revised. Prior immediate half-reduction is rejected history, not an order or trade. Run clinical_repair.py after audit_fix.py for full reproduction.

## RXRX

{
  "price": 3.665,
  "risk_adjusted_values": [
    0.1656277854027023,
    0.6014340112266817,
    2.237100070097198
  ],
  "all_success_values": [
    0.6376887281126377,
    2.4502015313219467,
    6.516575435246194
  ],
  "first_financing_month": [
    18,
    21,
    26
  ],
  "minimum_cash": [
    100.0,
    100.0,
    100.0
  ],
  "necessary_common_probability": [
    6.840333802876856,
    1.5332902442411573,
    0.545651166013651
  ],
  "necessary_peak_multiplier_original_PoS": [
    76.60546328087405,
    8.138456407791908,
    1.715127977393703
  ]
}

Conditional fully funded paths only. External financing price can exceed author rNPV and is NOT asserted achievable. Without financing the forecast cannot continue when cash depletes; options include early termination, licensing, sale or insolvency. No arbitrary continuation with negative cash. Initial cash includes estimated post-offering balances and restricted/intervening-burn uncertainty, so cash runway is scenario not bank proof.

Precommercial full-program budgets are paid on every probability-weighted revenue path; this is a conservative expected-cost approximation, not a calibrated decision tree. Failure can stop trials earlier and reduce subsequent burn/dilution. The paired early-termination sensitivity drops pipeline PV to zero while halving spending after2years; no benefit from saved cost while silently keeping failed drug sales.

Necessary common PoS holds every program at same probability with its scenario commercial peaks; values>1 mean impossible under that combination. Alternatively required peak multiplier holds original program probabilities fixed. These invert the price equation, do not estimate true probabilities; joint dependence between programs not calibrated.

risk-adjusted strong is NOT a success ceiling. All-program PoS=1 at same strong commercial assumptions is an explicit conditional right-tail illustration, not a probability forecast nor an upper bound on success. Commercial peaks can also exceed/fall short of scenarios.

{
  "status": "ROOT_DECISION_RECORDED_FOR_FINAL_ACCEPTANCE",
  "confirmed_shares": 20,
  "research_target_remaining": 20,
  "action": "Hold existing position, no add; root retained current9-position facts. Prior half-reduction proposal not adopted and not execution.",
  "reason": "No newly verified clinical/regulatory/financing deterioration during this model-only review and original protection not triggered at the source snapshot. Existing funding supports the next milestone; RXRX has real preliminary efficacy and a registration-development path, SCTX remains early human study with IPO runway. Clinical and commercial upside can exceed risk-adjusted strong. This supports retaining finite existing option exposure while declining new exposure; not proof marketprice is cheap. Prior RXRX reduction already recognized.",
  "limitations": "Current NAV, fees and exact new cash unknown; no budget compliance claim, no continuous monitoring. Clinical data remain early; total loss and future dilution possible.",
  "deadline": "2026-10-30 before11/2 clinical-data event; at next requested review decide event exposure using updated evidence, not indefinite temporaryhold.",
  "exit": "Material efficacy/safety failure or viable registration path denied ->20to0. Cash/financing worsens enough to threaten milestone -> reunderwrite and reduce quantified exposure. Old3.6/4automatic batches remain retired."
}

## SCTX

{
  "price": 20.325,
  "risk_adjusted_values": [
    0.9216861078589169,
    2.7275385583976517,
    13.67399038677094
  ],
  "all_success_values": [
    2.6212585334312353,
    16.74129870037871,
    69.61849374788588
  ],
  "first_financing_month": [
    17,
    21,
    25
  ],
  "minimum_cash": [
    50.0,
    50.0,
    50.0
  ],
  "necessary_common_probability": [
    10.895756215023788,
    1.2328179502616106,
    0.27017221894826193
  ],
  "necessary_peak_multiplier_original_PoS": [
    217.91512430047578,
    13.76141098906634,
    1.5735228596105888
  ]
}

Conditional fully funded paths only. External financing price can exceed author rNPV and is NOT asserted achievable. Without financing the forecast cannot continue when cash depletes; options include early termination, licensing, sale or insolvency. No arbitrary continuation with negative cash. Initial cash includes estimated post-offering balances and restricted/intervening-burn uncertainty, so cash runway is scenario not bank proof.

Precommercial full-program budgets are paid on every probability-weighted revenue path; this is a conservative expected-cost approximation, not a calibrated decision tree. Failure can stop trials earlier and reduce subsequent burn/dilution. The paired early-termination sensitivity drops pipeline PV to zero while halving spending after2years; no benefit from saved cost while silently keeping failed drug sales.

Necessary common PoS holds every program at same probability with its scenario commercial peaks; values>1 mean impossible under that combination. Alternatively required peak multiplier holds original program probabilities fixed. These invert the price equation, do not estimate true probabilities; joint dependence between programs not calibrated.

risk-adjusted strong is NOT a success ceiling. All-program PoS=1 at same strong commercial assumptions is an explicit conditional right-tail illustration, not a probability forecast nor an upper bound on success. Commercial peaks can also exceed/fall short of scenarios.

{
  "status": "ROOT_DECISION_RECORDED_FOR_FINAL_ACCEPTANCE",
  "confirmed_shares": 2,
  "research_target_remaining": 2,
  "action": "Hold existing position, no add; root retained current9-position facts. Prior half-reduction proposal not adopted and not execution.",
  "reason": "No newly verified clinical/regulatory/financing deterioration during this model-only review and original protection not triggered at the source snapshot. Existing funding supports the next milestone; RXRX has real preliminary efficacy and a registration-development path, SCTX remains early human study with IPO runway. Clinical and commercial upside can exceed risk-adjusted strong. This supports retaining finite existing option exposure while declining new exposure; not proof marketprice is cheap. Prior RXRX reduction already recognized.",
  "limitations": "Current NAV, fees and exact new cash unknown; no budget compliance claim, no continuous monitoring. Clinical data remain early; total loss and future dilution possible.",
  "deadline": "Next material safety/financing update and before2027H1firsthuman data; requested-review only.",
  "protection": "Original mutually exclusive FIRST reduction remains: rebound25-26 without new human evidence ->2to1; OR regularclose<16.7 AND XBI<145 ->2to1. Neither inferred triggered by this model revision. Serious safety/registration/funding failure triggers earlier reassessment including exit; no new lower threshold."
}
