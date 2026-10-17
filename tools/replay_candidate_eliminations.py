#!/usr/bin/env python3
"""Attach short official-Vampire replays to named historical eliminations.

This is optional evidence reconstruction, not an exhaustive lower-bound run.
Each subprocess has a process-group timeout as well as Vampire's own limit.
"""

import concurrent.futures
import json
import os
from pathlib import Path
import re
import signal
import subprocess

from candidate_index import ROOT, REPO, build


VAMPIRE = REPO / "vendor/vampire-5.0.1/bin/macos-arm64/vampire"


def replay(row):
    input_path = ROOT / "evidence" / (row["id"] + ".in")
    output_path = input_path.with_name(input_path.stem + "_vampire501.out")
    variables = sorted(set(re.findall(r"\b[A-Z][A-Za-z0-9_]*\b", row["tptp_ab"])))
    if row["system"] == "CD_CN":
        target = "t(i(i(n(P),P),P))" if row["labels"] == "c1914" else "t(i(P,i(n(P),Q)))"
    else:
        code = "cf" if row["system"] == "CD_CF" else "ct"
        target = json.loads((REPO / f"runs/{code}_definition.json").read_text())["counter_modeling_formulas"][0]
    target = row.get("target", target)
    target_variables = sorted(set(re.findall(r"\b[A-Z][A-Za-z0-9_]*\b", target)))
    input_path.write_text(
        f"% Individual elimination replay for {row['id']}; Polish {row['polish']}.\n"
        "fof(mp,axiom,![X,Y]: ((t(X) & t(i(X,Y))) => t(Y))).\n"
        + f"fof(candidate,axiom,![{','.join(variables)}]: t({row['tptp_ab']})).\n"
        + row.get("extra_axioms", "")
        + f"fof(classical_target,conjecture,![{','.join(target_variables)}]: {target}).\n"
    )
    command = [str(VAMPIRE), "--mode", "portfolio", "--schedule", "casc_sat", "--cores", "2", "--time_limit", "30", "--proof", "tptp", str(input_path.relative_to(REPO))]
    with output_path.open("w") as output:
        process = subprocess.Popen(command, cwd=REPO, stdout=output, stderr=subprocess.STDOUT, start_new_session=True)
        try:
            process.wait(timeout=40)
        except subprocess.TimeoutExpired:
            os.killpg(process.pid, signal.SIGTERM)
            try:
                process.wait(timeout=3)
            except subprocess.TimeoutExpired:
                os.killpg(process.pid, signal.SIGKILL)
                process.wait()
    text = output_path.read_text()
    ok = bool(re.search(r"SZS status (CounterSatisfiable|Satisfiable)\b", text))
    if ok:
        method = "finite Vampire countermodel" if "output start FiniteModel" in text else "completed Vampire saturation"
        row.update(method=method, evidence=str(output_path.relative_to(REPO)))
        row["note"] = "Official Vampire 5.0.1 confirms insufficiency. The adjacent .in file states CD, the candidate, and a classical target."
        if row.get("extra_axioms"):
            row["note"] += " Auxiliary equations restrict the model search; satisfiability with these extra constraints still supplies a countermodel to the unconstrained candidate/CD problem."
    return row, ok


def main():
    rows = json.loads((ROOT / "named_candidates.json").read_text())
    pending = [row for row in rows if "historical" in row["method"]]
    updated = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        for future in concurrent.futures.as_completed([pool.submit(replay, row) for row in pending]):
            row, ok = future.result()
            updated[row["id"]] = row
            print(row["id"], "confirmed" if ok else "unresolved replay", flush=True)
    rows = [updated.get(row["id"], row) for row in rows]
    (ROOT / "named_candidates.json").write_text(json.dumps(rows, indent=2) + "\n")
    build()


if __name__ == "__main__":
    main()
