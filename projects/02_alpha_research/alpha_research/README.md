# Alpha Research Rebuild v3

This is a from-scratch rebuild of the multi-strategy IDX/BEI quantitative ML research platform.

It is intentionally **not** a patch on top of legacy scripts. The platform is built around:

- canonical raw tables
- unified feature contract
- historical/live schema parity
- explicit model registry
- deterministic workflow entrypoints
- continual retraining as challenger, not auto-promotion

## Quick start

```bash
python3 -m pip install -e .
python3 workflows/validate_project_layout.py --root . --create
python3 workflows/build_canonical_raw.py --root . --start-date 2015-01-01 --end-date 2026-05-13
python3 workflows/build_feature_store.py --root . --scope history --start-date 2016-01-01 --end-date 2025-12-31
python3 workflows/build_feature_store.py --root . --scope live --start-date 2026-03-09 --end-date 2026-05-13
python3 workflows/build_training_dataset.py --root . --feature-scope history --start-date 2016-01-01 --end-date 2025-12-31
python3 workflows/build_folds.py --root . --freq year --fold-set yearly --first-val-year 2018 --last-val-year 2025
python3 workflows/train_models.py --root . --fold-set yearly --families sm_tracker,ara_predictor,multi_strategy_time --algos hgb,rank_hgb,regime_hgb
python3 workflows/build_model_registry.py --root . --run-id latest --output configs/model_registry.json
python3 workflows/run_daily_signal.py --root . --from-date 2026-03-09 --end-date 2026-05-13 --target-date 2026-05-18 --registry configs/model_registry.json --require-broksum
```

See `docs/END_TO_END_WORKFLOW.md` and `docs/DATA_CONTRACTS.md`.
