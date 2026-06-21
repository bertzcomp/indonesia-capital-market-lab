# Execution Readiness Score Report

This report ranks model-produced watchlist tickers by pre-market execution readiness. It does not replace live orderbook/running-trade confirmation.

## Tier counts

- A_READY_WNS: 0
- B_WATCH_CONFIRM: 6
- C_CONDITIONAL: 10
- D_LOW_PRIORITY: 2

## Top candidates

| Rank | Ticker | ERS | Tier | Setup | nStrat | Trigger | Stop | RR | Warnings |
|---:|---|---:|---|---|---:|---:|---:|---:|---|
| 1 | CUAN | 69.71 | B_WATCH_CONFIRM | distressed_rebound | 7 | 775.0 | 720.0 | 9.636364 | numeric_no_trade_reason_present;risk_above_ideal;still_far_below_ma20 |
| 2 | UNSP | 67.04 | B_WATCH_CONFIRM | single_or_mixed_signal | 3 | 294.0 | 286.0 | 12.25 | numeric_no_trade_reason_present;still_far_below_ma20 |
| 3 | DSSA | 65.6 | B_WATCH_CONFIRM | distressed_rebound | 6 | 930.0 | 875.0 | 14.545455 | numeric_no_trade_reason_present;trigger_not_close;still_far_below_ma20 |
| 4 | SIMP | 64.81 | B_WATCH_CONFIRM | multi_strategy_confluence | 5 | 615.0 | 585.0 | 5.666667 | numeric_no_trade_reason_present;still_far_below_ma20 |
| 5 | BANK | 62.97 | B_WATCH_CONFIRM | single_or_mixed_signal | 3 | 432.0 | 412.0 | 10.4 | numeric_no_trade_reason_present;still_far_below_ma20 |
| 6 | MBMA | 62.84 | B_WATCH_CONFIRM | single_or_mixed_signal | 2 | 550.0 | 505.0 | 2.888889 | numeric_no_trade_reason_present;risk_above_ideal;still_far_below_ma20 |
| 7 | TIRA | 58.64 | C_CONDITIONAL | distressed_rebound | 3 | 625.0 | 575.0 | 5.2 | numeric_no_trade_reason_present;risk_above_ideal;still_far_below_ma20 |
| 8 | PBSA | 54.32 | C_CONDITIONAL | single_or_mixed_signal | 1 | 860.0 | 815.0 | 6.0 | numeric_no_trade_reason_present;still_far_below_ma20 |
| 9 | MSIN | 52.5 | C_CONDITIONAL | single_or_mixed_signal | 2 | 650.0 | 595.0 | 3.363636 | numeric_no_trade_reason_present;risk_above_ideal;volume_ratio_weak;still_far_below_ma20 |
| 10 | TRIN | 50.78 | C_CONDITIONAL | single_or_mixed_signal | 1 | 585.0 | 535.0 | 3.1 | numeric_no_trade_reason_present;risk_above_ideal;still_far_below_ma20 |
| 11 | BNBR | 50.34 | C_CONDITIONAL | single_or_mixed_signal | 1 | 165.0 | 153.0 | 1.75 | numeric_no_trade_reason_present;risk_above_ideal;volume_ratio_weak;still_far_below_ma20 |
| 12 | GPSO | 48.57 | C_CONDITIONAL | single_or_mixed_signal | 1 | 490.0 | 450.0 | 1.75 | numeric_no_trade_reason_present;risk_above_ideal |
| 13 | CYBR | 47.56 | C_CONDITIONAL | distressed_rebound | 2 | 660.0 | 605.0 | 1.727273 | numeric_no_trade_reason_present;risk_above_ideal;still_far_below_ma20 |
| 14 | BEEF | 46.77 | C_CONDITIONAL | high_volume_event | 1 | 173.0 | 159.0 | 3.214286 | numeric_no_trade_reason_present;risk_above_ideal;still_far_below_ma20 |
| 15 | BKDP | 46.73 | C_CONDITIONAL | high_volume_event | 1 | 114.0 | 104.0 | 1.7 | numeric_no_trade_reason_present;risk_above_ideal |
| 16 | BULL | 45.91 | C_CONDITIONAL | single_or_mixed_signal | 1 | 448.0 | 412.0 | 3.25 | numeric_no_trade_reason_present;risk_above_ideal |
| 17 | PACK | 43.7 | D_LOW_PRIORITY | single_or_mixed_signal | 1 | 350.0 | 322.0 | 1.714286 | numeric_no_trade_reason_present;risk_above_ideal;volume_ratio_weak |
| 18 | NSSS | 40.24 | D_LOW_PRIORITY | single_or_mixed_signal | 1 | 715.0 | 655.0 | 2.75 | numeric_no_trade_reason_present;risk_above_ideal;volume_ratio_weak |

## Execution notes

- A tier means priority WNS, not automatic buy.
- Trigger tick area is where orderbook/running trade should be watched for acceptance/retest.
- If warnings include `numeric_no_trade_reason_present`, keep it watchlist-only unless live market confirmation is exceptional.