# Execution Readiness Score Report

This report ranks model-produced watchlist tickers by pre-market execution readiness. It does not replace live orderbook/running-trade confirmation.

## Tier counts

- A_READY_WNS: 0
- B_WATCH_CONFIRM: 4
- C_CONDITIONAL: 6
- D_LOW_PRIORITY: 2

## Top candidates

| Rank | Ticker | ERS | Tier | Setup | nStrat | Trigger | Stop | RR | Warnings |
|---:|---|---:|---|---|---:|---:|---:|---:|---|
| 1 | DEWA | 71.43 | B_WATCH_CONFIRM | multi_strategy_confluence | 6 | 340.0 | 318.0 | 3.181818 | numeric_no_trade_reason_present;still_far_below_ma20 |
| 2 | SSMS | 67.32 | B_WATCH_CONFIRM | distressed_rebound | 5 | 755.0 | 710.0 | 5.888889 | numeric_no_trade_reason_present;still_far_below_ma20 |
| 3 | BUVA | 66.0 | B_WATCH_CONFIRM | distressed_rebound | 6 | 635.0 | 590.0 | 6.666667 | numeric_no_trade_reason_present;risk_above_ideal;trigger_not_close;still_far_below_ma20 |
| 4 | MSIN | 64.81 | B_WATCH_CONFIRM | distressed_rebound | 5 | 438.0 | 418.0 | 11.1 | numeric_no_trade_reason_present;trigger_not_close;still_far_below_ma20 |
| 5 | CDIA | 58.24 | C_CONDITIONAL | single_or_mixed_signal | 3 | 780.0 | 715.0 | 1.769231 | numeric_no_trade_reason_present;risk_above_ideal;still_far_below_ma20 |
| 6 | BNBR | 56.03 | C_CONDITIONAL | single_or_mixed_signal | 3 | 131.0 | 120.0 | 2.909091 | numeric_no_trade_reason_present;risk_above_ideal;still_far_below_ma20 |
| 7 | DSSA | 55.61 | C_CONDITIONAL | distressed_rebound | 5 | 464.0 | 430.0 | 11.058824 | numeric_no_trade_reason_present;risk_above_ideal;trigger_not_close;still_far_below_ma20 |
| 8 | KIJA | 53.33 | C_CONDITIONAL | distressed_rebound | 1 | 124.0 | 118.0 | 6.666667 | numeric_no_trade_reason_present;volume_ratio_weak;still_far_below_ma20 |
| 9 | CUAN | 51.11 | C_CONDITIONAL | multi_strategy_confluence | 4 | 530.0 | 486.0 | 3.75 | numeric_no_trade_reason_present;risk_above_ideal;trigger_not_close;still_far_below_ma20 |
| 10 | INET | 49.32 | C_CONDITIONAL | single_or_mixed_signal | 2 | 220.0 | 202.0 | 2.888889 | numeric_no_trade_reason_present;risk_above_ideal;volume_ratio_weak;still_far_below_ma20 |
| 11 | WBSA | 43.5 | D_LOW_PRIORITY | single_or_mixed_signal | 1 | 765.0 | 700.0 | 12.923077 | numeric_no_trade_reason_present;risk_above_ideal;trigger_not_close;still_far_below_ma20 |
| 12 | MBMA | 40.04 | D_LOW_PRIORITY | single_or_mixed_signal | 1 | 488.0 | 448.0 | 1.8 | numeric_no_trade_reason_present;risk_above_ideal;volume_ratio_weak;still_far_below_ma20 |

## Execution notes

- A tier means priority WNS, not automatic buy.
- Trigger tick area is where orderbook/running trade should be watched for acceptance/retest.
- If warnings include `numeric_no_trade_reason_present`, keep it watchlist-only unless live market confirmation is exceptional.