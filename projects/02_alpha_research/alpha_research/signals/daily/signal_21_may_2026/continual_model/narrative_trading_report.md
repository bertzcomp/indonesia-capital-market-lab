# Narrative Trading Intelligence Report

## Market Context

Signal universe is built from the latest available market panel dated **2026-05-20**. macro risk score: -1.660. 5-day market return proxy: -6.13%. 20-day market volatility proxy: 0.012. FX pressure: 0.00%. Brent move: -5.63%. coal proxy move: -5.59%. Regime label: **risk_off**.

## Operating Principle

This report is not a simple BUY/SELL list. Each signal is interpreted as a conditional trading thesis. Execution is valid only when price structure, liquidity, momentum, and behavioural confirmation remain aligned. If those conditions fail, no-trade or early exit is the correct risk decision.

## Signal Thesis and Execution Plan

### 1. MBMA — momentum_5d_continual_defensive

**Confidence:** Medium  
**Risk Grade:** Controlled  
**Primary Score:** `score_momentum_5d` = 0.507310  
**Risk Flags:** OK  

**Trade thesis.** MBMA is selected by the **momentum_5d_continual_defensive** setup (cross-sectional momentum continuation). The primary model evidence is `score_momentum_5d` at 0.507. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -25.20%; 20-day return is -36.99%; 20-day volatility is 4.83%; volume expansion is visible with volume ratio 2.73. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.002; rank-1 buyer is CC with streak 1; rank-1 seller is YU; buyer dominance is 22.21%; daily share of the dominant buyer is 13.99%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Enter only if price holds above prior close or reclaims intraday VWAP/support. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 432 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 2. CUAN — momentum_5d_continual_defensive

**Confidence:** Watchlist only  
**Risk Grade:** Medium  
**Primary Score:** `score_momentum_5d` = 0.468298  
**Risk Flags:** OK  

**Trade thesis.** CUAN is selected by the **momentum_5d_continual_defensive** setup (cross-sectional momentum continuation). The primary model evidence is `score_momentum_5d` at 0.468. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -54.62%; 20-day return is -58.74%; 20-day volatility is 8.86%; volume ratio is neutral at 1.45. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.002; rank-1 buyer is AK with streak 4; rank-1 seller is KZ; buyer dominance is 26.70%; daily share of the dominant buyer is 4.78%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Enter only if price holds above prior close or reclaims intraday VWAP/support. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 543 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 3. DSSA — momentum_5d_continual_defensive

**Confidence:** Watchlist only  
**Risk Grade:** Controlled  
**Primary Score:** `score_momentum_5d` = 0.441456  
**Risk Flags:** OK  

**Trade thesis.** DSSA is selected by the **momentum_5d_continual_defensive** setup (cross-sectional momentum continuation). The primary model evidence is `score_momentum_5d` at 0.441. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -52.19%; 20-day return is -77.53%; 20-day volatility is 7.85%; volume expansion is visible with volume ratio 4.45. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.000; rank-1 buyer is NI with streak 1; rank-1 seller is ZP; buyer dominance is 31.11%; daily share of the dominant buyer is 1.98%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Enter only if price holds above prior close or reclaims intraday VWAP/support. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 653 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 4. SSMS — momentum_5d_continual_defensive

**Confidence:** Watchlist only  
**Risk Grade:** Controlled  
**Primary Score:** `score_momentum_5d` = 0.436250  
**Risk Flags:** OK  

**Trade thesis.** SSMS is selected by the **momentum_5d_continual_defensive** setup (cross-sectional momentum continuation). The primary model evidence is `score_momentum_5d` at 0.436. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -33.93%; 20-day return is -29.92%; 20-day volatility is 4.92%; volume ratio is neutral at 1.21. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.001; rank-1 buyer is CC with streak 1; rank-1 seller is KZ; buyer dominance is 20.61%; daily share of the dominant buyer is 13.99%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Enter only if price holds above prior close or reclaims intraday VWAP/support. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 868 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 5. UNSP — momentum_5d_continual_defensive

**Confidence:** Watchlist only  
**Risk Grade:** Controlled  
**Primary Score:** `score_momentum_5d` = 0.433220  
**Risk Flags:** OK  

**Trade thesis.** UNSP is selected by the **momentum_5d_continual_defensive** setup (cross-sectional momentum continuation). The primary model evidence is `score_momentum_5d` at 0.433. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -32.43%; 20-day return is -37.50%; 20-day volatility is 5.62%; volume ratio is neutral at 1.31. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.000; rank-1 buyer is CP with streak 1; rank-1 seller is CP; buyer dominance is 44.11%; daily share of the dominant buyer is 1.86%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Enter only if price holds above prior close or reclaims intraday VWAP/support. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 232 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 6. DEWA — momentum_10d_continual_aggressive

**Confidence:** Medium  
**Risk Grade:** Controlled  
**Primary Score:** `score_momentum_10d` = 0.548395  
**Risk Flags:** OK  

**Trade thesis.** DEWA is selected by the **momentum_10d_continual_aggressive** setup (cross-sectional momentum continuation). The primary model evidence is `score_momentum_10d` at 0.548. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -25.88%; 20-day return is -28.00%; 20-day volatility is 4.94%; volume expansion is visible with volume ratio 2.19. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.009; rank-1 buyer is AK with streak 1; rank-1 seller is XL; buyer dominance is 18.15%; daily share of the dominant buyer is 4.78%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Enter only if price holds above prior close or reclaims intraday VWAP/support. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 355 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 7. PSAB — momentum_10d_continual_aggressive

**Confidence:** Medium  
**Risk Grade:** Controlled  
**Primary Score:** `score_momentum_10d` = 0.543992  
**Risk Flags:** OK  

**Trade thesis.** PSAB is selected by the **momentum_10d_continual_aggressive** setup (cross-sectional momentum continuation). The primary model evidence is `score_momentum_10d` at 0.544. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -23.53%; 20-day return is -24.27%; 20-day volatility is 5.58%; volume ratio is neutral at 1.17. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.002; rank-1 buyer is CC with streak 1; rank-1 seller is AK; buyer dominance is 14.92%; daily share of the dominant buyer is 13.99%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Enter only if price holds above prior close or reclaims intraday VWAP/support. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 363 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 8. NICL — momentum_10d_continual_aggressive

**Confidence:** Medium  
**Risk Grade:** Controlled  
**Primary Score:** `score_momentum_10d` = 0.538838  
**Risk Flags:** OK  

**Trade thesis.** NICL is selected by the **momentum_10d_continual_aggressive** setup (cross-sectional momentum continuation). The primary model evidence is `score_momentum_10d` at 0.539. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -31.76%; 20-day return is -38.30%; 20-day volatility is 4.59%; volume participation is still thin with volume ratio 0.59. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.002; rank-1 buyer is PD with streak 1; rank-1 seller is YP; buyer dominance is 16.10%; daily share of the dominant buyer is 2.45%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Enter only if price holds above prior close or reclaims intraday VWAP/support. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 547 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 9. NSSS — scalping_continual_defensive

**Confidence:** High  
**Risk Grade:** Controlled  
**Primary Score:** `score_scalp` = 0.708095  
**Risk Flags:** OK  

**Trade thesis.** NSSS is selected by the **scalping_continual_defensive** setup (short-time momentum execution). The primary model evidence is `score_scalp` at 0.708. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -29.81%; 20-day return is -27.10%; 20-day volatility is 5.87%; volume participation is still thin with volume ratio 0.41. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.000; rank-1 buyer is IF with streak 43; rank-1 seller is IF; buyer dominance is 31.29%; daily share of the dominant buyer is 0.70%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Needs intraday confirmation; do not enter if opening liquidity fades. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 524 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 10. WBSA — scalping_continual_defensive

**Confidence:** High  
**Risk Grade:** Medium  
**Primary Score:** `score_scalp` = 0.703204  
**Risk Flags:** OK  

**Trade thesis.** WBSA is selected by the **scalping_continual_defensive** setup (short-time momentum execution). The primary model evidence is `score_scalp` at 0.703. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -46.23%; 20-day return is 178.37%; 20-day volatility is 15.86%; volume expansion is visible with volume ratio 4.78. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.005; rank-1 buyer is MG with streak 1; rank-1 seller is XL; buyer dominance is 27.30%; daily share of the dominant buyer is 1.63%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Needs intraday confirmation; do not enter if opening liquidity fades. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 722 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 11. SIMP — position_continual

**Confidence:** Watchlist only  
**Risk Grade:** Controlled  
**Primary Score:** `score_position` = 0.321276  
**Risk Flags:** OK  

**Trade thesis.** SIMP is selected by the **position_continual** setup (position continuation / structural setup). The primary model evidence is `score_position` at 0.321. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -23.81%; 20-day return is -28.66%; 20-day volatility is 5.18%; volume ratio is neutral at 0.82. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.003; rank-1 buyer is AK with streak 1; rank-1 seller is YJ; buyer dominance is 20.99%; daily share of the dominant buyer is 4.78%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer close confirmation and stable liquidity rather than intraday spike. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 524 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 12. ASPR — ara_candidate_continual

**Confidence:** Medium, risk-adjusted  
**Risk Grade:** Medium-high  
**Primary Score:** `score_ara` = 0.855240  
**Risk Flags:** DOMINANT_RANK1_BUYER  

**Trade thesis.** ASPR is selected by the **ara_candidate_continual** setup (tactical event / watchlist). The primary model evidence is `score_ara` at 0.855. The price/volume context indicates that price is trading above the 20-day mean, suggesting structure is still constructive relative to its recent base; 5-day return is 3.66%; 20-day return is 50.00%; 20-day volatility is 11.02%; volume expansion is visible with volume ratio 3.61. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.003; rank-1 buyer is XL with streak 4; rank-1 seller is XL; buyer dominance is 31.45%; daily share of the dominant buyer is 39.04%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Only after strong opening confirmation; avoid chasing failed gap-up moves. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; excessive dependence on one broker continuing to dominate without broader participation; as a volatility-adjusted reference, thesis quality weakens materially around 364 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 13. BUVA — momentum_5d_continual_defensive

**Confidence:** Low-to-medium  
**Risk Grade:** Medium  
**Primary Score:** `score_momentum_5d` = 0.518505  
**Risk Flags:** DOMINANT_RANK1_BUYER  

**Trade thesis.** BUVA is selected by the **momentum_5d_continual_defensive** setup (cross-sectional momentum continuation). The primary model evidence is `score_momentum_5d` at 0.519. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -28.19%; 20-day return is -32.08%; 20-day volatility is 5.39%; volume ratio is neutral at 1.12. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.003; rank-1 buyer is XL with streak 17; rank-1 seller is XL; buyer dominance is 26.83%; daily share of the dominant buyer is 39.04%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Enter only if price holds above prior close or reclaims intraday VWAP/support. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; excessive dependence on one broker continuing to dominate without broader participation; as a volatility-adjusted reference, thesis quality weakens materially around 760 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 14. KOKA — momentum_5d_continual_defensive

**Confidence:** Low-to-medium  
**Risk Grade:** Medium  
**Primary Score:** `score_momentum_5d` = 0.434883  
**Risk Flags:** DOMINANT_RANK1_BUYER  

**Trade thesis.** KOKA is selected by the **momentum_5d_continual_defensive** setup (cross-sectional momentum continuation). The primary model evidence is `score_momentum_5d` at 0.435. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -30.86%; 20-day return is -34.95%; 20-day volatility is 4.69%; volume ratio is neutral at 0.96. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.000; rank-1 buyer is XL with streak 2; rank-1 seller is XL; buyer dominance is 15.95%; daily share of the dominant buyer is 39.04%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Enter only if price holds above prior close or reclaims intraday VWAP/support. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; excessive dependence on one broker continuing to dominate without broader participation; as a volatility-adjusted reference, thesis quality weakens materially around 114 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 15. BIPI — momentum_10d_continual_aggressive

**Confidence:** Low-to-medium  
**Risk Grade:** Medium  
**Primary Score:** `score_momentum_10d` = 0.540437  
**Risk Flags:** DOMINANT_RANK1_BUYER  

**Trade thesis.** BIPI is selected by the **momentum_10d_continual_aggressive** setup (cross-sectional momentum continuation). The primary model evidence is `score_momentum_10d` at 0.540. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -17.89%; 20-day return is -22.31%; 20-day volatility is 5.42%; volume ratio is neutral at 1.42. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.013; rank-1 buyer is XL with streak 1; rank-1 seller is XL; buyer dominance is 16.75%; daily share of the dominant buyer is 39.04%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Enter only if price holds above prior close or reclaims intraday VWAP/support. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; excessive dependence on one broker continuing to dominate without broader participation; as a volatility-adjusted reference, thesis quality weakens materially around 188 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 16. CDIA — momentum_20d_continual_research

**Confidence:** Watchlist only  
**Risk Grade:** Controlled  
**Primary Score:** `score_momentum_20d` = 0.441873  
**Risk Flags:** OK  

**Trade thesis.** CDIA is selected by the **momentum_20d_continual_research** setup (cross-sectional momentum continuation). The primary model evidence is `score_momentum_20d` at 0.442. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -33.61%; 20-day return is -29.78%; 20-day volatility is 7.32%; volume ratio is neutral at 0.74. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.002; rank-1 buyer is CC with streak 1; rank-1 seller is LG; buyer dominance is 24.84%; daily share of the dominant buyer is 13.99%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Enter only if price holds above prior close or reclaims intraday VWAP/support. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 727 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

## Portfolio-Level Notes

Avoid forcing trades simply because a ticker appears in the report. Prioritize candidates whose thesis remains valid after the market opens, avoid concentration in the same dominant broker behaviour, and reduce exposure when multiple names depend on the same liquidity pattern. If market breadth weakens or volatility becomes abnormal, scale down position sizing or move signals to watchlist-only.