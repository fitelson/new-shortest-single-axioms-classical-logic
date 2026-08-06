#!/usr/bin/env python3
"""Audit the publication search lengths and print exact headline commands."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO))

from Globals import ConstantSpec, ModelSpec, OperationSpec, PredicateSpec  # noqa: E402
from TreeForms import TreeForm  # noqa: E402

HEADLINE_RUNS = {
    "CN": (21, "runs/cn_definition.json", None),
    "CF": (19, "runs/cf_definition.json", None),
    "CT": (19, "runs/ct_definition.json", None),
    "BACF": (
        17,
        "runs/bacf_definition.json",
        "i(i(i(i(p,q),r),i(i(i(r,f),q),f)),f)=r",
    ),
    "BAAN": (
        20,
        "runs/baan_definition.json",
        "a(n(a(a(p,n(q)),r)),n(a(n(q),n(a(a(r,s),p)))))=q",
    ),
    "BAON": (
        20,
        "runs/baon_definition.json",
        "o(n(o(p,o(n(q),r))),n(o(n(q),n(o(o(r,p),s)))))=q",
    ),
    "BACN": (
        17,
        "runs/bacn_definition.json",
        "i(i(i(i(p,i(q,r)),s),q),n(i(s,n(q))))=s",
    ),
}

LOWER_BOUND_RUNS = {
    "CN": (19, "runs/cn_definition.json"),
    "CF": (17, "runs/cf_definition.json"),
    "CT": (17, "runs/ct_definition.json"),
    "BACF": (15, "runs/bacf_definition.json"),
    "BAAN": (19, "runs/baan_definition.json"),
    "BAON": (19, "runs/baon_definition.json"),
    "BACN": (16, "runs/bacn_definition.json"),
}


def load_tree(config_path: Path) -> TreeForm:
    config = json.loads(config_path.read_text(encoding="utf-8"))
    spec = ModelSpec(
        PredicateSpec.parse(config["predicate"]),
        tuple(OperationSpec.parse(item) for item in config["operators"]),
        tuple(ConstantSpec.parse(item) for item in config["constants"]),
    )
    return TreeForm(spec, 14)


def equation_generator_length(formula: str) -> int:
    """Count all function/constant/variable occurrences and equality."""
    if formula.count("=") != 1:
        raise ValueError(f"expected one equality: {formula}")
    return len(re.findall(r"[A-Za-z][A-Za-z0-9_]*", formula)) + 1


def main() -> None:
    print(
        "name\ttarget\tstructural_forms\tcandidate_instances\t"
        "displayed_equation_count"
    )
    for name, (target, relative_config, formula) in HEADLINE_RUNS.items():
        tree = load_tree(REPO / relative_config)
        displayed_count = "-"
        if formula is not None:
            actual = equation_generator_length(formula)
            if actual != target:
                raise AssertionError(
                    f"{name}: displayed equation has generator length {actual}, "
                    f"not configured target {target}"
                )
            displayed_count = str(actual)
        print(
            f"{name}\t{target}\t{tree.form_count(target)}\t"
            f"{tree.formula_count(target)}\t{displayed_count}"
        )

    print("\nLower-bound frontier runs:")
    print("name\ttarget\tstructural_forms\tcandidate_instances")
    for name, (target, relative_config) in LOWER_BOUND_RUNS.items():
        tree = load_tree(REPO / relative_config)
        print(
            f"{name}\t{target}\t{tree.form_count(target)}\t"
            f"{tree.formula_count(target)}"
        )

    print("\nExact lower-bound Vampire 5.0.1 casc_sat commands:")
    for name, (target, relative_config) in LOWER_BOUND_RUNS.items():
        print(f"python3 run.py {name}_LOWER1 {target} {relative_config}")


if __name__ == "__main__":
    main()
