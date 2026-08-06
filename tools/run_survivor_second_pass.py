#!/usr/bin/env python3
"""Run the stronger, short parallel Vampire pass over merged survivors."""

from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import json
from pathlib import Path
import shlex
import sys


REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO))

from ModelTools import ConstantSpec, ModelSpec, OperationSpec, PredicateSpec  # noqa: E402
from TheoremProverUtils import VampireWrapper  # noqa: E402


DEFAULT_MANIFEST = REPO / "runs" / "headline_reproduction_manifest.json"


def load_config(config_path: Path) -> tuple[ModelSpec, str]:
    config = json.loads(config_path.read_text(encoding="utf-8"))
    spec = ModelSpec(
        PredicateSpec.parse(config["predicate"]),
        tuple(OperationSpec.parse(item) for item in config["operators"]),
        tuple(ConstantSpec.parse(item) for item in config["constants"]),
    )
    return spec, "\n".join(config["vampire_template"]) + "\n"


def command_template(settings: dict) -> list[str]:
    return [
        "theorem_provers/vampire",
        "--time_limit",
        str(settings["time_limit_seconds"]),
        "--mode",
        "portfolio",
        "--schedule",
        "casc_sat",
        "--memory_limit",
        str(settings["memory_limit_mib"]),
        "--cores",
        str(settings["cores"]),
        "--fmb_start_size",
        str(settings["fmb_start_size"]),
        "--input_syntax",
        "tptp",
        "<candidate.in>",
    ]


def run_label(run: dict, settings: dict) -> tuple[str, int, dict[str, int]]:
    label = run["label"]
    length = run["length"]
    initial_name = f"{run['run_prefix']}_{label}_V501"
    ledger = (
        REPO
        / "Remaining"
        / initial_name
        / f"{initial_name}{length}Survivors.merged.jsonl"
    )
    if not ledger.exists():
        raise RuntimeError(f"initial-pass merged ledger does not exist: {ledger}")

    records = [json.loads(line) for line in ledger.read_text().splitlines() if line.strip()]
    output_dir = REPO / "second_pass_outputs" / label
    output_dir.mkdir(parents=True, exist_ok=True)
    outcome_ledger = output_dir / f"{label}{length}Outcomes.jsonl"
    completed = {}
    if outcome_ledger.exists():
        for line in outcome_ledger.read_text().splitlines():
            if line.strip():
                record = json.loads(line)
                completed[record["formula"]] = record

    spec, template = load_config(REPO / run["config"])
    second_pass_models = REPO / "CounterModels" / f"SECOND_PASS_{label}_V501"
    second_pass_models.mkdir(parents=True, exist_ok=True)
    wrapper = VampireWrapper(
        str(REPO / "theorem_provers" / "vampire"),
        template,
        str(second_pass_models),
        spec,
        verify_models=True,
        optional_args={
            "--time_limit": str(settings["time_limit_seconds"]),
            "--memory_limit": str(settings["memory_limit_mib"]),
            "--cores": str(settings["cores"]),
            "--fmb_start_size": str(settings["fmb_start_size"]),
        },
    )

    counts = {"proof": 0, "finite_model": 0, "saturated": 0, "unresolved": 0}
    for record in completed.values():
        counts[record["second_pass_outcome"]] += 1

    with outcome_ledger.open("a", encoding="utf-8") as sink:
        for record in records:
            formula = record["formula"]
            if formula in completed:
                continue
            wrapper(formula)
            outcome = wrapper.last_outcome or "unresolved"
            raw_output = wrapper.last_output or ""
            digest = hashlib.sha256(formula.encode("utf-8")).hexdigest()[:20]
            raw_path = output_dir / f"{digest}.out"
            raw_path.write_text(raw_output, encoding="utf-8")
            result = {
                "formula": formula,
                "initial_pass_outcome": record["outcome"],
                "second_pass_outcome": outcome,
                "raw_output": str(raw_path.relative_to(REPO)),
                "vampire_command": command_template(settings),
            }
            sink.write(json.dumps(result, sort_keys=True) + "\n")
            sink.flush()
            counts[outcome] += 1
            print(f"{label}: {outcome}: {formula}", flush=True)
    summary = {
        "label": label,
        "target_length": length,
        "initial_survivors": len(records),
        "second_pass_settings": settings,
        "outcomes": counts,
        "complete": sum(counts.values()) == len(records),
    }
    (output_dir / f"{label}{length}Summary.json").write_text(
        json.dumps(summary, indent=2) + "\n", encoding="utf-8"
    )
    return label, len(records), counts


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--only", nargs="*", default=[])
    parser.add_argument("--max_workers", type=int, default=2)
    parser.add_argument("--dry_run", action="store_true")
    args = parser.parse_args()

    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    settings = manifest["second_pass"]
    selected = {label.upper() for label in args.only}
    runs = [
        {**run, "run_prefix": manifest["run_prefix"]}
        for run in manifest["runs"]
        if not selected or run["label"] in selected
    ]
    if selected - {run["label"] for run in runs}:
        raise SystemExit("unknown run label: " + ", ".join(sorted(selected)))
    if args.dry_run:
        print(shlex.join(command_template(settings)))
        for run in runs:
            print(f"{run['label']}: merged survivors only")
        return

    with concurrent.futures.ThreadPoolExecutor(max_workers=args.max_workers) as pool:
        futures = [pool.submit(run_label, run, settings) for run in runs]
        for future in concurrent.futures.as_completed(futures):
            label, total, counts = future.result()
            print(f"{label}: {total} survivors, {counts}", flush=True)


if __name__ == "__main__":
    main()
