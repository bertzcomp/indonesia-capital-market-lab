# Numeric Trading Desk Report — 2026-05-26

This report is generated from live model scores, selected signal policy, canonical OHLCV, ATR, support/resistance, liquidity, and broker-flow diagnostics. It is not a simple BUY/SELL list; each plan is conditional on execution behaviour.

## Summary

| Plan quality | Count |
|---|---:|
| ACTIONABLE | 8 |
| CONDITIONAL | 13 |
| WATCHLIST_ONLY | 3 |
| NO_TRADE | 18 |

## DSSA — scalping_continual_defensive — ACTIONABLE

**Score:** 0.738 vs policy min 0.05 · **Close:** 432 · **ATR14:** 155.6 · **Volume ratio 20D:** 4.09 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 376–464, entry trigger **464**, stop **430**, risk 34 points (7.33%).

**Targets:** TP1 **545** (2.38R), TP2 **565** (2.97R), TP3 **820** (10.47R). Recommended base-case RR: **2.97R**.

**Why entry:** Hybrid entry uses close 432 and ATR14 155.6: buy zone 376–464. Entry is valid only if price can trade/hold around 464 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 430 is placed below support structure (432 / 432). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 545 (2.38R), TP2 565 (2.97R), TP3 820 (10.47R). Targets are ATR/structure capped for hold_days=1. ATR14=155.6, resistance_5/10/20/60=820/1,660/3,360/97,000. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## DSSA — momentum_5d_continual_defensive — ACTIONABLE

**Score:** 0.563 vs policy min 0.30 · **Close:** 432 · **ATR14:** 155.6 · **Volume ratio 20D:** 4.09 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 376–464, entry trigger **464**, stop **430**, risk 34 points (7.33%).

**Targets:** TP1 **545** (2.38R), TP2 **820** (10.47R), TP3 **840** (11.06R). Recommended base-case RR: **10.47R**.

**Why entry:** Hybrid entry uses close 432 and ATR14 155.6: buy zone 376–464. Entry is valid only if price can trade/hold around 464 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 430 is placed below support structure (432 / 432). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 545 (2.38R), TP2 820 (10.47R), TP3 840 (11.06R). Targets are ATR/structure capped for hold_days=3. ATR14=155.6, resistance_5/10/20/60=820/1,660/3,360/97,000. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## DSSA — swing_continual_defensive — ACTIONABLE

**Score:** 0.563 vs policy min 0.30 · **Close:** 432 · **ATR14:** 155.6 · **Volume ratio 20D:** 4.09 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 376–464, entry trigger **464**, stop **430**, risk 34 points (7.33%).

**Targets:** TP1 **545** (2.38R), TP2 **565** (2.97R), TP3 **820** (10.47R). Recommended base-case RR: **2.97R**.

**Why entry:** Hybrid entry uses close 432 and ATR14 155.6: buy zone 376–464. Entry is valid only if price can trade/hold around 464 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 430 is placed below support structure (432 / 432). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 545 (2.38R), TP2 565 (2.97R), TP3 820 (10.47R). Targets are ATR/structure capped for hold_days=1. ATR14=155.6, resistance_5/10/20/60=820/1,660/3,360/97,000. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## DSSA — momentum_10d_continual_aggressive — ACTIONABLE

**Score:** 0.539 vs policy min 0.30 · **Close:** 432 · **ATR14:** 155.6 · **Volume ratio 20D:** 4.09 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 376–464, entry trigger **464**, stop **430**, risk 34 points (7.33%).

**Targets:** TP1 **815** (10.32R), TP2 **820** (10.47R), TP3 **840** (11.06R). Recommended base-case RR: **10.47R**.

**Why entry:** Hybrid entry uses close 432 and ATR14 155.6: buy zone 376–464. Entry is valid only if price can trade/hold around 464 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 430 is placed below support structure (432 / 432). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 815 (10.32R), TP2 820 (10.47R), TP3 840 (11.06R). Targets are ATR/structure capped for hold_days=5. ATR14=155.6, resistance_5/10/20/60=820/1,660/3,360/97,000. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## MSIN — momentum_10d_continual_aggressive — ACTIONABLE

**Score:** 0.532 vs policy min 0.30 · **Close:** 420 · **ATR14:** 82.3 · **Volume ratio 20D:** 1.98 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 390–438, entry trigger **438**, stop **418**, risk 20 points (4.57%).

**Targets:** TP1 **625** (9.35R), TP2 **650** (10.60R), TP3 **660** (11.10R). Recommended base-case RR: **10.60R**.

**Why entry:** Hybrid entry uses close 420 and ATR14 82.3: buy zone 390–438. Entry is valid only if price can trade/hold around 438 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 418 is placed below support structure (420 / 420). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 625 (9.35R), TP2 650 (10.60R), TP3 660 (11.10R). Targets are ATR/structure capped for hold_days=5. ATR14=82.3, resistance_5/10/20/60=650/835/950/1,450. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## MSIN — momentum_5d_continual_defensive — ACTIONABLE

**Score:** 0.515 vs policy min 0.30 · **Close:** 420 · **ATR14:** 82.3 · **Volume ratio 20D:** 1.98 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 390–438, entry trigger **438**, stop **418**, risk 20 points (4.57%).

**Targets:** TP1 **480** (2.10R), TP2 **650** (10.60R), TP3 **660** (11.10R). Recommended base-case RR: **10.60R**.

**Why entry:** Hybrid entry uses close 420 and ATR14 82.3: buy zone 390–438. Entry is valid only if price can trade/hold around 438 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 418 is placed below support structure (420 / 420). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 480 (2.10R), TP2 650 (10.60R), TP3 660 (11.10R). Targets are ATR/structure capped for hold_days=3. ATR14=82.3, resistance_5/10/20/60=650/835/950/1,450. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## MSIN — swing_continual_defensive — ACTIONABLE

**Score:** 0.515 vs policy min 0.30 · **Close:** 420 · **ATR14:** 82.3 · **Volume ratio 20D:** 1.98 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 390–438, entry trigger **438**, stop **418**, risk 20 points (4.57%).

**Targets:** TP1 **480** (2.10R), TP2 **490** (2.60R), TP3 **645** (10.35R). Recommended base-case RR: **2.60R**.

**Why entry:** Hybrid entry uses close 420 and ATR14 82.3: buy zone 390–438. Entry is valid only if price can trade/hold around 438 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 418 is placed below support structure (420 / 420). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 480 (2.10R), TP2 490 (2.60R), TP3 645 (10.35R). Targets are ATR/structure capped for hold_days=1. ATR14=82.3, resistance_5/10/20/60=650/835/950/1,450. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## SSMS — momentum_10d_continual_aggressive — ACTIONABLE

**Score:** 0.508 vs policy min 0.30 · **Close:** 735 · **ATR14:** 87.1 · **Volume ratio 20D:** 1.54 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 700–755, entry trigger **755**, stop **710**, risk 45 points (5.96%).

**Targets:** TP1 **950** (4.33R), TP2 **995** (5.33R), TP3 **1,020** (5.89R). Recommended base-case RR: **5.33R**.

**Why entry:** Hybrid entry uses close 735 and ATR14 87.1: buy zone 700–755. Entry is valid only if price can trade/hold around 755 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 710 is placed below support structure (715 / 715). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 950 (4.33R), TP2 995 (5.33R), TP3 1,020 (5.89R). Targets are ATR/structure capped for hold_days=5. ATR14=87.1, resistance_5/10/20/60=995/1,420/1,470/1,800. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BUVA — ara_candidate_continual — CONDITIONAL

**Score:** 0.880 vs policy min 0.50 · **Close:** 610 · **ATR14:** 107.5 · **Volume ratio 20D:** 1.21 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 570–635, entry trigger **635**, stop **590**, risk 45 points (7.09%).

**Targets:** TP1 **690** (1.22R), TP2 **715** (1.78R), TP3 **905** (6.00R). Recommended base-case RR: **1.78R**.

**Why entry:** Hybrid entry uses close 610 and ATR14 107.5: buy zone 570–635. Entry is valid only if price can trade/hold around 635 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 590 is placed below support structure (595 / 595). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 690 (1.22R), TP2 715 (1.78R), TP3 905 (6.00R). Targets are ATR/structure capped for hold_days=1. ATR14=107.5, resistance_5/10/20/60=910/1,175/1,380/1,695. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.22R is below strategy minimum 1.25R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## BUVA — scalping_continual_defensive — CONDITIONAL

**Score:** 0.717 vs policy min 0.05 · **Close:** 610 · **ATR14:** 107.5 · **Volume ratio 20D:** 1.21 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 570–635, entry trigger **635**, stop **590**, risk 45 points (7.09%).

**Targets:** TP1 **690** (1.22R), TP2 **715** (1.78R), TP3 **905** (6.00R). Recommended base-case RR: **1.78R**.

**Why entry:** Hybrid entry uses close 610 and ATR14 107.5: buy zone 570–635. Entry is valid only if price can trade/hold around 635 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 590 is placed below support structure (595 / 595). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 690 (1.22R), TP2 715 (1.78R), TP3 905 (6.00R). Targets are ATR/structure capped for hold_days=1. ATR14=107.5, resistance_5/10/20/60=910/1,175/1,380/1,695. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.22R is below strategy minimum 1.25R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## DEWA — scalping_continual_defensive — CONDITIONAL

**Score:** 0.717 vs policy min 0.05 · **Close:** 330 · **ATR14:** 42.0 · **Volume ratio 20D:** 0.87 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 314–340, entry trigger **340**, stop **318**, risk 22 points (6.47%).

**Targets:** TP1 **382** (1.91R), TP2 **398** (2.64R), TP3 **410** (3.18R). Recommended base-case RR: **2.64R**.

**Why entry:** Hybrid entry uses close 330 and ATR14 42.0: buy zone 314–340. Entry is valid only if price can trade/hold around 340 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 318 is placed below support structure (320 / 320). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 382 (1.91R), TP2 398 (2.64R), TP3 410 (3.18R). Targets are ATR/structure capped for hold_days=1. ATR14=42.0, resistance_5/10/20/60=398/535/575/655. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## SSMS — scalping_continual_defensive — CONDITIONAL

**Score:** 0.705 vs policy min 0.05 · **Close:** 735 · **ATR14:** 87.1 · **Volume ratio 20D:** 1.54 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 700–755, entry trigger **755**, stop **710**, risk 45 points (5.96%).

**Targets:** TP1 **800** (1.00R), TP2 **835** (1.78R), TP3 **975** (4.89R). Recommended base-case RR: **1.78R**.

**Why entry:** Hybrid entry uses close 735 and ATR14 87.1: buy zone 700–755. Entry is valid only if price can trade/hold around 755 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 710 is placed below support structure (715 / 715). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 800 (1.00R), TP2 835 (1.78R), TP3 975 (4.89R). Targets are ATR/structure capped for hold_days=1. ATR14=87.1, resistance_5/10/20/60=995/1,420/1,470/1,800. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BUVA — momentum_5d_continual_defensive — CONDITIONAL

**Score:** 0.596 vs policy min 0.30 · **Close:** 610 · **ATR14:** 107.5 · **Volume ratio 20D:** 1.21 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 570–635, entry trigger **635**, stop **590**, risk 45 points (7.09%).

**Targets:** TP1 **690** (1.22R), TP2 **910** (6.11R), TP3 **935** (6.67R). Recommended base-case RR: **6.11R**.

**Why entry:** Hybrid entry uses close 610 and ATR14 107.5: buy zone 570–635. Entry is valid only if price can trade/hold around 635 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 590 is placed below support structure (595 / 595). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 690 (1.22R), TP2 910 (6.11R), TP3 935 (6.67R). Targets are ATR/structure capped for hold_days=3. ATR14=107.5, resistance_5/10/20/60=910/1,175/1,380/1,695. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.22R is below strategy minimum 1.25R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## BUVA — swing_continual_defensive — CONDITIONAL

**Score:** 0.596 vs policy min 0.30 · **Close:** 610 · **ATR14:** 107.5 · **Volume ratio 20D:** 1.21 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 570–635, entry trigger **635**, stop **590**, risk 45 points (7.09%).

**Targets:** TP1 **690** (1.22R), TP2 **715** (1.78R), TP3 **905** (6.00R). Recommended base-case RR: **1.78R**.

**Why entry:** Hybrid entry uses close 610 and ATR14 107.5: buy zone 570–635. Entry is valid only if price can trade/hold around 635 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 590 is placed below support structure (595 / 595). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 690 (1.22R), TP2 715 (1.78R), TP3 905 (6.00R). Targets are ATR/structure capped for hold_days=1. ATR14=107.5, resistance_5/10/20/60=910/1,175/1,380/1,695. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.22R is below strategy minimum 1.25R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## DEWA — momentum_5d_continual_defensive — CONDITIONAL

**Score:** 0.545 vs policy min 0.30 · **Close:** 330 · **ATR14:** 42.0 · **Volume ratio 20D:** 0.87 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 314–340, entry trigger **340**, stop **318**, risk 22 points (6.47%).

**Targets:** TP1 **398** (2.64R), TP2 **410** (3.18R), TP3 **422** (3.73R). Recommended base-case RR: **3.18R**.

**Why entry:** Hybrid entry uses close 330 and ATR14 42.0: buy zone 314–340. Entry is valid only if price can trade/hold around 340 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 318 is placed below support structure (320 / 320). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 398 (2.64R), TP2 410 (3.18R), TP3 422 (3.73R). Targets are ATR/structure capped for hold_days=3. ATR14=42.0, resistance_5/10/20/60=398/535/575/655. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## DEWA — swing_continual_defensive — CONDITIONAL

**Score:** 0.545 vs policy min 0.30 · **Close:** 330 · **ATR14:** 42.0 · **Volume ratio 20D:** 0.87 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 314–340, entry trigger **340**, stop **318**, risk 22 points (6.47%).

**Targets:** TP1 **382** (1.91R), TP2 **398** (2.64R), TP3 **410** (3.18R). Recommended base-case RR: **2.64R**.

**Why entry:** Hybrid entry uses close 330 and ATR14 42.0: buy zone 314–340. Entry is valid only if price can trade/hold around 340 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 318 is placed below support structure (320 / 320). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 382 (1.91R), TP2 398 (2.64R), TP3 410 (3.18R). Targets are ATR/structure capped for hold_days=1. ATR14=42.0, resistance_5/10/20/60=398/535/575/655. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## DEWA — momentum_10d_continual_aggressive — CONDITIONAL

**Score:** 0.536 vs policy min 0.30 · **Close:** 330 · **ATR14:** 42.0 · **Volume ratio 20D:** 0.87 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 314–340, entry trigger **340**, stop **318**, risk 22 points (6.47%).

**Targets:** TP1 **398** (2.64R), TP2 **410** (3.18R), TP3 **422** (3.73R). Recommended base-case RR: **3.18R**.

**Why entry:** Hybrid entry uses close 330 and ATR14 42.0: buy zone 314–340. Entry is valid only if price can trade/hold around 340 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 318 is placed below support structure (320 / 320). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 398 (2.64R), TP2 410 (3.18R), TP3 422 (3.73R). Targets are ATR/structure capped for hold_days=5. ATR14=42.0, resistance_5/10/20/60=398/535/575/655. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## SSMS — momentum_5d_continual_defensive — CONDITIONAL

**Score:** 0.503 vs policy min 0.30 · **Close:** 735 · **ATR14:** 87.1 · **Volume ratio 20D:** 1.54 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 700–755, entry trigger **755**, stop **710**, risk 45 points (5.96%).

**Targets:** TP1 **800** (1.00R), TP2 **995** (5.33R), TP3 **1,020** (5.89R). Recommended base-case RR: **5.33R**.

**Why entry:** Hybrid entry uses close 735 and ATR14 87.1: buy zone 700–755. Entry is valid only if price can trade/hold around 755 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 710 is placed below support structure (715 / 715). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 800 (1.00R), TP2 995 (5.33R), TP3 1,020 (5.89R). Targets are ATR/structure capped for hold_days=3. ATR14=87.1, resistance_5/10/20/60=995/1,420/1,470/1,800. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## SSMS — swing_continual_defensive — CONDITIONAL

**Score:** 0.503 vs policy min 0.30 · **Close:** 735 · **ATR14:** 87.1 · **Volume ratio 20D:** 1.54 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 700–755, entry trigger **755**, stop **710**, risk 45 points (5.96%).

**Targets:** TP1 **800** (1.00R), TP2 **835** (1.78R), TP3 **975** (4.89R). Recommended base-case RR: **1.78R**.

**Why entry:** Hybrid entry uses close 735 and ATR14 87.1: buy zone 700–755. Entry is valid only if price can trade/hold around 755 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 710 is placed below support structure (715 / 715). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 800 (1.00R), TP2 835 (1.78R), TP3 975 (4.89R). Targets are ATR/structure capped for hold_days=1. ATR14=87.1, resistance_5/10/20/60=995/1,420/1,470/1,800. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BUVA — position_continual — CONDITIONAL

**Score:** 0.305 vs policy min 0.30 · **Close:** 610 · **ATR14:** 107.5 · **Volume ratio 20D:** 1.21 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 570–635, entry trigger **635**, stop **590**, risk 45 points (7.09%).

**Targets:** TP1 **910** (6.11R), TP2 **935** (6.67R), TP3 **960** (7.22R). Recommended base-case RR: **6.67R**.

**Why entry:** Hybrid entry uses close 610 and ATR14 107.5: buy zone 570–635. Entry is valid only if price can trade/hold around 635 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 590 is placed below support structure (595 / 595). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 910 (6.11R), TP2 935 (6.67R), TP3 960 (7.22R). Targets are ATR/structure capped for hold_days=10. ATR14=107.5, resistance_5/10/20/60=910/1,175/1,380/1,695. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## DEWA — position_continual — CONDITIONAL

**Score:** 0.304 vs policy min 0.30 · **Close:** 330 · **ATR14:** 42.0 · **Volume ratio 20D:** 0.87 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 314–340, entry trigger **340**, stop **318**, risk 22 points (6.47%).

**Targets:** TP1 **398** (2.64R), TP2 **410** (3.18R), TP3 **422** (3.73R). Recommended base-case RR: **3.18R**.

**Why entry:** Hybrid entry uses close 330 and ATR14 42.0: buy zone 314–340. Entry is valid only if price can trade/hold around 340 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 318 is placed below support structure (320 / 320). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 398 (2.64R), TP2 410 (3.18R), TP3 422 (3.73R). Targets are ATR/structure capped for hold_days=10. ATR14=42.0, resistance_5/10/20/60=398/535/575/655. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## DSSA — position_continual — WATCHLIST_ONLY

**Score:** 0.300 vs policy min 0.30 · **Close:** 432 · **ATR14:** 155.6 · **Volume ratio 20D:** 4.09 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 376–464, entry trigger **464**, stop **430**, risk 34 points (7.33%).

**Targets:** TP1 **820** (10.47R), TP2 **840** (11.06R), TP3 **860** (11.65R). Recommended base-case RR: **11.06R**.

**Why entry:** Hybrid entry uses close 432 and ATR14 155.6: buy zone 376–464. Entry is valid only if price can trade/hold around 464 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 430 is placed below support structure (432 / 432). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 820 (10.47R), TP2 840 (11.06R), TP3 860 (11.65R). Targets are ATR/structure capped for hold_days=10. ATR14=155.6, resistance_5/10/20/60=820/1,660/3,360/97,000. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** score 0.300 below policy min_score 0.30

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Generic strategy rule.

---

## MSIN — position_continual — WATCHLIST_ONLY

**Score:** 0.293 vs policy min 0.30 · **Close:** 420 · **ATR14:** 82.3 · **Volume ratio 20D:** 1.98 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 390–438, entry trigger **438**, stop **418**, risk 20 points (4.57%).

**Targets:** TP1 **650** (10.60R), TP2 **660** (11.10R), TP3 **670** (11.60R). Recommended base-case RR: **11.10R**.

**Why entry:** Hybrid entry uses close 420 and ATR14 82.3: buy zone 390–438. Entry is valid only if price can trade/hold around 438 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 418 is placed below support structure (420 / 420). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 650 (10.60R), TP2 660 (11.10R), TP3 670 (11.60R). Targets are ATR/structure capped for hold_days=10. ATR14=82.3, resistance_5/10/20/60=650/835/950/1,450. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** score 0.293 below policy min_score 0.30

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Generic strategy rule.

---

## SSMS — position_continual — WATCHLIST_ONLY

**Score:** 0.293 vs policy min 0.30 · **Close:** 735 · **ATR14:** 87.1 · **Volume ratio 20D:** 1.54 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 700–755, entry trigger **755**, stop **710**, risk 45 points (5.96%).

**Targets:** TP1 **995** (5.33R), TP2 **1,020** (5.89R), TP3 **1,045** (6.44R). Recommended base-case RR: **5.89R**.

**Why entry:** Hybrid entry uses close 735 and ATR14 87.1: buy zone 700–755. Entry is valid only if price can trade/hold around 755 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 710 is placed below support structure (715 / 715). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 995 (5.33R), TP2 1,020 (5.89R), TP3 1,045 (6.44R). Targets are ATR/structure capped for hold_days=10. ATR14=87.1, resistance_5/10/20/60=995/1,420/1,470/1,800. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** score 0.293 below policy min_score 0.30

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Generic strategy rule.

---

## WBSA — scalping_continual_defensive — NO_TRADE

**Score:** 0.704 vs policy min 0.05 · **Close:** 660 · **ATR14:** 518.9 · **Volume ratio 20D:** 2.70 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 478–765, entry trigger **765**, stop **700**, risk 65 points (8.50%).

**Targets:** TP1 **1,025** (4.00R), TP2 **1,605** (12.92R), TP3 **1,640** (13.46R). Recommended base-case RR: **12.92R**.

**Why entry:** Hybrid entry uses close 660 and ATR14 518.9: buy zone 478–765. Entry is valid only if price can trade/hold around 765 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 700 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,025 (4.00R), TP2 1,605 (12.92R), TP3 1,640 (13.46R). Targets are ATR/structure capped for hold_days=1. ATR14=518.9, resistance_5/10/20/60=885/1,605/1,605/1,605. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 15.91% > max 8.00%; entry-to-stop risk 8.50% exceeds max strategy risk 8.00%; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## BNBR — momentum_5d_continual_defensive — NO_TRADE

**Score:** 0.538 vs policy min 0.30 · **Close:** 126 · **ATR14:** 20.9 · **Volume ratio 20D:** 0.74 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 118–131, entry trigger **131**, stop **120**, risk 11 points (8.40%).

**Targets:** TP1 **157** (2.36R), TP2 **163** (2.91R), TP3 **169** (3.45R). Recommended base-case RR: **2.91R**.

**Why entry:** Hybrid entry uses close 126 and ATR14 20.9: buy zone 118–131. Entry is valid only if price can trade/hold around 131 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 120 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 157 (2.36R), TP2 163 (2.91R), TP3 169 (3.45R). Targets are ATR/structure capped for hold_days=3. ATR14=20.9, resistance_5/10/20/60=157/218/240/240. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.40% exceeds max strategy risk 8.00%; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## BNBR — swing_continual_defensive — NO_TRADE

**Score:** 0.538 vs policy min 0.30 · **Close:** 126 · **ATR14:** 20.9 · **Volume ratio 20D:** 0.74 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 118–131, entry trigger **131**, stop **120**, risk 11 points (8.40%).

**Targets:** TP1 **152** (1.91R), TP2 **157** (2.36R), TP3 **158** (2.45R). Recommended base-case RR: **2.36R**.

**Why entry:** Hybrid entry uses close 126 and ATR14 20.9: buy zone 118–131. Entry is valid only if price can trade/hold around 131 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 120 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 152 (1.91R), TP2 157 (2.36R), TP3 158 (2.45R). Targets are ATR/structure capped for hold_days=1. ATR14=20.9, resistance_5/10/20/60=157/218/240/240. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.40% exceeds max strategy risk 8.00%; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## CUAN — momentum_10d_continual_aggressive — NO_TRADE

**Score:** 0.531 vs policy min 0.30 · **Close:** 505 · **ATR14:** 118.2 · **Volume ratio 20D:** 2.04 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 462–530, entry trigger **530**, stop **486**, risk 44 points (8.30%).

**Targets:** TP1 **670** (3.18R), TP2 **695** (3.75R), TP3 **720** (4.32R). Recommended base-case RR: **3.75R**.

**Why entry:** Hybrid entry uses close 505 and ATR14 118.2: buy zone 462–530. Entry is valid only if price can trade/hold around 530 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 486 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 670 (3.18R), TP2 695 (3.75R), TP3 720 (4.32R). Targets are ATR/structure capped for hold_days=5. ATR14=118.2, resistance_5/10/20/60=670/1,305/1,620/1,990. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.30% exceeds max strategy risk 8.00%; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## CDIA — momentum_10d_continual_aggressive — NO_TRADE

**Score:** 0.519 vs policy min 0.30 · **Close:** 755 · **ATR14:** 111.4 · **Volume ratio 20D:** 1.26 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 715–780, entry trigger **780**, stop **715**, risk 65 points (8.33%).

**Targets:** TP1 **875** (1.46R), TP2 **895** (1.77R), TP3 **940** (2.46R). Recommended base-case RR: **1.77R**.

**Why entry:** Hybrid entry uses close 755 and ATR14 111.4: buy zone 715–780. Entry is valid only if price can trade/hold around 780 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 715 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 875 (1.46R), TP2 895 (1.77R), TP3 940 (2.46R). Targets are ATR/structure capped for hold_days=5. ATR14=111.4, resistance_5/10/20/60=875/1,230/1,230/1,340. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.33% exceeds max strategy risk 8.00%; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## INET — momentum_10d_continual_aggressive — NO_TRADE

**Score:** 0.519 vs policy min 0.30 · **Close:** 214 · **ATR14:** 23.6 · **Volume ratio 20D:** 0.42 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 204–220, entry trigger **220**, stop **202**, risk 18 points (8.18%).

**Targets:** TP1 **262** (2.33R), TP2 **272** (2.89R), TP3 **282** (3.44R). Recommended base-case RR: **2.89R**.

**Why entry:** Hybrid entry uses close 214 and ATR14 23.6: buy zone 204–220. Entry is valid only if price can trade/hold around 220 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 202 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 262 (2.33R), TP2 272 (2.89R), TP3 282 (3.44R). Targets are ATR/structure capped for hold_days=5. ATR14=23.6, resistance_5/10/20/60=262/324/360/438. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.18% exceeds max strategy risk 8.00%; volume ratio 0.42 below required 0.60; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## CUAN — momentum_5d_continual_defensive — NO_TRADE

**Score:** 0.515 vs policy min 0.30 · **Close:** 505 · **ATR14:** 118.2 · **Volume ratio 20D:** 2.04 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 462–530, entry trigger **530**, stop **486**, risk 44 points (8.30%).

**Targets:** TP1 **670** (3.18R), TP2 **695** (3.75R), TP3 **720** (4.32R). Recommended base-case RR: **3.75R**.

**Why entry:** Hybrid entry uses close 505 and ATR14 118.2: buy zone 462–530. Entry is valid only if price can trade/hold around 530 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 486 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 670 (3.18R), TP2 695 (3.75R), TP3 720 (4.32R). Targets are ATR/structure capped for hold_days=3. ATR14=118.2, resistance_5/10/20/60=670/1,305/1,620/1,990. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.30% exceeds max strategy risk 8.00%; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## CUAN — swing_continual_defensive — NO_TRADE

**Score:** 0.515 vs policy min 0.30 · **Close:** 505 · **ATR14:** 118.2 · **Volume ratio 20D:** 2.04 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 462–530, entry trigger **530**, stop **486**, risk 44 points (8.30%).

**Targets:** TP1 **650** (2.73R), TP2 **670** (3.18R), TP3 **695** (3.75R). Recommended base-case RR: **3.18R**.

**Why entry:** Hybrid entry uses close 505 and ATR14 118.2: buy zone 462–530. Entry is valid only if price can trade/hold around 530 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 486 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 650 (2.73R), TP2 670 (3.18R), TP3 695 (3.75R). Targets are ATR/structure capped for hold_days=1. ATR14=118.2, resistance_5/10/20/60=670/1,305/1,620/1,990. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.30% exceeds max strategy risk 8.00%; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## CDIA — momentum_20d_continual_research — NO_TRADE

**Score:** 0.385 vs policy min 0.30 · **Close:** 755 · **ATR14:** 111.4 · **Volume ratio 20D:** 1.26 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 715–780, entry trigger **780**, stop **715**, risk 65 points (8.33%).

**Targets:** TP1 **875** (1.46R), TP2 **895** (1.77R), TP3 **940** (2.46R). Recommended base-case RR: **1.77R**.

**Why entry:** Hybrid entry uses close 755 and ATR14 111.4: buy zone 715–780. Entry is valid only if price can trade/hold around 780 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 715 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 875 (1.46R), TP2 895 (1.77R), TP3 940 (2.46R). Targets are ATR/structure capped for hold_days=10. ATR14=111.4, resistance_5/10/20/60=875/1,230/1,230/1,340. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** strategy policy has execution_enabled=false; entry-to-stop risk 8.33% exceeds max strategy risk 8.00%; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## MSIN — momentum_20d_continual_research — NO_TRADE

**Score:** 0.382 vs policy min 0.30 · **Close:** 420 · **ATR14:** 82.3 · **Volume ratio 20D:** 1.98 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 390–438, entry trigger **438**, stop **418**, risk 20 points (4.57%).

**Targets:** TP1 **650** (10.60R), TP2 **660** (11.10R), TP3 **670** (11.60R). Recommended base-case RR: **11.10R**.

**Why entry:** Hybrid entry uses close 420 and ATR14 82.3: buy zone 390–438. Entry is valid only if price can trade/hold around 438 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 418 is placed below support structure (420 / 420). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 650 (10.60R), TP2 660 (11.10R), TP3 670 (11.60R). Targets are ATR/structure capped for hold_days=10. ATR14=82.3, resistance_5/10/20/60=650/835/950/1,450. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** strategy policy has execution_enabled=false

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## KIJA — momentum_20d_continual_research — NO_TRADE

**Score:** 0.381 vs policy min 0.30 · **Close:** 122 · **ATR14:** 10.0 · **Volume ratio 20D:** 0.42 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 118–124, entry trigger **124**, stop **118**, risk 6 points (4.84%).

**Targets:** TP1 **130** (1.00R), TP2 **164** (6.67R), TP3 **167** (7.17R). Recommended base-case RR: **6.67R**.

**Why entry:** Hybrid entry uses close 122 and ATR14 10.0: buy zone 118–124. Entry is valid only if price can trade/hold around 124 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 118 is placed below support structure (119 / 119). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 130 (1.00R), TP2 164 (6.67R), TP3 167 (7.17R). Targets are ATR/structure capped for hold_days=10. ATR14=10.0, resistance_5/10/20/60=164/182/220/240. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** strategy policy has execution_enabled=false; TP1 reward/risk 1.00R is below strategy minimum 1.25R; volume ratio 0.42 below required 0.60

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## DEWA — momentum_20d_continual_research — NO_TRADE

**Score:** 0.354 vs policy min 0.30 · **Close:** 330 · **ATR14:** 42.0 · **Volume ratio 20D:** 0.87 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 314–340, entry trigger **340**, stop **318**, risk 22 points (6.47%).

**Targets:** TP1 **398** (2.64R), TP2 **410** (3.18R), TP3 **422** (3.73R). Recommended base-case RR: **3.18R**.

**Why entry:** Hybrid entry uses close 330 and ATR14 42.0: buy zone 314–340. Entry is valid only if price can trade/hold around 340 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 318 is placed below support structure (320 / 320). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 398 (2.64R), TP2 410 (3.18R), TP3 422 (3.73R). Targets are ATR/structure capped for hold_days=10. ATR14=42.0, resistance_5/10/20/60=398/535/575/655. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** strategy policy has execution_enabled=false; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## BUVA — momentum_20d_continual_research — NO_TRADE

**Score:** 0.337 vs policy min 0.30 · **Close:** 610 · **ATR14:** 107.5 · **Volume ratio 20D:** 1.21 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 570–635, entry trigger **635**, stop **590**, risk 45 points (7.09%).

**Targets:** TP1 **910** (6.11R), TP2 **935** (6.67R), TP3 **960** (7.22R). Recommended base-case RR: **6.67R**.

**Why entry:** Hybrid entry uses close 610 and ATR14 107.5: buy zone 570–635. Entry is valid only if price can trade/hold around 635 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 590 is placed below support structure (595 / 595). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 910 (6.11R), TP2 935 (6.67R), TP3 960 (7.22R). Targets are ATR/structure capped for hold_days=10. ATR14=107.5, resistance_5/10/20/60=910/1,175/1,380/1,695. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** strategy policy has execution_enabled=false; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## BNBR — position_continual — NO_TRADE

**Score:** 0.310 vs policy min 0.30 · **Close:** 126 · **ATR14:** 20.9 · **Volume ratio 20D:** 0.74 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 118–131, entry trigger **131**, stop **120**, risk 11 points (8.40%).

**Targets:** TP1 **157** (2.36R), TP2 **163** (2.91R), TP3 **169** (3.45R). Recommended base-case RR: **2.91R**.

**Why entry:** Hybrid entry uses close 126 and ATR14 20.9: buy zone 118–131. Entry is valid only if price can trade/hold around 131 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 120 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 157 (2.36R), TP2 163 (2.91R), TP3 169 (3.45R). Targets are ATR/structure capped for hold_days=10. ATR14=20.9, resistance_5/10/20/60=157/218/240/240. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.40% exceeds max strategy risk 8.00%; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## CUAN — position_continual — NO_TRADE

**Score:** 0.299 vs policy min 0.30 · **Close:** 505 · **ATR14:** 118.2 · **Volume ratio 20D:** 2.04 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 462–530, entry trigger **530**, stop **486**, risk 44 points (8.30%).

**Targets:** TP1 **670** (3.18R), TP2 **695** (3.75R), TP3 **720** (4.32R). Recommended base-case RR: **3.75R**.

**Why entry:** Hybrid entry uses close 505 and ATR14 118.2: buy zone 462–530. Entry is valid only if price can trade/hold around 530 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 486 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 670 (3.18R), TP2 695 (3.75R), TP3 720 (4.32R). Targets are ATR/structure capped for hold_days=10. ATR14=118.2, resistance_5/10/20/60=670/1,305/1,620/1,990. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.30% exceeds max strategy risk 8.00%; score 0.299 below policy min_score 0.30; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Generic strategy rule.

---

## MBMA — position_continual — NO_TRADE

**Score:** 0.297 vs policy min 0.30 · **Close:** 476 · **ATR14:** 54.2 · **Volume ratio 20D:** 0.69 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 456–488, entry trigger **488**, stop **448**, risk 40 points (8.20%).

**Targets:** TP1 **530** (1.05R), TP2 **560** (1.80R), TP3 **585** (2.42R). Recommended base-case RR: **1.80R**.

**Why entry:** Hybrid entry uses close 476 and ATR14 54.2: buy zone 456–488. Entry is valid only if price can trade/hold around 488 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 448 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 530 (1.05R), TP2 560 (1.80R), TP3 585 (2.42R). Targets are ATR/structure capped for hold_days=10. ATR14=54.2, resistance_5/10/20/60=510/680/770/945. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.20% exceeds max strategy risk 8.00%; score 0.297 below policy min_score 0.30; TP1 reward/risk 1.05R is below strategy minimum 1.25R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Generic strategy rule.

---

## CDIA — position_continual — NO_TRADE

**Score:** 0.296 vs policy min 0.30 · **Close:** 755 · **ATR14:** 111.4 · **Volume ratio 20D:** 1.26 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 715–780, entry trigger **780**, stop **715**, risk 65 points (8.33%).

**Targets:** TP1 **875** (1.46R), TP2 **895** (1.77R), TP3 **940** (2.46R). Recommended base-case RR: **1.77R**.

**Why entry:** Hybrid entry uses close 755 and ATR14 111.4: buy zone 715–780. Entry is valid only if price can trade/hold around 780 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 715 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 875 (1.46R), TP2 895 (1.77R), TP3 940 (2.46R). Targets are ATR/structure capped for hold_days=10. ATR14=111.4, resistance_5/10/20/60=875/1,230/1,230/1,340. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.33% exceeds max strategy risk 8.00%; score 0.296 below policy min_score 0.30; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Generic strategy rule.

---

## INET — position_continual — NO_TRADE

**Score:** 0.290 vs policy min 0.30 · **Close:** 214 · **ATR14:** 23.6 · **Volume ratio 20D:** 0.42 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 204–220, entry trigger **220**, stop **202**, risk 18 points (8.18%).

**Targets:** TP1 **262** (2.33R), TP2 **272** (2.89R), TP3 **282** (3.44R). Recommended base-case RR: **2.89R**.

**Why entry:** Hybrid entry uses close 214 and ATR14 23.6: buy zone 204–220. Entry is valid only if price can trade/hold around 220 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 202 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 262 (2.33R), TP2 272 (2.89R), TP3 282 (3.44R). Targets are ATR/structure capped for hold_days=10. ATR14=23.6, resistance_5/10/20/60=262/324/360/438. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.18% exceeds max strategy risk 8.00%; score 0.290 below policy min_score 0.30; volume ratio 0.42 below required 0.60; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Generic strategy rule.

---
