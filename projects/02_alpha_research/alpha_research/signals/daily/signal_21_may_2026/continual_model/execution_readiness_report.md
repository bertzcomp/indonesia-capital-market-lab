# Execution Readiness Score Report

This report ranks model-produced watchlist tickers by pre-market execution readiness. It does not replace live orderbook/running-trade confirmation.

## Tier counts

- A_READY_WNS: 0
- B_WATCH_CONFIRM: 6
- C_CONDITIONAL: 9
- D_LOW_PRIORITY: 1

## Top candidates

| Rank | Ticker | ERS | Tier | Setup | nStrat | Trigger | Stop | RR | Warnings |
|---:|---|---:|---|---|---:|---:|---:|---:|---|
| 1 | CUAN | 67.65 | B_WATCH_CONFIRM | distressed_rebound | 6 | 615.0 | 570.0 | 15.333333 | numeric_no_trade_reason_present;risk_above_ideal;trigger_not_close;still_far_below_ma20 |
| 2 | MBMA | 65.23 | B_WATCH_CONFIRM | distressed_rebound | 5 | 472.0 | 434.0 | 5.078947 | numeric_no_trade_reason_present;risk_above_ideal;still_far_below_ma20 |
| 3 | SSMS | 64.72 | B_WATCH_CONFIRM | multi_strategy_confluence | 4 | 945.0 | 910.0 | 13.571429 | numeric_no_trade_reason_present;still_far_below_ma20 |
| 4 | UNSP | 63.69 | B_WATCH_CONFIRM | distressed_rebound | 3 | 256.0 | 248.0 | 14.5 | numeric_no_trade_reason_present;still_far_below_ma20 |
| 5 | CDIA | 61.16 | B_WATCH_CONFIRM | single_or_mixed_signal | 2 | 815.0 | 770.0 | 9.222222 | numeric_no_trade_reason_present;still_far_below_ma20 |
| 6 | PSAB | 60.85 | B_WATCH_CONFIRM | single_or_mixed_signal | 2 | 398.0 | 376.0 | 8.272727 | numeric_no_trade_reason_present;still_far_below_ma20 |
| 7 | BUVA | 58.78 | C_CONDITIONAL | distressed_rebound | 2 | 840.0 | 770.0 | 4.785714 | numeric_no_trade_reason_present;risk_above_ideal;still_far_below_ma20 |
| 8 | DEWA | 58.52 | C_CONDITIONAL | single_or_mixed_signal | 1 | 386.0 | 354.0 | 4.5 | numeric_no_trade_reason_present;risk_above_ideal;still_far_below_ma20 |
| 9 | NICL | 57.06 | C_CONDITIONAL | distressed_rebound | 3 | 595.0 | 555.0 | 7.0 | numeric_no_trade_reason_present;risk_above_ideal;volume_ratio_weak;still_far_below_ma20 |
| 10 | KOKA | 56.5 | C_CONDITIONAL | distressed_rebound | 3 | 124.0 | 114.0 | 5.4 | numeric_no_trade_reason_present;risk_above_ideal;still_far_below_ma20 |
| 11 | BIPI | 55.45 | C_CONDITIONAL | single_or_mixed_signal | 1 | 208.0 | 191.0 | 3.764706 | numeric_no_trade_reason_present;risk_above_ideal;still_far_below_ma20 |
| 12 | DSSA | 55.15 | C_CONDITIONAL | distressed_rebound | 4 | 755.0 | 690.0 | 11.846154 | numeric_no_trade_reason_present;risk_above_ideal;trigger_not_close;still_far_below_ma20 |
| 13 | SIMP | 52.39 | C_CONDITIONAL | single_or_mixed_signal | 1 | 575.0 | 525.0 | 3.6 | numeric_no_trade_reason_present;risk_above_ideal;still_far_below_ma20 |
| 14 | NSSS | 51.58 | C_CONDITIONAL | single_or_mixed_signal | 3 | 585.0 | 535.0 | 5.3 | numeric_no_trade_reason_present;risk_above_ideal;volume_ratio_weak;still_far_below_ma20 |
| 15 | ASPR | 48.67 | C_CONDITIONAL | high_volume_event | 1 | 408.0 | 374.0 | 1.705882 | numeric_no_trade_reason_present;risk_above_ideal |
| 16 | WBSA | 43.63 | D_LOW_PRIORITY | high_volume_event | 1 | 925.0 | 850.0 | 9.6 | numeric_no_trade_reason_present;risk_above_ideal;trigger_not_close;still_far_below_ma20 |

## Execution notes

- A tier means priority WNS, not automatic buy.
- Trigger tick area is where orderbook/running trade should be watched for acceptance/retest.
- If warnings include `numeric_no_trade_reason_present`, keep it watchlist-only unless live market confirmation is exceptional.