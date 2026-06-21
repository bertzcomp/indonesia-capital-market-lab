# Alpha Research Local Dashboard

This patch adds a local Streamlit dashboard for the reconstructed alpha research platform.

## Install dependencies

```bash
pip install streamlit plotly pandas polars pyarrow
```

## Run dashboard

From project root:

```bash
python3 workflows/run_local_dashboard.py --root . --port 8501
```

Then open:

```text
http://localhost:8501
```

Alternative direct command:

```bash
streamlit run dashboards/local_research_dashboard.py -- --root .
```

## Pages

- **Overview**: artifact health, history/live feature status, latest base scores.
- **Daily Signals**: inspect latest signal folder, main signals, execution shortlist, strategy watchlists, diagnostics, and report.
- **Live Scores**: score distribution and raw live base score table.
- **Evaluation**: backtest, forward test, random search, and Monte Carlo JSON viewers.
- **Registry & Policy**: inspect `configs/model_registry.json` and `configs/signal_policy.json`.
- **Data Coverage**: canonical raw table coverage.
- **Model Runs**: model run overview and training summary viewer.
- **Command Builder**: safe daily EOD command generator.

## Notes

The dashboard is read-only by default. It does not modify project artifacts.
