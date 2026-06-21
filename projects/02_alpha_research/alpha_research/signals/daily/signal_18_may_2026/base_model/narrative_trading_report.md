# Narrative Trading Intelligence Report

## Market Context

Signal universe is built from the latest available market panel dated **2026-05-13**. macro risk score: -1.497. 5-day market return proxy: -3.57%. 20-day market volatility proxy: 0.012. FX pressure: 0.00%. Brent move: -1.99%. coal proxy move: -1.97%. Regime label: **risk_off**.

## Operating Principle

This report is not a simple BUY/SELL list. Each signal is interpreted as a conditional trading thesis. Execution is valid only when price structure, liquidity, momentum, and behavioural confirmation remain aligned. If those conditions fail, no-trade or early exit is the correct risk decision.

## Signal Thesis and Execution Plan

### 1. MBMA — swing_hgb_defensive

**Confidence:** Medium-high  
**Risk Grade:** Controlled  
**Primary Score:** `score_swing__multi_strategy_time__hgb__swing` = 0.606502  
**Risk Flags:** OK  

**Trade thesis.** MBMA is selected by the **swing_hgb_defensive** setup (defensive swing continuation). The primary model evidence is `score_swing__multi_strategy_time__hgb__swing` at 0.607. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -15.22%; 20-day return is -25.00%; 20-day volatility is 4.06%; volume participation is still thin with volume ratio 0.57. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.000; rank-1 buyer is CC with streak 1; rank-1 seller is ZP; buyer dominance is 17.99%; daily share of the dominant buyer is 7.06%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer confirmation above prior close or controlled pullback/retest. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 555 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 2. PBSA — swing_hgb_defensive

**Confidence:** Medium-high  
**Risk Grade:** Controlled  
**Primary Score:** `score_swing__multi_strategy_time__hgb__swing` = 0.606068  
**Risk Flags:** OK  

**Trade thesis.** PBSA is selected by the **swing_hgb_defensive** setup (defensive swing continuation). The primary model evidence is `score_swing__multi_strategy_time__hgb__swing` at 0.606. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -25.11%; 20-day return is -24.46%; 20-day volatility is 4.10%; volume participation is still thin with volume ratio 0.60. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.000; rank-1 buyer is NI with streak 1; rank-1 seller is LG; buyer dominance is 29.47%; daily share of the dominant buyer is 1.39%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer confirmation above prior close or controlled pullback/retest. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 835 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 3. MSJA — swing_hgb_defensive

**Confidence:** Medium-high  
**Risk Grade:** Controlled  
**Primary Score:** `score_swing__multi_strategy_time__hgb__swing` = 0.605376  
**Risk Flags:** OK  

**Trade thesis.** MSJA is selected by the **swing_hgb_defensive** setup (defensive swing continuation). The primary model evidence is `score_swing__multi_strategy_time__hgb__swing` at 0.605. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -20.38%; 20-day return is -16.40%; 20-day volatility is 5.18%; volume ratio is neutral at 1.12. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.000; rank-1 buyer is AZ with streak 1; rank-1 seller is CC; buyer dominance is 50.47%; daily share of the dominant buyer is 1.62%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer confirmation above prior close or controlled pullback/retest. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 391 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 4. CYBR — swing_hgb_defensive

**Confidence:** Medium  
**Risk Grade:** Medium  
**Primary Score:** `score_swing__multi_strategy_time__hgb__swing` = 0.598765  
**Risk Flags:** OK  

**Trade thesis.** CYBR is selected by the **swing_hgb_defensive** setup (defensive swing continuation). The primary model evidence is `score_swing__multi_strategy_time__hgb__swing` at 0.599. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -48.21%; 20-day return is -57.65%; 20-day volatility is 11.34%; volume ratio is neutral at 0.75. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.000; rank-1 buyer is TP with streak 1; rank-1 seller is AK; buyer dominance is 24.79%; daily share of the dominant buyer is 0.81%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer confirmation above prior close or controlled pullback/retest. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 598 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 5. TIRA — swing_hgb_defensive

**Confidence:** Medium  
**Risk Grade:** Controlled  
**Primary Score:** `score_swing__multi_strategy_time__hgb__swing` = 0.595547  
**Risk Flags:** OK  

**Trade thesis.** TIRA is selected by the **swing_hgb_defensive** setup (defensive swing continuation). The primary model evidence is `score_swing__multi_strategy_time__hgb__swing` at 0.596. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -26.86%; 20-day return is -35.35%; 20-day volatility is 5.65%; volume expansion is visible with volume ratio 1.89. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.000; rank-1 buyer is DU with streak 1; rank-1 seller is XA; buyer dominance is 83.37%; daily share of the dominant buyer is 0.35%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer confirmation above prior close or controlled pullback/retest. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 595 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 6. MAIN — swing_hgb_defensive

**Confidence:** Medium  
**Risk Grade:** Controlled  
**Primary Score:** `score_swing__multi_strategy_time__hgb__swing` = 0.587726  
**Risk Flags:** OK  

**Trade thesis.** MAIN is selected by the **swing_hgb_defensive** setup (defensive swing continuation). The primary model evidence is `score_swing__multi_strategy_time__hgb__swing` at 0.588. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -14.50%; 20-day return is -11.86%; 20-day volatility is 4.07%; volume participation is still thin with volume ratio 0.64. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.000; rank-1 buyer is YP with streak 1; rank-1 seller is XL; buyer dominance is 36.93%; daily share of the dominant buyer is 5.21%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer confirmation above prior close or controlled pullback/retest. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 812 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 7. RSCH — swing_hgb_defensive

**Confidence:** Medium  
**Risk Grade:** Controlled  
**Primary Score:** `score_swing__multi_strategy_time__hgb__swing` = 0.586683  
**Risk Flags:** OK  

**Trade thesis.** RSCH is selected by the **swing_hgb_defensive** setup (defensive swing continuation). The primary model evidence is `score_swing__multi_strategy_time__hgb__swing` at 0.587. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -11.35%; 20-day return is -21.88%; 20-day volatility is 4.77%; volume ratio is neutral at 0.75. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.002; rank-1 buyer is BQ with streak 1; rank-1 seller is BQ; buyer dominance is 14.69%; daily share of the dominant buyer is 0.93%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer confirmation above prior close or controlled pullback/retest. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 235 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 8. PEVE — swing_hgb_defensive

**Confidence:** Medium  
**Risk Grade:** Controlled  
**Primary Score:** `score_swing__multi_strategy_time__hgb__swing` = 0.581021  
**Risk Flags:** OK  

**Trade thesis.** PEVE is selected by the **swing_hgb_defensive** setup (defensive swing continuation). The primary model evidence is `score_swing__multi_strategy_time__hgb__swing` at 0.581. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -16.19%; 20-day return is -27.27%; 20-day volatility is 2.31%; volume expansion is visible with volume ratio 5.94. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.000; rank-1 buyer is YP with streak 1; rank-1 seller is EP; buyer dominance is 60.45%; daily share of the dominant buyer is 5.21%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer confirmation above prior close or controlled pullback/retest. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 342 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 9. BEEF — swing_hgb_defensive

**Confidence:** Medium  
**Risk Grade:** Controlled  
**Primary Score:** `score_swing__multi_strategy_time__hgb__swing` = 0.570681  
**Risk Flags:** OK  

**Trade thesis.** BEEF is selected by the **swing_hgb_defensive** setup (defensive swing continuation). The primary model evidence is `score_swing__multi_strategy_time__hgb__swing` at 0.571. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -23.79%; 20-day return is -35.12%; 20-day volatility is 5.40%; volume expansion is visible with volume ratio 6.28. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.005; rank-1 buyer is SQ with streak 1; rank-1 seller is LG; buyer dominance is 39.44%; daily share of the dominant buyer is 2.31%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer confirmation above prior close or controlled pullback/retest. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 146 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 10. UNSP — swing_hgb_defensive

**Confidence:** Medium  
**Risk Grade:** Controlled  
**Primary Score:** `score_swing__multi_strategy_time__hgb__swing` = 0.565378  
**Risk Flags:** OK  

**Trade thesis.** UNSP is selected by the **swing_hgb_defensive** setup (defensive swing continuation). The primary model evidence is `score_swing__multi_strategy_time__hgb__swing` at 0.565. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -16.32%; 20-day return is -8.62%; 20-day volatility is 5.69%; volume expansion is visible with volume ratio 2.70. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.000; rank-1 buyer is HD with streak 1; rank-1 seller is BQ; buyer dominance is 58.32%; daily share of the dominant buyer is 0.35%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer confirmation above prior close or controlled pullback/retest. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 295 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 11. KOKA — swing_hgb_defensive

**Confidence:** Low-to-medium  
**Risk Grade:** Medium  
**Primary Score:** `score_swing__multi_strategy_time__hgb__swing` = 0.614905  
**Risk Flags:** DOMINANT_RANK1_BUYER  

**Trade thesis.** KOKA is selected by the **swing_hgb_defensive** setup (defensive swing continuation). The primary model evidence is `score_swing__multi_strategy_time__hgb__swing` at 0.615. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -19.57%; 20-day return is -17.32%; 20-day volatility is 4.33%; volume ratio is neutral at 1.05. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.000; rank-1 buyer is XL with streak 1; rank-1 seller is XL; buyer dominance is 29.00%; daily share of the dominant buyer is 43.29%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer confirmation above prior close or controlled pullback/retest. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; excessive dependence on one broker continuing to dominate without broader participation; as a volatility-adjusted reference, thesis quality weakens materially around 140 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 12. TRIN — swing_hgb_defensive

**Confidence:** Low-to-medium  
**Risk Grade:** Medium  
**Primary Score:** `score_swing__multi_strategy_time__hgb__swing` = 0.609034  
**Risk Flags:** DOMINANT_RANK1_BUYER  

**Trade thesis.** TRIN is selected by the **swing_hgb_defensive** setup (defensive swing continuation). The primary model evidence is `score_swing__multi_strategy_time__hgb__swing` at 0.609. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -15.38%; 20-day return is -26.67%; 20-day volatility is 3.42%; volume participation is still thin with volume ratio 0.46. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.000; rank-1 buyer is XL with streak 1; rank-1 seller is CC; buyer dominance is 36.72%; daily share of the dominant buyer is 43.29%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer confirmation above prior close or controlled pullback/retest. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; excessive dependence on one broker continuing to dominate without broader participation; as a volatility-adjusted reference, thesis quality weakens materially around 579 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 13. SOCI — swing_hgb_defensive

**Confidence:** Low-to-medium  
**Risk Grade:** Medium  
**Primary Score:** `score_swing__multi_strategy_time__hgb__swing` = 0.581261  
**Risk Flags:** DOMINANT_RANK1_BUYER  

**Trade thesis.** SOCI is selected by the **swing_hgb_defensive** setup (defensive swing continuation). The primary model evidence is `score_swing__multi_strategy_time__hgb__swing` at 0.581. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -8.13%; 20-day return is -11.37%; 20-day volatility is 4.46%; volume participation is still thin with volume ratio 0.56. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.003; rank-1 buyer is XL with streak 1; rank-1 seller is XL; buyer dominance is 21.39%; daily share of the dominant buyer is 43.29%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer confirmation above prior close or controlled pullback/retest. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; excessive dependence on one broker continuing to dominate without broader participation; as a volatility-adjusted reference, thesis quality weakens materially around 427 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 14. TRON — swing_hgb_defensive

**Confidence:** Low-to-medium  
**Risk Grade:** Medium  
**Primary Score:** `score_swing__multi_strategy_time__hgb__swing` = 0.579599  
**Risk Flags:** DOMINANT_RANK1_BUYER  

**Trade thesis.** TRON is selected by the **swing_hgb_defensive** setup (defensive swing continuation). The primary model evidence is `score_swing__multi_strategy_time__hgb__swing` at 0.580. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -12.95%; 20-day return is -28.82%; 20-day volatility is 3.84%; volume participation is still thin with volume ratio 0.52. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.000; rank-1 buyer is XL with streak 13; rank-1 seller is XL; buyer dominance is 30.86%; daily share of the dominant buyer is 43.29%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer confirmation above prior close or controlled pullback/retest. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; excessive dependence on one broker continuing to dominate without broader participation; as a volatility-adjusted reference, thesis quality weakens materially around 115 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 15. BEER — swing_hgb_defensive

**Confidence:** Low-to-medium  
**Risk Grade:** Medium  
**Primary Score:** `score_swing__multi_strategy_time__hgb__swing` = 0.567273  
**Risk Flags:** DOMINANT_RANK1_BUYER  

**Trade thesis.** BEER is selected by the **swing_hgb_defensive** setup (defensive swing continuation). The primary model evidence is `score_swing__multi_strategy_time__hgb__swing` at 0.567. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -17.78%; 20-day return is -16.54%; 20-day volatility is 7.49%; volume participation is still thin with volume ratio 0.25. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.000; rank-1 buyer is XL with streak 1; rank-1 seller is XL; buyer dominance is 24.45%; daily share of the dominant buyer is 43.29%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer confirmation above prior close or controlled pullback/retest. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; excessive dependence on one broker continuing to dominate without broader participation; as a volatility-adjusted reference, thesis quality weakens materially around 102 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 16. DPUM — ara_candidate

**Confidence:** Low-to-medium  
**Risk Grade:** High  
**Primary Score:** `score_ara` = 0.294875  
**Risk Flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD  

**Trade thesis.** DPUM is selected by the **ara_candidate** setup (tactical event / watchlist). The primary model evidence is `score_ara` at 0.295. The price/volume context indicates that price is trading above the 20-day mean, suggesting structure is still constructive relative to its recent base; 5-day return is 57.38%; 20-day return is 62.71%; 20-day volatility is 14.08%; volume expansion is visible with volume ratio 1.81. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.004; rank-1 buyer is XL with streak 3; rank-1 seller is XL; buyer dominance is 33.50%; daily share of the dominant buyer is 43.29%; BDM confirmation is present, improving behavioural confidence.

**Execution plan.** Entry should not be treated as automatic at the open. Only after strong opening confirmation; avoid chasing failed gap-up moves. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; excessive dependence on one broker continuing to dominate without broader participation; as a volatility-adjusted reference, thesis quality weakens materially around 177 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 17. PEGE — market_maker_silent_accum_defensive

**Confidence:** Low-to-medium  
**Risk Grade:** High  
**Primary Score:** `score_mm_silent` = 0.383159  
**Risk Flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD  

**Trade thesis.** PEGE is selected by the **market_maker_silent_accum_defensive** setup (silent accumulation / liquidity behaviour). The primary model evidence is `score_mm_silent` at 0.383. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -13.25%; 20-day return is 8.26%; 20-day volatility is 9.20%; volume expansion is visible with volume ratio 2.18. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.002; rank-1 buyer is XL with streak 32; rank-1 seller is XL; buyer dominance is 51.27%; daily share of the dominant buyer is 43.29%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer retest or stable bid support after accumulation confirmation. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; excessive dependence on one broker continuing to dominate without broader participation; as a volatility-adjusted reference, thesis quality weakens materially around 121 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 18. MSIN — market_maker_silent_accum_defensive

**Confidence:** Low-to-medium  
**Risk Grade:** Medium-high  
**Primary Score:** `score_mm_silent` = 0.345114  
**Risk Flags:** BELOW_EXECUTION_THRESHOLD  

**Trade thesis.** MSIN is selected by the **market_maker_silent_accum_defensive** setup (silent accumulation / liquidity behaviour). The primary model evidence is `score_mm_silent` at 0.345. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -22.29%; 20-day return is -32.11%; 20-day volatility is 9.63%; volume ratio is neutral at 1.16. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.004; rank-1 buyer is EP with streak 7; rank-1 seller is AK; buyer dominance is 41.45%; daily share of the dominant buyer is 1.27%; BDM confirmation is present, improving behavioural confidence.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer retest or stable bid support after accumulation confirmation. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 593 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 19. PACK — market_maker_silent_accum_defensive

**Confidence:** Low-to-medium  
**Risk Grade:** Medium-high  
**Primary Score:** `score_mm_silent` = 0.342291  
**Risk Flags:** BELOW_EXECUTION_THRESHOLD  

**Trade thesis.** PACK is selected by the **market_maker_silent_accum_defensive** setup (silent accumulation / liquidity behaviour). The primary model evidence is `score_mm_silent` at 0.342. The price/volume context indicates that price is trading above the 20-day mean, suggesting structure is still constructive relative to its recent base; 5-day return is 35.65%; 20-day return is 80.35%; 20-day volatility is 8.54%; volume expansion is visible with volume ratio 1.87. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.002; rank-1 buyer is SQ with streak 1; rank-1 seller is SQ; buyer dominance is 84.58%; daily share of the dominant buyer is 2.31%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer retest or stable bid support after accumulation confirmation. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 287 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 20. OASA — market_maker_silent_accum_defensive

**Confidence:** Low-to-medium  
**Risk Grade:** Medium-high  
**Primary Score:** `score_mm_silent` = 0.337747  
**Risk Flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD  

**Trade thesis.** OASA is selected by the **market_maker_silent_accum_defensive** setup (silent accumulation / liquidity behaviour). The primary model evidence is `score_mm_silent` at 0.338. The price/volume context indicates that price is trading above the 20-day mean, suggesting structure is still constructive relative to its recent base; 5-day return is 2.53%; 20-day return is 32.68%; 20-day volatility is 6.56%; volume ratio is neutral at 0.92. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.009; rank-1 buyer is XL with streak 10; rank-1 seller is XL; buyer dominance is 20.73%; daily share of the dominant buyer is 43.29%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer retest or stable bid support after accumulation confirmation. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; excessive dependence on one broker continuing to dominate without broader participation; as a volatility-adjusted reference, thesis quality weakens materially around 374 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 21. BELL — market_maker_silent_accum_defensive

**Confidence:** Low-to-medium  
**Risk Grade:** Medium-high  
**Primary Score:** `score_mm_silent` = 0.336074  
**Risk Flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD  

**Trade thesis.** BELL is selected by the **market_maker_silent_accum_defensive** setup (silent accumulation / liquidity behaviour). The primary model evidence is `score_mm_silent` at 0.336. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -18.35%; 20-day return is -16.77%; 20-day volatility is 5.83%; volume participation is still thin with volume ratio 0.18. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.000; rank-1 buyer is XL with streak 17; rank-1 seller is XL; buyer dominance is 48.00%; daily share of the dominant buyer is 43.29%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer retest or stable bid support after accumulation confirmation. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; excessive dependence on one broker continuing to dominate without broader participation; as a volatility-adjusted reference, thesis quality weakens materially around 120 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 22. MEDS — market_maker_silent_accum_defensive

**Confidence:** Low-to-medium  
**Risk Grade:** Medium-high  
**Primary Score:** `score_mm_silent` = 0.333939  
**Risk Flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD  

**Trade thesis.** MEDS is selected by the **market_maker_silent_accum_defensive** setup (silent accumulation / liquidity behaviour). The primary model evidence is `score_mm_silent` at 0.334. The price/volume context indicates that price is trading above the 20-day mean, suggesting structure is still constructive relative to its recent base; 5-day return is 35.90%; 20-day return is 58.21%; 20-day volatility is 6.90%; volume expansion is visible with volume ratio 3.01. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.002; rank-1 buyer is XL with streak 8; rank-1 seller is XL; buyer dominance is 26.50%; daily share of the dominant buyer is 43.29%; BDM confirmation is present, improving behavioural confidence.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer retest or stable bid support after accumulation confirmation. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; excessive dependence on one broker continuing to dominate without broader participation; as a volatility-adjusted reference, thesis quality weakens materially around 98 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 23. PGJO — momentum_10d_hgb_aggressive

**Confidence:** Low-to-medium  
**Risk Grade:** Medium  
**Primary Score:** `score_momentum_10d__momentum_ranker__hgb__momentum_10d` = 0.456622  
**Risk Flags:** BELOW_EXECUTION_THRESHOLD  

**Trade thesis.** PGJO is selected by the **momentum_10d_hgb_aggressive** setup (cross-sectional momentum continuation). The primary model evidence is `score_momentum_10d__momentum_ranker__hgb__momentum_10d` at 0.457. The price/volume context indicates that price is trading above the 20-day mean, suggesting structure is still constructive relative to its recent base; 5-day return is 6.02%; 20-day return is 57.14%; 20-day volatility is 5.47%; volume expansion is visible with volume ratio 1.96. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.000; rank-1 buyer is MG with streak 1; rank-1 seller is XL; buyer dominance is 66.29%; daily share of the dominant buyer is 0.93%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Enter only if price holds above prior close or reclaims intraday VWAP/support. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 820 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 24. UVCR — momentum_10d_hgb_aggressive

**Confidence:** Low-to-medium  
**Risk Grade:** Medium  
**Primary Score:** `score_momentum_10d__momentum_ranker__hgb__momentum_10d` = 0.450048  
**Risk Flags:** BELOW_EXECUTION_THRESHOLD  

**Trade thesis.** UVCR is selected by the **momentum_10d_hgb_aggressive** setup (cross-sectional momentum continuation). The primary model evidence is `score_momentum_10d__momentum_ranker__hgb__momentum_10d` at 0.450. The price/volume context indicates that price is trading above the 20-day mean, suggesting structure is still constructive relative to its recent base; 5-day return is 16.00%; 20-day return is 58.90%; 20-day volatility is 3.41%; volume ratio is neutral at 1.08. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.004; rank-1 buyer is CP with streak 1; rank-1 seller is CP; buyer dominance is 24.35%; daily share of the dominant buyer is 3.12%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Enter only if price holds above prior close or reclaims intraday VWAP/support. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 222 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 25. KING — momentum_10d_hgb_aggressive

**Confidence:** Low-to-medium  
**Risk Grade:** Medium-high  
**Primary Score:** `score_momentum_10d__momentum_ranker__hgb__momentum_10d` = 0.427065  
**Risk Flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD  

**Trade thesis.** KING is selected by the **momentum_10d_hgb_aggressive** setup (cross-sectional momentum continuation). The primary model evidence is `score_momentum_10d__momentum_ranker__hgb__momentum_10d` at 0.427. The price/volume context indicates that price is trading above the 20-day mean, suggesting structure is still constructive relative to its recent base; 5-day return is 10.31%; 20-day return is 84.96%; 20-day volatility is 5.00%; volume expansion is visible with volume ratio 1.72. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.001; rank-1 buyer is XL with streak 1; rank-1 seller is IN; buyer dominance is 17.43%; daily share of the dominant buyer is 43.29%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Enter only if price holds above prior close or reclaims intraday VWAP/support. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; excessive dependence on one broker continuing to dominate without broader participation; as a volatility-adjusted reference, thesis quality weakens materially around 461 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 26. GPSO — momentum_10d_hgb_aggressive

**Confidence:** Low-to-medium  
**Risk Grade:** Medium  
**Primary Score:** `score_momentum_10d__momentum_ranker__hgb__momentum_10d` = 0.420349  
**Risk Flags:** BELOW_EXECUTION_THRESHOLD  

**Trade thesis.** GPSO is selected by the **momentum_10d_hgb_aggressive** setup (cross-sectional momentum continuation). The primary model evidence is `score_momentum_10d__momentum_ranker__hgb__momentum_10d` at 0.420. The price/volume context indicates that price is trading above the 20-day mean, suggesting structure is still constructive relative to its recent base; 5-day return is 38.15%; 20-day return is 52.23%; 20-day volatility is 4.96%; volume ratio is neutral at 0.92. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.000; rank-1 buyer is XC with streak 1; rank-1 seller is CP; buyer dominance is 17.11%; daily share of the dominant buyer is 3.12%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Enter only if price holds above prior close or reclaims intraday VWAP/support. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 448 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 27. NEST — momentum_10d_hgb_aggressive

**Confidence:** Low-to-medium  
**Risk Grade:** Medium  
**Primary Score:** `score_momentum_10d__momentum_ranker__hgb__momentum_10d` = 0.419459  
**Risk Flags:** BELOW_EXECUTION_THRESHOLD  

**Trade thesis.** NEST is selected by the **momentum_10d_hgb_aggressive** setup (cross-sectional momentum continuation). The primary model evidence is `score_momentum_10d__momentum_ranker__hgb__momentum_10d` at 0.419. The price/volume context indicates that price is trading above the 20-day mean, suggesting structure is still constructive relative to its recent base; 5-day return is 34.09%; 20-day return is 80.98%; 20-day volatility is 7.78%; volume expansion is visible with volume ratio 7.85. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.000; rank-1 buyer is AZ with streak 1; rank-1 seller is XA; buyer dominance is 18.92%; daily share of the dominant buyer is 1.62%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Enter only if price holds above prior close or reclaims intraday VWAP/support. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 543 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 28. MMIX — momentum_10d_hgb_aggressive

**Confidence:** Low-to-medium  
**Risk Grade:** Medium  
**Primary Score:** `score_momentum_10d__momentum_ranker__hgb__momentum_10d` = 0.408815  
**Risk Flags:** BELOW_EXECUTION_THRESHOLD  

**Trade thesis.** MMIX is selected by the **momentum_10d_hgb_aggressive** setup (cross-sectional momentum continuation). The primary model evidence is `score_momentum_10d__momentum_ranker__hgb__momentum_10d` at 0.409. The price/volume context indicates that price is trading above the 20-day mean, suggesting structure is still constructive relative to its recent base; 5-day return is 26.49%; 20-day return is 51.59%; 20-day volatility is 7.33%; volume participation is still thin with volume ratio 0.45. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.000; rank-1 buyer is XA with streak 1; rank-1 seller is XL; buyer dominance is 19.39%; daily share of the dominant buyer is 1.27%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Enter only if price holds above prior close or reclaims intraday VWAP/support. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 351 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 29. CUAN — position_xgb

**Confidence:** Low-to-medium  
**Risk Grade:** Medium-high  
**Primary Score:** `score_position__multi_strategy_time__xgb__position` = 0.497697  
**Risk Flags:** BELOW_EXECUTION_THRESHOLD  

**Trade thesis.** CUAN is selected by the **position_xgb** setup (position continuation / structural setup). The primary model evidence is `score_position__multi_strategy_time__xgb__position` at 0.498. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -34.62%; 20-day return is -30.89%; 20-day volatility is 8.70%; volume ratio is neutral at 1.34. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.003; rank-1 buyer is AK with streak 1; rank-1 seller is XL; buyer dominance is 13.53%; daily share of the dominant buyer is 1.97%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer close confirmation and stable liquidity rather than intraday spike. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 782 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 30. NICL — position_xgb

**Confidence:** Low-to-medium  
**Risk Grade:** Medium  
**Primary Score:** `score_position__multi_strategy_time__xgb__position` = 0.486211  
**Risk Flags:** BELOW_EXECUTION_THRESHOLD  

**Trade thesis.** NICL is selected by the **position_xgb** setup (position continuation / structural setup). The primary model evidence is `score_position__multi_strategy_time__xgb__position` at 0.486. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -15.08%; 20-day return is -13.64%; 20-day volatility is 4.52%; volume participation is still thin with volume ratio 0.31. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.009; rank-1 buyer is SH with streak 1; rank-1 seller is CP; buyer dominance is 11.55%; daily share of the dominant buyer is 0.35%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer close confirmation and stable liquidity rather than intraday spike. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 717 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

## Portfolio-Level Notes

Avoid forcing trades simply because a ticker appears in the report. Prioritize candidates whose thesis remains valid after the market opens, avoid concentration in the same dominant broker behaviour, and reduce exposure when multiple names depend on the same liquidity pattern. If market breadth weakens or volatility becomes abnormal, scale down position sizing or move signals to watchlist-only.