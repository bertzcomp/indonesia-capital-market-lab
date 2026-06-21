# Numeric Trading Desk Report — 2026-06-12

This report is generated from live model scores, selected signal policy, canonical OHLCV, ATR, support/resistance, liquidity, and broker-flow diagnostics. It is not a simple BUY/SELL list; each plan is conditional on execution behaviour.

## Summary

| Plan quality | Count |
|---|---:|
| CONDITIONAL | 2 |
| WATCHLIST_ONLY | 3 |
| NO_TRADE | 37 |

## PSAB — scalping_continual_defensive — CONDITIONAL

**Score:** 0.668 vs policy min 0.05 · **Close:** 468 · **ATR14:** 53.6 · **Volume ratio 20D:** 0.30 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 448–480, entry trigger **480**, stop **448**, risk 32 points (6.67%).

**Targets:** TP1 **535** (1.72R), TP2 **555** (2.34R), TP3 **560** (2.50R). Recommended base-case RR: **2.34R**.

**Why entry:** Hybrid entry uses close 468 and ATR14 53.6: buy zone 448–480. Entry is valid only if price can trade/hold around 480 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 448 is placed below support structure (450 / 360). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 535 (1.72R), TP2 555 (2.34R), TP3 560 (2.50R). Targets are ATR/structure capped for hold_days=1. ATR14=53.6, resistance_5/10/20/60=555/560/560/590. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** volume ratio 0.30 below required 0.60; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## RSCH — momentum_10d_continual_aggressive — CONDITIONAL

**Score:** 0.356 vs policy min 0.30 · **Close:** 316 · **ATR14:** 17.3 · **Volume ratio 20D:** 0.76 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 308–320, entry trigger **320**, stop **298**, risk 22 points (6.88%).

**Targets:** TP1 **342** (1.00R), TP2 **390** (3.18R), TP3 **394** (3.36R). Recommended base-case RR: **3.18R**.

**Why entry:** Hybrid entry uses close 316 and ATR14 17.3: buy zone 308–320. Entry is valid only if price can trade/hold around 320 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 298 uses 1.20×ATR14 volatility cap. Thesis invalidates if the move reverses beyond normal volatility. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 342 (1.00R), TP2 390 (3.18R), TP3 394 (3.36R). Targets are ATR/structure capped for hold_days=5. ATR14=17.3, resistance_5/10/20/60=322/322/322/394. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## ARCI — position_continual — WATCHLIST_ONLY

**Score:** 0.289 vs policy min 0.30 · **Close:** 975 · **ATR14:** 104.6 · **Volume ratio 20D:** 1.62 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 935–1,000, entry trigger **1,000**, stop **920**, risk 80 points (8.00%).

**Targets:** TP1 **1,240** (3.00R), TP2 **1,280** (3.50R), TP3 **1,320** (4.00R). Recommended base-case RR: **3.50R**.

**Why entry:** Hybrid entry uses close 975 and ATR14 104.6: buy zone 935–1,000. Entry is valid only if price can trade/hold around 1,000 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 920 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,240 (3.00R), TP2 1,280 (3.50R), TP3 1,320 (4.00R). Targets are ATR/structure capped for hold_days=10. ATR14=104.6, resistance_5/10/20/60=1,015/1,240/1,475/1,840. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** score 0.289 below policy min_score 0.30

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Generic strategy rule.

---

## ARCI — momentum_5d_continual_defensive — WATCHLIST_ONLY

**Score:** 0.244 vs policy min 0.30 · **Close:** 975 · **ATR14:** 104.6 · **Volume ratio 20D:** 1.62 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 935–1,000, entry trigger **1,000**, stop **920**, risk 80 points (8.00%).

**Targets:** TP1 **1,185** (2.31R), TP2 **1,240** (3.00R), TP3 **1,280** (3.50R). Recommended base-case RR: **3.00R**.

**Why entry:** Hybrid entry uses close 975 and ATR14 104.6: buy zone 935–1,000. Entry is valid only if price can trade/hold around 1,000 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 920 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,185 (2.31R), TP2 1,240 (3.00R), TP3 1,280 (3.50R). Targets are ATR/structure capped for hold_days=3. ATR14=104.6, resistance_5/10/20/60=1,015/1,240/1,475/1,840. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** score 0.244 below policy min_score 0.30

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Generic strategy rule.

---

## ARCI — swing_continual_defensive — WATCHLIST_ONLY

**Score:** 0.244 vs policy min 0.30 · **Close:** 975 · **ATR14:** 104.6 · **Volume ratio 20D:** 1.62 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 935–1,000, entry trigger **1,000**, stop **920**, risk 80 points (8.00%).

**Targets:** TP1 **1,080** (1.00R), TP2 **1,190** (2.38R), TP3 **1,240** (3.00R). Recommended base-case RR: **2.38R**.

**Why entry:** Hybrid entry uses close 975 and ATR14 104.6: buy zone 935–1,000. Entry is valid only if price can trade/hold around 1,000 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 920 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,080 (1.00R), TP2 1,190 (2.38R), TP3 1,240 (3.00R). Targets are ATR/structure capped for hold_days=1. ATR14=104.6, resistance_5/10/20/60=1,015/1,240/1,475/1,840. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** score 0.244 below policy min_score 0.30; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Generic strategy rule.

---

## BABY — ara_candidate_continual — NO_TRADE

**Score:** 0.864 vs policy min 0.50 · **Close:** 200 · **ATR14:** 20.4 · **Volume ratio 20D:** 4.07 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 192–206, entry trigger **206**, stop **189**, risk 17 points (8.25%).

**Targets:** TP1 **224** (1.06R), TP2 **244** (2.24R), TP3 **254** (2.82R). Recommended base-case RR: **2.24R**.

**Why entry:** Hybrid entry uses close 200 and ATR14 20.4: buy zone 192–206. Entry is valid only if price can trade/hold around 206 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 189 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 224 (1.06R), TP2 244 (2.24R), TP3 254 (2.82R). Targets are ATR/structure capped for hold_days=1. ATR14=20.4, resistance_5/10/20/60=254/254/254/450. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.25% exceeds max strategy risk 8.00%; TP1 reward/risk 1.06R is below strategy minimum 1.25R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## GULA — momentum_10d_continual_aggressive — NO_TRADE

**Score:** 0.419 vs policy min 0.30 · **Close:** 575 · **ATR14:** 49.2 · **Volume ratio 20D:** 1.12 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 555–585, entry trigger **585**, stop **535**, risk 50 points (8.55%).

**Targets:** TP1 **635** (1.00R), TP2 **670** (1.70R), TP3 **705** (2.40R). Recommended base-case RR: **1.70R**.

**Why entry:** Hybrid entry uses close 575 and ATR14 49.2: buy zone 555–585. Entry is valid only if price can trade/hold around 585 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 535 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 635 (1.00R), TP2 670 (1.70R), TP3 705 (2.40R). Targets are ATR/structure capped for hold_days=5. ATR14=49.2, resistance_5/10/20/60=610/610/610/610. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.55% exceeds max strategy risk 8.00%; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## SUPA — momentum_10d_continual_aggressive — NO_TRADE

**Score:** 0.368 vs policy min 0.30 · **Close:** 615 · **ATR14:** 62.9 · **Volume ratio 20D:** 1.06 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 590–630, entry trigger **630**, stop **575**, risk 55 points (8.73%).

**Targets:** TP1 **685** (1.00R), TP2 **725** (1.73R), TP3 **765** (2.45R). Recommended base-case RR: **1.73R**.

**Why entry:** Hybrid entry uses close 615 and ATR14 62.9: buy zone 590–630. Entry is valid only if price can trade/hold around 630 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 575 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 685 (1.00R), TP2 725 (1.73R), TP3 765 (2.45R). Targets are ATR/structure capped for hold_days=5. ATR14=62.9, resistance_5/10/20/60=675/880/905/970. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.73% exceeds max strategy risk 8.00%; TP1 reward/risk 1.00R is below strategy minimum 1.25R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## SUPA — scalping_continual_defensive — NO_TRADE

**Score:** 0.349 vs policy min 0.05 · **Close:** 615 · **ATR14:** 62.9 · **Volume ratio 20D:** 1.06 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 590–630, entry trigger **630**, stop **575**, risk 55 points (8.73%).

**Targets:** TP1 **685** (1.00R), TP2 **725** (1.73R), TP3 **765** (2.45R). Recommended base-case RR: **1.73R**.

**Why entry:** Hybrid entry uses close 615 and ATR14 62.9: buy zone 590–630. Entry is valid only if price can trade/hold around 630 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 575 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 685 (1.00R), TP2 725 (1.73R), TP3 765 (2.45R). Targets are ATR/structure capped for hold_days=1. ATR14=62.9, resistance_5/10/20/60=675/880/905/970. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.73% exceeds max strategy risk 8.00%; TP1 reward/risk 1.00R is below strategy minimum 1.25R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## BAIK — momentum_10d_continual_aggressive — NO_TRADE

**Score:** 0.347 vs policy min 0.30 · **Close:** 680 · **ATR14:** 56.9 · **Volume ratio 20D:** 4.99 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 660–695, entry trigger **695**, stop **635**, risk 60 points (8.63%).

**Targets:** TP1 **755** (1.00R), TP2 **800** (1.75R), TP3 **840** (2.42R). Recommended base-case RR: **1.75R**.

**Why entry:** Hybrid entry uses close 680 and ATR14 56.9: buy zone 660–695. Entry is valid only if price can trade/hold around 695 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 635 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 755 (1.00R), TP2 800 (1.75R), TP3 840 (2.42R). Targets are ATR/structure capped for hold_days=5. ATR14=56.9, resistance_5/10/20/60=690/690/690/750. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.63% exceeds max strategy risk 8.00%; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## OASA — momentum_10d_continual_aggressive — NO_TRADE

**Score:** 0.346 vs policy min 0.30 · **Close:** 260 · **ATR14:** 38.3 · **Volume ratio 20D:** 0.67 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 246–268, entry trigger **268**, stop **246**, risk 22 points (8.21%).

**Targets:** TP1 **290** (1.00R), TP2 **372** (4.73R), TP3 **384** (5.27R). Recommended base-case RR: **4.73R**.

**Why entry:** Hybrid entry uses close 260 and ATR14 38.3: buy zone 246–268. Entry is valid only if price can trade/hold around 268 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 246 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 290 (1.00R), TP2 372 (4.73R), TP3 384 (5.27R). Targets are ATR/structure capped for hold_days=5. ATR14=38.3, resistance_5/10/20/60=268/372/432/466. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.21% exceeds max strategy risk 8.00%; TP1 reward/risk 1.00R is below strategy minimum 1.25R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## GPSO — momentum_10d_continual_aggressive — NO_TRADE

**Score:** 0.342 vs policy min 0.30 · **Close:** 336 · **ATR14:** 31.0 · **Volume ratio 20D:** 2.32 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 324–344, entry trigger **344**, stop **316**, risk 28 points (8.14%).

**Targets:** TP1 **380** (1.29R), TP2 **392** (1.71R), TP3 **412** (2.43R). Recommended base-case RR: **1.71R**.

**Why entry:** Hybrid entry uses close 336 and ATR14 31.0: buy zone 324–344. Entry is valid only if price can trade/hold around 344 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 316 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 380 (1.29R), TP2 392 (1.71R), TP3 412 (2.43R). Targets are ATR/structure capped for hold_days=5. ATR14=31.0, resistance_5/10/20/60=380/520/520/520. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.14% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## SGER — momentum_10d_continual_aggressive — NO_TRADE

**Score:** 0.341 vs policy min 0.30 · **Close:** 406 · **ATR14:** 38.9 · **Volume ratio 20D:** 5.79 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 392–414, entry trigger **414**, stop **380**, risk 34 points (8.21%).

**Targets:** TP1 **476** (1.82R), TP2 **494** (2.35R), TP3 **496** (2.41R). Recommended base-case RR: **2.35R**.

**Why entry:** Hybrid entry uses close 406 and ATR14 38.9: buy zone 392–414. Entry is valid only if price can trade/hold around 414 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 380 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 476 (1.82R), TP2 494 (2.35R), TP3 496 (2.41R). Targets are ATR/structure capped for hold_days=5. ATR14=38.9, resistance_5/10/20/60=406/406/406/476. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.21% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## ESSA — scalping_continual_defensive — NO_TRADE

**Score:** 0.331 vs policy min 0.05 · **Close:** 600 · **ATR14:** 51.4 · **Volume ratio 20D:** 1.17 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 580–615, entry trigger **615**, stop **565**, risk 50 points (8.13%).

**Targets:** TP1 **665** (1.00R), TP2 **700** (1.70R), TP3 **735** (2.40R). Recommended base-case RR: **1.70R**.

**Why entry:** Hybrid entry uses close 600 and ATR14 51.4: buy zone 580–615. Entry is valid only if price can trade/hold around 615 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 565 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 665 (1.00R), TP2 700 (1.70R), TP3 735 (2.40R). Targets are ATR/structure capped for hold_days=1. ATR14=51.4, resistance_5/10/20/60=635/710/845/995. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.13% exceeds max strategy risk 8.00%; TP1 reward/risk 1.00R is below strategy minimum 1.25R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## SUPA — momentum_5d_continual_defensive — NO_TRADE

**Score:** 0.305 vs policy min 0.30 · **Close:** 615 · **ATR14:** 62.9 · **Volume ratio 20D:** 1.06 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 590–630, entry trigger **630**, stop **575**, risk 55 points (8.73%).

**Targets:** TP1 **685** (1.00R), TP2 **725** (1.73R), TP3 **765** (2.45R). Recommended base-case RR: **1.73R**.

**Why entry:** Hybrid entry uses close 615 and ATR14 62.9: buy zone 590–630. Entry is valid only if price can trade/hold around 630 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 575 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 685 (1.00R), TP2 725 (1.73R), TP3 765 (2.45R). Targets are ATR/structure capped for hold_days=3. ATR14=62.9, resistance_5/10/20/60=675/880/905/970. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.73% exceeds max strategy risk 8.00%; TP1 reward/risk 1.00R is below strategy minimum 1.25R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## SUPA — swing_continual_defensive — NO_TRADE

**Score:** 0.305 vs policy min 0.30 · **Close:** 615 · **ATR14:** 62.9 · **Volume ratio 20D:** 1.06 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 590–630, entry trigger **630**, stop **575**, risk 55 points (8.73%).

**Targets:** TP1 **685** (1.00R), TP2 **725** (1.73R), TP3 **765** (2.45R). Recommended base-case RR: **1.73R**.

**Why entry:** Hybrid entry uses close 615 and ATR14 62.9: buy zone 590–630. Entry is valid only if price can trade/hold around 630 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 575 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 685 (1.00R), TP2 725 (1.73R), TP3 765 (2.45R). Targets are ATR/structure capped for hold_days=1. ATR14=62.9, resistance_5/10/20/60=675/880/905/970. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.73% exceeds max strategy risk 8.00%; TP1 reward/risk 1.00R is below strategy minimum 1.25R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## APLN — scalping_continual_defensive — NO_TRADE

**Score:** 0.298 vs policy min 0.05 · **Close:** 126 · **ATR14:** 12.1 · **Volume ratio 20D:** 0.59 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 121–129, entry trigger **129**, stop **118**, risk 11 points (8.53%).

**Targets:** TP1 **140** (1.00R), TP2 **151** (2.00R), TP3 **156** (2.45R). Recommended base-case RR: **2.00R**.

**Why entry:** Hybrid entry uses close 126 and ATR14 12.1: buy zone 121–129. Entry is valid only if price can trade/hold around 129 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 118 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 140 (1.00R), TP2 151 (2.00R), TP3 156 (2.45R). Targets are ATR/structure capped for hold_days=1. ATR14=12.1, resistance_5/10/20/60=131/156/191/240. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.53% exceeds max strategy risk 8.00%; TP1 reward/risk 1.00R is below strategy minimum 1.25R; volume ratio 0.59 below required 0.60

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## SUPA — position_continual — NO_TRADE

**Score:** 0.289 vs policy min 0.30 · **Close:** 615 · **ATR14:** 62.9 · **Volume ratio 20D:** 1.06 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 590–630, entry trigger **630**, stop **575**, risk 55 points (8.73%).

**Targets:** TP1 **685** (1.00R), TP2 **725** (1.73R), TP3 **765** (2.45R). Recommended base-case RR: **1.73R**.

**Why entry:** Hybrid entry uses close 615 and ATR14 62.9: buy zone 590–630. Entry is valid only if price can trade/hold around 630 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 575 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 685 (1.00R), TP2 725 (1.73R), TP3 765 (2.45R). Targets are ATR/structure capped for hold_days=10. ATR14=62.9, resistance_5/10/20/60=675/880/905/970. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.73% exceeds max strategy risk 8.00%; score 0.289 below policy min_score 0.30; TP1 reward/risk 1.00R is below strategy minimum 1.25R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Generic strategy rule.

---

## GPSO — scalping_continual_defensive — NO_TRADE

**Score:** 0.286 vs policy min 0.05 · **Close:** 336 · **ATR14:** 31.0 · **Volume ratio 20D:** 2.32 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 324–344, entry trigger **344**, stop **316**, risk 28 points (8.14%).

**Targets:** TP1 **376** (1.14R), TP2 **392** (1.71R), TP3 **412** (2.43R). Recommended base-case RR: **1.71R**.

**Why entry:** Hybrid entry uses close 336 and ATR14 31.0: buy zone 324–344. Entry is valid only if price can trade/hold around 344 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 316 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 376 (1.14R), TP2 392 (1.71R), TP3 412 (2.43R). Targets are ATR/structure capped for hold_days=1. ATR14=31.0, resistance_5/10/20/60=380/520/520/520. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.14% exceeds max strategy risk 8.00%; TP1 reward/risk 1.14R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## KIJA — position_continual — NO_TRADE

**Score:** 0.276 vs policy min 0.30 · **Close:** 116 · **ATR14:** 9.4 · **Volume ratio 20D:** 0.75 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 112–118, entry trigger **118**, stop **108**, risk 10 points (8.47%).

**Targets:** TP1 **128** (1.00R), TP2 **135** (1.70R), TP3 **142** (2.40R). Recommended base-case RR: **1.70R**.

**Why entry:** Hybrid entry uses close 116 and ATR14 9.4: buy zone 112–118. Entry is valid only if price can trade/hold around 118 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 108 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 128 (1.00R), TP2 135 (1.70R), TP3 142 (2.40R). Targets are ATR/structure capped for hold_days=10. ATR14=9.4, resistance_5/10/20/60=117/125/181/220. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.47% exceeds max strategy risk 8.00%; score 0.276 below policy min_score 0.30; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Generic strategy rule.

---

## GPSO — momentum_5d_continual_defensive — NO_TRADE

**Score:** 0.276 vs policy min 0.30 · **Close:** 336 · **ATR14:** 31.0 · **Volume ratio 20D:** 2.32 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 324–344, entry trigger **344**, stop **316**, risk 28 points (8.14%).

**Targets:** TP1 **380** (1.29R), TP2 **392** (1.71R), TP3 **412** (2.43R). Recommended base-case RR: **1.71R**.

**Why entry:** Hybrid entry uses close 336 and ATR14 31.0: buy zone 324–344. Entry is valid only if price can trade/hold around 344 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 316 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 380 (1.29R), TP2 392 (1.71R), TP3 412 (2.43R). Targets are ATR/structure capped for hold_days=3. ATR14=31.0, resistance_5/10/20/60=380/520/520/520. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.14% exceeds max strategy risk 8.00%; score 0.276 below policy min_score 0.30

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Generic strategy rule.

---

## GPSO — swing_continual_defensive — NO_TRADE

**Score:** 0.276 vs policy min 0.30 · **Close:** 336 · **ATR14:** 31.0 · **Volume ratio 20D:** 2.32 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 324–344, entry trigger **344**, stop **316**, risk 28 points (8.14%).

**Targets:** TP1 **376** (1.14R), TP2 **392** (1.71R), TP3 **412** (2.43R). Recommended base-case RR: **1.71R**.

**Why entry:** Hybrid entry uses close 336 and ATR14 31.0: buy zone 324–344. Entry is valid only if price can trade/hold around 344 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 316 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 376 (1.14R), TP2 392 (1.71R), TP3 412 (2.43R). Targets are ATR/structure capped for hold_days=1. ATR14=31.0, resistance_5/10/20/60=380/520/520/520. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.14% exceeds max strategy risk 8.00%; score 0.276 below policy min_score 0.30; TP1 reward/risk 1.14R is below strategy minimum 1.25R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Generic strategy rule.

---

## GPSO — position_continual — NO_TRADE

**Score:** 0.275 vs policy min 0.30 · **Close:** 336 · **ATR14:** 31.0 · **Volume ratio 20D:** 2.32 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 324–344, entry trigger **344**, stop **316**, risk 28 points (8.14%).

**Targets:** TP1 **380** (1.29R), TP2 **392** (1.71R), TP3 **412** (2.43R). Recommended base-case RR: **1.71R**.

**Why entry:** Hybrid entry uses close 336 and ATR14 31.0: buy zone 324–344. Entry is valid only if price can trade/hold around 344 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 316 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 380 (1.29R), TP2 392 (1.71R), TP3 412 (2.43R). Targets are ATR/structure capped for hold_days=10. ATR14=31.0, resistance_5/10/20/60=380/520/520/520. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.14% exceeds max strategy risk 8.00%; score 0.275 below policy min_score 0.30

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Generic strategy rule.

---

## OASA — momentum_5d_continual_defensive — NO_TRADE

**Score:** 0.274 vs policy min 0.30 · **Close:** 260 · **ATR14:** 38.3 · **Volume ratio 20D:** 0.67 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 246–268, entry trigger **268**, stop **246**, risk 22 points (8.21%).

**Targets:** TP1 **290** (1.00R), TP2 **372** (4.73R), TP3 **384** (5.27R). Recommended base-case RR: **4.73R**.

**Why entry:** Hybrid entry uses close 260 and ATR14 38.3: buy zone 246–268. Entry is valid only if price can trade/hold around 268 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 246 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 290 (1.00R), TP2 372 (4.73R), TP3 384 (5.27R). Targets are ATR/structure capped for hold_days=3. ATR14=38.3, resistance_5/10/20/60=268/372/432/466. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.21% exceeds max strategy risk 8.00%; score 0.274 below policy min_score 0.30; TP1 reward/risk 1.00R is below strategy minimum 1.25R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Generic strategy rule.

---

## OASA — swing_continual_defensive — NO_TRADE

**Score:** 0.274 vs policy min 0.30 · **Close:** 260 · **ATR14:** 38.3 · **Volume ratio 20D:** 0.67 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 246–268, entry trigger **268**, stop **246**, risk 22 points (8.21%).

**Targets:** TP1 **290** (1.00R), TP2 **306** (1.73R), TP3 **364** (4.36R). Recommended base-case RR: **1.73R**.

**Why entry:** Hybrid entry uses close 260 and ATR14 38.3: buy zone 246–268. Entry is valid only if price can trade/hold around 268 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 246 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 290 (1.00R), TP2 306 (1.73R), TP3 364 (4.36R). Targets are ATR/structure capped for hold_days=1. ATR14=38.3, resistance_5/10/20/60=268/372/432/466. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.21% exceeds max strategy risk 8.00%; score 0.274 below policy min_score 0.30; TP1 reward/risk 1.00R is below strategy minimum 1.25R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Generic strategy rule.

---

## BRMS — position_continual — NO_TRADE

**Score:** 0.257 vs policy min 0.30 · **Close:** 530 · **ATR14:** 67.0 · **Volume ratio 20D:** 1.49 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 505–545, entry trigger **545**, stop **500**, risk 45 points (8.26%).

**Targets:** TP1 **590** (1.00R), TP2 **625** (1.78R), TP3 **655** (2.44R). Recommended base-case RR: **1.78R**.

**Why entry:** Hybrid entry uses close 530 and ATR14 67.0: buy zone 505–545. Entry is valid only if price can trade/hold around 545 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 500 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 590 (1.00R), TP2 625 (1.78R), TP3 655 (2.44R). Targets are ATR/structure capped for hold_days=10. ATR14=67.0, resistance_5/10/20/60=565/635/795/930. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.26% exceeds max strategy risk 8.00%; score 0.257 below policy min_score 0.30; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Generic strategy rule.

---

## PYFA — position_continual — NO_TRADE

**Score:** 0.255 vs policy min 0.30 · **Close:** 194 · **ATR14:** 23.9 · **Volume ratio 20D:** 0.66 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 185–199, entry trigger **199**, stop **183**, risk 16 points (8.04%).

**Targets:** TP1 **216** (1.06R), TP2 **228** (1.81R), TP3 **238** (2.44R). Recommended base-case RR: **1.81R**.

**Why entry:** Hybrid entry uses close 194 and ATR14 23.9: buy zone 185–199. Entry is valid only if price can trade/hold around 199 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 183 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 216 (1.06R), TP2 228 (1.81R), TP3 238 (2.44R). Targets are ATR/structure capped for hold_days=10. ATR14=23.9, resistance_5/10/20/60=208/242/422/446. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.04% exceeds max strategy risk 8.00%; score 0.255 below policy min_score 0.30; TP1 reward/risk 1.06R is below strategy minimum 1.25R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Generic strategy rule.

---

## OASA — position_continual — NO_TRADE

**Score:** 0.254 vs policy min 0.30 · **Close:** 260 · **ATR14:** 38.3 · **Volume ratio 20D:** 0.67 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 246–268, entry trigger **268**, stop **246**, risk 22 points (8.21%).

**Targets:** TP1 **372** (4.73R), TP2 **384** (5.27R), TP3 **396** (5.82R). Recommended base-case RR: **5.27R**.

**Why entry:** Hybrid entry uses close 260 and ATR14 38.3: buy zone 246–268. Entry is valid only if price can trade/hold around 268 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 246 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 372 (4.73R), TP2 384 (5.27R), TP3 396 (5.82R). Targets are ATR/structure capped for hold_days=10. ATR14=38.3, resistance_5/10/20/60=268/372/432/466. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.21% exceeds max strategy risk 8.00%; score 0.254 below policy min_score 0.30; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Generic strategy rule.

---

## SSMS — position_continual — NO_TRADE

**Score:** 0.253 vs policy min 0.30 · **Close:** 745 · **ATR14:** 72.5 · **Volume ratio 20D:** 0.98 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 715–760, entry trigger **760**, stop **695**, risk 65 points (8.55%).

**Targets:** TP1 **825** (1.00R), TP2 **875** (1.77R), TP3 **920** (2.46R). Recommended base-case RR: **1.77R**.

**Why entry:** Hybrid entry uses close 745 and ATR14 72.5: buy zone 715–760. Entry is valid only if price can trade/hold around 760 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 695 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 825 (1.00R), TP2 875 (1.77R), TP3 920 (2.46R). Targets are ATR/structure capped for hold_days=10. ATR14=72.5, resistance_5/10/20/60=775/825/1,430/1,500. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.55% exceeds max strategy risk 8.00%; score 0.253 below policy min_score 0.30; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Generic strategy rule.

---

## APLN — position_continual — NO_TRADE

**Score:** 0.253 vs policy min 0.30 · **Close:** 126 · **ATR14:** 12.1 · **Volume ratio 20D:** 0.59 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 121–129, entry trigger **129**, stop **118**, risk 11 points (8.53%).

**Targets:** TP1 **156** (2.45R), TP2 **162** (3.00R), TP3 **168** (3.55R). Recommended base-case RR: **3.00R**.

**Why entry:** Hybrid entry uses close 126 and ATR14 12.1: buy zone 121–129. Entry is valid only if price can trade/hold around 129 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 118 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 156 (2.45R), TP2 162 (3.00R), TP3 168 (3.55R). Targets are ATR/structure capped for hold_days=10. ATR14=12.1, resistance_5/10/20/60=131/156/191/240. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.53% exceeds max strategy risk 8.00%; score 0.253 below policy min_score 0.30; volume ratio 0.59 below required 0.60

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Generic strategy rule.

---

## NIKL — position_continual — NO_TRADE

**Score:** 0.253 vs policy min 0.30 · **Close:** 192 · **ATR14:** 27.1 · **Volume ratio 20D:** 0.60 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 182–198, entry trigger **198**, stop **182**, risk 16 points (8.08%).

**Targets:** TP1 **240** (2.62R), TP2 **248** (3.12R), TP3 **256** (3.62R). Recommended base-case RR: **3.12R**.

**Why entry:** Hybrid entry uses close 192 and ATR14 27.1: buy zone 182–198. Entry is valid only if price can trade/hold around 198 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 182 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 240 (2.62R), TP2 248 (3.12R), TP3 256 (3.62R). Targets are ATR/structure capped for hold_days=10. ATR14=27.1, resistance_5/10/20/60=240/260/370/510. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.08% exceeds max strategy risk 8.00%; score 0.253 below policy min_score 0.30; volume ratio 0.60 below required 0.60

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Generic strategy rule.

---

## KIJA — momentum_20d_continual_research — NO_TRADE

**Score:** 0.246 vs policy min 0.30 · **Close:** 116 · **ATR14:** 9.4 · **Volume ratio 20D:** 0.75 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 112–118, entry trigger **118**, stop **108**, risk 10 points (8.47%).

**Targets:** TP1 **128** (1.00R), TP2 **135** (1.70R), TP3 **142** (2.40R). Recommended base-case RR: **1.70R**.

**Why entry:** Hybrid entry uses close 116 and ATR14 9.4: buy zone 112–118. Entry is valid only if price can trade/hold around 118 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 108 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 128 (1.00R), TP2 135 (1.70R), TP3 142 (2.40R). Targets are ATR/structure capped for hold_days=10. ATR14=9.4, resistance_5/10/20/60=117/125/181/220. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** strategy policy has execution_enabled=false; entry-to-stop risk 8.47% exceeds max strategy risk 8.00%; score 0.246 below policy min_score 0.30; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Generic strategy rule.

---

## GULA — momentum_5d_continual_defensive — NO_TRADE

**Score:** 0.238 vs policy min 0.30 · **Close:** 575 · **ATR14:** 49.2 · **Volume ratio 20D:** 1.12 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 555–585, entry trigger **585**, stop **535**, risk 50 points (8.55%).

**Targets:** TP1 **635** (1.00R), TP2 **670** (1.70R), TP3 **705** (2.40R). Recommended base-case RR: **1.70R**.

**Why entry:** Hybrid entry uses close 575 and ATR14 49.2: buy zone 555–585. Entry is valid only if price can trade/hold around 585 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 535 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 635 (1.00R), TP2 670 (1.70R), TP3 705 (2.40R). Targets are ATR/structure capped for hold_days=3. ATR14=49.2, resistance_5/10/20/60=610/610/610/610. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.55% exceeds max strategy risk 8.00%; score 0.238 below policy min_score 0.30; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Generic strategy rule.

---

## GULA — swing_continual_defensive — NO_TRADE

**Score:** 0.238 vs policy min 0.30 · **Close:** 575 · **ATR14:** 49.2 · **Volume ratio 20D:** 1.12 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 555–585, entry trigger **585**, stop **535**, risk 50 points (8.55%).

**Targets:** TP1 **635** (1.00R), TP2 **670** (1.70R), TP3 **705** (2.40R). Recommended base-case RR: **1.70R**.

**Why entry:** Hybrid entry uses close 575 and ATR14 49.2: buy zone 555–585. Entry is valid only if price can trade/hold around 585 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 535 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 635 (1.00R), TP2 670 (1.70R), TP3 705 (2.40R). Targets are ATR/structure capped for hold_days=1. ATR14=49.2, resistance_5/10/20/60=610/610/610/610. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.55% exceeds max strategy risk 8.00%; score 0.238 below policy min_score 0.30; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Generic strategy rule.

---

## OASA — momentum_20d_continual_research — NO_TRADE

**Score:** 0.228 vs policy min 0.30 · **Close:** 260 · **ATR14:** 38.3 · **Volume ratio 20D:** 0.67 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 246–268, entry trigger **268**, stop **246**, risk 22 points (8.21%).

**Targets:** TP1 **372** (4.73R), TP2 **384** (5.27R), TP3 **396** (5.82R). Recommended base-case RR: **5.27R**.

**Why entry:** Hybrid entry uses close 260 and ATR14 38.3: buy zone 246–268. Entry is valid only if price can trade/hold around 268 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 246 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 372 (4.73R), TP2 384 (5.27R), TP3 396 (5.82R). Targets are ATR/structure capped for hold_days=10. ATR14=38.3, resistance_5/10/20/60=268/372/432/466. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** strategy policy has execution_enabled=false; entry-to-stop risk 8.21% exceeds max strategy risk 8.00%; score 0.228 below policy min_score 0.30; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Generic strategy rule.

---

## NIKL — momentum_5d_continual_defensive — NO_TRADE

**Score:** 0.227 vs policy min 0.30 · **Close:** 192 · **ATR14:** 27.1 · **Volume ratio 20D:** 0.60 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 182–198, entry trigger **198**, stop **182**, risk 16 points (8.08%).

**Targets:** TP1 **240** (2.62R), TP2 **248** (3.12R), TP3 **256** (3.62R). Recommended base-case RR: **3.12R**.

**Why entry:** Hybrid entry uses close 192 and ATR14 27.1: buy zone 182–198. Entry is valid only if price can trade/hold around 198 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 182 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 240 (2.62R), TP2 248 (3.12R), TP3 256 (3.62R). Targets are ATR/structure capped for hold_days=3. ATR14=27.1, resistance_5/10/20/60=240/260/370/510. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.08% exceeds max strategy risk 8.00%; score 0.227 below policy min_score 0.30; volume ratio 0.60 below required 0.60

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Generic strategy rule.

---

## NIKL — swing_continual_defensive — NO_TRADE

**Score:** 0.227 vs policy min 0.30 · **Close:** 192 · **ATR14:** 27.1 · **Volume ratio 20D:** 0.60 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 182–198, entry trigger **198**, stop **182**, risk 16 points (8.08%).

**Targets:** TP1 **214** (1.00R), TP2 **240** (2.62R), TP3 **248** (3.12R). Recommended base-case RR: **2.62R**.

**Why entry:** Hybrid entry uses close 192 and ATR14 27.1: buy zone 182–198. Entry is valid only if price can trade/hold around 198 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 182 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 214 (1.00R), TP2 240 (2.62R), TP3 248 (3.12R). Targets are ATR/structure capped for hold_days=1. ATR14=27.1, resistance_5/10/20/60=240/260/370/510. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.08% exceeds max strategy risk 8.00%; score 0.227 below policy min_score 0.30; TP1 reward/risk 1.00R is below strategy minimum 1.25R; volume ratio 0.60 below required 0.60

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Generic strategy rule.

---

## NZIA — momentum_5d_continual_defensive — NO_TRADE

**Score:** 0.226 vs policy min 0.30 · **Close:** 177 · **ATR14:** 40.5 · **Volume ratio 20D:** 0.15 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 162–186, entry trigger **186**, stop **171**, risk 15 points (8.06%).

**Targets:** TP1 **234** (3.20R), TP2 **242** (3.73R), TP3 **250** (4.27R). Recommended base-case RR: **3.73R**.

**Why entry:** Hybrid entry uses close 177 and ATR14 40.5: buy zone 162–186. Entry is valid only if price can trade/hold around 186 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 171 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 234 (3.20R), TP2 242 (3.73R), TP3 250 (4.27R). Targets are ATR/structure capped for hold_days=3. ATR14=40.5, resistance_5/10/20/60=234/316/316/316. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.06% exceeds max strategy risk 8.00%; score 0.226 below policy min_score 0.30; volume ratio 0.15 below required 0.60; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Generic strategy rule.

---

## NZIA — swing_continual_defensive — NO_TRADE

**Score:** 0.226 vs policy min 0.30 · **Close:** 177 · **ATR14:** 40.5 · **Volume ratio 20D:** 0.15 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 162–186, entry trigger **186**, stop **171**, risk 15 points (8.06%).

**Targets:** TP1 **228** (2.80R), TP2 **234** (3.20R), TP3 **242** (3.73R). Recommended base-case RR: **3.20R**.

**Why entry:** Hybrid entry uses close 177 and ATR14 40.5: buy zone 162–186. Entry is valid only if price can trade/hold around 186 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 171 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 228 (2.80R), TP2 234 (3.20R), TP3 242 (3.73R). Targets are ATR/structure capped for hold_days=1. ATR14=40.5, resistance_5/10/20/60=234/316/316/316. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.06% exceeds max strategy risk 8.00%; score 0.226 below policy min_score 0.30; volume ratio 0.15 below required 0.60; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Generic strategy rule.

---

## CDIA — momentum_20d_continual_research — NO_TRADE

**Score:** 0.213 vs policy min 0.30 · **Close:** 690 · **ATR14:** 103.2 · **Volume ratio 20D:** 0.54 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 650–715, entry trigger **715**, stop **655**, risk 60 points (8.39%).

**Targets:** TP1 **775** (1.00R), TP2 **820** (1.75R), TP3 **860** (2.42R). Recommended base-case RR: **1.75R**.

**Why entry:** Hybrid entry uses close 690 and ATR14 103.2: buy zone 650–715. Entry is valid only if price can trade/hold around 715 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 655 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 775 (1.00R), TP2 820 (1.75R), TP3 860 (2.42R). Targets are ATR/structure capped for hold_days=10. ATR14=103.2, resistance_5/10/20/60=745/950/1,075/1,340. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** strategy policy has execution_enabled=false; entry-to-stop risk 8.39% exceeds max strategy risk 8.00%; score 0.213 below policy min_score 0.30; TP1 reward/risk 1.00R is below strategy minimum 1.25R; volume ratio 0.54 below required 0.60; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Generic strategy rule.

---

## SUPA — momentum_20d_continual_research — NO_TRADE

**Score:** 0.212 vs policy min 0.30 · **Close:** 615 · **ATR14:** 62.9 · **Volume ratio 20D:** 1.06 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 590–630, entry trigger **630**, stop **575**, risk 55 points (8.73%).

**Targets:** TP1 **685** (1.00R), TP2 **725** (1.73R), TP3 **765** (2.45R). Recommended base-case RR: **1.73R**.

**Why entry:** Hybrid entry uses close 615 and ATR14 62.9: buy zone 590–630. Entry is valid only if price can trade/hold around 630 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 575 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 685 (1.00R), TP2 725 (1.73R), TP3 765 (2.45R). Targets are ATR/structure capped for hold_days=10. ATR14=62.9, resistance_5/10/20/60=675/880/905/970. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** strategy policy has execution_enabled=false; entry-to-stop risk 8.73% exceeds max strategy risk 8.00%; score 0.212 below policy min_score 0.30; TP1 reward/risk 1.00R is below strategy minimum 1.25R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Generic strategy rule.

---

## INET — momentum_20d_continual_research — NO_TRADE

**Score:** 0.201 vs policy min 0.30 · **Close:** 199 · **ATR14:** 26.7 · **Volume ratio 20D:** 1.23 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 189–206, entry trigger **206**, stop **189**, risk 17 points (8.25%).

**Targets:** TP1 **244** (2.24R), TP2 **254** (2.82R), TP3 **264** (3.41R). Recommended base-case RR: **2.82R**.

**Why entry:** Hybrid entry uses close 199 and ATR14 26.7: buy zone 189–206. Entry is valid only if price can trade/hold around 206 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 189 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 244 (2.24R), TP2 254 (2.82R), TP3 264 (3.41R). Targets are ATR/structure capped for hold_days=10. ATR14=26.7, resistance_5/10/20/60=206/244/306/360. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** strategy policy has execution_enabled=false; entry-to-stop risk 8.25% exceeds max strategy risk 8.00%; score 0.201 below policy min_score 0.30; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Generic strategy rule.

---
