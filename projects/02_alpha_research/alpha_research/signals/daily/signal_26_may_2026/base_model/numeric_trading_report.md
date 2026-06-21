# Numeric Trading Desk Report — 2026-05-25

This report is generated from live model scores, selected signal policy, canonical OHLCV, ATR, support/resistance, liquidity, and broker-flow diagnostics. It is not a simple BUY/SELL list; each plan is conditional on execution behaviour.

## Summary

| Plan quality | Count |
|---|---:|
| ACTIONABLE | 2 |
| CONDITIONAL | 5 |
| WATCHLIST_ONLY | 7 |
| NO_TRADE | 42 |

## TMPO — position_xgb — ACTIONABLE

**Score:** 0.583 vs policy min 0.55 · **Close:** 108 · **ATR14:** 10.9 · **Volume ratio 20D:** 2.32 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 103–110, entry trigger **110**, stop **102**, risk 8 points (7.27%).

**Targets:** TP1 **126** (2.00R), TP2 **130** (2.50R), TP3 **134** (3.00R). Recommended base-case RR: **2.50R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 108: zone 103–110 uses ATR14 10.9 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 110 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 102 is placed below support structure (103 / 103). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 126 (2.00R), TP2 130 (2.50R), TP3 134 (3.00R). Targets are ATR/structure capped for hold_days=1. ATR14=10.9, resistance_5/10/20/60=130/135/152/168. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## SSMS — position_xgb — ACTIONABLE

**Score:** 0.582 vs policy min 0.55 · **Close:** 775 · **ATR14:** 85.0 · **Volume ratio 20D:** 1.88 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 735–785, entry trigger **785**, stop **765**, risk 20 points (2.55%).

**Targets:** TP1 **830** (2.25R), TP2 **840** (2.75R), TP3 **1,105** (16.00R). Recommended base-case RR: **2.75R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 775: zone 735–785 uses ATR14 85.0 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 785 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 765 is placed below support structure (770 / 770). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 830 (2.25R), TP2 840 (2.75R), TP3 1,105 (16.00R). Targets are ATR/structure capped for hold_days=1. ATR14=85.0, resistance_5/10/20/60=1,105/1,445/1,470/1,800. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## BFIN — swing_hgb_defensive — CONDITIONAL

**Score:** 0.668 vs policy min 0.50 · **Close:** 720 · **ATR14:** 43.6 · **Volume ratio 20D:** 1.02 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 700–725, entry trigger **725**, stop **685**, risk 40 points (5.52%).

**Targets:** TP1 **765** (1.00R), TP2 **805** (2.00R), TP3 **825** (2.50R). Recommended base-case RR: **2.00R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 720: zone 700–725 uses ATR14 43.6 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 725 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 685 is placed below support structure (690 / 690). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 765 (1.00R), TP2 805 (2.00R), TP3 825 (2.50R). Targets are ATR/structure capped for hold_days=1. ATR14=43.6, resistance_5/10/20/60=820/825/965/965. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## KIJA — swing_hgb_defensive — CONDITIONAL

**Score:** 0.657 vs policy min 0.50 · **Close:** 124 · **ATR14:** 10.2 · **Volume ratio 20D:** 1.68 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 119–126, entry trigger **126**, stop **118**, risk 8 points (6.35%).

**Targets:** TP1 **134** (1.00R), TP2 **140** (1.75R), TP3 **146** (2.50R). Recommended base-case RR: **1.75R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 124: zone 119–126 uses ATR14 10.2 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 126 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 118 is placed below support structure (119 / 119). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 134 (1.00R), TP2 140 (1.75R), TP3 146 (2.50R). Targets are ATR/structure capped for hold_days=1. ATR14=10.2, resistance_5/10/20/60=172/183/220/240. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## MOLI — swing_hgb_defensive — CONDITIONAL

**Score:** 0.655 vs policy min 0.50 · **Close:** 220 · **ATR14:** 23.4 · **Volume ratio 20D:** 0.80 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 208–224, entry trigger **224**, stop **212**, risk 12 points (5.36%).

**Targets:** TP1 **236** (1.00R), TP2 **268** (3.67R), TP3 **274** (4.17R). Recommended base-case RR: **3.67R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 220: zone 208–224 uses ATR14 23.4 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 224 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 212 is placed below support structure (214 / 214). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 236 (1.00R), TP2 268 (3.67R), TP3 274 (4.17R). Targets are ATR/structure capped for hold_days=1. ATR14=23.4, resistance_5/10/20/60=268/318/318/318. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.25R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## TRIN — swing_hgb_defensive — CONDITIONAL

**Score:** 0.650 vs policy min 0.50 · **Close:** 472 · **ATR14:** 66.6 · **Volume ratio 20D:** 0.61 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 442–480, entry trigger **480**, stop **448**, risk 32 points (6.67%).

**Targets:** TP1 **515** (1.09R), TP2 **600** (3.75R), TP3 **620** (4.38R). Recommended base-case RR: **3.75R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 472: zone 442–480 uses ATR14 66.6 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 480 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 448 is placed below support structure (450 / 450). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 515 (1.09R), TP2 600 (3.75R), TP3 620 (4.38R). Targets are ATR/structure capped for hold_days=1. ATR14=66.6, resistance_5/10/20/60=600/715/860/1,225. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.09R is below strategy minimum 1.25R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## KIJA — position_xgb — CONDITIONAL

**Score:** 0.580 vs policy min 0.55 · **Close:** 124 · **ATR14:** 10.2 · **Volume ratio 20D:** 1.68 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 119–126, entry trigger **126**, stop **118**, risk 8 points (6.35%).

**Targets:** TP1 **134** (1.00R), TP2 **140** (1.75R), TP3 **165** (4.88R). Recommended base-case RR: **1.75R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 124: zone 119–126 uses ATR14 10.2 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 126 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 118 is placed below support structure (119 / 119). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 134 (1.00R), TP2 140 (1.75R), TP3 165 (4.88R). Targets are ATR/structure capped for hold_days=1. ATR14=10.2, resistance_5/10/20/60=172/183/220/240. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.35R

**Risk flags:** OK

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## SSMS — market_maker_silent_accum_defensive — WATCHLIST_ONLY

**Score:** 0.462 vs policy min 0.55 · **Close:** 775 · **ATR14:** 85.0 · **Volume ratio 20D:** 1.88 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 745–795, entry trigger **795**, stop **765**, risk 30 points (3.77%).

**Targets:** TP1 **840** (1.50R), TP2 **850** (1.83R), TP3 **870** (2.50R). Recommended base-case RR: **1.83R**.

**Why entry:** Hybrid entry uses close 775 and ATR14 85.0: buy zone 745–795. Entry is valid only if price can trade/hold around 795 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 765 is placed below support structure (770 / 770). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 840 (1.50R), TP2 850 (1.83R), TP3 870 (2.50R). Targets are ATR/structure capped for hold_days=1. ATR14=85.0, resistance_5/10/20/60=1,105/1,445/1,470/1,800. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** score 0.462 below policy min_score 0.55

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Defensive accumulation. Prefer retest and clean broker flow.

---

## MSIN — market_maker_silent_accum_defensive — WATCHLIST_ONLY

**Score:** 0.461 vs policy min 0.55 · **Close:** 494 · **ATR14:** 79.4 · **Volume ratio 20D:** 1.26 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 466–510, entry trigger **510**, stop **474**, risk 36 points (7.06%).

**Targets:** TP1 **550** (1.11R), TP2 **655** (4.03R), TP3 **680** (4.72R). Recommended base-case RR: **4.03R**.

**Why entry:** Hybrid entry uses close 494 and ATR14 79.4: buy zone 466–510. Entry is valid only if price can trade/hold around 510 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 474 is placed below support structure (480 / 480). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 550 (1.11R), TP2 655 (4.03R), TP3 680 (4.72R). Targets are ATR/structure capped for hold_days=1. ATR14=79.4, resistance_5/10/20/60=680/835/985/1,450. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** score 0.461 below policy min_score 0.55; TP1 reward/risk 1.11R is below strategy minimum 1.25R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Defensive accumulation. Prefer retest and clean broker flow.

---

## FUJI — market_maker_silent_accum_defensive — WATCHLIST_ONLY

**Score:** 0.455 vs policy min 0.55 · **Close:** 280 · **ATR14:** 21.1 · **Volume ratio 20D:** 2.06 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 272–286, entry trigger **286**, stop **268**, risk 18 points (6.29%).

**Targets:** TP1 **308** (1.22R), TP2 **318** (1.78R), TP3 **330** (2.44R). Recommended base-case RR: **1.78R**.

**Why entry:** Hybrid entry uses close 280 and ATR14 21.1: buy zone 272–286. Entry is valid only if price can trade/hold around 286 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 268 is placed below support structure (270 / 270). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 308 (1.22R), TP2 318 (1.78R), TP3 330 (2.44R). Targets are ATR/structure capped for hold_days=1. ATR14=21.1, resistance_5/10/20/60=316/336/404/525. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** score 0.455 below policy min_score 0.55; TP1 reward/risk 1.22R is below strategy minimum 1.25R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Defensive accumulation. Prefer retest and clean broker flow.

---

## UVCR — momentum_10d_hgb_aggressive — WATCHLIST_ONLY

**Score:** 0.431 vs policy min 0.60 · **Close:** 234 · **ATR14:** 13.1 · **Volume ratio 20D:** 0.98 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 230–242, entry trigger **242**, stop **224**, risk 18 points (7.44%).

**Targets:** TP1 **260** (1.00R), TP2 **274** (1.78R), TP3 **286** (2.44R). Recommended base-case RR: **1.78R**.

**Why entry:** Entry trigger 242 is set above recent resistance 240 plus one IDX tick. This requires confirmation instead of buying blindly at close 234. Entry is valid only if price can trade/hold around 242 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 224 uses 1.30×ATR14 volatility cap. Thesis invalidates if the move reverses beyond normal volatility. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 260 (1.00R), TP2 274 (1.78R), TP3 286 (2.44R). Targets are ATR/structure capped for hold_days=2. ATR14=13.1, resistance_5/10/20/60=240/240/240/240. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** score 0.431 below policy min_score 0.60; TP1 reward/risk 1.00R is below strategy minimum 1.40R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## BKDP — momentum_10d_hgb_aggressive — WATCHLIST_ONLY

**Score:** 0.424 vs policy min 0.60 · **Close:** 114 · **ATR14:** 12.9 · **Volume ratio 20D:** 1.81 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 111–120, entry trigger **120**, stop **108**, risk 12 points (10.00%).

**Targets:** TP1 **132** (1.00R), TP2 **141** (1.75R), TP3 **149** (2.42R). Recommended base-case RR: **1.75R**.

**Why entry:** Entry trigger 120 is set above recent resistance 119 plus one IDX tick. This requires confirmation instead of buying blindly at close 114. Entry is valid only if price can trade/hold around 120 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 108 is capped by max risk 10.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 132 (1.00R), TP2 141 (1.75R), TP3 149 (2.42R). Targets are ATR/structure capped for hold_days=2. ATR14=12.9, resistance_5/10/20/60=119/119/119/119. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** score 0.424 below policy min_score 0.60; TP1 reward/risk 1.00R is below strategy minimum 1.40R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## GULA — momentum_10d_hgb_aggressive — WATCHLIST_ONLY

**Score:** 0.424 vs policy min 0.60 · **Close:** 458 · **ATR14:** 25.0 · **Volume ratio 20D:** 2.71 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 452–460, entry trigger **460**, stop **426**, risk 34 points (7.39%).

**Targets:** TP1 **494** (1.00R), TP2 **520** (1.76R), TP3 **545** (2.50R). Recommended base-case RR: **1.76R**.

**Why entry:** Entry trigger 460 is set above recent resistance 458 plus one IDX tick. This requires confirmation instead of buying blindly at close 458. Entry is valid only if price can trade/hold around 460 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 426 uses 1.30×ATR14 volatility cap. Thesis invalidates if the move reverses beyond normal volatility. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 494 (1.00R), TP2 520 (1.76R), TP3 545 (2.50R). Targets are ATR/structure capped for hold_days=2. ATR14=25.0, resistance_5/10/20/60=458/458/458/458. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** score 0.424 below policy min_score 0.60; TP1 reward/risk 1.00R is below strategy minimum 1.40R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## GPSO — momentum_10d_hgb_aggressive — WATCHLIST_ONLY

**Score:** 0.416 vs policy min 0.60 · **Close:** 490 · **ATR14:** 28.9 · **Volume ratio 20D:** 2.17 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 484–505, entry trigger **505**, stop **466**, risk 39 points (7.72%).

**Targets:** TP1 **545** (1.03R), TP2 **575** (1.79R), TP3 **600** (2.44R). Recommended base-case RR: **1.79R**.

**Why entry:** Entry trigger 505 is set above recent resistance 500 plus one IDX tick. This requires confirmation instead of buying blindly at close 490. Entry is valid only if price can trade/hold around 505 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 466 uses 1.30×ATR14 volatility cap. Thesis invalidates if the move reverses beyond normal volatility. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 545 (1.03R), TP2 575 (1.79R), TP3 600 (2.44R). Targets are ATR/structure capped for hold_days=2. ATR14=28.9, resistance_5/10/20/60=500/500/500/535. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** score 0.416 below policy min_score 0.60; TP1 reward/risk 1.03R is below strategy minimum 1.40R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## MSJA — swing_hgb_defensive — NO_TRADE

**Score:** 0.674 vs policy min 0.50 · **Close:** 420 · **ATR14:** 41.7 · **Volume ratio 20D:** 1.35 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 400–426, entry trigger **426**, stop **394**, risk 32 points (7.51%).

**Targets:** TP1 **458** (1.00R), TP2 **482** (1.75R), TP3 **505** (2.47R). Recommended base-case RR: **1.75R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 420: zone 400–426 uses ATR14 41.7 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 426 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 394 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 458 (1.00R), TP2 482 (1.75R), TP3 505 (2.47R). Targets are ATR/structure capped for hold_days=1. ATR14=41.7, resistance_5/10/20/60=448/555/555/560. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.51% exceeds max strategy risk 7.50%; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## NCKL — swing_hgb_defensive — NO_TRADE

**Score:** 0.667 vs policy min 0.50 · **Close:** 875 · **ATR14:** 64.3 · **Volume ratio 20D:** 1.20 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 845–885, entry trigger **885**, stop **815**, risk 70 points (7.91%).

**Targets:** TP1 **950** (0.93R), TP2 **1,005** (1.71R), TP3 **1,055** (2.43R). Recommended base-case RR: **1.71R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 875: zone 845–885 uses ATR14 64.3 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 885 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 815 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 950 (0.93R), TP2 1,005 (1.71R), TP3 1,055 (2.43R). Targets are ATR/structure capped for hold_days=1. ATR14=64.3, resistance_5/10/20/60=1,000/1,070/1,245/1,595. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.91% exceeds max strategy risk 7.50%; TP1 reward/risk 0.93R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## BANK — swing_hgb_defensive — NO_TRADE

**Score:** 0.663 vs policy min 0.50 · **Close:** 284 · **ATR14:** 59.9 · **Volume ratio 20D:** 17.90 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 260–290, entry trigger **290**, stop **268**, risk 22 points (7.59%).

**Targets:** TP1 **320** (1.36R), TP2 **328** (1.73R), TP3 **430** (6.36R). Recommended base-case RR: **1.73R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 284: zone 260–290 uses ATR14 59.9 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 290 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 268 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 320 (1.36R), TP2 328 (1.73R), TP3 430 (6.36R). Targets are ATR/structure capped for hold_days=1. ATR14=59.9, resistance_5/10/20/60=430/640/640/655. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.59% exceeds max strategy risk 7.50%

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## SMBR — swing_hgb_defensive — NO_TRADE

**Score:** 0.659 vs policy min 0.50 · **Close:** 171 · **ATR14:** 11.4 · **Volume ratio 20D:** 0.51 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 165–173, entry trigger **173**, stop **160**, risk 13 points (7.51%).

**Targets:** TP1 **185** (0.92R), TP2 **194** (1.62R), TP3 **206** (2.54R). Recommended base-case RR: **1.62R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 171: zone 165–173 uses ATR14 11.4 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 173 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 160 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 185 (0.92R), TP2 194 (1.62R), TP3 206 (2.54R). Targets are ATR/structure capped for hold_days=1. ATR14=11.4, resistance_5/10/20/60=191/218/242/298. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.51% exceeds max strategy risk 7.50%; TP1 reward/risk 0.92R is below strategy minimum 1.25R; volume ratio 0.51 below required 0.60

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## SIMP — swing_hgb_defensive — NO_TRADE

**Score:** 0.658 vs policy min 0.50 · **Close:** 565 · **ATR14:** 48.9 · **Volume ratio 20D:** 0.51 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 540–570, entry trigger **570**, stop **525**, risk 45 points (7.89%).

**Targets:** TP1 **620** (1.11R), TP2 **650** (1.78R), TP3 **680** (2.44R). Recommended base-case RR: **1.78R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 565: zone 540–570 uses ATR14 48.9 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 570 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 525 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 620 (1.11R), TP2 650 (1.78R), TP3 680 (2.44R). Targets are ATR/structure capped for hold_days=1. ATR14=48.9, resistance_5/10/20/60=630/770/920/930. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.89% exceeds max strategy risk 7.50%; TP1 reward/risk 1.11R is below strategy minimum 1.25R; volume ratio 0.51 below required 0.60

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## FPNI — swing_hgb_defensive — NO_TRADE

**Score:** 0.657 vs policy min 0.50 · **Close:** 368 · **ATR14:** 40.6 · **Volume ratio 20D:** 0.96 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 348–374, entry trigger **374**, stop **344**, risk 30 points (8.02%).

**Targets:** TP1 **410** (1.20R), TP2 **426** (1.73R), TP3 **446** (2.40R). Recommended base-case RR: **1.73R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 368: zone 348–374 uses ATR14 40.6 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 374 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 344 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 410 (1.20R), TP2 426 (1.73R), TP3 446 (2.40R). Targets are ATR/structure capped for hold_days=1. ATR14=40.6, resistance_5/10/20/60=410/510/580/800. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.02% exceeds max strategy risk 7.50%; TP1 reward/risk 1.20R is below strategy minimum 1.25R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## SOFA — swing_hgb_defensive — NO_TRADE

**Score:** 0.657 vs policy min 0.50 · **Close:** 370 · **ATR14:** 39.7 · **Volume ratio 20D:** 1.29 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 352–374, entry trigger **374**, stop **344**, risk 30 points (8.02%).

**Targets:** TP1 **404** (1.00R), TP2 **426** (1.73R), TP3 **446** (2.40R). Recommended base-case RR: **1.73R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 370: zone 352–374 uses ATR14 39.7 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 374 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 344 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 404 (1.00R), TP2 426 (1.73R), TP3 446 (2.40R). Targets are ATR/structure capped for hold_days=1. ATR14=39.7, resistance_5/10/20/60=386/420/520/630. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.02% exceeds max strategy risk 7.50%; TP1 reward/risk 1.00R is below strategy minimum 1.25R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## TOBA — swing_hgb_defensive — NO_TRADE

**Score:** 0.656 vs policy min 0.50 · **Close:** 446 · **ATR14:** 42.8 · **Volume ratio 20D:** 0.46 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 426–452, entry trigger **452**, stop **418**, risk 34 points (7.52%).

**Targets:** TP1 **486** (1.00R), TP2 **530** (2.29R), TP3 **535** (2.44R). Recommended base-case RR: **2.29R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 446: zone 426–452 uses ATR14 42.8 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 452 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 418 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 486 (1.00R), TP2 530 (2.29R), TP3 535 (2.44R). Targets are ATR/structure capped for hold_days=1. ATR14=42.8, resistance_5/10/20/60=530/650/695/815. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.52% exceeds max strategy risk 7.50%; TP1 reward/risk 1.00R is below strategy minimum 1.25R; volume ratio 0.46 below required 0.60

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## KOKA — swing_hgb_defensive — NO_TRADE

**Score:** 0.656 vs policy min 0.50 · **Close:** 120 · **ATR14:** 16.6 · **Volume ratio 20D:** 1.88 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 112–122, entry trigger **122**, stop **112**, risk 10 points (8.20%).

**Targets:** TP1 **132** (1.00R), TP2 **147** (2.50R), TP3 **152** (3.00R). Recommended base-case RR: **2.50R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 120: zone 112–122 uses ATR14 16.6 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 122 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 112 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 132 (1.00R), TP2 147 (2.50R), TP3 152 (3.00R). Targets are ATR/structure capped for hold_days=1. ATR14=16.6, resistance_5/10/20/60=147/184/226/318. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.20% exceeds max strategy risk 7.50%; TP1 reward/risk 1.00R is below strategy minimum 1.25R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## NSSS — swing_hgb_defensive — NO_TRADE

**Score:** 0.653 vs policy min 0.50 · **Close:** 490 · **ATR14:** 72.6 · **Volume ratio 20D:** 0.46 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 456–498, entry trigger **498**, stop **460**, risk 38 points (7.63%).

**Targets:** TP1 **540** (1.11R), TP2 **565** (1.76R), TP3 **680** (4.79R). Recommended base-case RR: **1.76R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 490: zone 456–498 uses ATR14 72.6 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 498 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 460 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 540 (1.11R), TP2 565 (1.76R), TP3 680 (4.79R). Targets are ATR/structure capped for hold_days=1. ATR14=72.6, resistance_5/10/20/60=700/850/1,060/1,300. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.63% exceeds max strategy risk 7.50%; TP1 reward/risk 1.11R is below strategy minimum 1.25R; volume ratio 0.46 below required 0.60

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## SOCI — swing_hgb_defensive — NO_TRADE

**Score:** 0.650 vs policy min 0.50 · **Close:** 378 · **ATR14:** 39.0 · **Volume ratio 20D:** 0.60 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 360–382, entry trigger **382**, stop **352**, risk 30 points (7.85%).

**Targets:** TP1 **422** (1.33R), TP2 **442** (2.00R), TP3 **454** (2.40R). Recommended base-case RR: **2.00R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 378: zone 360–382 uses ATR14 39.0 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 382 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 352 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 422 (1.33R), TP2 442 (2.00R), TP3 454 (2.40R). Targets are ATR/structure capped for hold_days=1. ATR14=39.0, resistance_5/10/20/60=442/540/565/780. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.85% exceeds max strategy risk 7.50%; volume ratio 0.60 below required 0.60; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## MIDI — scalping_rank_hgb — NO_TRADE

**Score:** 0.615 vs policy min 0.60 · **Close:** 294 · **ATR14:** 15.3 · **Volume ratio 20D:** 2.04 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 290–328, entry trigger **328**, stop **314**, risk 14 points (4.27%).

**Targets:** TP1 **340** (0.86R), TP2 **346** (1.29R), TP3 **362** (2.43R). Recommended base-case RR: **1.29R**.

**Why entry:** Entry trigger 328 is set above recent resistance 326 plus one IDX tick. This requires confirmation instead of buying blindly at close 294. Entry is valid only if price can trade/hold around 328 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 314 uses 0.90×ATR14 volatility cap. Thesis invalidates if the move reverses beyond normal volatility. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 340 (0.86R), TP2 346 (1.29R), TP3 362 (2.43R). Targets are ATR/structure capped for hold_days=1. ATR14=15.3, resistance_5/10/20/60=326/356/356/356. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 11.56% > max 5.00%; TP1 reward/risk 0.86R is below strategy minimum 1.10R

**Risk flags:** OK

**Strategy risk note:** Top-1 short-horizon scalp; invalidation must be quick.

---

## KOKA — position_xgb — NO_TRADE

**Score:** 0.585 vs policy min 0.55 · **Close:** 120 · **ATR14:** 16.6 · **Volume ratio 20D:** 1.88 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 112–122, entry trigger **122**, stop **111**, risk 11 points (9.02%).

**Targets:** TP1 **146** (2.18R), TP2 **147** (2.27R), TP3 **149** (2.45R). Recommended base-case RR: **2.27R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 120: zone 112–122 uses ATR14 16.6 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 122 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 111 is capped by max risk 9.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 146 (2.18R), TP2 147 (2.27R), TP3 149 (2.45R). Targets are ATR/structure capped for hold_days=1. ATR14=16.6, resistance_5/10/20/60=147/184/226/318. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 9.02% exceeds max strategy risk 9.00%; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## NCKL — position_xgb — NO_TRADE

**Score:** 0.585 vs policy min 0.55 · **Close:** 875 · **ATR14:** 64.3 · **Volume ratio 20D:** 1.20 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 845–885, entry trigger **885**, stop **805**, risk 80 points (9.04%).

**Targets:** TP1 **975** (1.12R), TP2 **1,025** (1.75R), TP3 **1,080** (2.44R). Recommended base-case RR: **1.75R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 875: zone 845–885 uses ATR14 64.3 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 885 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 805 is capped by max risk 9.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 975 (1.12R), TP2 1,025 (1.75R), TP3 1,080 (2.44R). Targets are ATR/structure capped for hold_days=1. ATR14=64.3, resistance_5/10/20/60=1,000/1,070/1,245/1,595. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 9.04% exceeds max strategy risk 9.00%; TP1 reward/risk 1.12R is below strategy minimum 1.35R

**Risk flags:** OK

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## SOCI — position_xgb — NO_TRADE

**Score:** 0.583 vs policy min 0.55 · **Close:** 378 · **ATR14:** 39.0 · **Volume ratio 20D:** 0.60 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 360–382, entry trigger **382**, stop **346**, risk 36 points (9.42%).

**Targets:** TP1 **438** (1.56R), TP2 **444** (1.72R), TP3 **470** (2.44R). Recommended base-case RR: **1.72R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 378: zone 360–382 uses ATR14 39.0 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 382 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 346 is capped by max risk 9.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 438 (1.56R), TP2 444 (1.72R), TP3 470 (2.44R). Targets are ATR/structure capped for hold_days=1. ATR14=39.0, resistance_5/10/20/60=442/540/565/780. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 9.42% exceeds max strategy risk 9.00%; volume ratio 0.60 below required 0.60; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## VKTR — position_xgb — NO_TRADE

**Score:** 0.580 vs policy min 0.55 · **Close:** 720 · **ATR14:** 87.1 · **Volume ratio 20D:** 0.53 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 680–730, entry trigger **730**, stop **660**, risk 70 points (9.59%).

**Targets:** TP1 **855** (1.79R), TP2 **885** (2.21R), TP3 **900** (2.43R). Recommended base-case RR: **2.21R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 720: zone 680–730 uses ATR14 87.1 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 730 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 660 is capped by max risk 9.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 855 (1.79R), TP2 885 (2.21R), TP3 900 (2.43R). Targets are ATR/structure capped for hold_days=1. ATR14=87.1, resistance_5/10/20/60=885/995/1,015/1,100. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 9.59% exceeds max strategy risk 9.00%; volume ratio 0.53 below required 0.60; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## BRMS — position_xgb — NO_TRADE

**Score:** 0.579 vs policy min 0.55 · **Close:** 605 · **ATR14:** 64.3 · **Volume ratio 20D:** 0.84 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 575–615, entry trigger **615**, stop **555**, risk 60 points (9.76%).

**Targets:** TP1 **675** (1.00R), TP2 **755** (2.33R), TP3 **760** (2.42R). Recommended base-case RR: **2.33R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 605: zone 575–615 uses ATR14 64.3 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 615 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 555 is capped by max risk 9.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 675 (1.00R), TP2 755 (2.33R), TP3 760 (2.42R). Targets are ATR/structure capped for hold_days=1. ATR14=64.3, resistance_5/10/20/60=755/835/930/1,120. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 9.76% exceeds max strategy risk 9.00%; TP1 reward/risk 1.00R is below strategy minimum 1.35R

**Risk flags:** OK

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## NSSS — position_xgb — NO_TRADE

**Score:** 0.577 vs policy min 0.55 · **Close:** 490 · **ATR14:** 72.6 · **Volume ratio 20D:** 0.46 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 456–498, entry trigger **498**, stop **452**, risk 46 points (9.24%).

**Targets:** TP1 **545** (1.02R), TP2 **675** (3.85R), TP3 **700** (4.39R). Recommended base-case RR: **3.85R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 490: zone 456–498 uses ATR14 72.6 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 498 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 452 is capped by max risk 9.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 545 (1.02R), TP2 675 (3.85R), TP3 700 (4.39R). Targets are ATR/structure capped for hold_days=1. ATR14=72.6, resistance_5/10/20/60=700/850/1,060/1,300. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 9.24% exceeds max strategy risk 9.00%; TP1 reward/risk 1.02R is below strategy minimum 1.35R; volume ratio 0.46 below required 0.60

**Risk flags:** OK

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## FPNI — position_xgb — NO_TRADE

**Score:** 0.576 vs policy min 0.55 · **Close:** 368 · **ATR14:** 40.6 · **Volume ratio 20D:** 0.96 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 348–374, entry trigger **374**, stop **340**, risk 34 points (9.09%).

**Targets:** TP1 **410** (1.06R), TP2 **432** (1.71R), TP3 **456** (2.41R). Recommended base-case RR: **1.71R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 368: zone 348–374 uses ATR14 40.6 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 374 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 340 is capped by max risk 9.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 410 (1.06R), TP2 432 (1.71R), TP3 456 (2.41R). Targets are ATR/structure capped for hold_days=1. ATR14=40.6, resistance_5/10/20/60=410/510/580/800. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 9.09% exceeds max strategy risk 9.00%; TP1 reward/risk 1.06R is below strategy minimum 1.35R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## COIN — position_xgb — NO_TRADE

**Score:** 0.574 vs policy min 0.55 · **Close:** 835 · **ATR14:** 111.4 · **Volume ratio 20D:** 0.43 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 780–850, entry trigger **850**, stop **770**, risk 80 points (9.41%).

**Targets:** TP1 **980** (1.62R), TP2 **990** (1.75R), TP3 **1,045** (2.44R). Recommended base-case RR: **1.75R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 835: zone 780–850 uses ATR14 111.4 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 850 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 770 is capped by max risk 9.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 980 (1.62R), TP2 990 (1.75R), TP3 1,045 (2.44R). Targets are ATR/structure capped for hold_days=1. ATR14=111.4, resistance_5/10/20/60=980/1,370/1,440/2,080. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 9.41% exceeds max strategy risk 9.00%; volume ratio 0.43 below required 0.60; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## MBMA — position_xgb — NO_TRADE

**Score:** 0.573 vs policy min 0.55 · **Close:** 496 · **ATR14:** 53.4 · **Volume ratio 20D:** 1.53 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 470–505, entry trigger **505**, stop **458**, risk 47 points (9.31%).

**Targets:** TP1 **555** (1.06R), TP2 **585** (1.70R), TP3 **620** (2.45R). Recommended base-case RR: **1.70R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 496: zone 470–505 uses ATR14 53.4 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 505 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 458 is capped by max risk 9.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 555 (1.06R), TP2 585 (1.70R), TP3 620 (2.45R). Targets are ATR/structure capped for hold_days=1. ATR14=53.4, resistance_5/10/20/60=550/680/770/945. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 9.31% exceeds max strategy risk 9.00%; TP1 reward/risk 1.06R is below strategy minimum 1.35R

**Risk flags:** OK

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## DEWA — position_xgb — NO_TRADE

**Score:** 0.573 vs policy min 0.55 · **Close:** 350 · **ATR14:** 41.0 · **Volume ratio 20D:** 0.98 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 330–356, entry trigger **356**, stop **322**, risk 34 points (9.55%).

**Targets:** TP1 **390** (1.00R), TP2 **450** (2.76R), TP3 **468** (3.29R). Recommended base-case RR: **2.76R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 350: zone 330–356 uses ATR14 41.0 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 356 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 322 is capped by max risk 9.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 390 (1.00R), TP2 450 (2.76R), TP3 468 (3.29R). Targets are ATR/structure capped for hold_days=1. ATR14=41.0, resistance_5/10/20/60=450/535/575/655. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 9.55% exceeds max strategy risk 9.00%; TP1 reward/risk 1.00R is below strategy minimum 1.35R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## BIPI — position_xgb — NO_TRADE

**Score:** 0.571 vs policy min 0.55 · **Close:** 179 · **ATR14:** 25.2 · **Volume ratio 20D:** 0.71 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 167–182, entry trigger **182**, stop **165**, risk 17 points (9.34%).

**Targets:** TP1 **199** (1.00R), TP2 **232** (2.94R), TP3 **242** (3.53R). Recommended base-case RR: **2.94R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 179: zone 167–182 uses ATR14 25.2 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 182 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 165 is capped by max risk 9.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 199 (1.00R), TP2 232 (2.94R), TP3 242 (3.53R). Targets are ATR/structure capped for hold_days=1. ATR14=25.2, resistance_5/10/20/60=232/262/302/342. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 9.34% exceeds max strategy risk 9.00%; TP1 reward/risk 1.00R is below strategy minimum 1.35R

**Risk flags:** OK

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## BUMI — position_xgb — NO_TRADE

**Score:** 0.570 vs policy min 0.55 · **Close:** 171 · **ATR14:** 17.4 · **Volume ratio 20D:** 1.17 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 163–173, entry trigger **173**, stop **157**, risk 16 points (9.25%).

**Targets:** TP1 **189** (1.00R), TP2 **212** (2.44R), TP3 **220** (2.94R). Recommended base-case RR: **2.44R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 171: zone 163–173 uses ATR14 17.4 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 173 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 157 is capped by max risk 9.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 189 (1.00R), TP2 212 (2.44R), TP3 220 (2.94R). Targets are ATR/structure capped for hold_days=1. ATR14=17.4, resistance_5/10/20/60=212/250/256/306. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 9.25% exceeds max strategy risk 9.00%; TP1 reward/risk 1.00R is below strategy minimum 1.35R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## BBHI — market_maker_silent_accum_defensive — NO_TRADE

**Score:** 0.507 vs policy min 0.55 · **Close:** 980 · **ATR14:** 69.6 · **Volume ratio 20D:** 3.03 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 955–995, entry trigger **995**, stop **920**, risk 75 points (7.54%).

**Targets:** TP1 **1,065** (0.93R), TP2 **1,125** (1.73R), TP3 **1,170** (2.33R). Recommended base-case RR: **1.73R**.

**Why entry:** Hybrid entry uses close 980 and ATR14 69.6: buy zone 955–995. Entry is valid only if price can trade/hold around 995 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 920 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,065 (0.93R), TP2 1,125 (1.73R), TP3 1,170 (2.33R). Targets are ATR/structure capped for hold_days=1. ATR14=69.6, resistance_5/10/20/60=1,000/1,275/1,310/1,445. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.54% exceeds max strategy risk 7.50%; score 0.507 below policy min_score 0.55; TP1 reward/risk 0.93R is below strategy minimum 1.25R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Defensive accumulation. Prefer retest and clean broker flow.

---

## DEWA — momentum_5d_hgb_defensive — NO_TRADE

**Score:** 0.467 vs policy min 0.55 · **Close:** 350 · **ATR14:** 41.0 · **Volume ratio 20D:** 0.98 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 340–540, entry trigger **540**, stop **500**, risk 40 points (7.41%).

**Targets:** TP1 **580** (1.00R), TP2 **610** (1.75R), TP3 **640** (2.50R). Recommended base-case RR: **1.75R**.

**Why entry:** Entry trigger 540 is set above recent resistance 535 plus one IDX tick. This requires confirmation instead of buying blindly at close 350. Entry is valid only if price can trade/hold around 540 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 500 is capped by max risk 7.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 580 (1.00R), TP2 610 (1.75R), TP3 640 (2.50R). Targets are ATR/structure capped for hold_days=1. ATR14=41.0, resistance_5/10/20/60=450/535/575/655. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 54.29% > max 8.00%; entry-to-stop risk 7.41% exceeds max strategy risk 7.00%; score 0.467 below policy min_score 0.55; TP1 reward/risk 1.00R is below strategy minimum 1.25R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Selective high-liquidity 5D momentum sleeve.

---

## KOKA — market_maker_silent_accum_defensive — NO_TRADE

**Score:** 0.461 vs policy min 0.55 · **Close:** 120 · **ATR14:** 16.6 · **Volume ratio 20D:** 1.88 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 114–124, entry trigger **124**, stop **114**, risk 10 points (8.06%).

**Targets:** TP1 **141** (1.70R), TP2 **147** (2.30R), TP3 **148** (2.40R). Recommended base-case RR: **2.30R**.

**Why entry:** Hybrid entry uses close 120 and ATR14 16.6: buy zone 114–124. Entry is valid only if price can trade/hold around 124 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 114 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 141 (1.70R), TP2 147 (2.30R), TP3 148 (2.40R). Targets are ATR/structure capped for hold_days=1. ATR14=16.6, resistance_5/10/20/60=147/184/226/318. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.06% exceeds max strategy risk 7.50%; score 0.461 below policy min_score 0.55; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Defensive accumulation. Prefer retest and clean broker flow.

---

## CUAN — momentum_5d_hgb_defensive — NO_TRADE

**Score:** 0.460 vs policy min 0.55 · **Close:** 486 · **ATR14:** 114.9 · **Volume ratio 20D:** 1.24 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 462–1,310, entry trigger **1,310**, stop **1,215**, risk 95 points (7.25%).

**Targets:** TP1 **1,405** (1.00R), TP2 **1,475** (1.74R), TP3 **1,610** (3.16R). Recommended base-case RR: **1.74R**.

**Why entry:** Entry trigger 1,310 is set above recent resistance 1,305 plus one IDX tick. This requires confirmation instead of buying blindly at close 486. Entry is valid only if price can trade/hold around 1,310 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 1,215 is capped by max risk 7.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,405 (1.00R), TP2 1,475 (1.74R), TP3 1,610 (3.16R). Targets are ATR/structure capped for hold_days=1. ATR14=114.9, resistance_5/10/20/60=775/1,305/1,620/1,990. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 169.55% > max 8.00%; entry-to-stop risk 7.25% exceeds max strategy risk 7.00%; score 0.460 below policy min_score 0.55; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Selective high-liquidity 5D momentum sleeve.

---

## KDTN — market_maker_silent_accum_defensive — NO_TRADE

**Score:** 0.449 vs policy min 0.55 · **Close:** 835 · **ATR14:** 121.1 · **Volume ratio 20D:** 0.50 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 790–860, entry trigger **860**, stop **795**, risk 65 points (7.56%).

**Targets:** TP1 **925** (1.00R), TP2 **1,040** (2.77R), TP3 **1,075** (3.31R). Recommended base-case RR: **2.77R**.

**Why entry:** Hybrid entry uses close 835 and ATR14 121.1: buy zone 790–860. Entry is valid only if price can trade/hold around 860 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 795 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 925 (1.00R), TP2 1,040 (2.77R), TP3 1,075 (3.31R). Targets are ATR/structure capped for hold_days=1. ATR14=121.1, resistance_5/10/20/60=1,040/1,040/1,350/1,350. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.56% exceeds max strategy risk 7.50%; score 0.449 below policy min_score 0.55; TP1 reward/risk 1.00R is below strategy minimum 1.25R; volume ratio 0.50 below required 0.60

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Defensive accumulation. Prefer retest and clean broker flow.

---

## SOTS — market_maker_silent_accum_defensive — NO_TRADE

**Score:** 0.440 vs policy min 0.55 · **Close:** 780 · **ATR14:** 110.4 · **Volume ratio 20D:** 0.87 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 740–805, entry trigger **805**, stop **740**, risk 65 points (8.07%).

**Targets:** TP1 **870** (1.00R), TP2 **985** (2.77R), TP3 **1,020** (3.31R). Recommended base-case RR: **2.77R**.

**Why entry:** Hybrid entry uses close 780 and ATR14 110.4: buy zone 740–805. Entry is valid only if price can trade/hold around 805 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 740 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 870 (1.00R), TP2 985 (2.77R), TP3 1,020 (3.31R). Targets are ATR/structure capped for hold_days=1. ATR14=110.4, resistance_5/10/20/60=985/1,050/1,500/2,930. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.07% exceeds max strategy risk 7.50%; score 0.440 below policy min_score 0.55; TP1 reward/risk 1.00R is below strategy minimum 1.25R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Defensive accumulation. Prefer retest and clean broker flow.

---

## TRIN — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.423 vs policy min 0.60 · **Close:** 472 · **ATR14:** 66.6 · **Volume ratio 20D:** 0.61 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 458–720, entry trigger **720**, stop **645**, risk 75 points (10.42%).

**Targets:** TP1 **845** (1.67R), TP2 **860** (1.87R), TP3 **900** (2.40R). Recommended base-case RR: **1.87R**.

**Why entry:** Entry trigger 720 is set above recent resistance 715 plus one IDX tick. This requires confirmation instead of buying blindly at close 472. Entry is valid only if price can trade/hold around 720 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 645 is capped by max risk 10.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 845 (1.67R), TP2 860 (1.87R), TP3 900 (2.40R). Targets are ATR/structure capped for hold_days=2. ATR14=66.6, resistance_5/10/20/60=600/715/860/1,225. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 52.54% > max 15.00%; entry-to-stop risk 10.42% exceeds max strategy risk 10.00%; score 0.423 below policy min_score 0.60; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## NINE — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.418 vs policy min 0.60 · **Close:** 103 · **ATR14:** 16.8 · **Volume ratio 20D:** 0.59 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 99–165, entry trigger **165**, stop **148**, risk 17 points (10.30%).

**Targets:** TP1 **182** (1.00R), TP2 **194** (1.71R), TP3 **206** (2.41R). Recommended base-case RR: **1.71R**.

**Why entry:** Entry trigger 165 is set above recent resistance 164 plus one IDX tick. This requires confirmation instead of buying blindly at close 103. Entry is valid only if price can trade/hold around 165 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 148 is capped by max risk 10.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 182 (1.00R), TP2 194 (1.71R), TP3 206 (2.41R). Targets are ATR/structure capped for hold_days=2. ATR14=16.8, resistance_5/10/20/60=130/164/166/182. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 60.19% > max 15.00%; entry-to-stop risk 10.30% exceeds max strategy risk 10.00%; score 0.418 below policy min_score 0.60; TP1 reward/risk 1.00R is below strategy minimum 1.40R; volume ratio 0.59 below required 0.60

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## KIJA — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.412 vs policy min 0.60 · **Close:** 124 · **ATR14:** 10.2 · **Volume ratio 20D:** 1.68 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 121–184, entry trigger **184**, stop **170**, risk 14 points (7.61%).

**Targets:** TP1 **198** (1.00R), TP2 **218** (2.43R), TP3 **220** (2.57R). Recommended base-case RR: **2.43R**.

**Why entry:** Entry trigger 184 is set above recent resistance 183 plus one IDX tick. This requires confirmation instead of buying blindly at close 124. Entry is valid only if price can trade/hold around 184 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 170 uses 1.30×ATR14 volatility cap. Thesis invalidates if the move reverses beyond normal volatility. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 198 (1.00R), TP2 218 (2.43R), TP3 220 (2.57R). Targets are ATR/structure capped for hold_days=2. ATR14=10.2, resistance_5/10/20/60=172/183/220/240. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 48.39% > max 15.00%; score 0.412 below policy min_score 0.60; TP1 reward/risk 1.00R is below strategy minimum 1.40R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## NICL — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.409 vs policy min 0.60 · **Close:** 555 · **ATR14:** 62.1 · **Volume ratio 20D:** 0.33 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 540–920, entry trigger **920**, stop **835**, risk 85 points (9.24%).

**Targets:** TP1 **1,030** (1.29R), TP2 **1,065** (1.71R), TP3 **1,125** (2.41R). Recommended base-case RR: **1.71R**.

**Why entry:** Entry trigger 920 is set above recent resistance 915 plus one IDX tick. This requires confirmation instead of buying blindly at close 555. Entry is valid only if price can trade/hold around 920 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 835 uses 1.30×ATR14 volatility cap. Thesis invalidates if the move reverses beyond normal volatility. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,030 (1.29R), TP2 1,065 (1.71R), TP3 1,125 (2.41R). Targets are ATR/structure capped for hold_days=2. ATR14=62.1, resistance_5/10/20/60=720/915/1,030/1,285. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 65.77% > max 15.00%; score 0.409 below policy min_score 0.60; TP1 reward/risk 1.29R is below strategy minimum 1.40R; volume ratio 0.33 below required 0.60

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## SSMS — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.409 vs policy min 0.60 · **Close:** 775 · **ATR14:** 85.0 · **Volume ratio 20D:** 1.88 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 755–1,450, entry trigger **1,450**, stop **1,335**, risk 115 points (7.93%).

**Targets:** TP1 **1,565** (1.00R), TP2 **1,730** (2.43R), TP3 **1,800** (3.04R). Recommended base-case RR: **2.43R**.

**Why entry:** Entry trigger 1,450 is set above recent resistance 1,445 plus one IDX tick. This requires confirmation instead of buying blindly at close 775. Entry is valid only if price can trade/hold around 1,450 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 1,335 uses 1.30×ATR14 volatility cap. Thesis invalidates if the move reverses beyond normal volatility. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,565 (1.00R), TP2 1,730 (2.43R), TP3 1,800 (3.04R). Targets are ATR/structure capped for hold_days=2. ATR14=85.0, resistance_5/10/20/60=1,105/1,445/1,470/1,800. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 87.10% > max 15.00%; score 0.409 below policy min_score 0.60; TP1 reward/risk 1.00R is below strategy minimum 1.40R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## NZIA — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.404 vs policy min 0.60 · **Close:** 116 · **ATR14:** 14.9 · **Volume ratio 20D:** 0.30 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 113–184, entry trigger **184**, stop **165**, risk 19 points (10.33%).

**Targets:** TP1 **208** (1.26R), TP2 **218** (1.79R), TP3 **230** (2.42R). Recommended base-case RR: **1.79R**.

**Why entry:** Entry trigger 184 is set above recent resistance 183 plus one IDX tick. This requires confirmation instead of buying blindly at close 116. Entry is valid only if price can trade/hold around 184 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 165 is capped by max risk 10.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 208 (1.26R), TP2 218 (1.79R), TP3 230 (2.42R). Targets are ATR/structure capped for hold_days=2. ATR14=14.9, resistance_5/10/20/60=159/183/208/316. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 58.62% > max 15.00%; entry-to-stop risk 10.33% exceeds max strategy risk 10.00%; score 0.404 below policy min_score 0.60; TP1 reward/risk 1.26R is below strategy minimum 1.40R; volume ratio 0.30 below required 0.60; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## BUMI — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.401 vs policy min 0.60 · **Close:** 171 · **ATR14:** 17.4 · **Volume ratio 20D:** 1.17 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 167–252, entry trigger **252**, stop **228**, risk 24 points (9.52%).

**Targets:** TP1 **276** (1.00R), TP2 **306** (2.25R), TP3 **310** (2.42R). Recommended base-case RR: **2.25R**.

**Why entry:** Entry trigger 252 is set above recent resistance 250 plus one IDX tick. This requires confirmation instead of buying blindly at close 171. Entry is valid only if price can trade/hold around 252 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 228 uses 1.30×ATR14 volatility cap. Thesis invalidates if the move reverses beyond normal volatility. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 276 (1.00R), TP2 306 (2.25R), TP3 310 (2.42R). Targets are ATR/structure capped for hold_days=2. ATR14=17.4, resistance_5/10/20/60=212/250/256/306. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 47.37% > max 15.00%; score 0.401 below policy min_score 0.60; TP1 reward/risk 1.00R is below strategy minimum 1.40R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## RMKO — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.398 vs policy min 0.60 · **Close:** 336 · **ATR14:** 41.8 · **Volume ratio 20D:** 0.38 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 326–510, entry trigger **510**, stop **458**, risk 52 points (10.20%).

**Targets:** TP1 **590** (1.54R), TP2 **605** (1.83R), TP3 **635** (2.40R). Recommended base-case RR: **1.83R**.

**Why entry:** Entry trigger 510 is set above recent resistance 505 plus one IDX tick. This requires confirmation instead of buying blindly at close 336. Entry is valid only if price can trade/hold around 510 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 458 is capped by max risk 10.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 590 (1.54R), TP2 605 (1.83R), TP3 635 (2.40R). Targets are ATR/structure capped for hold_days=2. ATR14=41.8, resistance_5/10/20/60=452/505/605/1,180. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 51.79% > max 15.00%; entry-to-stop risk 10.20% exceeds max strategy risk 10.00%; score 0.398 below policy min_score 0.60; volume ratio 0.38 below required 0.60; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## BRMS — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.398 vs policy min 0.60 · **Close:** 605 · **ATR14:** 64.3 · **Volume ratio 20D:** 0.84 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 590–840, entry trigger **840**, stop **755**, risk 85 points (10.12%).

**Targets:** TP1 **930** (1.06R), TP2 **985** (1.71R), TP3 **1,045** (2.41R). Recommended base-case RR: **1.71R**.

**Why entry:** Entry trigger 840 is set above recent resistance 835 plus one IDX tick. This requires confirmation instead of buying blindly at close 605. Entry is valid only if price can trade/hold around 840 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 755 uses 1.30×ATR14 volatility cap. Thesis invalidates if the move reverses beyond normal volatility. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 930 (1.06R), TP2 985 (1.71R), TP3 1,045 (2.41R). Targets are ATR/structure capped for hold_days=2. ATR14=64.3, resistance_5/10/20/60=755/835/930/1,120. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 38.84% > max 15.00%; entry-to-stop risk 10.12% exceeds max strategy risk 10.00%; score 0.398 below policy min_score 0.60; TP1 reward/risk 1.06R is below strategy minimum 1.40R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## NCKL — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.398 vs policy min 0.60 · **Close:** 875 · **ATR14:** 64.3 · **Volume ratio 20D:** 1.20 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 860–1,075, entry trigger **1,075**, stop **990**, risk 85 points (7.91%).

**Targets:** TP1 **1,195** (1.41R), TP2 **1,245** (2.00R), TP3 **1,280** (2.41R). Recommended base-case RR: **2.00R**.

**Why entry:** Entry trigger 1,075 is set above recent resistance 1,070 plus one IDX tick. This requires confirmation instead of buying blindly at close 875. Entry is valid only if price can trade/hold around 1,075 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 990 uses 1.30×ATR14 volatility cap. Thesis invalidates if the move reverses beyond normal volatility. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,195 (1.41R), TP2 1,245 (2.00R), TP3 1,280 (2.41R). Targets are ATR/structure capped for hold_days=2. ATR14=64.3, resistance_5/10/20/60=1,000/1,070/1,245/1,595. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 22.86% > max 15.00%; score 0.398 below policy min_score 0.60

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## COIN — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.397 vs policy min 0.60 · **Close:** 835 · **ATR14:** 111.4 · **Volume ratio 20D:** 0.43 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 810–1,375, entry trigger **1,375**, stop **1,235**, risk 140 points (10.18%).

**Targets:** TP1 **1,515** (1.00R), TP2 **1,615** (1.71R), TP3 **1,715** (2.43R). Recommended base-case RR: **1.71R**.

**Why entry:** Entry trigger 1,375 is set above recent resistance 1,370 plus one IDX tick. This requires confirmation instead of buying blindly at close 835. Entry is valid only if price can trade/hold around 1,375 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 1,235 is capped by max risk 10.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,515 (1.00R), TP2 1,615 (1.71R), TP3 1,715 (2.43R). Targets are ATR/structure capped for hold_days=2. ATR14=111.4, resistance_5/10/20/60=980/1,370/1,440/2,080. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 64.67% > max 15.00%; entry-to-stop risk 10.18% exceeds max strategy risk 10.00%; score 0.397 below policy min_score 0.60; TP1 reward/risk 1.00R is below strategy minimum 1.40R; volume ratio 0.43 below required 0.60; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## TALF — ara_candidate — NO_TRADE

**Score:** 0.386 vs policy min 0.50 · **Close:** 975 · **ATR14:** 88.9 · **Volume ratio 20D:** 2.82 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 955–980, entry trigger **980**, stop **880**, risk 100 points (10.20%).

**Targets:** TP1 **1,070** (0.90R), TP2 **1,150** (1.70R), TP3 **1,220** (2.40R). Recommended base-case RR: **1.70R**.

**Why entry:** Entry trigger 980 is set above recent resistance 975 plus one IDX tick. This requires confirmation instead of buying blindly at close 975. Entry is valid only if price can trade/hold around 980 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 880 uses 1.10×ATR14 volatility cap. Thesis invalidates if the move reverses beyond normal volatility. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,070 (0.90R), TP2 1,150 (1.70R), TP3 1,220 (2.40R). Targets are ATR/structure capped for hold_days=1. ATR14=88.9, resistance_5/10/20/60=975/975/975/975. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 10.20% exceeds max strategy risk 10.00%; score 0.386 below policy min_score 0.50; TP1 reward/risk 0.90R is below strategy minimum 1.30R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** High drawdown tactical setup. Use as execution only if confirmation is strong and liquidity is clean.

---
