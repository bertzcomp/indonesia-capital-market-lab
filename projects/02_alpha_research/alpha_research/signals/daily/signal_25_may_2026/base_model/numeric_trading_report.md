# Numeric Trading Desk Report — 2026-05-22

This report is generated from live model scores, selected signal policy, canonical OHLCV, ATR, support/resistance, liquidity, and broker-flow diagnostics. It is not a simple BUY/SELL list; each plan is conditional on execution behaviour.

## Summary

| Plan quality | Count |
|---|---:|
| CONDITIONAL | 8 |
| WATCHLIST_ONLY | 3 |
| NO_TRADE | 45 |

## HRUM — swing_hgb_defensive — CONDITIONAL

**Score:** 0.662 vs policy min 0.50 · **Close:** 790 · **ATR14:** 53.9 · **Volume ratio 20D:** 2.55 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 765–800, entry trigger **800**, stop **740**, risk 60 points (7.50%).

**Targets:** TP1 **855** (0.92R), TP2 **900** (1.67R), TP3 **945** (2.42R). Recommended base-case RR: **1.67R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 790: zone 765–800 uses ATR14 53.9 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 800 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 740 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 855 (0.92R), TP2 900 (1.67R), TP3 945 (2.42R). Targets are ATR/structure capped for hold_days=1. ATR14=53.9, resistance_5/10/20/60=895/1,015/1,060/1,270. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 0.92R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## KIJA — swing_hgb_defensive — CONDITIONAL

**Score:** 0.638 vs policy min 0.50 · **Close:** 121 · **ATR14:** 10.1 · **Volume ratio 20D:** 2.37 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 116–123, entry trigger **123**, stop **118**, risk 5 points (4.07%).

**Targets:** TP1 **129** (1.20R), TP2 **132** (1.80R), TP3 **135** (2.40R). Recommended base-case RR: **1.80R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 121: zone 116–123 uses ATR14 10.1 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 123 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 118 is placed below support structure (119 / 119). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 129 (1.20R), TP2 132 (1.80R), TP3 135 (2.40R). Targets are ATR/structure capped for hold_days=1. ATR14=10.1, resistance_5/10/20/60=174/189/220/240. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.20R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## PGLI — swing_hgb_defensive — CONDITIONAL

**Score:** 0.629 vs policy min 0.50 · **Close:** 177 · **ATR14:** 29.9 · **Volume ratio 20D:** 2.18 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 163–180, entry trigger **180**, stop **176**, risk 4 points (2.22%).

**Targets:** TP1 **195** (3.75R), TP2 **197** (4.25R), TP3 **256** (19.00R). Recommended base-case RR: **4.25R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 177: zone 163–180 uses ATR14 29.9 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 180 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 176 is placed below support structure (177 / 177). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 195 (3.75R), TP2 197 (4.25R), TP3 256 (19.00R). Targets are ATR/structure capped for hold_days=1. ATR14=29.9, resistance_5/10/20/60=256/256/320/320. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## TMPO — position_xgb — CONDITIONAL

**Score:** 0.564 vs policy min 0.55 · **Close:** 108 · **ATR14:** 10.6 · **Volume ratio 20D:** 5.22 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 103–110, entry trigger **110**, stop **102**, risk 8 points (7.27%).

**Targets:** TP1 **125** (1.88R), TP2 **130** (2.50R), TP3 **134** (3.00R). Recommended base-case RR: **2.50R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 108: zone 103–110 uses ATR14 10.6 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 110 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 102 is placed below support structure (103 / 103). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 125 (1.88R), TP2 130 (2.50R), TP3 134 (3.00R). Targets are ATR/structure capped for hold_days=1. ATR14=10.6, resistance_5/10/20/60=130/152/152/168. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## DIVA — position_xgb — CONDITIONAL

**Score:** 0.564 vs policy min 0.55 · **Close:** 136 · **ATR14:** 26.3 · **Volume ratio 20D:** 0.96 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 125–139, entry trigger **139**, stop **129**, risk 10 points (7.19%).

**Targets:** TP1 **176** (3.70R), TP2 **180** (4.10R), TP3 **185** (4.60R). Recommended base-case RR: **4.10R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 136: zone 125–139 uses ATR14 26.3 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 139 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 129 is placed below support structure (130 / 130). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 176 (3.70R), TP2 180 (4.10R), TP3 185 (4.60R). Targets are ATR/structure capped for hold_days=1. ATR14=26.3, resistance_5/10/20/60=180/198/202/254. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## IRSX — position_xgb — CONDITIONAL

**Score:** 0.558 vs policy min 0.55 · **Close:** 328 · **ATR14:** 45.7 · **Volume ratio 20D:** 2.40 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 306–334, entry trigger **334**, stop **316**, risk 18 points (5.39%).

**Targets:** TP1 **358** (1.33R), TP2 **366** (1.78R), TP3 **472** (7.67R). Recommended base-case RR: **1.78R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 328: zone 306–334 uses ATR14 45.7 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 334 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 316 is placed below support structure (318 / 318). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 358 (1.33R), TP2 366 (1.78R), TP3 472 (7.67R). Targets are ATR/structure capped for hold_days=1. ATR14=45.7, resistance_5/10/20/60=472/480/525/685. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.33R is below strategy minimum 1.35R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## KIJA — position_xgb — CONDITIONAL

**Score:** 0.553 vs policy min 0.55 · **Close:** 121 · **ATR14:** 10.1 · **Volume ratio 20D:** 2.37 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 116–123, entry trigger **123**, stop **118**, risk 5 points (4.07%).

**Targets:** TP1 **129** (1.20R), TP2 **132** (1.80R), TP3 **135** (2.40R). Recommended base-case RR: **1.80R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 121: zone 116–123 uses ATR14 10.1 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 123 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 118 is placed below support structure (119 / 119). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 129 (1.20R), TP2 132 (1.80R), TP3 135 (2.40R). Targets are ATR/structure capped for hold_days=1. ATR14=10.1, resistance_5/10/20/60=174/189/220/240. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.20R is below strategy minimum 1.35R

**Risk flags:** OK

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## SCMA — position_xgb — CONDITIONAL

**Score:** 0.552 vs policy min 0.55 · **Close:** 220 · **ATR14:** 14.0 · **Volume ratio 20D:** 0.58 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 212–222, entry trigger **222**, stop **212**, risk 10 points (4.50%).

**Targets:** TP1 **232** (1.00R), TP2 **254** (3.20R), TP3 **260** (3.80R). Recommended base-case RR: **3.20R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 220: zone 212–222 uses ATR14 14.0 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 222 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 212 is placed below support structure (214 / 214). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 232 (1.00R), TP2 254 (3.20R), TP3 260 (3.80R). Targets are ATR/structure capped for hold_days=1. ATR14=14.0, resistance_5/10/20/60=254/266/312/320. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.35R; volume ratio 0.58 below required 0.60; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## UVCR — momentum_10d_hgb_aggressive — WATCHLIST_ONLY

**Score:** 0.450 vs policy min 0.60 · **Close:** 228 · **ATR14:** 12.9 · **Volume ratio 20D:** 1.41 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 224–236, entry trigger **236**, stop **218**, risk 18 points (7.63%).

**Targets:** TP1 **254** (1.00R), TP2 **268** (1.78R), TP3 **280** (2.44R). Recommended base-case RR: **1.78R**.

**Why entry:** Entry trigger 236 is set above recent resistance 234 plus one IDX tick. This requires confirmation instead of buying blindly at close 228. Entry is valid only if price can trade/hold around 236 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 218 uses 1.30×ATR14 volatility cap. Thesis invalidates if the move reverses beyond normal volatility. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 254 (1.00R), TP2 268 (1.78R), TP3 280 (2.44R). Targets are ATR/structure capped for hold_days=2. ATR14=12.9, resistance_5/10/20/60=234/234/234/234. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** score 0.450 below policy min_score 0.60; TP1 reward/risk 1.00R is below strategy minimum 1.40R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## GULA — momentum_10d_hgb_aggressive — WATCHLIST_ONLY

**Score:** 0.431 vs policy min 0.60 · **Close:** 424 · **ATR14:** 23.7 · **Volume ratio 20D:** 0.88 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 418–438, entry trigger **438**, stop **406**, risk 32 points (7.31%).

**Targets:** TP1 **470** (1.00R), TP2 **494** (1.75R), TP3 **515** (2.41R). Recommended base-case RR: **1.75R**.

**Why entry:** Entry trigger 438 is set above recent resistance 436 plus one IDX tick. This requires confirmation instead of buying blindly at close 424. Entry is valid only if price can trade/hold around 438 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 406 uses 1.30×ATR14 volatility cap. Thesis invalidates if the move reverses beyond normal volatility. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 470 (1.00R), TP2 494 (1.75R), TP3 515 (2.41R). Targets are ATR/structure capped for hold_days=2. ATR14=23.7, resistance_5/10/20/60=432/436/436/436. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** score 0.431 below policy min_score 0.60; TP1 reward/risk 1.00R is below strategy minimum 1.40R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## GPSO — momentum_10d_hgb_aggressive — WATCHLIST_ONLY

**Score:** 0.411 vs policy min 0.60 · **Close:** 478 · **ATR14:** 31.1 · **Volume ratio 20D:** 1.03 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 470–505, entry trigger **505**, stop **464**, risk 41 points (8.12%).

**Targets:** TP1 **550** (1.10R), TP2 **575** (1.71R), TP3 **605** (2.44R). Recommended base-case RR: **1.71R**.

**Why entry:** Entry trigger 505 is set above recent resistance 500 plus one IDX tick. This requires confirmation instead of buying blindly at close 478. Entry is valid only if price can trade/hold around 505 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 464 uses 1.30×ATR14 volatility cap. Thesis invalidates if the move reverses beyond normal volatility. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 550 (1.10R), TP2 575 (1.71R), TP3 605 (2.44R). Targets are ATR/structure capped for hold_days=2. ATR14=31.1, resistance_5/10/20/60=500/500/500/535. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** score 0.411 below policy min_score 0.60; TP1 reward/risk 1.10R is below strategy minimum 1.40R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## SIMP — swing_hgb_defensive — NO_TRADE

**Score:** 0.651 vs policy min 0.50 · **Close:** 560 · **ATR14:** 51.1 · **Volume ratio 20D:** 0.56 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 535–570, entry trigger **570**, stop **525**, risk 45 points (7.89%).

**Targets:** TP1 **625** (1.22R), TP2 **650** (1.78R), TP3 **680** (2.44R). Recommended base-case RR: **1.78R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 560: zone 535–570 uses ATR14 51.1 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 570 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 525 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 625 (1.22R), TP2 650 (1.78R), TP3 680 (2.44R). Targets are ATR/structure capped for hold_days=1. ATR14=51.1, resistance_5/10/20/60=645/830/920/930. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.89% exceeds max strategy risk 7.50%; TP1 reward/risk 1.22R is below strategy minimum 1.25R; volume ratio 0.56 below required 0.60

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## SSMS — scalping_rank_hgb — NO_TRADE

**Score:** 0.648 vs policy min 0.60 · **Close:** 875 · **ATR14:** 85.7 · **Volume ratio 20D:** 0.51 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 855–1,215, entry trigger **1,215**, stop **1,160**, risk 55 points (4.53%).

**Targets:** TP1 **1,270** (1.00R), TP2 **1,310** (1.73R), TP3 **1,350** (2.45R). Recommended base-case RR: **1.73R**.

**Why entry:** Entry trigger 1,215 is set above recent resistance 1,210 plus one IDX tick. This requires confirmation instead of buying blindly at close 875. Entry is valid only if price can trade/hold around 1,215 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 1,160 is capped by max risk 4.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,270 (1.00R), TP2 1,310 (1.73R), TP3 1,350 (2.45R). Targets are ATR/structure capped for hold_days=1. ATR14=85.7, resistance_5/10/20/60=1,210/1,450/1,470/1,800. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 38.86% > max 5.00%; entry-to-stop risk 4.53% exceeds max strategy risk 4.50%; TP1 reward/risk 1.00R is below strategy minimum 1.10R; volume ratio 0.51 below required 0.60

**Risk flags:** OK

**Strategy risk note:** Top-1 short-horizon scalp; invalidation must be quick.

---

## TOBA — swing_hgb_defensive — NO_TRADE

**Score:** 0.642 vs policy min 0.50 · **Close:** 448 · **ATR14:** 44.9 · **Volume ratio 20D:** 1.02 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 426–454, entry trigger **454**, stop **418**, risk 36 points (7.93%).

**Targets:** TP1 **490** (1.00R), TP2 **535** (2.25R), TP3 **555** (2.81R). Recommended base-case RR: **2.25R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 448: zone 426–454 uses ATR14 44.9 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 454 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 418 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 490 (1.00R), TP2 535 (2.25R), TP3 555 (2.81R). Targets are ATR/structure capped for hold_days=1. ATR14=44.9, resistance_5/10/20/60=555/650/705/815. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.93% exceeds max strategy risk 7.50%; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## PYFA — swing_hgb_defensive — NO_TRADE

**Score:** 0.640 vs policy min 0.50 · **Close:** 242 · **ATR14:** 36.7 · **Volume ratio 20D:** 0.66 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 224–246, entry trigger **246**, stop **226**, risk 20 points (8.13%).

**Targets:** TP1 **266** (1.00R), TP2 **314** (3.40R), TP3 **318** (3.60R). Recommended base-case RR: **3.40R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 242: zone 224–246 uses ATR14 36.7 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 246 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 226 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 266 (1.00R), TP2 314 (3.40R), TP3 318 (3.60R). Targets are ATR/structure capped for hold_days=1. ATR14=36.7, resistance_5/10/20/60=318/380/406/466. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.13% exceeds max strategy risk 7.50%; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## CDIA — swing_hgb_defensive — NO_TRADE

**Score:** 0.638 vs policy min 0.50 · **Close:** 750 · **ATR14:** 109.3 · **Volume ratio 20D:** 0.69 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 700–765, entry trigger **765**, stop **705**, risk 60 points (7.84%).

**Targets:** TP1 **825** (1.00R), TP2 **965** (3.33R), TP3 **1,000** (3.92R). Recommended base-case RR: **3.33R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 750: zone 700–765 uses ATR14 109.3 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 765 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 705 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 825 (1.00R), TP2 965 (3.33R), TP3 1,000 (3.92R). Targets are ATR/structure capped for hold_days=1. ATR14=109.3, resistance_5/10/20/60=1,000/1,230/1,255/1,340. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.84% exceeds max strategy risk 7.50%; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## INET — swing_hgb_defensive — NO_TRADE

**Score:** 0.637 vs policy min 0.50 · **Close:** 230 · **ATR14:** 25.4 · **Volume ratio 20D:** 0.81 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 218–234, entry trigger **234**, stop **216**, risk 18 points (7.69%).

**Targets:** TP1 **252** (1.00R), TP2 **280** (2.56R), TP3 **290** (3.11R). Recommended base-case RR: **2.56R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 230: zone 218–234 uses ATR14 25.4 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 234 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 216 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 252 (1.00R), TP2 280 (2.56R), TP3 290 (3.11R). Targets are ATR/structure capped for hold_days=1. ATR14=25.4, resistance_5/10/20/60=280/324/360/438. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.69% exceeds max strategy risk 7.50%; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## RMKO — swing_hgb_defensive — NO_TRADE

**Score:** 0.636 vs policy min 0.50 · **Close:** 346 · **ATR14:** 43.7 · **Volume ratio 20D:** 1.15 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 326–352, entry trigger **352**, stop **324**, risk 28 points (7.95%).

**Targets:** TP1 **380** (1.00R), TP2 **432** (2.86R), TP3 **452** (3.57R). Recommended base-case RR: **2.86R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 346: zone 326–352 uses ATR14 43.7 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 352 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 324 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 380 (1.00R), TP2 432 (2.86R), TP3 452 (3.57R). Targets are ATR/structure capped for hold_days=1. ATR14=43.7, resistance_5/10/20/60=452/505/645/1,180. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.95% exceeds max strategy risk 7.50%; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## FOLK — swing_hgb_defensive — NO_TRADE

**Score:** 0.635 vs policy min 0.50 · **Close:** 234 · **ATR14:** 35.6 · **Volume ratio 20D:** 1.38 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 216–238, entry trigger **238**, stop **220**, risk 18 points (7.56%).

**Targets:** TP1 **256** (1.00R), TP2 **270** (1.78R), TP3 **328** (5.00R). Recommended base-case RR: **1.78R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 234: zone 216–238 uses ATR14 35.6 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 238 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 220 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 256 (1.00R), TP2 270 (1.78R), TP3 328 (5.00R). Targets are ATR/structure capped for hold_days=1. ATR14=35.6, resistance_5/10/20/60=332/410/410/785. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.56% exceeds max strategy risk 7.50%; TP1 reward/risk 1.00R is below strategy minimum 1.25R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## UNSP — swing_hgb_defensive — NO_TRADE

**Score:** 0.635 vs policy min 0.50 · **Close:** 248 · **ATR14:** 24.7 · **Volume ratio 20D:** 0.76 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 236–252, entry trigger **252**, stop **232**, risk 20 points (7.94%).

**Targets:** TP1 **278** (1.30R), TP2 **290** (1.90R), TP3 **300** (2.40R). Recommended base-case RR: **1.90R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 248: zone 236–252 uses ATR14 24.7 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 252 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 232 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 278 (1.30R), TP2 290 (1.90R), TP3 300 (2.40R). Targets are ATR/structure capped for hold_days=1. ATR14=24.7, resistance_5/10/20/60=290/392/450/450. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.94% exceeds max strategy risk 7.50%; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## KRAS — swing_hgb_defensive — NO_TRADE

**Score:** 0.634 vs policy min 0.50 · **Close:** 232 · **ATR14:** 15.3 · **Volume ratio 20D:** 0.54 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 224–234, entry trigger **234**, stop **216**, risk 18 points (7.69%).

**Targets:** TP1 **250** (0.89R), TP2 **262** (1.56R), TP3 **278** (2.44R). Recommended base-case RR: **1.56R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 232: zone 224–234 uses ATR14 15.3 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 234 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 216 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 250 (0.89R), TP2 262 (1.56R), TP3 278 (2.44R). Targets are ATR/structure capped for hold_days=1. ATR14=15.3, resistance_5/10/20/60=264/310/314/382. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.69% exceeds max strategy risk 7.50%; TP1 reward/risk 0.89R is below strategy minimum 1.25R; volume ratio 0.54 below required 0.60

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## PSAB — swing_hgb_defensive — NO_TRADE

**Score:** 0.632 vs policy min 0.50 · **Close:** 426 · **ATR14:** 41.4 · **Volume ratio 20D:** 1.41 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 406–432, entry trigger **432**, stop **398**, risk 34 points (7.87%).

**Targets:** TP1 **474** (1.24R), TP2 **496** (1.88R), TP3 **515** (2.44R). Recommended base-case RR: **1.88R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 426: zone 406–432 uses ATR14 41.4 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 432 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 398 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 474 (1.24R), TP2 496 (1.88R), TP3 515 (2.44R). Targets are ATR/structure capped for hold_days=1. ATR14=41.4, resistance_5/10/20/60=496/580/590/590. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.87% exceeds max strategy risk 7.50%; TP1 reward/risk 1.24R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## SOCI — swing_hgb_defensive — NO_TRADE

**Score:** 0.629 vs policy min 0.50 · **Close:** 388 · **ATR14:** 40.8 · **Volume ratio 20D:** 0.70 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 368–394, entry trigger **394**, stop **364**, risk 30 points (7.61%).

**Targets:** TP1 **436** (1.40R), TP2 **454** (2.00R), TP3 **466** (2.40R). Recommended base-case RR: **2.00R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 388: zone 368–394 uses ATR14 40.8 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 394 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 364 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 436 (1.40R), TP2 454 (2.00R), TP3 466 (2.40R). Targets are ATR/structure capped for hold_days=1. ATR14=40.8, resistance_5/10/20/60=454/540/570/780. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.61% exceeds max strategy risk 7.50%; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## VKTR — swing_hgb_defensive — NO_TRADE

**Score:** 0.629 vs policy min 0.50 · **Close:** 745 · **ATR14:** 89.6 · **Volume ratio 20D:** 1.15 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 700–755, entry trigger **755**, stop **695**, risk 60 points (7.95%).

**Targets:** TP1 **845** (1.50R), TP2 **885** (2.17R), TP3 **900** (2.42R). Recommended base-case RR: **2.17R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 745: zone 700–755 uses ATR14 89.6 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 755 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 695 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 845 (1.50R), TP2 885 (2.17R), TP3 900 (2.42R). Targets are ATR/structure capped for hold_days=1. ATR14=89.6, resistance_5/10/20/60=885/995/1,020/1,100. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.95% exceeds max strategy risk 7.50%

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## MBMA — position_xgb — NO_TRADE

**Score:** 0.560 vs policy min 0.55 · **Close:** 482 · **ATR14:** 54.2 · **Volume ratio 20D:** 2.58 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 456–488, entry trigger **488**, stop **444**, risk 44 points (9.02%).

**Targets:** TP1 **565** (1.75R), TP2 **580** (2.09R), TP3 **595** (2.43R). Recommended base-case RR: **2.09R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 482: zone 456–488 uses ATR14 54.2 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 488 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 444 is capped by max risk 9.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 565 (1.75R), TP2 580 (2.09R), TP3 595 (2.43R). Targets are ATR/structure capped for hold_days=1. ATR14=54.2, resistance_5/10/20/60=580/690/770/945. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 9.02% exceeds max strategy risk 9.00%

**Risk flags:** OK

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## DEWA — position_xgb — NO_TRADE

**Score:** 0.560 vs policy min 0.55 · **Close:** 378 · **ATR14:** 41.5 · **Volume ratio 20D:** 1.88 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 358–384, entry trigger **384**, stop **348**, risk 36 points (9.38%).

**Targets:** TP1 **420** (1.00R), TP2 **482** (2.72R), TP3 **500** (3.22R). Recommended base-case RR: **2.72R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 378: zone 358–384 uses ATR14 41.5 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 384 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 348 is capped by max risk 9.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 420 (1.00R), TP2 482 (2.72R), TP3 500 (3.22R). Targets are ATR/structure capped for hold_days=1. ATR14=41.5, resistance_5/10/20/60=482/535/575/655. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 9.38% exceeds max strategy risk 9.00%; TP1 reward/risk 1.00R is below strategy minimum 1.35R

**Risk flags:** OK

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## BIPI — position_xgb — NO_TRADE

**Score:** 0.560 vs policy min 0.55 · **Close:** 184 · **ATR14:** 26.9 · **Volume ratio 20D:** 2.01 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 171–187, entry trigger **187**, stop **170**, risk 17 points (9.09%).

**Targets:** TP1 **226** (2.29R), TP2 **234** (2.76R), TP3 **244** (3.35R). Recommended base-case RR: **2.76R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 184: zone 171–187 uses ATR14 26.9 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 187 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 170 is capped by max risk 9.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 226 (2.29R), TP2 234 (2.76R), TP3 244 (3.35R). Targets are ATR/structure capped for hold_days=1. ATR14=26.9, resistance_5/10/20/60=234/262/304/342. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 9.09% exceeds max strategy risk 9.00%; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## KOKA — position_xgb — NO_TRADE

**Score:** 0.560 vs policy min 0.55 · **Close:** 119 · **ATR14:** 15.6 · **Volume ratio 20D:** 3.32 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 111–121, entry trigger **121**, stop **110**, risk 11 points (9.09%).

**Targets:** TP1 **143** (2.00R), TP2 **148** (2.45R), TP3 **154** (3.00R). Recommended base-case RR: **2.45R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 119: zone 111–121 uses ATR14 15.6 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 121 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 110 is capped by max risk 9.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 143 (2.00R), TP2 148 (2.45R), TP3 154 (3.00R). Targets are ATR/structure capped for hold_days=1. ATR14=15.6, resistance_5/10/20/60=148/185/226/318. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 9.09% exceeds max strategy risk 9.00%; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## BUMI — position_xgb — NO_TRADE

**Score:** 0.557 vs policy min 0.55 · **Close:** 185 · **ATR14:** 17.9 · **Volume ratio 20D:** 1.77 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 176–187, entry trigger **187**, stop **170**, risk 17 points (9.09%).

**Targets:** TP1 **212** (1.47R), TP2 **216** (1.71R), TP3 **228** (2.41R). Recommended base-case RR: **1.71R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 185: zone 176–187 uses ATR14 17.9 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 187 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 170 is capped by max risk 9.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 212 (1.47R), TP2 216 (1.71R), TP3 228 (2.41R). Targets are ATR/structure capped for hold_days=1. ATR14=17.9, resistance_5/10/20/60=214/250/258/306. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 9.09% exceeds max strategy risk 9.00%

**Risk flags:** OK

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## FUTR — position_xgb — NO_TRADE

**Score:** 0.555 vs policy min 0.55 · **Close:** 183 · **ATR14:** 25.1 · **Volume ratio 20D:** 1.14 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 171–186, entry trigger **186**, stop **169**, risk 17 points (9.14%).

**Targets:** TP1 **204** (1.06R), TP2 **244** (3.41R), TP3 **254** (4.00R). Recommended base-case RR: **3.41R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 183: zone 171–186 uses ATR14 25.1 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 186 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 169 is capped by max risk 9.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 204 (1.06R), TP2 244 (3.41R), TP3 254 (4.00R). Targets are ATR/structure capped for hold_days=1. ATR14=25.1, resistance_5/10/20/60=244/246/288/410. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 9.14% exceeds max strategy risk 9.00%; TP1 reward/risk 1.06R is below strategy minimum 1.35R

**Risk flags:** OK

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## NCKL — position_xgb — NO_TRADE

**Score:** 0.552 vs policy min 0.55 · **Close:** 855 · **ATR14:** 62.9 · **Volume ratio 20D:** 1.23 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 825–865, entry trigger **865**, stop **785**, risk 80 points (9.25%).

**Targets:** TP1 **955** (1.12R), TP2 **1,005** (1.75R), TP3 **1,060** (2.44R). Recommended base-case RR: **1.75R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 855: zone 825–865 uses ATR14 62.9 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 865 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 785 is capped by max risk 9.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 955 (1.12R), TP2 1,005 (1.75R), TP3 1,060 (2.44R). Targets are ATR/structure capped for hold_days=1. ATR14=62.9, resistance_5/10/20/60=1,000/1,120/1,245/1,595. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 9.25% exceeds max strategy risk 9.00%; TP1 reward/risk 1.12R is below strategy minimum 1.35R

**Risk flags:** OK

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## PSAB — position_xgb — NO_TRADE

**Score:** 0.551 vs policy min 0.55 · **Close:** 426 · **ATR14:** 41.4 · **Volume ratio 20D:** 1.41 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 406–432, entry trigger **432**, stop **392**, risk 40 points (9.26%).

**Targets:** TP1 **490** (1.45R), TP2 **500** (1.70R), TP3 **530** (2.45R). Recommended base-case RR: **1.70R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 426: zone 406–432 uses ATR14 41.4 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 432 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 392 is capped by max risk 9.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 490 (1.45R), TP2 500 (1.70R), TP3 530 (2.45R). Targets are ATR/structure capped for hold_days=1. ATR14=41.4, resistance_5/10/20/60=496/580/590/590. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 9.26% exceeds max strategy risk 9.00%

**Risk flags:** OK

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## TRIN — position_xgb — NO_TRADE

**Score:** 0.550 vs policy min 0.55 · **Close:** 498 · **ATR14:** 69.6 · **Volume ratio 20D:** 1.03 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 466–505, entry trigger **505**, stop **458**, risk 47 points (9.31%).

**Targets:** TP1 **600** (2.02R), TP2 **625** (2.55R), TP3 **650** (3.09R). Recommended base-case RR: **2.55R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 498: zone 466–505 uses ATR14 69.6 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 505 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 458 is capped by max risk 9.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 600 (2.02R), TP2 625 (2.55R), TP3 650 (3.09R). Targets are ATR/structure capped for hold_days=1. ATR14=69.6, resistance_5/10/20/60=600/740/870/1,225. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 9.31% exceeds max strategy risk 9.00%

**Risk flags:** OK

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## INET — position_xgb — NO_TRADE

**Score:** 0.549 vs policy min 0.55 · **Close:** 230 · **ATR14:** 25.4 · **Volume ratio 20D:** 0.81 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 218–234, entry trigger **234**, stop **212**, risk 22 points (9.40%).

**Targets:** TP1 **270** (1.64R), TP2 **280** (2.09R), TP3 **288** (2.45R). Recommended base-case RR: **2.09R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 230: zone 218–234 uses ATR14 25.4 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 234 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 212 is capped by max risk 9.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 270 (1.64R), TP2 280 (2.09R), TP3 288 (2.45R). Targets are ATR/structure capped for hold_days=1. ATR14=25.4, resistance_5/10/20/60=280/324/360/438. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 9.40% exceeds max strategy risk 9.00%; score 0.549 below policy min_score 0.55

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## KING — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.538 vs policy min 0.60 · **Close:** 565 · **ATR14:** 61.4 · **Volume ratio 20D:** 1.02 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 550–570, entry trigger **570**, stop **510**, risk 60 points (10.53%).

**Targets:** TP1 **630** (1.00R), TP2 **675** (1.75R), TP3 **715** (2.42R). Recommended base-case RR: **1.75R**.

**Why entry:** Entry trigger 570 is set above recent resistance 565 plus one IDX tick. This requires confirmation instead of buying blindly at close 565. Entry is valid only if price can trade/hold around 570 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 510 is capped by max risk 10.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 630 (1.00R), TP2 675 (1.75R), TP3 715 (2.42R). Targets are ATR/structure capped for hold_days=2. ATR14=61.4, resistance_5/10/20/60=565/565/565/565. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 10.53% exceeds max strategy risk 10.00%; score 0.538 below policy min_score 0.60; TP1 reward/risk 1.00R is below strategy minimum 1.40R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## DSSA — momentum_5d_hgb_defensive — NO_TRADE

**Score:** 0.503 vs policy min 0.55 · **Close:** 545 · **ATR14:** 184.6 · **Volume ratio 20D:** 3.26 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 505–1,725, entry trigger **1,725**, stop **1,600**, risk 125 points (7.25%).

**Targets:** TP1 **1,850** (1.00R), TP2 **1,940** (1.72R), TP3 **2,030** (2.44R). Recommended base-case RR: **1.72R**.

**Why entry:** Entry trigger 1,725 is set above recent resistance 1,720 plus one IDX tick. This requires confirmation instead of buying blindly at close 545. Entry is valid only if price can trade/hold around 1,725 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 1,600 is capped by max risk 7.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,850 (1.00R), TP2 1,940 (1.72R), TP3 2,030 (2.44R). Targets are ATR/structure capped for hold_days=1. ATR14=184.6, resistance_5/10/20/60=945/1,720/3,400/98,000. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 216.51% > max 8.00%; entry-to-stop risk 7.25% exceeds max strategy risk 7.00%; score 0.503 below policy min_score 0.55; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Selective high-liquidity 5D momentum sleeve.

---

## SOTS — market_maker_silent_accum_defensive — NO_TRADE

**Score:** 0.493 vs policy min 0.55 · **Close:** 760 · **ATR14:** 116.1 · **Volume ratio 20D:** 1.52 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 715–785, entry trigger **785**, stop **725**, risk 60 points (7.64%).

**Targets:** TP1 **845** (1.00R), TP2 **985** (3.33R), TP3 **1,015** (3.83R). Recommended base-case RR: **3.33R**.

**Why entry:** Hybrid entry uses close 760 and ATR14 116.1: buy zone 715–785. Entry is valid only if price can trade/hold around 785 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 725 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 845 (1.00R), TP2 985 (3.33R), TP3 1,015 (3.83R). Targets are ATR/structure capped for hold_days=1. ATR14=116.1, resistance_5/10/20/60=985/1,060/1,500/2,930. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.64% exceeds max strategy risk 7.50%; score 0.493 below policy min_score 0.55; TP1 reward/risk 1.00R is below strategy minimum 1.25R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Defensive accumulation. Prefer retest and clean broker flow.

---

## IRSX — momentum_5d_hgb_defensive — NO_TRADE

**Score:** 0.487 vs policy min 0.55 · **Close:** 328 · **ATR14:** 45.7 · **Volume ratio 20D:** 2.40 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 318–482, entry trigger **482**, stop **448**, risk 34 points (7.05%).

**Targets:** TP1 **525** (1.26R), TP2 **540** (1.71R), TP3 **565** (2.44R). Recommended base-case RR: **1.71R**.

**Why entry:** Entry trigger 482 is set above recent resistance 480 plus one IDX tick. This requires confirmation instead of buying blindly at close 328. Entry is valid only if price can trade/hold around 482 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 448 is capped by max risk 7.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 525 (1.26R), TP2 540 (1.71R), TP3 565 (2.44R). Targets are ATR/structure capped for hold_days=1. ATR14=45.7, resistance_5/10/20/60=472/480/525/685. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 46.95% > max 8.00%; entry-to-stop risk 7.05% exceeds max strategy risk 7.00%; score 0.487 below policy min_score 0.55; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Selective high-liquidity 5D momentum sleeve.

---

## TMPO — market_maker_silent_accum_defensive — NO_TRADE

**Score:** 0.444 vs policy min 0.55 · **Close:** 108 · **ATR14:** 10.6 · **Volume ratio 20D:** 5.22 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 104–111, entry trigger **111**, stop **102**, risk 9 points (8.11%).

**Targets:** TP1 **120** (1.00R), TP2 **130** (2.11R), TP3 **133** (2.44R). Recommended base-case RR: **2.11R**.

**Why entry:** Hybrid entry uses close 108 and ATR14 10.6: buy zone 104–111. Entry is valid only if price can trade/hold around 111 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 102 is placed below support structure (103 / 103). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 120 (1.00R), TP2 130 (2.11R), TP3 133 (2.44R). Targets are ATR/structure capped for hold_days=1. ATR14=10.6, resistance_5/10/20/60=130/152/152/168. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.11% exceeds max strategy risk 7.50%; score 0.444 below policy min_score 0.55; TP1 reward/risk 1.00R is below strategy minimum 1.25R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Defensive accumulation. Prefer retest and clean broker flow.

---

## KOKA — market_maker_silent_accum_defensive — NO_TRADE

**Score:** 0.442 vs policy min 0.55 · **Close:** 119 · **ATR14:** 15.6 · **Volume ratio 20D:** 3.32 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 113–123, entry trigger **123**, stop **113**, risk 10 points (8.13%).

**Targets:** TP1 **133** (1.00R), TP2 **148** (2.50R), TP3 **153** (3.00R). Recommended base-case RR: **2.50R**.

**Why entry:** Hybrid entry uses close 119 and ATR14 15.6: buy zone 113–123. Entry is valid only if price can trade/hold around 123 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 113 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 133 (1.00R), TP2 148 (2.50R), TP3 153 (3.00R). Targets are ATR/structure capped for hold_days=1. ATR14=15.6, resistance_5/10/20/60=148/185/226/318. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.13% exceeds max strategy risk 7.50%; score 0.442 below policy min_score 0.55; TP1 reward/risk 1.00R is below strategy minimum 1.25R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Defensive accumulation. Prefer retest and clean broker flow.

---

## KIJA — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.441 vs policy min 0.60 · **Close:** 121 · **ATR14:** 10.1 · **Volume ratio 20D:** 2.37 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 118–190, entry trigger **190**, stop **176**, risk 14 points (7.37%).

**Targets:** TP1 **204** (1.00R), TP2 **220** (2.14R), TP3 **224** (2.43R). Recommended base-case RR: **2.14R**.

**Why entry:** Entry trigger 190 is set above recent resistance 189 plus one IDX tick. This requires confirmation instead of buying blindly at close 121. Entry is valid only if price can trade/hold around 190 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 176 uses 1.30×ATR14 volatility cap. Thesis invalidates if the move reverses beyond normal volatility. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 204 (1.00R), TP2 220 (2.14R), TP3 224 (2.43R). Targets are ATR/structure capped for hold_days=2. ATR14=10.1, resistance_5/10/20/60=174/189/220/240. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 57.02% > max 15.00%; score 0.441 below policy min_score 0.60; TP1 reward/risk 1.00R is below strategy minimum 1.40R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## CDIA — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.437 vs policy min 0.60 · **Close:** 750 · **ATR14:** 109.3 · **Volume ratio 20D:** 0.69 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 725–1,235, entry trigger **1,235**, stop **1,110**, risk 125 points (10.12%).

**Targets:** TP1 **1,360** (1.00R), TP2 **1,450** (1.72R), TP3 **1,535** (2.40R). Recommended base-case RR: **1.72R**.

**Why entry:** Entry trigger 1,235 is set above recent resistance 1,230 plus one IDX tick. This requires confirmation instead of buying blindly at close 750. Entry is valid only if price can trade/hold around 1,235 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 1,110 is capped by max risk 10.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,360 (1.00R), TP2 1,450 (1.72R), TP3 1,535 (2.40R). Targets are ATR/structure capped for hold_days=2. ATR14=109.3, resistance_5/10/20/60=1,000/1,230/1,255/1,340. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 64.67% > max 15.00%; entry-to-stop risk 10.12% exceeds max strategy risk 10.00%; score 0.437 below policy min_score 0.60; TP1 reward/risk 1.00R is below strategy minimum 1.40R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## BEEF — market_maker_silent_accum_defensive — NO_TRADE

**Score:** 0.426 vs policy min 0.55 · **Close:** 151 · **ATR14:** 22.6 · **Volume ratio 20D:** 1.33 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 143–156, entry trigger **156**, stop **144**, risk 12 points (7.69%).

**Targets:** TP1 **168** (1.00R), TP2 **188** (2.67R), TP3 **194** (3.17R). Recommended base-case RR: **2.67R**.

**Why entry:** Hybrid entry uses close 151 and ATR14 22.6: buy zone 143–156. Entry is valid only if price can trade/hold around 156 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 144 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 168 (1.00R), TP2 188 (2.67R), TP3 194 (3.17R). Targets are ATR/structure capped for hold_days=1. ATR14=22.6, resistance_5/10/20/60=188/212/302/388. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.69% exceeds max strategy risk 7.50%; score 0.426 below policy min_score 0.55; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Defensive accumulation. Prefer retest and clean broker flow.

---

## NZIA — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.426 vs policy min 0.60 · **Close:** 117 · **ATR14:** 16.4 · **Volume ratio 20D:** 0.40 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 113–184, entry trigger **184**, stop **165**, risk 19 points (10.33%).

**Targets:** TP1 **214** (1.58R), TP2 **218** (1.79R), TP3 **230** (2.42R). Recommended base-case RR: **1.79R**.

**Why entry:** Entry trigger 184 is set above recent resistance 183 plus one IDX tick. This requires confirmation instead of buying blindly at close 117. Entry is valid only if price can trade/hold around 184 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 165 is capped by max risk 10.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 214 (1.58R), TP2 218 (1.79R), TP3 230 (2.42R). Targets are ATR/structure capped for hold_days=2. ATR14=16.4, resistance_5/10/20/60=160/183/214/316. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 57.26% > max 15.00%; entry-to-stop risk 10.33% exceeds max strategy risk 10.00%; score 0.426 below policy min_score 0.60; volume ratio 0.40 below required 0.60

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## HRUM — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.425 vs policy min 0.60 · **Close:** 790 · **ATR14:** 53.9 · **Volume ratio 20D:** 2.55 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 775–1,020, entry trigger **1,020**, stop **945**, risk 75 points (7.35%).

**Targets:** TP1 **1,095** (1.00R), TP2 **1,150** (1.73R), TP3 **1,200** (2.40R). Recommended base-case RR: **1.73R**.

**Why entry:** Entry trigger 1,020 is set above recent resistance 1,015 plus one IDX tick. This requires confirmation instead of buying blindly at close 790. Entry is valid only if price can trade/hold around 1,020 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 945 uses 1.30×ATR14 volatility cap. Thesis invalidates if the move reverses beyond normal volatility. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,095 (1.00R), TP2 1,150 (1.73R), TP3 1,200 (2.40R). Targets are ATR/structure capped for hold_days=2. ATR14=53.9, resistance_5/10/20/60=895/1,015/1,060/1,270. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 29.11% > max 15.00%; score 0.425 below policy min_score 0.60; TP1 reward/risk 1.00R is below strategy minimum 1.40R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## SIMP — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.423 vs policy min 0.60 · **Close:** 560 · **ATR14:** 51.1 · **Volume ratio 20D:** 0.56 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 545–835, entry trigger **835**, stop **765**, risk 70 points (8.38%).

**Targets:** TP1 **920** (1.21R), TP2 **955** (1.71R), TP3 **1,005** (2.43R). Recommended base-case RR: **1.71R**.

**Why entry:** Entry trigger 835 is set above recent resistance 830 plus one IDX tick. This requires confirmation instead of buying blindly at close 560. Entry is valid only if price can trade/hold around 835 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 765 uses 1.30×ATR14 volatility cap. Thesis invalidates if the move reverses beyond normal volatility. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 920 (1.21R), TP2 955 (1.71R), TP3 1,005 (2.43R). Targets are ATR/structure capped for hold_days=2. ATR14=51.1, resistance_5/10/20/60=645/830/920/930. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 49.11% > max 15.00%; score 0.423 below policy min_score 0.60; TP1 reward/risk 1.21R is below strategy minimum 1.40R; volume ratio 0.56 below required 0.60

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## NSSS — market_maker_silent_accum_defensive — NO_TRADE

**Score:** 0.420 vs policy min 0.55 · **Close:** 472 · **ATR14:** 78.8 · **Volume ratio 20D:** 0.36 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 444–488, entry trigger **488**, stop **450**, risk 38 points (7.79%).

**Targets:** TP1 **530** (1.11R), TP2 **555** (1.76R), TP3 **580** (2.42R). Recommended base-case RR: **1.76R**.

**Why entry:** Hybrid entry uses close 472 and ATR14 78.8: buy zone 444–488. Entry is valid only if price can trade/hold around 488 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 450 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 530 (1.11R), TP2 555 (1.76R), TP3 580 (2.42R). Targets are ATR/structure capped for hold_days=1. ATR14=78.8, resistance_5/10/20/60=770/865/1,060/1,300. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.79% exceeds max strategy risk 7.50%; score 0.420 below policy min_score 0.55; TP1 reward/risk 1.11R is below strategy minimum 1.25R; volume ratio 0.36 below required 0.60

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Defensive accumulation. Prefer retest and clean broker flow.

---

## PART — market_maker_silent_accum_defensive — NO_TRADE

**Score:** 0.415 vs policy min 0.55 · **Close:** 102 · **ATR14:** 8.9 · **Volume ratio 20D:** 0.84 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 98–104, entry trigger **104**, stop **96**, risk 8 points (7.69%).

**Targets:** TP1 **113** (1.12R), TP2 **118** (1.75R), TP3 **124** (2.50R). Recommended base-case RR: **1.75R**.

**Why entry:** Hybrid entry uses close 102 and ATR14 8.9: buy zone 98–104. Entry is valid only if price can trade/hold around 104 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 96 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 113 (1.12R), TP2 118 (1.75R), TP3 124 (2.50R). Targets are ATR/structure capped for hold_days=1. ATR14=8.9, resistance_5/10/20/60=114/127/148/240. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.69% exceeds max strategy risk 7.50%; score 0.415 below policy min_score 0.55; TP1 reward/risk 1.12R is below strategy minimum 1.25R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Defensive accumulation. Prefer retest and clean broker flow.

---

## UNSP — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.414 vs policy min 0.60 · **Close:** 248 · **ATR14:** 24.7 · **Volume ratio 20D:** 0.76 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 242–394, entry trigger **394**, stop **360**, risk 34 points (8.63%).

**Targets:** TP1 **440** (1.35R), TP2 **452** (1.71R), TP3 **476** (2.41R). Recommended base-case RR: **1.71R**.

**Why entry:** Entry trigger 394 is set above recent resistance 392 plus one IDX tick. This requires confirmation instead of buying blindly at close 248. Entry is valid only if price can trade/hold around 394 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 360 uses 1.30×ATR14 volatility cap. Thesis invalidates if the move reverses beyond normal volatility. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 440 (1.35R), TP2 452 (1.71R), TP3 476 (2.41R). Targets are ATR/structure capped for hold_days=2. ATR14=24.7, resistance_5/10/20/60=290/392/450/450. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 58.87% > max 15.00%; score 0.414 below policy min_score 0.60; TP1 reward/risk 1.35R is below strategy minimum 1.40R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## TRIN — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.413 vs policy min 0.60 · **Close:** 498 · **ATR14:** 69.6 · **Volume ratio 20D:** 1.03 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 484–745, entry trigger **745**, stop **670**, risk 75 points (10.07%).

**Targets:** TP1 **870** (1.67R), TP2 **875** (1.73R), TP3 **925** (2.40R). Recommended base-case RR: **1.73R**.

**Why entry:** Entry trigger 745 is set above recent resistance 740 plus one IDX tick. This requires confirmation instead of buying blindly at close 498. Entry is valid only if price can trade/hold around 745 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 670 is capped by max risk 10.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 870 (1.67R), TP2 875 (1.73R), TP3 925 (2.40R). Targets are ATR/structure capped for hold_days=2. ATR14=69.6, resistance_5/10/20/60=600/740/870/1,225. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 49.60% > max 15.00%; entry-to-stop risk 10.07% exceeds max strategy risk 10.00%; score 0.413 below policy min_score 0.60

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## PBSA — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.411 vs policy min 0.60 · **Close:** 850 · **ATR14:** 92.5 · **Volume ratio 20D:** 2.72 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 830–1,180, entry trigger **1,180**, stop **1,060**, risk 120 points (10.17%).

**Targets:** TP1 **1,300** (1.00R), TP2 **1,385** (1.71R), TP3 **1,470** (2.42R). Recommended base-case RR: **1.71R**.

**Why entry:** Entry trigger 1,180 is set above recent resistance 1,175 plus one IDX tick. This requires confirmation instead of buying blindly at close 850. Entry is valid only if price can trade/hold around 1,180 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 1,060 is capped by max risk 10.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,300 (1.00R), TP2 1,385 (1.71R), TP3 1,470 (2.42R). Targets are ATR/structure capped for hold_days=2. ATR14=92.5, resistance_5/10/20/60=900/1,175/1,255/1,585. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 38.82% > max 15.00%; entry-to-stop risk 10.17% exceeds max strategy risk 10.00%; score 0.411 below policy min_score 0.60; TP1 reward/risk 1.00R is below strategy minimum 1.40R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## RMKO — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.410 vs policy min 0.60 · **Close:** 346 · **ATR14:** 43.7 · **Volume ratio 20D:** 1.15 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 336–510, entry trigger **510**, stop **458**, risk 52 points (10.20%).

**Targets:** TP1 **565** (1.06R), TP2 **645** (2.60R), TP3 **675** (3.17R). Recommended base-case RR: **2.60R**.

**Why entry:** Entry trigger 510 is set above recent resistance 505 plus one IDX tick. This requires confirmation instead of buying blindly at close 346. Entry is valid only if price can trade/hold around 510 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 458 is capped by max risk 10.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 565 (1.06R), TP2 645 (2.60R), TP3 675 (3.17R). Targets are ATR/structure capped for hold_days=2. ATR14=43.7, resistance_5/10/20/60=452/505/645/1,180. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 47.40% > max 15.00%; entry-to-stop risk 10.20% exceeds max strategy risk 10.00%; score 0.410 below policy min_score 0.60; TP1 reward/risk 1.06R is below strategy minimum 1.40R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## COIN — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.409 vs policy min 0.60 · **Close:** 835 · **ATR14:** 117.1 · **Volume ratio 20D:** 0.62 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 810–1,375, entry trigger **1,375**, stop **1,235**, risk 140 points (10.18%).

**Targets:** TP1 **1,515** (1.00R), TP2 **1,615** (1.71R), TP3 **1,715** (2.43R). Recommended base-case RR: **1.71R**.

**Why entry:** Entry trigger 1,375 is set above recent resistance 1,370 plus one IDX tick. This requires confirmation instead of buying blindly at close 835. Entry is valid only if price can trade/hold around 1,375 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 1,235 is capped by max risk 10.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,515 (1.00R), TP2 1,615 (1.71R), TP3 1,715 (2.43R). Targets are ATR/structure capped for hold_days=2. ATR14=117.1, resistance_5/10/20/60=1,020/1,370/1,465/2,080. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 64.67% > max 15.00%; entry-to-stop risk 10.18% exceeds max strategy risk 10.00%; score 0.409 below policy min_score 0.60; TP1 reward/risk 1.00R is below strategy minimum 1.40R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## PYFA — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.408 vs policy min 0.60 · **Close:** 242 · **ATR14:** 36.7 · **Volume ratio 20D:** 0.66 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 234–382, entry trigger **382**, stop **342**, risk 40 points (10.47%).

**Targets:** TP1 **422** (1.00R), TP2 **450** (1.70R), TP3 **478** (2.40R). Recommended base-case RR: **1.70R**.

**Why entry:** Entry trigger 382 is set above recent resistance 380 plus one IDX tick. This requires confirmation instead of buying blindly at close 242. Entry is valid only if price can trade/hold around 382 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 342 is capped by max risk 10.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 422 (1.00R), TP2 450 (1.70R), TP3 478 (2.40R). Targets are ATR/structure capped for hold_days=2. ATR14=36.7, resistance_5/10/20/60=318/380/406/466. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 57.85% > max 15.00%; entry-to-stop risk 10.47% exceeds max strategy risk 10.00%; score 0.408 below policy min_score 0.60; TP1 reward/risk 1.00R is below strategy minimum 1.40R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## BMTR — market_maker_silent_accum_defensive — NO_TRADE

**Score:** 0.407 vs policy min 0.55 · **Close:** 130 · **ATR14:** 9.8 · **Volume ratio 20D:** 0.47 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 126–132, entry trigger **132**, stop **122**, risk 10 points (7.58%).

**Targets:** TP1 **142** (1.00R), TP2 **149** (1.70R), TP3 **156** (2.40R). Recommended base-case RR: **1.70R**.

**Why entry:** Hybrid entry uses close 130 and ATR14 9.8: buy zone 126–132. Entry is valid only if price can trade/hold around 132 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 122 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 142 (1.00R), TP2 149 (1.70R), TP3 156 (2.40R). Targets are ATR/structure capped for hold_days=1. ATR14=9.8, resistance_5/10/20/60=143/178/204/204. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.58% exceeds max strategy risk 7.50%; score 0.407 below policy min_score 0.55; TP1 reward/risk 1.00R is below strategy minimum 1.25R; volume ratio 0.47 below required 0.60

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Defensive accumulation. Prefer retest and clean broker flow.

---

## PBSA — ara_candidate — NO_TRADE

**Score:** 0.357 vs policy min 0.50 · **Close:** 850 · **ATR14:** 92.5 · **Volume ratio 20D:** 2.72 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 830–1,180, entry trigger **1,180**, stop **1,075**, risk 105 points (8.90%).

**Targets:** TP1 **1,275** (0.90R), TP2 **1,360** (1.71R), TP3 **1,435** (2.43R). Recommended base-case RR: **1.71R**.

**Why entry:** Entry trigger 1,180 is set above recent resistance 1,175 plus one IDX tick. This requires confirmation instead of buying blindly at close 850. Entry is valid only if price can trade/hold around 1,180 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 1,075 uses 1.10×ATR14 volatility cap. Thesis invalidates if the move reverses beyond normal volatility. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,275 (0.90R), TP2 1,360 (1.71R), TP3 1,435 (2.43R). Targets are ATR/structure capped for hold_days=1. ATR14=92.5, resistance_5/10/20/60=900/1,175/1,255/1,585. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 38.82% > max 12.00%; score 0.357 below policy min_score 0.50; TP1 reward/risk 0.90R is below strategy minimum 1.30R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** High drawdown tactical setup. Use as execution only if confirmation is strong and liquidity is clean.

---
