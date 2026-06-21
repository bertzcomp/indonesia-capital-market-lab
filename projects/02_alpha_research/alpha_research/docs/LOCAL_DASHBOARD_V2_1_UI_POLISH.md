# Local Dashboard v2.1 UI Polish

This patch improves the visual system and usability of the Streamlit dashboard.

## Key improvements

- Cleaner sidebar with reduced visual noise
- Light/Dark CSS-driven theme toggle
- More consistent dashboard background and card surfaces
- More polished signal cards
- Better trading playbook layout
- Playbook sections are split into Thesis, Entry, Invalidation, Exit, No-Trade, and Context checks
- Raw card fields moved into a nested advanced expander
- Updated daily signal tabs with clearer visual labels

## Apply

```bash
unzip -o alpha_research_local_dashboard_v2_1_ui_patch.zip
```

## Run

```bash
python3 workflows/run_local_dashboard.py --root . --port 8501
```

