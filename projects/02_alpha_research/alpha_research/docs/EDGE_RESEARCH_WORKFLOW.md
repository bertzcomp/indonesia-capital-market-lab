# Edge Research Workflow

Use `workflows/research_signal_edge.py` to test whether model scores or raw features contain measurable edge before promoting them into daily signal policy.

Two modes:

1. **Score edge** from validation/enriched panels:

```bash
python3 workflows/research_signal_edge.py \
  --root . \
  --score-panel signals/validation/continual_q3_2024_q1_2026_panel_enriched.parquet \
  --family momentum_ranker \
  --forward-start 2026-01-20 \
  --min-traded-value 500000000 \
  --require-broksum \
  --out-dir data/research/edge/continual_momentum_ranker_2026
```

2. **Feature edge** from labeled datasets:

```bash
python3 workflows/research_signal_edge.py \
  --root . \
  --dataset data/datasets/training/full_labeled.parquet \
  --family multi_strategy_time \
  --start-date 2024-07-01 \
  --end-date 2026-04-30 \
  --min-traded-value 500000000 \
  --require-broksum \
  --out-dir data/research/edge/full_labeled_multi_strategy_2024_2026
```

Outputs:

- `edge_summary.csv`: IC, quantile lift, best top-k metrics.
- `quantile_edge.csv`: bucket-by-bucket edge.
- `topk_edge.csv`: daily top-k simulation metrics.
- `edge_research_report.md`: markdown summary.
- `edge_research_meta.json`: reproducibility metadata.
