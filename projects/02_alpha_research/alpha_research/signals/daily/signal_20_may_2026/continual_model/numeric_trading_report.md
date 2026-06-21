# Numeric Trading Desk Report — 2026-05-19

This report is generated from live model scores, selected signal policy, canonical OHLCV, ATR, support/resistance, liquidity, and broker-flow diagnostics. It is not a simple BUY/SELL list; each plan is conditional on execution behaviour.

## Summary

| Plan quality | Count |
|---|---:|
| ACTIONABLE | 12 |
| CONDITIONAL | 19 |
| WATCHLIST_ONLY | 1 |
| NO_TRADE | 10 |

## DSSA — scalping_continual_defensive — ACTIONABLE

**Score:** 0.758 vs policy min 0.05 · **Close:** 750 · **ATR14:** 245.4 · **Volume ratio 20D:** 5.23 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 660–800, entry trigger **800**, stop **745**, risk 55 points (6.88%).

**Targets:** TP1 **925** (2.27R), TP2 **955** (2.82R), TP3 **985** (3.36R). Recommended base-case RR: **2.82R**.

**Why entry:** Hybrid entry uses close 750 and ATR14 245.4: buy zone 660–800. Entry is valid only if price can trade/hold around 800 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 745 is placed below support structure (750 / 750). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 925 (2.27R), TP2 955 (2.82R), TP3 985 (3.36R). Targets are ATR/structure capped for hold_days=1. ATR14=245.4, resistance_5/10/20/60=1,660/2,110/3,500/98,000. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## CUAN — scalping_continual_defensive — ACTIONABLE

**Score:** 0.756 vs policy min 0.05 · **Close:** 650 · **ATR14:** 119.6 · **Volume ratio 20D:** 1.49 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 605–675, entry trigger **675**, stop **635**, risk 40 points (5.93%).

**Targets:** TP1 **735** (1.50R), TP2 **745** (1.75R), TP3 **775** (2.50R). Recommended base-case RR: **1.75R**.

**Why entry:** Hybrid entry uses close 650 and ATR14 119.6: buy zone 605–675. Entry is valid only if price can trade/hold around 675 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 635 is placed below support structure (640 / 640). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 735 (1.50R), TP2 745 (1.75R), TP3 775 (2.50R). Targets are ATR/structure capped for hold_days=1. ATR14=119.6, resistance_5/10/20/60=1,305/1,360/1,620/1,990. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## CUAN — momentum_5d_continual_defensive — ACTIONABLE

**Score:** 0.687 vs policy min 0.30 · **Close:** 650 · **ATR14:** 119.6 · **Volume ratio 20D:** 1.49 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 605–675, entry trigger **675**, stop **635**, risk 40 points (5.93%).

**Targets:** TP1 **735** (1.50R), TP2 **745** (1.75R), TP3 **775** (2.50R). Recommended base-case RR: **1.75R**.

**Why entry:** Hybrid entry uses close 650 and ATR14 119.6: buy zone 605–675. Entry is valid only if price can trade/hold around 675 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 635 is placed below support structure (640 / 640). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 735 (1.50R), TP2 745 (1.75R), TP3 775 (2.50R). Targets are ATR/structure capped for hold_days=3. ATR14=119.6, resistance_5/10/20/60=1,305/1,360/1,620/1,990. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## CUAN — swing_continual_defensive — ACTIONABLE

**Score:** 0.687 vs policy min 0.30 · **Close:** 650 · **ATR14:** 119.6 · **Volume ratio 20D:** 1.49 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 605–675, entry trigger **675**, stop **635**, risk 40 points (5.93%).

**Targets:** TP1 **735** (1.50R), TP2 **745** (1.75R), TP3 **775** (2.50R). Recommended base-case RR: **1.75R**.

**Why entry:** Hybrid entry uses close 650 and ATR14 119.6: buy zone 605–675. Entry is valid only if price can trade/hold around 675 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 635 is placed below support structure (640 / 640). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 735 (1.50R), TP2 745 (1.75R), TP3 775 (2.50R). Targets are ATR/structure capped for hold_days=1. ATR14=119.6, resistance_5/10/20/60=1,305/1,360/1,620/1,990. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## DSSA — momentum_5d_continual_defensive — ACTIONABLE

**Score:** 0.669 vs policy min 0.30 · **Close:** 750 · **ATR14:** 245.4 · **Volume ratio 20D:** 5.23 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 660–800, entry trigger **800**, stop **745**, risk 55 points (6.88%).

**Targets:** TP1 **925** (2.27R), TP2 **955** (2.82R), TP3 **1,660** (15.64R). Recommended base-case RR: **2.82R**.

**Why entry:** Hybrid entry uses close 750 and ATR14 245.4: buy zone 660–800. Entry is valid only if price can trade/hold around 800 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 745 is placed below support structure (750 / 750). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 925 (2.27R), TP2 955 (2.82R), TP3 1,660 (15.64R). Targets are ATR/structure capped for hold_days=3. ATR14=245.4, resistance_5/10/20/60=1,660/2,110/3,500/98,000. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## DSSA — swing_continual_defensive — ACTIONABLE

**Score:** 0.669 vs policy min 0.30 · **Close:** 750 · **ATR14:** 245.4 · **Volume ratio 20D:** 5.23 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 660–800, entry trigger **800**, stop **745**, risk 55 points (6.88%).

**Targets:** TP1 **925** (2.27R), TP2 **955** (2.82R), TP3 **985** (3.36R). Recommended base-case RR: **2.82R**.

**Why entry:** Hybrid entry uses close 750 and ATR14 245.4: buy zone 660–800. Entry is valid only if price can trade/hold around 800 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 745 is placed below support structure (750 / 750). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 925 (2.27R), TP2 955 (2.82R), TP3 985 (3.36R). Targets are ATR/structure capped for hold_days=1. ATR14=245.4, resistance_5/10/20/60=1,660/2,110/3,500/98,000. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## DSSA — momentum_10d_continual_aggressive — ACTIONABLE

**Score:** 0.572 vs policy min 0.30 · **Close:** 750 · **ATR14:** 245.4 · **Volume ratio 20D:** 5.23 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 660–800, entry trigger **800**, stop **745**, risk 55 points (6.88%).

**Targets:** TP1 **925** (2.27R), TP2 **1,660** (15.64R), TP3 **1,690** (16.18R). Recommended base-case RR: **15.64R**.

**Why entry:** Hybrid entry uses close 750 and ATR14 245.4: buy zone 660–800. Entry is valid only if price can trade/hold around 800 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 745 is placed below support structure (750 / 750). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 925 (2.27R), TP2 1,660 (15.64R), TP3 1,690 (16.18R). Targets are ATR/structure capped for hold_days=5. ATR14=245.4, resistance_5/10/20/60=1,660/2,110/3,500/98,000. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## CUAN — momentum_10d_continual_aggressive — ACTIONABLE

**Score:** 0.559 vs policy min 0.30 · **Close:** 650 · **ATR14:** 119.6 · **Volume ratio 20D:** 1.49 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 605–675, entry trigger **675**, stop **635**, risk 40 points (5.93%).

**Targets:** TP1 **735** (1.50R), TP2 **745** (1.75R), TP3 **1,305** (15.75R). Recommended base-case RR: **1.75R**.

**Why entry:** Hybrid entry uses close 650 and ATR14 119.6: buy zone 605–675. Entry is valid only if price can trade/hold around 675 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 635 is placed below support structure (640 / 640). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 735 (1.50R), TP2 745 (1.75R), TP3 1,305 (15.75R). Targets are ATR/structure capped for hold_days=5. ATR14=119.6, resistance_5/10/20/60=1,305/1,360/1,620/1,990. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## NSSS — position_continual — ACTIONABLE

**Score:** 0.348 vs policy min 0.30 · **Close:** 605 · **ATR14:** 80.0 · **Volume ratio 20D:** 0.66 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 575–625, entry trigger **625**, stop **590**, risk 35 points (5.60%).

**Targets:** TP1 **850** (6.43R), TP2 **870** (7.00R), TP3 **890** (7.57R). Recommended base-case RR: **7.00R**.

**Why entry:** Hybrid entry uses close 605 and ATR14 80.0: buy zone 575–625. Entry is valid only if price can trade/hold around 625 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 590 is placed below support structure (595 / 595). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 850 (6.43R), TP2 870 (7.00R), TP3 890 (7.57R). Targets are ATR/structure capped for hold_days=10. ATR14=80.0, resistance_5/10/20/60=850/935/1,060/1,300. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## DSSA — position_continual — ACTIONABLE

**Score:** 0.324 vs policy min 0.30 · **Close:** 750 · **ATR14:** 245.4 · **Volume ratio 20D:** 5.23 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 660–800, entry trigger **800**, stop **745**, risk 55 points (6.88%).

**Targets:** TP1 **925** (2.27R), TP2 **1,660** (15.64R), TP3 **1,690** (16.18R). Recommended base-case RR: **15.64R**.

**Why entry:** Hybrid entry uses close 750 and ATR14 245.4: buy zone 660–800. Entry is valid only if price can trade/hold around 800 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 745 is placed below support structure (750 / 750). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 925 (2.27R), TP2 1,660 (15.64R), TP3 1,690 (16.18R). Targets are ATR/structure capped for hold_days=10. ATR14=245.4, resistance_5/10/20/60=1,660/2,110/3,500/98,000. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## CUAN — position_continual — ACTIONABLE

**Score:** 0.312 vs policy min 0.30 · **Close:** 650 · **ATR14:** 119.6 · **Volume ratio 20D:** 1.49 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 605–675, entry trigger **675**, stop **635**, risk 40 points (5.93%).

**Targets:** TP1 **735** (1.50R), TP2 **1,305** (15.75R), TP3 **1,325** (16.25R). Recommended base-case RR: **15.75R**.

**Why entry:** Hybrid entry uses close 650 and ATR14 119.6: buy zone 605–675. Entry is valid only if price can trade/hold around 675 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 635 is placed below support structure (640 / 640). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 735 (1.50R), TP2 1,305 (15.75R), TP3 1,325 (16.25R). Targets are ATR/structure capped for hold_days=10. ATR14=119.6, resistance_5/10/20/60=1,305/1,360/1,620/1,990. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BANK — position_continual — ACTIONABLE

**Score:** 0.308 vs policy min 0.30 · **Close:** 380 · **ATR14:** 63.0 · **Volume ratio 20D:** 2.97 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 356–394, entry trigger **394**, stop **376**, risk 18 points (4.57%).

**Targets:** TP1 **426** (1.78R), TP2 **630** (13.11R), TP3 **640** (13.67R). Recommended base-case RR: **13.11R**.

**Why entry:** Hybrid entry uses close 380 and ATR14 63.0: buy zone 356–394. Entry is valid only if price can trade/hold around 394 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 376 is placed below support structure (378 / 378). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 426 (1.78R), TP2 630 (13.11R), TP3 640 (13.67R). Targets are ATR/structure capped for hold_days=10. ATR14=63.0, resistance_5/10/20/60=630/640/640/655. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BUMI — ara_candidate_continual — CONDITIONAL

**Score:** 0.876 vs policy min 0.50 · **Close:** 186 · **ATR14:** 14.4 · **Volume ratio 20D:** 2.85 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 180–189, entry trigger **189**, stop **177**, risk 12 points (6.35%).

**Targets:** TP1 **202** (1.08R), TP2 **210** (1.75R), TP3 **218** (2.42R). Recommended base-case RR: **1.75R**.

**Why entry:** Hybrid entry uses close 186 and ATR14 14.4: buy zone 180–189. Entry is valid only if price can trade/hold around 189 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 177 is placed below support structure (178 / 178). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 202 (1.08R), TP2 210 (1.75R), TP3 218 (2.42R). Targets are ATR/structure capped for hold_days=1. ATR14=14.4, resistance_5/10/20/60=238/250/268/306. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.08R is below strategy minimum 1.25R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## PSAB — scalping_continual_defensive — CONDITIONAL

**Score:** 0.742 vs policy min 0.05 · **Close:** 412 · **ATR14:** 37.1 · **Volume ratio 20D:** 1.50 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 398–420, entry trigger **420**, stop **402**, risk 18 points (4.29%).

**Targets:** TP1 **440** (1.11R), TP2 **452** (1.78R), TP3 **464** (2.44R). Recommended base-case RR: **1.78R**.

**Why entry:** Hybrid entry uses close 412 and ATR14 37.1: buy zone 398–420. Entry is valid only if price can trade/hold around 420 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 402 is placed below support structure (404 / 404). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 440 (1.11R), TP2 452 (1.78R), TP3 464 (2.44R). Targets are ATR/structure capped for hold_days=1. ATR14=37.1, resistance_5/10/20/60=580/580/590/590. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.11R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## MBMA — scalping_continual_defensive — CONDITIONAL

**Score:** 0.717 vs policy min 0.05 · **Close:** 476 · **ATR14:** 47.6 · **Volume ratio 20D:** 3.70 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 458–486, entry trigger **486**, stop **462**, risk 24 points (4.94%).

**Targets:** TP1 **510** (1.00R), TP2 **530** (1.83R), TP3 **545** (2.46R). Recommended base-case RR: **1.83R**.

**Why entry:** Hybrid entry uses close 476 and ATR14 47.6: buy zone 458–486. Entry is valid only if price can trade/hold around 486 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 462 is placed below support structure (464 / 464). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 510 (1.00R), TP2 530 (1.83R), TP3 545 (2.46R). Targets are ATR/structure capped for hold_days=1. ATR14=47.6, resistance_5/10/20/60=680/710/775/945. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## MBMA — momentum_5d_continual_defensive — CONDITIONAL

**Score:** 0.652 vs policy min 0.30 · **Close:** 476 · **ATR14:** 47.6 · **Volume ratio 20D:** 3.70 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 458–486, entry trigger **486**, stop **462**, risk 24 points (4.94%).

**Targets:** TP1 **510** (1.00R), TP2 **530** (1.83R), TP3 **680** (8.08R). Recommended base-case RR: **1.83R**.

**Why entry:** Hybrid entry uses close 476 and ATR14 47.6: buy zone 458–486. Entry is valid only if price can trade/hold around 486 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 462 is placed below support structure (464 / 464). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 510 (1.00R), TP2 530 (1.83R), TP3 680 (8.08R). Targets are ATR/structure capped for hold_days=3. ATR14=47.6, resistance_5/10/20/60=680/710/775/945. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## MBMA — swing_continual_defensive — CONDITIONAL

**Score:** 0.652 vs policy min 0.30 · **Close:** 476 · **ATR14:** 47.6 · **Volume ratio 20D:** 3.70 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 458–486, entry trigger **486**, stop **462**, risk 24 points (4.94%).

**Targets:** TP1 **510** (1.00R), TP2 **530** (1.83R), TP3 **545** (2.46R). Recommended base-case RR: **1.83R**.

**Why entry:** Hybrid entry uses close 476 and ATR14 47.6: buy zone 458–486. Entry is valid only if price can trade/hold around 486 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 462 is placed below support structure (464 / 464). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 510 (1.00R), TP2 530 (1.83R), TP3 545 (2.46R). Targets are ATR/structure capped for hold_days=1. ATR14=47.6, resistance_5/10/20/60=680/710/775/945. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## FOLK — momentum_5d_continual_defensive — CONDITIONAL

**Score:** 0.578 vs policy min 0.30 · **Close:** 252 · **ATR14:** 31.9 · **Volume ratio 20D:** 0.89 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 240–260, entry trigger **260**, stop **244**, risk 16 points (6.15%).

**Targets:** TP1 **276** (1.00R), TP2 **360** (6.25R), TP3 **368** (6.75R). Recommended base-case RR: **6.25R**.

**Why entry:** Hybrid entry uses close 252 and ATR14 31.9: buy zone 240–260. Entry is valid only if price can trade/hold around 260 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 244 is placed below support structure (246 / 246). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 276 (1.00R), TP2 360 (6.25R), TP3 368 (6.75R). Targets are ATR/structure capped for hold_days=3. ATR14=31.9, resistance_5/10/20/60=360/410/410/785. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.25R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## FOLK — swing_continual_defensive — CONDITIONAL

**Score:** 0.578 vs policy min 0.30 · **Close:** 252 · **ATR14:** 31.9 · **Volume ratio 20D:** 0.89 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 240–260, entry trigger **260**, stop **244**, risk 16 points (6.15%).

**Targets:** TP1 **276** (1.00R), TP2 **288** (1.75R), TP3 **300** (2.50R). Recommended base-case RR: **1.75R**.

**Why entry:** Hybrid entry uses close 252 and ATR14 31.9: buy zone 240–260. Entry is valid only if price can trade/hold around 260 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 244 is placed below support structure (246 / 246). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 276 (1.00R), TP2 288 (1.75R), TP3 300 (2.50R). Targets are ATR/structure capped for hold_days=1. ATR14=31.9, resistance_5/10/20/60=360/410/410/785. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.25R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## KOKA — momentum_5d_continual_defensive — CONDITIONAL

**Score:** 0.577 vs policy min 0.30 · **Close:** 128 · **ATR14:** 14.3 · **Volume ratio 20D:** 0.95 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 123–131, entry trigger **131**, stop **122**, risk 9 points (6.87%).

**Targets:** TP1 **140** (1.00R), TP2 **176** (5.00R), TP3 **184** (5.89R). Recommended base-case RR: **5.00R**.

**Why entry:** Hybrid entry uses close 128 and ATR14 14.3: buy zone 123–131. Entry is valid only if price can trade/hold around 131 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 122 is placed below support structure (123 / 123). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 140 (1.00R), TP2 176 (5.00R), TP3 184 (5.89R). Targets are ATR/structure capped for hold_days=3. ATR14=14.3, resistance_5/10/20/60=184/185/226/318. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.25R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## KOKA — swing_continual_defensive — CONDITIONAL

**Score:** 0.577 vs policy min 0.30 · **Close:** 128 · **ATR14:** 14.3 · **Volume ratio 20D:** 0.95 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 123–131, entry trigger **131**, stop **122**, risk 9 points (6.87%).

**Targets:** TP1 **140** (1.00R), TP2 **147** (1.78R), TP3 **153** (2.44R). Recommended base-case RR: **1.78R**.

**Why entry:** Hybrid entry uses close 128 and ATR14 14.3: buy zone 123–131. Entry is valid only if price can trade/hold around 131 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 122 is placed below support structure (123 / 123). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 140 (1.00R), TP2 147 (1.78R), TP3 153 (2.44R). Targets are ATR/structure capped for hold_days=1. ATR14=14.3, resistance_5/10/20/60=184/185/226/318. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.25R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## NICL — momentum_5d_continual_defensive — CONDITIONAL

**Score:** 0.567 vs policy min 0.30 · **Close:** 640 · **ATR14:** 57.5 · **Volume ratio 20D:** 0.34 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 615–655, entry trigger **655**, stop **620**, risk 35 points (5.34%).

**Targets:** TP1 **690** (1.00R), TP2 **715** (1.71R), TP3 **880** (6.43R). Recommended base-case RR: **1.71R**.

**Why entry:** Hybrid entry uses close 640 and ATR14 57.5: buy zone 615–655. Entry is valid only if price can trade/hold around 655 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 620 is placed below support structure (625 / 625). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 690 (1.00R), TP2 715 (1.71R), TP3 880 (6.43R). Targets are ATR/structure capped for hold_days=3. ATR14=57.5, resistance_5/10/20/60=880/925/1,100/1,285. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.25R; volume ratio 0.34 below required 0.60; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## NICL — swing_continual_defensive — CONDITIONAL

**Score:** 0.567 vs policy min 0.30 · **Close:** 640 · **ATR14:** 57.5 · **Volume ratio 20D:** 0.34 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 615–655, entry trigger **655**, stop **620**, risk 35 points (5.34%).

**Targets:** TP1 **690** (1.00R), TP2 **715** (1.71R), TP3 **740** (2.43R). Recommended base-case RR: **1.71R**.

**Why entry:** Hybrid entry uses close 640 and ATR14 57.5: buy zone 615–655. Entry is valid only if price can trade/hold around 655 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 620 is placed below support structure (625 / 625). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 690 (1.00R), TP2 715 (1.71R), TP3 740 (2.43R). Targets are ATR/structure capped for hold_days=1. ATR14=57.5, resistance_5/10/20/60=880/925/1,100/1,285. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.25R; volume ratio 0.34 below required 0.60; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## MBMA — momentum_10d_continual_aggressive — CONDITIONAL

**Score:** 0.559 vs policy min 0.30 · **Close:** 476 · **ATR14:** 47.6 · **Volume ratio 20D:** 3.70 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 458–486, entry trigger **486**, stop **462**, risk 24 points (4.94%).

**Targets:** TP1 **510** (1.00R), TP2 **680** (8.08R), TP3 **695** (8.71R). Recommended base-case RR: **8.08R**.

**Why entry:** Hybrid entry uses close 476 and ATR14 47.6: buy zone 458–486. Entry is valid only if price can trade/hold around 486 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 462 is placed below support structure (464 / 464). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 510 (1.00R), TP2 680 (8.08R), TP3 695 (8.71R). Targets are ATR/structure capped for hold_days=5. ATR14=47.6, resistance_5/10/20/60=680/710/775/945. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## DEWA — momentum_10d_continual_aggressive — CONDITIONAL

**Score:** 0.553 vs policy min 0.30 · **Close:** 388 · **ATR14:** 33.7 · **Volume ratio 20D:** 2.65 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 376–396, entry trigger **396**, stop **372**, risk 24 points (6.06%).

**Targets:** TP1 **420** (1.00R), TP2 **535** (5.79R), TP3 **550** (6.42R). Recommended base-case RR: **5.79R**.

**Why entry:** Hybrid entry uses close 388 and ATR14 33.7: buy zone 376–396. Entry is valid only if price can trade/hold around 396 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 372 is placed below support structure (374 / 374). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 420 (1.00R), TP2 535 (5.79R), TP3 550 (6.42R). Targets are ATR/structure capped for hold_days=5. ATR14=33.7, resistance_5/10/20/60=535/535/595/655. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.25R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## PSAB — momentum_10d_continual_aggressive — CONDITIONAL

**Score:** 0.532 vs policy min 0.30 · **Close:** 412 · **ATR14:** 37.1 · **Volume ratio 20D:** 1.50 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 398–420, entry trigger **420**, stop **402**, risk 18 points (4.29%).

**Targets:** TP1 **440** (1.11R), TP2 **570** (8.33R), TP3 **580** (8.89R). Recommended base-case RR: **8.33R**.

**Why entry:** Hybrid entry uses close 412 and ATR14 37.1: buy zone 398–420. Entry is valid only if price can trade/hold around 420 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 402 is placed below support structure (404 / 404). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 440 (1.11R), TP2 570 (8.33R), TP3 580 (8.89R). Targets are ATR/structure capped for hold_days=5. ATR14=37.1, resistance_5/10/20/60=580/580/590/590. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.11R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## NCKL — momentum_10d_continual_aggressive — CONDITIONAL

**Score:** 0.526 vs policy min 0.30 · **Close:** 870 · **ATR14:** 56.8 · **Volume ratio 20D:** 2.39 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 850–885, entry trigger **885**, stop **845**, risk 40 points (4.52%).

**Targets:** TP1 **925** (1.00R), TP2 **1,070** (4.62R), TP3 **1,090** (5.12R). Recommended base-case RR: **4.62R**.

**Why entry:** Hybrid entry uses close 870 and ATR14 56.8: buy zone 850–885. Entry is valid only if price can trade/hold around 885 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 845 is placed below support structure (850 / 850). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 925 (1.00R), TP2 1,070 (4.62R), TP3 1,090 (5.12R). Targets are ATR/structure capped for hold_days=5. ATR14=56.8, resistance_5/10/20/60=1,070/1,160/1,245/1,595. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BUVA — momentum_10d_continual_aggressive — CONDITIONAL

**Score:** 0.524 vs policy min 0.30 · **Close:** 855 · **ATR14:** 104.6 · **Volume ratio 20D:** 1.50 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 815–880, entry trigger **880**, stop **845**, risk 35 points (3.98%).

**Targets:** TP1 **935** (1.57R), TP2 **1,175** (8.43R), TP3 **1,195** (9.00R). Recommended base-case RR: **8.43R**.

**Why entry:** Hybrid entry uses close 855 and ATR14 104.6: buy zone 815–880. Entry is valid only if price can trade/hold around 880 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 845 is placed below support structure (850 / 850). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 935 (1.57R), TP2 1,175 (8.43R), TP3 1,195 (9.00R). Targets are ATR/structure capped for hold_days=5. ATR14=104.6, resistance_5/10/20/60=1,175/1,190/1,390/1,695. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## BUMI — position_continual — CONDITIONAL

**Score:** 0.302 vs policy min 0.30 · **Close:** 186 · **ATR14:** 14.4 · **Volume ratio 20D:** 2.85 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 180–189, entry trigger **189**, stop **177**, risk 12 points (6.35%).

**Targets:** TP1 **236** (3.92R), TP2 **238** (4.08R), TP3 **244** (4.58R). Recommended base-case RR: **4.08R**.

**Why entry:** Hybrid entry uses close 186 and ATR14 14.4: buy zone 180–189. Entry is valid only if price can trade/hold around 189 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 177 is placed below support structure (178 / 178). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 236 (3.92R), TP2 238 (4.08R), TP3 244 (4.58R). Targets are ATR/structure capped for hold_days=10. ATR14=14.4, resistance_5/10/20/60=238/250/268/306. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## BEEF — position_continual — CONDITIONAL

**Score:** 0.302 vs policy min 0.30 · **Close:** 157 · **ATR14:** 23.2 · **Volume ratio 20D:** 1.30 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 148–162, entry trigger **162**, stop **150**, risk 12 points (7.41%).

**Targets:** TP1 **202** (3.33R), TP2 **208** (3.83R), TP3 **214** (4.33R). Recommended base-case RR: **3.83R**.

**Why entry:** Hybrid entry uses close 157 and ATR14 23.2: buy zone 148–162. Entry is valid only if price can trade/hold around 162 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 150 is placed below support structure (151 / 151). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 202 (3.33R), TP2 208 (3.83R), TP3 214 (4.33R). Targets are ATR/structure capped for hold_days=10. ATR14=23.2, resistance_5/10/20/60=202/244/302/388. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## MBMA — position_continual — CONDITIONAL

**Score:** 0.302 vs policy min 0.30 · **Close:** 476 · **ATR14:** 47.6 · **Volume ratio 20D:** 3.70 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 458–486, entry trigger **486**, stop **462**, risk 24 points (4.94%).

**Targets:** TP1 **510** (1.00R), TP2 **680** (8.08R), TP3 **695** (8.71R). Recommended base-case RR: **8.08R**.

**Why entry:** Hybrid entry uses close 476 and ATR14 47.6: buy zone 458–486. Entry is valid only if price can trade/hold around 486 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 462 is placed below support structure (464 / 464). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 510 (1.00R), TP2 680 (8.08R), TP3 695 (8.71R). Targets are ATR/structure capped for hold_days=10. ATR14=47.6, resistance_5/10/20/60=680/710/775/945. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## SOFA — position_continual — WATCHLIST_ONLY

**Score:** 0.299 vs policy min 0.30 · **Close:** 324 · **ATR14:** 36.6 · **Volume ratio 20D:** 0.83 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 310–332, entry trigger **332**, stop **322**, risk 10 points (3.01%).

**Targets:** TP1 **420** (8.80R), TP2 **426** (9.40R), TP3 **432** (10.00R). Recommended base-case RR: **9.40R**.

**Why entry:** Hybrid entry uses close 324 and ATR14 36.6: buy zone 310–332. Entry is valid only if price can trade/hold around 332 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 322 is placed below support structure (324 / 324). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 420 (8.80R), TP2 426 (9.40R), TP3 432 (10.00R). Targets are ATR/structure capped for hold_days=10. ATR14=36.6, resistance_5/10/20/60=420/492/540/630. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** score 0.299 below policy min_score 0.30

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Generic strategy rule.

---

## BULL — scalping_continual_defensive — NO_TRADE

**Score:** 0.706 vs policy min 0.05 · **Close:** 402 · **ATR14:** 50.4 · **Volume ratio 20D:** 0.72 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 384–414, entry trigger **414**, stop **380**, risk 34 points (8.21%).

**Targets:** TP1 **448** (1.00R), TP2 **472** (1.71R), TP3 **540** (3.71R). Recommended base-case RR: **1.71R**.

**Why entry:** Hybrid entry uses close 402 and ATR14 50.4: buy zone 384–414. Entry is valid only if price can trade/hold around 414 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 380 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 448 (1.00R), TP2 472 (1.71R), TP3 540 (3.71R). Targets are ATR/structure capped for hold_days=1. ATR14=50.4, resistance_5/10/20/60=545/565/610/610. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.21% exceeds max strategy risk 8.00%; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## TRUE — momentum_5d_continual_defensive — NO_TRADE

**Score:** 0.566 vs policy min 0.30 · **Close:** 120 · **ATR14:** 14.8 · **Volume ratio 20D:** 0.50 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 114–123, entry trigger **123**, stop **113**, risk 10 points (8.13%).

**Targets:** TP1 **133** (1.00R), TP2 **170** (4.70R), TP3 **173** (5.00R). Recommended base-case RR: **4.70R**.

**Why entry:** Hybrid entry uses close 120 and ATR14 14.8: buy zone 114–123. Entry is valid only if price can trade/hold around 123 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 113 is placed below support structure (114 / 114). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 133 (1.00R), TP2 170 (4.70R), TP3 173 (5.00R). Targets are ATR/structure capped for hold_days=3. ATR14=14.8, resistance_5/10/20/60=173/173/220/290. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.13% exceeds max strategy risk 8.00%; TP1 reward/risk 1.00R is below strategy minimum 1.25R; volume ratio 0.50 below required 0.60; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## TRUE — swing_continual_defensive — NO_TRADE

**Score:** 0.566 vs policy min 0.30 · **Close:** 120 · **ATR14:** 14.8 · **Volume ratio 20D:** 0.50 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 114–123, entry trigger **123**, stop **113**, risk 10 points (8.13%).

**Targets:** TP1 **133** (1.00R), TP2 **140** (1.70R), TP3 **147** (2.40R). Recommended base-case RR: **1.70R**.

**Why entry:** Hybrid entry uses close 120 and ATR14 14.8: buy zone 114–123. Entry is valid only if price can trade/hold around 123 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 113 is placed below support structure (114 / 114). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 133 (1.00R), TP2 140 (1.70R), TP3 147 (2.40R). Targets are ATR/structure capped for hold_days=1. ATR14=14.8, resistance_5/10/20/60=173/173/220/290. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.13% exceeds max strategy risk 8.00%; TP1 reward/risk 1.00R is below strategy minimum 1.25R; volume ratio 0.50 below required 0.60; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## DSSA — momentum_20d_continual_research — NO_TRADE

**Score:** 0.470 vs policy min 0.30 · **Close:** 750 · **ATR14:** 245.4 · **Volume ratio 20D:** 5.23 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 660–800, entry trigger **800**, stop **745**, risk 55 points (6.88%).

**Targets:** TP1 **925** (2.27R), TP2 **1,660** (15.64R), TP3 **1,690** (16.18R). Recommended base-case RR: **15.64R**.

**Why entry:** Hybrid entry uses close 750 and ATR14 245.4: buy zone 660–800. Entry is valid only if price can trade/hold around 800 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 745 is placed below support structure (750 / 750). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 925 (2.27R), TP2 1,660 (15.64R), TP3 1,690 (16.18R). Targets are ATR/structure capped for hold_days=10. ATR14=245.4, resistance_5/10/20/60=1,660/2,110/3,500/98,000. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** strategy policy has execution_enabled=false

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## MBMA — momentum_20d_continual_research — NO_TRADE

**Score:** 0.424 vs policy min 0.30 · **Close:** 476 · **ATR14:** 47.6 · **Volume ratio 20D:** 3.70 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 458–486, entry trigger **486**, stop **462**, risk 24 points (4.94%).

**Targets:** TP1 **510** (1.00R), TP2 **680** (8.08R), TP3 **695** (8.71R). Recommended base-case RR: **8.08R**.

**Why entry:** Hybrid entry uses close 476 and ATR14 47.6: buy zone 458–486. Entry is valid only if price can trade/hold around 486 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 462 is placed below support structure (464 / 464). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 510 (1.00R), TP2 680 (8.08R), TP3 695 (8.71R). Targets are ATR/structure capped for hold_days=10. ATR14=47.6, resistance_5/10/20/60=680/710/775/945. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** strategy policy has execution_enabled=false; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## NSSS — momentum_20d_continual_research — NO_TRADE

**Score:** 0.388 vs policy min 0.30 · **Close:** 605 · **ATR14:** 80.0 · **Volume ratio 20D:** 0.66 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 575–625, entry trigger **625**, stop **590**, risk 35 points (5.60%).

**Targets:** TP1 **850** (6.43R), TP2 **870** (7.00R), TP3 **890** (7.57R). Recommended base-case RR: **7.00R**.

**Why entry:** Hybrid entry uses close 605 and ATR14 80.0: buy zone 575–625. Entry is valid only if price can trade/hold around 625 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 590 is placed below support structure (595 / 595). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 850 (6.43R), TP2 870 (7.00R), TP3 890 (7.57R). Targets are ATR/structure capped for hold_days=10. ATR14=80.0, resistance_5/10/20/60=850/935/1,060/1,300. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** strategy policy has execution_enabled=false

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## UNSP — momentum_20d_continual_research — NO_TRADE

**Score:** 0.367 vs policy min 0.30 · **Close:** 276 · **ATR14:** 24.1 · **Volume ratio 20D:** 2.03 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 266–282, entry trigger **282**, stop **258**, risk 24 points (8.51%).

**Targets:** TP1 **360** (3.25R), TP2 **372** (3.75R), TP3 **384** (4.25R). Recommended base-case RR: **3.75R**.

**Why entry:** Hybrid entry uses close 276 and ATR14 24.1: buy zone 266–282. Entry is valid only if price can trade/hold around 282 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 258 is placed below support structure (260 / 260). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 360 (3.25R), TP2 372 (3.75R), TP3 384 (4.25R). Targets are ATR/structure capped for hold_days=10. ATR14=24.1, resistance_5/10/20/60=372/400/450/450. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** strategy policy has execution_enabled=false; entry-to-stop risk 8.51% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## PBSA — momentum_20d_continual_research — NO_TRADE

**Score:** 0.342 vs policy min 0.30 · **Close:** 780 · **ATR14:** 72.1 · **Volume ratio 20D:** 1.09 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 750–795, entry trigger **795**, stop **730**, risk 65 points (8.18%).

**Targets:** TP1 **1,015** (3.38R), TP2 **1,050** (3.92R), TP3 **1,085** (4.46R). Recommended base-case RR: **3.92R**.

**Why entry:** Hybrid entry uses close 780 and ATR14 72.1: buy zone 750–795. Entry is valid only if price can trade/hold around 795 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 730 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,015 (3.38R), TP2 1,050 (3.92R), TP3 1,085 (4.46R). Targets are ATR/structure capped for hold_days=10. ATR14=72.1, resistance_5/10/20/60=1,015/1,240/1,270/1,600. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** strategy policy has execution_enabled=false; entry-to-stop risk 8.18% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## PBSA — position_continual — NO_TRADE

**Score:** 0.308 vs policy min 0.30 · **Close:** 780 · **ATR14:** 72.1 · **Volume ratio 20D:** 1.09 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 750–795, entry trigger **795**, stop **730**, risk 65 points (8.18%).

**Targets:** TP1 **1,015** (3.38R), TP2 **1,050** (3.92R), TP3 **1,085** (4.46R). Recommended base-case RR: **3.92R**.

**Why entry:** Hybrid entry uses close 780 and ATR14 72.1: buy zone 750–795. Entry is valid only if price can trade/hold around 795 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 730 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,015 (3.38R), TP2 1,050 (3.92R), TP3 1,085 (4.46R). Targets are ATR/structure capped for hold_days=10. ATR14=72.1, resistance_5/10/20/60=1,015/1,240/1,270/1,600. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.18% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## UNSP — position_continual — NO_TRADE

**Score:** 0.299 vs policy min 0.30 · **Close:** 276 · **ATR14:** 24.1 · **Volume ratio 20D:** 2.03 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 266–282, entry trigger **282**, stop **258**, risk 24 points (8.51%).

**Targets:** TP1 **360** (3.25R), TP2 **372** (3.75R), TP3 **384** (4.25R). Recommended base-case RR: **3.75R**.

**Why entry:** Hybrid entry uses close 276 and ATR14 24.1: buy zone 266–282. Entry is valid only if price can trade/hold around 282 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 258 is placed below support structure (260 / 260). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 360 (3.25R), TP2 372 (3.75R), TP3 384 (4.25R). Targets are ATR/structure capped for hold_days=10. ATR14=24.1, resistance_5/10/20/60=372/400/450/450. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.51% exceeds max strategy risk 8.00%; score 0.299 below policy min_score 0.30

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Generic strategy rule.

---
