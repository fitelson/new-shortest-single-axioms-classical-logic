#!/usr/bin/env python3
"""Bounded reconstruction tranche for the legacy C/f weight-17 exception."""

import concurrent.futures
import json
import os
from pathlib import Path
import signal
import subprocess


REPO = Path(__file__).resolve().parents[1]
EVIDENCE = REPO / "results/candidate_index/evidence"
VAMPIRE = REPO / "vendor/vampire-5.0.1/bin/macos-arm64/vampire"


def run_case(name, options, input_path):
    output_path = EVIDENCE / (name + ".out")
    command = [str(VAMPIRE), "--mode", "vampire", "--time_limit", "45", "--proof", "tptp", *options, str(input_path.relative_to(REPO))]
    with output_path.open("w") as output:
        process = subprocess.Popen(command, cwd=REPO, stdout=output, stderr=subprocess.STDOUT, start_new_session=True)
        try:
            process.wait(timeout=55)
        except subprocess.TimeoutExpired:
            os.killpg(process.pid, signal.SIGTERM)
            try:
                process.wait(timeout=3)
            except subprocess.TimeoutExpired:
                os.killpg(process.pid, signal.SIGKILL)
                process.wait()
    text = output_path.read_text()
    status = next((line for line in text.splitlines() if "SZS status" in line), "no decisive status")
    print(name, status, flush=True)
    return {"name": name, "command": command, "returncode": process.returncode, "status": status}


def main():
    original = EVIDENCE / "CD_CF17_legacy_exception.in"
    constrained = EVIDENCE / "CD_CF17_gap_falsum.in"
    constrained.write_text(original.read_text() + "fof(falsum_undesignated,axiom,~t(f)).\n")
    cases = []
    for algorithm in ["discount", "otter"]:
        for selection in [2, 3, 4, 10, 11, -10]:
            name = f"CD_CF17_gap_{algorithm}_{selection}"
            options = ["--saturation_algorithm", algorithm, "--selection", str(selection), "--age_weight_ratio", "1:4", "--symbol_precedence", "reverse_arity", "--backward_subsumption_resolution", "on"]
            cases.append((name, options, constrained))
    records = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        for future in concurrent.futures.as_completed([pool.submit(run_case, *case) for case in cases]):
            records.append(future.result())
    (EVIDENCE / "CD_CF17_reconstruction_tranche.json").write_text(json.dumps(records, indent=2) + "\n")


if __name__ == "__main__":
    main()
