# Numeric Trading Desk Report — 2026-06-03

This report is generated from live model scores, selected signal policy, canonical OHLCV, ATR, support/resistance, liquidity, and broker-flow diagnostics. It is not a simple BUY/SELL list; each plan is conditional on execution behaviour.

## Summary

| Plan quality | Count |
|---|---:|
| ACTIONABLE | 12 |
| CONDITIONAL | 18 |
| NO_TRADE | 12 |

## BULL — scalping_continual_defensive — ACTIONABLE

**Score:** 0.746 vs policy min 0.05 · **Close:** 324 · **ATR14:** 44.3 · **Volume ratio 20D:** 1.60 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 308–334, entry trigger **334**, stop **322**, risk 12 points (3.59%).

**Targets:** TP1 **358** (2.00R), TP2 **414** (6.67R), TP3 **428** (7.83R). Recommended base-case RR: **6.67R**.

**Why entry:** Hybrid entry uses close 324 and ATR14 44.3: buy zone 308–334. Entry is valid only if price can trade/hold around 334 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 322 is placed below support structure (324 / 324). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 358 (2.00R), TP2 414 (6.67R), TP3 428 (7.83R). Targets are ATR/structure capped for hold_days=1. ATR14=44.3, resistance_5/10/20/60=428/458/545/610. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## DEWA — momentum_10d_continual_aggressive — ACTIONABLE

**Score:** 0.659 vs policy min 0.30 · **Close:** 294 · **ATR14:** 45.4 · **Volume ratio 20D:** 1.43 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 278–304, entry trigger **304**, stop **282**, risk 22 points (7.24%).

**Targets:** TP1 **384** (3.64R), TP2 **396** (4.18R), TP3 **408** (4.73R). Recommended base-case RR: **4.18R**.

**Why entry:** Hybrid entry uses close 294 and ATR14 45.4: buy zone 278–304. Entry is valid only if price can trade/hold around 304 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 282 is placed below support structure (284 / 284). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 384 (3.64R), TP2 396 (4.18R), TP3 408 (4.73R). Targets are ATR/structure capped for hold_days=5. ATR14=45.4, resistance_5/10/20/60=384/482/535/630. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BULL — momentum_10d_continual_aggressive — ACTIONABLE

**Score:** 0.658 vs policy min 0.30 · **Close:** 324 · **ATR14:** 44.3 · **Volume ratio 20D:** 1.60 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 308–334, entry trigger **334**, stop **322**, risk 12 points (3.59%).

**Targets:** TP1 **428** (7.83R), TP2 **434** (8.33R), TP3 **440** (8.83R). Recommended base-case RR: **8.33R**.

**Why entry:** Hybrid entry uses close 324 and ATR14 44.3: buy zone 308–334. Entry is valid only if price can trade/hold around 334 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 322 is placed below support structure (324 / 324). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 428 (7.83R), TP2 434 (8.33R), TP3 440 (8.83R). Targets are ATR/structure capped for hold_days=5. ATR14=44.3, resistance_5/10/20/60=428/458/545/610. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## INET — momentum_10d_continual_aggressive — ACTIONABLE

**Score:** 0.652 vs policy min 0.30 · **Close:** 199 · **ATR14:** 25.6 · **Volume ratio 20D:** 1.24 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 190–206, entry trigger **206**, stop **190**, risk 16 points (7.77%).

**Targets:** TP1 **244** (2.38R), TP2 **252** (2.88R), TP3 **260** (3.38R). Recommended base-case RR: **2.88R**.

**Why entry:** Hybrid entry uses close 199 and ATR14 25.6: buy zone 190–206. Entry is valid only if price can trade/hold around 206 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 190 is placed below support structure (192 / 192). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 244 (2.38R), TP2 252 (2.88R), TP3 260 (3.38R). Targets are ATR/structure capped for hold_days=5. ATR14=25.6, resistance_5/10/20/60=244/280/334/418. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BIPI — momentum_10d_continual_aggressive — ACTIONABLE

**Score:** 0.651 vs policy min 0.30 · **Close:** 152 · **ATR14:** 24.0 · **Volume ratio 20D:** 1.21 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 143–157, entry trigger **157**, stop **150**, risk 7 points (4.46%).

**Targets:** TP1 **190** (4.71R), TP2 **194** (5.29R), TP3 **198** (5.86R). Recommended base-case RR: **5.29R**.

**Why entry:** Hybrid entry uses close 152 and ATR14 24.0: buy zone 143–157. Entry is valid only if price can trade/hold around 157 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 150 is placed below support structure (151 / 151). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 190 (4.71R), TP2 194 (5.29R), TP3 198 (5.86R). Targets are ATR/structure capped for hold_days=5. ATR14=24.0, resistance_5/10/20/60=190/234/262/342. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## DEWA — momentum_5d_continual_defensive — ACTIONABLE

**Score:** 0.623 vs policy min 0.30 · **Close:** 294 · **ATR14:** 45.4 · **Volume ratio 20D:** 1.43 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 278–304, entry trigger **304**, stop **282**, risk 22 points (7.24%).

**Targets:** TP1 **384** (3.64R), TP2 **396** (4.18R), TP3 **408** (4.73R). Recommended base-case RR: **4.18R**.

**Why entry:** Hybrid entry uses close 294 and ATR14 45.4: buy zone 278–304. Entry is valid only if price can trade/hold around 304 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 282 is placed below support structure (284 / 284). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 384 (3.64R), TP2 396 (4.18R), TP3 408 (4.73R). Targets are ATR/structure capped for hold_days=3. ATR14=45.4, resistance_5/10/20/60=384/482/535/630. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BUMI — momentum_10d_continual_aggressive — ACTIONABLE

**Score:** 0.616 vs policy min 0.30 · **Close:** 148 · **ATR14:** 16.9 · **Volume ratio 20D:** 1.49 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 142–152, entry trigger **152**, stop **140**, risk 12 points (7.89%).

**Targets:** TP1 **184** (2.67R), TP2 **190** (3.17R), TP3 **196** (3.67R). Recommended base-case RR: **3.17R**.

**Why entry:** Hybrid entry uses close 148 and ATR14 16.9: buy zone 142–152. Entry is valid only if price can trade/hold around 152 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 140 is placed below support structure (141 / 141). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 184 (2.67R), TP2 190 (3.17R), TP3 196 (3.67R). Targets are ATR/structure capped for hold_days=5. ATR14=16.9, resistance_5/10/20/60=184/214/250/298. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## DEWA — position_continual — ACTIONABLE

**Score:** 0.327 vs policy min 0.30 · **Close:** 294 · **ATR14:** 45.4 · **Volume ratio 20D:** 1.43 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 278–304, entry trigger **304**, stop **282**, risk 22 points (7.24%).

**Targets:** TP1 **384** (3.64R), TP2 **396** (4.18R), TP3 **408** (4.73R). Recommended base-case RR: **4.18R**.

**Why entry:** Hybrid entry uses close 294 and ATR14 45.4: buy zone 278–304. Entry is valid only if price can trade/hold around 304 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 282 is placed below support structure (284 / 284). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 384 (3.64R), TP2 396 (4.18R), TP3 408 (4.73R). Targets are ATR/structure capped for hold_days=10. ATR14=45.4, resistance_5/10/20/60=384/482/535/630. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## INET — position_continual — ACTIONABLE

**Score:** 0.327 vs policy min 0.30 · **Close:** 199 · **ATR14:** 25.6 · **Volume ratio 20D:** 1.24 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 190–206, entry trigger **206**, stop **190**, risk 16 points (7.77%).

**Targets:** TP1 **244** (2.38R), TP2 **252** (2.88R), TP3 **260** (3.38R). Recommended base-case RR: **2.88R**.

**Why entry:** Hybrid entry uses close 199 and ATR14 25.6: buy zone 190–206. Entry is valid only if price can trade/hold around 206 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 190 is placed below support structure (192 / 192). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 244 (2.38R), TP2 252 (2.88R), TP3 260 (3.38R). Targets are ATR/structure capped for hold_days=10. ATR14=25.6, resistance_5/10/20/60=244/280/334/418. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BULL — position_continual — ACTIONABLE

**Score:** 0.322 vs policy min 0.30 · **Close:** 324 · **ATR14:** 44.3 · **Volume ratio 20D:** 1.60 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 308–334, entry trigger **334**, stop **322**, risk 12 points (3.59%).

**Targets:** TP1 **428** (7.83R), TP2 **434** (8.33R), TP3 **440** (8.83R). Recommended base-case RR: **8.33R**.

**Why entry:** Hybrid entry uses close 324 and ATR14 44.3: buy zone 308–334. Entry is valid only if price can trade/hold around 334 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 322 is placed below support structure (324 / 324). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 428 (7.83R), TP2 434 (8.33R), TP3 440 (8.83R). Targets are ATR/structure capped for hold_days=10. ATR14=44.3, resistance_5/10/20/60=428/458/545/610. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## GTSI — position_continual — ACTIONABLE

**Score:** 0.314 vs policy min 0.30 · **Close:** 123 · **ATR14:** 20.5 · **Volume ratio 20D:** 1.96 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 115–128, entry trigger **128**, stop **118**, risk 10 points (7.81%).

**Targets:** TP1 **180** (5.20R), TP2 **185** (5.70R), TP3 **190** (6.20R). Recommended base-case RR: **5.70R**.

**Why entry:** Hybrid entry uses close 123 and ATR14 20.5: buy zone 115–128. Entry is valid only if price can trade/hold around 128 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 118 is placed below support structure (119 / 119). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 180 (5.20R), TP2 185 (5.70R), TP3 190 (6.20R). Targets are ATR/structure capped for hold_days=10. ATR14=20.5, resistance_5/10/20/60=180/214/238/340. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BIPI — position_continual — ACTIONABLE

**Score:** 0.314 vs policy min 0.30 · **Close:** 152 · **ATR14:** 24.0 · **Volume ratio 20D:** 1.21 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 143–157, entry trigger **157**, stop **150**, risk 7 points (4.46%).

**Targets:** TP1 **190** (4.71R), TP2 **194** (5.29R), TP3 **198** (5.86R). Recommended base-case RR: **5.29R**.

**Why entry:** Hybrid entry uses close 152 and ATR14 24.0: buy zone 143–157. Entry is valid only if price can trade/hold around 157 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 150 is placed below support structure (151 / 151). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 190 (4.71R), TP2 194 (5.29R), TP3 198 (5.86R). Targets are ATR/structure capped for hold_days=10. ATR14=24.0, resistance_5/10/20/60=190/234/262/342. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## DEWA — ara_candidate_continual — CONDITIONAL

**Score:** 0.886 vs policy min 0.50 · **Close:** 294 · **ATR14:** 45.4 · **Volume ratio 20D:** 1.43 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 278–304, entry trigger **304**, stop **282**, risk 22 points (7.24%).

**Targets:** TP1 **328** (1.09R), TP2 **384** (3.64R), TP3 **396** (4.18R). Recommended base-case RR: **3.64R**.

**Why entry:** Hybrid entry uses close 294 and ATR14 45.4: buy zone 278–304. Entry is valid only if price can trade/hold around 304 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 282 is placed below support structure (284 / 284). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 328 (1.09R), TP2 384 (3.64R), TP3 396 (4.18R). Targets are ATR/structure capped for hold_days=1. ATR14=45.4, resistance_5/10/20/60=384/482/535/630. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.09R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## DEWA — scalping_continual_defensive — CONDITIONAL

**Score:** 0.748 vs policy min 0.05 · **Close:** 294 · **ATR14:** 45.4 · **Volume ratio 20D:** 1.43 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 278–304, entry trigger **304**, stop **282**, risk 22 points (7.24%).

**Targets:** TP1 **328** (1.09R), TP2 **384** (3.64R), TP3 **396** (4.18R). Recommended base-case RR: **3.64R**.

**Why entry:** Hybrid entry uses close 294 and ATR14 45.4: buy zone 278–304. Entry is valid only if price can trade/hold around 304 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 282 is placed below support structure (284 / 284). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 328 (1.09R), TP2 384 (3.64R), TP3 396 (4.18R). Targets are ATR/structure capped for hold_days=1. ATR14=45.4, resistance_5/10/20/60=384/482/535/630. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.09R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BUMI — scalping_continual_defensive — CONDITIONAL

**Score:** 0.728 vs policy min 0.05 · **Close:** 148 · **ATR14:** 16.9 · **Volume ratio 20D:** 1.49 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 142–152, entry trigger **152**, stop **140**, risk 12 points (7.89%).

**Targets:** TP1 **164** (1.00R), TP2 **183** (2.58R), TP3 **184** (2.67R). Recommended base-case RR: **2.58R**.

**Why entry:** Hybrid entry uses close 148 and ATR14 16.9: buy zone 142–152. Entry is valid only if price can trade/hold around 152 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 140 is placed below support structure (141 / 141). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 164 (1.00R), TP2 183 (2.58R), TP3 184 (2.67R). Targets are ATR/structure capped for hold_days=1. ATR14=16.9, resistance_5/10/20/60=184/214/250/298. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BNBR — scalping_continual_defensive — CONDITIONAL

**Score:** 0.725 vs policy min 0.05 · **Close:** 109 · **ATR14:** 21.9 · **Volume ratio 20D:** 1.00 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 101–114, entry trigger **114**, stop **107**, risk 7 points (6.14%).

**Targets:** TP1 **125** (1.57R), TP2 **145** (4.43R), TP3 **149** (5.00R). Recommended base-case RR: **4.43R**.

**Why entry:** Hybrid entry uses close 109 and ATR14 21.9: buy zone 101–114. Entry is valid only if price can trade/hold around 114 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 107 is placed below support structure (108 / 108). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 125 (1.57R), TP2 145 (4.43R), TP3 149 (5.00R). Targets are ATR/structure capped for hold_days=1. ATR14=21.9, resistance_5/10/20/60=145/174/224/240. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## GTSI — scalping_continual_defensive — CONDITIONAL

**Score:** 0.718 vs policy min 0.05 · **Close:** 123 · **ATR14:** 20.5 · **Volume ratio 20D:** 1.96 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 115–128, entry trigger **128**, stop **118**, risk 10 points (7.81%).

**Targets:** TP1 **139** (1.10R), TP2 **145** (1.70R), TP3 **180** (5.20R). Recommended base-case RR: **1.70R**.

**Why entry:** Hybrid entry uses close 123 and ATR14 20.5: buy zone 115–128. Entry is valid only if price can trade/hold around 128 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 118 is placed below support structure (119 / 119). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 139 (1.10R), TP2 145 (1.70R), TP3 180 (5.20R). Targets are ATR/structure capped for hold_days=1. ATR14=20.5, resistance_5/10/20/60=180/214/238/340. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.10R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BNBR — momentum_5d_continual_defensive — CONDITIONAL

**Score:** 0.629 vs policy min 0.30 · **Close:** 109 · **ATR14:** 21.9 · **Volume ratio 20D:** 1.00 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 101–114, entry trigger **114**, stop **107**, risk 7 points (6.14%).

**Targets:** TP1 **145** (4.43R), TP2 **149** (5.00R), TP3 **153** (5.57R). Recommended base-case RR: **5.00R**.

**Why entry:** Hybrid entry uses close 109 and ATR14 21.9: buy zone 101–114. Entry is valid only if price can trade/hold around 114 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 107 is placed below support structure (108 / 108). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 145 (4.43R), TP2 149 (5.00R), TP3 153 (5.57R). Targets are ATR/structure capped for hold_days=3. ATR14=21.9, resistance_5/10/20/60=145/174/224/240. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## BNBR — swing_continual_defensive — CONDITIONAL

**Score:** 0.629 vs policy min 0.30 · **Close:** 109 · **ATR14:** 21.9 · **Volume ratio 20D:** 1.00 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 101–114, entry trigger **114**, stop **107**, risk 7 points (6.14%).

**Targets:** TP1 **125** (1.57R), TP2 **145** (4.43R), TP3 **149** (5.00R). Recommended base-case RR: **4.43R**.

**Why entry:** Hybrid entry uses close 109 and ATR14 21.9: buy zone 101–114. Entry is valid only if price can trade/hold around 114 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 107 is placed below support structure (108 / 108). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 125 (1.57R), TP2 145 (4.43R), TP3 149 (5.00R). Targets are ATR/structure capped for hold_days=1. ATR14=21.9, resistance_5/10/20/60=145/174/224/240. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## HUMI — momentum_5d_continual_defensive — CONDITIONAL

**Score:** 0.626 vs policy min 0.30 · **Close:** 120 · **ATR14:** 18.1 · **Volume ratio 20D:** 1.02 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 113–124, entry trigger **124**, stop **115**, risk 9 points (7.26%).

**Targets:** TP1 **156** (3.56R), TP2 **161** (4.11R), TP3 **166** (4.67R). Recommended base-case RR: **4.11R**.

**Why entry:** Hybrid entry uses close 120 and ATR14 18.1: buy zone 113–124. Entry is valid only if price can trade/hold around 124 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 115 is placed below support structure (116 / 116). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 156 (3.56R), TP2 161 (4.11R), TP3 166 (4.67R). Targets are ATR/structure capped for hold_days=3. ATR14=18.1, resistance_5/10/20/60=161/194/195/276. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## HUMI — swing_continual_defensive — CONDITIONAL

**Score:** 0.626 vs policy min 0.30 · **Close:** 120 · **ATR14:** 18.1 · **Volume ratio 20D:** 1.02 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 113–124, entry trigger **124**, stop **115**, risk 9 points (7.26%).

**Targets:** TP1 **134** (1.11R), TP2 **157** (3.67R), TP3 **161** (4.11R). Recommended base-case RR: **3.67R**.

**Why entry:** Hybrid entry uses close 120 and ATR14 18.1: buy zone 113–124. Entry is valid only if price can trade/hold around 124 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 115 is placed below support structure (116 / 116). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 134 (1.11R), TP2 157 (3.67R), TP3 161 (4.11R). Targets are ATR/structure capped for hold_days=1. ATR14=18.1, resistance_5/10/20/60=161/194/195/276. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.11R is below strategy minimum 1.25R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## DEWA — swing_continual_defensive — CONDITIONAL

**Score:** 0.623 vs policy min 0.30 · **Close:** 294 · **ATR14:** 45.4 · **Volume ratio 20D:** 1.43 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 278–304, entry trigger **304**, stop **282**, risk 22 points (7.24%).

**Targets:** TP1 **328** (1.09R), TP2 **384** (3.64R), TP3 **396** (4.18R). Recommended base-case RR: **3.64R**.

**Why entry:** Hybrid entry uses close 294 and ATR14 45.4: buy zone 278–304. Entry is valid only if price can trade/hold around 304 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 282 is placed below support structure (284 / 284). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 328 (1.09R), TP2 384 (3.64R), TP3 396 (4.18R). Targets are ATR/structure capped for hold_days=1. ATR14=45.4, resistance_5/10/20/60=384/482/535/630. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.09R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## OASA — momentum_10d_continual_aggressive — CONDITIONAL

**Score:** 0.616 vs policy min 0.30 · **Close:** 298 · **ATR14:** 44.4 · **Volume ratio 20D:** 0.66 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 282–308, entry trigger **308**, stop **296**, risk 12 points (3.90%).

**Targets:** TP1 **408** (8.33R), TP2 **414** (8.83R), TP3 **420** (9.33R). Recommended base-case RR: **8.83R**.

**Why entry:** Hybrid entry uses close 298 and ATR14 44.4: buy zone 282–308. Entry is valid only if price can trade/hold around 308 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 296 is placed below support structure (298 / 298). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 408 (8.33R), TP2 414 (8.83R), TP3 420 (9.33R). Targets are ATR/structure capped for hold_days=5. ATR14=44.4, resistance_5/10/20/60=408/432/466/476. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## BNBR — momentum_10d_continual_aggressive — CONDITIONAL

**Score:** 0.607 vs policy min 0.30 · **Close:** 109 · **ATR14:** 21.9 · **Volume ratio 20D:** 1.00 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 101–114, entry trigger **114**, stop **107**, risk 7 points (6.14%).

**Targets:** TP1 **145** (4.43R), TP2 **149** (5.00R), TP3 **153** (5.57R). Recommended base-case RR: **5.00R**.

**Why entry:** Hybrid entry uses close 109 and ATR14 21.9: buy zone 101–114. Entry is valid only if price can trade/hold around 114 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 107 is placed below support structure (108 / 108). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 145 (4.43R), TP2 149 (5.00R), TP3 153 (5.57R). Targets are ATR/structure capped for hold_days=5. ATR14=21.9, resistance_5/10/20/60=145/174/224/240. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## GTSI — momentum_5d_continual_defensive — CONDITIONAL

**Score:** 0.593 vs policy min 0.30 · **Close:** 123 · **ATR14:** 20.5 · **Volume ratio 20D:** 1.96 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 115–128, entry trigger **128**, stop **118**, risk 10 points (7.81%).

**Targets:** TP1 **139** (1.10R), TP2 **180** (5.20R), TP3 **185** (5.70R). Recommended base-case RR: **5.20R**.

**Why entry:** Hybrid entry uses close 123 and ATR14 20.5: buy zone 115–128. Entry is valid only if price can trade/hold around 128 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 118 is placed below support structure (119 / 119). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 139 (1.10R), TP2 180 (5.20R), TP3 185 (5.70R). Targets are ATR/structure capped for hold_days=3. ATR14=20.5, resistance_5/10/20/60=180/214/238/340. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.10R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## GTSI — swing_continual_defensive — CONDITIONAL

**Score:** 0.593 vs policy min 0.30 · **Close:** 123 · **ATR14:** 20.5 · **Volume ratio 20D:** 1.96 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 115–128, entry trigger **128**, stop **118**, risk 10 points (7.81%).

**Targets:** TP1 **139** (1.10R), TP2 **145** (1.70R), TP3 **180** (5.20R). Recommended base-case RR: **1.70R**.

**Why entry:** Hybrid entry uses close 123 and ATR14 20.5: buy zone 115–128. Entry is valid only if price can trade/hold around 128 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 118 is placed below support structure (119 / 119). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 139 (1.10R), TP2 145 (1.70R), TP3 180 (5.20R). Targets are ATR/structure capped for hold_days=1. ATR14=20.5, resistance_5/10/20/60=180/214/238/340. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.10R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## DEFI — momentum_5d_continual_defensive — CONDITIONAL

**Score:** 0.576 vs policy min 0.30 · **Close:** 110 · **ATR14:** 28.4 · **Volume ratio 20D:** 0.23 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 100–116, entry trigger **116**, stop **109**, risk 7 points (6.03%).

**Targets:** TP1 **164** (6.86R), TP2 **168** (7.43R), TP3 **172** (8.00R). Recommended base-case RR: **7.43R**.

**Why entry:** Hybrid entry uses close 110 and ATR14 28.4: buy zone 100–116. Entry is valid only if price can trade/hold around 116 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 109 is placed below support structure (110 / 110). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 164 (6.86R), TP2 168 (7.43R), TP3 172 (8.00R). Targets are ATR/structure capped for hold_days=3. ATR14=28.4, resistance_5/10/20/60=164/188/250/274. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** volume ratio 0.23 below required 0.60; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## DEFI — swing_continual_defensive — CONDITIONAL

**Score:** 0.576 vs policy min 0.30 · **Close:** 110 · **ATR14:** 28.4 · **Volume ratio 20D:** 0.23 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 100–116, entry trigger **116**, stop **109**, risk 7 points (6.03%).

**Targets:** TP1 **131** (2.14R), TP2 **164** (6.86R), TP3 **168** (7.43R). Recommended base-case RR: **6.86R**.

**Why entry:** Hybrid entry uses close 110 and ATR14 28.4: buy zone 100–116. Entry is valid only if price can trade/hold around 116 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 109 is placed below support structure (110 / 110). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 131 (2.14R), TP2 164 (6.86R), TP3 168 (7.43R). Targets are ATR/structure capped for hold_days=1. ATR14=28.4, resistance_5/10/20/60=164/188/250/274. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** volume ratio 0.23 below required 0.60; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## BNBR — position_continual — CONDITIONAL

**Score:** 0.320 vs policy min 0.30 · **Close:** 109 · **ATR14:** 21.9 · **Volume ratio 20D:** 1.00 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 101–114, entry trigger **114**, stop **107**, risk 7 points (6.14%).

**Targets:** TP1 **145** (4.43R), TP2 **149** (5.00R), TP3 **153** (5.57R). Recommended base-case RR: **5.00R**.

**Why entry:** Hybrid entry uses close 109 and ATR14 21.9: buy zone 101–114. Entry is valid only if price can trade/hold around 114 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 107 is placed below support structure (108 / 108). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 145 (4.43R), TP2 149 (5.00R), TP3 153 (5.57R). Targets are ATR/structure capped for hold_days=10. ATR14=21.9, resistance_5/10/20/60=145/174/224/240. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## COCO — position_continual — CONDITIONAL

**Score:** 0.313 vs policy min 0.30 · **Close:** 206 · **ATR14:** 38.0 · **Volume ratio 20D:** 0.57 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 192–214, entry trigger **214**, stop **204**, risk 10 points (4.67%).

**Targets:** TP1 **274** (6.00R), TP2 **280** (6.60R), TP3 **286** (7.20R). Recommended base-case RR: **6.60R**.

**Why entry:** Hybrid entry uses close 206 and ATR14 38.0: buy zone 192–214. Entry is valid only if price can trade/hold around 214 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 204 is placed below support structure (206 / 206). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 274 (6.00R), TP2 280 (6.60R), TP3 286 (7.20R). Targets are ATR/structure capped for hold_days=10. ATR14=38.0, resistance_5/10/20/60=274/336/402/570. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** volume ratio 0.57 below required 0.60; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## RISE — momentum_5d_continual_defensive — NO_TRADE

**Score:** 0.582 vs policy min 0.30 · **Close:** 995 · **ATR14:** 162.5 · **Volume ratio 20D:** 3.86 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 935–1,030, entry trigger **1,030**, stop **945**, risk 85 points (8.25%).

**Targets:** TP1 **1,115** (1.00R), TP2 **1,515** (5.71R), TP3 **1,560** (6.24R). Recommended base-case RR: **5.71R**.

**Why entry:** Hybrid entry uses close 995 and ATR14 162.5: buy zone 935–1,030. Entry is valid only if price can trade/hold around 1,030 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 945 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,115 (1.00R), TP2 1,515 (5.71R), TP3 1,560 (6.24R). Targets are ATR/structure capped for hold_days=3. ATR14=162.5, resistance_5/10/20/60=1,515/1,575/1,810/3,520. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.25% exceeds max strategy risk 8.00%; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## RISE — swing_continual_defensive — NO_TRADE

**Score:** 0.582 vs policy min 0.30 · **Close:** 995 · **ATR14:** 162.5 · **Volume ratio 20D:** 3.86 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 935–1,030, entry trigger **1,030**, stop **945**, risk 85 points (8.25%).

**Targets:** TP1 **1,115** (1.00R), TP2 **1,175** (1.71R), TP3 **1,235** (2.41R). Recommended base-case RR: **1.71R**.

**Why entry:** Hybrid entry uses close 995 and ATR14 162.5: buy zone 935–1,030. Entry is valid only if price can trade/hold around 1,030 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 945 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,115 (1.00R), TP2 1,175 (1.71R), TP3 1,235 (2.41R). Targets are ATR/structure capped for hold_days=1. ATR14=162.5, resistance_5/10/20/60=1,515/1,575/1,810/3,520. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.25% exceeds max strategy risk 8.00%; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## ASPR — momentum_5d_continual_defensive — NO_TRADE

**Score:** 0.575 vs policy min 0.30 · **Close:** 184 · **ATR14:** 72.7 · **Volume ratio 20D:** 0.56 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 158–199, entry trigger **199**, stop **183**, risk 16 points (8.04%).

**Targets:** TP1 **246** (2.94R), TP2 **254** (3.44R), TP3 **262** (3.94R). Recommended base-case RR: **3.44R**.

**Why entry:** Hybrid entry uses close 184 and ATR14 72.7: buy zone 158–199. Entry is valid only if price can trade/hold around 199 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 183 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 246 (2.94R), TP2 254 (3.44R), TP3 262 (3.94R). Targets are ATR/structure capped for hold_days=3. ATR14=72.7, resistance_5/10/20/60=246/540/620/620. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 8.15% > max 8.00%; entry-to-stop risk 8.04% exceeds max strategy risk 8.00%; volume ratio 0.56 below required 0.60; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## ASPR — swing_continual_defensive — NO_TRADE

**Score:** 0.575 vs policy min 0.30 · **Close:** 184 · **ATR14:** 72.7 · **Volume ratio 20D:** 0.56 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 158–199, entry trigger **199**, stop **183**, risk 16 points (8.04%).

**Targets:** TP1 **246** (2.94R), TP2 **254** (3.44R), TP3 **262** (3.94R). Recommended base-case RR: **3.44R**.

**Why entry:** Hybrid entry uses close 184 and ATR14 72.7: buy zone 158–199. Entry is valid only if price can trade/hold around 199 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 183 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 246 (2.94R), TP2 254 (3.44R), TP3 262 (3.94R). Targets are ATR/structure capped for hold_days=1. ATR14=72.7, resistance_5/10/20/60=246/540/620/620. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 8.15% > max 8.00%; entry-to-stop risk 8.04% exceeds max strategy risk 8.00%; volume ratio 0.56 below required 0.60; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## BULL — momentum_20d_continual_research — NO_TRADE

**Score:** 0.418 vs policy min 0.30 · **Close:** 324 · **ATR14:** 44.3 · **Volume ratio 20D:** 1.60 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 308–334, entry trigger **334**, stop **322**, risk 12 points (3.59%).

**Targets:** TP1 **428** (7.83R), TP2 **434** (8.33R), TP3 **440** (8.83R). Recommended base-case RR: **8.33R**.

**Why entry:** Hybrid entry uses close 324 and ATR14 44.3: buy zone 308–334. Entry is valid only if price can trade/hold around 334 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 322 is placed below support structure (324 / 324). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 428 (7.83R), TP2 434 (8.33R), TP3 440 (8.83R). Targets are ATR/structure capped for hold_days=10. ATR14=44.3, resistance_5/10/20/60=428/458/545/610. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** strategy policy has execution_enabled=false

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BUVA — momentum_20d_continual_research — NO_TRADE

**Score:** 0.408 vs policy min 0.30 · **Close:** 725 · **ATR14:** 123.9 · **Volume ratio 20D:** 0.87 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 680–750, entry trigger **750**, stop **690**, risk 60 points (8.00%).

**Targets:** TP1 **895** (2.42R), TP2 **925** (2.92R), TP3 **955** (3.42R). Recommended base-case RR: **2.92R**.

**Why entry:** Hybrid entry uses close 725 and ATR14 123.9: buy zone 680–750. Entry is valid only if price can trade/hold around 750 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 690 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 895 (2.42R), TP2 925 (2.92R), TP3 955 (3.42R). Targets are ATR/structure capped for hold_days=10. ATR14=123.9, resistance_5/10/20/60=895/1,020/1,175/1,695. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** strategy policy has execution_enabled=false

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## DEWA — momentum_20d_continual_research — NO_TRADE

**Score:** 0.404 vs policy min 0.30 · **Close:** 294 · **ATR14:** 45.4 · **Volume ratio 20D:** 1.43 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 278–304, entry trigger **304**, stop **282**, risk 22 points (7.24%).

**Targets:** TP1 **384** (3.64R), TP2 **396** (4.18R), TP3 **408** (4.73R). Recommended base-case RR: **4.18R**.

**Why entry:** Hybrid entry uses close 294 and ATR14 45.4: buy zone 278–304. Entry is valid only if price can trade/hold around 304 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 282 is placed below support structure (284 / 284). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 384 (3.64R), TP2 396 (4.18R), TP3 408 (4.73R). Targets are ATR/structure capped for hold_days=10. ATR14=45.4, resistance_5/10/20/60=384/482/535/630. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** strategy policy has execution_enabled=false

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BRMS — momentum_20d_continual_research — NO_TRADE

**Score:** 0.349 vs policy min 0.30 · **Close:** 535 · **ATR14:** 73.7 · **Volume ratio 20D:** 1.35 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 505–550, entry trigger **550**, stop **505**, risk 45 points (8.18%).

**Targets:** TP1 **635** (1.89R), TP2 **660** (2.44R), TP3 **685** (3.00R). Recommended base-case RR: **2.44R**.

**Why entry:** Hybrid entry uses close 535 and ATR14 73.7: buy zone 505–550. Entry is valid only if price can trade/hold around 550 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 505 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 635 (1.89R), TP2 660 (2.44R), TP3 685 (3.00R). Targets are ATR/structure capped for hold_days=10. ATR14=73.7, resistance_5/10/20/60=635/755/845/1,085. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** strategy policy has execution_enabled=false; entry-to-stop risk 8.18% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BNBR — momentum_20d_continual_research — NO_TRADE

**Score:** 0.332 vs policy min 0.30 · **Close:** 109 · **ATR14:** 21.9 · **Volume ratio 20D:** 1.00 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 101–114, entry trigger **114**, stop **107**, risk 7 points (6.14%).

**Targets:** TP1 **145** (4.43R), TP2 **149** (5.00R), TP3 **153** (5.57R). Recommended base-case RR: **5.00R**.

**Why entry:** Hybrid entry uses close 109 and ATR14 21.9: buy zone 101–114. Entry is valid only if price can trade/hold around 114 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 107 is placed below support structure (108 / 108). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 145 (4.43R), TP2 149 (5.00R), TP3 153 (5.57R). Targets are ATR/structure capped for hold_days=10. ATR14=21.9, resistance_5/10/20/60=145/174/224/240. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** strategy policy has execution_enabled=false; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## RISE — position_continual — NO_TRADE

**Score:** 0.327 vs policy min 0.30 · **Close:** 995 · **ATR14:** 162.5 · **Volume ratio 20D:** 3.86 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 935–1,030, entry trigger **1,030**, stop **945**, risk 85 points (8.25%).

**Targets:** TP1 **1,515** (5.71R), TP2 **1,560** (6.24R), TP3 **1,605** (6.76R). Recommended base-case RR: **6.24R**.

**Why entry:** Hybrid entry uses close 995 and ATR14 162.5: buy zone 935–1,030. Entry is valid only if price can trade/hold around 1,030 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 945 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,515 (5.71R), TP2 1,560 (6.24R), TP3 1,605 (6.76R). Targets are ATR/structure capped for hold_days=10. ATR14=162.5, resistance_5/10/20/60=1,515/1,575/1,810/3,520. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.25% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BRMS — position_continual — NO_TRADE

**Score:** 0.321 vs policy min 0.30 · **Close:** 535 · **ATR14:** 73.7 · **Volume ratio 20D:** 1.35 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 505–550, entry trigger **550**, stop **505**, risk 45 points (8.18%).

**Targets:** TP1 **635** (1.89R), TP2 **660** (2.44R), TP3 **685** (3.00R). Recommended base-case RR: **2.44R**.

**Why entry:** Hybrid entry uses close 535 and ATR14 73.7: buy zone 505–550. Entry is valid only if price can trade/hold around 550 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 505 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 635 (1.89R), TP2 660 (2.44R), TP3 685 (3.00R). Targets are ATR/structure capped for hold_days=10. ATR14=73.7, resistance_5/10/20/60=635/755/845/1,085. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.18% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## MSIN — position_continual — NO_TRADE

**Score:** 0.315 vs policy min 0.30 · **Close:** 458 · **ATR14:** 83.9 · **Volume ratio 20D:** 3.80 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 428–476, entry trigger **476**, stop **436**, risk 40 points (8.40%).

**Targets:** TP1 **555** (1.98R), TP2 **575** (2.48R), TP3 **595** (2.98R). Recommended base-case RR: **2.48R**.

**Why entry:** Hybrid entry uses close 458 and ATR14 83.9: buy zone 428–476. Entry is valid only if price can trade/hold around 476 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 436 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 555 (1.98R), TP2 575 (2.48R), TP3 595 (2.98R). Targets are ATR/structure capped for hold_days=10. ATR14=83.9, resistance_5/10/20/60=555/680/900/1,450. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.40% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---
