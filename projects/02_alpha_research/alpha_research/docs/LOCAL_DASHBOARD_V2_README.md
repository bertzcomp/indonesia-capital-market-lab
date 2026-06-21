# Alpha Research Local Dashboard v2

Dashboard v2 redesigns the Daily Signals page from a raw artifact viewer into a decision-intelligence interface.

## Run

```bash
pip install streamlit plotly pandas polars pyarrow
python3 workflows/run_local_dashboard.py --root . --port 8501
```

Open:

```text
http://localhost:8501
```

## Daily Signals v2

The Daily Signals page now uses a decision-first structure:

1. Today's Brief
2. Execute
3. Narrative Cards
4. Watchlists
5. Risk Review
6. Analytics
7. Data Health
8. Raw Data

## Narrative Report Support

If the selected signal folder contains:

```text
narrative_signal_cards.csv
narrative_signal_cards.json
narrative_trading_report.md
```

then the dashboard automatically promotes these files into first-class UI components:

- Market context smart cards
- Execution/narrative signal cards
- Trade thesis expanders
- Entry, invalidation, exit, no-trade playbook
- Risk flag breakdown
- Broker concentration review

## Philosophy

Raw CSV/JSON files are hidden by default. The dashboard prioritizes:

- decision summary
- actionable execution board
- narrative thesis
- risk and behavioural context
- progressive disclosure for raw data
