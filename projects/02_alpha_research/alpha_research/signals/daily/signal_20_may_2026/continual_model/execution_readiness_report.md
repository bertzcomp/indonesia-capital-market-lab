# Execution Readiness Score Report

This report ranks model-produced watchlist tickers by pre-market execution readiness. It does not replace live orderbook/running-trade confirmation.

## Tier counts

- A_READY_WNS: 0
- B_WATCH_CONFIRM: 9
- C_CONDITIONAL: 10
- D_LOW_PRIORITY: 0

## Top candidates

| Rank | Ticker | ERS | Tier | Setup | nStrat | Trigger | Stop | RR | Warnings |
|---:|---|---:|---|---|---:|---:|---:|---:|---|
| 1 | MBMA | 73.62 | B_WATCH_CONFIRM | distressed_rebound | 6 | 486.0 | 462.0 | 8.083333 | numeric_no_trade_reason_present;still_far_below_ma20 |
| 2 | CUAN | 72.11 | B_WATCH_CONFIRM | distressed_rebound | 5 | 675.0 | 635.0 | 15.75 | numeric_no_trade_reason_present;still_far_below_ma20 |
| 3 | BUMI | 68.33 | B_WATCH_CONFIRM | single_or_mixed_signal | 2 | 189.0 | 177.0 | 4.083333 | numeric_no_trade_reason_present |
| 4 | DEWA | 67.54 | B_WATCH_CONFIRM | single_or_mixed_signal | 1 | 396.0 | 372.0 | 5.791667 | numeric_no_trade_reason_present;still_far_below_ma20 |
| 5 | NCKL | 67.13 | B_WATCH_CONFIRM | single_or_mixed_signal | 1 | 885.0 | 845.0 | 4.625 | numeric_no_trade_reason_present;still_far_below_ma20 |
| 6 | BUVA | 65.32 | B_WATCH_CONFIRM | single_or_mixed_signal | 1 | 880.0 | 845.0 | 8.428571 | numeric_no_trade_reason_present;still_far_below_ma20 |
| 7 | PSAB | 63.73 | B_WATCH_CONFIRM | single_or_mixed_signal | 2 | 420.0 | 402.0 | 8.333333 | numeric_no_trade_reason_present;still_far_below_ma20 |
| 8 | FOLK | 63.05 | B_WATCH_CONFIRM | single_or_mixed_signal | 2 | 260.0 | 244.0 | 6.25 | numeric_no_trade_reason_present;still_far_below_ma20 |
| 9 | DSSA | 61.97 | B_WATCH_CONFIRM | distressed_rebound | 6 | 800.0 | 745.0 | 15.636364 | numeric_no_trade_reason_present;risk_above_ideal;trigger_not_close;still_far_below_ma20 |
| 10 | BANK | 58.59 | C_CONDITIONAL | single_or_mixed_signal | 1 | 394.0 | 376.0 | 13.111111 | numeric_no_trade_reason_present;still_far_below_ma20 |
| 11 | KOKA | 58.13 | C_CONDITIONAL | distressed_rebound | 2 | 131.0 | 122.0 | 5.0 | numeric_no_trade_reason_present;risk_above_ideal;still_far_below_ma20 |
| 12 | BEEF | 57.92 | C_CONDITIONAL | single_or_mixed_signal | 1 | 162.0 | 150.0 | 3.833333 | numeric_no_trade_reason_present;risk_above_ideal;still_far_below_ma20 |
| 13 | PBSA | 57.84 | C_CONDITIONAL | single_or_mixed_signal | 2 | 795.0 | 730.0 | 3.923077 | numeric_no_trade_reason_present;risk_above_ideal;still_far_below_ma20 |
| 14 | NSSS | 57.7 | C_CONDITIONAL | single_or_mixed_signal | 2 | 625.0 | 590.0 | 7.0 | numeric_no_trade_reason_present;volume_ratio_weak;still_far_below_ma20 |
| 15 | SOFA | 56.48 | C_CONDITIONAL | single_or_mixed_signal | 1 | 332.0 | 322.0 | 9.4 | numeric_no_trade_reason_present;still_far_below_ma20 |
| 16 | NICL | 54.17 | C_CONDITIONAL | single_or_mixed_signal | 2 | 655.0 | 620.0 | 1.714286 | numeric_no_trade_reason_present;volume_ratio_weak;still_far_below_ma20 |
| 17 | UNSP | 53.24 | C_CONDITIONAL | single_or_mixed_signal | 2 | 282.0 | 258.0 | 3.75 | numeric_no_trade_reason_present;risk_above_ideal;still_far_below_ma20 |
| 18 | TRUE | 48.56 | C_CONDITIONAL | single_or_mixed_signal | 2 | 123.0 | 113.0 | 4.7 | numeric_no_trade_reason_present;risk_above_ideal;volume_ratio_weak;still_far_below_ma20 |
| 19 | BULL | 46.21 | C_CONDITIONAL | single_or_mixed_signal | 1 | 414.0 | 380.0 | 1.705882 | numeric_no_trade_reason_present;risk_above_ideal |

## Execution notes

- A tier means priority WNS, not automatic buy.
- Trigger tick area is where orderbook/running trade should be watched for acceptance/retest.
- If warnings include `numeric_no_trade_reason_present`, keep it watchlist-only unless live market confirmation is exceptional.