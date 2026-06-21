# Numeric Trading Desk Report — 2026-06-12

This report is generated from live model scores, selected signal policy, canonical OHLCV, ATR, support/resistance, liquidity, and broker-flow diagnostics. It is not a simple BUY/SELL list; each plan is conditional on execution behaviour.

## Summary

| Plan quality | Count |
|---|---:|
| CONDITIONAL | 2 |
| WATCHLIST_ONLY | 2 |
| NO_TRADE | 52 |

## TOWR — position_xgb — CONDITIONAL

**Score:** 0.581 vs policy min 0.55 · **Close:** 344 · **ATR14:** 20.9 · **Volume ratio 20D:** 2.43 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 334–348, entry trigger **348**, stop **318**, risk 30 points (8.62%).

**Targets:** TP1 **378** (1.00R), TP2 **400** (1.73R), TP3 **420** (2.40R). Recommended base-case RR: **1.73R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 344: zone 334–348 uses ATR14 20.9 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 348 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 318 uses 1.40×ATR14 volatility cap. Thesis invalidates if the move reverses beyond normal volatility. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 378 (1.00R), TP2 400 (1.73R), TP3 420 (2.40R). Targets are ATR/structure capped for hold_days=1. ATR14=20.9, resistance_5/10/20/60=354/398/476/520. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.35R

**Risk flags:** OK

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## OMED — market_maker_silent_accum_defensive — CONDITIONAL

**Score:** 0.578 vs policy min 0.55 · **Close:** 196 · **ATR14:** 17.3 · **Volume ratio 20D:** 1.40 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 189–200, entry trigger **200**, stop **185**, risk 15 points (7.50%).

**Targets:** TP1 **216** (1.07R), TP2 **226** (1.73R), TP3 **236** (2.40R). Recommended base-case RR: **1.73R**.

**Why entry:** Hybrid entry uses close 196 and ATR14 17.3: buy zone 189–200. Entry is valid only if price can trade/hold around 200 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 185 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 216 (1.07R), TP2 226 (1.73R), TP3 236 (2.40R). Targets are ATR/structure capped for hold_days=1. ATR14=17.3, resistance_5/10/20/60=206/240/310/318. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.07R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Defensive accumulation. Prefer retest and clean broker flow.

---

## CYBR — momentum_10d_hgb_aggressive — WATCHLIST_ONLY

**Score:** 0.365 vs policy min 0.60 · **Close:** 615 · **ATR14:** 41.1 · **Volume ratio 20D:** 1.48 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 605–645, entry trigger **645**, stop **590**, risk 55 points (8.53%).

**Targets:** TP1 **700** (1.00R), TP2 **740** (1.73R), TP3 **780** (2.45R). Recommended base-case RR: **1.73R**.

**Why entry:** Entry trigger 645 is set above recent resistance 640 plus one IDX tick. This requires confirmation instead of buying blindly at close 615. Entry is valid only if price can trade/hold around 645 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 590 uses 1.30×ATR14 volatility cap. Thesis invalidates if the move reverses beyond normal volatility. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 700 (1.00R), TP2 740 (1.73R), TP3 780 (2.45R). Targets are ATR/structure capped for hold_days=2. ATR14=41.1, resistance_5/10/20/60=640/640/1,325/1,590. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** score 0.365 below policy min_score 0.60; TP1 reward/risk 1.00R is below strategy minimum 1.40R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## RSCH — momentum_10d_hgb_aggressive — WATCHLIST_ONLY

**Score:** 0.361 vs policy min 0.60 · **Close:** 316 · **ATR14:** 17.3 · **Volume ratio 20D:** 0.76 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 312–324, entry trigger **324**, stop **300**, risk 24 points (7.41%).

**Targets:** TP1 **348** (1.00R), TP2 **382** (2.42R), TP3 **394** (2.92R). Recommended base-case RR: **2.42R**.

**Why entry:** Entry trigger 324 is set above recent resistance 322 plus one IDX tick. This requires confirmation instead of buying blindly at close 316. Entry is valid only if price can trade/hold around 324 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 300 uses 1.30×ATR14 volatility cap. Thesis invalidates if the move reverses beyond normal volatility. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 348 (1.00R), TP2 382 (2.42R), TP3 394 (2.92R). Targets are ATR/structure capped for hold_days=2. ATR14=17.3, resistance_5/10/20/60=322/322/322/394. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** score 0.361 below policy min_score 0.60; TP1 reward/risk 1.00R is below strategy minimum 1.40R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## OASA — swing_hgb_defensive — NO_TRADE

**Score:** 0.674 vs policy min 0.50 · **Close:** 260 · **ATR14:** 38.3 · **Volume ratio 20D:** 0.67 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 242–264, entry trigger **264**, stop **244**, risk 20 points (7.58%).

**Targets:** TP1 **284** (1.00R), TP2 **298** (1.70R), TP3 **360** (4.80R). Recommended base-case RR: **1.70R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 260: zone 242–264 uses ATR14 38.3 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 264 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 244 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 284 (1.00R), TP2 298 (1.70R), TP3 360 (4.80R). Targets are ATR/structure capped for hold_days=1. ATR14=38.3, resistance_5/10/20/60=268/372/432/466. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.58% exceeds max strategy risk 7.50%; TP1 reward/risk 1.00R is below strategy minimum 1.25R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## SSMS — swing_hgb_defensive — NO_TRADE

**Score:** 0.660 vs policy min 0.50 · **Close:** 745 · **ATR14:** 72.5 · **Volume ratio 20D:** 0.98 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 710–755, entry trigger **755**, stop **695**, risk 60 points (7.95%).

**Targets:** TP1 **815** (1.00R), TP2 **860** (1.75R), TP3 **900** (2.42R). Recommended base-case RR: **1.75R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 745: zone 710–755 uses ATR14 72.5 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 755 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 695 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 815 (1.00R), TP2 860 (1.75R), TP3 900 (2.42R). Targets are ATR/structure capped for hold_days=1. ATR14=72.5, resistance_5/10/20/60=775/825/1,430/1,500. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.95% exceeds max strategy risk 7.50%; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## SOCI — swing_hgb_defensive — NO_TRADE

**Score:** 0.648 vs policy min 0.50 · **Close:** 322 · **ATR14:** 39.6 · **Volume ratio 20D:** 1.35 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 304–326, entry trigger **326**, stop **300**, risk 26 points (7.98%).

**Targets:** TP1 **352** (1.00R), TP2 **372** (1.77R), TP3 **390** (2.46R). Recommended base-case RR: **1.77R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 322: zone 304–326 uses ATR14 39.6 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 326 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 300 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 352 (1.00R), TP2 372 (1.77R), TP3 390 (2.46R). Targets are ATR/structure capped for hold_days=1. ATR14=39.6, resistance_5/10/20/60=348/416/480/700. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.98% exceeds max strategy risk 7.50%; TP1 reward/risk 1.00R is below strategy minimum 1.25R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## NIKL — swing_hgb_defensive — NO_TRADE

**Score:** 0.644 vs policy min 0.50 · **Close:** 192 · **ATR14:** 27.1 · **Volume ratio 20D:** 0.60 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 179–195, entry trigger **195**, stop **180**, risk 15 points (7.69%).

**Targets:** TP1 **210** (1.00R), TP2 **240** (3.00R), TP3 **248** (3.53R). Recommended base-case RR: **3.00R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 192: zone 179–195 uses ATR14 27.1 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 195 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 180 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 210 (1.00R), TP2 240 (3.00R), TP3 248 (3.53R). Targets are ATR/structure capped for hold_days=1. ATR14=27.1, resistance_5/10/20/60=240/260/370/510. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.69% exceeds max strategy risk 7.50%; TP1 reward/risk 1.00R is below strategy minimum 1.25R; volume ratio 0.60 below required 0.60

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## GPSO — swing_hgb_defensive — NO_TRADE

**Score:** 0.643 vs policy min 0.50 · **Close:** 336 · **ATR14:** 31.0 · **Volume ratio 20D:** 2.32 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 322–340, entry trigger **340**, stop **314**, risk 26 points (7.65%).

**Targets:** TP1 **372** (1.23R), TP2 **386** (1.77R), TP3 **404** (2.46R). Recommended base-case RR: **1.77R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 336: zone 322–340 uses ATR14 31.0 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 340 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 314 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 372 (1.23R), TP2 386 (1.77R), TP3 404 (2.46R). Targets are ATR/structure capped for hold_days=1. ATR14=31.0, resistance_5/10/20/60=380/520/520/520. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.65% exceeds max strategy risk 7.50%; TP1 reward/risk 1.23R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## ARCI — swing_hgb_defensive — NO_TRADE

**Score:** 0.640 vs policy min 0.50 · **Close:** 975 · **ATR14:** 104.6 · **Volume ratio 20D:** 1.62 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 925–990, entry trigger **990**, stop **915**, risk 75 points (7.58%).

**Targets:** TP1 **1,065** (1.00R), TP2 **1,120** (1.73R), TP3 **1,240** (3.33R). Recommended base-case RR: **1.73R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 975: zone 925–990 uses ATR14 104.6 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 990 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 915 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,065 (1.00R), TP2 1,120 (1.73R), TP3 1,240 (3.33R). Targets are ATR/structure capped for hold_days=1. ATR14=104.6, resistance_5/10/20/60=1,015/1,240/1,475/1,840. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.58% exceeds max strategy risk 7.50%; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## SCMA — swing_hgb_defensive — NO_TRADE

**Score:** 0.635 vs policy min 0.50 · **Close:** 200 · **ATR14:** 16.9 · **Volume ratio 20D:** 0.86 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 192–202, entry trigger **202**, stop **186**, risk 16 points (7.92%).

**Targets:** TP1 **218** (1.00R), TP2 **230** (1.75R), TP3 **242** (2.50R). Recommended base-case RR: **1.75R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 200: zone 192–202 uses ATR14 16.9 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 202 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 186 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 218 (1.00R), TP2 230 (1.75R), TP3 242 (2.50R). Targets are ATR/structure capped for hold_days=1. ATR14=16.9, resistance_5/10/20/60=210/232/254/312. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.92% exceeds max strategy risk 7.50%; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## APLN — swing_hgb_defensive — NO_TRADE

**Score:** 0.634 vs policy min 0.50 · **Close:** 126 · **ATR14:** 12.1 · **Volume ratio 20D:** 0.59 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 120–128, entry trigger **128**, stop **118**, risk 10 points (7.81%).

**Targets:** TP1 **138** (1.00R), TP2 **150** (2.20R), TP3 **156** (2.80R). Recommended base-case RR: **2.20R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 126: zone 120–128 uses ATR14 12.1 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 128 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 118 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 138 (1.00R), TP2 150 (2.20R), TP3 156 (2.80R). Targets are ATR/structure capped for hold_days=1. ATR14=12.1, resistance_5/10/20/60=131/156/191/240. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.81% exceeds max strategy risk 7.50%; TP1 reward/risk 1.00R is below strategy minimum 1.25R; volume ratio 0.59 below required 0.60

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## BBYB — swing_hgb_defensive — NO_TRADE

**Score:** 0.633 vs policy min 0.50 · **Close:** 234 · **ATR14:** 19.7 · **Volume ratio 20D:** 0.87 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 224–236, entry trigger **236**, stop **218**, risk 18 points (7.63%).

**Targets:** TP1 **254** (1.00R), TP2 **272** (2.00R), TP3 **280** (2.44R). Recommended base-case RR: **2.00R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 234: zone 224–236 uses ATR14 19.7 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 236 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 218 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 254 (1.00R), TP2 272 (2.00R), TP3 280 (2.44R). Targets are ATR/structure capped for hold_days=1. ATR14=19.7, resistance_5/10/20/60=238/274/310/352. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.63% exceeds max strategy risk 7.50%; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## GTSI — swing_hgb_defensive — NO_TRADE

**Score:** 0.630 vs policy min 0.50 · **Close:** 134 · **ATR14:** 18.9 · **Volume ratio 20D:** 1.26 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 125–136, entry trigger **136**, stop **125**, risk 11 points (8.09%).

**Targets:** TP1 **147** (1.00R), TP2 **164** (2.55R), TP3 **170** (3.09R). Recommended base-case RR: **2.55R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 134: zone 125–136 uses ATR14 18.9 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 136 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 125 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 147 (1.00R), TP2 164 (2.55R), TP3 170 (3.09R). Targets are ATR/structure capped for hold_days=1. ATR14=18.9, resistance_5/10/20/60=139/164/222/294. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.09% exceeds max strategy risk 7.50%; TP1 reward/risk 1.00R is below strategy minimum 1.25R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## KIJA — swing_hgb_defensive — NO_TRADE

**Score:** 0.628 vs policy min 0.50 · **Close:** 116 · **ATR14:** 9.4 · **Volume ratio 20D:** 0.75 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 111–117, entry trigger **117**, stop **108**, risk 9 points (7.69%).

**Targets:** TP1 **126** (1.00R), TP2 **133** (1.78R), TP3 **139** (2.44R). Recommended base-case RR: **1.78R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 116: zone 111–117 uses ATR14 9.4 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 117 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 108 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 126 (1.00R), TP2 133 (1.78R), TP3 139 (2.44R). Targets are ATR/structure capped for hold_days=1. ATR14=9.4, resistance_5/10/20/60=117/125/181/220. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.69% exceeds max strategy risk 7.50%; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## HRUM — swing_hgb_defensive — NO_TRADE

**Score:** 0.627 vs policy min 0.50 · **Close:** 785 · **ATR14:** 70.0 · **Volume ratio 20D:** 1.13 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 750–795, entry trigger **795**, stop **735**, risk 60 points (7.55%).

**Targets:** TP1 **855** (1.00R), TP2 **900** (1.75R), TP3 **940** (2.42R). Recommended base-case RR: **1.75R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 785: zone 750–795 uses ATR14 70.0 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 795 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 735 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 855 (1.00R), TP2 900 (1.75R), TP3 940 (2.42R). Targets are ATR/structure capped for hold_days=1. ATR14=70.0, resistance_5/10/20/60=800/825/950/1,155. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.55% exceeds max strategy risk 7.50%; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## TOBA — swing_hgb_defensive — NO_TRADE

**Score:** 0.627 vs policy min 0.50 · **Close:** 402 · **ATR14:** 40.1 · **Volume ratio 20D:** 0.91 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 382–408, entry trigger **408**, stop **376**, risk 32 points (7.84%).

**Targets:** TP1 **450** (1.31R), TP2 **464** (1.75R), TP3 **486** (2.44R). Recommended base-case RR: **1.75R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 402: zone 382–408 uses ATR14 40.1 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 408 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 376 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 450 (1.31R), TP2 464 (1.75R), TP3 486 (2.44R). Targets are ATR/structure capped for hold_days=1. ATR14=40.1, resistance_5/10/20/60=412/452/590/705. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.84% exceeds max strategy risk 7.50%

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## INDS — market_maker_silent_accum_defensive — NO_TRADE

**Score:** 0.626 vs policy min 0.55 · **Close:** 272 · **ATR14:** 27.6 · **Volume ratio 20D:** 3.39 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 262–278, entry trigger **278**, stop **256**, risk 22 points (7.91%).

**Targets:** TP1 **306** (1.27R), TP2 **318** (1.82R), TP3 **332** (2.45R). Recommended base-case RR: **1.82R**.

**Why entry:** Hybrid entry uses close 272 and ATR14 27.6: buy zone 262–278. Entry is valid only if price can trade/hold around 278 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 256 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 306 (1.27R), TP2 318 (1.82R), TP3 332 (2.45R). Targets are ATR/structure capped for hold_days=1. ATR14=27.6, resistance_5/10/20/60=318/318/394/1,030. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.91% exceeds max strategy risk 7.50%; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Defensive accumulation. Prefer retest and clean broker flow.

---

## PYFA — swing_hgb_defensive — NO_TRADE

**Score:** 0.624 vs policy min 0.50 · **Close:** 194 · **ATR14:** 23.9 · **Volume ratio 20D:** 0.66 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 183–197, entry trigger **197**, stop **182**, risk 15 points (7.61%).

**Targets:** TP1 **212** (1.00R), TP2 **224** (1.80R), TP3 **234** (2.47R). Recommended base-case RR: **1.80R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 194: zone 183–197 uses ATR14 23.9 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 197 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 182 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 212 (1.00R), TP2 224 (1.80R), TP3 234 (2.47R). Targets are ATR/structure capped for hold_days=1. ATR14=23.9, resistance_5/10/20/60=208/242/422/446. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.61% exceeds max strategy risk 7.50%; TP1 reward/risk 1.00R is below strategy minimum 1.25R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## DEFI — swing_hgb_defensive — NO_TRADE

**Score:** 0.623 vs policy min 0.50 · **Close:** 113 · **ATR14:** 20.9 · **Volume ratio 20D:** 1.29 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 103–116, entry trigger **116**, stop **107**, risk 9 points (7.76%).

**Targets:** TP1 **127** (1.22R), TP2 **132** (1.78R), TP3 **138** (2.44R). Recommended base-case RR: **1.78R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 113: zone 103–116 uses ATR14 20.9 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 116 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 107 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 127 (1.22R), TP2 132 (1.78R), TP3 138 (2.44R). Targets are ATR/structure capped for hold_days=1. ATR14=20.9, resistance_5/10/20/60=124/145/212/274. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.76% exceeds max strategy risk 7.50%; TP1 reward/risk 1.22R is below strategy minimum 1.25R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## SUPA — position_xgb — NO_TRADE

**Score:** 0.610 vs policy min 0.55 · **Close:** 615 · **ATR14:** 62.9 · **Volume ratio 20D:** 1.06 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 585–625, entry trigger **625**, stop **565**, risk 60 points (9.60%).

**Targets:** TP1 **685** (1.00R), TP2 **730** (1.75R), TP3 **770** (2.42R). Recommended base-case RR: **1.75R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 615: zone 585–625 uses ATR14 62.9 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 625 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 565 is capped by max risk 9.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 685 (1.00R), TP2 730 (1.75R), TP3 770 (2.42R). Targets are ATR/structure capped for hold_days=1. ATR14=62.9, resistance_5/10/20/60=675/880/905/970. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 9.60% exceeds max strategy risk 9.00%; TP1 reward/risk 1.00R is below strategy minimum 1.35R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## KIJA — market_maker_silent_accum_defensive — NO_TRADE

**Score:** 0.609 vs policy min 0.55 · **Close:** 116 · **ATR14:** 9.4 · **Volume ratio 20D:** 0.75 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 112–118, entry trigger **118**, stop **109**, risk 9 points (7.63%).

**Targets:** TP1 **127** (1.00R), TP2 **134** (1.78R), TP3 **140** (2.44R). Recommended base-case RR: **1.78R**.

**Why entry:** Hybrid entry uses close 116 and ATR14 9.4: buy zone 112–118. Entry is valid only if price can trade/hold around 118 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 109 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 127 (1.00R), TP2 134 (1.78R), TP3 140 (2.44R). Targets are ATR/structure capped for hold_days=1. ATR14=9.4, resistance_5/10/20/60=117/125/181/220. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.63% exceeds max strategy risk 7.50%; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Defensive accumulation. Prefer retest and clean broker flow.

---

## GPSO — position_xgb — NO_TRADE

**Score:** 0.609 vs policy min 0.55 · **Close:** 336 · **ATR14:** 31.0 · **Volume ratio 20D:** 2.32 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 322–340, entry trigger **340**, stop **308**, risk 32 points (9.41%).

**Targets:** TP1 **380** (1.25R), TP2 **396** (1.75R), TP3 **418** (2.44R). Recommended base-case RR: **1.75R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 336: zone 322–340 uses ATR14 31.0 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 340 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 308 is capped by max risk 9.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 380 (1.25R), TP2 396 (1.75R), TP3 418 (2.44R). Targets are ATR/structure capped for hold_days=1. ATR14=31.0, resistance_5/10/20/60=380/520/520/520. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 9.41% exceeds max strategy risk 9.00%; TP1 reward/risk 1.25R is below strategy minimum 1.35R

**Risk flags:** OK

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## CTTH — market_maker_silent_accum_defensive — NO_TRADE

**Score:** 0.606 vs policy min 0.55 · **Close:** 137 · **ATR14:** 34.3 · **Volume ratio 20D:** 2.78 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 125–144, entry trigger **144**, stop **133**, risk 11 points (7.64%).

**Targets:** TP1 **167** (2.09R), TP2 **173** (2.64R), TP3 **179** (3.18R). Recommended base-case RR: **2.64R**.

**Why entry:** Hybrid entry uses close 137 and ATR14 34.3: buy zone 125–144. Entry is valid only if price can trade/hold around 144 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 133 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 167 (2.09R), TP2 173 (2.64R), TP3 179 (3.18R). Targets are ATR/structure capped for hold_days=1. ATR14=34.3, resistance_5/10/20/60=167/176/182/216. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.64% exceeds max strategy risk 7.50%; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Defensive accumulation. Prefer retest and clean broker flow.

---

## ESSA — position_xgb — NO_TRADE

**Score:** 0.594 vs policy min 0.55 · **Close:** 600 · **ATR14:** 51.4 · **Volume ratio 20D:** 1.17 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 575–610, entry trigger **610**, stop **555**, risk 55 points (9.02%).

**Targets:** TP1 **665** (1.00R), TP2 **705** (1.73R), TP3 **745** (2.45R). Recommended base-case RR: **1.73R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 600: zone 575–610 uses ATR14 51.4 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 610 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 555 is capped by max risk 9.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 665 (1.00R), TP2 705 (1.73R), TP3 745 (2.45R). Targets are ATR/structure capped for hold_days=1. ATR14=51.4, resistance_5/10/20/60=635/710/845/995. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 9.02% exceeds max strategy risk 9.00%; TP1 reward/risk 1.00R is below strategy minimum 1.35R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## PSKT — market_maker_silent_accum_defensive — NO_TRADE

**Score:** 0.592 vs policy min 0.55 · **Close:** 189 · **ATR14:** 25.5 · **Volume ratio 20D:** 0.94 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 180–195, entry trigger **195**, stop **180**, risk 15 points (7.69%).

**Targets:** TP1 **210** (1.00R), TP2 **234** (2.60R), TP3 **242** (3.13R). Recommended base-case RR: **2.60R**.

**Why entry:** Hybrid entry uses close 189 and ATR14 25.5: buy zone 180–195. Entry is valid only if price can trade/hold around 195 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 180 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 210 (1.00R), TP2 234 (2.60R), TP3 242 (3.13R). Targets are ATR/structure capped for hold_days=1. ATR14=25.5, resistance_5/10/20/60=199/234/270/316. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.69% exceeds max strategy risk 7.50%; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Defensive accumulation. Prefer retest and clean broker flow.

---

## EMTK — position_xgb — NO_TRADE

**Score:** 0.590 vs policy min 0.55 · **Close:** 550 · **ATR14:** 46.9 · **Volume ratio 20D:** 0.82 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 525–555, entry trigger **555**, stop **505**, risk 50 points (9.01%).

**Targets:** TP1 **605** (1.00R), TP2 **640** (1.70R), TP3 **675** (2.40R). Recommended base-case RR: **1.70R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 550: zone 525–555 uses ATR14 46.9 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 555 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 505 is capped by max risk 9.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 605 (1.00R), TP2 640 (1.70R), TP3 675 (2.40R). Targets are ATR/structure capped for hold_days=1. ATR14=46.9, resistance_5/10/20/60=570/665/760/975. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 9.01% exceeds max strategy risk 9.00%; TP1 reward/risk 1.00R is below strategy minimum 1.35R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## ARCI — position_xgb — NO_TRADE

**Score:** 0.589 vs policy min 0.55 · **Close:** 975 · **ATR14:** 104.6 · **Volume ratio 20D:** 1.62 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 925–990, entry trigger **990**, stop **900**, risk 90 points (9.09%).

**Targets:** TP1 **1,080** (1.00R), TP2 **1,240** (2.78R), TP3 **1,285** (3.28R). Recommended base-case RR: **2.78R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 975: zone 925–990 uses ATR14 104.6 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 990 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 900 is capped by max risk 9.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,080 (1.00R), TP2 1,240 (2.78R), TP3 1,285 (3.28R). Targets are ATR/structure capped for hold_days=1. ATR14=104.6, resistance_5/10/20/60=1,015/1,240/1,475/1,840. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 9.09% exceeds max strategy risk 9.00%; TP1 reward/risk 1.00R is below strategy minimum 1.35R

**Risk flags:** OK

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## APLN — position_xgb — NO_TRADE

**Score:** 0.584 vs policy min 0.55 · **Close:** 126 · **ATR14:** 12.1 · **Volume ratio 20D:** 0.59 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 120–128, entry trigger **128**, stop **116**, risk 12 points (9.38%).

**Targets:** TP1 **140** (1.00R), TP2 **156** (2.33R), TP3 **157** (2.42R). Recommended base-case RR: **2.33R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 126: zone 120–128 uses ATR14 12.1 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 128 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 116 is capped by max risk 9.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 140 (1.00R), TP2 156 (2.33R), TP3 157 (2.42R). Targets are ATR/structure capped for hold_days=1. ATR14=12.1, resistance_5/10/20/60=131/156/191/240. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 9.38% exceeds max strategy risk 9.00%; TP1 reward/risk 1.00R is below strategy minimum 1.35R; volume ratio 0.59 below required 0.60

**Risk flags:** OK

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## BRMS — position_xgb — NO_TRADE

**Score:** 0.580 vs policy min 0.55 · **Close:** 530 · **ATR14:** 67.0 · **Volume ratio 20D:** 1.49 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 498–540, entry trigger **540**, stop **490**, risk 50 points (9.26%).

**Targets:** TP1 **590** (1.00R), TP2 **625** (1.70R), TP3 **660** (2.40R). Recommended base-case RR: **1.70R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 530: zone 498–540 uses ATR14 67.0 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 540 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 490 is capped by max risk 9.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 590 (1.00R), TP2 625 (1.70R), TP3 660 (2.40R). Targets are ATR/structure capped for hold_days=1. ATR14=67.0, resistance_5/10/20/60=565/635/795/930. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 9.26% exceeds max strategy risk 9.00%; TP1 reward/risk 1.00R is below strategy minimum 1.35R

**Risk flags:** OK

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## PYFA — position_xgb — NO_TRADE

**Score:** 0.578 vs policy min 0.55 · **Close:** 194 · **ATR14:** 23.9 · **Volume ratio 20D:** 0.66 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 183–197, entry trigger **197**, stop **179**, risk 18 points (9.14%).

**Targets:** TP1 **216** (1.06R), TP2 **228** (1.72R), TP3 **242** (2.50R). Recommended base-case RR: **1.72R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 194: zone 183–197 uses ATR14 23.9 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 197 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 179 is capped by max risk 9.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 216 (1.06R), TP2 228 (1.72R), TP3 242 (2.50R). Targets are ATR/structure capped for hold_days=1. ATR14=23.9, resistance_5/10/20/60=208/242/422/446. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 9.14% exceeds max strategy risk 9.00%; TP1 reward/risk 1.06R is below strategy minimum 1.35R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## SOCI — position_xgb — NO_TRADE

**Score:** 0.577 vs policy min 0.55 · **Close:** 322 · **ATR14:** 39.6 · **Volume ratio 20D:** 1.35 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 304–326, entry trigger **326**, stop **296**, risk 30 points (9.20%).

**Targets:** TP1 **356** (1.00R), TP2 **378** (1.73R), TP3 **398** (2.40R). Recommended base-case RR: **1.73R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 322: zone 304–326 uses ATR14 39.6 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 326 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 296 is capped by max risk 9.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 356 (1.00R), TP2 378 (1.73R), TP3 398 (2.40R). Targets are ATR/structure capped for hold_days=1. ATR14=39.6, resistance_5/10/20/60=348/416/480/700. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 9.20% exceeds max strategy risk 9.00%; TP1 reward/risk 1.00R is below strategy minimum 1.35R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## KIJA — position_xgb — NO_TRADE

**Score:** 0.577 vs policy min 0.55 · **Close:** 116 · **ATR14:** 9.4 · **Volume ratio 20D:** 0.75 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 111–117, entry trigger **117**, stop **106**, risk 11 points (9.40%).

**Targets:** TP1 **128** (1.00R), TP2 **136** (1.73R), TP3 **144** (2.45R). Recommended base-case RR: **1.73R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 116: zone 111–117 uses ATR14 9.4 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 117 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 106 is capped by max risk 9.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 128 (1.00R), TP2 136 (1.73R), TP3 144 (2.45R). Targets are ATR/structure capped for hold_days=1. ATR14=9.4, resistance_5/10/20/60=117/125/181/220. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 9.40% exceeds max strategy risk 9.00%; TP1 reward/risk 1.00R is below strategy minimum 1.35R

**Risk flags:** OK

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## OMED — position_xgb — NO_TRADE

**Score:** 0.576 vs policy min 0.55 · **Close:** 196 · **ATR14:** 17.3 · **Volume ratio 20D:** 1.40 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 188–198, entry trigger **198**, stop **180**, risk 18 points (9.09%).

**Targets:** TP1 **216** (1.00R), TP2 **230** (1.78R), TP3 **242** (2.44R). Recommended base-case RR: **1.78R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 196: zone 188–198 uses ATR14 17.3 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 198 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 180 is capped by max risk 9.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 216 (1.00R), TP2 230 (1.78R), TP3 242 (2.44R). Targets are ATR/structure capped for hold_days=1. ATR14=17.3, resistance_5/10/20/60=206/240/310/318. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 9.09% exceeds max strategy risk 9.00%; TP1 reward/risk 1.00R is below strategy minimum 1.35R

**Risk flags:** OK

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## NIKL — position_xgb — NO_TRADE

**Score:** 0.572 vs policy min 0.55 · **Close:** 192 · **ATR14:** 27.1 · **Volume ratio 20D:** 0.60 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 179–195, entry trigger **195**, stop **177**, risk 18 points (9.23%).

**Targets:** TP1 **234** (2.17R), TP2 **240** (2.50R), TP3 **250** (3.06R). Recommended base-case RR: **2.50R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 192: zone 179–195 uses ATR14 27.1 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 195 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 177 is capped by max risk 9.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 234 (2.17R), TP2 240 (2.50R), TP3 250 (3.06R). Targets are ATR/structure capped for hold_days=1. ATR14=27.1, resistance_5/10/20/60=240/260/370/510. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 9.23% exceeds max strategy risk 9.00%; volume ratio 0.60 below required 0.60

**Risk flags:** OK

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## GTSI — position_xgb — NO_TRADE

**Score:** 0.570 vs policy min 0.55 · **Close:** 134 · **ATR14:** 18.9 · **Volume ratio 20D:** 1.26 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 125–136, entry trigger **136**, stop **123**, risk 13 points (9.56%).

**Targets:** TP1 **163** (2.08R), TP2 **164** (2.15R), TP3 **168** (2.46R). Recommended base-case RR: **2.15R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 134: zone 125–136 uses ATR14 18.9 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 136 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 123 is capped by max risk 9.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 163 (2.08R), TP2 164 (2.15R), TP3 168 (2.46R). Targets are ATR/structure capped for hold_days=1. ATR14=18.9, resistance_5/10/20/60=139/164/222/294. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 9.56% exceeds max strategy risk 9.00%; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## IRSX — position_xgb — NO_TRADE

**Score:** 0.568 vs policy min 0.55 · **Close:** 294 · **ATR14:** 45.6 · **Volume ratio 20D:** 0.89 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 272–300, entry trigger **300**, stop **272**, risk 28 points (9.33%).

**Targets:** TP1 **328** (1.00R), TP2 **348** (1.71R), TP3 **368** (2.43R). Recommended base-case RR: **1.71R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 294: zone 272–300 uses ATR14 45.6 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 300 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 272 is capped by max risk 9.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 328 (1.00R), TP2 348 (1.71R), TP3 368 (2.43R). Targets are ATR/structure capped for hold_days=1. ATR14=45.6, resistance_5/10/20/60=326/386/480/540. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 9.33% exceeds max strategy risk 9.00%; TP1 reward/risk 1.00R is below strategy minimum 1.35R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## PSDN — market_maker_silent_accum_defensive — NO_TRADE

**Score:** 0.565 vs policy min 0.55 · **Close:** 115 · **ATR14:** 16.7 · **Volume ratio 20D:** 1.48 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 109–119, entry trigger **119**, stop **110**, risk 9 points (7.56%).

**Targets:** TP1 **128** (1.00R), TP2 **135** (1.78R), TP3 **141** (2.44R). Recommended base-case RR: **1.78R**.

**Why entry:** Hybrid entry uses close 115 and ATR14 16.7: buy zone 109–119. Entry is valid only if price can trade/hold around 119 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 110 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 128 (1.00R), TP2 135 (1.78R), TP3 141 (2.44R). Targets are ATR/structure capped for hold_days=1. ATR14=16.7, resistance_5/10/20/60=127/134/178/260. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.56% exceeds max strategy risk 7.50%; TP1 reward/risk 1.00R is below strategy minimum 1.25R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Defensive accumulation. Prefer retest and clean broker flow.

---

## KIJA — scalping_rank_hgb — NO_TRADE

**Score:** 0.561 vs policy min 0.60 · **Close:** 116 · **ATR14:** 9.4 · **Volume ratio 20D:** 0.75 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 114–118, entry trigger **118**, stop **112**, risk 6 points (5.08%).

**Targets:** TP1 **125** (1.17R), TP2 **129** (1.83R), TP3 **133** (2.50R). Recommended base-case RR: **1.83R**.

**Why entry:** Entry trigger 118 is set above recent resistance 117 plus one IDX tick. This requires confirmation instead of buying blindly at close 116. Entry is valid only if price can trade/hold around 118 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 112 is capped by max risk 4.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 125 (1.17R), TP2 129 (1.83R), TP3 133 (2.50R). Targets are ATR/structure capped for hold_days=1. ATR14=9.4, resistance_5/10/20/60=117/125/181/220. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 5.08% exceeds max strategy risk 4.50%; score 0.561 below policy min_score 0.60

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Top-1 short-horizon scalp; invalidation must be quick.

---

## ESIP — market_maker_silent_accum_defensive — NO_TRADE

**Score:** 0.535 vs policy min 0.55 · **Close:** 113 · **ATR14:** 16.5 · **Volume ratio 20D:** 0.59 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 107–117, entry trigger **117**, stop **108**, risk 9 points (7.69%).

**Targets:** TP1 **126** (1.00R), TP2 **133** (1.78R), TP3 **139** (2.44R). Recommended base-case RR: **1.78R**.

**Why entry:** Hybrid entry uses close 113 and ATR14 16.5: buy zone 107–117. Entry is valid only if price can trade/hold around 117 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 108 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 126 (1.00R), TP2 133 (1.78R), TP3 139 (2.44R). Targets are ATR/structure capped for hold_days=1. ATR14=16.5, resistance_5/10/20/60=124/137/206/238. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.69% exceeds max strategy risk 7.50%; score 0.535 below policy min_score 0.55; TP1 reward/risk 1.00R is below strategy minimum 1.25R; volume ratio 0.59 below required 0.60; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Defensive accumulation. Prefer retest and clean broker flow.

---

## GULA — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.446 vs policy min 0.60 · **Close:** 575 · **ATR14:** 49.2 · **Volume ratio 20D:** 1.12 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 565–615, entry trigger **615**, stop **550**, risk 65 points (10.57%).

**Targets:** TP1 **680** (1.00R), TP2 **730** (1.77R), TP3 **775** (2.46R). Recommended base-case RR: **1.77R**.

**Why entry:** Entry trigger 615 is set above recent resistance 610 plus one IDX tick. This requires confirmation instead of buying blindly at close 575. Entry is valid only if price can trade/hold around 615 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 550 uses 1.30×ATR14 volatility cap. Thesis invalidates if the move reverses beyond normal volatility. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 680 (1.00R), TP2 730 (1.77R), TP3 775 (2.46R). Targets are ATR/structure capped for hold_days=2. ATR14=49.2, resistance_5/10/20/60=610/610/610/610. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 10.57% exceeds max strategy risk 10.00%; score 0.446 below policy min_score 0.60; TP1 reward/risk 1.00R is below strategy minimum 1.40R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## GPSO — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.416 vs policy min 0.60 · **Close:** 336 · **ATR14:** 31.0 · **Volume ratio 20D:** 2.32 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 328–525, entry trigger **525**, stop **484**, risk 41 points (7.81%).

**Targets:** TP1 **570** (1.10R), TP2 **595** (1.71R), TP3 **625** (2.44R). Recommended base-case RR: **1.71R**.

**Why entry:** Entry trigger 525 is set above recent resistance 520 plus one IDX tick. This requires confirmation instead of buying blindly at close 336. Entry is valid only if price can trade/hold around 525 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 484 uses 1.30×ATR14 volatility cap. Thesis invalidates if the move reverses beyond normal volatility. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 570 (1.10R), TP2 595 (1.71R), TP3 625 (2.44R). Targets are ATR/structure capped for hold_days=2. ATR14=31.0, resistance_5/10/20/60=380/520/520/520. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 56.25% > max 15.00%; score 0.416 below policy min_score 0.60; TP1 reward/risk 1.10R is below strategy minimum 1.40R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## SSMS — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.404 vs policy min 0.60 · **Close:** 745 · **ATR14:** 72.5 · **Volume ratio 20D:** 0.98 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 730–830, entry trigger **830**, stop **745**, risk 85 points (10.24%).

**Targets:** TP1 **915** (1.00R), TP2 **975** (1.71R), TP3 **1,035** (2.41R). Recommended base-case RR: **1.71R**.

**Why entry:** Entry trigger 830 is set above recent resistance 825 plus one IDX tick. This requires confirmation instead of buying blindly at close 745. Entry is valid only if price can trade/hold around 830 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 745 is capped by max risk 10.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 915 (1.00R), TP2 975 (1.71R), TP3 1,035 (2.41R). Targets are ATR/structure capped for hold_days=2. ATR14=72.5, resistance_5/10/20/60=775/825/1,430/1,500. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 10.24% exceeds max strategy risk 10.00%; score 0.404 below policy min_score 0.60; TP1 reward/risk 1.00R is below strategy minimum 1.40R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## ARCI — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.403 vs policy min 0.60 · **Close:** 975 · **ATR14:** 104.6 · **Volume ratio 20D:** 1.62 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 950–1,245, entry trigger **1,245**, stop **1,120**, risk 125 points (10.04%).

**Targets:** TP1 **1,440** (1.56R), TP2 **1,475** (1.84R), TP3 **1,545** (2.40R). Recommended base-case RR: **1.84R**.

**Why entry:** Entry trigger 1,245 is set above recent resistance 1,240 plus one IDX tick. This requires confirmation instead of buying blindly at close 975. Entry is valid only if price can trade/hold around 1,245 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 1,120 is capped by max risk 10.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,440 (1.56R), TP2 1,475 (1.84R), TP3 1,545 (2.40R). Targets are ATR/structure capped for hold_days=2. ATR14=104.6, resistance_5/10/20/60=1,015/1,240/1,475/1,840. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 27.69% > max 15.00%; entry-to-stop risk 10.04% exceeds max strategy risk 10.00%; score 0.403 below policy min_score 0.60

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## GULA — momentum_5d_hgb_defensive — NO_TRADE

**Score:** 0.400 vs policy min 0.55 · **Close:** 575 · **ATR14:** 49.2 · **Volume ratio 20D:** 1.12 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 565–615, entry trigger **615**, stop **570**, risk 45 points (7.32%).

**Targets:** TP1 **660** (1.00R), TP2 **695** (1.78R), TP3 **725** (2.44R). Recommended base-case RR: **1.78R**.

**Why entry:** Entry trigger 615 is set above recent resistance 610 plus one IDX tick. This requires confirmation instead of buying blindly at close 575. Entry is valid only if price can trade/hold around 615 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 570 is capped by max risk 7.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 660 (1.00R), TP2 695 (1.78R), TP3 725 (2.44R). Targets are ATR/structure capped for hold_days=1. ATR14=49.2, resistance_5/10/20/60=610/610/610/610. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.32% exceeds max strategy risk 7.00%; score 0.400 below policy min_score 0.55; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Selective high-liquidity 5D momentum sleeve.

---

## SUPA — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.395 vs policy min 0.60 · **Close:** 615 · **ATR14:** 62.9 · **Volume ratio 20D:** 1.06 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 600–885, entry trigger **885**, stop **800**, risk 85 points (9.60%).

**Targets:** TP1 **970** (1.00R), TP2 **1,030** (1.71R), TP3 **1,090** (2.41R). Recommended base-case RR: **1.71R**.

**Why entry:** Entry trigger 885 is set above recent resistance 880 plus one IDX tick. This requires confirmation instead of buying blindly at close 615. Entry is valid only if price can trade/hold around 885 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 800 uses 1.30×ATR14 volatility cap. Thesis invalidates if the move reverses beyond normal volatility. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 970 (1.00R), TP2 1,030 (1.71R), TP3 1,090 (2.41R). Targets are ATR/structure capped for hold_days=2. ATR14=62.9, resistance_5/10/20/60=675/880/905/970. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 43.90% > max 15.00%; score 0.395 below policy min_score 0.60; TP1 reward/risk 1.00R is below strategy minimum 1.40R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## GPSO — momentum_5d_hgb_defensive — NO_TRADE

**Score:** 0.392 vs policy min 0.55 · **Close:** 336 · **ATR14:** 31.0 · **Volume ratio 20D:** 2.32 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 328–525, entry trigger **525**, stop **488**, risk 37 points (7.05%).

**Targets:** TP1 **560** (0.95R), TP2 **580** (1.49R), TP3 **610** (2.30R). Recommended base-case RR: **1.49R**.

**Why entry:** Entry trigger 525 is set above recent resistance 520 plus one IDX tick. This requires confirmation instead of buying blindly at close 336. Entry is valid only if price can trade/hold around 525 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 488 uses 1.15×ATR14 volatility cap. Thesis invalidates if the move reverses beyond normal volatility. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 560 (0.95R), TP2 580 (1.49R), TP3 610 (2.30R). Targets are ATR/structure capped for hold_days=1. ATR14=31.0, resistance_5/10/20/60=380/520/520/520. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 56.25% > max 8.00%; entry-to-stop risk 7.05% exceeds max strategy risk 7.00%; score 0.392 below policy min_score 0.55; TP1 reward/risk 0.95R is below strategy minimum 1.25R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Selective high-liquidity 5D momentum sleeve.

---

## RGAS — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.386 vs policy min 0.60 · **Close:** 149 · **ATR14:** 14.9 · **Volume ratio 20D:** 3.53 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 146–173, entry trigger **173**, stop **155**, risk 18 points (10.40%).

**Targets:** TP1 **191** (1.00R), TP2 **204** (1.72R), TP3 **218** (2.50R). Recommended base-case RR: **1.72R**.

**Why entry:** Entry trigger 173 is set above recent resistance 172 plus one IDX tick. This requires confirmation instead of buying blindly at close 149. Entry is valid only if price can trade/hold around 173 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 155 is capped by max risk 10.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 191 (1.00R), TP2 204 (1.72R), TP3 218 (2.50R). Targets are ATR/structure capped for hold_days=2. ATR14=14.9, resistance_5/10/20/60=172/172/172/172. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 16.11% > max 15.00%; entry-to-stop risk 10.40% exceeds max strategy risk 10.00%; score 0.386 below policy min_score 0.60; TP1 reward/risk 1.00R is below strategy minimum 1.40R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## OASA — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.386 vs policy min 0.60 · **Close:** 260 · **ATR14:** 38.3 · **Volume ratio 20D:** 0.67 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 252–374, entry trigger **374**, stop **336**, risk 38 points (10.16%).

**Targets:** TP1 **432** (1.53R), TP2 **440** (1.74R), TP3 **466** (2.42R). Recommended base-case RR: **1.74R**.

**Why entry:** Entry trigger 374 is set above recent resistance 372 plus one IDX tick. This requires confirmation instead of buying blindly at close 260. Entry is valid only if price can trade/hold around 374 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 336 is capped by max risk 10.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 432 (1.53R), TP2 440 (1.74R), TP3 466 (2.42R). Targets are ATR/structure capped for hold_days=2. ATR14=38.3, resistance_5/10/20/60=268/372/432/466. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 43.85% > max 15.00%; entry-to-stop risk 10.16% exceeds max strategy risk 10.00%; score 0.386 below policy min_score 0.60; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## COCO — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.386 vs policy min 0.60 · **Close:** 194 · **ATR14:** 33.6 · **Volume ratio 20D:** 1.25 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 187–268, entry trigger **268**, stop **240**, risk 28 points (10.45%).

**Targets:** TP1 **296** (1.00R), TP2 **364** (3.43R), TP3 **378** (3.93R). Recommended base-case RR: **3.43R**.

**Why entry:** Entry trigger 268 is set above recent resistance 266 plus one IDX tick. This requires confirmation instead of buying blindly at close 194. Entry is valid only if price can trade/hold around 268 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 240 is capped by max risk 10.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 296 (1.00R), TP2 364 (3.43R), TP3 378 (3.93R). Targets are ATR/structure capped for hold_days=2. ATR14=33.6, resistance_5/10/20/60=218/266/364/570. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 38.14% > max 15.00%; entry-to-stop risk 10.45% exceeds max strategy risk 10.00%; score 0.386 below policy min_score 0.60; TP1 reward/risk 1.00R is below strategy minimum 1.40R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## NIKL — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.373 vs policy min 0.60 · **Close:** 192 · **ATR14:** 27.1 · **Volume ratio 20D:** 0.60 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 186–262, entry trigger **262**, stop **234**, risk 28 points (10.69%).

**Targets:** TP1 **290** (1.00R), TP2 **310** (1.71R), TP3 **370** (3.86R). Recommended base-case RR: **1.71R**.

**Why entry:** Entry trigger 262 is set above recent resistance 260 plus one IDX tick. This requires confirmation instead of buying blindly at close 192. Entry is valid only if price can trade/hold around 262 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 234 is capped by max risk 10.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 290 (1.00R), TP2 310 (1.71R), TP3 370 (3.86R). Targets are ATR/structure capped for hold_days=2. ATR14=27.1, resistance_5/10/20/60=240/260/370/510. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 36.46% > max 15.00%; entry-to-stop risk 10.69% exceeds max strategy risk 10.00%; score 0.373 below policy min_score 0.60; TP1 reward/risk 1.00R is below strategy minimum 1.40R; volume ratio 0.60 below required 0.60

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## GTSI — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.367 vs policy min 0.60 · **Close:** 134 · **ATR14:** 18.9 · **Volume ratio 20D:** 1.26 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 130–165, entry trigger **165**, stop **148**, risk 17 points (10.30%).

**Targets:** TP1 **182** (1.00R), TP2 **222** (3.35R), TP3 **232** (3.94R). Recommended base-case RR: **3.35R**.

**Why entry:** Entry trigger 165 is set above recent resistance 164 plus one IDX tick. This requires confirmation instead of buying blindly at close 134. Entry is valid only if price can trade/hold around 165 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 148 is capped by max risk 10.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 182 (1.00R), TP2 222 (3.35R), TP3 232 (3.94R). Targets are ATR/structure capped for hold_days=2. ATR14=18.9, resistance_5/10/20/60=139/164/222/294. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 23.13% > max 15.00%; entry-to-stop risk 10.30% exceeds max strategy risk 10.00%; score 0.367 below policy min_score 0.60; TP1 reward/risk 1.00R is below strategy minimum 1.40R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## PYFA — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.366 vs policy min 0.60 · **Close:** 194 · **ATR14:** 23.9 · **Volume ratio 20D:** 0.66 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 189–244, entry trigger **244**, stop **218**, risk 26 points (10.66%).

**Targets:** TP1 **270** (1.00R), TP2 **290** (1.77R), TP3 **308** (2.46R). Recommended base-case RR: **1.77R**.

**Why entry:** Entry trigger 244 is set above recent resistance 242 plus one IDX tick. This requires confirmation instead of buying blindly at close 194. Entry is valid only if price can trade/hold around 244 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 218 is capped by max risk 10.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 270 (1.00R), TP2 290 (1.77R), TP3 308 (2.46R). Targets are ATR/structure capped for hold_days=2. ATR14=23.9, resistance_5/10/20/60=208/242/422/446. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 25.77% > max 15.00%; entry-to-stop risk 10.66% exceeds max strategy risk 10.00%; score 0.366 below policy min_score 0.60; TP1 reward/risk 1.00R is below strategy minimum 1.40R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## BNBR — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.359 vs policy min 0.60 · **Close:** 110 · **ATR14:** 17.4 · **Volume ratio 20D:** 1.33 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 106–144, entry trigger **144**, stop **129**, risk 15 points (10.42%).

**Targets:** TP1 **159** (1.00R), TP2 **186** (2.80R), TP3 **194** (3.33R). Recommended base-case RR: **2.80R**.

**Why entry:** Entry trigger 144 is set above recent resistance 143 plus one IDX tick. This requires confirmation instead of buying blindly at close 110. Entry is valid only if price can trade/hold around 144 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 129 is capped by max risk 10.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 159 (1.00R), TP2 186 (2.80R), TP3 194 (3.33R). Targets are ATR/structure capped for hold_days=2. ATR14=17.4, resistance_5/10/20/60=115/143/186/240. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 30.91% > max 15.00%; entry-to-stop risk 10.42% exceeds max strategy risk 10.00%; score 0.359 below policy min_score 0.60; TP1 reward/risk 1.00R is below strategy minimum 1.40R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## ESSA — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.359 vs policy min 0.60 · **Close:** 600 · **ATR14:** 51.4 · **Volume ratio 20D:** 1.17 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 585–715, entry trigger **715**, stop **645**, risk 70 points (9.79%).

**Targets:** TP1 **810** (1.36R), TP2 **845** (1.86R), TP3 **885** (2.43R). Recommended base-case RR: **1.86R**.

**Why entry:** Entry trigger 715 is set above recent resistance 710 plus one IDX tick. This requires confirmation instead of buying blindly at close 600. Entry is valid only if price can trade/hold around 715 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 645 uses 1.30×ATR14 volatility cap. Thesis invalidates if the move reverses beyond normal volatility. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 810 (1.36R), TP2 845 (1.86R), TP3 885 (2.43R). Targets are ATR/structure capped for hold_days=2. ATR14=51.4, resistance_5/10/20/60=635/710/845/995. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 19.17% > max 15.00%; score 0.359 below policy min_score 0.60; TP1 reward/risk 1.36R is below strategy minimum 1.40R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## ASPR — ara_candidate — NO_TRADE

**Score:** 0.233 vs policy min 0.50 · **Close:** 216 · **ATR14:** 42.6 · **Volume ratio 20D:** 1.68 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 206–226, entry trigger **226**, stop **202**, risk 24 points (10.62%).

**Targets:** TP1 **250** (1.00R), TP2 **268** (1.75R), TP3 **284** (2.42R). Recommended base-case RR: **1.75R**.

**Why entry:** Entry trigger 226 is set above recent resistance 224 plus one IDX tick. This requires confirmation instead of buying blindly at close 216. Entry is valid only if price can trade/hold around 226 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 202 is capped by max risk 10.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 250 (1.00R), TP2 268 (1.75R), TP3 284 (2.42R). Targets are ATR/structure capped for hold_days=1. ATR14=42.6, resistance_5/10/20/60=218/224/540/620. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 10.62% exceeds max strategy risk 10.00%; score 0.233 below policy min_score 0.50; TP1 reward/risk 1.00R is below strategy minimum 1.30R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** High drawdown tactical setup. Use as execution only if confirmation is strong and liquidity is clean.

---
