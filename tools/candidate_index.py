#!/usr/bin/env python3
"""Build and search the archive's candidate-to-evidence index (standard library only).

Rebuild curated tables with ``build``.  ``import-project PATH`` also imports
the preserved development records; it does not run a prover or a search.
"""

from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import itertools
import json
from pathlib import Path
import re
import shutil
import sys
import tarfile


REPO = Path(__file__).resolve().parents[1]
ROOT = REPO / "results/candidate_index"
LETTERS = "pqrstuvwxyzabcdefghijklm"
LEGACY = {
    "CD_CN20": ("CN20Results/CN_20_CounterModels.txt", "CD_CN", 20),
    "CD_CF17": ("C017Results/C0_17_CounterModels.txt", "CD_CF", 17),
    "CD_CO17": ("C117Results/C1_17_CounterModels.txt", "CD_CO", 17),
}
FIELDS = (
    "id", "labels", "system", "weight", "polish", "tptp_ab", "tptp_xyz",
    "legacy_polish", "status", "method", "evidence", "note",
)


def parse_tptp(text: str):
    tokens = re.findall(r"[A-Za-z_][A-Za-z_0-9]*|[(),=]", text)
    position = 0

    def term():
        nonlocal position
        name = tokens[position]
        position += 1
        args = []
        if position < len(tokens) and tokens[position] == "(":
            position += 1
            while True:
                args.append(term())
                marker = tokens[position]
                position += 1
                if marker == ")":
                    break
                if marker != ",":
                    raise ValueError(f"unexpected token in {text}: {marker}")
        return name, tuple(args)

    node = term()
    if node[0] == "t":
        node = node[1][0]
    if position < len(tokens) and tokens[position] == "=":
        position += 1
        node = "=", (node, term())
    if position != len(tokens):
        raise ValueError(f"unparsed term suffix: {text}")
    return node


def parse_polish(text: str, system: str, *, legacy: bool = False):
    text = re.sub(r"\s+", "", text)
    position = 0
    arities = {"C": 2, "N": 1, "A": 2, "O": 2} if system.startswith("EQ_") else {"C": 2, "N": 1}

    def term():
        nonlocal position
        symbol = text[position]
        position += 1
        if system in {"CD_CF", "CD_CO"} and symbol in ({"O"} if legacy else ({"F", "f"} if system == "CD_CF" else {"O", "o"})):
            return ("f" if system == "CD_CF" else "o"), ()
        if symbol in arities:
            name = {"C": "i", "N": "n", "A": "a", "O": "o"}[symbol]
            return name, tuple(term() for _ in range(arities[symbol]))
        return "V" + symbol, ()

    node = term()
    if position < len(text) and text[position] == "=":
        position += 1
        node = "=", (node, term())
    if position != len(text):
        raise ValueError(f"unparsed Polish suffix: {text[position:]}")
    return node


def is_variable(node):
    return not node[1] and node[0] not in {"f", "o"}


def canonical(node):
    names = {}

    def visit(item):
        if is_variable(item):
            if item[0] not in names:
                names[item[0]] = len(names)
            return "v", names[item[0]]
        return item[0], tuple(visit(child) for child in item[1])

    return visit(node)


def spell(node, mode="polish", *, legacy=False):
    names = {}
    alphabet = "XYZUVWABCDEFGHIJKLMNOPQRST" if mode == "xyz" else "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def visit(item):
        name, args = item
        if is_variable(item):
            if name not in names:
                index = len(names)
                names[name] = str(index) if legacy else (LETTERS[index] if mode == "polish" else alphabet[index])
            return names[name]
        if not args:
            return ("O" if legacy else ("F" if name == "f" else "o")) if mode == "polish" else name
        if name == "=":
            return visit(args[0]) + "=" + visit(args[1])
        if mode == "polish":
            return {"i": "C", "n": "N", "a": "A", "o": "O"}[name] + "".join(visit(a) for a in args)
        return name + "(" + ",".join(visit(a) for a in args) + ")"

    return visit(node)


def weight(node):
    return 1 + sum(weight(a) for a in node[1])


def extract_assertion(line):
    start = line.index("t(") + 2
    depth = 0
    for position in range(start, len(line)):
        if line[position] == "(":
            depth += 1
        elif line[position] == ")":
            if depth == 0:
                return line[start:position]
            depth -= 1
    raise ValueError(f"unterminated assertion: {line}")


def source_copy(project, relative, target):
    source = project / relative
    target = ROOT / "evidence" / target
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists() and target.read_bytes() != source.read_bytes():
        raise ValueError(f"refusing to overwrite changed evidence: {target}")
    if not target.exists():
        shutil.copyfile(source, target)
    return str(target.relative_to(REPO))


def model_from_text(text):
    # Older Vampire outputs leave these domain atoms unquoted; later ones
    # quote them. Normalize their spelling without changing table entries.
    text = re.sub(r"'?(fmb_\$i_\d+)'?", r"'\1'", text)
    order = max(map(int, re.findall(r"fmb_\$i_(\d+)", text)))
    designated = [False] * order
    for negated, index in re.findall(r"(?<![A-Za-z_])(~?)t\('fmb_\$i_(\d+)'\)", text):
        designated[int(index) - 1] = not negated
    implication = [[None] * order for _ in range(order)]
    for x, y, z in re.findall(r"i\('fmb_\$i_(\d+)','fmb_\$i_(\d+)'\)\s*=\s*'fmb_\$i_(\d+)'", text):
        implication[int(x)-1][int(y)-1] = int(z)-1
    negation = [None] * order
    for x, y in re.findall(r"n\('fmb_\$i_(\d+)'\)\s*=\s*'fmb_\$i_(\d+)'", text):
        negation[int(x)-1] = int(y)-1
    if any(x is None for row in implication for x in row):
        raise ValueError("incomplete implication table")
    return {"order": order, "designated": designated, "i": implication, "n": negation, "constant": 0}


def stock_models(code):
    with tarfile.open(REPO / f"data/model_stocks/REPRO_{code}_V501.tar.gz") as archive:
        members = [m for m in archive.getmembers() if m.isfile() and m.name.endswith(".out")]
        members.sort(key=lambda m: (int(m.name.split("legacy-countermodel-")[-1].split("-")[0]), m.name))
        for member in members:
            stream = archive.extractfile(member)
            assert stream is not None
            text = stream.read().decode()
            yield member.name, text, model_from_text(text)


def holds(node, model):
    """Exact array evaluation; numpy is imported only by development import."""
    import numpy as np

    names = {}

    def register(item):
        if is_variable(item):
            names.setdefault(item[0], len(names))
        for arg in item[1]:
            register(arg)

    register(node)
    tables = {k: np.array(model[k]) for k in ["i", "n"]}

    def evaluate(item):
        name, args = item
        if is_variable(item):
            shape = [1] * len(names)
            shape[names[name]] = model["order"]
            return np.arange(model["order"]).reshape(shape)
        if not args:
            return model["constant"]
        values = [evaluate(a) for a in args]
        return tables[name][tuple(values)]

    values = evaluate(node)
    return bool(np.array(model["designated"])[values].all())


def verify_finite(node, model, target):
    """Independent, exhaustive scalar verification; no third-party packages."""
    domain = range(model["order"])
    designated = model["designated"]
    assert all(not (designated[x] and designated[model["i"][x][y]]) or designated[y] for x in domain for y in domain)

    def counterexample(formula):
        names = []

        def variables(item):
            if is_variable(item) and item[0] not in names:
                names.append(item[0])
            for child in item[1]:
                variables(child)

        variables(formula)

        def evaluate(item, assignment):
            name, args = item
            if is_variable(item):
                return assignment[name]
            if not args:
                return model["constant"]
            values = [evaluate(arg, assignment) for arg in args]
            return model["i"][values[0]][values[1]] if name == "i" else model["n"][values[0]]

        for values in itertools.product(domain, repeat=len(names)):
            assignment = dict(zip(names, values))
            result = evaluate(formula, assignment)
            if not designated[result]:
                return {"assignment": assignment, "value": result}
        return None

    assert counterexample(node) is None, "the model does not validate every instance of the candidate"
    witness = counterexample(target)
    assert witness is not None, "the model does not refute the stated classical target"
    return {"order": model["order"], "candidate_valid": True, "modus_ponens_valid": True, "target_counterexample": witness, "domain_numbering": "zero-based"}


def compact_model(text, system):
    order = int(text[0])
    cursor = 1
    designated = [value == "1" for value in text[cursor:cursor+order]]
    cursor += order
    table = [int(value) for value in text[cursor:cursor+order*order]]
    cursor += order*order
    negation = [int(value) for value in text[cursor:cursor+order]] if system == "CD_CN" else [None]*order
    if system == "CD_CN":
        cursor += order
    assert cursor == len(text), "malformed compact legacy model"
    return {"order": order, "designated": designated, "i": [table[i*order:(i+1)*order] for i in range(order)], "n": negation, "constant": 0}


def classical_target(system):
    code = {"CD_CN": "cn", "CD_CF": "cf", "CD_CO": "ct"}[system]
    return parse_tptp(json.loads((REPO / f"runs/{code}_definition.json").read_text())["counter_modeling_formulas"][0])


def record(identifier, system, node, labels, status, method, evidence="", note=""):
    return dict(zip(FIELDS, [identifier, labels, system, weight(node), spell(node), spell(node, "ab"), spell(node, "xyz"), spell(node, legacy=True), status, method, evidence, note]))


def import_project(project):
    ROOT.mkdir(parents=True, exist_ok=True)
    existing = ROOT / "named_candidates.json"
    if existing.exists():
        # Preserve later certificate recovery and label corrections.
        import_ledgers(project, json.loads(existing.read_text()))
        build()
        return
    rows = []
    cn_source = "problems/condensed_detachment/classical_implication_negation/meredith_CN_19_ruling_out.in"
    cn_snapshot = source_copy(project, cn_source, "CN19_development_notes.in")
    seen = set()
    occurrences = {}
    for line in (project / cn_source).read_text().splitlines():
        match = re.search(r"fof\((c19\d+),\s*axiom", line)
        if not match:
            continue
        node = parse_tptp(extract_assertion(line))
        key = canonical(node)
        if key in seen:
            continue
        seen.add(key)
        label = match[1]
        occurrences[label] = occurrences.get(label, 0) + 1
        identifier = "CD_CN19_" + label + ("b" if occurrences[label] > 1 else "")
        method = "historical finite-model report" if "(sat)" in line or "Paradox" in line else "historical countersatisfiability report"
        rows.append(record(identifier, "CD_CN", node, label, "eliminated", method, cn_snapshot, "The development notes use c1918 for two different formulas; use the formula or stable row ID to distinguish them." if label == "c1918" else ""))
    original = [
        ("legacy_O1", "CD_CN", "CCCpqCCrNsCtNtCCtpCrp", "O1 (2021); O_1", "open", "unresolved same-length classification"),
        ("legacy_O2", "CD_CF", "CCCpqrCCCCsftCrpCsp", "O2 (2021); O_2", "open", "unresolved same-length classification"),
        ("legacy_O3", "CD_CO", "CCpCqrCCCrsCoqCtCpr", "O3 (2021); O_3", "open", "unresolved same-length classification"),
        ("O4", "CD_CO", "CCCpqCorCsCCrpCtp", "O4 (2021 and AJL); O_4", "open", "unresolved lower-bound candidate"),
        ("legacy_O5", "CD_CO", "CCCpqrCCrCoCrpCsp", "O5 (2021); old O5; legacy O_5", "eliminated", "completed Vampire saturation"),
        ("O5", "CD_CO", "CCpqCrCCCqsCopCtq", "O5 (AJL); O6 (2021); legacy O_6", "eliminated", "seven-element countermodel (Appendix B)"),
        ("cand102", "CD_CN", "CCCpNqrCCCCsNstCrqCsq", "cand102; CN weight-21 open example", "open", "unresolved same-length classification"),
    ]
    for identifier, system, formula, labels, status, method in original:
        rows.append(record(identifier, system, parse_polish(formula, system), labels, status, method))
    # Four non-model cases in the complete legacy C/N weight-20 table.
    cn20 = project / "code/legacy_walsh_search/Results/CN20Results/specialcases"
    for number, formula in enumerate((cn20 / "CN_20_Remaining.txt").read_text().splitlines(), 1):
        node = parse_polish(formula, "CD_CN", legacy=True)
        evidence = source_copy(project, str((cn20 / (formula + ".out")).relative_to(project)), f"CN20_exception_{number:02d}_vampire451.out")
        text = (ROOT / "evidence" / f"CN20_exception_{number:02d}_vampire451.out").read_text()
        if "SZS status CounterSatisfiable" not in text:
            raise ValueError(f"no successful status in {evidence}")
        method = "finite Vampire model" if "output start FiniteModel" in text else "completed Vampire saturation"
        rows.append(record(f"CD_CN20_exception_{number:02d}", "CD_CN", node, formula, "eliminated", method, evidence, "The retained transcript includes unsuccessful portfolio slices followed by the successful CounterSatisfiable result."))
    missing_cf = "CCCCC01O23CC30C40"
    rows.append(record("CD_CF17_legacy_exception", "CD_CF", parse_polish(missing_cf, "CD_CF", legacy=True), missing_cf + "; F17; F_17; F_{17}", "open", "unresolved weight-17 C/f lower-bound candidate", note="No definitive elimination certificate is available. This case prevents a proved-shortest claim for the 19-symbol CD C/f axioms; the separate equational C/f result is unaffected."))
    ct_remaining = project / "code/legacy_walsh_search/Results/C117Results/specialcases/C1_17_Remaning.txt"
    for number, formula in enumerate(ct_remaining.read_text().splitlines(), 1):
        node = parse_polish(formula, "CD_CO", legacy=True)
        if not any(r["system"] == "CD_CO" and canonical(parse_tptp(r["tptp_ab"])) == canonical(node) for r in rows):
            rows.append(record(f"CD_CO17_legacy_exception_{number:02d}", "CD_CO", node, formula, "eliminated", "historical elimination; witness lookup pending"))
    source_copy(project, "problems/condensed_detachment/implication_constants/C_o_17_symbol_candidate_O5_vampire_saturation.txt", "legacy_O5_historical_saturation.in")
    source_copy(project, "problems/condensed_detachment/implication_constants/C_o_17_symbol_candidate_O6_countermodel_verification.py", "O5_AJL_legacy_O6_countermodel_verification.py")
    source_copy(project, "problems/condensed_detachment/classical_implication_negation/cn19_chain_verification.py", "CN19_chain_verification.py")
    # Associate candidates with an exact model from the already archived stocks.
    for code, system, config in [("CN", "CD_CN", "cn"), ("CF", "CD_CF", "cf"), ("CT", "CD_CO", "ct")]:
        todo = [r for r in rows if r["system"] == system and r["status"] == "eliminated" and ("historical" in r["method"])]
        target = parse_tptp(json.loads((REPO / f"runs/{config}_definition.json").read_text())["counter_modeling_formulas"][0])
        for filename, text, model in stock_models(code):
            if not todo:
                break
            for row in todo[:]:
                if holds(parse_tptp(row["tptp_ab"]), model):
                    assert not holds(target, model), filename
                    assert all(not (model["designated"][x] and model["designated"][model["i"][x][y]]) or model["designated"][y] for x in range(model["order"]) for y in range(model["order"]))
                    destination = ROOT / "evidence" / (row["id"] + "_countermodel.out")
                    destination.write_text(text)
                    row["method"] = f"{model['order']}-element countermodel"
                    row["evidence"] = str(destination.relative_to(REPO))
                    row["note"] += f" Exact evaluation verifies the candidate, modus ponens, and failure of the classical target in runs/{config}_definition.json. Source stock: {filename}."
                    todo.remove(row)
        for row in todo:
            if row["labels"] == "c1913":
                row.update(method="syntactic infinite-chain proof (Appendix A)", evidence="results/candidate_index/evidence/CN19_chain_verification.py", note="The proof is in Appendix A; the script checks its recurrence and finite examples, and is not a replacement for the induction.")
            else:
                row["note"] += " Historical result retained; an individual model or successful transcript still needs to be attached."
    for row in rows:
        if row["id"] == "legacy_O5":
            row.update(evidence="results/candidate_index/evidence/legacy_O5_vampire501.out", note="Fresh official Vampire 5.0.1 replay returns CounterSatisfiable with Saturation. Input: results/candidate_index/evidence/legacy_O5.in. This is not AJL O5.")
        elif row["id"] == "O5":
            row.update(evidence="results/candidate_index/evidence/O5_AJL_legacy_O6_countermodel_verification.py", note="AJL Appendix B; designated set {3,6}, o=3; refutes L4. Historical working files call this O6.")
        elif row["id"] == "O4":
            row["note"] = "Only remaining weight-17 C/o lower-bound candidate; no elimination is claimed."
    (ROOT / "named_candidates.json").write_text(json.dumps(rows, indent=2) + "\n")
    import_ledgers(project, rows)
    build()


def import_ledgers(project, rows):
    old_manifest = ROOT / "legacy_manifest.json"
    manifests = ([r for r in json.loads(old_manifest.read_text())
                  if r["dataset"] not in LEGACY] if old_manifest.exists() else [])
    for name, (source_relative, system, size) in LEGACY.items():
        source = project / "code/legacy_walsh_search/Results" / source_relative
        destination = ROOT / "legacy" / (name + ".tsv.gz")
        destination.parent.mkdir(parents=True, exist_ok=True)
        digest = hashlib.sha256()
        total = models = 0
        exceptions = []
        with source.open("rb") as source_stream, destination.open("wb") as out:
            with gzip.GzipFile(filename="", mode="wb", fileobj=out, mtime=0, compresslevel=6) as zipped:
                zipped.write(b"legacy_polish\tmethod\tcompact_countermodel\tevidence_id\n")
                for total, raw in enumerate(source_stream, 1):
                    digest.update(raw)
                    formula, sep, model = raw.decode().strip().partition(":")
                    if sep and model:
                        models += 1
                        line = f"{formula}\tfinite countermodel\t{model}\t\n"
                    else:
                        key = canonical(parse_polish(formula, system, legacy=True))
                        candidates = [r for r in rows if r["system"] == system and canonical(parse_tptp(r["tptp_ab"])) == key]
                        if len(candidates) != 1:
                            raise ValueError(f"cannot map legacy exception: {name} {formula}")
                        row = candidates[0]
                        line = f"{formula}\tsee named candidate\t\t{row['id']}\n"
                        exceptions.append({"line": total, "formula": formula, "id": row["id"]})
                    zipped.write(line.encode())
        manifests.append({"dataset": name, "system": system, "weight": size, "file": str(destination.relative_to(REPO)), "source": "code/legacy_walsh_search/Results/" + source_relative, "source_sha256": digest.hexdigest(), "rows": total, "finite_model_rows": models, "exceptions": exceptions})
        print(f"Imported {name}: {total:,} rows; {models:,} finite-model assignments", flush=True)
    (ROOT / "legacy_manifest.json").write_text(json.dumps(manifests, indent=2) + "\n")


def write_tsv(path, fields, rows):
    with path.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def refresh_legacy_links():
    """Keep exception methods in the named table, without copying stale labels."""
    for name in LEGACY:
        path = ROOT / "legacy" / (name + ".tsv.gz")
        temporary = path.with_suffix(".refresh")
        with gzip.open(path, "rt") as source, temporary.open("wb") as destination:
            with gzip.GzipFile(filename="", mode="wb", fileobj=destination, mtime=0, compresslevel=6) as zipped:
                for line in source:
                    columns = line.rstrip("\n").split("\t")
                    if len(columns) == 4 and columns[3] and columns[3] != "evidence_id":
                        columns[1] = "see named candidate"
                        line = "\t".join(columns) + "\n"
                    zipped.write(line.encode())
        temporary.replace(path)
        print(f"Refreshed exception links in {name}", flush=True)


def import_same_length(project):
    """Export the saved general-filter lists without inventing current verdicts."""
    sources = [
        ("CD_CN", 21, "CN21Results", "CN_21_Remaining.txt", 782),
        ("CD_CF", 19, "C019Results", "C0_19_Remaining.txt", 162),
        ("CD_CO", 19, "C119Results", "C1_19_Remaning.txt", 188),
    ]
    directory = ROOT / "same_length"
    directory.mkdir(parents=True, exist_ok=True)
    rows = []
    overview = ["# Preserved same-length general-filter survivors", "", "These historical lists contain candidates surviving the original general filters at the lengths of the displayed CD axioms. They include formulas subsequently proved sufficient; membership is not a current unresolved verdict. For current statuses of named examples use [named_candidates.md](../named_candidates.md).", "", "The combined [same_length_candidates.tsv](../same_length_candidates.tsv) supplies ordinary Polish and parenthesized TPTP alongside the original digit-variable notation.", "", "| System | Weight | Historical rows | Exact saved list |", "|---|---:|---:|---|"]
    for system, size, folder, filename, expected in sources:
        source = project / "code/legacy_walsh_search/Results" / folder / "specialcases" / filename
        destination = directory / f"{system}_{size}_legacy.txt"
        if destination.exists() and destination.read_bytes() != source.read_bytes():
            raise ValueError(f"refusing to overwrite changed source snapshot: {destination}")
        if not destination.exists():
            shutil.copyfile(source, destination)
        formulas = [(n, line.strip()) for n, line in enumerate(source.read_text().splitlines(), 1) if line.strip()]
        assert len(formulas) == expected, source
        for number, formula in formulas:
            node = parse_polish(formula, system, legacy=True)
            assert weight(node) == size, (source, number)
            rows.append(record(f"{system}_{size}_legacy_{number:04d}", system, node, "", "historical general-filter survivor", "no current classification asserted by this historical list", str(destination.relative_to(REPO)) + f"#L{number}", "Original source: code/legacy_walsh_search/Results/" + folder + "/specialcases/" + filename))
        overview.append(f"| {system} | {size} | {len(formulas)} | [{destination.name}]({destination.name}) |")
    write_tsv(ROOT / "same_length_candidates.tsv", FIELDS, rows)
    (directory / "README.md").write_text("\n".join(overview) + "\n")
    print(f"Exported {len(rows)} historical same-length candidates; no prover or model finder was launched.")


def build():
    rows = json.loads((ROOT / "named_candidates.json").read_text())
    write_tsv(ROOT / "named_candidates.tsv", FIELDS, rows)
    lines = ["# Named candidates and individual elimination evidence", "", "Both paper and legacy labels are listed. `O5 (2021)` and `O5 (AJL)` are different formulas. All formulas below are searchable in Polish and in parenthesized TPTP notation in [named_candidates.tsv](named_candidates.tsv).", "", "| Stable ID / labels | System / weight | Polish formula | Status / method | Evidence |", "|---|---|---|---|---|"]
    for row in rows:
        evidence = row["evidence"]
        link = ""
        if evidence:
            link = "[record](" + str(Path(evidence).relative_to("results/candidate_index")) + ")" if evidence.startswith("results/candidate_index/") else evidence
        no_record = "Open; no elimination claimed" if row["status"] == "open" else "Historical certificate not recovered"
        lines.append(f"| <a id=\"{row['id']}\"></a>`{row['id']}`; {row['labels']} | {row['system']} / {row['weight']} | `{row['polish']}` | {row['status']}: {row['method']} | {link or no_record} |")
    lines += ["", "## Notes and provenance", ""]
    for row in rows:
        if row["note"]:
            lines.append(f"- **{row['id']}:** {row['note'].strip()}")
    (ROOT / "named_candidates.md").write_text("\n".join(lines) + "\n")
    summaries = []
    survivors = []
    manifest_root = REPO / "results/equational_lower_bounds"
    for run in json.loads((manifest_root / "manifest.json").read_text())["runs"]:
        if run["signature_code"] == "BAAN":
            continue
        summaries.append({k: run[k] for k in ["signature_code", "target_length", "candidate_instances", "eliminated_by_target_truth_table", "eliminated_by_cached_countermodels", "eliminated_by_new_countermodels", "eliminated_by_saturation", "survivors_written"]})
        for relative in run["survivor_files"]:
            path = manifest_root / relative
            for number, raw in enumerate(path.read_text().splitlines(), 1):
                if not raw.strip():
                    continue
                item = json.loads(raw)
                system = "EQ_" + {"BACN": "CN", "BAON": "ON"}[run["signature_code"]]
                node = parse_tptp(item["formula"])
                shard = re.search(r"shard(\d+)", path.name)[1]
                identifier = f"{system}_{run['target_length']}_s{shard}_{item['candidate_number']:04d}"
                survivors.append(record(identifier, system, node, "", "open", "unresolved survivor; no elimination claimed", str(path.relative_to(REPO)) + f"#L{number}", "A/N candidates are obtained from O/N by Boolean duality; the older independent A/N screen is historical data and uses a different target basis." if system == "EQ_ON" else ""))
    write_tsv(ROOT / "equational_screen_summary.tsv", list(summaries[0]), summaries)
    write_tsv(ROOT / "equational_survivors.tsv", FIELDS, survivors)
    eq = ["# Equational elimination totals and unresolved candidates", "", "These are the paper's C/f, C/N, and O/N screens. A/N follows by duality. The archived independent A/N screen used a different target basis and is not substituted for the dual O/N results.", "", "Individual eliminated-equation outcomes were not preserved by the historical instrumentation. The table gives the actual aggregate method counts; it does not invent per-formula attribution. Every unresolved formula is individually listed in [equational_survivors.tsv](equational_survivors.tsv).", "", "| System | Weight | Generated | Truth table | Cached model | New model | Saturation | Unresolved |", "|---|---:|---:|---:|---:|---:|---:|---:|"]
    for row in summaries:
        eq.append("| " + " | ".join(str(v) for v in row.values()) + " |")
    eq += ["", "The source reports and exact survivor lists are under [equational_lower_bounds](../equational_lower_bounds/README.md). `manifest.json` supplies the statistics filenames for each row. A timeout is unresolved, not an elimination.", "", "## Individual unresolved formulas", "", "| Stable ID | System / weight | Polish | TPTP | Source ledger |", "|---|---|---|---|---|"]
    for row in survivors:
        eq.append(f"| `{row['id']}` | {row['system']} / {row['weight']} | `{row['polish']}` | `{row['tptp_ab']}` | [row](../../{row['evidence']}) |")
    (ROOT / "equational_candidates.md").write_text("\n".join(eq) + "\n")
    check()


def check():
    rows = json.loads((ROOT / "named_candidates.json").read_text())
    assert len({row["id"] for row in rows}) == len(rows)
    for row in rows:
        node = parse_tptp(row["tptp_ab"])
        assert weight(node) == row["weight"], row["id"]
        assert canonical(parse_tptp(row["tptp_xyz"])) == canonical(node)
        assert canonical(parse_polish(row["polish"], row["system"])) == canonical(node)
        assert canonical(parse_polish(row["legacy_polish"], row["system"], legacy=True)) == canonical(node)
        if row["evidence"]:
            assert (REPO / row["evidence"]).is_file(), row["evidence"]
            if row["evidence"].endswith("_countermodel.out") or row["id"] == "CD_CN19_c1914":
                model = model_from_text((REPO / row["evidence"]).read_text())
                verify_finite(node, model, classical_target(row["system"]))
            elif row["method"] in {"completed Vampire saturation", "finite Vampire model", "finite Vampire countermodel"}:
                output = (REPO / row["evidence"]).read_text()
                assert re.search(r"SZS status (CounterSatisfiable|Satisfiable)\b", output), row["id"]
        if row["status"] == "eliminated":
            assert row["evidence"], f"elimination without evidence: {row['id']}"
    old = next(row for row in rows if row["id"] == "legacy_O5")
    text = (REPO / old["evidence"]).read_text()
    assert "Vampire 5.0.1" in text and "SZS status CounterSatisfiable" in text and "output start Saturation" in text
    with (ROOT / "equational_survivors.tsv").open() as stream:
        survivors = list(csv.DictReader(stream, delimiter="\t"))
    assert sum(row["system"] == "EQ_CN" for row in survivors) == 23
    assert sum(row["system"] == "EQ_ON" for row in survivors) == 351
    for row in survivors:
        assert (REPO / row["evidence"].split("#")[0]).is_file()
        node = parse_tptp(row["tptp_ab"])
        assert weight(node) == int(row["weight"])
        assert canonical(parse_polish(row["polish"], row["system"])) == canonical(node)
    import verify_candidate_reductions
    reductions = verify_candidate_reductions.verify()
    assert reductions == json.loads((ROOT / "reduction_checks.json").read_text())
    co_survivors = set()
    for shard in (0, 1):
        stats = json.loads((ROOT / f"evidence/CO17_instance_stats_shard{shard}.json").read_text())
        assert stats["target_length"] == 17 and stats["counters_reconcile"]
        assert stats["structural_forms_completed"] == stats["expected_structural_forms"]
        ledger = (ROOT / f"evidence/CO17_instance_survivors_shard{shard}.jsonl").read_text().splitlines()
        assert len(ledger) == stats["survivors_written"] == 2
        co_survivors.update(canonical(parse_tptp(json.loads(raw)["formula"])) for raw in ledger)
    assert co_survivors == {canonical(parse_tptp(r["tptp_ab"])) for r in rows if r["id"] in {"O4", "O4_ident_t_s", "O5", "O5_ident_t_r"}}
    padding_path = ROOT / "cn19_padding_exceptions.json"
    if padding_path.exists():
        padding = json.loads(padding_path.read_text())
        assert len(padding) == 77
        assert sum("output_sha256" in r for r in padding) == 59
        by_id = {r["id"]: r for r in rows}
        for item in padding:
            p = item["padded"]
            assert len(p) == 21 and p[0] == "C" and p[1].isdigit() and p[1] not in p[2:]
            tail = parse_polish(p[2:], "CD_CN", legacy=True)
            assert spell(tail, legacy=True) == item["stripped_legacy_polish"]
            assert (REPO / item["evidence"]).is_file(), item["id"]
            if "output_sha256" in item:
                output = (REPO / item["evidence"]).read_bytes()
                assert hashlib.sha256(output).hexdigest() == item["output_sha256"]
                assert b"SZS status CounterSatisfiable" in output
                if item["method"] == "finite model":
                    verify_finite(tail, model_from_text(output.decode()), classical_target("CD_CN"))
            else:
                assert by_id[item["named_candidate"]]["legacy_polish"] == item["stripped_legacy_polish"]
    print(f"Checked {len(rows)} named rows, {len(survivors)} equational survivors, and the legacy-O5 replay.")


def lookup(query, system, verify=False):
    rows = json.loads((ROOT / "named_candidates.json").read_text())
    with (ROOT / "equational_survivors.tsv").open() as stream:
        rows += list(csv.DictReader(stream, delimiter="\t"))
    historical = ROOT / "same_length_candidates.tsv"
    if historical.exists():
        with historical.open() as stream:
            rows += list(csv.DictReader(stream, delimiter="\t"))
    named = [r for r in rows if query.lower() == r["id"].lower() or query.lower() in [x.strip().lower() for x in r["labels"].split(";")]]
    def report(matches):
        if verify:
            for item in matches:
                evidence = item["evidence"]
                if evidence.endswith("_countermodel.out") or item["id"] == "CD_CN19_c1914":
                    item["verification"] = verify_finite(parse_tptp(item["tptp_ab"]), model_from_text((REPO / evidence).read_text()), classical_target(item["system"]))
        print(json.dumps(matches, indent=2))

    if named:
        report(named)
        return
    if not system:
        raise ValueError("For formula lookup, give --system CD_CN, CD_CF, CD_CO, EQ_CN, or EQ_ON; labels such as legacy_O5 need no system.")
    node = parse_tptp(query) if "(" in query else parse_polish(query, system)
    key = canonical(node)
    matches = [r for r in rows if r["system"] == system and canonical(parse_tptp(r["tptp_ab"])) == key]
    if matches:
        current = [r for r in matches if r["status"] != "historical general-filter survivor"]
        matches = current or matches
        report(matches)
        return
    legacy_query = spell(node, legacy=True)
    for name, (_, candidate_system, size) in LEGACY.items():
        if system != candidate_system or weight(node) != size:
            continue
        with gzip.open(ROOT / "legacy" / (name + ".tsv.gz"), "rt") as stream:
            for number, row in enumerate(csv.DictReader(stream, delimiter="\t"), 1):
                if row["legacy_polish"] == legacy_query:
                    result = {"dataset": name, "candidate_row": number, **row}
                    if verify and row["compact_countermodel"]:
                        result["verification"] = verify_finite(node, compact_model(row["compact_countermodel"], system), classical_target(system))
                    if row["evidence_id"]:
                        result["named_candidate"] = next(r for r in rows if r["id"] == row["evidence_id"])
                    print(json.dumps(result, indent=2))
                    return
    padding_table = ROOT / "legacy/CD_CN19_from_CN21.tsv.gz"
    if system == "CD_CN" and weight(node) == 19 and padding_table.exists():
        with gzip.open(padding_table, "rt") as stream:
            for number, row in enumerate(csv.DictReader(stream, delimiter="\t"), 1):
                if row["legacy_polish"] != legacy_query:
                    continue
                result = {"dataset": "CD_CN19_from_CN21", "candidate_row": number, **row}
                if verify and row["compact_countermodel"]:
                    result["verification"] = verify_finite(node, compact_model(row["compact_countermodel"], system), classical_target(system))
                if row["evidence_id"]:
                    result["padding_exception"] = next(r for r in json.loads((ROOT / "cn19_padding_exceptions.json").read_text()) if r["id"] == row["evidence_id"])
                print(json.dumps(result, indent=2))
                return
    print("No individual record in the indexed datasets; this is not an elimination result.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("build")
    sub.add_parser("check")
    sub.add_parser("refresh-legacy-links")
    imp = sub.add_parser("import-project")
    imp.add_argument("project", type=Path)
    same = sub.add_parser("import-same-length")
    same.add_argument("project", type=Path)
    find = sub.add_parser("find")
    find.add_argument("query")
    find.add_argument("--system", choices=["CD_CN", "CD_CF", "CD_CO", "EQ_CN", "EQ_ON"])
    find.add_argument("--verify", action="store_true", help="exhaustively check a compact finite countermodel when available")
    args = parser.parse_args()
    if args.command == "import-project":
        import_project(args.project.resolve())
    elif args.command == "import-same-length":
        import_same_length(args.project.resolve())
    elif args.command == "build":
        build()
    elif args.command == "check":
        check()
    elif args.command == "refresh-legacy-links":
        refresh_legacy_links()
    else:
        lookup(args.query, args.system, args.verify)


if __name__ == "__main__":
    main()
