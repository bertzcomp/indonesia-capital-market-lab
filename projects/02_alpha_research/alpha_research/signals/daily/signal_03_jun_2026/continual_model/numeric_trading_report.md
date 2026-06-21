# Numeric Trading Desk Report — 2026-06-02

This report is generated from live model scores, selected signal policy, canonical OHLCV, ATR, support/resistance, liquidity, and broker-flow diagnostics. It is not a simple BUY/SELL list; each plan is conditional on execution behaviour.

## Summary

| Plan quality | Count |
|---|---:|
| ACTIONABLE | 1 |
| CONDITIONAL | 14 |
| WATCHLIST_ONLY | 3 |
| NO_TRADE | 24 |

## DGWG — scalping_continual_defensive — ACTIONABLE

**Score:** 0.625 vs policy min 0.05 · **Close:** 306 · **ATR14:** 16.6 · **Volume ratio 20D:** 1.07 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 300–310, entry trigger **310**, stop **304**, risk 6 points (1.94%).

**Targets:** TP1 **320** (1.67R), TP2 **340** (5.00R), TP3 **344** (5.67R). Recommended base-case RR: **5.00R**.

**Why entry:** Hybrid entry uses close 306 and ATR14 16.6: buy zone 300–310. Entry is valid only if price can trade/hold around 310 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 304 is placed below support structure (306 / 306). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 320 (1.67R), TP2 340 (5.00R), TP3 344 (5.67R). Targets are ATR/structure capped for hold_days=1. ATR14=16.6, resistance_5/10/20/60=344/374/402/510. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## GTSI — ara_candidate_continual — CONDITIONAL

**Score:** 0.850 vs policy min 0.50 · **Close:** 140 · **ATR14:** 19.6 · **Volume ratio 20D:** 2.48 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 133–144, entry trigger **144**, stop **138**, risk 6 points (4.17%).

**Targets:** TP1 **154** (1.67R), TP2 **180** (6.00R), TP3 **183** (6.50R). Recommended base-case RR: **6.00R**.

**Why entry:** Hybrid entry uses close 140 and ATR14 19.6: buy zone 133–144. Entry is valid only if price can trade/hold around 144 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 138 is placed below support structure (139 / 139). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 154 (1.67R), TP2 180 (6.00R), TP3 183 (6.50R). Targets are ATR/structure capped for hold_days=1. ATR14=19.6, resistance_5/10/20/60=180/222/240/348. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## GTSI — scalping_continual_defensive — CONDITIONAL

**Score:** 0.632 vs policy min 0.05 · **Close:** 140 · **ATR14:** 19.6 · **Volume ratio 20D:** 2.48 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 133–144, entry trigger **144**, stop **138**, risk 6 points (4.17%).

**Targets:** TP1 **154** (1.67R), TP2 **180** (6.00R), TP3 **183** (6.50R). Recommended base-case RR: **6.00R**.

**Why entry:** Hybrid entry uses close 140 and ATR14 19.6: buy zone 133–144. Entry is valid only if price can trade/hold around 144 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 138 is placed below support structure (139 / 139). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 154 (1.67R), TP2 180 (6.00R), TP3 183 (6.50R). Targets are ATR/structure capped for hold_days=1. ATR14=19.6, resistance_5/10/20/60=180/222/240/348. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## OMED — scalping_continual_defensive — CONDITIONAL

**Score:** 0.630 vs policy min 0.05 · **Close:** 206 · **ATR14:** 22.0 · **Volume ratio 20D:** 1.12 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 198–212, entry trigger **212**, stop **200**, risk 12 points (5.66%).

**Targets:** TP1 **224** (1.00R), TP2 **250** (3.17R), TP3 **256** (3.67R). Recommended base-case RR: **3.17R**.

**Why entry:** Hybrid entry uses close 206 and ATR14 22.0: buy zone 198–212. Entry is valid only if price can trade/hold around 212 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 200 is placed below support structure (202 / 202). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 224 (1.00R), TP2 250 (3.17R), TP3 256 (3.67R). Targets are ATR/structure capped for hold_days=1. ATR14=22.0, resistance_5/10/20/60=250/252/310/318. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## TPMA — scalping_continual_defensive — CONDITIONAL

**Score:** 0.607 vs policy min 0.05 · **Close:** 438 · **ATR14:** 20.3 · **Volume ratio 20D:** 1.32 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 430–444, entry trigger **444**, stop **434**, risk 10 points (2.25%).

**Targets:** TP1 **456** (1.20R), TP2 **462** (1.80R), TP3 **496** (5.20R). Recommended base-case RR: **1.80R**.

**Why entry:** Hybrid entry uses close 438 and ATR14 20.3: buy zone 430–444. Entry is valid only if price can trade/hold around 444 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 434 is placed below support structure (436 / 436). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 456 (1.20R), TP2 462 (1.80R), TP3 496 (5.20R). Targets are ATR/structure capped for hold_days=1. ATR14=20.3, resistance_5/10/20/60=510/550/585/630. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.20R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## DEWA — momentum_10d_continual_aggressive — CONDITIONAL

**Score:** 0.475 vs policy min 0.30 · **Close:** 334 · **ATR14:** 42.9 · **Volume ratio 20D:** 0.67 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 318–344, entry trigger **344**, stop **318**, risk 26 points (7.56%).

**Targets:** TP1 **398** (2.08R), TP2 **412** (2.62R), TP3 **426** (3.15R). Recommended base-case RR: **2.62R**.

**Why entry:** Hybrid entry uses close 334 and ATR14 42.9: buy zone 318–344. Entry is valid only if price can trade/hold around 344 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 318 is placed below support structure (320 / 320). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 398 (2.08R), TP2 412 (2.62R), TP3 426 (3.15R). Targets are ATR/structure capped for hold_days=5. ATR14=42.9, resistance_5/10/20/60=398/505/535/640. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## HATM — momentum_10d_continual_aggressive — CONDITIONAL

**Score:** 0.445 vs policy min 0.30 · **Close:** 382 · **ATR14:** 21.0 · **Volume ratio 20D:** 3.09 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 374–388, entry trigger **388**, stop **362**, risk 26 points (6.70%).

**Targets:** TP1 **414** (1.00R), TP2 **434** (1.77R), TP3 **452** (2.46R). Recommended base-case RR: **1.77R**.

**Why entry:** Hybrid entry uses close 382 and ATR14 21.0: buy zone 374–388. Entry is valid only if price can trade/hold around 388 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 362 uses 1.20×ATR14 volatility cap. Thesis invalidates if the move reverses beyond normal volatility. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 414 (1.00R), TP2 434 (1.77R), TP3 452 (2.46R). Targets are ATR/structure capped for hold_days=5. ATR14=21.0, resistance_5/10/20/60=386/386/386/386. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## GTSI — momentum_5d_continual_defensive — CONDITIONAL

**Score:** 0.423 vs policy min 0.30 · **Close:** 140 · **ATR14:** 19.6 · **Volume ratio 20D:** 2.48 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 133–144, entry trigger **144**, stop **138**, risk 6 points (4.17%).

**Targets:** TP1 **179** (5.83R), TP2 **180** (6.00R), TP3 **183** (6.50R). Recommended base-case RR: **6.00R**.

**Why entry:** Hybrid entry uses close 140 and ATR14 19.6: buy zone 133–144. Entry is valid only if price can trade/hold around 144 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 138 is placed below support structure (139 / 139). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 179 (5.83R), TP2 180 (6.00R), TP3 183 (6.50R). Targets are ATR/structure capped for hold_days=3. ATR14=19.6, resistance_5/10/20/60=180/222/240/348. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## GTSI — swing_continual_defensive — CONDITIONAL

**Score:** 0.423 vs policy min 0.30 · **Close:** 140 · **ATR14:** 19.6 · **Volume ratio 20D:** 2.48 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 133–144, entry trigger **144**, stop **138**, risk 6 points (4.17%).

**Targets:** TP1 **154** (1.67R), TP2 **180** (6.00R), TP3 **183** (6.50R). Recommended base-case RR: **6.00R**.

**Why entry:** Hybrid entry uses close 140 and ATR14 19.6: buy zone 133–144. Entry is valid only if price can trade/hold around 144 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 138 is placed below support structure (139 / 139). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 154 (1.67R), TP2 180 (6.00R), TP3 183 (6.50R). Targets are ATR/structure capped for hold_days=1. ATR14=19.6, resistance_5/10/20/60=180/222/240/348. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## GULA — momentum_10d_continual_aggressive — CONDITIONAL

**Score:** 0.421 vs policy min 0.30 · **Close:** 545 · **ATR14:** 29.3 · **Volume ratio 20D:** 1.07 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 530–555, entry trigger **555**, stop **515**, risk 40 points (7.21%).

**Targets:** TP1 **595** (1.00R), TP2 **625** (1.75R), TP3 **655** (2.50R). Recommended base-case RR: **1.75R**.

**Why entry:** Hybrid entry uses close 545 and ATR14 29.3: buy zone 530–555. Entry is valid only if price can trade/hold around 555 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 515 uses 1.20×ATR14 volatility cap. Thesis invalidates if the move reverses beyond normal volatility. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 595 (1.00R), TP2 625 (1.75R), TP3 655 (2.50R). Targets are ATR/structure capped for hold_days=5. ATR14=29.3, resistance_5/10/20/60=550/550/550/550. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BUMI — momentum_5d_continual_defensive — CONDITIONAL

**Score:** 0.389 vs policy min 0.30 · **Close:** 161 · **ATR14:** 15.8 · **Volume ratio 20D:** 0.71 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 155–165, entry trigger **165**, stop **156**, risk 9 points (5.45%).

**Targets:** TP1 **186** (2.33R), TP2 **191** (2.89R), TP3 **196** (3.44R). Recommended base-case RR: **2.89R**.

**Why entry:** Hybrid entry uses close 161 and ATR14 15.8: buy zone 155–165. Entry is valid only if price can trade/hold around 165 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 156 is placed below support structure (157 / 157). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 186 (2.33R), TP2 191 (2.89R), TP3 196 (3.44R). Targets are ATR/structure capped for hold_days=3. ATR14=15.8, resistance_5/10/20/60=186/220/250/306. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## BUMI — swing_continual_defensive — CONDITIONAL

**Score:** 0.389 vs policy min 0.30 · **Close:** 161 · **ATR14:** 15.8 · **Volume ratio 20D:** 0.71 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 155–165, entry trigger **165**, stop **156**, risk 9 points (5.45%).

**Targets:** TP1 **181** (1.78R), TP2 **186** (2.33R), TP3 **187** (2.44R). Recommended base-case RR: **2.33R**.

**Why entry:** Hybrid entry uses close 161 and ATR14 15.8: buy zone 155–165. Entry is valid only if price can trade/hold around 165 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 156 is placed below support structure (157 / 157). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 181 (1.78R), TP2 186 (2.33R), TP3 187 (2.44R). Targets are ATR/structure capped for hold_days=1. ATR14=15.8, resistance_5/10/20/60=186/220/250/306. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## FORE — momentum_5d_continual_defensive — CONDITIONAL

**Score:** 0.386 vs policy min 0.30 · **Close:** 730 · **ATR14:** 85.7 · **Volume ratio 20D:** 0.33 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 700–750, entry trigger **750**, stop **690**, risk 60 points (8.00%).

**Targets:** TP1 **810** (1.00R), TP2 **945** (3.25R), TP3 **975** (3.75R). Recommended base-case RR: **3.25R**.

**Why entry:** Hybrid entry uses close 730 and ATR14 85.7: buy zone 700–750. Entry is valid only if price can trade/hold around 750 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 690 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 810 (1.00R), TP2 945 (3.25R), TP3 975 (3.75R). Targets are ATR/structure capped for hold_days=3. ATR14=85.7, resistance_5/10/20/60=945/1,035/1,135/1,135. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.25R; volume ratio 0.33 below required 0.60; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## FORE — swing_continual_defensive — CONDITIONAL

**Score:** 0.386 vs policy min 0.30 · **Close:** 730 · **ATR14:** 85.7 · **Volume ratio 20D:** 0.33 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 700–750, entry trigger **750**, stop **690**, risk 60 points (8.00%).

**Targets:** TP1 **810** (1.00R), TP2 **905** (2.58R), TP3 **945** (3.25R). Recommended base-case RR: **2.58R**.

**Why entry:** Hybrid entry uses close 730 and ATR14 85.7: buy zone 700–750. Entry is valid only if price can trade/hold around 750 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 690 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 810 (1.00R), TP2 905 (2.58R), TP3 945 (3.25R). Targets are ATR/structure capped for hold_days=1. ATR14=85.7, resistance_5/10/20/60=945/1,035/1,135/1,135. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.25R; volume ratio 0.33 below required 0.60; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## DEWA — position_continual — CONDITIONAL

**Score:** 0.334 vs policy min 0.30 · **Close:** 334 · **ATR14:** 42.9 · **Volume ratio 20D:** 0.67 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 318–344, entry trigger **344**, stop **318**, risk 26 points (7.56%).

**Targets:** TP1 **398** (2.08R), TP2 **412** (2.62R), TP3 **426** (3.15R). Recommended base-case RR: **2.62R**.

**Why entry:** Hybrid entry uses close 334 and ATR14 42.9: buy zone 318–344. Entry is valid only if price can trade/hold around 344 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 318 is placed below support structure (320 / 320). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 398 (2.08R), TP2 412 (2.62R), TP3 426 (3.15R). Targets are ATR/structure capped for hold_days=10. ATR14=42.9, resistance_5/10/20/60=398/505/535/640. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## KIJA — position_continual — WATCHLIST_ONLY

**Score:** 0.299 vs policy min 0.30 · **Close:** 122 · **ATR14:** 9.3 · **Volume ratio 20D:** 0.41 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 118–124, entry trigger **124**, stop **117**, risk 7 points (5.65%).

**Targets:** TP1 **133** (1.29R), TP2 **136** (1.71R), TP3 **141** (2.43R). Recommended base-case RR: **1.71R**.

**Why entry:** Hybrid entry uses close 122 and ATR14 9.3: buy zone 118–124. Entry is valid only if price can trade/hold around 124 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 117 is placed below support structure (118 / 118). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 133 (1.29R), TP2 136 (1.71R), TP3 141 (2.43R). Targets are ATR/structure capped for hold_days=10. ATR14=9.3, resistance_5/10/20/60=133/174/190/230. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** score 0.299 below policy min_score 0.30; volume ratio 0.41 below required 0.60

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Generic strategy rule.

---

## GTSI — position_continual — WATCHLIST_ONLY

**Score:** 0.298 vs policy min 0.30 · **Close:** 140 · **ATR14:** 19.6 · **Volume ratio 20D:** 2.48 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 133–144, entry trigger **144**, stop **138**, risk 6 points (4.17%).

**Targets:** TP1 **180** (6.00R), TP2 **183** (6.50R), TP3 **186** (7.00R). Recommended base-case RR: **6.50R**.

**Why entry:** Hybrid entry uses close 140 and ATR14 19.6: buy zone 133–144. Entry is valid only if price can trade/hold around 144 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 138 is placed below support structure (139 / 139). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 180 (6.00R), TP2 183 (6.50R), TP3 186 (7.00R). Targets are ATR/structure capped for hold_days=10. ATR14=19.6, resistance_5/10/20/60=180/222/240/348. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** score 0.298 below policy min_score 0.30; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Generic strategy rule.

---

## ESSA — position_continual — WATCHLIST_ONLY

**Score:** 0.286 vs policy min 0.30 · **Close:** 665 · **ATR14:** 59.3 · **Volume ratio 20D:** 0.55 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 640–680, entry trigger **680**, stop **640**, risk 40 points (5.88%).

**Targets:** TP1 **720** (1.00R), TP2 **750** (1.75R), TP3 **780** (2.50R). Recommended base-case RR: **1.75R**.

**Why entry:** Hybrid entry uses close 665 and ATR14 59.3: buy zone 640–680. Entry is valid only if price can trade/hold around 680 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 640 is placed below support structure (645 / 645). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 720 (1.00R), TP2 750 (1.75R), TP3 780 (2.50R). Targets are ATR/structure capped for hold_days=10. ATR14=59.3, resistance_5/10/20/60=720/825/995/995. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** score 0.286 below policy min_score 0.30; TP1 reward/risk 1.00R is below strategy minimum 1.25R; volume ratio 0.55 below required 0.60

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Generic strategy rule.

---

## MSIN — scalping_continual_defensive — NO_TRADE

**Score:** 0.675 vs policy min 0.05 · **Close:** 370 · **ATR14:** 79.5 · **Volume ratio 20D:** 1.91 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 342–386, entry trigger **386**, stop **354**, risk 32 points (8.29%).

**Targets:** TP1 **426** (1.25R), TP2 **530** (4.50R), TP3 **555** (5.28R). Recommended base-case RR: **4.50R**.

**Why entry:** Hybrid entry uses close 370 and ATR14 79.5: buy zone 342–386. Entry is valid only if price can trade/hold around 386 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 354 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 426 (1.25R), TP2 530 (4.50R), TP3 555 (5.28R). Targets are ATR/structure capped for hold_days=1. ATR14=79.5, resistance_5/10/20/60=555/680/900/1,450. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.29% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## MSIN — momentum_5d_continual_defensive — NO_TRADE

**Score:** 0.572 vs policy min 0.30 · **Close:** 370 · **ATR14:** 79.5 · **Volume ratio 20D:** 1.91 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 342–386, entry trigger **386**, stop **354**, risk 32 points (8.29%).

**Targets:** TP1 **426** (1.25R), TP2 **555** (5.28R), TP3 **575** (5.91R). Recommended base-case RR: **5.28R**.

**Why entry:** Hybrid entry uses close 370 and ATR14 79.5: buy zone 342–386. Entry is valid only if price can trade/hold around 386 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 354 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 426 (1.25R), TP2 555 (5.28R), TP3 575 (5.91R). Targets are ATR/structure capped for hold_days=3. ATR14=79.5, resistance_5/10/20/60=555/680/900/1,450. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.29% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## MSIN — swing_continual_defensive — NO_TRADE

**Score:** 0.572 vs policy min 0.30 · **Close:** 370 · **ATR14:** 79.5 · **Volume ratio 20D:** 1.91 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 342–386, entry trigger **386**, stop **354**, risk 32 points (8.29%).

**Targets:** TP1 **426** (1.25R), TP2 **530** (4.50R), TP3 **555** (5.28R). Recommended base-case RR: **4.50R**.

**Why entry:** Hybrid entry uses close 370 and ATR14 79.5: buy zone 342–386. Entry is valid only if price can trade/hold around 386 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 354 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 426 (1.25R), TP2 530 (4.50R), TP3 555 (5.28R). Targets are ATR/structure capped for hold_days=1. ATR14=79.5, resistance_5/10/20/60=555/680/900/1,450. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.29% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## ASPR — momentum_5d_continual_defensive — NO_TRADE

**Score:** 0.480 vs policy min 0.30 · **Close:** 216 · **ATR14:** 76.6 · **Volume ratio 20D:** 3.13 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 189–232, entry trigger **232**, stop **212**, risk 20 points (8.62%).

**Targets:** TP1 **366** (6.70R), TP2 **378** (7.30R), TP3 **388** (7.80R). Recommended base-case RR: **7.30R**.

**Why entry:** Hybrid entry uses close 216 and ATR14 76.6: buy zone 189–232. Entry is valid only if price can trade/hold around 232 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 212 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 366 (6.70R), TP2 378 (7.30R), TP3 388 (7.80R). Targets are ATR/structure capped for hold_days=3. ATR14=76.6, resistance_5/10/20/60=378/540/620/620. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.62% exceeds max strategy risk 8.00%; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## ASPR — swing_continual_defensive — NO_TRADE

**Score:** 0.480 vs policy min 0.30 · **Close:** 216 · **ATR14:** 76.6 · **Volume ratio 20D:** 3.13 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 189–232, entry trigger **232**, stop **212**, risk 20 points (8.62%).

**Targets:** TP1 **272** (2.00R), TP2 **370** (6.90R), TP3 **378** (7.30R). Recommended base-case RR: **6.90R**.

**Why entry:** Hybrid entry uses close 216 and ATR14 76.6: buy zone 189–232. Entry is valid only if price can trade/hold around 232 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 212 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 272 (2.00R), TP2 370 (6.90R), TP3 378 (7.30R). Targets are ATR/structure capped for hold_days=1. ATR14=76.6, resistance_5/10/20/60=378/540/620/620. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.62% exceeds max strategy risk 8.00%; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## BRMS — momentum_10d_continual_aggressive — NO_TRADE

**Score:** 0.430 vs policy min 0.30 · **Close:** 580 · **ATR14:** 69.6 · **Volume ratio 20D:** 1.08 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 555–595, entry trigger **595**, stop **545**, risk 50 points (8.40%).

**Targets:** TP1 **645** (1.00R), TP2 **680** (1.70R), TP3 **715** (2.40R). Recommended base-case RR: **1.70R**.

**Why entry:** Hybrid entry uses close 580 and ATR14 69.6: buy zone 555–595. Entry is valid only if price can trade/hold around 595 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 545 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 645 (1.00R), TP2 680 (1.70R), TP3 715 (2.40R). Targets are ATR/structure capped for hold_days=5. ATR14=69.6, resistance_5/10/20/60=640/785/845/1,095. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.40% exceeds max strategy risk 8.00%; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## WBSA — momentum_5d_continual_defensive — NO_TRADE

**Score:** 0.427 vs policy min 0.30 · **Close:** 640 · **ATR14:** 151.4 · **Volume ratio 20D:** 0.41 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 585–675, entry trigger **675**, stop **620**, risk 55 points (8.15%).

**Targets:** TP1 **885** (3.82R), TP2 **915** (4.36R), TP3 **945** (4.91R). Recommended base-case RR: **4.36R**.

**Why entry:** Hybrid entry uses close 640 and ATR14 151.4: buy zone 585–675. Entry is valid only if price can trade/hold around 675 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 620 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 885 (3.82R), TP2 915 (4.36R), TP3 945 (4.91R). Targets are ATR/structure capped for hold_days=3. ATR14=151.4, resistance_5/10/20/60=885/1,325/1,605/1,605. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.15% exceeds max strategy risk 8.00%; volume ratio 0.41 below required 0.60; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## WBSA — swing_continual_defensive — NO_TRADE

**Score:** 0.427 vs policy min 0.30 · **Close:** 640 · **ATR14:** 151.4 · **Volume ratio 20D:** 0.41 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 585–675, entry trigger **675**, stop **620**, risk 55 points (8.15%).

**Targets:** TP1 **755** (1.45R), TP2 **885** (3.82R), TP3 **915** (4.36R). Recommended base-case RR: **3.82R**.

**Why entry:** Hybrid entry uses close 640 and ATR14 151.4: buy zone 585–675. Entry is valid only if price can trade/hold around 675 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 620 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 755 (1.45R), TP2 885 (3.82R), TP3 915 (4.36R). Targets are ATR/structure capped for hold_days=1. ATR14=151.4, resistance_5/10/20/60=885/1,325/1,605/1,605. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.15% exceeds max strategy risk 8.00%; volume ratio 0.41 below required 0.60; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## MSIN — momentum_10d_continual_aggressive — NO_TRADE

**Score:** 0.420 vs policy min 0.30 · **Close:** 370 · **ATR14:** 79.5 · **Volume ratio 20D:** 1.91 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 342–386, entry trigger **386**, stop **354**, risk 32 points (8.29%).

**Targets:** TP1 **555** (5.28R), TP2 **575** (5.91R), TP3 **595** (6.53R). Recommended base-case RR: **5.91R**.

**Why entry:** Hybrid entry uses close 370 and ATR14 79.5: buy zone 342–386. Entry is valid only if price can trade/hold around 386 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 354 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 555 (5.28R), TP2 575 (5.91R), TP3 595 (6.53R). Targets are ATR/structure capped for hold_days=5. ATR14=79.5, resistance_5/10/20/60=555/680/900/1,450. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.29% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BULL — momentum_10d_continual_aggressive — NO_TRADE

**Score:** 0.417 vs policy min 0.30 · **Close:** 380 · **ATR14:** 42.2 · **Volume ratio 20D:** 0.70 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 364–390, entry trigger **390**, stop **358**, risk 32 points (8.21%).

**Targets:** TP1 **428** (1.19R), TP2 **446** (1.75R), TP3 **468** (2.44R). Recommended base-case RR: **1.75R**.

**Why entry:** Hybrid entry uses close 380 and ATR14 42.2: buy zone 364–390. Entry is valid only if price can trade/hold around 390 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 358 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 428 (1.19R), TP2 446 (1.75R), TP3 468 (2.44R). Targets are ATR/structure capped for hold_days=5. ATR14=42.2, resistance_5/10/20/60=428/480/545/610. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.21% exceeds max strategy risk 8.00%; TP1 reward/risk 1.19R is below strategy minimum 1.25R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## DSSA — momentum_10d_continual_aggressive — NO_TRADE

**Score:** 0.413 vs policy min 0.30 · **Close:** 615 · **ATR14:** 143.1 · **Volume ratio 20D:** 1.13 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 560–645, entry trigger **645**, stop **590**, risk 55 points (8.53%).

**Targets:** TP1 **720** (1.36R), TP2 **1,115** (8.55R), TP3 **1,145** (9.09R). Recommended base-case RR: **8.55R**.

**Why entry:** Hybrid entry uses close 615 and ATR14 143.1: buy zone 560–645. Entry is valid only if price can trade/hold around 645 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 590 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 720 (1.36R), TP2 1,115 (8.55R), TP3 1,145 (9.09R). Targets are ATR/structure capped for hold_days=5. ATR14=143.1, resistance_5/10/20/60=615/1,115/1,895/88,675. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.53% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## DSSA — momentum_5d_continual_defensive — NO_TRADE

**Score:** 0.386 vs policy min 0.30 · **Close:** 615 · **ATR14:** 143.1 · **Volume ratio 20D:** 1.13 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 560–645, entry trigger **645**, stop **590**, risk 55 points (8.53%).

**Targets:** TP1 **720** (1.36R), TP2 **1,095** (8.18R), TP3 **1,115** (8.55R). Recommended base-case RR: **8.18R**.

**Why entry:** Hybrid entry uses close 615 and ATR14 143.1: buy zone 560–645. Entry is valid only if price can trade/hold around 645 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 590 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 720 (1.36R), TP2 1,095 (8.18R), TP3 1,115 (8.55R). Targets are ATR/structure capped for hold_days=3. ATR14=143.1, resistance_5/10/20/60=615/1,115/1,895/88,675. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.53% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## DSSA — swing_continual_defensive — NO_TRADE

**Score:** 0.386 vs policy min 0.30 · **Close:** 615 · **ATR14:** 143.1 · **Volume ratio 20D:** 1.13 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 560–645, entry trigger **645**, stop **590**, risk 55 points (8.53%).

**Targets:** TP1 **720** (1.36R), TP2 **740** (1.73R), TP3 **780** (2.45R). Recommended base-case RR: **1.73R**.

**Why entry:** Hybrid entry uses close 615 and ATR14 143.1: buy zone 560–645. Entry is valid only if price can trade/hold around 645 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 590 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 720 (1.36R), TP2 740 (1.73R), TP3 780 (2.45R). Targets are ATR/structure capped for hold_days=1. ATR14=143.1, resistance_5/10/20/60=615/1,115/1,895/88,675. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.53% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## MSIN — position_continual — NO_TRADE

**Score:** 0.312 vs policy min 0.30 · **Close:** 370 · **ATR14:** 79.5 · **Volume ratio 20D:** 1.91 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 342–386, entry trigger **386**, stop **354**, risk 32 points (8.29%).

**Targets:** TP1 **555** (5.28R), TP2 **575** (5.91R), TP3 **595** (6.53R). Recommended base-case RR: **5.91R**.

**Why entry:** Hybrid entry uses close 370 and ATR14 79.5: buy zone 342–386. Entry is valid only if price can trade/hold around 386 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 354 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 555 (5.28R), TP2 575 (5.91R), TP3 595 (6.53R). Targets are ATR/structure capped for hold_days=10. ATR14=79.5, resistance_5/10/20/60=555/680/900/1,450. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.29% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## DEWA — momentum_20d_continual_research — NO_TRADE

**Score:** 0.309 vs policy min 0.30 · **Close:** 334 · **ATR14:** 42.9 · **Volume ratio 20D:** 0.67 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 318–344, entry trigger **344**, stop **318**, risk 26 points (7.56%).

**Targets:** TP1 **398** (2.08R), TP2 **412** (2.62R), TP3 **426** (3.15R). Recommended base-case RR: **2.62R**.

**Why entry:** Hybrid entry uses close 334 and ATR14 42.9: buy zone 318–344. Entry is valid only if price can trade/hold around 344 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 318 is placed below support structure (320 / 320). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 398 (2.08R), TP2 412 (2.62R), TP3 426 (3.15R). Targets are ATR/structure capped for hold_days=10. ATR14=42.9, resistance_5/10/20/60=398/505/535/640. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** strategy policy has execution_enabled=false; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## SSMS — position_continual — NO_TRADE

**Score:** 0.299 vs policy min 0.30 · **Close:** 815 · **ATR14:** 89.3 · **Volume ratio 20D:** 1.59 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 780–835, entry trigger **835**, stop **765**, risk 70 points (8.38%).

**Targets:** TP1 **910** (1.07R), TP2 **955** (1.71R), TP3 **1,005** (2.43R). Recommended base-case RR: **1.71R**.

**Why entry:** Hybrid entry uses close 815 and ATR14 89.3: buy zone 780–835. Entry is valid only if price can trade/hold around 835 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 765 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 910 (1.07R), TP2 955 (1.71R), TP3 1,005 (2.43R). Targets are ATR/structure capped for hold_days=10. ATR14=89.3, resistance_5/10/20/60=910/1,310/1,460/1,800. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.38% exceeds max strategy risk 8.00%; score 0.299 below policy min_score 0.30; TP1 reward/risk 1.07R is below strategy minimum 1.25R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Generic strategy rule.

---

## BULL — position_continual — NO_TRADE

**Score:** 0.292 vs policy min 0.30 · **Close:** 380 · **ATR14:** 42.2 · **Volume ratio 20D:** 0.70 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 364–390, entry trigger **390**, stop **358**, risk 32 points (8.21%).

**Targets:** TP1 **428** (1.19R), TP2 **446** (1.75R), TP3 **468** (2.44R). Recommended base-case RR: **1.75R**.

**Why entry:** Hybrid entry uses close 380 and ATR14 42.2: buy zone 364–390. Entry is valid only if price can trade/hold around 390 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 358 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 428 (1.19R), TP2 446 (1.75R), TP3 468 (2.44R). Targets are ATR/structure capped for hold_days=10. ATR14=42.2, resistance_5/10/20/60=428/480/545/610. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.21% exceeds max strategy risk 8.00%; score 0.292 below policy min_score 0.30; TP1 reward/risk 1.19R is below strategy minimum 1.25R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Generic strategy rule.

---

## DSSA — momentum_20d_continual_research — NO_TRADE

**Score:** 0.286 vs policy min 0.30 · **Close:** 615 · **ATR14:** 143.1 · **Volume ratio 20D:** 1.13 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 560–645, entry trigger **645**, stop **590**, risk 55 points (8.53%).

**Targets:** TP1 **1,100** (8.27R), TP2 **1,115** (8.55R), TP3 **1,145** (9.09R). Recommended base-case RR: **8.55R**.

**Why entry:** Hybrid entry uses close 615 and ATR14 143.1: buy zone 560–645. Entry is valid only if price can trade/hold around 645 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 590 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,100 (8.27R), TP2 1,115 (8.55R), TP3 1,145 (9.09R). Targets are ATR/structure capped for hold_days=10. ATR14=143.1, resistance_5/10/20/60=615/1,115/1,895/88,675. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** strategy policy has execution_enabled=false; entry-to-stop risk 8.53% exceeds max strategy risk 8.00%; score 0.286 below policy min_score 0.30

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Generic strategy rule.

---

## BRMS — position_continual — NO_TRADE

**Score:** 0.284 vs policy min 0.30 · **Close:** 580 · **ATR14:** 69.6 · **Volume ratio 20D:** 1.08 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 555–595, entry trigger **595**, stop **545**, risk 50 points (8.40%).

**Targets:** TP1 **645** (1.00R), TP2 **680** (1.70R), TP3 **715** (2.40R). Recommended base-case RR: **1.70R**.

**Why entry:** Hybrid entry uses close 580 and ATR14 69.6: buy zone 555–595. Entry is valid only if price can trade/hold around 595 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 545 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 645 (1.00R), TP2 680 (1.70R), TP3 715 (2.40R). Targets are ATR/structure capped for hold_days=10. ATR14=69.6, resistance_5/10/20/60=640/785/845/1,095. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.40% exceeds max strategy risk 8.00%; score 0.284 below policy min_score 0.30; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Generic strategy rule.

---

## WBSA — position_continual — NO_TRADE

**Score:** 0.282 vs policy min 0.30 · **Close:** 640 · **ATR14:** 151.4 · **Volume ratio 20D:** 0.41 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 585–675, entry trigger **675**, stop **620**, risk 55 points (8.15%).

**Targets:** TP1 **885** (3.82R), TP2 **915** (4.36R), TP3 **945** (4.91R). Recommended base-case RR: **4.36R**.

**Why entry:** Hybrid entry uses close 640 and ATR14 151.4: buy zone 585–675. Entry is valid only if price can trade/hold around 675 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 620 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 885 (3.82R), TP2 915 (4.36R), TP3 945 (4.91R). Targets are ATR/structure capped for hold_days=10. ATR14=151.4, resistance_5/10/20/60=885/1,325/1,605/1,605. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.15% exceeds max strategy risk 8.00%; score 0.282 below policy min_score 0.30; volume ratio 0.41 below required 0.60; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Generic strategy rule.

---

## BNBR — position_continual — NO_TRADE

**Score:** 0.280 vs policy min 0.30 · **Close:** 127 · **ATR14:** 21.1 · **Volume ratio 20D:** 0.83 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 119–132, entry trigger **132**, stop **121**, risk 11 points (8.33%).

**Targets:** TP1 **145** (1.18R), TP2 **151** (1.73R), TP3 **159** (2.45R). Recommended base-case RR: **1.73R**.

**Why entry:** Hybrid entry uses close 127 and ATR14 21.1: buy zone 119–132. Entry is valid only if price can trade/hold around 132 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 121 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 145 (1.18R), TP2 151 (1.73R), TP3 159 (2.45R). Targets are ATR/structure capped for hold_days=10. ATR14=21.1, resistance_5/10/20/60=145/186/224/240. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.33% exceeds max strategy risk 8.00%; score 0.280 below policy min_score 0.30; TP1 reward/risk 1.18R is below strategy minimum 1.25R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Generic strategy rule.

---

## MSIN — momentum_20d_continual_research — NO_TRADE

**Score:** 0.267 vs policy min 0.30 · **Close:** 370 · **ATR14:** 79.5 · **Volume ratio 20D:** 1.91 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 342–386, entry trigger **386**, stop **354**, risk 32 points (8.29%).

**Targets:** TP1 **555** (5.28R), TP2 **575** (5.91R), TP3 **595** (6.53R). Recommended base-case RR: **5.91R**.

**Why entry:** Hybrid entry uses close 370 and ATR14 79.5: buy zone 342–386. Entry is valid only if price can trade/hold around 386 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 354 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 555 (5.28R), TP2 575 (5.91R), TP3 595 (6.53R). Targets are ATR/structure capped for hold_days=10. ATR14=79.5, resistance_5/10/20/60=555/680/900/1,450. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** strategy policy has execution_enabled=false; entry-to-stop risk 8.29% exceeds max strategy risk 8.00%; score 0.267 below policy min_score 0.30

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Generic strategy rule.

---

## BRMS — momentum_20d_continual_research — NO_TRADE

**Score:** 0.258 vs policy min 0.30 · **Close:** 580 · **ATR14:** 69.6 · **Volume ratio 20D:** 1.08 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 555–595, entry trigger **595**, stop **545**, risk 50 points (8.40%).

**Targets:** TP1 **645** (1.00R), TP2 **680** (1.70R), TP3 **715** (2.40R). Recommended base-case RR: **1.70R**.

**Why entry:** Hybrid entry uses close 580 and ATR14 69.6: buy zone 555–595. Entry is valid only if price can trade/hold around 595 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 545 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 645 (1.00R), TP2 680 (1.70R), TP3 715 (2.40R). Targets are ATR/structure capped for hold_days=10. ATR14=69.6, resistance_5/10/20/60=640/785/845/1,095. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** strategy policy has execution_enabled=false; entry-to-stop risk 8.40% exceeds max strategy risk 8.00%; score 0.258 below policy min_score 0.30; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Generic strategy rule.

---

## BULL — momentum_20d_continual_research — NO_TRADE

**Score:** 0.251 vs policy min 0.30 · **Close:** 380 · **ATR14:** 42.2 · **Volume ratio 20D:** 0.70 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 364–390, entry trigger **390**, stop **358**, risk 32 points (8.21%).

**Targets:** TP1 **428** (1.19R), TP2 **446** (1.75R), TP3 **468** (2.44R). Recommended base-case RR: **1.75R**.

**Why entry:** Hybrid entry uses close 380 and ATR14 42.2: buy zone 364–390. Entry is valid only if price can trade/hold around 390 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 358 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 428 (1.19R), TP2 446 (1.75R), TP3 468 (2.44R). Targets are ATR/structure capped for hold_days=10. ATR14=42.2, resistance_5/10/20/60=428/480/545/610. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** strategy policy has execution_enabled=false; entry-to-stop risk 8.21% exceeds max strategy risk 8.00%; score 0.251 below policy min_score 0.30; TP1 reward/risk 1.19R is below strategy minimum 1.25R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Generic strategy rule.

---
