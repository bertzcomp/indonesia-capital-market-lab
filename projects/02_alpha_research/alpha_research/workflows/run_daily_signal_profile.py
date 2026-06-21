#!/usr/bin/env python3
"""Run live base scoring + daily signal using an explicit model profile.

v4 behavior:
- preserves existing profile subdirectories before run_daily_signal.py recreates the date folder;
- moves flat daily outputs to signals/daily/signal_<date>/<profile_output_subdir>/;
- optionally builds the ARA Watch Layer v3 inside that profile output directory.
"""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime
from pathlib import Path
from typing import Any


def _run(cmd: list[str], *, check: bool = True) -> subprocess.CompletedProcess:
    print("\n$ " + " ".join(cmd), flush=True)
    return subprocess.run(cmd, check=check)


def _load_profiles(root: Path) -> dict[str, Any]:
    profiles_path = root / "configs" / "signal_model_profiles.json"
    if not profiles_path.exists():
        raise SystemExit(f"Profile config not found: {profiles_path}")
    with profiles_path.open("r", encoding="utf-8") as f:
        return json.load(f)


def _load_profile(root: Path, profile_name: str, registry: str | None, signal_policy: str | None, output_subdir: str | None) -> dict[str, Any]:
    profiles = _load_profiles(root)
    p = profiles.get("profiles", {}).get(profile_name)
    if not p:
        available = sorted(profiles.get("profiles", {}).keys())
        raise SystemExit(f"Unknown profile={profile_name!r}. Available: {available}")
    return {
        "registry": registry or p["registry"],
        "signal_policy": signal_policy or p["signal_policy"],
        "output_subdir": output_subdir or p.get("output_subdir") or profile_name,
        "all_profile_subdirs": sorted({
            str(v.get("output_subdir"))
            for v in profiles.get("profiles", {}).values()
            if v.get("output_subdir")
        }),
    }


def _target_signal_dir(root: Path, target_date: str) -> Path:
    dt = datetime.strptime(target_date, "%Y-%m-%d")
    slug = dt.strftime("signal_%d_%b_%Y").lower()
    return root / "signals" / "daily" / slug


def _backup_existing_profile_subdirs(signal_dir: Path, profile_subdirs: list[str]) -> tuple[Path, dict[str, Path]]:
    tmp_root = Path(tempfile.mkdtemp(prefix="signal_profile_backup_"))
    backups: dict[str, Path] = {}
    if not signal_dir.exists():
        return tmp_root, backups
    for name in profile_subdirs:
        src = signal_dir / name
        if src.exists() and src.is_dir():
            dst = tmp_root / name
            shutil.copytree(src, dst)
            backups[name] = dst
    return tmp_root, backups


def _restore_profile_subdirs(signal_dir: Path, backups: dict[str, Path], current_output_subdir: str) -> list[str]:
    restored: list[str] = []
    signal_dir.mkdir(parents=True, exist_ok=True)
    for name, src in backups.items():
        if name == current_output_subdir:
            # Re-running same profile should replace that profile with the new output, not restore the old one.
            continue
        dst = signal_dir / name
        if dst.exists():
            shutil.rmtree(dst)
        shutil.copytree(src, dst)
        restored.append(name)
    return restored


def _move_generated_signal_output(signal_dir: Path, output_subdir: str, profile_subdirs: list[str], overwrite: bool = True) -> Path:
    if not signal_dir.exists():
        raise SystemExit(f"Daily signal directory was not created: {signal_dir}")

    target_dir = signal_dir / output_subdir
    if target_dir.exists() and overwrite:
        shutil.rmtree(target_dir)
    target_dir.mkdir(parents=True, exist_ok=True)

    reserved = set(profile_subdirs) | {output_subdir}
    moved: list[str] = []
    for child in sorted(signal_dir.iterdir(), key=lambda p: p.name):
        if child.name in reserved:
            continue
        dst = target_dir / child.name
        if dst.exists():
            if dst.is_dir():
                shutil.rmtree(dst)
            else:
                dst.unlink()
        shutil.move(str(child), str(dst))
        moved.append(child.name)

    meta = {
        "signal_dir": str(signal_dir),
        "profile_output_dir": str(target_dir),
        "output_subdir": output_subdir,
        "moved_items": moved,
        "profile_subdirs_reserved": sorted(reserved),
    }
    with (target_dir / "profile_output_meta.json").open("w", encoding="utf-8") as f:
        json.dump(meta, f, indent=2, ensure_ascii=False)

    print(json.dumps(meta, indent=2), flush=True)
    return target_dir


def main() -> None:
    ap = argparse.ArgumentParser(description="Run daily signal using named model registry/policy profile.")
    ap.add_argument("--root", default=".")
    ap.add_argument("--profile", default="champion", help="Profile name from configs/signal_model_profiles.json, e.g. base_model or continual_model.")
    ap.add_argument("--registry", default=None, help="Optional custom registry path. Overrides profile registry.")
    ap.add_argument("--signal-policy", default=None, help="Optional custom policy path. Overrides profile policy.")
    ap.add_argument("--output-subdir", default=None, help="Optional subdir under signals/daily/signal_<date>/.")
    ap.add_argument("--flat-output", action="store_true", help="Keep run_daily_signal.py output in the legacy flat signal_<date>/ directory.")
    ap.add_argument("--no-overwrite-profile-output", action="store_true", help="Do not delete an existing profile output subdir before moving new files.")
    ap.add_argument("--from-date", required=True)
    ap.add_argument("--end-date", required=True)
    ap.add_argument("--target-date", required=True)
    ap.add_argument("--feature-scope", default="live")
    ap.add_argument("--price-min", type=float, default=100)
    ap.add_argument("--price-max", type=float, default=1000)
    ap.add_argument("--min-traded-value", type=float, default=500000000)
    ap.add_argument("--require-broksum", action="store_true")
    ap.add_argument("--skip-base-scores", action="store_true", help="Skip build_live_base_scores and only run daily signal.")
    ap.add_argument("--skip-ara-watch-layer", action="store_true", help="Do not run workflows/build_ara_watch_layer.py after daily signal output is moved.")
    ap.add_argument("--ara-watch-policy", default="configs/ara_watch_policy.v3.json")
    ap.add_argument("--ara-watch-nonfatal", action="store_true", help="Warn instead of failing if the ARA watch layer errors.")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    profile = _load_profile(root, args.profile, args.registry, args.signal_policy, args.output_subdir)
    registry = profile["registry"]
    policy = profile["signal_policy"]
    output_subdir = profile["output_subdir"]
    signal_dir = _target_signal_dir(root, args.target_date)

    print(json.dumps({
        "profile": args.profile,
        "registry": registry,
        "signal_policy": policy,
        "output_subdir": output_subdir,
        "from_date": args.from_date,
        "end_date": args.end_date,
        "target_date": args.target_date,
        "skip_base_scores": args.skip_base_scores,
        "flat_output": args.flat_output,
        "skip_ara_watch_layer": args.skip_ara_watch_layer,
    }, indent=2), flush=True)

    backup_tmp, backups = _backup_existing_profile_subdirs(signal_dir, profile["all_profile_subdirs"])
    print(json.dumps({"backed_up_profile_subdirs": sorted(backups.keys()), "backup_tmp": str(backup_tmp)}, indent=2), flush=True)

    try:
        if not args.skip_base_scores:
            cmd = [
                sys.executable, "workflows/build_live_base_scores.py",
                "--root", str(root),
                "--feature-scope", args.feature_scope,
                "--registry", registry,
                "--from-date", args.from_date,
                "--end-date", args.end_date,
                "--price-min", str(args.price_min),
                "--price-max", str(args.price_max),
                "--min-traded-value", str(args.min_traded_value),
            ]
            if args.require_broksum:
                cmd.append("--require-broksum")
            _run(cmd)

        cmd = [
            sys.executable, "workflows/run_daily_signal.py",
            "--root", str(root),
            "--from-date", args.from_date,
            "--end-date", args.end_date,
            "--target-date", args.target_date,
            "--registry", registry,
            "--signal-policy", policy,
            "--price-min", str(args.price_min),
            "--price-max", str(args.price_max),
            "--min-traded-value", str(args.min_traded_value),
            "--skip-base-scores",
        ]
        if args.require_broksum:
            cmd.append("--require-broksum")
        _run(cmd)

        profile_output_dir = signal_dir
        if not args.flat_output:
            profile_output_dir = _move_generated_signal_output(
                signal_dir=signal_dir,
                output_subdir=output_subdir,
                profile_subdirs=profile["all_profile_subdirs"],
                overwrite=not args.no_overwrite_profile_output,
            )
            restored = _restore_profile_subdirs(signal_dir, backups, current_output_subdir=output_subdir)
            print(json.dumps({"restored_profile_subdirs": restored}, indent=2), flush=True)

        if not args.skip_ara_watch_layer:
            ara_cmd = [
                sys.executable, "workflows/build_ara_watch_layer.py",
                "--signal-dir", str(profile_output_dir),
                "--policy", args.ara_watch_policy,
            ]
            res = _run(ara_cmd, check=not args.ara_watch_nonfatal)
            if args.ara_watch_nonfatal and res.returncode != 0:
                print(f"WARNING: ARA watch layer failed with returncode={res.returncode}", flush=True)
    finally:
        shutil.rmtree(backup_tmp, ignore_errors=True)


if __name__ == "__main__":
    main()
