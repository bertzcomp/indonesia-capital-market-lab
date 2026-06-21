# Numeric Trading Desk Report — 2026-06-05

This report is generated from live model scores, selected signal policy, canonical OHLCV, ATR, support/resistance, liquidity, and broker-flow diagnostics. It is not a simple BUY/SELL list; each plan is conditional on execution behaviour.

## Summary

| Plan quality | Count |
|---|---:|
| ACTIONABLE | 10 |
| CONDITIONAL | 14 |
| WATCHLIST_ONLY | 2 |
| NO_TRADE | 30 |

## PSKT — swing_hgb_defensive — ACTIONABLE

**Score:** 0.796 vs policy min 0.50 · **Close:** 167 · **ATR14:** 25.6 · **Volume ratio 20D:** 0.63 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 155–170, entry trigger **170**, stop **160**, risk 10 points (5.88%).

**Targets:** TP1 **183** (1.30R), TP2 **187** (1.70R), TP3 **234** (6.40R). Recommended base-case RR: **1.70R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 167: zone 155–170 uses ATR14 25.6 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 170 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 160 is placed below support structure (161 / 161). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 183 (1.30R), TP2 187 (1.70R), TP3 234 (6.40R). Targets are ATR/structure capped for hold_days=1. ATR14=25.6, resistance_5/10/20/60=234/236/272/328. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## TOBA — swing_hgb_defensive — ACTIONABLE

**Score:** 0.793 vs policy min 0.50 · **Close:** 346 · **ATR14:** 38.6 · **Volume ratio 20D:** 0.62 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 328–350, entry trigger **350**, stop **342**, risk 8 points (2.29%).

**Targets:** TP1 **370** (2.50R), TP2 **374** (3.00R), TP3 **448** (12.25R). Recommended base-case RR: **3.00R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 346: zone 328–350 uses ATR14 38.6 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 350 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 342 is placed below support structure (344 / 344). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 370 (2.50R), TP2 374 (3.00R), TP3 448 (12.25R). Targets are ATR/structure capped for hold_days=1. ATR14=38.6, resistance_5/10/20/60=452/494/650/815. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## BBYB — swing_hgb_defensive — ACTIONABLE

**Score:** 0.774 vs policy min 0.50 · **Close:** 214 · **ATR14:** 18.4 · **Volume ratio 20D:** 0.75 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 204–216, entry trigger **216**, stop **210**, risk 6 points (2.78%).

**Targets:** TP1 **226** (1.67R), TP2 **228** (2.00R), TP3 **264** (8.00R). Recommended base-case RR: **2.00R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 214: zone 204–216 uses ATR14 18.4 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 216 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 210 is placed below support structure (212 / 212). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 226 (1.67R), TP2 228 (2.00R), TP3 264 (8.00R). Targets are ATR/structure capped for hold_days=1. ATR14=18.4, resistance_5/10/20/60=274/288/324/380. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## TRIN — swing_hgb_defensive — ACTIONABLE

**Score:** 0.772 vs policy min 0.50 · **Close:** 312 · **ATR14:** 67.4 · **Volume ratio 20D:** 1.59 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 286–320, entry trigger **320**, stop **296**, risk 24 points (7.50%).

**Targets:** TP1 **354** (1.42R), TP2 **362** (1.75R), TP3 **486** (6.92R). Recommended base-case RR: **1.75R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 312: zone 286–320 uses ATR14 67.4 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 320 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 296 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 354 (1.42R), TP2 362 (1.75R), TP3 486 (6.92R). Targets are ATR/structure capped for hold_days=1. ATR14=67.4, resistance_5/10/20/60=486/580/715/1,120. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## SOCI — swing_hgb_defensive — ACTIONABLE

**Score:** 0.769 vs policy min 0.50 · **Close:** 290 · **ATR14:** 41.0 · **Volume ratio 20D:** 0.69 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 270–296, entry trigger **296**, stop **288**, risk 8 points (2.70%).

**Targets:** TP1 **318** (2.75R), TP2 **322** (3.25R), TP3 **400** (13.00R). Recommended base-case RR: **3.25R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 290: zone 270–296 uses ATR14 41.0 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 296 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 288 is placed below support structure (290 / 290). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 318 (2.75R), TP2 322 (3.25R), TP3 400 (13.00R). Targets are ATR/structure capped for hold_days=1. ATR14=41.0, resistance_5/10/20/60=416/424/540/735. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## ARTO — position_xgb — ACTIONABLE

**Score:** 0.615 vs policy min 0.55 · **Close:** 930 · **ATR14:** 63.6 · **Volume ratio 20D:** 0.99 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 900–940, entry trigger **940**, stop **925**, risk 15 points (1.60%).

**Targets:** TP1 **975** (2.33R), TP2 **985** (3.00R), TP3 **1,185** (16.33R). Recommended base-case RR: **3.00R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 930: zone 900–940 uses ATR14 63.6 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 940 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 925 is placed below support structure (930 / 930). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 975 (2.33R), TP2 985 (3.00R), TP3 1,185 (16.33R). Targets are ATR/structure capped for hold_days=1. ATR14=63.6, resistance_5/10/20/60=1,185/1,185/1,310/1,650. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## SOCI — position_xgb — ACTIONABLE

**Score:** 0.607 vs policy min 0.55 · **Close:** 290 · **ATR14:** 41.0 · **Volume ratio 20D:** 0.69 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 270–296, entry trigger **296**, stop **288**, risk 8 points (2.70%).

**Targets:** TP1 **318** (2.75R), TP2 **322** (3.25R), TP3 **416** (15.00R). Recommended base-case RR: **3.25R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 290: zone 270–296 uses ATR14 41.0 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 296 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 288 is placed below support structure (290 / 290). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 318 (2.75R), TP2 322 (3.25R), TP3 416 (15.00R). Targets are ATR/structure capped for hold_days=1. ATR14=41.0, resistance_5/10/20/60=416/424/540/735. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## STAA — position_xgb — ACTIONABLE

**Score:** 0.603 vs policy min 0.55 · **Close:** 905 · **ATR14:** 53.2 · **Volume ratio 20D:** 0.91 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 880–915, entry trigger **915**, stop **885**, risk 30 points (3.28%).

**Targets:** TP1 **990** (2.50R), TP2 **1,020** (3.50R), TP3 **1,035** (4.00R). Recommended base-case RR: **3.50R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 905: zone 880–915 uses ATR14 53.2 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 915 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 885 is placed below support structure (890 / 890). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 990 (2.50R), TP2 1,020 (3.50R), TP3 1,035 (4.00R). Targets are ATR/structure capped for hold_days=1. ATR14=53.2, resistance_5/10/20/60=1,020/1,195/1,240/1,385. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## HRUM — position_xgb — ACTIONABLE

**Score:** 0.600 vs policy min 0.55 · **Close:** 680 · **ATR14:** 65.7 · **Volume ratio 20D:** 0.61 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 650–690, entry trigger **690**, stop **670**, risk 20 points (2.90%).

**Targets:** TP1 **725** (1.75R), TP2 **825** (6.75R), TP3 **835** (7.25R). Recommended base-case RR: **6.75R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 680: zone 650–690 uses ATR14 65.7 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 690 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 670 is placed below support structure (675 / 675). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 725 (1.75R), TP2 825 (6.75R), TP3 835 (7.25R). Targets are ATR/structure capped for hold_days=1. ATR14=65.7, resistance_5/10/20/60=825/830/1,010/1,260. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## HUMI — position_xgb — ACTIONABLE

**Score:** 0.598 vs policy min 0.55 · **Close:** 100 · **ATR14:** 18.4 · **Volume ratio 20D:** 0.80 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 92–102, entry trigger **102**, stop **96**, risk 6 points (5.88%).

**Targets:** TP1 **112** (1.67R), TP2 **147** (7.50R), TP3 **151** (8.17R). Recommended base-case RR: **7.50R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 100: zone 92–102 uses ATR14 18.4 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 102 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 96 is placed below support structure (97 / 97). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 112 (1.67R), TP2 147 (7.50R), TP3 151 (8.17R). Targets are ATR/structure capped for hold_days=1. ATR14=18.4, resistance_5/10/20/60=151/174/195/260. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## SCMA — swing_hgb_defensive — CONDITIONAL

**Score:** 0.791 vs policy min 0.50 · **Close:** 193 · **ATR14:** 14.9 · **Volume ratio 20D:** 0.92 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 186–195, entry trigger **195**, stop **181**, risk 14 points (7.18%).

**Targets:** TP1 **210** (1.07R), TP2 **222** (1.93R), TP3 **232** (2.64R). Recommended base-case RR: **1.93R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 193: zone 186–195 uses ATR14 14.9 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 195 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 181 is placed below support structure (182 / 182). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 210 (1.07R), TP2 222 (1.93R), TP3 232 (2.64R). Targets are ATR/structure capped for hold_days=1. ATR14=14.9, resistance_5/10/20/60=232/240/268/312. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.07R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## ELSA — swing_hgb_defensive — CONDITIONAL

**Score:** 0.777 vs policy min 0.50 · **Close:** 575 · **ATR14:** 43.9 · **Volume ratio 20D:** 0.54 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 555–580, entry trigger **580**, stop **560**, risk 20 points (3.45%).

**Targets:** TP1 **625** (2.25R), TP2 **645** (3.25R), TP3 **655** (3.75R). Recommended base-case RR: **3.25R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 575: zone 555–580 uses ATR14 43.9 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 580 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 560 is placed below support structure (565 / 565). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 625 (2.25R), TP2 645 (3.25R), TP3 655 (3.75R). Targets are ATR/structure capped for hold_days=1. ATR14=43.9, resistance_5/10/20/60=645/695/790/1,050. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** volume ratio 0.54 below required 0.60

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## NRCA — swing_hgb_defensive — CONDITIONAL

**Score:** 0.776 vs policy min 0.50 · **Close:** 410 · **ATR14:** 39.0 · **Volume ratio 20D:** 0.86 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 392–414, entry trigger **414**, stop **408**, risk 6 points (1.45%).

**Targets:** TP1 **434** (3.33R), TP2 **438** (4.00R), TP3 **510** (16.00R). Recommended base-case RR: **4.00R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 410: zone 392–414 uses ATR14 39.0 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 414 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 408 is placed below support structure (410 / 410). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 434 (3.33R), TP2 438 (4.00R), TP3 510 (16.00R). Targets are ATR/structure capped for hold_days=1. ATR14=39.0, resistance_5/10/20/60=510/510/635/795. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## OMED — swing_hgb_defensive — CONDITIONAL

**Score:** 0.773 vs policy min 0.50 · **Close:** 188 · **ATR14:** 18.4 · **Volume ratio 20D:** 0.99 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 179–190, entry trigger **190**, stop **180**, risk 10 points (5.26%).

**Targets:** TP1 **200** (1.00R), TP2 **208** (1.80R), TP3 **236** (4.60R). Recommended base-case RR: **1.80R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 188: zone 179–190 uses ATR14 18.4 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 190 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 180 is placed below support structure (181 / 181). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 200 (1.00R), TP2 208 (1.80R), TP3 236 (4.60R). Targets are ATR/structure capped for hold_days=1. ATR14=18.4, resistance_5/10/20/60=240/250/310/318. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## RMKO — swing_hgb_defensive — CONDITIONAL

**Score:** 0.771 vs policy min 0.50 · **Close:** 258 · **ATR14:** 47.4 · **Volume ratio 20D:** 1.07 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 236–264, entry trigger **264**, stop **256**, risk 8 points (3.03%).

**Targets:** TP1 **288** (3.00R), TP2 **292** (3.50R), TP3 **372** (13.50R). Recommended base-case RR: **3.50R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 258: zone 236–264 uses ATR14 47.4 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 264 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 256 is placed below support structure (258 / 258). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 288 (3.00R), TP2 292 (3.50R), TP3 372 (13.50R). Targets are ATR/structure capped for hold_days=1. ATR14=47.4, resistance_5/10/20/60=372/412/505/865. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## DKFT — swing_hgb_defensive — CONDITIONAL

**Score:** 0.770 vs policy min 0.50 · **Close:** 570 · **ATR14:** 50.4 · **Volume ratio 20D:** 1.32 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 545–580, entry trigger **580**, stop **550**, risk 30 points (5.17%).

**Targets:** TP1 **610** (1.00R), TP2 **635** (1.83R), TP3 **710** (4.33R). Recommended base-case RR: **1.83R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 570: zone 545–580 uses ATR14 50.4 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 580 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 550 is placed below support structure (555 / 555). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 610 (1.00R), TP2 635 (1.83R), TP3 710 (4.33R). Targets are ATR/structure capped for hold_days=1. ATR14=50.4, resistance_5/10/20/60=715/740/840/885. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## DKFT — position_xgb — CONDITIONAL

**Score:** 0.610 vs policy min 0.55 · **Close:** 570 · **ATR14:** 50.4 · **Volume ratio 20D:** 1.32 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 545–580, entry trigger **580**, stop **550**, risk 30 points (5.17%).

**Targets:** TP1 **610** (1.00R), TP2 **705** (4.17R), TP3 **715** (4.50R). Recommended base-case RR: **4.17R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 570: zone 545–580 uses ATR14 50.4 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 580 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 550 is placed below support structure (555 / 555). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 610 (1.00R), TP2 705 (4.17R), TP3 715 (4.50R). Targets are ATR/structure capped for hold_days=1. ATR14=50.4, resistance_5/10/20/60=715/740/840/885. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.35R

**Risk flags:** OK

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## VKTR — position_xgb — CONDITIONAL

**Score:** 0.608 vs policy min 0.55 · **Close:** 605 · **ATR14:** 94.6 · **Volume ratio 20D:** 0.95 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 560–615, entry trigger **615**, stop **565**, risk 50 points (8.13%).

**Targets:** TP1 **665** (1.00R), TP2 **830** (4.30R), TP3 **855** (4.80R). Recommended base-case RR: **4.30R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 605: zone 560–615 uses ATR14 94.6 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 615 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 565 is placed below support structure (570 / 570). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 665 (1.00R), TP2 830 (4.30R), TP3 855 (4.80R). Targets are ATR/structure capped for hold_days=1. ATR14=94.6, resistance_5/10/20/60=830/830/995/1,090. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.35R

**Risk flags:** OK

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## NRCA — position_xgb — CONDITIONAL

**Score:** 0.608 vs policy min 0.55 · **Close:** 410 · **ATR14:** 39.0 · **Volume ratio 20D:** 0.86 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 392–414, entry trigger **414**, stop **408**, risk 6 points (1.45%).

**Targets:** TP1 **434** (3.33R), TP2 **510** (16.00R), TP3 **515** (16.83R). Recommended base-case RR: **16.00R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 410: zone 392–414 uses ATR14 39.0 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 414 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 408 is placed below support structure (410 / 410). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 434 (3.33R), TP2 510 (16.00R), TP3 515 (16.83R). Targets are ATR/structure capped for hold_days=1. ATR14=39.0, resistance_5/10/20/60=510/510/635/795. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## SUPA — position_xgb — CONDITIONAL

**Score:** 0.605 vs policy min 0.55 · **Close:** 705 · **ATR14:** 42.1 · **Volume ratio 20D:** 2.13 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 685–710, entry trigger **710**, stop **700**, risk 10 points (1.41%).

**Targets:** TP1 **735** (2.50R), TP2 **740** (3.00R), TP3 **875** (16.50R). Recommended base-case RR: **3.00R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 705: zone 685–710 uses ATR14 42.1 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 710 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 700 is placed below support structure (705 / 705). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 735 (2.50R), TP2 740 (3.00R), TP3 875 (16.50R). Targets are ATR/structure capped for hold_days=1. ATR14=42.1, resistance_5/10/20/60=880/905/905/1,080. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## TPMA — position_xgb — CONDITIONAL

**Score:** 0.603 vs policy min 0.55 · **Close:** 360 · **ATR14:** 25.2 · **Volume ratio 20D:** 0.61 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 348–364, entry trigger **364**, stop **358**, risk 6 points (1.65%).

**Targets:** TP1 **378** (2.33R), TP2 **382** (3.00R), TP3 **386** (3.67R). Recommended base-case RR: **3.00R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 360: zone 348–364 uses ATR14 25.2 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 364 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 358 is placed below support structure (360 / 360). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 378 (2.33R), TP2 382 (3.00R), TP3 386 (3.67R). Targets are ATR/structure capped for hold_days=1. ATR14=25.2, resistance_5/10/20/60=500/515/565/620. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## BFIN — position_xgb — CONDITIONAL

**Score:** 0.601 vs policy min 0.55 · **Close:** 625 · **ATR14:** 36.8 · **Volume ratio 20D:** 0.75 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 605–630, entry trigger **630**, stop **615**, risk 15 points (2.38%).

**Targets:** TP1 **650** (1.33R), TP2 **720** (6.00R), TP3 **730** (6.67R). Recommended base-case RR: **6.00R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 625: zone 605–630 uses ATR14 36.8 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 630 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 615 is placed below support structure (620 / 620). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 650 (1.33R), TP2 720 (6.00R), TP3 730 (6.67R). Targets are ATR/structure capped for hold_days=1. ATR14=36.8, resistance_5/10/20/60=720/780/825/965. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.33R is below strategy minimum 1.35R

**Risk flags:** OK

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## BULL — position_xgb — CONDITIONAL

**Score:** 0.598 vs policy min 0.55 · **Close:** 298 · **ATR14:** 46.3 · **Volume ratio 20D:** 0.89 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 276–304, entry trigger **304**, stop **288**, risk 16 points (5.26%).

**Targets:** TP1 **328** (1.50R), TP2 **410** (6.62R), TP3 **418** (7.12R). Recommended base-case RR: **6.62R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 298: zone 276–304 uses ATR14 46.3 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 304 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 288 is placed below support structure (290 / 290). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 328 (1.50R), TP2 410 (6.62R), TP3 418 (7.12R). Targets are ATR/structure capped for hold_days=1. ATR14=46.3, resistance_5/10/20/60=410/428/545/610. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## UVCR — position_xgb — CONDITIONAL

**Score:** 0.598 vs policy min 0.55 · **Close:** 169 · **ATR14:** 16.1 · **Volume ratio 20D:** 0.44 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 161–171, entry trigger **171**, stop **164**, risk 7 points (4.09%).

**Targets:** TP1 **180** (1.29R), TP2 **183** (1.71R), TP3 **188** (2.43R). Recommended base-case RR: **1.71R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 169: zone 161–171 uses ATR14 16.1 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 171 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 164 is placed below support structure (165 / 165). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 180 (1.29R), TP2 183 (1.71R), TP3 188 (2.43R). Targets are ATR/structure capped for hold_days=1. ATR14=16.1, resistance_5/10/20/60=250/250/250/250. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.29R is below strategy minimum 1.35R; volume ratio 0.44 below required 0.60

**Risk flags:** OK

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## SOCI — market_maker_silent_accum_defensive — WATCHLIST_ONLY

**Score:** 0.520 vs policy min 0.55 · **Close:** 290 · **ATR14:** 41.0 · **Volume ratio 20D:** 0.69 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 274–300, entry trigger **300**, stop **288**, risk 12 points (4.00%).

**Targets:** TP1 **322** (1.83R), TP2 **328** (2.33R), TP3 **404** (8.67R). Recommended base-case RR: **2.33R**.

**Why entry:** Hybrid entry uses close 290 and ATR14 41.0: buy zone 274–300. Entry is valid only if price can trade/hold around 300 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 288 is placed below support structure (290 / 290). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 322 (1.83R), TP2 328 (2.33R), TP3 404 (8.67R). Targets are ATR/structure capped for hold_days=1. ATR14=41.0, resistance_5/10/20/60=416/424/540/735. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** score 0.520 below policy min_score 0.55

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Defensive accumulation. Prefer retest and clean broker flow.

---

## MSJA — market_maker_silent_accum_defensive — WATCHLIST_ONLY

**Score:** 0.512 vs policy min 0.55 · **Close:** 392 · **ATR14:** 36.0 · **Volume ratio 20D:** 0.66 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 378–400, entry trigger **400**, stop **378**, risk 22 points (5.50%).

**Targets:** TP1 **422** (1.00R), TP2 **438** (1.73R), TP3 **454** (2.45R). Recommended base-case RR: **1.73R**.

**Why entry:** Hybrid entry uses close 392 and ATR14 36.0: buy zone 378–400. Entry is valid only if price can trade/hold around 400 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 378 is placed below support structure (380 / 374). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 422 (1.00R), TP2 438 (1.73R), TP3 454 (2.45R). Targets are ATR/structure capped for hold_days=1. ATR14=36.0, resistance_5/10/20/60=414/448/555/560. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** score 0.512 below policy min_score 0.55; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Defensive accumulation. Prefer retest and clean broker flow.

---

## GTSI — swing_hgb_defensive — NO_TRADE

**Score:** 0.794 vs policy min 0.50 · **Close:** 109 · **ATR14:** 20.3 · **Volume ratio 20D:** 0.87 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 100–112, entry trigger **112**, stop **103**, risk 9 points (8.04%).

**Targets:** TP1 **123** (1.22R), TP2 **128** (1.78R), TP3 **163** (5.67R). Recommended base-case RR: **1.78R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 109: zone 100–112 uses ATR14 20.3 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 112 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 103 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 123 (1.22R), TP2 128 (1.78R), TP3 163 (5.67R). Targets are ATR/structure capped for hold_days=1. ATR14=20.3, resistance_5/10/20/60=164/192/238/334. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.04% exceeds max strategy risk 7.50%; TP1 reward/risk 1.22R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## VKTR — swing_hgb_defensive — NO_TRADE

**Score:** 0.785 vs policy min 0.50 · **Close:** 605 · **ATR14:** 94.6 · **Volume ratio 20D:** 0.95 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 560–615, entry trigger **615**, stop **565**, risk 50 points (8.13%).

**Targets:** TP1 **665** (1.00R), TP2 **700** (1.70R), TP3 **830** (4.30R). Recommended base-case RR: **1.70R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 605: zone 560–615 uses ATR14 94.6 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 615 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 565 is placed below support structure (570 / 570). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 665 (1.00R), TP2 700 (1.70R), TP3 830 (4.30R). Targets are ATR/structure capped for hold_days=1. ATR14=94.6, resistance_5/10/20/60=830/830/995/1,090. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.13% exceeds max strategy risk 7.50%; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## BIPI — swing_hgb_defensive — NO_TRADE

**Score:** 0.770 vs policy min 0.50 · **Close:** 137 · **ATR14:** 22.9 · **Volume ratio 20D:** 0.47 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 126–140, entry trigger **140**, stop **129**, risk 11 points (7.86%).

**Targets:** TP1 **152** (1.09R), TP2 **182** (3.82R), TP3 **190** (4.55R). Recommended base-case RR: **3.82R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 137: zone 126–140 uses ATR14 22.9 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 140 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 129 is placed below support structure (130 / 130). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 152 (1.09R), TP2 182 (3.82R), TP3 190 (4.55R). Targets are ATR/structure capped for hold_days=1. ATR14=22.9, resistance_5/10/20/60=190/212/262/342. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.86% exceeds max strategy risk 7.50%; TP1 reward/risk 1.09R is below strategy minimum 1.25R; volume ratio 0.47 below required 0.60

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## CTTH — swing_hgb_defensive — NO_TRADE

**Score:** 0.770 vs policy min 0.50 · **Close:** 112 · **ATR14:** 95.4 · **Volume ratio 20D:** 0.97 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 103–122, entry trigger **122**, stop **112**, risk 10 points (8.20%).

**Targets:** TP1 **176** (5.40R), TP2 **181** (5.90R), TP3 **186** (6.40R). Recommended base-case RR: **5.90R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 112: zone 103–122 uses ATR14 95.4 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 122 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 112 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 176 (5.40R), TP2 181 (5.90R), TP3 186 (6.40R). Targets are ATR/structure capped for hold_days=1. ATR14=95.4, resistance_5/10/20/60=176/182/216/216. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 8.93% > max 8.00%; entry-to-stop risk 8.20% exceeds max strategy risk 7.50%; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## DKFT — scalping_rank_hgb — NO_TRADE

**Score:** 0.679 vs policy min 0.60 · **Close:** 570 · **ATR14:** 50.4 · **Volume ratio 20D:** 1.32 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 555–720, entry trigger **720**, stop **685**, risk 35 points (4.86%).

**Targets:** TP1 **755** (1.00R), TP2 **780** (1.71R), TP3 **805** (2.43R). Recommended base-case RR: **1.71R**.

**Why entry:** Entry trigger 720 is set above recent resistance 715 plus one IDX tick. This requires confirmation instead of buying blindly at close 570. Entry is valid only if price can trade/hold around 720 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 685 is capped by max risk 4.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 755 (1.00R), TP2 780 (1.71R), TP3 805 (2.43R). Targets are ATR/structure capped for hold_days=1. ATR14=50.4, resistance_5/10/20/60=715/740/840/885. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 26.32% > max 5.00%; entry-to-stop risk 4.86% exceeds max strategy risk 4.50%; TP1 reward/risk 1.00R is below strategy minimum 1.10R

**Risk flags:** OK

**Strategy risk note:** Top-1 short-horizon scalp; invalidation must be quick.

---

## MBMA — position_xgb — NO_TRADE

**Score:** 0.597 vs policy min 0.55 · **Close:** 434 · **ATR14:** 48.9 · **Volume ratio 20D:** 0.73 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 410–440, entry trigger **440**, stop **400**, risk 40 points (9.09%).

**Targets:** TP1 **494** (1.35R), TP2 **510** (1.75R), TP3 **540** (2.50R). Recommended base-case RR: **1.75R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 434: zone 410–440 uses ATR14 48.9 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 440 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 400 is capped by max risk 9.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 494 (1.35R), TP2 510 (1.75R), TP3 540 (2.50R). Targets are ATR/structure capped for hold_days=1. ATR14=48.9, resistance_5/10/20/60=494/510/680/855. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 9.09% exceeds max strategy risk 9.00%

**Risk flags:** OK

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## ESSA — position_xgb — NO_TRADE

**Score:** 0.597 vs policy min 0.55 · **Close:** 585 · **ATR14:** 58.2 · **Volume ratio 20D:** 0.53 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 555–595, entry trigger **595**, stop **540**, risk 55 points (9.24%).

**Targets:** TP1 **680** (1.55R), TP2 **710** (2.09R), TP3 **730** (2.45R). Recommended base-case RR: **2.09R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 585: zone 555–595 uses ATR14 58.2 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 595 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 540 is placed below support structure (545 / 545). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 680 (1.55R), TP2 710 (2.09R), TP3 730 (2.45R). Targets are ATR/structure capped for hold_days=1. ATR14=58.2, resistance_5/10/20/60=710/755/915/995. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 9.24% exceeds max strategy risk 9.00%; volume ratio 0.53 below required 0.60

**Risk flags:** OK

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## APIC — market_maker_silent_accum_defensive — NO_TRADE

**Score:** 0.566 vs policy min 0.55 · **Close:** 515 · **ATR14:** 227.5 · **Volume ratio 20D:** 2.13 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 434–565, entry trigger **565**, stop **520**, risk 45 points (7.96%).

**Targets:** TP1 **680** (2.56R), TP2 **705** (3.11R), TP3 **730** (3.67R). Recommended base-case RR: **3.11R**.

**Why entry:** Hybrid entry uses close 515 and ATR14 227.5: buy zone 434–565. Entry is valid only if price can trade/hold around 565 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 520 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 680 (2.56R), TP2 705 (3.11R), TP3 730 (3.67R). Targets are ATR/structure capped for hold_days=1. ATR14=227.5, resistance_5/10/20/60=1,200/1,725/2,090/2,410. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 9.71% > max 8.00%; entry-to-stop risk 7.96% exceeds max strategy risk 7.50%

**Risk flags:** OK

**Strategy risk note:** Defensive accumulation. Prefer retest and clean broker flow.

---

## ESTI — market_maker_silent_accum_defensive — NO_TRADE

**Score:** 0.551 vs policy min 0.55 · **Close:** 123 · **ATR14:** 19.2 · **Volume ratio 20D:** 3.15 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 116–127, entry trigger **127**, stop **117**, risk 10 points (7.87%).

**Targets:** TP1 **137** (1.00R), TP2 **162** (3.50R), TP3 **165** (3.80R). Recommended base-case RR: **3.50R**.

**Why entry:** Hybrid entry uses close 123 and ATR14 19.2: buy zone 116–127. Entry is valid only if price can trade/hold around 127 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 117 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 137 (1.00R), TP2 162 (3.50R), TP3 165 (3.80R). Targets are ATR/structure capped for hold_days=1. ATR14=19.2, resistance_5/10/20/60=165/165/177/248. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.87% exceeds max strategy risk 7.50%; TP1 reward/risk 1.00R is below strategy minimum 1.25R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Defensive accumulation. Prefer retest and clean broker flow.

---

## TRIN — market_maker_silent_accum_defensive — NO_TRADE

**Score:** 0.546 vs policy min 0.55 · **Close:** 312 · **ATR14:** 67.4 · **Volume ratio 20D:** 1.59 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 288–326, entry trigger **326**, stop **300**, risk 26 points (7.98%).

**Targets:** TP1 **360** (1.31R), TP2 **372** (1.77R), TP3 **486** (6.15R). Recommended base-case RR: **1.77R**.

**Why entry:** Hybrid entry uses close 312 and ATR14 67.4: buy zone 288–326. Entry is valid only if price can trade/hold around 326 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 300 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 360 (1.31R), TP2 372 (1.77R), TP3 486 (6.15R). Targets are ATR/structure capped for hold_days=1. ATR14=67.4, resistance_5/10/20/60=486/580/715/1,120. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.98% exceeds max strategy risk 7.50%; score 0.546 below policy min_score 0.55

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Defensive accumulation. Prefer retest and clean broker flow.

---

## BULL — momentum_5d_hgb_defensive — NO_TRADE

**Score:** 0.535 vs policy min 0.55 · **Close:** 298 · **ATR14:** 46.3 · **Volume ratio 20D:** 0.89 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 288–430, entry trigger **430**, stop **398**, risk 32 points (7.44%).

**Targets:** TP1 **462** (1.00R), TP2 **486** (1.75R), TP3 **545** (3.59R). Recommended base-case RR: **1.75R**.

**Why entry:** Entry trigger 430 is set above recent resistance 428 plus one IDX tick. This requires confirmation instead of buying blindly at close 298. Entry is valid only if price can trade/hold around 430 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 398 is capped by max risk 7.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 462 (1.00R), TP2 486 (1.75R), TP3 545 (3.59R). Targets are ATR/structure capped for hold_days=1. ATR14=46.3, resistance_5/10/20/60=410/428/545/610. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 44.30% > max 8.00%; entry-to-stop risk 7.44% exceeds max strategy risk 7.00%; score 0.535 below policy min_score 0.55; TP1 reward/risk 1.00R is below strategy minimum 1.25R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Selective high-liquidity 5D momentum sleeve.

---

## SUPA — momentum_5d_hgb_defensive — NO_TRADE

**Score:** 0.508 vs policy min 0.55 · **Close:** 705 · **ATR14:** 42.1 · **Volume ratio 20D:** 2.13 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 695–910, entry trigger **910**, stop **860**, risk 50 points (5.49%).

**Targets:** TP1 **955** (0.90R), TP2 **985** (1.50R), TP3 **1,020** (2.20R). Recommended base-case RR: **1.50R**.

**Why entry:** Entry trigger 910 is set above recent resistance 905 plus one IDX tick. This requires confirmation instead of buying blindly at close 705. Entry is valid only if price can trade/hold around 910 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 860 uses 1.15×ATR14 volatility cap. Thesis invalidates if the move reverses beyond normal volatility. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 955 (0.90R), TP2 985 (1.50R), TP3 1,020 (2.20R). Targets are ATR/structure capped for hold_days=1. ATR14=42.1, resistance_5/10/20/60=880/905/905/1,080. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 29.08% > max 8.00%; score 0.508 below policy min_score 0.55; TP1 reward/risk 0.90R is below strategy minimum 1.25R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Selective high-liquidity 5D momentum sleeve.

---

## FUJI — market_maker_silent_accum_defensive — NO_TRADE

**Score:** 0.500 vs policy min 0.55 · **Close:** 276 · **ATR14:** 26.4 · **Volume ratio 20D:** 1.58 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 266–282, entry trigger **282**, stop **260**, risk 22 points (7.80%).

**Targets:** TP1 **304** (1.00R), TP2 **324** (1.91R), TP3 **336** (2.45R). Recommended base-case RR: **1.91R**.

**Why entry:** Hybrid entry uses close 276 and ATR14 26.4: buy zone 266–282. Entry is valid only if price can trade/hold around 282 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 260 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 304 (1.00R), TP2 324 (1.91R), TP3 336 (2.45R). Targets are ATR/structure capped for hold_days=1. ATR14=26.4, resistance_5/10/20/60=324/324/348/460. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.80% exceeds max strategy risk 7.50%; score 0.500 below policy min_score 0.55; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Defensive accumulation. Prefer retest and clean broker flow.

---

## SCMA — market_maker_silent_accum_defensive — NO_TRADE

**Score:** 0.490 vs policy min 0.55 · **Close:** 193 · **ATR14:** 14.9 · **Volume ratio 20D:** 0.92 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 187–196, entry trigger **196**, stop **181**, risk 15 points (7.65%).

**Targets:** TP1 **212** (1.07R), TP2 **224** (1.87R), TP3 **232** (2.40R). Recommended base-case RR: **1.87R**.

**Why entry:** Hybrid entry uses close 193 and ATR14 14.9: buy zone 187–196. Entry is valid only if price can trade/hold around 196 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 181 is placed below support structure (182 / 182). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 212 (1.07R), TP2 224 (1.87R), TP3 232 (2.40R). Targets are ATR/structure capped for hold_days=1. ATR14=14.9, resistance_5/10/20/60=232/240/268/312. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.65% exceeds max strategy risk 7.50%; score 0.490 below policy min_score 0.55; TP1 reward/risk 1.07R is below strategy minimum 1.25R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Defensive accumulation. Prefer retest and clean broker flow.

---

## IRSX — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.445 vs policy min 0.60 · **Close:** 242 · **ATR14:** 50.1 · **Volume ratio 20D:** 0.91 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 230–462, entry trigger **462**, stop **414**, risk 48 points (10.39%).

**Targets:** TP1 **510** (1.00R), TP2 **545** (1.73R), TP3 **580** (2.46R). Recommended base-case RR: **1.73R**.

**Why entry:** Entry trigger 462 is set above recent resistance 460 plus one IDX tick. This requires confirmation instead of buying blindly at close 242. Entry is valid only if price can trade/hold around 462 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 414 is capped by max risk 10.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 510 (1.00R), TP2 545 (1.73R), TP3 580 (2.46R). Targets are ATR/structure capped for hold_days=2. ATR14=50.1, resistance_5/10/20/60=386/460/480/675. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 90.91% > max 15.00%; entry-to-stop risk 10.39% exceeds max strategy risk 10.00%; score 0.445 below policy min_score 0.60; TP1 reward/risk 1.00R is below strategy minimum 1.40R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## VKTR — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.442 vs policy min 0.60 · **Close:** 605 · **ATR14:** 94.6 · **Volume ratio 20D:** 0.95 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 585–835, entry trigger **835**, stop **750**, risk 85 points (10.18%).

**Targets:** TP1 **995** (1.88R), TP2 **1,040** (2.41R), TP3 **1,085** (2.94R). Recommended base-case RR: **2.41R**.

**Why entry:** Entry trigger 835 is set above recent resistance 830 plus one IDX tick. This requires confirmation instead of buying blindly at close 605. Entry is valid only if price can trade/hold around 835 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 750 is capped by max risk 10.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 995 (1.88R), TP2 1,040 (2.41R), TP3 1,085 (2.94R). Targets are ATR/structure capped for hold_days=2. ATR14=94.6, resistance_5/10/20/60=830/830/995/1,090. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 38.02% > max 15.00%; entry-to-stop risk 10.18% exceeds max strategy risk 10.00%; score 0.442 below policy min_score 0.60

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## RMKO — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.437 vs policy min 0.60 · **Close:** 258 · **ATR14:** 47.4 · **Volume ratio 20D:** 1.07 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 248–414, entry trigger **414**, stop **372**, risk 42 points (10.14%).

**Targets:** TP1 **505** (2.17R), TP2 **530** (2.76R), TP3 **555** (3.36R). Recommended base-case RR: **2.76R**.

**Why entry:** Entry trigger 414 is set above recent resistance 412 plus one IDX tick. This requires confirmation instead of buying blindly at close 258. Entry is valid only if price can trade/hold around 414 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 372 is capped by max risk 10.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 505 (2.17R), TP2 530 (2.76R), TP3 555 (3.36R). Targets are ATR/structure capped for hold_days=2. ATR14=47.4, resistance_5/10/20/60=372/412/505/865. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 60.47% > max 15.00%; entry-to-stop risk 10.14% exceeds max strategy risk 10.00%; score 0.437 below policy min_score 0.60; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## DKFT — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.429 vs policy min 0.60 · **Close:** 570 · **ATR14:** 50.4 · **Volume ratio 20D:** 1.32 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 555–745, entry trigger **745**, stop **675**, risk 70 points (9.40%).

**Targets:** TP1 **840** (1.36R), TP2 **865** (1.71R), TP3 **915** (2.43R). Recommended base-case RR: **1.71R**.

**Why entry:** Entry trigger 745 is set above recent resistance 740 plus one IDX tick. This requires confirmation instead of buying blindly at close 570. Entry is valid only if price can trade/hold around 745 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 675 uses 1.30×ATR14 volatility cap. Thesis invalidates if the move reverses beyond normal volatility. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 840 (1.36R), TP2 865 (1.71R), TP3 915 (2.43R). Targets are ATR/structure capped for hold_days=2. ATR14=50.4, resistance_5/10/20/60=715/740/840/885. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 30.70% > max 15.00%; score 0.429 below policy min_score 0.60; TP1 reward/risk 1.36R is below strategy minimum 1.40R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## MMIX — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.428 vs policy min 0.60 · **Close:** 750 · **ATR14:** 102.8 · **Volume ratio 20D:** 6.65 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 725–790, entry trigger **790**, stop **710**, risk 80 points (10.13%).

**Targets:** TP1 **870** (1.00R), TP2 **930** (1.75R), TP3 **985** (2.44R). Recommended base-case RR: **1.75R**.

**Why entry:** Entry trigger 790 is set above recent resistance 785 plus one IDX tick. This requires confirmation instead of buying blindly at close 750. Entry is valid only if price can trade/hold around 790 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 710 is capped by max risk 10.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 870 (1.00R), TP2 930 (1.75R), TP3 985 (2.44R). Targets are ATR/structure capped for hold_days=2. ATR14=102.8, resistance_5/10/20/60=785/785/785/785. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 10.13% exceeds max strategy risk 10.00%; score 0.428 below policy min_score 0.60; TP1 reward/risk 1.00R is below strategy minimum 1.40R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## BIPI — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.427 vs policy min 0.60 · **Close:** 137 · **ATR14:** 22.9 · **Volume ratio 20D:** 0.47 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 132–214, entry trigger **214**, stop **192**, risk 22 points (10.28%).

**Targets:** TP1 **258** (2.00R), TP2 **262** (2.18R), TP3 **268** (2.45R). Recommended base-case RR: **2.18R**.

**Why entry:** Entry trigger 214 is set above recent resistance 212 plus one IDX tick. This requires confirmation instead of buying blindly at close 137. Entry is valid only if price can trade/hold around 214 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 192 is capped by max risk 10.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 258 (2.00R), TP2 262 (2.18R), TP3 268 (2.45R). Targets are ATR/structure capped for hold_days=2. ATR14=22.9, resistance_5/10/20/60=190/212/262/342. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 56.20% > max 15.00%; entry-to-stop risk 10.28% exceeds max strategy risk 10.00%; score 0.427 below policy min_score 0.60; volume ratio 0.47 below required 0.60

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## SSMS — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.426 vs policy min 0.60 · **Close:** 700 · **ATR14:** 96.8 · **Volume ratio 20D:** 0.94 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 680–1,000, entry trigger **1,000**, stop **900**, risk 100 points (10.00%).

**Targets:** TP1 **1,100** (1.00R), TP2 **1,170** (1.70R), TP3 **1,445** (4.45R). Recommended base-case RR: **1.70R**.

**Why entry:** Entry trigger 1,000 is set above recent resistance 995 plus one IDX tick. This requires confirmation instead of buying blindly at close 700. Entry is valid only if price can trade/hold around 1,000 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 900 is capped by max risk 10.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,100 (1.00R), TP2 1,170 (1.70R), TP3 1,445 (4.45R). Targets are ATR/structure capped for hold_days=2. ATR14=96.8, resistance_5/10/20/60=825/995/1,445/1,685. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 42.86% > max 15.00%; score 0.426 below policy min_score 0.60; TP1 reward/risk 1.00R is below strategy minimum 1.40R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## GTSI — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.425 vs policy min 0.60 · **Close:** 109 · **ATR14:** 20.3 · **Volume ratio 20D:** 0.87 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 104–193, entry trigger **193**, stop **173**, risk 20 points (10.36%).

**Targets:** TP1 **232** (1.95R), TP2 **238** (2.25R), TP3 **242** (2.45R). Recommended base-case RR: **2.25R**.

**Why entry:** Entry trigger 193 is set above recent resistance 192 plus one IDX tick. This requires confirmation instead of buying blindly at close 109. Entry is valid only if price can trade/hold around 193 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 173 is capped by max risk 10.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 232 (1.95R), TP2 238 (2.25R), TP3 242 (2.45R). Targets are ATR/structure capped for hold_days=2. ATR14=20.3, resistance_5/10/20/60=164/192/238/334. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 77.06% > max 15.00%; entry-to-stop risk 10.36% exceeds max strategy risk 10.00%; score 0.425 below policy min_score 0.60

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## CDIA — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.423 vs policy min 0.60 · **Close:** 640 · **ATR14:** 106.8 · **Volume ratio 20D:** 0.73 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 615–955, entry trigger **955**, stop **855**, risk 100 points (10.47%).

**Targets:** TP1 **1,055** (1.00R), TP2 **1,230** (2.75R), TP3 **1,280** (3.25R). Recommended base-case RR: **2.75R**.

**Why entry:** Entry trigger 955 is set above recent resistance 950 plus one IDX tick. This requires confirmation instead of buying blindly at close 640. Entry is valid only if price can trade/hold around 955 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 855 is capped by max risk 10.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,055 (1.00R), TP2 1,230 (2.75R), TP3 1,280 (3.25R). Targets are ATR/structure capped for hold_days=2. ATR14=106.8, resistance_5/10/20/60=950/950/1,230/1,340. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 49.22% > max 15.00%; entry-to-stop risk 10.47% exceeds max strategy risk 10.00%; score 0.423 below policy min_score 0.60; TP1 reward/risk 1.00R is below strategy minimum 1.40R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## TRIN — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.420 vs policy min 0.60 · **Close:** 312 · **ATR14:** 67.4 · **Volume ratio 20D:** 1.59 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 298–585, entry trigger **585**, stop **525**, risk 60 points (10.26%).

**Targets:** TP1 **710** (2.08R), TP2 **715** (2.17R), TP3 **730** (2.42R). Recommended base-case RR: **2.17R**.

**Why entry:** Entry trigger 585 is set above recent resistance 580 plus one IDX tick. This requires confirmation instead of buying blindly at close 312. Entry is valid only if price can trade/hold around 585 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 525 is capped by max risk 10.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 710 (2.08R), TP2 715 (2.17R), TP3 730 (2.42R). Targets are ATR/structure capped for hold_days=2. ATR14=67.4, resistance_5/10/20/60=486/580/715/1,120. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 87.50% > max 15.00%; entry-to-stop risk 10.26% exceeds max strategy risk 10.00%; score 0.420 below policy min_score 0.60

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## DEWA — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.420 vs policy min 0.60 · **Close:** 262 · **ATR14:** 45.2 · **Volume ratio 20D:** 0.92 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 252–400, entry trigger **400**, stop **360**, risk 40 points (10.00%).

**Targets:** TP1 **440** (1.00R), TP2 **535** (3.38R), TP3 **555** (3.88R). Recommended base-case RR: **3.38R**.

**Why entry:** Entry trigger 400 is set above recent resistance 398 plus one IDX tick. This requires confirmation instead of buying blindly at close 262. Entry is valid only if price can trade/hold around 400 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 360 is capped by max risk 10.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 440 (1.00R), TP2 535 (3.38R), TP3 555 (3.88R). Targets are ATR/structure capped for hold_days=2. ATR14=45.2, resistance_5/10/20/60=352/398/535/595. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 52.67% > max 15.00%; score 0.420 below policy min_score 0.60; TP1 reward/risk 1.00R is below strategy minimum 1.40R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## APIC — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.419 vs policy min 0.60 · **Close:** 515 · **ATR14:** 227.5 · **Volume ratio 20D:** 2.13 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 472–1,730, entry trigger **1,730**, stop **1,555**, risk 175 points (10.12%).

**Targets:** TP1 **2,090** (2.06R), TP2 **2,180** (2.57R), TP3 **2,270** (3.09R). Recommended base-case RR: **2.57R**.

**Why entry:** Entry trigger 1,730 is set above recent resistance 1,725 plus one IDX tick. This requires confirmation instead of buying blindly at close 515. Entry is valid only if price can trade/hold around 1,730 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 1,555 is capped by max risk 10.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 2,090 (2.06R), TP2 2,180 (2.57R), TP3 2,270 (3.09R). Targets are ATR/structure capped for hold_days=2. ATR14=227.5, resistance_5/10/20/60=1,200/1,725/2,090/2,410. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 235.92% > max 15.00%; entry-to-stop risk 10.12% exceeds max strategy risk 10.00%; score 0.419 below policy min_score 0.60

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## HUMI — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.419 vs policy min 0.60 · **Close:** 100 · **ATR14:** 18.4 · **Volume ratio 20D:** 0.80 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 96–175, entry trigger **175**, stop **157**, risk 18 points (10.29%).

**Targets:** TP1 **195** (1.11R), TP2 **206** (1.72R), TP3 **220** (2.50R). Recommended base-case RR: **1.72R**.

**Why entry:** Entry trigger 175 is set above recent resistance 174 plus one IDX tick. This requires confirmation instead of buying blindly at close 100. Entry is valid only if price can trade/hold around 175 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 157 is capped by max risk 10.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 195 (1.11R), TP2 206 (1.72R), TP3 220 (2.50R). Targets are ATR/structure capped for hold_days=2. ATR14=18.4, resistance_5/10/20/60=151/174/195/260. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 75.00% > max 15.00%; entry-to-stop risk 10.29% exceeds max strategy risk 10.00%; score 0.419 below policy min_score 0.60; TP1 reward/risk 1.11R is below strategy minimum 1.40R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## TOBA — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.417 vs policy min 0.60 · **Close:** 346 · **ATR14:** 38.6 · **Volume ratio 20D:** 0.62 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 338–496, entry trigger **496**, stop **446**, risk 50 points (10.08%).

**Targets:** TP1 **550** (1.08R), TP2 **625** (2.58R), TP3 **650** (3.08R). Recommended base-case RR: **2.58R**.

**Why entry:** Entry trigger 496 is set above recent resistance 494 plus one IDX tick. This requires confirmation instead of buying blindly at close 346. Entry is valid only if price can trade/hold around 496 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 446 is capped by max risk 10.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 550 (1.08R), TP2 625 (2.58R), TP3 650 (3.08R). Targets are ATR/structure capped for hold_days=2. ATR14=38.6, resistance_5/10/20/60=452/494/650/815. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 43.35% > max 15.00%; entry-to-stop risk 10.08% exceeds max strategy risk 10.00%; score 0.417 below policy min_score 0.60; TP1 reward/risk 1.08R is below strategy minimum 1.40R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## CYBR — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.416 vs policy min 0.60 · **Close:** 550 · **ATR14:** 88.2 · **Volume ratio 20D:** 0.71 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 530–645, entry trigger **645**, stop **580**, risk 65 points (10.08%).

**Targets:** TP1 **710** (1.00R), TP2 **760** (1.77R), TP3 **805** (2.46R). Recommended base-case RR: **1.77R**.

**Why entry:** Entry trigger 645 is set above recent resistance 640 plus one IDX tick. This requires confirmation instead of buying blindly at close 550. Entry is valid only if price can trade/hold around 645 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 580 is capped by max risk 10.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 710 (1.00R), TP2 760 (1.77R), TP3 805 (2.46R). Targets are ATR/structure capped for hold_days=2. ATR14=88.2, resistance_5/10/20/60=620/640/1,330/1,590. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 17.27% > max 15.00%; entry-to-stop risk 10.08% exceeds max strategy risk 10.00%; score 0.416 below policy min_score 0.60; TP1 reward/risk 1.00R is below strategy minimum 1.40R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## ASPR — ara_candidate — NO_TRADE

**Score:** 0.357 vs policy min 0.50 · **Close:** 134 · **ATR14:** 59.8 · **Volume ratio 20D:** 0.42 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 123–545, entry trigger **545**, stop **490**, risk 55 points (10.09%).

**Targets:** TP1 **605** (1.09R), TP2 **640** (1.73R), TP3 **680** (2.45R). Recommended base-case RR: **1.73R**.

**Why entry:** Entry trigger 545 is set above recent resistance 540 plus one IDX tick. This requires confirmation instead of buying blindly at close 134. Entry is valid only if price can trade/hold around 545 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 490 is capped by max risk 10.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 605 (1.09R), TP2 640 (1.73R), TP3 680 (2.45R). Targets are ATR/structure capped for hold_days=1. ATR14=59.8, resistance_5/10/20/60=224/540/620/620. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 306.72% > max 12.00%; entry-to-stop risk 10.09% exceeds max strategy risk 10.00%; score 0.357 below policy min_score 0.50; TP1 reward/risk 1.09R is below strategy minimum 1.30R; volume ratio 0.42 below required 0.60; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** High drawdown tactical setup. Use as execution only if confirmation is strong and liquidity is clean.

---
