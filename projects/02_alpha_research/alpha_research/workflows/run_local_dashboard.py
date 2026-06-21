#!/usr/bin/env python3
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--port", type=int, default=8501)
    args = ap.parse_args()
    root = Path(args.root).resolve()
    app = root / "dashboards" / "local_research_dashboard.py"
    if not app.exists():
        raise FileNotFoundError(app)
    cmd = [
        sys.executable,
        "-m",
        "streamlit",
        "run",
        str(app),
        "--server.port",
        str(args.port),
        "--",
        "--root",
        str(root),
    ]
    subprocess.run(cmd, check=True)


if __name__ == "__main__":
    main()
w