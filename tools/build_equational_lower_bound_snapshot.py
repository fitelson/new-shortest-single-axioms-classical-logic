#!/usr/bin/env python3
"""Build the machine-readable summary of the archived equational screens."""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
ROOT = REPO / "results" / "equational_lower_bounds"
STATS = ROOT / "stats"
SURVIVORS = ROOT / "survivors"

SIGNATURES = {
    "bacf_definition.json": ("BACF", "C/f", 17),
    "bacn_definition.json": ("BACN", "C/N", 17),
    "baan_definition.json": ("BAAN", "A/N", 20),
    "baon_definition.json": ("BAON", "O/N", 20),
}

SUM_FIELDS = (
    "candidate_instances_generated",
    "eliminated_by_target_truth_table",
    "eliminated_by_cached_countermodels",
    "eliminated_by_new_countermodels",
    "eliminated_by_saturation",
    "survivors_written",
    "vampire_proofs",
    "vampire_finite_models",
    "vampire_saturations",
    "vampire_unresolved",
)


def load_stats() -> list[tuple[Path, dict]]:
    rows = []
    for path in sorted(STATS.glob("*.stats.json")):
        rows.append((path, json.loads(path.read_text(encoding="utf-8"))))
    return rows


def ledger_files(signature_code: str, target_length: int) -> list[Path]:
    directory = SURVIVORS / signature_code
    return sorted(directory.glob(f"length{target_length}_shard*.jsonl"))


def ledger_rows(paths: list[Path]) -> int:
    return sum(
        1
        for path in paths
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    )


def main() -> None:
    grouped: dict[tuple[str, int], list[tuple[Path, dict]]] = defaultdict(list)
    for path, row in load_stats():
        config_name = Path(row["config_file"]).name
        if config_name not in SIGNATURES:
            raise RuntimeError(f"unknown run definition in {path}: {config_name}")
        signature_code = SIGNATURES[config_name][0]
        grouped[(signature_code, int(row["target_length"]))].append((path, row))

    runs = []
    for (signature_code, target_length), pairs in sorted(grouped.items()):
        _, signature, displayed_length = SIGNATURES[
            Path(pairs[0][1]["config_file"]).name
        ]
        pairs.sort(key=lambda pair: int(pair[1]["shard_index"]))
        rows = [row for _, row in pairs]
        shard_count = int(rows[0]["shard_count"])
        if len(rows) != shard_count:
            raise RuntimeError(
                f"{signature_code} length {target_length}: expected {shard_count} shards, "
                f"found {len(rows)}"
            )
        if [int(row["shard_index"]) for row in rows] != list(range(shard_count)):
            raise RuntimeError(f"non-contiguous shards for {signature_code} {target_length}")
        global_forms = int(rows[0]["global_expected_structural_forms"])
        global_candidates = int(rows[0]["global_expected_candidate_instances"])
        structural_forms = sum(int(row["structural_forms_completed"]) for row in rows)
        totals = {field: sum(int(row[field]) for row in rows) for field in SUM_FIELDS}
        counters_reconcile = all(bool(row["counters_reconcile"]) for row in rows)
        full_coverage = (
            structural_forms == global_forms
            and totals["candidate_instances_generated"] == global_candidates
        )
        ledgers = ledger_files(signature_code, target_length)
        saved_survivors = ledger_rows(ledgers)
        if saved_survivors != totals["survivors_written"]:
            raise RuntimeError(
                f"{signature_code} length {target_length}: stats record "
                f"{totals['survivors_written']} survivors but ledgers contain "
                f"{saved_survivors}"
            )
        runs.append(
            {
                "signature_code": signature_code,
                "signature": signature,
                "displayed_axiom_length": displayed_length,
                "target_length": target_length,
                "shard_count": shard_count,
                "stats_files": [path.name for path, _ in pairs],
                "survivor_files": [
                    str(path.relative_to(ROOT)) for path in ledgers
                ],
                "structural_forms": structural_forms,
                "candidate_instances": totals.pop("candidate_instances_generated"),
                **totals,
                "counters_reconcile": counters_reconcile,
                "full_structural_coverage": full_coverage,
            }
        )

    manifest = {
        "schema_version": 1,
        "length_convention": "all symbols in both terms plus one equality symbol",
        "reference_prover": {
            "name": "Vampire",
            "version": "5.0.1",
            "release_commit": "1b13eaf",
        },
        "runs": runs,
    }
    destination = ROOT / "manifest.json"
    destination.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {destination} with {len(runs)} completed length runs.")


if __name__ == "__main__":
    main()
