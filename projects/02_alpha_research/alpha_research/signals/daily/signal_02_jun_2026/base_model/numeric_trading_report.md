# Numeric Trading Desk Report — 2026-05-29

This report is generated from live model scores, selected signal policy, canonical OHLCV, ATR, support/resistance, liquidity, and broker-flow diagnostics. It is not a simple BUY/SELL list; each plan is conditional on execution behaviour.

## Summary

| Plan quality | Count |
|---|---:|
| ACTIONABLE | 5 |
| CONDITIONAL | 14 |
| WATCHLIST_ONLY | 6 |
| NO_TRADE | 31 |

## SSMS — swing_hgb_defensive — ACTIONABLE

**Score:** 0.702 vs policy min 0.50 · **Close:** 700 · **ATR14:** 86.8 · **Volume ratio 20D:** 7.23 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 660–710, entry trigger **710**, stop **690**, risk 20 points (2.82%).

**Targets:** TP1 **755** (2.25R), TP2 **765** (2.75R), TP3 **930** (11.00R). Recommended base-case RR: **2.75R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 700: zone 660–710 uses ATR14 86.8 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 710 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 690 is placed below support structure (695 / 695). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 755 (2.25R), TP2 765 (2.75R), TP3 930 (11.00R). Targets are ATR/structure capped for hold_days=1. ATR14=86.8, resistance_5/10/20/60=950/1,420/1,470/1,800. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## BSDE — swing_hgb_defensive — ACTIONABLE

**Score:** 0.699 vs policy min 0.50 · **Close:** 630 · **ATR14:** 33.6 · **Volume ratio 20D:** 6.00 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 610–635, entry trigger **635**, stop **620**, risk 15 points (2.36%).

**Targets:** TP1 **655** (1.33R), TP2 **700** (4.33R), TP3 **720** (5.67R). Recommended base-case RR: **4.33R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 630: zone 610–635 uses ATR14 33.6 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 635 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 620 is placed below support structure (625 / 625). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 655 (1.33R), TP2 700 (4.33R), TP3 720 (5.67R). Targets are ATR/structure capped for hold_days=1. ATR14=33.6, resistance_5/10/20/60=720/780/835/910. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## FUJI — swing_hgb_defensive — ACTIONABLE

**Score:** 0.672 vs policy min 0.50 · **Close:** 274 · **ATR14:** 20.9 · **Volume ratio 20D:** 0.73 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 264–278, entry trigger **278**, stop **262**, risk 16 points (5.76%).

**Targets:** TP1 **300** (1.38R), TP2 **306** (1.75R), TP3 **318** (2.50R). Recommended base-case RR: **1.75R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 274: zone 264–278 uses ATR14 20.9 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 278 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 262 is placed below support structure (264 / 264). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 300 (1.38R), TP2 306 (1.75R), TP3 318 (2.50R). Targets are ATR/structure capped for hold_days=1. ATR14=20.9, resistance_5/10/20/60=306/336/378/505. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## BANK — swing_hgb_defensive — ACTIONABLE

**Score:** 0.670 vs policy min 0.50 · **Close:** 238 · **ATR14:** 56.5 · **Volume ratio 20D:** 4.52 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 218–244, entry trigger **244**, stop **236**, risk 8 points (3.28%).

**Targets:** TP1 **274** (3.75R), TP2 **346** (12.75R), TP3 **350** (13.25R). Recommended base-case RR: **12.75R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 238: zone 218–244 uses ATR14 56.5 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 244 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 236 is placed below support structure (238 / 238). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 274 (3.75R), TP2 346 (12.75R), TP3 350 (13.25R). Targets are ATR/structure capped for hold_days=1. ATR14=56.5, resistance_5/10/20/60=350/630/640/640. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## FUJI — position_xgb — ACTIONABLE

**Score:** 0.572 vs policy min 0.55 · **Close:** 274 · **ATR14:** 20.9 · **Volume ratio 20D:** 0.73 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 264–278, entry trigger **278**, stop **262**, risk 16 points (5.76%).

**Targets:** TP1 **306** (1.75R), TP2 **314** (2.25R), TP3 **318** (2.50R). Recommended base-case RR: **2.25R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 274: zone 264–278 uses ATR14 20.9 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 278 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 262 is placed below support structure (264 / 264). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 306 (1.75R), TP2 314 (2.25R), TP3 318 (2.50R). Targets are ATR/structure capped for hold_days=1. ATR14=20.9, resistance_5/10/20/60=306/336/378/505. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## GTSI — swing_hgb_defensive — CONDITIONAL

**Score:** 0.709 vs policy min 0.50 · **Close:** 158 · **ATR14:** 19.9 · **Volume ratio 20D:** 0.45 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 149–160, entry trigger **160**, stop **149**, risk 11 points (6.88%).

**Targets:** TP1 **171** (1.00R), TP2 **189** (2.64R), TP3 **195** (3.18R). Recommended base-case RR: **2.64R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 158: zone 149–160 uses ATR14 19.9 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 160 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 149 is placed below support structure (150 / 150). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 171 (1.00R), TP2 189 (2.64R), TP3 195 (3.18R). Targets are ATR/structure capped for hold_days=1. ATR14=19.9, resistance_5/10/20/60=189/238/274/350. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.25R; volume ratio 0.45 below required 0.60

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## KIJA — swing_hgb_defensive — CONDITIONAL

**Score:** 0.704 vs policy min 0.50 · **Close:** 124 · **ATR14:** 10.0 · **Volume ratio 20D:** 0.48 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 119–125, entry trigger **125**, stop **117**, risk 8 points (6.40%).

**Targets:** TP1 **133** (1.00R), TP2 **139** (1.75R), TP3 **145** (2.50R). Recommended base-case RR: **1.75R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 124: zone 119–125 uses ATR14 10.0 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 125 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 117 is placed below support structure (118 / 118). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 133 (1.00R), TP2 139 (1.75R), TP3 145 (2.50R). Targets are ATR/structure capped for hold_days=1. ATR14=10.0, resistance_5/10/20/60=159/182/220/240. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.25R; volume ratio 0.48 below required 0.60

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## STAA — swing_hgb_defensive — CONDITIONAL

**Score:** 0.689 vs policy min 0.50 · **Close:** 1,000 · **ATR14:** 53.6 · **Volume ratio 20D:** 1.53 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 975–1,010, entry trigger **1,010**, stop **970**, risk 40 points (3.96%).

**Targets:** TP1 **1,050** (1.00R), TP2 **1,110** (2.50R), TP3 **1,145** (3.38R). Recommended base-case RR: **2.50R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 1,000: zone 975–1,010 uses ATR14 53.6 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 1,010 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 970 is placed below support structure (975 / 975). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,050 (1.00R), TP2 1,110 (2.50R), TP3 1,145 (3.38R). Targets are ATR/structure capped for hold_days=1. ATR14=53.6, resistance_5/10/20/60=1,145/1,240/1,385/1,385. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.25R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## HRUM — swing_hgb_defensive — CONDITIONAL

**Score:** 0.687 vs policy min 0.50 · **Close:** 790 · **ATR14:** 55.7 · **Volume ratio 20D:** 0.63 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 760–800, entry trigger **800**, stop **740**, risk 60 points (7.50%).

**Targets:** TP1 **860** (1.00R), TP2 **905** (1.75R), TP3 **945** (2.42R). Recommended base-case RR: **1.75R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 790: zone 760–800 uses ATR14 55.7 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 800 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 740 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 860 (1.00R), TP2 905 (1.75R), TP3 945 (2.42R). Targets are ATR/structure capped for hold_days=1. ATR14=55.7, resistance_5/10/20/60=830/995/1,030/1,270. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## FORE — swing_hgb_defensive — CONDITIONAL

**Score:** 0.671 vs policy min 0.50 · **Close:** 705 · **ATR14:** 82.5 · **Volume ratio 20D:** 0.96 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 665–715, entry trigger **715**, stop **680**, risk 35 points (4.90%).

**Targets:** TP1 **760** (1.29R), TP2 **775** (1.71R), TP3 **800** (2.43R). Recommended base-case RR: **1.71R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 705: zone 665–715 uses ATR14 82.5 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 715 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 680 is placed below support structure (685 / 685). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 760 (1.29R), TP2 775 (1.71R), TP3 800 (2.43R). Targets are ATR/structure capped for hold_days=1. ATR14=82.5, resistance_5/10/20/60=1,005/1,035/1,050/1,050. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## KIJA — position_xgb — CONDITIONAL

**Score:** 0.576 vs policy min 0.55 · **Close:** 124 · **ATR14:** 10.0 · **Volume ratio 20D:** 0.48 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 119–125, entry trigger **125**, stop **117**, risk 8 points (6.40%).

**Targets:** TP1 **133** (1.00R), TP2 **139** (1.75R), TP3 **159** (4.25R). Recommended base-case RR: **1.75R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 124: zone 119–125 uses ATR14 10.0 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 125 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 117 is placed below support structure (118 / 118). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 133 (1.00R), TP2 139 (1.75R), TP3 159 (4.25R). Targets are ATR/structure capped for hold_days=1. ATR14=10.0, resistance_5/10/20/60=159/182/220/240. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.35R; volume ratio 0.48 below required 0.60

**Risk flags:** OK

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## STAA — position_xgb — CONDITIONAL

**Score:** 0.576 vs policy min 0.55 · **Close:** 1,000 · **ATR14:** 53.6 · **Volume ratio 20D:** 1.53 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 975–1,010, entry trigger **1,010**, stop **970**, risk 40 points (3.96%).

**Targets:** TP1 **1,050** (1.00R), TP2 **1,140** (3.25R), TP3 **1,145** (3.38R). Recommended base-case RR: **3.25R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 1,000: zone 975–1,010 uses ATR14 53.6 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 1,010 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 970 is placed below support structure (975 / 975). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,050 (1.00R), TP2 1,140 (3.25R), TP3 1,145 (3.38R). Targets are ATR/structure capped for hold_days=1. ATR14=53.6, resistance_5/10/20/60=1,145/1,240/1,385/1,385. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.35R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## BSDE — position_xgb — CONDITIONAL

**Score:** 0.574 vs policy min 0.55 · **Close:** 630 · **ATR14:** 33.6 · **Volume ratio 20D:** 6.00 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 610–635, entry trigger **635**, stop **620**, risk 15 points (2.36%).

**Targets:** TP1 **655** (1.33R), TP2 **720** (5.67R), TP3 **730** (6.33R). Recommended base-case RR: **5.67R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 630: zone 610–635 uses ATR14 33.6 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 635 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 620 is placed below support structure (625 / 625). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 655 (1.33R), TP2 720 (5.67R), TP3 730 (6.33R). Targets are ATR/structure capped for hold_days=1. ATR14=33.6, resistance_5/10/20/60=720/780/835/910. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.33R is below strategy minimum 1.35R

**Risk flags:** OK

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## ELSA — position_xgb — CONDITIONAL

**Score:** 0.574 vs policy min 0.55 · **Close:** 610 · **ATR14:** 44.6 · **Volume ratio 20D:** 0.57 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 585–615, entry trigger **615**, stop **595**, risk 20 points (3.25%).

**Targets:** TP1 **680** (3.25R), TP2 **695** (4.00R), TP3 **705** (4.50R). Recommended base-case RR: **4.00R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 610: zone 585–615 uses ATR14 44.6 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 615 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 595 is placed below support structure (600 / 600). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 680 (3.25R), TP2 695 (4.00R), TP3 705 (4.50R). Targets are ATR/structure capped for hold_days=1. ATR14=44.6, resistance_5/10/20/60=695/785/845/1,050. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** volume ratio 0.57 below required 0.60

**Risk flags:** OK

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## RALS — position_xgb — CONDITIONAL

**Score:** 0.573 vs policy min 0.55 · **Close:** 380 · **ATR14:** 12.9 · **Volume ratio 20D:** 2.04 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 374–382, entry trigger **382**, stop **376**, risk 6 points (1.57%).

**Targets:** TP1 **390** (1.33R), TP2 **394** (2.00R), TP3 **398** (2.67R). Recommended base-case RR: **2.00R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 380: zone 374–382 uses ATR14 12.9 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 382 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 376 is placed below support structure (378 / 378). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 390 (1.33R), TP2 394 (2.00R), TP3 398 (2.67R). Targets are ATR/structure capped for hold_days=1. ATR14=12.9, resistance_5/10/20/60=454/464/464/530. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.33R is below strategy minimum 1.35R

**Risk flags:** OK

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## GTSI — position_xgb — CONDITIONAL

**Score:** 0.573 vs policy min 0.55 · **Close:** 158 · **ATR14:** 19.9 · **Volume ratio 20D:** 0.45 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 149–160, entry trigger **160**, stop **149**, risk 11 points (6.88%).

**Targets:** TP1 **188** (2.55R), TP2 **189** (2.64R), TP3 **195** (3.18R). Recommended base-case RR: **2.64R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 158: zone 149–160 uses ATR14 19.9 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 160 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 149 is placed below support structure (150 / 150). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 188 (2.55R), TP2 189 (2.64R), TP3 195 (3.18R). Targets are ATR/structure capped for hold_days=1. ATR14=19.9, resistance_5/10/20/60=189/238/274/350. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** volume ratio 0.45 below required 0.60

**Risk flags:** OK

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## NSSS — position_xgb — CONDITIONAL

**Score:** 0.568 vs policy min 0.55 · **Close:** 462 · **ATR14:** 69.9 · **Volume ratio 20D:** 0.30 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 430–470, entry trigger **470**, stop **434**, risk 36 points (7.66%).

**Targets:** TP1 **570** (2.78R), TP2 **575** (2.92R), TP3 **595** (3.47R). Recommended base-case RR: **2.92R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 462: zone 430–470 uses ATR14 69.9 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 470 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 434 is placed below support structure (436 / 436). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 570 (2.78R), TP2 575 (2.92R), TP3 595 (3.47R). Targets are ATR/structure capped for hold_days=1. ATR14=69.9, resistance_5/10/20/60=575/850/1,060/1,300. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** volume ratio 0.30 below required 0.60

**Risk flags:** OK

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## DEWA — position_xgb — CONDITIONAL

**Score:** 0.565 vs policy min 0.55 · **Close:** 334 · **ATR14:** 42.3 · **Volume ratio 20D:** 0.63 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 314–340, entry trigger **340**, stop **318**, risk 22 points (6.47%).

**Targets:** TP1 **398** (2.64R), TP2 **410** (3.18R), TP3 **422** (3.73R). Recommended base-case RR: **3.18R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 334: zone 314–340 uses ATR14 42.3 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 340 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 318 is placed below support structure (320 / 320). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 398 (2.64R), TP2 410 (3.18R), TP3 422 (3.73R). Targets are ATR/structure capped for hold_days=1. ATR14=42.3, resistance_5/10/20/60=398/535/570/655. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## FORE — position_xgb — CONDITIONAL

**Score:** 0.564 vs policy min 0.55 · **Close:** 705 · **ATR14:** 82.5 · **Volume ratio 20D:** 0.96 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 665–715, entry trigger **715**, stop **680**, risk 35 points (4.90%).

**Targets:** TP1 **760** (1.29R), TP2 **775** (1.71R), TP3 **1,005** (8.29R). Recommended base-case RR: **1.71R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 705: zone 665–715 uses ATR14 82.5 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 715 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 680 is placed below support structure (685 / 685). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 760 (1.29R), TP2 775 (1.71R), TP3 1,005 (8.29R). Targets are ATR/structure capped for hold_days=1. ATR14=82.5, resistance_5/10/20/60=1,005/1,035/1,050/1,050. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.29R is below strategy minimum 1.35R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## APIC — market_maker_silent_accum_defensive — WATCHLIST_ONLY

**Score:** 0.523 vs policy min 0.55 · **Close:** 980 · **ATR14:** 305.7 · **Volume ratio 20D:** 6.07 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 870–1,045, entry trigger **1,045**, stop **975**, risk 70 points (6.70%).

**Targets:** TP1 **1,200** (2.21R), TP2 **1,235** (2.71R), TP3 **1,725** (9.71R). Recommended base-case RR: **2.71R**.

**Why entry:** Hybrid entry uses close 980 and ATR14 305.7: buy zone 870–1,045. Entry is valid only if price can trade/hold around 1,045 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 975 is placed below support structure (980 / 980). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,200 (2.21R), TP2 1,235 (2.71R), TP3 1,725 (9.71R). Targets are ATR/structure capped for hold_days=1. ATR14=305.7, resistance_5/10/20/60=1,725/2,090/2,410/2,410. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** score 0.523 below policy min_score 0.55

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Defensive accumulation. Prefer retest and clean broker flow.

---

## FUJI — market_maker_silent_accum_defensive — WATCHLIST_ONLY

**Score:** 0.465 vs policy min 0.55 · **Close:** 274 · **ATR14:** 20.9 · **Volume ratio 20D:** 0.73 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 266–280, entry trigger **280**, stop **262**, risk 18 points (6.43%).

**Targets:** TP1 **302** (1.22R), TP2 **312** (1.78R), TP3 **324** (2.44R). Recommended base-case RR: **1.78R**.

**Why entry:** Hybrid entry uses close 274 and ATR14 20.9: buy zone 266–280. Entry is valid only if price can trade/hold around 280 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 262 is placed below support structure (264 / 264). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 302 (1.22R), TP2 312 (1.78R), TP3 324 (2.44R). Targets are ATR/structure capped for hold_days=1. ATR14=20.9, resistance_5/10/20/60=306/336/378/505. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** score 0.465 below policy min_score 0.55; TP1 reward/risk 1.22R is below strategy minimum 1.25R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Defensive accumulation. Prefer retest and clean broker flow.

---

## KIJA — market_maker_silent_accum_defensive — WATCHLIST_ONLY

**Score:** 0.451 vs policy min 0.55 · **Close:** 124 · **ATR14:** 10.0 · **Volume ratio 20D:** 0.48 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 120–126, entry trigger **126**, stop **117**, risk 9 points (7.14%).

**Targets:** TP1 **135** (1.00R), TP2 **142** (1.78R), TP3 **148** (2.44R). Recommended base-case RR: **1.78R**.

**Why entry:** Hybrid entry uses close 124 and ATR14 10.0: buy zone 120–126. Entry is valid only if price can trade/hold around 126 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 117 is placed below support structure (118 / 118). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 135 (1.00R), TP2 142 (1.78R), TP3 148 (2.44R). Targets are ATR/structure capped for hold_days=1. ATR14=10.0, resistance_5/10/20/60=159/182/220/240. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** score 0.451 below policy min_score 0.55; TP1 reward/risk 1.00R is below strategy minimum 1.25R; volume ratio 0.48 below required 0.60

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Defensive accumulation. Prefer retest and clean broker flow.

---

## GULA — momentum_5d_hgb_defensive — WATCHLIST_ONLY

**Score:** 0.435 vs policy min 0.55 · **Close:** 545 · **ATR14:** 29.2 · **Volume ratio 20D:** 1.59 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 535–555, entry trigger **555**, stop **520**, risk 35 points (6.31%).

**Targets:** TP1 **585** (0.86R), TP2 **605** (1.43R), TP3 **635** (2.29R). Recommended base-case RR: **1.43R**.

**Why entry:** Entry trigger 555 is set above recent resistance 550 plus one IDX tick. This requires confirmation instead of buying blindly at close 545. Entry is valid only if price can trade/hold around 555 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 520 uses 1.15×ATR14 volatility cap. Thesis invalidates if the move reverses beyond normal volatility. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 585 (0.86R), TP2 605 (1.43R), TP3 635 (2.29R). Targets are ATR/structure capped for hold_days=1. ATR14=29.2, resistance_5/10/20/60=550/550/550/550. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** score 0.435 below policy min_score 0.55; TP1 reward/risk 0.86R is below strategy minimum 1.25R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Selective high-liquidity 5D momentum sleeve.

---

## GULA — momentum_10d_hgb_aggressive — WATCHLIST_ONLY

**Score:** 0.425 vs policy min 0.60 · **Close:** 545 · **ATR14:** 29.2 · **Volume ratio 20D:** 1.59 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 535–555, entry trigger **555**, stop **515**, risk 40 points (7.21%).

**Targets:** TP1 **595** (1.00R), TP2 **625** (1.75R), TP3 **655** (2.50R). Recommended base-case RR: **1.75R**.

**Why entry:** Entry trigger 555 is set above recent resistance 550 plus one IDX tick. This requires confirmation instead of buying blindly at close 545. Entry is valid only if price can trade/hold around 555 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 515 uses 1.30×ATR14 volatility cap. Thesis invalidates if the move reverses beyond normal volatility. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 595 (1.00R), TP2 625 (1.75R), TP3 655 (2.50R). Targets are ATR/structure capped for hold_days=2. ATR14=29.2, resistance_5/10/20/60=550/550/550/550. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** score 0.425 below policy min_score 0.60; TP1 reward/risk 1.00R is below strategy minimum 1.40R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## MIDI — market_maker_silent_accum_defensive — WATCHLIST_ONLY

**Score:** 0.421 vs policy min 0.55 · **Close:** 274 · **ATR14:** 16.0 · **Volume ratio 20D:** 5.39 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 268–278, entry trigger **278**, stop **272**, risk 6 points (2.16%).

**Targets:** TP1 **286** (1.33R), TP2 **308** (5.00R), TP3 **318** (6.67R). Recommended base-case RR: **5.00R**.

**Why entry:** Hybrid entry uses close 274 and ATR14 16.0: buy zone 268–278. Entry is valid only if price can trade/hold around 278 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 272 is placed below support structure (274 / 274). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 286 (1.33R), TP2 308 (5.00R), TP3 318 (6.67R). Targets are ATR/structure capped for hold_days=1. ATR14=16.0, resistance_5/10/20/60=322/356/356/356. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** score 0.421 below policy min_score 0.55

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Defensive accumulation. Prefer retest and clean broker flow.

---

## TRIN — swing_hgb_defensive — NO_TRADE

**Score:** 0.711 vs policy min 0.50 · **Close:** 468 · **ATR14:** 66.9 · **Volume ratio 20D:** 1.38 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 436–476, entry trigger **476**, stop **440**, risk 36 points (7.56%).

**Targets:** TP1 **545** (1.92R), TP2 **550** (2.06R), TP3 **565** (2.47R). Recommended base-case RR: **2.06R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 468: zone 436–476 uses ATR14 66.9 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 476 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 440 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 545 (1.92R), TP2 550 (2.06R), TP3 565 (2.47R). Targets are ATR/structure capped for hold_days=1. ATR14=66.9, resistance_5/10/20/60=550/695/860/1,225. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.56% exceeds max strategy risk 7.50%

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## RMKO — swing_hgb_defensive — NO_TRADE

**Score:** 0.700 vs policy min 0.50 · **Close:** 350 · **ATR14:** 44.8 · **Volume ratio 20D:** 0.88 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 328–356, entry trigger **356**, stop **328**, risk 28 points (7.87%).

**Targets:** TP1 **392** (1.29R), TP2 **404** (1.71R), TP3 **424** (2.43R). Recommended base-case RR: **1.71R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 350: zone 328–356 uses ATR14 44.8 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 356 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 328 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 392 (1.29R), TP2 404 (1.71R), TP3 424 (2.43R). Targets are ATR/structure capped for hold_days=1. ATR14=44.8, resistance_5/10/20/60=392/490/595/1,180. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.87% exceeds max strategy risk 7.50%

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## COIN — swing_hgb_defensive — NO_TRADE

**Score:** 0.684 vs policy min 0.50 · **Close:** 810 · **ATR14:** 112.5 · **Volume ratio 20D:** 0.75 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 755–825, entry trigger **825**, stop **760**, risk 65 points (7.88%).

**Targets:** TP1 **905** (1.23R), TP2 **940** (1.77R), TP3 **985** (2.46R). Recommended base-case RR: **1.77R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 810: zone 755–825 uses ATR14 112.5 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 825 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 760 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 905 (1.23R), TP2 940 (1.77R), TP3 985 (2.46R). Targets are ATR/structure capped for hold_days=1. ATR14=112.5, resistance_5/10/20/60=905/1,370/1,380/2,080. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.88% exceeds max strategy risk 7.50%; TP1 reward/risk 1.23R is below strategy minimum 1.25R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## VKTR — swing_hgb_defensive — NO_TRADE

**Score:** 0.684 vs policy min 0.50 · **Close:** 715 · **ATR14:** 86.1 · **Volume ratio 20D:** 0.46 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 675–725, entry trigger **725**, stop **670**, risk 55 points (7.59%).

**Targets:** TP1 **815** (1.64R), TP2 **820** (1.73R), TP3 **860** (2.45R). Recommended base-case RR: **1.73R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 715: zone 675–725 uses ATR14 86.1 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 725 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 670 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 815 (1.64R), TP2 820 (1.73R), TP3 860 (2.45R). Targets are ATR/structure capped for hold_days=1. ATR14=86.1, resistance_5/10/20/60=815/995/1,010/1,100. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.59% exceeds max strategy risk 7.50%; volume ratio 0.46 below required 0.60

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## TOBA — swing_hgb_defensive — NO_TRADE

**Score:** 0.680 vs policy min 0.50 · **Close:** 430 · **ATR14:** 42.2 · **Volume ratio 20D:** 0.51 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 410–436, entry trigger **436**, stop **402**, risk 34 points (7.80%).

**Targets:** TP1 **478** (1.24R), TP2 **494** (1.71R), TP3 **520** (2.47R). Recommended base-case RR: **1.71R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 430: zone 410–436 uses ATR14 42.2 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 436 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 402 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 478 (1.24R), TP2 494 (1.71R), TP3 520 (2.47R). Targets are ATR/structure capped for hold_days=1. ATR14=42.2, resistance_5/10/20/60=478/650/675/815. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.80% exceeds max strategy risk 7.50%; TP1 reward/risk 1.24R is below strategy minimum 1.25R; volume ratio 0.51 below required 0.60

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## INET — swing_hgb_defensive — NO_TRADE

**Score:** 0.674 vs policy min 0.50 · **Close:** 232 · **ATR14:** 24.6 · **Volume ratio 20D:** 0.82 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 220–236, entry trigger **236**, stop **218**, risk 18 points (7.63%).

**Targets:** TP1 **262** (1.44R), TP2 **268** (1.78R), TP3 **280** (2.44R). Recommended base-case RR: **1.78R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 232: zone 220–236 uses ATR14 24.6 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 236 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 218 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 262 (1.44R), TP2 268 (1.78R), TP3 280 (2.44R). Targets are ATR/structure capped for hold_days=1. ATR14=24.6, resistance_5/10/20/60=262/324/360/438. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.63% exceeds max strategy risk 7.50%; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## ESSA — scalping_rank_hgb — NO_TRADE

**Score:** 0.614 vs policy min 0.60 · **Close:** 670 · **ATR14:** 65.4 · **Volume ratio 20D:** 0.45 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 655–755, entry trigger **755**, stop **720**, risk 35 points (4.64%).

**Targets:** TP1 **790** (1.00R), TP2 **815** (1.71R), TP3 **840** (2.43R). Recommended base-case RR: **1.71R**.

**Why entry:** Entry trigger 755 is set above recent resistance 750 plus one IDX tick. This requires confirmation instead of buying blindly at close 670. Entry is valid only if price can trade/hold around 755 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 720 is capped by max risk 4.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 790 (1.00R), TP2 815 (1.71R), TP3 840 (2.43R). Targets are ATR/structure capped for hold_days=1. ATR14=65.4, resistance_5/10/20/60=750/910/995/995. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 12.69% > max 5.00%; entry-to-stop risk 4.64% exceeds max strategy risk 4.50%; TP1 reward/risk 1.00R is below strategy minimum 1.10R; volume ratio 0.45 below required 0.60

**Risk flags:** OK

**Strategy risk note:** Top-1 short-horizon scalp; invalidation must be quick.

---

## RMKO — position_xgb — NO_TRADE

**Score:** 0.577 vs policy min 0.55 · **Close:** 350 · **ATR14:** 44.8 · **Volume ratio 20D:** 0.88 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 328–356, entry trigger **356**, stop **322**, risk 34 points (9.55%).

**Targets:** TP1 **392** (1.06R), TP2 **414** (1.71R), TP3 **438** (2.41R). Recommended base-case RR: **1.71R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 350: zone 328–356 uses ATR14 44.8 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 356 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 322 is capped by max risk 9.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 392 (1.06R), TP2 414 (1.71R), TP3 438 (2.41R). Targets are ATR/structure capped for hold_days=1. ATR14=44.8, resistance_5/10/20/60=392/490/595/1,180. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 9.55% exceeds max strategy risk 9.00%; TP1 reward/risk 1.06R is below strategy minimum 1.35R

**Risk flags:** OK

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## TRIN — position_xgb — NO_TRADE

**Score:** 0.572 vs policy min 0.55 · **Close:** 468 · **ATR14:** 66.9 · **Volume ratio 20D:** 1.38 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 436–476, entry trigger **476**, stop **432**, risk 44 points (9.24%).

**Targets:** TP1 **550** (1.68R), TP2 **555** (1.80R), TP3 **585** (2.48R). Recommended base-case RR: **1.80R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 468: zone 436–476 uses ATR14 66.9 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 476 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 432 is capped by max risk 9.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 550 (1.68R), TP2 555 (1.80R), TP3 585 (2.48R). Targets are ATR/structure capped for hold_days=1. ATR14=66.9, resistance_5/10/20/60=550/695/860/1,225. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 9.24% exceeds max strategy risk 9.00%

**Risk flags:** OK

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## COIN — position_xgb — NO_TRADE

**Score:** 0.572 vs policy min 0.55 · **Close:** 810 · **ATR14:** 112.5 · **Volume ratio 20D:** 0.75 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 755–825, entry trigger **825**, stop **750**, risk 75 points (9.09%).

**Targets:** TP1 **905** (1.07R), TP2 **955** (1.73R), TP3 **1,005** (2.40R). Recommended base-case RR: **1.73R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 810: zone 755–825 uses ATR14 112.5 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 825 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 750 is capped by max risk 9.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 905 (1.07R), TP2 955 (1.73R), TP3 1,005 (2.40R). Targets are ATR/structure capped for hold_days=1. ATR14=112.5, resistance_5/10/20/60=905/1,370/1,380/2,080. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 9.09% exceeds max strategy risk 9.00%; TP1 reward/risk 1.07R is below strategy minimum 1.35R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## HRUM — position_xgb — NO_TRADE

**Score:** 0.571 vs policy min 0.55 · **Close:** 790 · **ATR14:** 55.7 · **Volume ratio 20D:** 0.63 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 760–800, entry trigger **800**, stop **725**, risk 75 points (9.38%).

**Targets:** TP1 **875** (1.00R), TP2 **930** (1.73R), TP3 **980** (2.40R). Recommended base-case RR: **1.73R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 790: zone 760–800 uses ATR14 55.7 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 800 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 725 is capped by max risk 9.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 875 (1.00R), TP2 930 (1.73R), TP3 980 (2.40R). Targets are ATR/structure capped for hold_days=1. ATR14=55.7, resistance_5/10/20/60=830/995/1,030/1,270. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 9.38% exceeds max strategy risk 9.00%; TP1 reward/risk 1.00R is below strategy minimum 1.35R

**Risk flags:** OK

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## INET — position_xgb — NO_TRADE

**Score:** 0.564 vs policy min 0.55 · **Close:** 232 · **ATR14:** 24.6 · **Volume ratio 20D:** 0.82 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 220–236, entry trigger **236**, stop **214**, risk 22 points (9.32%).

**Targets:** TP1 **262** (1.18R), TP2 **274** (1.73R), TP3 **290** (2.45R). Recommended base-case RR: **1.73R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 232: zone 220–236 uses ATR14 24.6 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 236 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 214 is capped by max risk 9.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 262 (1.18R), TP2 274 (1.73R), TP3 290 (2.45R). Targets are ATR/structure capped for hold_days=1. ATR14=24.6, resistance_5/10/20/60=262/324/360/438. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 9.32% exceeds max strategy risk 9.00%; TP1 reward/risk 1.18R is below strategy minimum 1.35R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## SSMS — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.464 vs policy min 0.60 · **Close:** 700 · **ATR14:** 86.8 · **Volume ratio 20D:** 7.23 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 680–1,425, entry trigger **1,425**, stop **1,310**, risk 115 points (8.07%).

**Targets:** TP1 **1,540** (1.00R), TP2 **1,625** (1.74R), TP3 **1,705** (2.43R). Recommended base-case RR: **1.74R**.

**Why entry:** Entry trigger 1,425 is set above recent resistance 1,420 plus one IDX tick. This requires confirmation instead of buying blindly at close 700. Entry is valid only if price can trade/hold around 1,425 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 1,310 uses 1.30×ATR14 volatility cap. Thesis invalidates if the move reverses beyond normal volatility. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,540 (1.00R), TP2 1,625 (1.74R), TP3 1,705 (2.43R). Targets are ATR/structure capped for hold_days=2. ATR14=86.8, resistance_5/10/20/60=950/1,420/1,470/1,800. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 103.57% > max 15.00%; score 0.464 below policy min_score 0.60; TP1 reward/risk 1.00R is below strategy minimum 1.40R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## OMED — market_maker_silent_accum_defensive — NO_TRADE

**Score:** 0.460 vs policy min 0.55 · **Close:** 230 · **ATR14:** 19.3 · **Volume ratio 20D:** 1.56 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 222–234, entry trigger **234**, stop **216**, risk 18 points (7.69%).

**Targets:** TP1 **252** (1.00R), TP2 **266** (1.78R), TP3 **278** (2.44R). Recommended base-case RR: **1.78R**.

**Why entry:** Hybrid entry uses close 230 and ATR14 19.3: buy zone 222–234. Entry is valid only if price can trade/hold around 234 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 216 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 252 (1.00R), TP2 266 (1.78R), TP3 278 (2.44R). Targets are ATR/structure capped for hold_days=1. ATR14=19.3, resistance_5/10/20/60=250/284/314/318. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.69% exceeds max strategy risk 7.50%; score 0.460 below policy min_score 0.55; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Defensive accumulation. Prefer retest and clean broker flow.

---

## PBSA — market_maker_silent_accum_defensive — NO_TRADE

**Score:** 0.454 vs policy min 0.55 · **Close:** 870 · **ATR14:** 94.3 · **Volume ratio 20D:** 0.94 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 835–890, entry trigger **890**, stop **820**, risk 70 points (7.87%).

**Targets:** TP1 **975** (1.21R), TP2 **1,010** (1.71R), TP3 **1,060** (2.43R). Recommended base-case RR: **1.71R**.

**Why entry:** Hybrid entry uses close 870 and ATR14 94.3: buy zone 835–890. Entry is valid only if price can trade/hold around 890 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 820 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 975 (1.21R), TP2 1,010 (1.71R), TP3 1,060 (2.43R). Targets are ATR/structure capped for hold_days=1. ATR14=94.3, resistance_5/10/20/60=880/975/1,240/1,480. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.87% exceeds max strategy risk 7.50%; score 0.454 below policy min_score 0.55; TP1 reward/risk 1.21R is below strategy minimum 1.25R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Defensive accumulation. Prefer retest and clean broker flow.

---

## BRMS — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.451 vs policy min 0.60 · **Close:** 595 · **ATR14:** 64.3 · **Volume ratio 20D:** 2.78 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 580–835, entry trigger **835**, stop **750**, risk 85 points (10.18%).

**Targets:** TP1 **930** (1.12R), TP2 **980** (1.71R), TP3 **1,040** (2.41R). Recommended base-case RR: **1.71R**.

**Why entry:** Entry trigger 835 is set above recent resistance 830 plus one IDX tick. This requires confirmation instead of buying blindly at close 595. Entry is valid only if price can trade/hold around 835 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 750 uses 1.30×ATR14 volatility cap. Thesis invalidates if the move reverses beyond normal volatility. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 930 (1.12R), TP2 980 (1.71R), TP3 1,040 (2.41R). Targets are ATR/structure capped for hold_days=2. ATR14=64.3, resistance_5/10/20/60=680/830/930/1,095. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 40.34% > max 15.00%; entry-to-stop risk 10.18% exceeds max strategy risk 10.00%; score 0.451 below policy min_score 0.60; TP1 reward/risk 1.12R is below strategy minimum 1.40R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## BANK — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.447 vs policy min 0.60 · **Close:** 238 · **ATR14:** 56.5 · **Volume ratio 20D:** 4.52 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 226–635, entry trigger **635**, stop **570**, risk 65 points (10.24%).

**Targets:** TP1 **700** (1.00R), TP2 **750** (1.77R), TP3 **795** (2.46R). Recommended base-case RR: **1.77R**.

**Why entry:** Entry trigger 635 is set above recent resistance 630 plus one IDX tick. This requires confirmation instead of buying blindly at close 238. Entry is valid only if price can trade/hold around 635 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 570 is capped by max risk 10.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 700 (1.00R), TP2 750 (1.77R), TP3 795 (2.46R). Targets are ATR/structure capped for hold_days=2. ATR14=56.5, resistance_5/10/20/60=350/630/640/640. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 166.81% > max 15.00%; entry-to-stop risk 10.24% exceeds max strategy risk 10.00%; score 0.447 below policy min_score 0.60; TP1 reward/risk 1.00R is below strategy minimum 1.40R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## BUVA — momentum_5d_hgb_defensive — NO_TRADE

**Score:** 0.436 vs policy min 0.55 · **Close:** 760 · **ATR14:** 113.6 · **Volume ratio 20D:** 1.36 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 735–1,180, entry trigger **1,180**, stop **1,095**, risk 85 points (7.20%).

**Targets:** TP1 **1,265** (1.00R), TP2 **1,375** (2.29R), TP3 **1,385** (2.41R). Recommended base-case RR: **2.29R**.

**Why entry:** Entry trigger 1,180 is set above recent resistance 1,175 plus one IDX tick. This requires confirmation instead of buying blindly at close 760. Entry is valid only if price can trade/hold around 1,180 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 1,095 is capped by max risk 7.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,265 (1.00R), TP2 1,375 (2.29R), TP3 1,385 (2.41R). Targets are ATR/structure capped for hold_days=1. ATR14=113.6, resistance_5/10/20/60=850/1,175/1,380/1,695. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 55.26% > max 8.00%; entry-to-stop risk 7.20% exceeds max strategy risk 7.00%; score 0.436 below policy min_score 0.55; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Selective high-liquidity 5D momentum sleeve.

---

## TRIN — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.430 vs policy min 0.60 · **Close:** 468 · **ATR14:** 66.9 · **Volume ratio 20D:** 1.38 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 454–700, entry trigger **700**, stop **630**, risk 70 points (10.00%).

**Targets:** TP1 **825** (1.79R), TP2 **860** (2.29R), TP3 **870** (2.43R). Recommended base-case RR: **2.29R**.

**Why entry:** Entry trigger 700 is set above recent resistance 695 plus one IDX tick. This requires confirmation instead of buying blindly at close 468. Entry is valid only if price can trade/hold around 700 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 630 is capped by max risk 10.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 825 (1.79R), TP2 860 (2.29R), TP3 870 (2.43R). Targets are ATR/structure capped for hold_days=2. ATR14=66.9, resistance_5/10/20/60=550/695/860/1,225. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 49.57% > max 15.00%; score 0.430 below policy min_score 0.60

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## MBMA — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.424 vs policy min 0.60 · **Close:** 478 · **ATR14:** 53.5 · **Volume ratio 20D:** 0.64 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 466–670, entry trigger **670**, stop **600**, risk 70 points (10.45%).

**Targets:** TP1 **740** (1.00R), TP2 **790** (1.71R), TP3 **840** (2.43R). Recommended base-case RR: **1.71R**.

**Why entry:** Entry trigger 670 is set above recent resistance 665 plus one IDX tick. This requires confirmation instead of buying blindly at close 478. Entry is valid only if price can trade/hold around 670 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 600 uses 1.30×ATR14 volatility cap. Thesis invalidates if the move reverses beyond normal volatility. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 740 (1.00R), TP2 790 (1.71R), TP3 840 (2.43R). Targets are ATR/structure capped for hold_days=2. ATR14=53.5, resistance_5/10/20/60=510/665/740/945. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 40.17% > max 15.00%; entry-to-stop risk 10.45% exceeds max strategy risk 10.00%; score 0.424 below policy min_score 0.60; TP1 reward/risk 1.00R is below strategy minimum 1.40R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## RMKO — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.418 vs policy min 0.60 · **Close:** 350 · **ATR14:** 44.8 · **Volume ratio 20D:** 0.88 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 340–492, entry trigger **492**, stop **442**, risk 50 points (10.16%).

**Targets:** TP1 **575** (1.66R), TP2 **595** (2.06R), TP3 **615** (2.46R). Recommended base-case RR: **2.06R**.

**Why entry:** Entry trigger 492 is set above recent resistance 490 plus one IDX tick. This requires confirmation instead of buying blindly at close 350. Entry is valid only if price can trade/hold around 492 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 442 is capped by max risk 10.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 575 (1.66R), TP2 595 (2.06R), TP3 615 (2.46R). Targets are ATR/structure capped for hold_days=2. ATR14=44.8, resistance_5/10/20/60=392/490/595/1,180. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 40.57% > max 15.00%; entry-to-stop risk 10.16% exceeds max strategy risk 10.00%; score 0.418 below policy min_score 0.60

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## TRUE — market_maker_silent_accum_defensive — NO_TRADE

**Score:** 0.417 vs policy min 0.55 · **Close:** 100 · **ATR14:** 15.1 · **Volume ratio 20D:** 0.77 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 94–104, entry trigger **104**, stop **96**, risk 8 points (7.69%).

**Targets:** TP1 **120** (2.00R), TP2 **124** (2.50R), TP3 **128** (3.00R). Recommended base-case RR: **2.50R**.

**Why entry:** Hybrid entry uses close 100 and ATR14 15.1: buy zone 94–104. Entry is valid only if price can trade/hold around 104 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 96 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 120 (2.00R), TP2 124 (2.50R), TP3 128 (3.00R). Targets are ATR/structure capped for hold_days=1. ATR14=15.1, resistance_5/10/20/60=120/173/190/290. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.69% exceeds max strategy risk 7.50%; score 0.417 below policy min_score 0.55; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Defensive accumulation. Prefer retest and clean broker flow.

---

## BSDE — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.417 vs policy min 0.60 · **Close:** 630 · **ATR14:** 33.6 · **Volume ratio 20D:** 6.00 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 620–785, entry trigger **785**, stop **740**, risk 45 points (5.73%).

**Targets:** TP1 **835** (1.11R), TP2 **865** (1.78R), TP3 **895** (2.44R). Recommended base-case RR: **1.78R**.

**Why entry:** Entry trigger 785 is set above recent resistance 780 plus one IDX tick. This requires confirmation instead of buying blindly at close 630. Entry is valid only if price can trade/hold around 785 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 740 uses 1.30×ATR14 volatility cap. Thesis invalidates if the move reverses beyond normal volatility. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 835 (1.11R), TP2 865 (1.78R), TP3 895 (2.44R). Targets are ATR/structure capped for hold_days=2. ATR14=33.6, resistance_5/10/20/60=720/780/835/910. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 24.60% > max 15.00%; score 0.417 below policy min_score 0.60; TP1 reward/risk 1.11R is below strategy minimum 1.40R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## GTSI — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.414 vs policy min 0.60 · **Close:** 158 · **ATR14:** 19.9 · **Volume ratio 20D:** 0.45 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 154–240, entry trigger **240**, stop **216**, risk 24 points (10.00%).

**Targets:** TP1 **274** (1.42R), TP2 **282** (1.75R), TP3 **298** (2.42R). Recommended base-case RR: **1.75R**.

**Why entry:** Entry trigger 240 is set above recent resistance 238 plus one IDX tick. This requires confirmation instead of buying blindly at close 158. Entry is valid only if price can trade/hold around 240 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 216 is capped by max risk 10.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 274 (1.42R), TP2 282 (1.75R), TP3 298 (2.42R). Targets are ATR/structure capped for hold_days=2. ATR14=19.9, resistance_5/10/20/60=189/238/274/350. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 51.90% > max 15.00%; score 0.414 below policy min_score 0.60; volume ratio 0.45 below required 0.60

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## KIJA — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.412 vs policy min 0.60 · **Close:** 124 · **ATR14:** 10.0 · **Volume ratio 20D:** 0.48 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 122–183, entry trigger **183**, stop **170**, risk 13 points (7.10%).

**Targets:** TP1 **196** (1.00R), TP2 **216** (2.54R), TP3 **220** (2.85R). Recommended base-case RR: **2.54R**.

**Why entry:** Entry trigger 183 is set above recent resistance 182 plus one IDX tick. This requires confirmation instead of buying blindly at close 124. Entry is valid only if price can trade/hold around 183 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 170 uses 1.30×ATR14 volatility cap. Thesis invalidates if the move reverses beyond normal volatility. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 196 (1.00R), TP2 216 (2.54R), TP3 220 (2.85R). Targets are ATR/structure capped for hold_days=2. ATR14=10.0, resistance_5/10/20/60=159/182/220/240. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 47.58% > max 15.00%; score 0.412 below policy min_score 0.60; TP1 reward/risk 1.00R is below strategy minimum 1.40R; volume ratio 0.48 below required 0.60

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## NSSS — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.410 vs policy min 0.60 · **Close:** 462 · **ATR14:** 69.9 · **Volume ratio 20D:** 0.30 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 448–855, entry trigger **855**, stop **765**, risk 90 points (10.53%).

**Targets:** TP1 **945** (1.00R), TP2 **1,060** (2.28R), TP3 **1,075** (2.44R). Recommended base-case RR: **2.28R**.

**Why entry:** Entry trigger 855 is set above recent resistance 850 plus one IDX tick. This requires confirmation instead of buying blindly at close 462. Entry is valid only if price can trade/hold around 855 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 765 is capped by max risk 10.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 945 (1.00R), TP2 1,060 (2.28R), TP3 1,075 (2.44R). Targets are ATR/structure capped for hold_days=2. ATR14=69.9, resistance_5/10/20/60=575/850/1,060/1,300. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 85.06% > max 15.00%; entry-to-stop risk 10.53% exceeds max strategy risk 10.00%; score 0.410 below policy min_score 0.60; TP1 reward/risk 1.00R is below strategy minimum 1.40R; volume ratio 0.30 below required 0.60

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## HRUM — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.409 vs policy min 0.60 · **Close:** 790 · **ATR14:** 55.7 · **Volume ratio 20D:** 0.63 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 775–1,000, entry trigger **1,000**, stop **925**, risk 75 points (7.50%).

**Targets:** TP1 **1,075** (1.00R), TP2 **1,130** (1.73R), TP3 **1,180** (2.40R). Recommended base-case RR: **1.73R**.

**Why entry:** Entry trigger 1,000 is set above recent resistance 995 plus one IDX tick. This requires confirmation instead of buying blindly at close 790. Entry is valid only if price can trade/hold around 1,000 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 925 uses 1.30×ATR14 volatility cap. Thesis invalidates if the move reverses beyond normal volatility. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,075 (1.00R), TP2 1,130 (1.73R), TP3 1,180 (2.40R). Targets are ATR/structure capped for hold_days=2. ATR14=55.7, resistance_5/10/20/60=830/995/1,030/1,270. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 26.58% > max 15.00%; score 0.409 below policy min_score 0.60; TP1 reward/risk 1.00R is below strategy minimum 1.40R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## SIMP — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.409 vs policy min 0.60 · **Close:** 555 · **ATR14:** 46.4 · **Volume ratio 20D:** 0.58 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 545–760, entry trigger **760**, stop **695**, risk 65 points (8.55%).

**Targets:** TP1 **825** (1.00R), TP2 **915** (2.38R), TP3 **920** (2.46R). Recommended base-case RR: **2.38R**.

**Why entry:** Entry trigger 760 is set above recent resistance 755 plus one IDX tick. This requires confirmation instead of buying blindly at close 555. Entry is valid only if price can trade/hold around 760 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 695 uses 1.30×ATR14 volatility cap. Thesis invalidates if the move reverses beyond normal volatility. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 825 (1.00R), TP2 915 (2.38R), TP3 920 (2.46R). Targets are ATR/structure capped for hold_days=2. ATR14=46.4, resistance_5/10/20/60=585/755/920/930. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 36.94% > max 15.00%; score 0.409 below policy min_score 0.60; TP1 reward/risk 1.00R is below strategy minimum 1.40R; volume ratio 0.58 below required 0.60; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## NICL — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.407 vs policy min 0.60 · **Close:** 570 · **ATR14:** 61.4 · **Volume ratio 20D:** 0.76 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 555–880, entry trigger **880**, stop **800**, risk 80 points (9.09%).

**Targets:** TP1 **965** (1.06R), TP2 **1,020** (1.75R), TP3 **1,075** (2.44R). Recommended base-case RR: **1.75R**.

**Why entry:** Entry trigger 880 is set above recent resistance 875 plus one IDX tick. This requires confirmation instead of buying blindly at close 570. Entry is valid only if price can trade/hold around 880 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 800 uses 1.30×ATR14 volatility cap. Thesis invalidates if the move reverses beyond normal volatility. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 965 (1.06R), TP2 1,020 (1.75R), TP3 1,075 (2.44R). Targets are ATR/structure capped for hold_days=2. ATR14=61.4, resistance_5/10/20/60=600/875/965/1,285. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 54.39% > max 15.00%; score 0.407 below policy min_score 0.60; TP1 reward/risk 1.06R is below strategy minimum 1.40R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## COIN — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.406 vs policy min 0.60 · **Close:** 810 · **ATR14:** 112.5 · **Volume ratio 20D:** 0.75 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 785–1,375, entry trigger **1,375**, stop **1,235**, risk 140 points (10.18%).

**Targets:** TP1 **1,515** (1.00R), TP2 **1,615** (1.71R), TP3 **1,715** (2.43R). Recommended base-case RR: **1.71R**.

**Why entry:** Entry trigger 1,375 is set above recent resistance 1,370 plus one IDX tick. This requires confirmation instead of buying blindly at close 810. Entry is valid only if price can trade/hold around 1,375 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 1,235 is capped by max risk 10.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,515 (1.00R), TP2 1,615 (1.71R), TP3 1,715 (2.43R). Targets are ATR/structure capped for hold_days=2. ATR14=112.5, resistance_5/10/20/60=905/1,370/1,380/2,080. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 69.75% > max 15.00%; entry-to-stop risk 10.18% exceeds max strategy risk 10.00%; score 0.406 below policy min_score 0.60; TP1 reward/risk 1.00R is below strategy minimum 1.40R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## CUAN — ara_candidate — NO_TRADE

**Score:** 0.219 vs policy min 0.50 · **Close:** 630 · **ATR14:** 122.9 · **Volume ratio 20D:** 3.72 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 605–1,310, entry trigger **1,310**, stop **1,175**, risk 135 points (10.31%).

**Targets:** TP1 **1,435** (0.93R), TP2 **1,555** (1.81R), TP3 **1,635** (2.41R). Recommended base-case RR: **1.81R**.

**Why entry:** Entry trigger 1,310 is set above recent resistance 1,305 plus one IDX tick. This requires confirmation instead of buying blindly at close 630. Entry is valid only if price can trade/hold around 1,310 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 1,175 is capped by max risk 10.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,435 (0.93R), TP2 1,555 (1.81R), TP3 1,635 (2.41R). Targets are ATR/structure capped for hold_days=1. ATR14=122.9, resistance_5/10/20/60=630/1,305/1,555/1,860. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 107.94% > max 12.00%; entry-to-stop risk 10.31% exceeds max strategy risk 10.00%; score 0.219 below policy min_score 0.50; TP1 reward/risk 0.93R is below strategy minimum 1.30R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** High drawdown tactical setup. Use as execution only if confirmation is strong and liquidity is clean.

---
