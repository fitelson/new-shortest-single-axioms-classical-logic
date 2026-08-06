#!/usr/bin/env python3
"""Merge and validate disjoint headline-search shard reports and ledgers."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
COUNTERS = (
    "structural_forms_completed",
    "candidate_instances_generated",
    "eliminated_by_target_truth_table",
    "target_tautologies",
    "eliminated_by_cached_countermodels",
    "candidates_reaching_vampire_stage",
    "vampire_calls",
    "vampire_proofs",
    "vampire_finite_models",
    "vampire_saturations",
    "vampire_unresolved",
    "eliminated_by_new_countermodels",
    "eliminated_by_saturation",
    "survivors_written",
)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output_name")
    parser.add_argument("target_length", type=int)
    parser.add_argument("shard_names", nargs="+")
    args = parser.parse_args()

    reports = []
    records = []
    for shard_name in args.shard_names:
        stats_path = REPO / "partial_run_saves" / f"{shard_name}{args.target_length}.stats.json"
        report = json.loads(stats_path.read_text())
        if not report["counters_reconcile"]:
            raise RuntimeError(f"non-reconciling shard: {stats_path}")
        reports.append(report)
        ledger = REPO / "Remaining" / shard_name / f"{shard_name}{args.target_length}Survivors.jsonl"
        if ledger.exists():
            records.extend(
                json.loads(line) for line in ledger.read_text().splitlines() if line.strip()
            )

    shard_count = reports[0]["shard_count"]
    if len(reports) != shard_count:
        raise RuntimeError(f"expected {shard_count} reports, received {len(reports)}")
    if {report["shard_index"] for report in reports} != set(range(shard_count)):
        raise RuntimeError("shard indices are not complete and disjoint")
    globals_structural = {report["global_expected_structural_forms"] for report in reports}
    globals_candidates = {report["global_expected_candidate_instances"] for report in reports}
    if len(globals_structural) != 1 or len(globals_candidates) != 1:
        raise RuntimeError("shards disagree about the global search space")

    merged = {
        "schema_version": 1,
        "run_name": args.output_name,
        "target_length": args.target_length,
        "merged_shards": args.shard_names,
        "global_expected_structural_forms": globals_structural.pop(),
        "global_expected_candidate_instances": globals_candidates.pop(),
    }
    for counter in COUNTERS:
        merged[counter] = sum(report[counter] for report in reports)
    merged["accounted_candidates"] = (
        merged["eliminated_by_target_truth_table"]
        + merged["eliminated_by_cached_countermodels"]
        + merged["eliminated_by_new_countermodels"]
        + merged["eliminated_by_saturation"]
        + merged["survivors_written"]
    )
    merged["counters_reconcile"] = (
        merged["candidate_instances_generated"] == merged["accounted_candidates"]
    )
    merged["structural_forms_complete"] = (
        merged["structural_forms_completed"] == merged["global_expected_structural_forms"]
    )
    merged["candidate_space_complete"] = (
        merged["candidate_instances_generated"] == merged["global_expected_candidate_instances"]
    )
    if not all(
        (
            merged["counters_reconcile"],
            merged["structural_forms_complete"],
            merged["candidate_space_complete"],
        )
    ):
        raise RuntimeError("merged shards do not constitute a complete reconciled search")

    unique_records = {
        (record["formula"], record["outcome"]): record for record in records
    }
    if len(unique_records) != len(records):
        raise RuntimeError("duplicate survivor records across shards")
    merged["survivor_records"] = len(records)

    stats_output = REPO / "partial_run_saves" / f"{args.output_name}{args.target_length}.merged.stats.json"
    stats_output.write_text(json.dumps(merged, indent=2) + "\n")
    ledger_dir = REPO / "Remaining" / args.output_name
    ledger_dir.mkdir(parents=True, exist_ok=True)
    ledger_output = ledger_dir / f"{args.output_name}{args.target_length}Survivors.merged.jsonl"
    ledger_output.write_text(
        "".join(json.dumps(record, sort_keys=True) + "\n" for record in records)
    )
    print(json.dumps(merged, indent=2))


if __name__ == "__main__":
    main()
