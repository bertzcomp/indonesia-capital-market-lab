import argparse
import json
from alpha_research.evaluation.backtest import build_validation_signal_panel


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', default='.')
    ap.add_argument('--run-id', default=None, help='Single run id or comma-separated run ids.')
    ap.add_argument('--run-ids', default=None, help='Comma-separated run ids. Overrides --run-id if provided.')
    ap.add_argument('--output', default=None)
    a = ap.parse_args()
    run_ids = a.run_ids or a.run_id
    if not run_ids:
        raise SystemExit('Provide --run-id or --run-ids')
    print(json.dumps(build_validation_signal_panel(a.root, run_ids, a.output), indent=2, default=str))


if __name__ == '__main__':
    main()
