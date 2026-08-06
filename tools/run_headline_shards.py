#!/usr/bin/env python3
"""Run or display the reproducible two-shard headline search matrix."""

from __future__ import annotations

import argparse
import concurrent.futures
import json
from pathlib import Path
import shlex
import subprocess
import sys


REPO = Path(__file__).resolve().parents[1]
DEFAULT_MANIFEST = REPO / "runs" / "headline_reproduction_manifest.json"


def load_jobs(manifest_path: Path, selected: set[str]) -> tuple[dict, list[dict]]:
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    shard_count = manifest["shard_count"]
    prefix = manifest["run_prefix"]
    jobs = []
    for run in manifest["runs"]:
        if selected and run["label"] not in selected:
            continue
        for shard_index in range(shard_count):
            name = f"{prefix}_{run['label']}_V501_S{shard_index}"
            jobs.append({**run, "name": name, "shard_index": shard_index})
    return manifest, jobs


def command(job: dict, shard_count: int) -> list[str]:
    return [
        sys.executable,
        "run.py",
        job["name"],
        str(job["length"]),
        job["config"],
        "--model_namespace",
        job["model_namespace"],
        "--shard_index",
        str(job["shard_index"]),
        "--shard_count",
        str(shard_count),
    ]


def run_job(job: dict, shard_count: int, log_dir: Path) -> tuple[str, int]:
    log_path = log_dir / f"{job['name']}.log"
    with log_path.open("a", encoding="utf-8") as log:
        result = subprocess.run(
            command(job, shard_count),
            cwd=REPO,
            stdout=log,
            stderr=subprocess.STDOUT,
            check=False,
        )
    return job["name"], result.returncode


def merge_run(run: dict, shard_count: int, prefix: str) -> None:
    shard_names = [f"{prefix}_{run['label']}_V501_S{i}" for i in range(shard_count)]
    subprocess.run(
        [
            sys.executable,
            "tools/merge_shards.py",
            f"{prefix}_{run['label']}_V501",
            str(run["length"]),
            *shard_names,
        ],
        cwd=REPO,
        check=True,
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--only", nargs="*", default=[], help="Run labels, such as CN CF")
    parser.add_argument("--max_workers", type=int, default=14)
    parser.add_argument("--dry_run", action="store_true")
    args = parser.parse_args()

    selected = {label.upper() for label in args.only}
    manifest, jobs = load_jobs(args.manifest, selected)
    if selected - {job["label"] for job in jobs}:
        raise SystemExit("unknown run label: " + ", ".join(sorted(selected)))
    shard_count = manifest["shard_count"]

    if args.dry_run:
        for job in jobs:
            print(shlex.join(command(job, shard_count)))
        return

    log_dir = REPO / "run_logs" / "headline_v501"
    log_dir.mkdir(parents=True, exist_ok=True)
    failures = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.max_workers) as pool:
        futures = [pool.submit(run_job, job, shard_count, log_dir) for job in jobs]
        for future in concurrent.futures.as_completed(futures):
            name, returncode = future.result()
            print(f"{name}: exit {returncode}", flush=True)
            if returncode != 0:
                failures.append(name)
    if failures:
        raise SystemExit("failed shards: " + ", ".join(sorted(failures)))

    for run in manifest["runs"]:
        if not selected or run["label"] in selected:
            merge_run(run, shard_count, manifest["run_prefix"])


if __name__ == "__main__":
    main()
