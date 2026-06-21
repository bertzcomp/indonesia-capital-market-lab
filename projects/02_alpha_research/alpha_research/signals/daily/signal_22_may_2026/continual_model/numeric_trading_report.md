# Numeric Trading Desk Report — 2026-05-21

This report is generated from live model scores, selected signal policy, canonical OHLCV, ATR, support/resistance, liquidity, and broker-flow diagnostics. It is not a simple BUY/SELL list; each plan is conditional on execution behaviour.

## Summary

| Plan quality | Count |
|---|---:|
| ACTIONABLE | 12 |
| CONDITIONAL | 23 |
| NO_TRADE | 7 |

## CDIA — ara_candidate_continual — ACTIONABLE

**Score:** 0.873 vs policy min 0.50 · **Close:** 705 · **ATR14:** 105.7 · **Volume ratio 20D:** 0.79 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 665–730, entry trigger **730**, stop **690**, risk 40 points (5.48%).

**Targets:** TP1 **785** (1.38R), TP2 **800** (1.75R), TP3 **995** (6.62R). Recommended base-case RR: **1.75R**.

**Why entry:** Hybrid entry uses close 705 and ATR14 105.7: buy zone 665–730. Entry is valid only if price can trade/hold around 730 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 690 is placed below support structure (695 / 695). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 785 (1.38R), TP2 800 (1.75R), TP3 995 (6.62R). Targets are ATR/structure capped for hold_days=1. ATR14=105.7, resistance_5/10/20/60=1,035/1,230/1,340/1,340. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BRMS — scalping_continual_defensive — ACTIONABLE

**Score:** 0.752 vs policy min 0.05 · **Close:** 565 · **ATR14:** 59.6 · **Volume ratio 20D:** 2.73 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 540–580, entry trigger **580**, stop **560**, risk 20 points (3.45%).

**Targets:** TP1 **610** (1.50R), TP2 **615** (1.75R), TP3 **630** (2.50R). Recommended base-case RR: **1.75R**.

**Why entry:** Hybrid entry uses close 565 and ATR14 59.6: buy zone 540–580. Entry is valid only if price can trade/hold around 580 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 560 is placed below support structure (565 / 565). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 610 (1.50R), TP2 615 (1.75R), TP3 630 (2.50R). Targets are ATR/structure capped for hold_days=1. ATR14=59.6, resistance_5/10/20/60=785/835/930/1,120. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## INET — scalping_continual_defensive — ACTIONABLE

**Score:** 0.722 vs policy min 0.05 · **Close:** 218 · **ATR14:** 25.1 · **Volume ratio 20D:** 1.09 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 208–224, entry trigger **224**, stop **216**, risk 8 points (3.57%).

**Targets:** TP1 **238** (1.75R), TP2 **242** (2.25R), TP3 **288** (8.00R). Recommended base-case RR: **2.25R**.

**Why entry:** Hybrid entry uses close 218 and ATR14 25.1: buy zone 208–224. Entry is valid only if price can trade/hold around 224 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 216 is placed below support structure (218 / 218). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 238 (1.75R), TP2 242 (2.25R), TP3 288 (8.00R). Targets are ATR/structure capped for hold_days=1. ATR14=25.1, resistance_5/10/20/60=296/324/360/438. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BRMS — momentum_10d_continual_aggressive — ACTIONABLE

**Score:** 0.630 vs policy min 0.30 · **Close:** 565 · **ATR14:** 59.6 · **Volume ratio 20D:** 2.73 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 540–580, entry trigger **580**, stop **560**, risk 20 points (3.45%).

**Targets:** TP1 **610** (1.50R), TP2 **785** (10.25R), TP3 **795** (10.75R). Recommended base-case RR: **10.25R**.

**Why entry:** Hybrid entry uses close 565 and ATR14 59.6: buy zone 540–580. Entry is valid only if price can trade/hold around 580 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 560 is placed below support structure (565 / 565). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 610 (1.50R), TP2 785 (10.25R), TP3 795 (10.75R). Targets are ATR/structure capped for hold_days=5. ATR14=59.6, resistance_5/10/20/60=785/835/930/1,120. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## INET — momentum_10d_continual_aggressive — ACTIONABLE

**Score:** 0.630 vs policy min 0.30 · **Close:** 218 · **ATR14:** 25.1 · **Volume ratio 20D:** 1.09 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 208–224, entry trigger **224**, stop **216**, risk 8 points (3.57%).

**Targets:** TP1 **238** (1.75R), TP2 **296** (9.00R), TP3 **300** (9.50R). Recommended base-case RR: **9.00R**.

**Why entry:** Hybrid entry uses close 218 and ATR14 25.1: buy zone 208–224. Entry is valid only if price can trade/hold around 224 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 216 is placed below support structure (218 / 218). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 238 (1.75R), TP2 296 (9.00R), TP3 300 (9.50R). Targets are ATR/structure capped for hold_days=5. ATR14=25.1, resistance_5/10/20/60=296/324/360/438. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BRMS — momentum_5d_continual_defensive — ACTIONABLE

**Score:** 0.614 vs policy min 0.30 · **Close:** 565 · **ATR14:** 59.6 · **Volume ratio 20D:** 2.73 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 540–580, entry trigger **580**, stop **560**, risk 20 points (3.45%).

**Targets:** TP1 **610** (1.50R), TP2 **770** (9.50R), TP3 **785** (10.25R). Recommended base-case RR: **9.50R**.

**Why entry:** Hybrid entry uses close 565 and ATR14 59.6: buy zone 540–580. Entry is valid only if price can trade/hold around 580 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 560 is placed below support structure (565 / 565). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 610 (1.50R), TP2 770 (9.50R), TP3 785 (10.25R). Targets are ATR/structure capped for hold_days=3. ATR14=59.6, resistance_5/10/20/60=785/835/930/1,120. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BRMS — swing_continual_defensive — ACTIONABLE

**Score:** 0.614 vs policy min 0.30 · **Close:** 565 · **ATR14:** 59.6 · **Volume ratio 20D:** 2.73 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 540–580, entry trigger **580**, stop **560**, risk 20 points (3.45%).

**Targets:** TP1 **610** (1.50R), TP2 **615** (1.75R), TP3 **630** (2.50R). Recommended base-case RR: **1.75R**.

**Why entry:** Hybrid entry uses close 565 and ATR14 59.6: buy zone 540–580. Entry is valid only if price can trade/hold around 580 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 560 is placed below support structure (565 / 565). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 610 (1.50R), TP2 615 (1.75R), TP3 630 (2.50R). Targets are ATR/structure capped for hold_days=1. ATR14=59.6, resistance_5/10/20/60=785/835/930/1,120. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## INET — momentum_5d_continual_defensive — ACTIONABLE

**Score:** 0.591 vs policy min 0.30 · **Close:** 218 · **ATR14:** 25.1 · **Volume ratio 20D:** 1.09 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 208–224, entry trigger **224**, stop **216**, risk 8 points (3.57%).

**Targets:** TP1 **238** (1.75R), TP2 **296** (9.00R), TP3 **300** (9.50R). Recommended base-case RR: **9.00R**.

**Why entry:** Hybrid entry uses close 218 and ATR14 25.1: buy zone 208–224. Entry is valid only if price can trade/hold around 224 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 216 is placed below support structure (218 / 218). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 238 (1.75R), TP2 296 (9.00R), TP3 300 (9.50R). Targets are ATR/structure capped for hold_days=3. ATR14=25.1, resistance_5/10/20/60=296/324/360/438. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## INET — swing_continual_defensive — ACTIONABLE

**Score:** 0.591 vs policy min 0.30 · **Close:** 218 · **ATR14:** 25.1 · **Volume ratio 20D:** 1.09 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 208–224, entry trigger **224**, stop **216**, risk 8 points (3.57%).

**Targets:** TP1 **238** (1.75R), TP2 **242** (2.25R), TP3 **288** (8.00R). Recommended base-case RR: **2.25R**.

**Why entry:** Hybrid entry uses close 218 and ATR14 25.1: buy zone 208–224. Entry is valid only if price can trade/hold around 224 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 216 is placed below support structure (218 / 218). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 238 (1.75R), TP2 242 (2.25R), TP3 288 (8.00R). Targets are ATR/structure capped for hold_days=1. ATR14=25.1, resistance_5/10/20/60=296/324/360/438. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## CDIA — position_continual — ACTIONABLE

**Score:** 0.332 vs policy min 0.30 · **Close:** 705 · **ATR14:** 105.7 · **Volume ratio 20D:** 0.79 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 665–730, entry trigger **730**, stop **690**, risk 40 points (5.48%).

**Targets:** TP1 **1,035** (7.62R), TP2 **1,055** (8.12R), TP3 **1,075** (8.62R). Recommended base-case RR: **8.12R**.

**Why entry:** Hybrid entry uses close 705 and ATR14 105.7: buy zone 665–730. Entry is valid only if price can trade/hold around 730 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 690 is placed below support structure (695 / 695). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,035 (7.62R), TP2 1,055 (8.12R), TP3 1,075 (8.62R). Targets are ATR/structure capped for hold_days=10. ATR14=105.7, resistance_5/10/20/60=1,035/1,230/1,340/1,340. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## MBMA — position_continual — ACTIONABLE

**Score:** 0.329 vs policy min 0.30 · **Close:** 440 · **ATR14:** 52.0 · **Volume ratio 20D:** 1.08 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 420–452, entry trigger **452**, stop **422**, risk 30 points (6.64%).

**Targets:** TP1 **615** (5.43R), TP2 **630** (5.93R), TP3 **645** (6.43R). Recommended base-case RR: **5.93R**.

**Why entry:** Hybrid entry uses close 440 and ATR14 52.0: buy zone 420–452. Entry is valid only if price can trade/hold around 452 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 422 is placed below support structure (424 / 424). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 615 (5.43R), TP2 630 (5.93R), TP3 645 (6.43R). Targets are ATR/structure capped for hold_days=10. ATR14=52.0, resistance_5/10/20/60=615/710/775/945. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## INET — position_continual — ACTIONABLE

**Score:** 0.328 vs policy min 0.30 · **Close:** 218 · **ATR14:** 25.1 · **Volume ratio 20D:** 1.09 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 208–224, entry trigger **224**, stop **216**, risk 8 points (3.57%).

**Targets:** TP1 **296** (9.00R), TP2 **300** (9.50R), TP3 **304** (10.00R). Recommended base-case RR: **9.50R**.

**Why entry:** Hybrid entry uses close 218 and ATR14 25.1: buy zone 208–224. Entry is valid only if price can trade/hold around 224 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 216 is placed below support structure (218 / 218). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 296 (9.00R), TP2 300 (9.50R), TP3 304 (10.00R). Targets are ATR/structure capped for hold_days=10. ATR14=25.1, resistance_5/10/20/60=296/324/360/438. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## DEWA — scalping_continual_defensive — CONDITIONAL

**Score:** 0.752 vs policy min 0.05 · **Close:** 334 · **ATR14:** 38.8 · **Volume ratio 20D:** 1.88 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 320–342, entry trigger **342**, stop **322**, risk 20 points (5.85%).

**Targets:** TP1 **362** (1.00R), TP2 **376** (1.70R), TP3 **390** (2.40R). Recommended base-case RR: **1.70R**.

**Why entry:** Hybrid entry uses close 334 and ATR14 38.8: buy zone 320–342. Entry is valid only if price can trade/hold around 342 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 322 is placed below support structure (324 / 324). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 362 (1.00R), TP2 376 (1.70R), TP3 390 (2.40R). Targets are ATR/structure capped for hold_days=1. ATR14=38.8, resistance_5/10/20/60=505/535/595/655. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BUVA — scalping_continual_defensive — CONDITIONAL

**Score:** 0.730 vs policy min 0.05 · **Close:** 695 · **ATR14:** 113.9 · **Volume ratio 20D:** 1.28 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 655–720, entry trigger **720**, stop **690**, risk 30 points (4.17%).

**Targets:** TP1 **780** (2.00R), TP2 **795** (2.50R), TP3 **810** (3.00R). Recommended base-case RR: **2.50R**.

**Why entry:** Hybrid entry uses close 695 and ATR14 113.9: buy zone 655–720. Entry is valid only if price can trade/hold around 720 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 690 is placed below support structure (695 / 695). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 780 (2.00R), TP2 795 (2.50R), TP3 810 (3.00R). Targets are ATR/structure capped for hold_days=1. ATR14=113.9, resistance_5/10/20/60=1,130/1,175/1,390/1,695. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## PSAB — scalping_continual_defensive — CONDITIONAL

**Score:** 0.726 vs policy min 0.05 · **Close:** 372 · **ATR14:** 38.8 · **Volume ratio 20D:** 1.18 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 358–380, entry trigger **380**, stop **362**, risk 18 points (4.74%).

**Targets:** TP1 **400** (1.11R), TP2 **412** (1.78R), TP3 **424** (2.44R). Recommended base-case RR: **1.78R**.

**Why entry:** Hybrid entry uses close 372 and ATR14 38.8: buy zone 358–380. Entry is valid only if price can trade/hold around 380 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 362 is placed below support structure (364 / 364). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 400 (1.11R), TP2 412 (1.78R), TP3 424 (2.44R). Targets are ATR/structure capped for hold_days=1. ATR14=38.8, resistance_5/10/20/60=520/580/590/590. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.11R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BIPI — momentum_10d_continual_aggressive — CONDITIONAL

**Score:** 0.650 vs policy min 0.30 · **Close:** 172 · **ATR14:** 26.0 · **Volume ratio 20D:** 1.57 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 162–178, entry trigger **178**, stop **171**, risk 7 points (3.93%).

**Targets:** TP1 **234** (8.00R), TP2 **238** (8.57R), TP3 **242** (9.14R). Recommended base-case RR: **8.57R**.

**Why entry:** Hybrid entry uses close 172 and ATR14 26.0: buy zone 162–178. Entry is valid only if price can trade/hold around 178 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 171 is placed below support structure (172 / 172). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 234 (8.00R), TP2 238 (8.57R), TP3 242 (9.14R). Targets are ATR/structure capped for hold_days=5. ATR14=26.0, resistance_5/10/20/60=234/262/304/342. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## BUVA — momentum_10d_continual_aggressive — CONDITIONAL

**Score:** 0.645 vs policy min 0.30 · **Close:** 695 · **ATR14:** 113.9 · **Volume ratio 20D:** 1.28 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 655–720, entry trigger **720**, stop **690**, risk 30 points (4.17%).

**Targets:** TP1 **780** (2.00R), TP2 **1,130** (13.67R), TP3 **1,145** (14.17R). Recommended base-case RR: **13.67R**.

**Why entry:** Hybrid entry uses close 695 and ATR14 113.9: buy zone 655–720. Entry is valid only if price can trade/hold around 720 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 690 is placed below support structure (695 / 695). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 780 (2.00R), TP2 1,130 (13.67R), TP3 1,145 (14.17R). Targets are ATR/structure capped for hold_days=5. ATR14=113.9, resistance_5/10/20/60=1,130/1,175/1,390/1,695. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## BNBR — momentum_10d_continual_aggressive — CONDITIONAL

**Score:** 0.637 vs policy min 0.30 · **Close:** 126 · **ATR14:** 19.9 · **Volume ratio 20D:** 0.85 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 119–130, entry trigger **130**, stop **125**, risk 5 points (3.85%).

**Targets:** TP1 **140** (2.00R), TP2 **186** (11.20R), TP3 **189** (11.80R). Recommended base-case RR: **11.20R**.

**Why entry:** Hybrid entry uses close 126 and ATR14 19.9: buy zone 119–130. Entry is valid only if price can trade/hold around 130 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 125 is placed below support structure (126 / 126). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 140 (2.00R), TP2 186 (11.20R), TP3 189 (11.80R). Targets are ATR/structure capped for hold_days=5. ATR14=19.9, resistance_5/10/20/60=186/224/240/240. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## DEWA — momentum_10d_continual_aggressive — CONDITIONAL

**Score:** 0.636 vs policy min 0.30 · **Close:** 334 · **ATR14:** 38.8 · **Volume ratio 20D:** 1.88 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 320–342, entry trigger **342**, stop **322**, risk 20 points (5.85%).

**Targets:** TP1 **362** (1.00R), TP2 **500** (7.90R), TP3 **505** (8.15R). Recommended base-case RR: **7.90R**.

**Why entry:** Hybrid entry uses close 334 and ATR14 38.8: buy zone 320–342. Entry is valid only if price can trade/hold around 342 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 322 is placed below support structure (324 / 324). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 362 (1.00R), TP2 500 (7.90R), TP3 505 (8.15R). Targets are ATR/structure capped for hold_days=5. ATR14=38.8, resistance_5/10/20/60=505/535/595/655. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BUVA — momentum_5d_continual_defensive — CONDITIONAL

**Score:** 0.634 vs policy min 0.30 · **Close:** 695 · **ATR14:** 113.9 · **Volume ratio 20D:** 1.28 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 655–720, entry trigger **720**, stop **690**, risk 30 points (4.17%).

**Targets:** TP1 **780** (2.00R), TP2 **795** (2.50R), TP3 **1,130** (13.67R). Recommended base-case RR: **2.50R**.

**Why entry:** Hybrid entry uses close 695 and ATR14 113.9: buy zone 655–720. Entry is valid only if price can trade/hold around 720 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 690 is placed below support structure (695 / 695). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 780 (2.00R), TP2 795 (2.50R), TP3 1,130 (13.67R). Targets are ATR/structure capped for hold_days=3. ATR14=113.9, resistance_5/10/20/60=1,130/1,175/1,390/1,695. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## BUVA — swing_continual_defensive — CONDITIONAL

**Score:** 0.634 vs policy min 0.30 · **Close:** 695 · **ATR14:** 113.9 · **Volume ratio 20D:** 1.28 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 655–720, entry trigger **720**, stop **690**, risk 30 points (4.17%).

**Targets:** TP1 **780** (2.00R), TP2 **795** (2.50R), TP3 **810** (3.00R). Recommended base-case RR: **2.50R**.

**Why entry:** Hybrid entry uses close 695 and ATR14 113.9: buy zone 655–720. Entry is valid only if price can trade/hold around 720 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 690 is placed below support structure (695 / 695). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 780 (2.00R), TP2 795 (2.50R), TP3 810 (3.00R). Targets are ATR/structure capped for hold_days=1. ATR14=113.9, resistance_5/10/20/60=1,130/1,175/1,390/1,695. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## DEWA — momentum_5d_continual_defensive — CONDITIONAL

**Score:** 0.617 vs policy min 0.30 · **Close:** 334 · **ATR14:** 38.8 · **Volume ratio 20D:** 1.88 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 320–342, entry trigger **342**, stop **322**, risk 20 points (5.85%).

**Targets:** TP1 **362** (1.00R), TP2 **376** (1.70R), TP3 **505** (8.15R). Recommended base-case RR: **1.70R**.

**Why entry:** Hybrid entry uses close 334 and ATR14 38.8: buy zone 320–342. Entry is valid only if price can trade/hold around 342 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 322 is placed below support structure (324 / 324). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 362 (1.00R), TP2 376 (1.70R), TP3 505 (8.15R). Targets are ATR/structure capped for hold_days=3. ATR14=38.8, resistance_5/10/20/60=505/535/595/655. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## DEWA — swing_continual_defensive — CONDITIONAL

**Score:** 0.617 vs policy min 0.30 · **Close:** 334 · **ATR14:** 38.8 · **Volume ratio 20D:** 1.88 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 320–342, entry trigger **342**, stop **322**, risk 20 points (5.85%).

**Targets:** TP1 **362** (1.00R), TP2 **376** (1.70R), TP3 **390** (2.40R). Recommended base-case RR: **1.70R**.

**Why entry:** Hybrid entry uses close 334 and ATR14 38.8: buy zone 320–342. Entry is valid only if price can trade/hold around 342 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 322 is placed below support structure (324 / 324). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 362 (1.00R), TP2 376 (1.70R), TP3 390 (2.40R). Targets are ATR/structure capped for hold_days=1. ATR14=38.8, resistance_5/10/20/60=505/535/595/655. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BIPI — momentum_5d_continual_defensive — CONDITIONAL

**Score:** 0.605 vs policy min 0.30 · **Close:** 172 · **ATR14:** 26.0 · **Volume ratio 20D:** 1.57 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 162–178, entry trigger **178**, stop **171**, risk 7 points (3.93%).

**Targets:** TP1 **224** (6.57R), TP2 **234** (8.00R), TP3 **238** (8.57R). Recommended base-case RR: **8.00R**.

**Why entry:** Hybrid entry uses close 172 and ATR14 26.0: buy zone 162–178. Entry is valid only if price can trade/hold around 178 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 171 is placed below support structure (172 / 172). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 224 (6.57R), TP2 234 (8.00R), TP3 238 (8.57R). Targets are ATR/structure capped for hold_days=3. ATR14=26.0, resistance_5/10/20/60=234/262/304/342. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## BIPI — swing_continual_defensive — CONDITIONAL

**Score:** 0.605 vs policy min 0.30 · **Close:** 172 · **ATR14:** 26.0 · **Volume ratio 20D:** 1.57 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 162–178, entry trigger **178**, stop **171**, risk 7 points (3.93%).

**Targets:** TP1 **191** (1.86R), TP2 **226** (6.86R), TP3 **234** (8.00R). Recommended base-case RR: **6.86R**.

**Why entry:** Hybrid entry uses close 172 and ATR14 26.0: buy zone 162–178. Entry is valid only if price can trade/hold around 178 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 171 is placed below support structure (172 / 172). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 191 (1.86R), TP2 226 (6.86R), TP3 234 (8.00R). Targets are ATR/structure capped for hold_days=1. ATR14=26.0, resistance_5/10/20/60=234/262/304/342. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## BNBR — momentum_5d_continual_defensive — CONDITIONAL

**Score:** 0.603 vs policy min 0.30 · **Close:** 126 · **ATR14:** 19.9 · **Volume ratio 20D:** 0.85 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 119–130, entry trigger **130**, stop **125**, risk 5 points (3.85%).

**Targets:** TP1 **140** (2.00R), TP2 **186** (11.20R), TP3 **189** (11.80R). Recommended base-case RR: **11.20R**.

**Why entry:** Hybrid entry uses close 126 and ATR14 19.9: buy zone 119–130. Entry is valid only if price can trade/hold around 130 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 125 is placed below support structure (126 / 126). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 140 (2.00R), TP2 186 (11.20R), TP3 189 (11.80R). Targets are ATR/structure capped for hold_days=3. ATR14=19.9, resistance_5/10/20/60=186/224/240/240. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## BNBR — swing_continual_defensive — CONDITIONAL

**Score:** 0.603 vs policy min 0.30 · **Close:** 126 · **ATR14:** 19.9 · **Volume ratio 20D:** 0.85 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 119–130, entry trigger **130**, stop **125**, risk 5 points (3.85%).

**Targets:** TP1 **140** (2.00R), TP2 **143** (2.60R), TP3 **180** (10.00R). Recommended base-case RR: **2.60R**.

**Why entry:** Hybrid entry uses close 126 and ATR14 19.9: buy zone 119–130. Entry is valid only if price can trade/hold around 130 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 125 is placed below support structure (126 / 126). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 140 (2.00R), TP2 143 (2.60R), TP3 180 (10.00R). Targets are ATR/structure capped for hold_days=1. ATR14=19.9, resistance_5/10/20/60=186/224/240/240. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## VKTR — momentum_10d_continual_aggressive — CONDITIONAL

**Score:** 0.602 vs policy min 0.30 · **Close:** 655 · **ATR14:** 86.1 · **Volume ratio 20D:** 1.40 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 620–675, entry trigger **675**, stop **650**, risk 25 points (3.70%).

**Targets:** TP1 **870** (7.80R), TP2 **895** (8.80R), TP3 **910** (9.40R). Recommended base-case RR: **8.80R**.

**Why entry:** Hybrid entry uses close 655 and ATR14 86.1: buy zone 620–675. Entry is valid only if price can trade/hold around 675 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 650 is placed below support structure (655 / 655). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 870 (7.80R), TP2 895 (8.80R), TP3 910 (9.40R). Targets are ATR/structure capped for hold_days=5. ATR14=86.1, resistance_5/10/20/60=895/995/1,060/1,100. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## VKTR — momentum_5d_continual_defensive — CONDITIONAL

**Score:** 0.578 vs policy min 0.30 · **Close:** 655 · **ATR14:** 86.1 · **Volume ratio 20D:** 1.40 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 620–675, entry trigger **675**, stop **650**, risk 25 points (3.70%).

**Targets:** TP1 **720** (1.80R), TP2 **895** (8.80R), TP3 **910** (9.40R). Recommended base-case RR: **8.80R**.

**Why entry:** Hybrid entry uses close 655 and ATR14 86.1: buy zone 620–675. Entry is valid only if price can trade/hold around 675 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 650 is placed below support structure (655 / 655). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 720 (1.80R), TP2 895 (8.80R), TP3 910 (9.40R). Targets are ATR/structure capped for hold_days=3. ATR14=86.1, resistance_5/10/20/60=895/995/1,060/1,100. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## VKTR — swing_continual_defensive — CONDITIONAL

**Score:** 0.578 vs policy min 0.30 · **Close:** 655 · **ATR14:** 86.1 · **Volume ratio 20D:** 1.40 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 620–675, entry trigger **675**, stop **650**, risk 25 points (3.70%).

**Targets:** TP1 **720** (1.80R), TP2 **735** (2.40R), TP3 **895** (8.80R). Recommended base-case RR: **2.40R**.

**Why entry:** Hybrid entry uses close 655 and ATR14 86.1: buy zone 620–675. Entry is valid only if price can trade/hold around 675 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 650 is placed below support structure (655 / 655). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 720 (1.80R), TP2 735 (2.40R), TP3 895 (8.80R). Targets are ATR/structure capped for hold_days=1. ATR14=86.1, resistance_5/10/20/60=895/995/1,060/1,100. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## BNBR — position_continual — CONDITIONAL

**Score:** 0.334 vs policy min 0.30 · **Close:** 126 · **ATR14:** 19.9 · **Volume ratio 20D:** 0.85 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 119–130, entry trigger **130**, stop **125**, risk 5 points (3.85%).

**Targets:** TP1 **186** (11.20R), TP2 **189** (11.80R), TP3 **192** (12.40R). Recommended base-case RR: **11.80R**.

**Why entry:** Hybrid entry uses close 126 and ATR14 19.9: buy zone 119–130. Entry is valid only if price can trade/hold around 130 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 125 is placed below support structure (126 / 126). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 186 (11.20R), TP2 189 (11.80R), TP3 192 (12.40R). Targets are ATR/structure capped for hold_days=10. ATR14=19.9, resistance_5/10/20/60=186/224/240/240. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## DEWA — position_continual — CONDITIONAL

**Score:** 0.332 vs policy min 0.30 · **Close:** 334 · **ATR14:** 38.8 · **Volume ratio 20D:** 1.88 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 320–342, entry trigger **342**, stop **322**, risk 20 points (5.85%).

**Targets:** TP1 **362** (1.00R), TP2 **505** (8.15R), TP3 **515** (8.65R). Recommended base-case RR: **8.15R**.

**Why entry:** Hybrid entry uses close 334 and ATR14 38.8: buy zone 320–342. Entry is valid only if price can trade/hold around 342 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 322 is placed below support structure (324 / 324). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 362 (1.00R), TP2 505 (8.15R), TP3 515 (8.65R). Targets are ATR/structure capped for hold_days=10. ATR14=38.8, resistance_5/10/20/60=505/535/595/655. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BUVA — position_continual — CONDITIONAL

**Score:** 0.326 vs policy min 0.30 · **Close:** 695 · **ATR14:** 113.9 · **Volume ratio 20D:** 1.28 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 655–720, entry trigger **720**, stop **690**, risk 30 points (4.17%).

**Targets:** TP1 **1,085** (12.17R), TP2 **1,130** (13.67R), TP3 **1,145** (14.17R). Recommended base-case RR: **13.67R**.

**Why entry:** Hybrid entry uses close 695 and ATR14 113.9: buy zone 655–720. Entry is valid only if price can trade/hold around 720 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 690 is placed below support structure (695 / 695). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,085 (12.17R), TP2 1,130 (13.67R), TP3 1,145 (14.17R). Targets are ATR/structure capped for hold_days=10. ATR14=113.9, resistance_5/10/20/60=1,130/1,175/1,390/1,695. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## BIPI — position_continual — CONDITIONAL

**Score:** 0.326 vs policy min 0.30 · **Close:** 172 · **ATR14:** 26.0 · **Volume ratio 20D:** 1.57 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 162–178, entry trigger **178**, stop **171**, risk 7 points (3.93%).

**Targets:** TP1 **234** (8.00R), TP2 **238** (8.57R), TP3 **242** (9.14R). Recommended base-case RR: **8.57R**.

**Why entry:** Hybrid entry uses close 172 and ATR14 26.0: buy zone 162–178. Entry is valid only if price can trade/hold around 178 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 171 is placed below support structure (172 / 172). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 234 (8.00R), TP2 238 (8.57R), TP3 242 (9.14R). Targets are ATR/structure capped for hold_days=10. ATR14=26.0, resistance_5/10/20/60=234/262/304/342. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## IRSX — position_continual — CONDITIONAL

**Score:** 0.324 vs policy min 0.30 · **Close:** 374 · **ATR14:** 45.6 · **Volume ratio 20D:** 1.62 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 358–384, entry trigger **384**, stop **372**, risk 12 points (3.12%).

**Targets:** TP1 **480** (8.00R), TP2 **486** (8.50R), TP3 **492** (9.00R). Recommended base-case RR: **8.50R**.

**Why entry:** Hybrid entry uses close 374 and ATR14 45.6: buy zone 358–384. Entry is valid only if price can trade/hold around 384 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 372 is placed below support structure (374 / 374). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 480 (8.00R), TP2 486 (8.50R), TP3 492 (9.00R). Targets are ATR/structure capped for hold_days=10. ATR14=45.6, resistance_5/10/20/60=480/480/525/685. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## BUVA — momentum_20d_continual_research — NO_TRADE

**Score:** 0.526 vs policy min 0.30 · **Close:** 695 · **ATR14:** 113.9 · **Volume ratio 20D:** 1.28 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 655–720, entry trigger **720**, stop **690**, risk 30 points (4.17%).

**Targets:** TP1 **1,085** (12.17R), TP2 **1,130** (13.67R), TP3 **1,145** (14.17R). Recommended base-case RR: **13.67R**.

**Why entry:** Hybrid entry uses close 695 and ATR14 113.9: buy zone 655–720. Entry is valid only if price can trade/hold around 720 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 690 is placed below support structure (695 / 695). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,085 (12.17R), TP2 1,130 (13.67R), TP3 1,145 (14.17R). Targets are ATR/structure capped for hold_days=10. ATR14=113.9, resistance_5/10/20/60=1,130/1,175/1,390/1,695. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** strategy policy has execution_enabled=false; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## CDIA — momentum_20d_continual_research — NO_TRADE

**Score:** 0.487 vs policy min 0.30 · **Close:** 705 · **ATR14:** 105.7 · **Volume ratio 20D:** 0.79 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 665–730, entry trigger **730**, stop **690**, risk 40 points (5.48%).

**Targets:** TP1 **1,035** (7.62R), TP2 **1,055** (8.12R), TP3 **1,075** (8.62R). Recommended base-case RR: **8.12R**.

**Why entry:** Hybrid entry uses close 705 and ATR14 105.7: buy zone 665–730. Entry is valid only if price can trade/hold around 730 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 690 is placed below support structure (695 / 695). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,035 (7.62R), TP2 1,055 (8.12R), TP3 1,075 (8.62R). Targets are ATR/structure capped for hold_days=10. ATR14=105.7, resistance_5/10/20/60=1,035/1,230/1,340/1,340. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** strategy policy has execution_enabled=false

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BNBR — momentum_20d_continual_research — NO_TRADE

**Score:** 0.456 vs policy min 0.30 · **Close:** 126 · **ATR14:** 19.9 · **Volume ratio 20D:** 0.85 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 119–130, entry trigger **130**, stop **125**, risk 5 points (3.85%).

**Targets:** TP1 **186** (11.20R), TP2 **189** (11.80R), TP3 **192** (12.40R). Recommended base-case RR: **11.80R**.

**Why entry:** Hybrid entry uses close 126 and ATR14 19.9: buy zone 119–130. Entry is valid only if price can trade/hold around 130 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 125 is placed below support structure (126 / 126). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 186 (11.20R), TP2 189 (11.80R), TP3 192 (12.40R). Targets are ATR/structure capped for hold_days=10. ATR14=19.9, resistance_5/10/20/60=186/224/240/240. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** strategy policy has execution_enabled=false; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## VKTR — momentum_20d_continual_research — NO_TRADE

**Score:** 0.455 vs policy min 0.30 · **Close:** 655 · **ATR14:** 86.1 · **Volume ratio 20D:** 1.40 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 620–675, entry trigger **675**, stop **650**, risk 25 points (3.70%).

**Targets:** TP1 **895** (8.80R), TP2 **910** (9.40R), TP3 **925** (10.00R). Recommended base-case RR: **9.40R**.

**Why entry:** Hybrid entry uses close 655 and ATR14 86.1: buy zone 620–675. Entry is valid only if price can trade/hold around 675 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 650 is placed below support structure (655 / 655). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 895 (8.80R), TP2 910 (9.40R), TP3 925 (10.00R). Targets are ATR/structure capped for hold_days=10. ATR14=86.1, resistance_5/10/20/60=895/995/1,060/1,100. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** strategy policy has execution_enabled=false; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## CUAN — momentum_20d_continual_research — NO_TRADE

**Score:** 0.454 vs policy min 0.30 · **Close:** 535 · **ATR14:** 123.2 · **Volume ratio 20D:** 0.82 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 490–560, entry trigger **560**, stop **515**, risk 45 points (8.04%).

**Targets:** TP1 **885** (7.22R), TP2 **910** (7.78R), TP3 **935** (8.33R). Recommended base-case RR: **7.78R**.

**Why entry:** Hybrid entry uses close 535 and ATR14 123.2: buy zone 490–560. Entry is valid only if price can trade/hold around 560 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 515 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 885 (7.22R), TP2 910 (7.78R), TP3 935 (8.33R). Targets are ATR/structure capped for hold_days=10. ATR14=123.2, resistance_5/10/20/60=885/1,320/1,620/1,990. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** strategy policy has execution_enabled=false; entry-to-stop risk 8.04% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## CUAN — position_continual — NO_TRADE

**Score:** 0.332 vs policy min 0.30 · **Close:** 535 · **ATR14:** 123.2 · **Volume ratio 20D:** 0.82 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 490–560, entry trigger **560**, stop **515**, risk 45 points (8.04%).

**Targets:** TP1 **885** (7.22R), TP2 **910** (7.78R), TP3 **935** (8.33R). Recommended base-case RR: **7.78R**.

**Why entry:** Hybrid entry uses close 535 and ATR14 123.2: buy zone 490–560. Entry is valid only if price can trade/hold around 560 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 515 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 885 (7.22R), TP2 910 (7.78R), TP3 935 (8.33R). Targets are ATR/structure capped for hold_days=10. ATR14=123.2, resistance_5/10/20/60=885/1,320/1,620/1,990. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.04% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## DSSA — position_continual — NO_TRADE

**Score:** 0.330 vs policy min 0.30 · **Close:** 610 · **ATR14:** 203.6 · **Volume ratio 20D:** 4.13 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 535–655, entry trigger **655**, stop **600**, risk 55 points (8.40%).

**Targets:** TP1 **1,115** (8.36R), TP2 **1,145** (8.91R), TP3 **1,175** (9.45R). Recommended base-case RR: **8.91R**.

**Why entry:** Hybrid entry uses close 610 and ATR14 203.6: buy zone 535–655. Entry is valid only if price can trade/hold around 655 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 600 is placed below support structure (605 / 605). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,115 (8.36R), TP2 1,145 (8.91R), TP3 1,175 (9.45R). Targets are ATR/structure capped for hold_days=10. ATR14=203.6, resistance_5/10/20/60=1,115/1,790/3,500/98,000. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.40% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---
