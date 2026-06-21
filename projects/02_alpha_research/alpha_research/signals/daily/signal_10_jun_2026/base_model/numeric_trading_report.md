# Numeric Trading Desk Report — 2026-06-09

This report is generated from live model scores, selected signal policy, canonical OHLCV, ATR, support/resistance, liquidity, and broker-flow diagnostics. It is not a simple BUY/SELL list; each plan is conditional on execution behaviour.

## Summary

| Plan quality | Count |
|---|---:|
| ACTIONABLE | 1 |
| CONDITIONAL | 4 |
| WATCHLIST_ONLY | 1 |
| NO_TRADE | 50 |

## UVCR — swing_hgb_defensive — ACTIONABLE

**Score:** 0.665 vs policy min 0.50 · **Close:** 133 · **ATR14:** 17.9 · **Volume ratio 20D:** 2.51 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 124–135, entry trigger **135**, stop **128**, risk 7 points (5.19%).

**Targets:** TP1 **144** (1.29R), TP2 **147** (1.71R), TP3 **152** (2.43R). Recommended base-case RR: **1.71R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 133: zone 124–135 uses ATR14 17.9 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 135 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 128 is placed below support structure (129 / 129). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 144 (1.29R), TP2 147 (1.71R), TP3 152 (2.43R). Targets are ATR/structure capped for hold_days=1. ATR14=17.9, resistance_5/10/20/60=242/250/250/250. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## BMTR — position_xgb — CONDITIONAL

**Score:** 0.599 vs policy min 0.55 · **Close:** 109 · **ATR14:** 7.6 · **Volume ratio 20D:** 1.84 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 105–110, entry trigger **110**, stop **101**, risk 9 points (8.18%).

**Targets:** TP1 **121** (1.22R), TP2 **126** (1.78R), TP3 **132** (2.44R). Recommended base-case RR: **1.78R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 109: zone 105–110 uses ATR14 7.6 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 110 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 101 is placed below support structure (102 / 102). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 121 (1.22R), TP2 126 (1.78R), TP3 132 (2.44R). Targets are ATR/structure capped for hold_days=1. ATR14=7.6, resistance_5/10/20/60=126/132/167/204. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.22R is below strategy minimum 1.35R

**Risk flags:** OK

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## ARCI — position_xgb — CONDITIONAL

**Score:** 0.596 vs policy min 0.55 · **Close:** 985 · **ATR14:** 109.6 · **Volume ratio 20D:** 0.67 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 935–1,000, entry trigger **1,000**, stop **910**, risk 90 points (9.00%).

**Targets:** TP1 **1,155** (1.72R), TP2 **1,200** (2.22R), TP3 **1,220** (2.44R). Recommended base-case RR: **2.22R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 985: zone 935–1,000 uses ATR14 109.6 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 1,000 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 910 is placed below support structure (915 / 915). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,155 (1.72R), TP2 1,200 (2.22R), TP3 1,220 (2.44R). Targets are ATR/structure capped for hold_days=1. ATR14=109.6, resistance_5/10/20/60=1,155/1,265/1,625/2,020. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## PWON — position_xgb — CONDITIONAL

**Score:** 0.595 vs policy min 0.55 · **Close:** 242 · **ATR14:** 13.3 · **Volume ratio 20D:** 4.61 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 236–244, entry trigger **244**, stop **238**, risk 6 points (2.46%).

**Targets:** TP1 **252** (1.33R), TP2 **256** (2.00R), TP3 **290** (7.67R). Recommended base-case RR: **2.00R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 242: zone 236–244 uses ATR14 13.3 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 244 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 238 is placed below support structure (240 / 240). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 252 (1.33R), TP2 256 (2.00R), TP3 290 (7.67R). Targets are ATR/structure capped for hold_days=1. ATR14=13.3, resistance_5/10/20/60=290/300/326/362. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.33R is below strategy minimum 1.35R

**Risk flags:** OK

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## STAA — position_xgb — CONDITIONAL

**Score:** 0.595 vs policy min 0.55 · **Close:** 905 · **ATR14:** 55.4 · **Volume ratio 20D:** 1.69 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 880–915, entry trigger **915**, stop **855**, risk 60 points (6.56%).

**Targets:** TP1 **975** (1.00R), TP2 **1,020** (1.75R), TP3 **1,060** (2.42R). Recommended base-case RR: **1.75R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 905: zone 880–915 uses ATR14 55.4 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 915 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 855 is placed below support structure (860 / 860). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 975 (1.00R), TP2 1,020 (1.75R), TP3 1,060 (2.42R). Targets are ATR/structure capped for hold_days=1. ATR14=55.4, resistance_5/10/20/60=935/1,045/1,240/1,385. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.35R

**Risk flags:** OK

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## GULA — momentum_10d_hgb_aggressive — WATCHLIST_ONLY

**Score:** 0.402 vs policy min 0.60 · **Close:** 560 · **ATR14:** 41.5 · **Volume ratio 20D:** 1.41 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 550–575, entry trigger **575**, stop **520**, risk 55 points (9.57%).

**Targets:** TP1 **630** (1.00R), TP2 **670** (1.73R), TP3 **710** (2.45R). Recommended base-case RR: **1.73R**.

**Why entry:** Entry trigger 575 is set above recent resistance 570 plus one IDX tick. This requires confirmation instead of buying blindly at close 560. Entry is valid only if price can trade/hold around 575 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 520 uses 1.30×ATR14 volatility cap. Thesis invalidates if the move reverses beyond normal volatility. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 630 (1.00R), TP2 670 (1.73R), TP3 710 (2.45R). Targets are ATR/structure capped for hold_days=2. ATR14=41.5, resistance_5/10/20/60=570/570/570/570. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** score 0.402 below policy min_score 0.60; TP1 reward/risk 1.00R is below strategy minimum 1.40R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## SSMS — swing_hgb_defensive — NO_TRADE

**Score:** 0.699 vs policy min 0.50 · **Close:** 740 · **ATR14:** 88.9 · **Volume ratio 20D:** 0.98 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 695–750, entry trigger **750**, stop **690**, risk 60 points (8.00%).

**Targets:** TP1 **820** (1.17R), TP2 **855** (1.75R), TP3 **895** (2.42R). Recommended base-case RR: **1.75R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 740: zone 695–750 uses ATR14 88.9 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 750 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 690 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 820 (1.17R), TP2 855 (1.75R), TP3 895 (2.42R). Targets are ATR/structure capped for hold_days=1. ATR14=88.9, resistance_5/10/20/60=820/910/1,430/1,570. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.00% exceeds max strategy risk 7.50%; TP1 reward/risk 1.17R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## NICL — swing_hgb_defensive — NO_TRADE

**Score:** 0.694 vs policy min 0.50 · **Close:** 505 · **ATR14:** 70.1 · **Volume ratio 20D:** 1.72 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 472–515, entry trigger **515**, stop **476**, risk 39 points (7.57%).

**Targets:** TP1 **555** (1.03R), TP2 **630** (2.95R), TP3 **650** (3.46R). Recommended base-case RR: **2.95R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 505: zone 472–515 uses ATR14 70.1 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 515 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 476 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 555 (1.03R), TP2 630 (2.95R), TP3 650 (3.46R). Targets are ATR/structure capped for hold_days=1. ATR14=70.1, resistance_5/10/20/60=630/630/875/1,100. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.57% exceeds max strategy risk 7.50%; TP1 reward/risk 1.03R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## TPMA — swing_hgb_defensive — NO_TRADE

**Score:** 0.694 vs policy min 0.50 · **Close:** 360 · **ATR14:** 28.1 · **Volume ratio 20D:** 0.60 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 346–364, entry trigger **364**, stop **336**, risk 28 points (7.69%).

**Targets:** TP1 **392** (1.00R), TP2 **412** (1.71R), TP3 **436** (2.57R). Recommended base-case RR: **1.71R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 360: zone 346–364 uses ATR14 28.1 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 364 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 336 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 392 (1.00R), TP2 412 (1.71R), TP3 436 (2.57R). Targets are ATR/structure capped for hold_days=1. ATR14=28.1, resistance_5/10/20/60=438/510/565/615. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.69% exceeds max strategy risk 7.50%; TP1 reward/risk 1.00R is below strategy minimum 1.25R; volume ratio 0.60 below required 0.60

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## HRUM — swing_hgb_defensive — NO_TRADE

**Score:** 0.686 vs policy min 0.50 · **Close:** 705 · **ATR14:** 73.6 · **Volume ratio 20D:** 0.92 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 670–715, entry trigger **715**, stop **660**, risk 55 points (7.69%).

**Targets:** TP1 **790** (1.36R), TP2 **825** (2.00R), TP3 **850** (2.45R). Recommended base-case RR: **2.00R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 705: zone 670–715 uses ATR14 73.6 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 715 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 660 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 790 (1.36R), TP2 825 (2.00R), TP3 850 (2.45R). Targets are ATR/structure capped for hold_days=1. ATR14=73.6, resistance_5/10/20/60=825/830/1,010/1,260. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.69% exceeds max strategy risk 7.50%

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## EMTK — swing_hgb_defensive — NO_TRADE

**Score:** 0.686 vs policy min 0.50 · **Close:** 535 · **ATR14:** 49.0 · **Volume ratio 20D:** 1.61 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 510–540, entry trigger **540**, stop **498**, risk 42 points (7.78%).

**Targets:** TP1 **590** (1.19R), TP2 **615** (1.79R), TP3 **645** (2.50R). Recommended base-case RR: **1.79R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 535: zone 510–540 uses ATR14 49.0 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 540 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 498 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 590 (1.19R), TP2 615 (1.79R), TP3 645 (2.50R). Targets are ATR/structure capped for hold_days=1. ATR14=49.0, resistance_5/10/20/60=615/675/830/975. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.78% exceeds max strategy risk 7.50%; TP1 reward/risk 1.19R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## BFIN — swing_hgb_defensive — NO_TRADE

**Score:** 0.684 vs policy min 0.50 · **Close:** 640 · **ATR14:** 40.4 · **Volume ratio 20D:** 0.75 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 620–645, entry trigger **645**, stop **595**, risk 50 points (7.75%).

**Targets:** TP1 **690** (0.90R), TP2 **720** (1.50R), TP3 **765** (2.40R). Recommended base-case RR: **1.50R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 640: zone 620–645 uses ATR14 40.4 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 645 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 595 uses 1.20×ATR14 volatility cap. Thesis invalidates if the move reverses beyond normal volatility. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 690 (0.90R), TP2 720 (1.50R), TP3 765 (2.40R). Targets are ATR/structure capped for hold_days=1. ATR14=40.4, resistance_5/10/20/60=700/740/825/965. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.75% exceeds max strategy risk 7.50%; TP1 reward/risk 0.90R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## GZCO — swing_hgb_defensive — NO_TRADE

**Score:** 0.680 vs policy min 0.50 · **Close:** 127 · **ATR14:** 17.8 · **Volume ratio 20D:** 1.12 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 118–129, entry trigger **129**, stop **119**, risk 10 points (7.75%).

**Targets:** TP1 **139** (1.00R), TP2 **158** (2.90R), TP3 **163** (3.40R). Recommended base-case RR: **2.90R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 127: zone 118–129 uses ATR14 17.8 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 129 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 119 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 139 (1.00R), TP2 158 (2.90R), TP3 163 (3.40R). Targets are ATR/structure capped for hold_days=1. ATR14=17.8, resistance_5/10/20/60=158/166/232/252. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.75% exceeds max strategy risk 7.50%; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## TRIN — swing_hgb_defensive — NO_TRADE

**Score:** 0.678 vs policy min 0.50 · **Close:** 430 · **ATR14:** 71.3 · **Volume ratio 20D:** 3.20 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 396–438, entry trigger **438**, stop **404**, risk 34 points (7.76%).

**Targets:** TP1 **510** (2.12R), TP2 **515** (2.26R), TP3 **520** (2.41R). Recommended base-case RR: **2.26R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 430: zone 396–438 uses ATR14 71.3 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 438 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 404 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 510 (2.12R), TP2 515 (2.26R), TP3 520 (2.41R). Targets are ATR/structure capped for hold_days=1. ATR14=71.3, resistance_5/10/20/60=430/515/700/970. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.76% exceeds max strategy risk 7.50%

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## BBYB — swing_hgb_defensive — NO_TRADE

**Score:** 0.678 vs policy min 0.50 · **Close:** 218 · **ATR14:** 20.6 · **Volume ratio 20D:** 1.89 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 208–222, entry trigger **222**, stop **204**, risk 18 points (8.11%).

**Targets:** TP1 **240** (1.00R), TP2 **260** (2.11R), TP3 **266** (2.44R). Recommended base-case RR: **2.11R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 218: zone 208–222 uses ATR14 20.6 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 222 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 204 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 240 (1.00R), TP2 260 (2.11R), TP3 266 (2.44R). Targets are ATR/structure capped for hold_days=1. ATR14=20.6, resistance_5/10/20/60=264/282/324/360. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.11% exceeds max strategy risk 7.50%; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## SOFA — swing_hgb_defensive — NO_TRADE

**Score:** 0.673 vs policy min 0.50 · **Close:** 258 · **ATR14:** 43.0 · **Volume ratio 20D:** 2.28 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 238–264, entry trigger **264**, stop **244**, risk 20 points (7.58%).

**Targets:** TP1 **286** (1.10R), TP2 **298** (1.70R), TP3 **362** (4.90R). Recommended base-case RR: **1.70R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 258: zone 238–264 uses ATR14 43.0 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 264 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 244 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 286 (1.10R), TP2 298 (1.70R), TP3 362 (4.90R). Targets are ATR/structure capped for hold_days=1. ATR14=43.0, resistance_5/10/20/60=362/446/446/580. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.58% exceeds max strategy risk 7.50%; TP1 reward/risk 1.10R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## TOBA — swing_hgb_defensive — NO_TRADE

**Score:** 0.673 vs policy min 0.50 · **Close:** 360 · **ATR14:** 42.2 · **Volume ratio 20D:** 1.02 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 340–366, entry trigger **366**, stop **338**, risk 28 points (7.65%).

**Targets:** TP1 **394** (1.00R), TP2 **440** (2.64R), TP3 **454** (3.14R). Recommended base-case RR: **2.64R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 360: zone 340–366 uses ATR14 42.2 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 366 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 338 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 394 (1.00R), TP2 440 (2.64R), TP3 454 (3.14R). Targets are ATR/structure capped for hold_days=1. ATR14=42.2, resistance_5/10/20/60=440/462/650/750. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.65% exceeds max strategy risk 7.50%; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## BUKA — swing_hgb_defensive — NO_TRADE

**Score:** 0.670 vs policy min 0.50 · **Close:** 109 · **ATR14:** 7.6 · **Volume ratio 20D:** 1.12 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 105–110, entry trigger **110**, stop **101**, risk 9 points (8.18%).

**Targets:** TP1 **118** (0.89R), TP2 **124** (1.56R), TP3 **132** (2.44R). Recommended base-case RR: **1.56R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 109: zone 105–110 uses ATR14 7.6 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 110 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 101 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 118 (0.89R), TP2 124 (1.56R), TP3 132 (2.44R). Targets are ATR/structure capped for hold_days=1. ATR14=7.6, resistance_5/10/20/60=126/131/152/184. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.18% exceeds max strategy risk 7.50%; TP1 reward/risk 0.89R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## NSSS — swing_hgb_defensive — NO_TRADE

**Score:** 0.667 vs policy min 0.50 · **Close:** 386 · **ATR14:** 59.1 · **Volume ratio 20D:** 0.61 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 358–392, entry trigger **392**, stop **362**, risk 30 points (7.65%).

**Targets:** TP1 **452** (2.00R), TP2 **468** (2.53R), TP3 **484** (3.07R). Recommended base-case RR: **2.53R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 386: zone 358–392 uses ATR14 59.1 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 392 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 362 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 452 (2.00R), TP2 468 (2.53R), TP3 484 (3.07R). Targets are ATR/structure capped for hold_days=1. ATR14=59.1, resistance_5/10/20/60=468/510/850/1,110. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.65% exceeds max strategy risk 7.50%

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## SOCI — swing_hgb_defensive — NO_TRADE

**Score:** 0.664 vs policy min 0.50 · **Close:** 296 · **ATR14:** 40.1 · **Volume ratio 20D:** 0.86 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 276–302, entry trigger **302**, stop **278**, risk 24 points (7.95%).

**Targets:** TP1 **326** (1.00R), TP2 **344** (1.75R), TP3 **396** (3.92R). Recommended base-case RR: **1.75R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 296: zone 276–302 uses ATR14 40.1 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 302 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 278 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 326 (1.00R), TP2 344 (1.75R), TP3 396 (3.92R). Targets are ATR/structure capped for hold_days=1. ATR14=40.1, resistance_5/10/20/60=396/416/540/735. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.95% exceeds max strategy risk 7.50%; TP1 reward/risk 1.00R is below strategy minimum 1.25R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## NSSS — market_maker_silent_accum_defensive — NO_TRADE

**Score:** 0.619 vs policy min 0.55 · **Close:** 386 · **ATR14:** 59.1 · **Volume ratio 20D:** 0.61 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 364–398, entry trigger **398**, stop **368**, risk 30 points (7.54%).

**Targets:** TP1 **458** (2.00R), TP2 **468** (2.33R), TP3 **470** (2.40R). Recommended base-case RR: **2.33R**.

**Why entry:** Hybrid entry uses close 386 and ATR14 59.1: buy zone 364–398. Entry is valid only if price can trade/hold around 398 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 368 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 458 (2.00R), TP2 468 (2.33R), TP3 470 (2.40R). Targets are ATR/structure capped for hold_days=1. ATR14=59.1, resistance_5/10/20/60=468/510/850/1,110. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.54% exceeds max strategy risk 7.50%

**Risk flags:** OK

**Strategy risk note:** Defensive accumulation. Prefer retest and clean broker flow.

---

## GZCO — position_xgb — NO_TRADE

**Score:** 0.602 vs policy min 0.55 · **Close:** 127 · **ATR14:** 17.8 · **Volume ratio 20D:** 1.12 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 118–129, entry trigger **129**, stop **117**, risk 12 points (9.30%).

**Targets:** TP1 **154** (2.08R), TP2 **158** (2.42R), TP3 **164** (2.92R). Recommended base-case RR: **2.42R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 127: zone 118–129 uses ATR14 17.8 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 129 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 117 is capped by max risk 9.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 154 (2.08R), TP2 158 (2.42R), TP3 164 (2.92R). Targets are ATR/structure capped for hold_days=1. ATR14=17.8, resistance_5/10/20/60=158/166/232/252. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 9.30% exceeds max strategy risk 9.00%

**Risk flags:** OK

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## ARTO — position_xgb — NO_TRADE

**Score:** 0.602 vs policy min 0.55 · **Close:** 940 · **ATR14:** 83.2 · **Volume ratio 20D:** 2.57 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 900–950, entry trigger **950**, stop **860**, risk 90 points (9.47%).

**Targets:** TP1 **1,040** (1.00R), TP2 **1,150** (2.22R), TP3 **1,185** (2.61R). Recommended base-case RR: **2.22R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 940: zone 900–950 uses ATR14 83.2 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 950 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 860 is capped by max risk 9.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,040 (1.00R), TP2 1,150 (2.22R), TP3 1,185 (2.61R). Targets are ATR/structure capped for hold_days=1. ATR14=83.2, resistance_5/10/20/60=1,185/1,185/1,290/1,590. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 9.47% exceeds max strategy risk 9.00%; TP1 reward/risk 1.00R is below strategy minimum 1.35R

**Risk flags:** OK

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## AGRO — position_xgb — NO_TRADE

**Score:** 0.601 vs policy min 0.55 · **Close:** 133 · **ATR14:** 9.4 · **Volume ratio 20D:** 1.56 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 128–134, entry trigger **134**, stop **121**, risk 13 points (9.70%).

**Targets:** TP1 **147** (1.00R), TP2 **157** (1.77R), TP3 **166** (2.46R). Recommended base-case RR: **1.77R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 133: zone 128–134 uses ATR14 9.4 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 134 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 121 is capped by max risk 9.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 147 (1.00R), TP2 157 (1.77R), TP3 166 (2.46R). Targets are ATR/structure capped for hold_days=1. ATR14=9.4, resistance_5/10/20/60=165/169/194/248. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 9.70% exceeds max strategy risk 9.00%; TP1 reward/risk 1.00R is below strategy minimum 1.35R

**Risk flags:** OK

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## EMTK — position_xgb — NO_TRADE

**Score:** 0.600 vs policy min 0.55 · **Close:** 535 · **ATR14:** 49.0 · **Volume ratio 20D:** 1.61 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 510–540, entry trigger **540**, stop **490**, risk 50 points (9.26%).

**Targets:** TP1 **610** (1.40R), TP2 **625** (1.70R), TP3 **660** (2.40R). Recommended base-case RR: **1.70R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 535: zone 510–540 uses ATR14 49.0 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 540 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 490 is capped by max risk 9.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 610 (1.40R), TP2 625 (1.70R), TP3 660 (2.40R). Targets are ATR/structure capped for hold_days=1. ATR14=49.0, resistance_5/10/20/60=615/675/830/975. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 9.26% exceeds max strategy risk 9.00%

**Risk flags:** OK

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## SOCI — position_xgb — NO_TRADE

**Score:** 0.599 vs policy min 0.55 · **Close:** 296 · **ATR14:** 40.1 · **Volume ratio 20D:** 0.86 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 276–302, entry trigger **302**, stop **274**, risk 28 points (9.27%).

**Targets:** TP1 **330** (1.00R), TP2 **396** (3.36R), TP3 **410** (3.86R). Recommended base-case RR: **3.36R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 296: zone 276–302 uses ATR14 40.1 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 302 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 274 is capped by max risk 9.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 330 (1.00R), TP2 396 (3.36R), TP3 410 (3.86R). Targets are ATR/structure capped for hold_days=1. ATR14=40.1, resistance_5/10/20/60=396/416/540/735. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 9.27% exceeds max strategy risk 9.00%; TP1 reward/risk 1.00R is below strategy minimum 1.35R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## BUKA — position_xgb — NO_TRADE

**Score:** 0.598 vs policy min 0.55 · **Close:** 109 · **ATR14:** 7.6 · **Volume ratio 20D:** 1.12 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 105–110, entry trigger **110**, stop **100**, risk 10 points (9.09%).

**Targets:** TP1 **121** (1.10R), TP2 **127** (1.70R), TP3 **134** (2.40R). Recommended base-case RR: **1.70R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 109: zone 105–110 uses ATR14 7.6 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 110 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 100 is placed below support structure (101 / 101). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 121 (1.10R), TP2 127 (1.70R), TP3 134 (2.40R). Targets are ATR/structure capped for hold_days=1. ATR14=7.6, resistance_5/10/20/60=126/131/152/184. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 9.09% exceeds max strategy risk 9.00%; TP1 reward/risk 1.10R is below strategy minimum 1.35R

**Risk flags:** OK

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## ESSA — position_xgb — NO_TRADE

**Score:** 0.598 vs policy min 0.55 · **Close:** 610 · **ATR14:** 60.4 · **Volume ratio 20D:** 0.78 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 580–620, entry trigger **620**, stop **560**, risk 60 points (9.68%).

**Targets:** TP1 **680** (1.00R), TP2 **725** (1.75R), TP3 **765** (2.42R). Recommended base-case RR: **1.75R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 610: zone 580–620 uses ATR14 60.4 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 620 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 560 is capped by max risk 9.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 680 (1.00R), TP2 725 (1.75R), TP3 765 (2.42R). Targets are ATR/structure capped for hold_days=1. ATR14=60.4, resistance_5/10/20/60=675/720/915/995. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 9.68% exceeds max strategy risk 9.00%; TP1 reward/risk 1.00R is below strategy minimum 1.35R

**Risk flags:** OK

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## TRIN — scalping_rank_hgb — NO_TRADE

**Score:** 0.597 vs policy min 0.60 · **Close:** 430 · **ATR14:** 71.3 · **Volume ratio 20D:** 3.20 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 414–432, entry trigger **432**, stop **412**, risk 20 points (4.63%).

**Targets:** TP1 **468** (1.80R), TP2 **515** (4.15R), TP3 **525** (4.65R). Recommended base-case RR: **4.15R**.

**Why entry:** Entry trigger 432 is set above recent resistance 430 plus one IDX tick. This requires confirmation instead of buying blindly at close 430. Entry is valid only if price can trade/hold around 432 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 412 is capped by max risk 4.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 468 (1.80R), TP2 515 (4.15R), TP3 525 (4.65R). Targets are ATR/structure capped for hold_days=1. ATR14=71.3, resistance_5/10/20/60=430/515/700/970. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 4.63% exceeds max strategy risk 4.50%; score 0.597 below policy min_score 0.60

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Top-1 short-horizon scalp; invalidation must be quick.

---

## COIN — position_xgb — NO_TRADE

**Score:** 0.597 vs policy min 0.55 · **Close:** 680 · **ATR14:** 99.6 · **Volume ratio 20D:** 0.66 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 635–690, entry trigger **690**, stop **625**, risk 65 points (9.42%).

**Targets:** TP1 **825** (2.08R), TP2 **860** (2.62R), TP3 **895** (3.15R). Recommended base-case RR: **2.62R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 680: zone 635–690 uses ATR14 99.6 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 690 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 625 is capped by max risk 9.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 825 (2.08R), TP2 860 (2.62R), TP3 895 (3.15R). Targets are ATR/structure capped for hold_days=1. ATR14=99.6, resistance_5/10/20/60=825/905/1,370/1,555. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 9.42% exceeds max strategy risk 9.00%; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## ICON — market_maker_silent_accum_defensive — NO_TRADE

**Score:** 0.593 vs policy min 0.55 · **Close:** 105 · **ATR14:** 15.1 · **Volume ratio 20D:** 1.76 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 99–109, entry trigger **109**, stop **100**, risk 9 points (8.26%).

**Targets:** TP1 **123** (1.56R), TP2 **125** (1.78R), TP3 **131** (2.44R). Recommended base-case RR: **1.78R**.

**Why entry:** Hybrid entry uses close 105 and ATR14 15.1: buy zone 99–109. Entry is valid only if price can trade/hold around 109 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 100 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 123 (1.56R), TP2 125 (1.78R), TP3 131 (2.44R). Targets are ATR/structure capped for hold_days=1. ATR14=15.1, resistance_5/10/20/60=123/123/160/167. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.26% exceeds max strategy risk 7.50%; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Defensive accumulation. Prefer retest and clean broker flow.

---

## NRCA — position_xgb — NO_TRADE

**Score:** 0.593 vs policy min 0.55 · **Close:** 410 · **ATR14:** 43.4 · **Volume ratio 20D:** 0.91 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 390–416, entry trigger **416**, stop **378**, risk 38 points (9.13%).

**Targets:** TP1 **454** (1.00R), TP2 **505** (2.34R), TP3 **510** (2.47R). Recommended base-case RR: **2.34R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 410: zone 390–416 uses ATR14 43.4 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 416 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 378 is capped by max risk 9.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 454 (1.00R), TP2 505 (2.34R), TP3 510 (2.47R). Targets are ATR/structure capped for hold_days=1. ATR14=43.4, resistance_5/10/20/60=505/510/635/795. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 9.13% exceeds max strategy risk 9.00%; TP1 reward/risk 1.00R is below strategy minimum 1.35R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## NSSS — position_xgb — NO_TRADE

**Score:** 0.593 vs policy min 0.55 · **Close:** 386 · **ATR14:** 59.1 · **Volume ratio 20D:** 0.61 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 358–392, entry trigger **392**, stop **356**, risk 36 points (9.18%).

**Targets:** TP1 **468** (2.11R), TP2 **486** (2.61R), TP3 **505** (3.14R). Recommended base-case RR: **2.61R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 386: zone 358–392 uses ATR14 59.1 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 392 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 356 is capped by max risk 9.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 468 (2.11R), TP2 486 (2.61R), TP3 505 (3.14R). Targets are ATR/structure capped for hold_days=1. ATR14=59.1, resistance_5/10/20/60=468/510/850/1,110. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 9.18% exceeds max strategy risk 9.00%

**Risk flags:** OK

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## ASSA — position_xgb — NO_TRADE

**Score:** 0.592 vs policy min 0.55 · **Close:** 565 · **ATR14:** 47.5 · **Volume ratio 20D:** 0.82 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 540–570, entry trigger **570**, stop **515**, risk 55 points (9.65%).

**Targets:** TP1 **635** (1.18R), TP2 **665** (1.73R), TP3 **705** (2.45R). Recommended base-case RR: **1.73R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 565: zone 540–570 uses ATR14 47.5 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 570 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 515 is capped by max risk 9.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 635 (1.18R), TP2 665 (1.73R), TP3 705 (2.45R). Targets are ATR/structure capped for hold_days=1. ATR14=47.5, resistance_5/10/20/60=635/680/830/1,155. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 9.65% exceeds max strategy risk 9.00%; TP1 reward/risk 1.18R is below strategy minimum 1.35R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## PSDN — market_maker_silent_accum_defensive — NO_TRADE

**Score:** 0.565 vs policy min 0.55 · **Close:** 113 · **ATR14:** 17.9 · **Volume ratio 20D:** 2.20 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 106–117, entry trigger **117**, stop **108**, risk 9 points (7.69%).

**Targets:** TP1 **128** (1.22R), TP2 **133** (1.78R), TP3 **139** (2.44R). Recommended base-case RR: **1.78R**.

**Why entry:** Hybrid entry uses close 113 and ATR14 17.9: buy zone 106–117. Entry is valid only if price can trade/hold around 117 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 108 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 128 (1.22R), TP2 133 (1.78R), TP3 139 (2.44R). Targets are ATR/structure capped for hold_days=1. ATR14=17.9, resistance_5/10/20/60=128/154/195/260. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.69% exceeds max strategy risk 7.50%; TP1 reward/risk 1.22R is below strategy minimum 1.25R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Defensive accumulation. Prefer retest and clean broker flow.

---

## PBSA — market_maker_silent_accum_defensive — NO_TRADE

**Score:** 0.563 vs policy min 0.55 · **Close:** 705 · **ATR14:** 114.3 · **Volume ratio 20D:** 1.43 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 665–730, entry trigger **730**, stop **675**, risk 55 points (7.53%).

**Targets:** TP1 **825** (1.73R), TP2 **855** (2.27R), TP3 **865** (2.45R). Recommended base-case RR: **2.27R**.

**Why entry:** Hybrid entry uses close 705 and ATR14 114.3: buy zone 665–730. Entry is valid only if price can trade/hold around 730 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 675 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 825 (1.73R), TP2 855 (2.27R), TP3 865 (2.45R). Targets are ATR/structure capped for hold_days=1. ATR14=114.3, resistance_5/10/20/60=825/940/985/1,345. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.53% exceeds max strategy risk 7.50%

**Risk flags:** OK

**Strategy risk note:** Defensive accumulation. Prefer retest and clean broker flow.

---

## PSKT — market_maker_silent_accum_defensive — NO_TRADE

**Score:** 0.551 vs policy min 0.55 · **Close:** 185 · **ATR14:** 28.3 · **Volume ratio 20D:** 2.08 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 175–191, entry trigger **191**, stop **176**, risk 15 points (7.85%).

**Targets:** TP1 **220** (1.93R), TP2 **230** (2.60R), TP3 **238** (3.13R). Recommended base-case RR: **2.60R**.

**Why entry:** Hybrid entry uses close 185 and ATR14 28.3: buy zone 175–191. Entry is valid only if price can trade/hold around 191 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 176 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 220 (1.93R), TP2 230 (2.60R), TP3 238 (3.13R). Targets are ATR/structure capped for hold_days=1. ATR14=28.3, resistance_5/10/20/60=230/234/270/316. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.85% exceeds max strategy risk 7.50%; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Defensive accumulation. Prefer retest and clean broker flow.

---

## BMTR — market_maker_silent_accum_defensive — NO_TRADE

**Score:** 0.541 vs policy min 0.55 · **Close:** 109 · **ATR14:** 7.6 · **Volume ratio 20D:** 1.84 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 106–111, entry trigger **111**, stop **102**, risk 9 points (8.11%).

**Targets:** TP1 **119** (0.89R), TP2 **125** (1.56R), TP3 **133** (2.44R). Recommended base-case RR: **1.56R**.

**Why entry:** Hybrid entry uses close 109 and ATR14 7.6: buy zone 106–111. Entry is valid only if price can trade/hold around 111 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 102 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 119 (0.89R), TP2 125 (1.56R), TP3 133 (2.44R). Targets are ATR/structure capped for hold_days=1. ATR14=7.6, resistance_5/10/20/60=126/132/167/204. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.11% exceeds max strategy risk 7.50%; score 0.541 below policy min_score 0.55; TP1 reward/risk 0.89R is below strategy minimum 1.25R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Defensive accumulation. Prefer retest and clean broker flow.

---

## OMED — market_maker_silent_accum_defensive — NO_TRADE

**Score:** 0.537 vs policy min 0.55 · **Close:** 194 · **ATR14:** 18.2 · **Volume ratio 20D:** 0.69 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 187–198, entry trigger **198**, stop **183**, risk 15 points (7.58%).

**Targets:** TP1 **214** (1.07R), TP2 **224** (1.73R), TP3 **234** (2.40R). Recommended base-case RR: **1.73R**.

**Why entry:** Hybrid entry uses close 194 and ATR14 18.2: buy zone 187–198. Entry is valid only if price can trade/hold around 198 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 183 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 214 (1.07R), TP2 224 (1.73R), TP3 234 (2.40R). Targets are ATR/structure capped for hold_days=1. ATR14=18.2, resistance_5/10/20/60=214/250/310/318. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.58% exceeds max strategy risk 7.50%; score 0.537 below policy min_score 0.55; TP1 reward/risk 1.07R is below strategy minimum 1.25R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Defensive accumulation. Prefer retest and clean broker flow.

---

## DEWA — momentum_5d_hgb_defensive — NO_TRADE

**Score:** 0.437 vs policy min 0.55 · **Close:** 280 · **ATR14:** 46.0 · **Volume ratio 20D:** 1.50 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 270–400, entry trigger **400**, stop **372**, risk 28 points (7.00%).

**Targets:** TP1 **428** (1.00R), TP2 **448** (1.71R), TP3 **520** (4.29R). Recommended base-case RR: **1.71R**.

**Why entry:** Entry trigger 400 is set above recent resistance 398 plus one IDX tick. This requires confirmation instead of buying blindly at close 280. Entry is valid only if price can trade/hold around 400 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 372 is capped by max risk 7.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 428 (1.00R), TP2 448 (1.71R), TP3 520 (4.29R). Targets are ATR/structure capped for hold_days=1. ATR14=46.0, resistance_5/10/20/60=340/398/535/595. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 42.86% > max 8.00%; score 0.437 below policy min_score 0.55; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Selective high-liquidity 5D momentum sleeve.

---

## EMTK — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.422 vs policy min 0.60 · **Close:** 535 · **ATR14:** 49.0 · **Volume ratio 20D:** 1.61 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 525–680, entry trigger **680**, stop **615**, risk 65 points (9.56%).

**Targets:** TP1 **745** (1.00R), TP2 **830** (2.31R), TP3 **840** (2.46R). Recommended base-case RR: **2.31R**.

**Why entry:** Entry trigger 680 is set above recent resistance 675 plus one IDX tick. This requires confirmation instead of buying blindly at close 535. Entry is valid only if price can trade/hold around 680 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 615 uses 1.30×ATR14 volatility cap. Thesis invalidates if the move reverses beyond normal volatility. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 745 (1.00R), TP2 830 (2.31R), TP3 840 (2.46R). Targets are ATR/structure capped for hold_days=2. ATR14=49.0, resistance_5/10/20/60=615/675/830/975. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 27.10% > max 15.00%; score 0.422 below policy min_score 0.60; TP1 reward/risk 1.00R is below strategy minimum 1.40R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## SOFA — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.422 vs policy min 0.60 · **Close:** 258 · **ATR14:** 43.0 · **Volume ratio 20D:** 2.28 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 248–448, entry trigger **448**, stop **402**, risk 46 points (10.27%).

**Targets:** TP1 **494** (1.00R), TP2 **580** (2.87R), TP3 **605** (3.41R). Recommended base-case RR: **2.87R**.

**Why entry:** Entry trigger 448 is set above recent resistance 446 plus one IDX tick. This requires confirmation instead of buying blindly at close 258. Entry is valid only if price can trade/hold around 448 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 402 is capped by max risk 10.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 494 (1.00R), TP2 580 (2.87R), TP3 605 (3.41R). Targets are ATR/structure capped for hold_days=2. ATR14=43.0, resistance_5/10/20/60=362/446/446/580. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 73.64% > max 15.00%; entry-to-stop risk 10.27% exceeds max strategy risk 10.00%; score 0.422 below policy min_score 0.60; TP1 reward/risk 1.00R is below strategy minimum 1.40R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## UVCR — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.421 vs policy min 0.60 · **Close:** 133 · **ATR14:** 17.9 · **Volume ratio 20D:** 2.51 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 129–252, entry trigger **252**, stop **228**, risk 24 points (9.52%).

**Targets:** TP1 **276** (1.00R), TP2 **294** (1.75R), TP3 **310** (2.42R). Recommended base-case RR: **1.75R**.

**Why entry:** Entry trigger 252 is set above recent resistance 250 plus one IDX tick. This requires confirmation instead of buying blindly at close 133. Entry is valid only if price can trade/hold around 252 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 228 uses 1.30×ATR14 volatility cap. Thesis invalidates if the move reverses beyond normal volatility. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 276 (1.00R), TP2 294 (1.75R), TP3 310 (2.42R). Targets are ATR/structure capped for hold_days=2. ATR14=17.9, resistance_5/10/20/60=242/250/250/250. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 89.47% > max 15.00%; score 0.421 below policy min_score 0.60; TP1 reward/risk 1.00R is below strategy minimum 1.40R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## NICL — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.419 vs policy min 0.60 · **Close:** 505 · **ATR14:** 70.1 · **Volume ratio 20D:** 1.72 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 490–635, entry trigger **635**, stop **570**, risk 65 points (10.24%).

**Targets:** TP1 **700** (1.00R), TP2 **865** (3.54R), TP3 **875** (3.69R). Recommended base-case RR: **3.54R**.

**Why entry:** Entry trigger 635 is set above recent resistance 630 plus one IDX tick. This requires confirmation instead of buying blindly at close 505. Entry is valid only if price can trade/hold around 635 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 570 is capped by max risk 10.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 700 (1.00R), TP2 865 (3.54R), TP3 875 (3.69R). Targets are ATR/structure capped for hold_days=2. ATR14=70.1, resistance_5/10/20/60=630/630/875/1,100. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 25.74% > max 15.00%; entry-to-stop risk 10.24% exceeds max strategy risk 10.00%; score 0.419 below policy min_score 0.60; TP1 reward/risk 1.00R is below strategy minimum 1.40R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## SSMS — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.413 vs policy min 0.60 · **Close:** 740 · **ATR14:** 88.9 · **Volume ratio 20D:** 0.98 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 720–915, entry trigger **915**, stop **820**, risk 95 points (10.38%).

**Targets:** TP1 **1,010** (1.00R), TP2 **1,080** (1.74R), TP3 **1,145** (2.42R). Recommended base-case RR: **1.74R**.

**Why entry:** Entry trigger 915 is set above recent resistance 910 plus one IDX tick. This requires confirmation instead of buying blindly at close 740. Entry is valid only if price can trade/hold around 915 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 820 is capped by max risk 10.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,010 (1.00R), TP2 1,080 (1.74R), TP3 1,145 (2.42R). Targets are ATR/structure capped for hold_days=2. ATR14=88.9, resistance_5/10/20/60=820/910/1,430/1,570. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 23.65% > max 15.00%; entry-to-stop risk 10.38% exceeds max strategy risk 10.00%; score 0.413 below policy min_score 0.60; TP1 reward/risk 1.00R is below strategy minimum 1.40R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## UVCR — momentum_5d_hgb_defensive — NO_TRADE

**Score:** 0.412 vs policy min 0.55 · **Close:** 133 · **ATR14:** 17.9 · **Volume ratio 20D:** 2.51 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 129–252, entry trigger **252**, stop **234**, risk 18 points (7.14%).

**Targets:** TP1 **270** (1.00R), TP2 **284** (1.78R), TP3 **296** (2.44R). Recommended base-case RR: **1.78R**.

**Why entry:** Entry trigger 252 is set above recent resistance 250 plus one IDX tick. This requires confirmation instead of buying blindly at close 133. Entry is valid only if price can trade/hold around 252 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 234 is capped by max risk 7.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 270 (1.00R), TP2 284 (1.78R), TP3 296 (2.44R). Targets are ATR/structure capped for hold_days=1. ATR14=17.9, resistance_5/10/20/60=242/250/250/250. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 89.47% > max 8.00%; entry-to-stop risk 7.14% exceeds max strategy risk 7.00%; score 0.412 below policy min_score 0.55; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Selective high-liquidity 5D momentum sleeve.

---

## BUMI — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.406 vs policy min 0.60 · **Close:** 146 · **ATR14:** 17.9 · **Volume ratio 20D:** 1.29 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 142–187, entry trigger **187**, stop **168**, risk 19 points (10.16%).

**Targets:** TP1 **206** (1.00R), TP2 **238** (2.68R), TP3 **248** (3.21R). Recommended base-case RR: **2.68R**.

**Why entry:** Entry trigger 187 is set above recent resistance 186 plus one IDX tick. This requires confirmation instead of buying blindly at close 146. Entry is valid only if price can trade/hold around 187 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 168 is capped by max risk 10.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 206 (1.00R), TP2 238 (2.68R), TP3 248 (3.21R). Targets are ATR/structure capped for hold_days=2. ATR14=17.9, resistance_5/10/20/60=164/186/238/268. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 28.08% > max 15.00%; entry-to-stop risk 10.16% exceeds max strategy risk 10.00%; score 0.406 below policy min_score 0.60; TP1 reward/risk 1.00R is below strategy minimum 1.40R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## NSSS — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.402 vs policy min 0.60 · **Close:** 386 · **ATR14:** 59.1 · **Volume ratio 20D:** 0.61 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 374–515, entry trigger **515**, stop **462**, risk 53 points (10.29%).

**Targets:** TP1 **570** (1.04R), TP2 **610** (1.79R), TP3 **645** (2.45R). Recommended base-case RR: **1.79R**.

**Why entry:** Entry trigger 515 is set above recent resistance 510 plus one IDX tick. This requires confirmation instead of buying blindly at close 386. Entry is valid only if price can trade/hold around 515 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 462 is capped by max risk 10.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 570 (1.04R), TP2 610 (1.79R), TP3 645 (2.45R). Targets are ATR/structure capped for hold_days=2. ATR14=59.1, resistance_5/10/20/60=468/510/850/1,110. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 33.42% > max 15.00%; entry-to-stop risk 10.29% exceeds max strategy risk 10.00%; score 0.402 below policy min_score 0.60; TP1 reward/risk 1.04R is below strategy minimum 1.40R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## TOWR — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.401 vs policy min 0.60 · **Close:** 322 · **ATR14:** 20.7 · **Volume ratio 20D:** 2.04 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 316–410, entry trigger **410**, stop **382**, risk 28 points (6.83%).

**Targets:** TP1 **438** (1.00R), TP2 **478** (2.43R), TP3 **490** (2.86R). Recommended base-case RR: **2.43R**.

**Why entry:** Entry trigger 410 is set above recent resistance 408 plus one IDX tick. This requires confirmation instead of buying blindly at close 322. Entry is valid only if price can trade/hold around 410 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 382 uses 1.30×ATR14 volatility cap. Thesis invalidates if the move reverses beyond normal volatility. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 438 (1.00R), TP2 478 (2.43R), TP3 490 (2.86R). Targets are ATR/structure capped for hold_days=2. ATR14=20.7, resistance_5/10/20/60=386/408/490/520. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 27.33% > max 15.00%; score 0.401 below policy min_score 0.60; TP1 reward/risk 1.00R is below strategy minimum 1.40R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## SOCI — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.401 vs policy min 0.60 · **Close:** 296 · **ATR14:** 40.1 · **Volume ratio 20D:** 0.86 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 286–418, entry trigger **418**, stop **376**, risk 42 points (10.05%).

**Targets:** TP1 **460** (1.00R), TP2 **540** (2.90R), TP3 **565** (3.50R). Recommended base-case RR: **2.90R**.

**Why entry:** Entry trigger 418 is set above recent resistance 416 plus one IDX tick. This requires confirmation instead of buying blindly at close 296. Entry is valid only if price can trade/hold around 418 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 376 is capped by max risk 10.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 460 (1.00R), TP2 540 (2.90R), TP3 565 (3.50R). Targets are ATR/structure capped for hold_days=2. ATR14=40.1, resistance_5/10/20/60=396/416/540/735. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 41.22% > max 15.00%; entry-to-stop risk 10.05% exceeds max strategy risk 10.00%; score 0.401 below policy min_score 0.60; TP1 reward/risk 1.00R is below strategy minimum 1.40R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## ARTO — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.397 vs policy min 0.60 · **Close:** 940 · **ATR14:** 83.2 · **Volume ratio 20D:** 2.57 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 920–1,190, entry trigger **1,190**, stop **1,080**, risk 110 points (9.24%).

**Targets:** TP1 **1,300** (1.00R), TP2 **1,380** (1.73R), TP3 **1,455** (2.41R). Recommended base-case RR: **1.73R**.

**Why entry:** Entry trigger 1,190 is set above recent resistance 1,185 plus one IDX tick. This requires confirmation instead of buying blindly at close 940. Entry is valid only if price can trade/hold around 1,190 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 1,080 uses 1.30×ATR14 volatility cap. Thesis invalidates if the move reverses beyond normal volatility. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,300 (1.00R), TP2 1,380 (1.73R), TP3 1,455 (2.41R). Targets are ATR/structure capped for hold_days=2. ATR14=83.2, resistance_5/10/20/60=1,185/1,185/1,290/1,590. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 26.60% > max 15.00%; score 0.397 below policy min_score 0.60; TP1 reward/risk 1.00R is below strategy minimum 1.40R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## BMTR — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.392 vs policy min 0.60 · **Close:** 109 · **ATR14:** 7.6 · **Volume ratio 20D:** 1.84 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 107–133, entry trigger **133**, stop **123**, risk 10 points (7.52%).

**Targets:** TP1 **143** (1.00R), TP2 **150** (1.70R), TP3 **167** (3.40R). Recommended base-case RR: **1.70R**.

**Why entry:** Entry trigger 133 is set above recent resistance 132 plus one IDX tick. This requires confirmation instead of buying blindly at close 109. Entry is valid only if price can trade/hold around 133 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 123 uses 1.30×ATR14 volatility cap. Thesis invalidates if the move reverses beyond normal volatility. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 143 (1.00R), TP2 150 (1.70R), TP3 167 (3.40R). Targets are ATR/structure capped for hold_days=2. ATR14=7.6, resistance_5/10/20/60=126/132/167/204. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 22.02% > max 15.00%; score 0.392 below policy min_score 0.60; TP1 reward/risk 1.00R is below strategy minimum 1.40R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## CYBR — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.390 vs policy min 0.60 · **Close:** 540 · **ATR14:** 40.4 · **Volume ratio 20D:** 1.70 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 530–625, entry trigger **625**, stop **570**, risk 55 points (8.80%).

**Targets:** TP1 **680** (1.00R), TP2 **720** (1.73R), TP3 **760** (2.45R). Recommended base-case RR: **1.73R**.

**Why entry:** Entry trigger 625 is set above recent resistance 620 plus one IDX tick. This requires confirmation instead of buying blindly at close 540. Entry is valid only if price can trade/hold around 625 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 570 uses 1.30×ATR14 volatility cap. Thesis invalidates if the move reverses beyond normal volatility. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 680 (1.00R), TP2 720 (1.73R), TP3 760 (2.45R). Targets are ATR/structure capped for hold_days=2. ATR14=40.4, resistance_5/10/20/60=610/620/1,325/1,590. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 15.74% > max 15.00%; score 0.390 below policy min_score 0.60; TP1 reward/risk 1.00R is below strategy minimum 1.40R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## BULL — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.390 vs policy min 0.60 · **Close:** 306 · **ATR14:** 46.0 · **Volume ratio 20D:** 1.22 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 296–430, entry trigger **430**, stop **386**, risk 44 points (10.23%).

**Targets:** TP1 **474** (1.00R), TP2 **545** (2.61R), TP3 **570** (3.18R). Recommended base-case RR: **2.61R**.

**Why entry:** Entry trigger 430 is set above recent resistance 428 plus one IDX tick. This requires confirmation instead of buying blindly at close 306. Entry is valid only if price can trade/hold around 430 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 386 is capped by max risk 10.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 474 (1.00R), TP2 545 (2.61R), TP3 570 (3.18R). Targets are ATR/structure capped for hold_days=2. ATR14=46.0, resistance_5/10/20/60=388/428/545/610. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 40.52% > max 15.00%; entry-to-stop risk 10.23% exceeds max strategy risk 10.00%; score 0.390 below policy min_score 0.60; TP1 reward/risk 1.00R is below strategy minimum 1.40R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## KIJA — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.390 vs policy min 0.60 · **Close:** 114 · **ATR14:** 10.8 · **Volume ratio 20D:** 1.81 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 111–134, entry trigger **134**, stop **120**, risk 14 points (10.45%).

**Targets:** TP1 **148** (1.00R), TP2 **158** (1.71R), TP3 **184** (3.57R). Recommended base-case RR: **1.71R**.

**Why entry:** Entry trigger 134 is set above recent resistance 133 plus one IDX tick. This requires confirmation instead of buying blindly at close 114. Entry is valid only if price can trade/hold around 134 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 120 is capped by max risk 10.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 148 (1.00R), TP2 158 (1.71R), TP3 184 (3.57R). Targets are ATR/structure capped for hold_days=2. ATR14=10.8, resistance_5/10/20/60=123/133/184/220. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 17.54% > max 15.00%; entry-to-stop risk 10.45% exceeds max strategy risk 10.00%; score 0.390 below policy min_score 0.60; TP1 reward/risk 1.00R is below strategy minimum 1.40R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## CTTH — ara_candidate — NO_TRADE

**Score:** 0.319 vs policy min 0.50 · **Close:** 129 · **ATR14:** 70.9 · **Volume ratio 20D:** 5.12 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 118–183, entry trigger **183**, stop **164**, risk 19 points (10.38%).

**Targets:** TP1 **220** (1.95R), TP2 **230** (2.47R), TP3 **240** (3.00R). Recommended base-case RR: **2.47R**.

**Why entry:** Entry trigger 183 is set above recent resistance 182 plus one IDX tick. This requires confirmation instead of buying blindly at close 129. Entry is valid only if price can trade/hold around 183 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 164 is capped by max risk 10.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 220 (1.95R), TP2 230 (2.47R), TP3 240 (3.00R). Targets are ATR/structure capped for hold_days=1. ATR14=70.9, resistance_5/10/20/60=157/182/216/216. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 41.86% > max 12.00%; entry-to-stop risk 10.38% exceeds max strategy risk 10.00%; score 0.319 below policy min_score 0.50; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** High drawdown tactical setup. Use as execution only if confirmation is strong and liquidity is clean.

---
