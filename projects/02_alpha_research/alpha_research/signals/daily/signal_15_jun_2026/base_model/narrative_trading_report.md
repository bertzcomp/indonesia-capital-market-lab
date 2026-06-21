# Narrative Trading Intelligence Report

## Market Context

Signal universe is built from the latest available market panel dated **2026-06-12**. macro risk score: -0.913. 5-day market return proxy: 5.49%. 20-day market volatility proxy: 0.026. FX pressure: 0.00%. Brent move: -3.39%. coal proxy move: -3.36%. Regime label: **neutral**.

## Operating Principle

This report is not a simple BUY/SELL list. Each signal is interpreted as a conditional trading thesis. Execution is valid only when price structure, liquidity, momentum, and behavioural confirmation remain aligned. If those conditions fail, no-trade or early exit is the correct risk decision.

## Signal Thesis and Execution Plan

### 1. KIJA — market_maker_silent_accum_defensive

**Confidence:** Medium-high  
**Risk Grade:** Controlled  
**Primary Score:** `score_mm_silent` = 0.609416  
**Risk Flags:** OK  

**Trade thesis.** KIJA is selected by the **market_maker_silent_accum_defensive** setup (silent accumulation / liquidity behaviour). The primary model evidence is `score_mm_silent` at 0.609. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is 0.00%; 20-day return is -35.56%; 20-day volatility is 4.13%; volume ratio is neutral at 0.75. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.000; rank-1 buyer is NI with streak 1; rank-1 seller is KI; buyer dominance is 51.67%; daily share of the dominant buyer is 1.74%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer retest or stable bid support after accumulation confirmation. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 110 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 2. PSKT — market_maker_silent_accum_defensive

**Confidence:** Medium  
**Risk Grade:** Medium  
**Primary Score:** `score_mm_silent` = 0.591614  
**Risk Flags:** OK  

**Trade thesis.** PSKT is selected by the **market_maker_silent_accum_defensive** setup (silent accumulation / liquidity behaviour). The primary model evidence is `score_mm_silent` at 0.592. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is 13.17%; 20-day return is -23.79%; 20-day volatility is 9.35%; volume ratio is neutral at 0.94. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.000; rank-1 buyer is CC with streak 2; rank-1 seller is CC; buyer dominance is 42.65%; daily share of the dominant buyer is 11.27%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer retest or stable bid support after accumulation confirmation. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 174 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 3. OMED — market_maker_silent_accum_defensive

**Confidence:** Medium  
**Risk Grade:** Controlled  
**Primary Score:** `score_mm_silent` = 0.578339  
**Risk Flags:** OK  

**Trade thesis.** OMED is selected by the **market_maker_silent_accum_defensive** setup (silent accumulation / liquidity behaviour). The primary model evidence is `score_mm_silent` at 0.578. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is 4.26%; 20-day return is -34.23%; 20-day volatility is 5.86%; volume ratio is neutral at 1.40. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.000; rank-1 buyer is LG with streak 2; rank-1 seller is LG; buyer dominance is 40.95%; daily share of the dominant buyer is 1.86%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer retest or stable bid support after accumulation confirmation. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 182 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 4. SSMS — swing_hgb_defensive

**Confidence:** Medium-high  
**Risk Grade:** Controlled  
**Primary Score:** `score_swing__multi_strategy_time__hgb__swing` = 0.660260  
**Risk Flags:** OK  

**Trade thesis.** SSMS is selected by the **swing_hgb_defensive** setup (defensive swing continuation). The primary model evidence is `score_swing__multi_strategy_time__hgb__swing` at 0.660. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is 6.43%; 20-day return is -46.40%; 20-day volatility is 6.85%; volume ratio is neutral at 0.98. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.001; rank-1 buyer is CC with streak 5; rank-1 seller is BQ; buyer dominance is 13.69%; daily share of the dominant buyer is 11.27%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer confirmation above prior close or controlled pullback/retest. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 685 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 5. NIKL — swing_hgb_defensive

**Confidence:** Medium-high  
**Risk Grade:** Controlled  
**Primary Score:** `score_swing__multi_strategy_time__hgb__swing` = 0.644399  
**Risk Flags:** OK  

**Trade thesis.** NIKL is selected by the **swing_hgb_defensive** setup (defensive swing continuation). The primary model evidence is `score_swing__multi_strategy_time__hgb__swing` at 0.644. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is 0.52%; 20-day return is -52.00%; 20-day volatility is 6.09%; volume participation is still thin with volume ratio 0.60. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.002; rank-1 buyer is AK with streak 3; rank-1 seller is YP; buyer dominance is 36.23%; daily share of the dominant buyer is 3.95%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer confirmation above prior close or controlled pullback/retest. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 177 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 6. GPSO — swing_hgb_defensive

**Confidence:** Medium-high  
**Risk Grade:** Controlled  
**Primary Score:** `score_swing__multi_strategy_time__hgb__swing` = 0.642700  
**Risk Flags:** OK  

**Trade thesis.** GPSO is selected by the **swing_hgb_defensive** setup (defensive swing continuation). The primary model evidence is `score_swing__multi_strategy_time__hgb__swing` at 0.643. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -18.84%; 20-day return is -23.64%; 20-day volatility is 6.28%; volume expansion is visible with volume ratio 2.32. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.001; rank-1 buyer is CP with streak 1; rank-1 seller is CP; buyer dominance is 39.61%; daily share of the dominant buyer is 3.02%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer confirmation above prior close or controlled pullback/retest. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 310 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 7. ARCI — swing_hgb_defensive

**Confidence:** Medium-high  
**Risk Grade:** Controlled  
**Primary Score:** `score_swing__multi_strategy_time__hgb__swing` = 0.639746  
**Risk Flags:** OK  

**Trade thesis.** ARCI is selected by the **swing_hgb_defensive** setup (defensive swing continuation). The primary model evidence is `score_swing__multi_strategy_time__hgb__swing` at 0.640. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -3.94%; 20-day return is -29.60%; 20-day volatility is 6.20%; volume expansion is visible with volume ratio 1.62. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.008; rank-1 buyer is AK with streak 1; rank-1 seller is XL; buyer dominance is 17.71%; daily share of the dominant buyer is 3.95%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer confirmation above prior close or controlled pullback/retest. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 899 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 8. SCMA — swing_hgb_defensive

**Confidence:** Medium-high  
**Risk Grade:** Controlled  
**Primary Score:** `score_swing__multi_strategy_time__hgb__swing` = 0.635396  
**Risk Flags:** OK  

**Trade thesis.** SCMA is selected by the **swing_hgb_defensive** setup (defensive swing continuation). The primary model evidence is `score_swing__multi_strategy_time__hgb__swing` at 0.635. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is 3.63%; 20-day return is -20.00%; 20-day volatility is 5.18%; volume ratio is neutral at 0.86. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.001; rank-1 buyer is CC with streak 1; rank-1 seller is ZP; buyer dominance is 18.73%; daily share of the dominant buyer is 11.27%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer confirmation above prior close or controlled pullback/retest. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 187 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 9. APLN — swing_hgb_defensive

**Confidence:** Medium-high  
**Risk Grade:** Controlled  
**Primary Score:** `score_swing__multi_strategy_time__hgb__swing` = 0.633759  
**Risk Flags:** OK  

**Trade thesis.** APLN is selected by the **swing_hgb_defensive** setup (defensive swing continuation). The primary model evidence is `score_swing__multi_strategy_time__hgb__swing` at 0.634. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -4.55%; 20-day return is -28.81%; 20-day volatility is 4.73%; volume participation is still thin with volume ratio 0.59. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.006; rank-1 buyer is AK with streak 3; rank-1 seller is CC; buyer dominance is 39.12%; daily share of the dominant buyer is 3.95%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer confirmation above prior close or controlled pullback/retest. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 119 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 10. BBYB — swing_hgb_defensive

**Confidence:** Medium-high  
**Risk Grade:** Controlled  
**Primary Score:** `score_swing__multi_strategy_time__hgb__swing` = 0.633116  
**Risk Flags:** OK  

**Trade thesis.** BBYB is selected by the **swing_hgb_defensive** setup (defensive swing continuation). The primary model evidence is `score_swing__multi_strategy_time__hgb__swing` at 0.633. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is 9.35%; 20-day return is -23.03%; 20-day volatility is 5.42%; volume ratio is neutral at 0.87. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.006; rank-1 buyer is CC with streak 2; rank-1 seller is PD; buyer dominance is 19.34%; daily share of the dominant buyer is 11.27%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer confirmation above prior close or controlled pullback/retest. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 218 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 11. HRUM — swing_hgb_defensive

**Confidence:** Medium-high  
**Risk Grade:** Controlled  
**Primary Score:** `score_swing__multi_strategy_time__hgb__swing` = 0.627155  
**Risk Flags:** OK  

**Trade thesis.** HRUM is selected by the **swing_hgb_defensive** setup (defensive swing continuation). The primary model evidence is `score_swing__multi_strategy_time__hgb__swing` at 0.627. The price/volume context indicates that price is trading above the 20-day mean, suggesting structure is still constructive relative to its recent base; 5-day return is 15.44%; 20-day return is -13.74%; 20-day volatility is 5.84%; volume ratio is neutral at 1.13. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.004; rank-1 buyer is EP with streak 1; rank-1 seller is EP; buyer dominance is 13.67%; daily share of the dominant buyer is 0.93%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer confirmation above prior close or controlled pullback/retest. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 728 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 12. TOBA — swing_hgb_defensive

**Confidence:** Medium-high  
**Risk Grade:** Controlled  
**Primary Score:** `score_swing__multi_strategy_time__hgb__swing` = 0.626890  
**Risk Flags:** OK  

**Trade thesis.** TOBA is selected by the **swing_hgb_defensive** setup (defensive swing continuation). The primary model evidence is `score_swing__multi_strategy_time__hgb__swing` at 0.627. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is 16.18%; 20-day return is -31.28%; 20-day volatility is 6.56%; volume ratio is neutral at 0.91. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.003; rank-1 buyer is CC with streak 1; rank-1 seller is XL; buyer dominance is 23.26%; daily share of the dominant buyer is 11.27%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer confirmation above prior close or controlled pullback/retest. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 370 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 13. TOWR — position_xgb

**Confidence:** Medium  
**Risk Grade:** Controlled  
**Primary Score:** `score_position__multi_strategy_time__xgb__position` = 0.580713  
**Risk Flags:** OK  

**Trade thesis.** TOWR is selected by the **position_xgb** setup (position continuation / structural setup). The primary model evidence is `score_position__multi_strategy_time__xgb__position` at 0.581. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is 4.24%; 20-day return is -27.43%; 20-day volatility is 2.76%; volume expansion is visible with volume ratio 2.43. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.005; rank-1 buyer is AK with streak 1; rank-1 seller is CC; buyer dominance is 19.22%; daily share of the dominant buyer is 3.95%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer close confirmation and stable liquidity rather than intraday spike. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 332 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 14. BRMS — position_xgb

**Confidence:** Medium  
**Risk Grade:** Controlled  
**Primary Score:** `score_position__multi_strategy_time__xgb__position` = 0.580369  
**Risk Flags:** OK  

**Trade thesis.** BRMS is selected by the **position_xgb** setup (position continuation / structural setup). The primary model evidence is `score_position__multi_strategy_time__xgb__position` at 0.580. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is 3.92%; 20-day return is -29.33%; 20-day volatility is 6.15%; volume ratio is neutral at 1.49. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.017; rank-1 buyer is AK with streak 2; rank-1 seller is CC; buyer dominance is 23.80%; daily share of the dominant buyer is 3.95%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer close confirmation and stable liquidity rather than intraday spike. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 489 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 15. INDS — market_maker_silent_accum_defensive

**Confidence:** Low-to-medium  
**Risk Grade:** Medium  
**Primary Score:** `score_mm_silent` = 0.626190  
**Risk Flags:** DOMINANT_RANK1_BUYER  

**Trade thesis.** INDS is selected by the **market_maker_silent_accum_defensive** setup (silent accumulation / liquidity behaviour). The primary model evidence is `score_mm_silent` at 0.626. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is 12.40%; 20-day return is -28.80%; 20-day volatility is 4.96%; volume expansion is visible with volume ratio 3.39. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.002; rank-1 buyer is XL with streak 2; rank-1 seller is XL; buyer dominance is 47.04%; daily share of the dominant buyer is 40.30%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer retest or stable bid support after accumulation confirmation. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; excessive dependence on one broker continuing to dominate without broader participation; as a volatility-adjusted reference, thesis quality weakens materially around 255 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 16. CTTH — market_maker_silent_accum_defensive

**Confidence:** Low-to-medium  
**Risk Grade:** Medium-high  
**Primary Score:** `score_mm_silent` = 0.606025  
**Risk Flags:** DOMINANT_RANK1_BUYER  

**Trade thesis.** CTTH is selected by the **market_maker_silent_accum_defensive** setup (silent accumulation / liquidity behaviour). The primary model evidence is `score_mm_silent` at 0.606. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is 22.32%; 20-day return is -32.18%; 20-day volatility is 10.53%; volume expansion is visible with volume ratio 2.78. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.001; rank-1 buyer is XL with streak 4; rank-1 seller is XL; buyer dominance is 40.78%; daily share of the dominant buyer is 40.30%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer retest or stable bid support after accumulation confirmation. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; excessive dependence on one broker continuing to dominate without broader participation; as a volatility-adjusted reference, thesis quality weakens materially around 126 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 17. PSDN — market_maker_silent_accum_defensive

**Confidence:** Low-to-medium  
**Risk Grade:** Medium  
**Primary Score:** `score_mm_silent` = 0.565215  
**Risk Flags:** DOMINANT_RANK1_BUYER  

**Trade thesis.** PSDN is selected by the **market_maker_silent_accum_defensive** setup (silent accumulation / liquidity behaviour). The primary model evidence is `score_mm_silent` at 0.565. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is 12.75%; 20-day return is -31.14%; 20-day volatility is 7.41%; volume ratio is neutral at 1.48. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.001; rank-1 buyer is XL with streak 6; rank-1 seller is XL; buyer dominance is 45.48%; daily share of the dominant buyer is 40.30%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer retest or stable bid support after accumulation confirmation. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; excessive dependence on one broker continuing to dominate without broader participation; as a volatility-adjusted reference, thesis quality weakens materially around 106 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 18. OASA — swing_hgb_defensive

**Confidence:** Medium, risk-adjusted  
**Risk Grade:** Medium  
**Primary Score:** `score_swing__multi_strategy_time__hgb__swing` = 0.674335  
**Risk Flags:** DOMINANT_RANK1_BUYER  

**Trade thesis.** OASA is selected by the **swing_hgb_defensive** setup (defensive swing continuation). The primary model evidence is `score_swing__multi_strategy_time__hgb__swing` at 0.674. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is 1.56%; 20-day return is -34.67%; 20-day volatility is 7.47%; volume participation is still thin with volume ratio 0.67. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.001; rank-1 buyer is XL with streak 4; rank-1 seller is XL; buyer dominance is 19.04%; daily share of the dominant buyer is 40.30%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer confirmation above prior close or controlled pullback/retest. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; excessive dependence on one broker continuing to dominate without broader participation; as a volatility-adjusted reference, thesis quality weakens materially around 239 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 19. SOCI — swing_hgb_defensive

**Confidence:** Low-to-medium  
**Risk Grade:** Medium  
**Primary Score:** `score_swing__multi_strategy_time__hgb__swing` = 0.648148  
**Risk Flags:** DOMINANT_RANK1_BUYER  

**Trade thesis.** SOCI is selected by the **swing_hgb_defensive** setup (defensive swing continuation). The primary model evidence is `score_swing__multi_strategy_time__hgb__swing` at 0.648. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is 11.03%; 20-day return is -31.78%; 20-day volatility is 6.41%; volume ratio is neutral at 1.35. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.006; rank-1 buyer is XL with streak 4; rank-1 seller is CC; buyer dominance is 22.13%; daily share of the dominant buyer is 40.30%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer confirmation above prior close or controlled pullback/retest. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; excessive dependence on one broker continuing to dominate without broader participation; as a volatility-adjusted reference, thesis quality weakens materially around 296 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 20. GTSI — swing_hgb_defensive

**Confidence:** Low-to-medium  
**Risk Grade:** Medium-high  
**Primary Score:** `score_swing__multi_strategy_time__hgb__swing` = 0.630009  
**Risk Flags:** DOMINANT_RANK1_BUYER  

**Trade thesis.** GTSI is selected by the **swing_hgb_defensive** setup (defensive swing continuation). The primary model evidence is `score_swing__multi_strategy_time__hgb__swing` at 0.630. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is 22.94%; 20-day return is -34.95%; 20-day volatility is 8.22%; volume ratio is neutral at 1.26. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.001; rank-1 buyer is XL with streak 4; rank-1 seller is XL; buyer dominance is 27.29%; daily share of the dominant buyer is 40.30%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer confirmation above prior close or controlled pullback/retest. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; excessive dependence on one broker continuing to dominate without broader participation; as a volatility-adjusted reference, thesis quality weakens materially around 123 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 21. PYFA — swing_hgb_defensive

**Confidence:** Low-to-medium  
**Risk Grade:** Medium  
**Primary Score:** `score_swing__multi_strategy_time__hgb__swing` = 0.624062  
**Risk Flags:** DOMINANT_RANK1_BUYER  

**Trade thesis.** PYFA is selected by the **swing_hgb_defensive** setup (defensive swing continuation). The primary model evidence is `score_swing__multi_strategy_time__hgb__swing` at 0.624. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is 7.78%; 20-day return is -50.26%; 20-day volatility is 6.13%; volume participation is still thin with volume ratio 0.66. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.002; rank-1 buyer is XL with streak 4; rank-1 seller is XL; buyer dominance is 28.24%; daily share of the dominant buyer is 40.30%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer confirmation above prior close or controlled pullback/retest. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; excessive dependence on one broker continuing to dominate without broader participation; as a volatility-adjusted reference, thesis quality weakens materially around 179 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 22. DEFI — swing_hgb_defensive

**Confidence:** Low-to-medium  
**Risk Grade:** Medium  
**Primary Score:** `score_swing__multi_strategy_time__hgb__swing` = 0.623123  
**Risk Flags:** DOMINANT_RANK1_BUYER  

**Trade thesis.** DEFI is selected by the **swing_hgb_defensive** setup (defensive swing continuation). The primary model evidence is `score_swing__multi_strategy_time__hgb__swing` at 0.623. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is 18.95%; 20-day return is -37.57%; 20-day volatility is 7.18%; volume ratio is neutral at 1.29. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.001; rank-1 buyer is XL with streak 5; rank-1 seller is XL; buyer dominance is 55.68%; daily share of the dominant buyer is 40.30%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer confirmation above prior close or controlled pullback/retest. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; excessive dependence on one broker continuing to dominate without broader participation; as a volatility-adjusted reference, thesis quality weakens materially around 104 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 23. SUPA — position_xgb

**Confidence:** Low-to-medium  
**Risk Grade:** Medium  
**Primary Score:** `score_position__multi_strategy_time__xgb__position` = 0.610032  
**Risk Flags:** DOMINANT_RANK1_BUYER  

**Trade thesis.** SUPA is selected by the **position_xgb** setup (position continuation / structural setup). The primary model evidence is `score_position__multi_strategy_time__xgb__position` at 0.610. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -12.77%; 20-day return is -26.35%; 20-day volatility is 5.42%; volume ratio is neutral at 1.06. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.000; rank-1 buyer is XL with streak 1; rank-1 seller is CC; buyer dominance is 22.59%; daily share of the dominant buyer is 40.30%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer close confirmation and stable liquidity rather than intraday spike. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; excessive dependence on one broker continuing to dominate without broader participation; as a volatility-adjusted reference, thesis quality weakens materially around 573 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 24. ESSA — position_xgb

**Confidence:** Low-to-medium  
**Risk Grade:** Medium  
**Primary Score:** `score_position__multi_strategy_time__xgb__position` = 0.594009  
**Risk Flags:** DOMINANT_RANK1_BUYER  

**Trade thesis.** ESSA is selected by the **position_xgb** setup (position continuation / structural setup). The primary model evidence is `score_position__multi_strategy_time__xgb__position` at 0.594. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is 2.56%; 20-day return is -28.14%; 20-day volatility is 4.12%; volume ratio is neutral at 1.17. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.008; rank-1 buyer is XL with streak 1; rank-1 seller is SQ; buyer dominance is 17.13%; daily share of the dominant buyer is 40.30%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer close confirmation and stable liquidity rather than intraday spike. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; excessive dependence on one broker continuing to dominate without broader participation; as a volatility-adjusted reference, thesis quality weakens materially around 569 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 25. EMTK — position_xgb

**Confidence:** Low-to-medium  
**Risk Grade:** Medium  
**Primary Score:** `score_position__multi_strategy_time__xgb__position` = 0.589875  
**Risk Flags:** DOMINANT_RANK1_BUYER  

**Trade thesis.** EMTK is selected by the **position_xgb** setup (position continuation / structural setup). The primary model evidence is `score_position__multi_strategy_time__xgb__position` at 0.590. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is 5.77%; 20-day return is -27.63%; 20-day volatility is 3.89%; volume ratio is neutral at 0.82. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.001; rank-1 buyer is XL with streak 1; rank-1 seller is YU; buyer dominance is 25.04%; daily share of the dominant buyer is 40.30%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer close confirmation and stable liquidity rather than intraday spike. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; excessive dependence on one broker continuing to dominate without broader participation; as a volatility-adjusted reference, thesis quality weakens materially around 523 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 26. IRSX — position_xgb

**Confidence:** Low-to-medium  
**Risk Grade:** Medium-high  
**Primary Score:** `score_position__multi_strategy_time__xgb__position` = 0.567712  
**Risk Flags:** DOMINANT_RANK1_BUYER  

**Trade thesis.** IRSX is selected by the **position_xgb** setup (position continuation / structural setup). The primary model evidence is `score_position__multi_strategy_time__xgb__position` at 0.568. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is 21.49%; 20-day return is -28.29%; 20-day volatility is 9.43%; volume ratio is neutral at 0.89. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.001; rank-1 buyer is XL with streak 1; rank-1 seller is XL; buyer dominance is 29.90%; daily share of the dominant buyer is 40.30%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer close confirmation and stable liquidity rather than intraday spike. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; excessive dependence on one broker continuing to dominate without broader participation; as a volatility-adjusted reference, thesis quality weakens materially around 270 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 27. ASPR — ara_candidate

**Confidence:** Low-to-medium  
**Risk Grade:** High  
**Primary Score:** `score_ara` = 0.233480  
**Risk Flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD  

**Trade thesis.** ASPR is selected by the **ara_candidate** setup (tactical event / watchlist). The primary model evidence is `score_ara` at 0.233. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is 61.19%; 20-day return is -52.63%; 20-day volatility is 15.86%; volume expansion is visible with volume ratio 1.68. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.000; rank-1 buyer is XL with streak 13; rank-1 seller is XL; buyer dominance is 31.57%; daily share of the dominant buyer is 40.30%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Only after strong opening confirmation; avoid chasing failed gap-up moves. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; excessive dependence on one broker continuing to dominate without broader participation; as a volatility-adjusted reference, thesis quality weakens materially around 199 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 28. ESIP — market_maker_silent_accum_defensive

**Confidence:** Low-to-medium  
**Risk Grade:** Medium-high  
**Primary Score:** `score_mm_silent` = 0.534683  
**Risk Flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD  

**Trade thesis.** ESIP is selected by the **market_maker_silent_accum_defensive** setup (silent accumulation / liquidity behaviour). The primary model evidence is `score_mm_silent` at 0.535. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is 16.49%; 20-day return is -39.57%; 20-day volatility is 6.78%; volume participation is still thin with volume ratio 0.59. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.001; rank-1 buyer is XL with streak 5; rank-1 seller is XL; buyer dominance is 48.50%; daily share of the dominant buyer is 40.30%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer retest or stable bid support after accumulation confirmation. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; excessive dependence on one broker continuing to dominate without broader participation; as a volatility-adjusted reference, thesis quality weakens materially around 104 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 29. GULA — momentum_5d_hgb_defensive

**Confidence:** Low-to-medium  
**Risk Grade:** Medium  
**Primary Score:** `score_momentum_5d__momentum_ranker__xgb__momentum_5d` = 0.400105  
**Risk Flags:** BELOW_EXECUTION_THRESHOLD  

**Trade thesis.** GULA is selected by the **momentum_5d_hgb_defensive** setup (cross-sectional momentum continuation). The primary model evidence is `score_momentum_5d__momentum_ranker__xgb__momentum_5d` at 0.400. The price/volume context indicates that price is trading above the 20-day mean, suggesting structure is still constructive relative to its recent base; 5-day return is 15.00%; 20-day return is 40.93%; 20-day volatility is 4.80%; volume ratio is neutral at 1.12. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.006; rank-1 buyer is MG with streak 1; rank-1 seller is MG; buyer dominance is 16.06%; daily share of the dominant buyer is 1.74%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Enter only if price holds above prior close or reclaims intraday VWAP/support. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 540 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 30. RGAS — momentum_10d_hgb_aggressive

**Confidence:** Low-to-medium  
**Risk Grade:** Medium  
**Primary Score:** `score_momentum_10d__momentum_ranker__hgb__momentum_10d` = 0.386357  
**Risk Flags:** BELOW_EXECUTION_THRESHOLD  

**Trade thesis.** RGAS is selected by the **momentum_10d_hgb_aggressive** setup (cross-sectional momentum continuation). The primary model evidence is `score_momentum_10d__momentum_ranker__hgb__momentum_10d` at 0.386. The price/volume context indicates that price is trading above the 20-day mean, suggesting structure is still constructive relative to its recent base; 5-day return is 47.52%; 20-day return is 60.22%; 20-day volatility is 7.30%; volume expansion is visible with volume ratio 3.53. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.002; rank-1 buyer is LG with streak 1; rank-1 seller is LG; buyer dominance is 38.91%; daily share of the dominant buyer is 1.86%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Enter only if price holds above prior close or reclaims intraday VWAP/support. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 137 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

## Portfolio-Level Notes

Avoid forcing trades simply because a ticker appears in the report. Prioritize candidates whose thesis remains valid after the market opens, avoid concentration in the same dominant broker behaviour, and reduce exposure when multiple names depend on the same liquidity pattern. If market breadth weakens or volatility becomes abnormal, scale down position sizing or move signals to watchlist-only.