# Narrative Trading Intelligence Report

## Market Context

Signal universe is built from the latest available market panel dated **2026-05-26**. macro risk score: -1.307. 5-day market return proxy: 0.59%. 20-day market volatility proxy: 0.014. FX pressure: 0.00%. Brent move: -3.82%. coal proxy move: -3.80%. Regime label: **risk_off**.

## Operating Principle

This report is not a simple BUY/SELL list. Each signal is interpreted as a conditional trading thesis. Execution is valid only when price structure, liquidity, momentum, and behavioural confirmation remain aligned. If those conditions fail, no-trade or early exit is the correct risk decision.

## Signal Thesis and Execution Plan

### 1. PGEO — scalping_rank_hgb

**Confidence:** Medium-high  
**Risk Grade:** Controlled  
**Primary Score:** `score_scalp__multi_strategy_time__rank_hgb__scalp` = 0.622514  
**Risk Flags:** OK  

**Trade thesis.** PGEO is selected by the **scalping_rank_hgb** setup (short-time momentum execution). The primary model evidence is `score_scalp__multi_strategy_time__rank_hgb__scalp` at 0.623. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -9.09%; 20-day return is -13.46%; 20-day volatility is 2.37%; volume ratio is neutral at 0.96. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.015; rank-1 buyer is ZP with streak 1; rank-1 seller is SQ; buyer dominance is 29.16%; daily share of the dominant buyer is 1.39%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Needs intraday confirmation; do not enter if opening liquidity fades. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 873 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 2. TRIN — swing_hgb_defensive

**Confidence:** Medium-high  
**Risk Grade:** Controlled  
**Primary Score:** `score_swing__multi_strategy_time__hgb__swing` = 0.667166  
**Risk Flags:** OK  

**Trade thesis.** TRIN is selected by the **swing_hgb_defensive** setup (defensive swing continuation). The primary model evidence is `score_swing__multi_strategy_time__hgb__swing` at 0.667. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -24.87%; 20-day return is -46.00%; 20-day volatility is 3.86%; volume ratio is neutral at 0.73. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.000; rank-1 buyer is CC with streak 1; rank-1 seller is CC; buyer dominance is 36.55%; daily share of the dominant buyer is 8.92%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer confirmation above prior close or controlled pullback/retest. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 411 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 3. BFIN — swing_hgb_defensive

**Confidence:** Medium-high  
**Risk Grade:** Controlled  
**Primary Score:** `score_swing__multi_strategy_time__hgb__swing` = 0.666434  
**Risk Flags:** OK  

**Trade thesis.** BFIN is selected by the **swing_hgb_defensive** setup (defensive swing continuation). The primary model evidence is `score_swing__multi_strategy_time__hgb__swing` at 0.666. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -9.62%; 20-day return is -18.97%; 20-day volatility is 3.45%; volume ratio is neutral at 0.99. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.000; rank-1 buyer is BB with streak 1; rank-1 seller is AZ; buyer dominance is 29.56%; daily share of the dominant buyer is 0.23%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer confirmation above prior close or controlled pullback/retest. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 675 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 4. SSMS — swing_hgb_defensive

**Confidence:** Medium-high  
**Risk Grade:** Controlled  
**Primary Score:** `score_swing__multi_strategy_time__hgb__swing` = 0.665208  
**Risk Flags:** OK  

**Trade thesis.** SSMS is selected by the **swing_hgb_defensive** setup (defensive swing continuation). The primary model evidence is `score_swing__multi_strategy_time__hgb__swing` at 0.665. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -26.13%; 20-day return is -44.11%; 20-day volatility is 5.28%; volume expansion is visible with volume ratio 1.54. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.004; rank-1 buyer is CC with streak 3; rank-1 seller is BB; buyer dominance is 21.97%; daily share of the dominant buyer is 8.92%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer confirmation above prior close or controlled pullback/retest. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 687 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 5. OMED — swing_hgb_defensive

**Confidence:** Medium-high  
**Risk Grade:** Controlled  
**Primary Score:** `score_swing__multi_strategy_time__hgb__swing` = 0.660832  
**Risk Flags:** OK  

**Trade thesis.** OMED is selected by the **swing_hgb_defensive** setup (defensive swing continuation). The primary model evidence is `score_swing__multi_strategy_time__hgb__swing` at 0.661. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -16.53%; 20-day return is -32.67%; 20-day volatility is 3.75%; volume participation is still thin with volume ratio 0.49. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.001; rank-1 buyer is CC with streak 1; rank-1 seller is AZ; buyer dominance is 59.61%; daily share of the dominant buyer is 8.92%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer confirmation above prior close or controlled pullback/retest. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 193 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 6. KIJA — swing_hgb_defensive

**Confidence:** Medium-high  
**Risk Grade:** Controlled  
**Primary Score:** `score_swing__multi_strategy_time__hgb__swing` = 0.655272  
**Risk Flags:** OK  

**Trade thesis.** KIJA is selected by the **swing_hgb_defensive** setup (defensive swing continuation). The primary model evidence is `score_swing__multi_strategy_time__hgb__swing` at 0.655. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -25.15%; 20-day return is -35.45%; 20-day volatility is 4.45%; volume participation is still thin with volume ratio 0.42. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.004; rank-1 buyer is YP with streak 1; rank-1 seller is XL; buyer dominance is 18.09%; daily share of the dominant buyer is 4.63%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer confirmation above prior close or controlled pullback/retest. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 115 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 7. HRUM — swing_hgb_defensive

**Confidence:** Medium-high  
**Risk Grade:** Controlled  
**Primary Score:** `score_swing__multi_strategy_time__hgb__swing` = 0.652794  
**Risk Flags:** OK  

**Trade thesis.** HRUM is selected by the **swing_hgb_defensive** setup (defensive swing continuation). The primary model evidence is `score_swing__multi_strategy_time__hgb__swing` at 0.653. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is 2.58%; 20-day return is -23.56%; 20-day volatility is 4.21%; volume participation is still thin with volume ratio 0.65. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.006; rank-1 buyer is CC with streak 6; rank-1 seller is CC; buyer dominance is 27.42%; daily share of the dominant buyer is 8.92%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer confirmation above prior close or controlled pullback/retest. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 753 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 8. BRMS — swing_hgb_defensive

**Confidence:** Medium-high  
**Risk Grade:** Controlled  
**Primary Score:** `score_swing__multi_strategy_time__hgb__swing` = 0.648976  
**Risk Flags:** OK  

**Trade thesis.** BRMS is selected by the **swing_hgb_defensive** setup (defensive swing continuation). The primary model evidence is `score_swing__multi_strategy_time__hgb__swing` at 0.649. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -9.70%; 20-day return is -28.82%; 20-day volatility is 5.50%; volume participation is still thin with volume ratio 0.58. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.009; rank-1 buyer is BK with streak 2; rank-1 seller is CC; buyer dominance is 27.26%; daily share of the dominant buyer is 0.93%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer confirmation above prior close or controlled pullback/retest. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 563 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 9. FOLK — swing_hgb_defensive

**Confidence:** Medium-high  
**Risk Grade:** Controlled  
**Primary Score:** `score_swing__multi_strategy_time__hgb__swing` = 0.648169  
**Risk Flags:** OK  

**Trade thesis.** FOLK is selected by the **swing_hgb_defensive** setup (defensive swing continuation). The primary model evidence is `score_swing__multi_strategy_time__hgb__swing` at 0.648. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -12.70%; 20-day return is -39.23%; 20-day volatility is 5.98%; volume ratio is neutral at 0.86. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.000; rank-1 buyer is CP with streak 1; rank-1 seller is AT; buyer dominance is 20.44%; daily share of the dominant buyer is 3.01%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer confirmation above prior close or controlled pullback/retest. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 204 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 10. NICL — swing_hgb_defensive

**Confidence:** Medium-high  
**Risk Grade:** Controlled  
**Primary Score:** `score_swing__multi_strategy_time__hgb__swing` = 0.645808  
**Risk Flags:** OK  

**Trade thesis.** NICL is selected by the **swing_hgb_defensive** setup (defensive swing continuation). The primary model evidence is `score_swing__multi_strategy_time__hgb__swing` at 0.646. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -14.84%; 20-day return is -45.50%; 20-day volatility is 4.31%; volume participation is still thin with volume ratio 0.68. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.002; rank-1 buyer is PI with streak 1; rank-1 seller is AI; buyer dominance is 23.56%; daily share of the dominant buyer is 0.12%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer confirmation above prior close or controlled pullback/retest. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 516 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 11. SGER — swing_hgb_defensive

**Confidence:** Medium-high  
**Risk Grade:** Controlled  
**Primary Score:** `score_swing__multi_strategy_time__hgb__swing` = 0.644197  
**Risk Flags:** OK  

**Trade thesis.** SGER is selected by the **swing_hgb_defensive** setup (defensive swing continuation). The primary model evidence is `score_swing__multi_strategy_time__hgb__swing` at 0.644. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -9.15%; 20-day return is -28.37%; 20-day volatility is 5.34%; volume ratio is neutral at 1.13. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.000; rank-1 buyer is TP with streak 1; rank-1 seller is YU; buyer dominance is 84.99%; daily share of the dominant buyer is 0.58%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer confirmation above prior close or controlled pullback/retest. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 278 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 12. STAA — swing_hgb_defensive

**Confidence:** Medium, risk-adjusted  
**Risk Grade:** Medium  
**Primary Score:** `score_swing__multi_strategy_time__hgb__swing` = 0.670177  
**Risk Flags:** DOMINANT_RANK1_BUYER  

**Trade thesis.** STAA is selected by the **swing_hgb_defensive** setup (defensive swing continuation). The primary model evidence is `score_swing__multi_strategy_time__hgb__swing` at 0.670. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -13.04%; 20-day return is -21.57%; 20-day volatility is 3.44%; volume ratio is neutral at 1.05. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.004; rank-1 buyer is XL with streak 2; rank-1 seller is KK; buyer dominance is 13.19%; daily share of the dominant buyer is 41.02%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer confirmation above prior close or controlled pullback/retest. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; excessive dependence on one broker continuing to dominate without broader participation; as a volatility-adjusted reference, thesis quality weakens materially around 957 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 13. RMKO — swing_hgb_defensive

**Confidence:** Medium, risk-adjusted  
**Risk Grade:** Medium  
**Primary Score:** `score_swing__multi_strategy_time__hgb__swing` = 0.650514  
**Risk Flags:** DOMINANT_RANK1_BUYER  

**Trade thesis.** RMKO is selected by the **swing_hgb_defensive** setup (defensive swing continuation). The primary model evidence is `score_swing__multi_strategy_time__hgb__swing` at 0.651. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -20.87%; 20-day return is -44.27%; 20-day volatility is 4.68%; volume ratio is neutral at 1.07. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.000; rank-1 buyer is XL with streak 2; rank-1 seller is XL; buyer dominance is 42.74%; daily share of the dominant buyer is 41.02%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer confirmation above prior close or controlled pullback/retest. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; excessive dependence on one broker continuing to dominate without broader participation; as a volatility-adjusted reference, thesis quality weakens materially around 307 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 14. GTSI — swing_hgb_defensive

**Confidence:** Low-to-medium  
**Risk Grade:** Medium  
**Primary Score:** `score_swing__multi_strategy_time__hgb__swing` = 0.648148  
**Risk Flags:** DOMINANT_RANK1_BUYER  

**Trade thesis.** GTSI is selected by the **swing_hgb_defensive** setup (defensive swing continuation). The primary model evidence is `score_swing__multi_strategy_time__hgb__swing` at 0.648. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -14.59%; 20-day return is -40.15%; 20-day volatility is 5.50%; volume participation is still thin with volume ratio 0.53. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.000; rank-1 buyer is XL with streak 30; rank-1 seller is CC; buyer dominance is 33.77%; daily share of the dominant buyer is 41.02%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer confirmation above prior close or controlled pullback/retest. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; excessive dependence on one broker continuing to dominate without broader participation; as a volatility-adjusted reference, thesis quality weakens materially around 147 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 15. FORE — swing_hgb_defensive

**Confidence:** Low-to-medium  
**Risk Grade:** Medium  
**Primary Score:** `score_swing__multi_strategy_time__hgb__swing` = 0.647938  
**Risk Flags:** DOMINANT_RANK1_BUYER  

**Trade thesis.** FORE is selected by the **swing_hgb_defensive** setup (defensive swing continuation). The primary model evidence is `score_swing__multi_strategy_time__hgb__swing` at 0.648. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -25.74%; 20-day return is -21.05%; 20-day volatility is 5.56%; volume ratio is neutral at 1.19. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.001; rank-1 buyer is XL with streak 3; rank-1 seller is XL; buyer dominance is 25.80%; daily share of the dominant buyer is 41.02%; BDM confirmation is present, improving behavioural confidence.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer confirmation above prior close or controlled pullback/retest. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; excessive dependence on one broker continuing to dominate without broader participation; as a volatility-adjusted reference, thesis quality weakens materially around 698 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 16. ESTI — swing_hgb_defensive

**Confidence:** Low-to-medium  
**Risk Grade:** Medium  
**Primary Score:** `score_swing__multi_strategy_time__hgb__swing` = 0.644383  
**Risk Flags:** DOMINANT_RANK1_BUYER  

**Trade thesis.** ESTI is selected by the **swing_hgb_defensive** setup (defensive swing continuation). The primary model evidence is `score_swing__multi_strategy_time__hgb__swing` at 0.644. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -9.86%; 20-day return is -29.28%; 20-day volatility is 3.66%; volume ratio is neutral at 1.45. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.000; rank-1 buyer is XL with streak 2; rank-1 seller is XL; buyer dominance is 37.63%; daily share of the dominant buyer is 41.02%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer confirmation above prior close or controlled pullback/retest. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; excessive dependence on one broker continuing to dominate without broader participation; as a volatility-adjusted reference, thesis quality weakens materially around 122 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 17. MGNA — ara_candidate

**Confidence:** Low-to-medium  
**Risk Grade:** High  
**Primary Score:** `score_ara` = 0.281224  
**Risk Flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD  

**Trade thesis.** MGNA is selected by the **ara_candidate** setup (tactical event / watchlist). The primary model evidence is `score_ara` at 0.281. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is 3.51%; 20-day return is -36.56%; 20-day volatility is 9.92%; volume expansion is visible with volume ratio 10.71. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.000; rank-1 buyer is XL with streak 3; rank-1 seller is XL; buyer dominance is 38.27%; daily share of the dominant buyer is 41.02%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Only after strong opening confirmation; avoid chasing failed gap-up moves. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; excessive dependence on one broker continuing to dominate without broader participation; as a volatility-adjusted reference, thesis quality weakens materially around 109 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 18. BBHI — market_maker_silent_accum_defensive

**Confidence:** Low-to-medium  
**Risk Grade:** Medium  
**Primary Score:** `score_mm_silent` = 0.441203  
**Risk Flags:** BELOW_EXECUTION_THRESHOLD  

**Trade thesis.** BBHI is selected by the **market_maker_silent_accum_defensive** setup (silent accumulation / liquidity behaviour). The primary model evidence is `score_mm_silent` at 0.441. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -0.53%; 20-day return is -27.80%; 20-day volatility is 7.17%; volume expansion is visible with volume ratio 4.45. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.001; rank-1 buyer is CD with streak 3; rank-1 seller is CD; buyer dominance is 83.86%; daily share of the dominant buyer is 0.35%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer retest or stable bid support after accumulation confirmation. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 860 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 19. MSJA — market_maker_silent_accum_defensive

**Confidence:** Low-to-medium  
**Risk Grade:** Medium  
**Primary Score:** `score_mm_silent` = 0.427112  
**Risk Flags:** BELOW_EXECUTION_THRESHOLD  

**Trade thesis.** MSJA is selected by the **market_maker_silent_accum_defensive** setup (silent accumulation / liquidity behaviour). The primary model evidence is `score_mm_silent` at 0.427. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is 0.49%; 20-day return is -20.38%; 20-day volatility is 5.16%; volume participation is still thin with volume ratio 0.68. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.000; rank-1 buyer is AZ with streak 8; rank-1 seller is AZ; buyer dominance is 49.43%; daily share of the dominant buyer is 0.93%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer retest or stable bid support after accumulation confirmation. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 387 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 20. FUJI — market_maker_silent_accum_defensive

**Confidence:** Low-to-medium  
**Risk Grade:** Medium  
**Primary Score:** `score_mm_silent` = 0.426221  
**Risk Flags:** BELOW_EXECUTION_THRESHOLD  

**Trade thesis.** FUJI is selected by the **market_maker_silent_accum_defensive** setup (silent accumulation / liquidity behaviour). The primary model evidence is `score_mm_silent` at 0.426. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -3.42%; 20-day return is -25.79%; 20-day volatility is 3.30%; volume expansion is visible with volume ratio 1.76. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.000; rank-1 buyer is CP with streak 2; rank-1 seller is CP; buyer dominance is 99.45%; daily share of the dominant buyer is 3.01%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer retest or stable bid support after accumulation confirmation. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 270 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 21. PBSA — market_maker_silent_accum_defensive

**Confidence:** Low-to-medium  
**Risk Grade:** Medium  
**Primary Score:** `score_mm_silent` = 0.423812  
**Risk Flags:** BELOW_EXECUTION_THRESHOLD  

**Trade thesis.** PBSA is selected by the **market_maker_silent_accum_defensive** setup (silent accumulation / liquidity behaviour). The primary model evidence is `score_mm_silent` at 0.424. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is 3.21%; 20-day return is -33.74%; 20-day volatility is 7.73%; volume participation is still thin with volume ratio 0.49. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.000; rank-1 buyer is AI with streak 1; rank-1 seller is SQ; buyer dominance is 69.78%; daily share of the dominant buyer is 1.27%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer retest or stable bid support after accumulation confirmation. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 741 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 22. CINT — market_maker_silent_accum_defensive

**Confidence:** Low-to-medium  
**Risk Grade:** Medium-high  
**Primary Score:** `score_mm_silent` = 0.417461  
**Risk Flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD  

**Trade thesis.** CINT is selected by the **market_maker_silent_accum_defensive** setup (silent accumulation / liquidity behaviour). The primary model evidence is `score_mm_silent` at 0.417. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -10.50%; 20-day return is -16.36%; 20-day volatility is 3.93%; volume expansion is visible with volume ratio 3.08. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.000; rank-1 buyer is XL with streak 2; rank-1 seller is XL; buyer dominance is 61.54%; daily share of the dominant buyer is 41.02%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer retest or stable bid support after accumulation confirmation. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; excessive dependence on one broker continuing to dominate without broader participation; as a volatility-adjusted reference, thesis quality weakens materially around 170 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 23. DEWA — momentum_5d_hgb_defensive

**Confidence:** Low-to-medium  
**Risk Grade:** Medium-high  
**Primary Score:** `score_momentum_5d__momentum_ranker__xgb__momentum_5d` = 0.471753  
**Risk Flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD  

**Trade thesis.** DEWA is selected by the **momentum_5d_hgb_defensive** setup (cross-sectional momentum continuation). The primary model evidence is `score_momentum_5d__momentum_ranker__xgb__momentum_5d` at 0.472. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -14.95%; 20-day return is -40.00%; 20-day volatility is 5.92%; volume ratio is neutral at 0.87. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.009; rank-1 buyer is XL with streak 2; rank-1 seller is AZ; buyer dominance is 15.45%; daily share of the dominant buyer is 41.02%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Enter only if price holds above prior close or reclaims intraday VWAP/support. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; excessive dependence on one broker continuing to dominate without broader participation; as a volatility-adjusted reference, thesis quality weakens materially around 306 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 24. DSSA — momentum_5d_hgb_defensive

**Confidence:** Low-to-medium  
**Risk Grade:** Medium  
**Primary Score:** `score_momentum_5d__momentum_ranker__xgb__momentum_5d` = 0.456992  
**Risk Flags:** BELOW_EXECUTION_THRESHOLD  

**Trade thesis.** DSSA is selected by the **momentum_5d_hgb_defensive** setup (cross-sectional momentum continuation). The primary model evidence is `score_momentum_5d__momentum_ranker__xgb__momentum_5d` at 0.457. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -42.40%; 20-day return is -86.71%; 20-day volatility is 6.86%; volume expansion is visible with volume ratio 4.09. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.023; rank-1 buyer is AK with streak 3; rank-1 seller is ZP; buyer dominance is 14.06%; daily share of the dominant buyer is 2.43%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Enter only if price holds above prior close or reclaims intraday VWAP/support. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 397 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 25. BKDP — momentum_10d_hgb_aggressive

**Confidence:** Low-to-medium  
**Risk Grade:** Medium  
**Primary Score:** `score_momentum_10d__momentum_ranker__hgb__momentum_10d` = 0.468955  
**Risk Flags:** BELOW_EXECUTION_THRESHOLD  

**Trade thesis.** BKDP is selected by the **momentum_10d_hgb_aggressive** setup (cross-sectional momentum continuation). The primary model evidence is `score_momentum_10d__momentum_ranker__hgb__momentum_10d` at 0.469. The price/volume context indicates that price is trading above the 20-day mean, suggesting structure is still constructive relative to its recent base; 5-day return is 19.05%; 20-day return is 98.41%; 20-day volatility is 7.05%; volume expansion is visible with volume ratio 1.83. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.000; rank-1 buyer is PC with streak 1; rank-1 seller is XL; buyer dominance is 22.12%; daily share of the dominant buyer is 0.46%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Enter only if price holds above prior close or reclaims intraday VWAP/support. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 115 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 26. HBAT — momentum_10d_hgb_aggressive

**Confidence:** Low-to-medium  
**Risk Grade:** Medium  
**Primary Score:** `score_momentum_10d__momentum_ranker__hgb__momentum_10d` = 0.444126  
**Risk Flags:** BELOW_EXECUTION_THRESHOLD  

**Trade thesis.** HBAT is selected by the **momentum_10d_hgb_aggressive** setup (cross-sectional momentum continuation). The primary model evidence is `score_momentum_10d__momentum_ranker__hgb__momentum_10d` at 0.444. The price/volume context indicates that price is trading above the 20-day mean, suggesting structure is still constructive relative to its recent base; 5-day return is 26.88%; 20-day return is 49.41%; 20-day volatility is 6.55%; volume expansion is visible with volume ratio 1.59. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.000; rank-1 buyer is XA with streak 1; rank-1 seller is AO; buyer dominance is 36.00%; daily share of the dominant buyer is 1.39%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Enter only if price holds above prior close or reclaims intraday VWAP/support. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 465 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 27. GULA — momentum_10d_hgb_aggressive

**Confidence:** Low-to-medium  
**Risk Grade:** Medium  
**Primary Score:** `score_momentum_10d__momentum_ranker__hgb__momentum_10d` = 0.439911  
**Risk Flags:** BELOW_EXECUTION_THRESHOLD  

**Trade thesis.** GULA is selected by the **momentum_10d_hgb_aggressive** setup (cross-sectional momentum continuation). The primary model evidence is `score_momentum_10d__momentum_ranker__hgb__momentum_10d` at 0.440. The price/volume context indicates that price is trading above the 20-day mean, suggesting structure is still constructive relative to its recent base; 5-day return is 21.36%; 20-day return is 62.34%; 20-day volatility is 4.38%; volume expansion is visible with volume ratio 3.17. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.001; rank-1 buyer is BR with streak 2; rank-1 seller is BR; buyer dominance is 12.62%; daily share of the dominant buyer is 0.58%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Enter only if price holds above prior close or reclaims intraday VWAP/support. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 473 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 28. MSIN — momentum_10d_hgb_aggressive

**Confidence:** Low-to-medium  
**Risk Grade:** Medium  
**Primary Score:** `score_momentum_10d__momentum_ranker__hgb__momentum_10d` = 0.419503  
**Risk Flags:** BELOW_EXECUTION_THRESHOLD  

**Trade thesis.** MSIN is selected by the **momentum_10d_hgb_aggressive** setup (cross-sectional momentum continuation). The primary model evidence is `score_momentum_10d__momentum_ranker__hgb__momentum_10d` at 0.420. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -34.88%; 20-day return is -54.84%; 20-day volatility is 6.69%; volume expansion is visible with volume ratio 1.98. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.003; rank-1 buyer is EP with streak 14; rank-1 seller is BB; buyer dominance is 23.88%; daily share of the dominant buyer is 1.51%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Enter only if price holds above prior close or reclaims intraday VWAP/support. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 386 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 29. TOBA — momentum_10d_hgb_aggressive

**Confidence:** Low-to-medium  
**Risk Grade:** Medium-high  
**Primary Score:** `score_momentum_10d__momentum_ranker__hgb__momentum_10d` = 0.410622  
**Risk Flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD  

**Trade thesis.** TOBA is selected by the **momentum_10d_hgb_aggressive** setup (cross-sectional momentum continuation). The primary model evidence is `score_momentum_10d__momentum_ranker__hgb__momentum_10d` at 0.411. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -11.89%; 20-day return is -36.30%; 20-day volatility is 4.91%; volume ratio is neutral at 0.71. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.001; rank-1 buyer is XL with streak 1; rank-1 seller is CC; buyer dominance is 18.49%; daily share of the dominant buyer is 41.02%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Enter only if price holds above prior close or reclaims intraday VWAP/support. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; excessive dependence on one broker continuing to dominate without broader participation; as a volatility-adjusted reference, thesis quality weakens materially around 404 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 30. BANK — momentum_10d_hgb_aggressive

**Confidence:** Low-to-medium  
**Risk Grade:** Medium-high  
**Primary Score:** `score_momentum_10d__momentum_ranker__hgb__momentum_10d` = 0.408061  
**Risk Flags:** BELOW_EXECUTION_THRESHOLD  

**Trade thesis.** BANK is selected by the **momentum_10d_hgb_aggressive** setup (cross-sectional momentum continuation). The primary model evidence is `score_momentum_10d__momentum_ranker__hgb__momentum_10d` at 0.408. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -26.84%; 20-day return is -48.52%; 20-day volatility is 8.49%; volume participation is still thin with volume ratio 0.60. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.000; rank-1 buyer is PO with streak 1; rank-1 seller is KZ; buyer dominance is 27.27%; daily share of the dominant buyer is 0.12%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Enter only if price holds above prior close or reclaims intraday VWAP/support. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 256 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

## Portfolio-Level Notes

Avoid forcing trades simply because a ticker appears in the report. Prioritize candidates whose thesis remains valid after the market opens, avoid concentration in the same dominant broker behaviour, and reduce exposure when multiple names depend on the same liquidity pattern. If market breadth weakens or volatility becomes abnormal, scale down position sizing or move signals to watchlist-only.