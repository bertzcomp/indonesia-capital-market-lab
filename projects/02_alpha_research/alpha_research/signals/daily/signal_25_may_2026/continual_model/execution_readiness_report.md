# Execution Readiness Score Report

This report ranks model-produced watchlist tickers by pre-market execution readiness. It does not replace live orderbook/running-trade confirmation.

## Tier counts

- A_READY_WNS: 0
- B_WATCH_CONFIRM: 3
- C_CONDITIONAL: 10
- D_LOW_PRIORITY: 4

## Top candidates

| Rank | Ticker | ERS | Tier | Setup | nStrat | Trigger | Stop | RR | Warnings |
|---:|---|---:|---|---|---:|---:|---:|---:|---|
| 1 | KIJA | 70.25 | B_WATCH_CONFIRM | distressed_rebound | 5 | 124.0 | 118.0 | 8.333333 | numeric_no_trade_reason_present;still_far_below_ma20 |
| 2 | BUVA | 62.7 | B_WATCH_CONFIRM | distressed_rebound | 5 | 745.0 | 685.0 | 5.083333 | numeric_no_trade_reason_present;risk_above_ideal;still_far_below_ma20 |
| 3 | BNBR | 60.21 | B_WATCH_CONFIRM | single_or_mixed_signal | 3 | 147.0 | 135.0 | 2.75 | numeric_no_trade_reason_present;risk_above_ideal;still_far_below_ma20 |
| 4 | MBMA | 59.78 | C_CONDITIONAL | single_or_mixed_signal | 2 | 494.0 | 454.0 | 2.65 | numeric_no_trade_reason_present;risk_above_ideal;still_far_below_ma20 |
| 5 | IRSX | 59.63 | C_CONDITIONAL | distressed_rebound | 1 | 338.0 | 316.0 | 1.727273 | numeric_no_trade_reason_present;risk_above_ideal;still_far_below_ma20 |
| 6 | BIPI | 59.58 | C_CONDITIONAL | single_or_mixed_signal | 2 | 190.0 | 174.0 | 3.25 | numeric_no_trade_reason_present;risk_above_ideal;still_far_below_ma20 |
| 7 | CDIA | 58.74 | C_CONDITIONAL | distressed_rebound | 5 | 775.0 | 710.0 | 4.0 | numeric_no_trade_reason_present;risk_above_ideal;volume_ratio_weak;still_far_below_ma20 |
| 8 | CUAN | 56.82 | C_CONDITIONAL | distressed_rebound | 5 | 540.0 | 496.0 | 6.704545 | numeric_no_trade_reason_present;risk_above_ideal;trigger_not_close;still_far_below_ma20 |
| 9 | DEWA | 56.0 | C_CONDITIONAL | single_or_mixed_signal | 1 | 388.0 | 356.0 | 3.4375 | numeric_no_trade_reason_present;risk_above_ideal;still_far_below_ma20 |
| 10 | DSSA | 54.65 | C_CONDITIONAL | distressed_rebound | 6 | 585.0 | 535.0 | 7.7 | numeric_no_trade_reason_present;risk_above_ideal;trigger_not_close;still_far_below_ma20 |
| 11 | TRIN | 49.78 | C_CONDITIONAL | single_or_mixed_signal | 1 | 515.0 | 472.0 | 2.55814 | numeric_no_trade_reason_present;risk_above_ideal;still_far_below_ma20 |
| 12 | NZIA | 46.23 | C_CONDITIONAL | distressed_rebound | 1 | 121.0 | 111.0 | 1.7 | numeric_no_trade_reason_present;risk_above_ideal;volume_ratio_weak;still_far_below_ma20 |
| 13 | WBSA | 45.19 | C_CONDITIONAL | single_or_mixed_signal | 1 | 770.0 | 705.0 | 9.076923 | numeric_no_trade_reason_present;risk_above_ideal;trigger_not_close;still_far_below_ma20 |
| 14 | DIVA | 44.67 | D_LOW_PRIORITY | single_or_mixed_signal | 1 | 142.0 | 130.0 | 3.166667 | numeric_no_trade_reason_present;risk_above_ideal;trigger_not_close |
| 15 | KOKA | 43.76 | D_LOW_PRIORITY | high_volume_event | 1 | 123.0 | 113.0 | 3.0 | numeric_no_trade_reason_present;risk_above_ideal;still_far_below_ma20 |
| 16 | NSSS | 43.68 | D_LOW_PRIORITY | distressed_rebound | 1 | 488.0 | 448.0 | 7.05 | numeric_no_trade_reason_present;risk_above_ideal;volume_ratio_weak;still_far_below_ma20 |
| 17 | UNSP | 43.64 | D_LOW_PRIORITY | single_or_mixed_signal | 1 | 254.0 | 232.0 | 1.727273 | numeric_no_trade_reason_present;risk_above_ideal;still_far_below_ma20 |

## Execution notes

- A tier means priority WNS, not automatic buy.
- Trigger tick area is where orderbook/running trade should be watched for acceptance/retest.
- If warnings include `numeric_no_trade_reason_present`, keep it watchlist-only unless live market confirmation is exceptional.