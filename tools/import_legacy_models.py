#!/usr/bin/env python3
"""Import and verify Walsh's compact legacy countermodel stock."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

import numpy as np


REPO = Path(__file__).resolve().parents[1]
PROJECT = REPO.parents[2]
sys.path.insert(0, str(REPO))

from Globals import ConstantSpec, ModelSpec, OperationSpec, PredicateSpec  # noqa: E402
from ModelTools import Model  # noqa: E402


SOURCES = {
    "CN": (
        PROJECT / "code/legacy_walsh_search/Results/CN21Results/CN_21_CounterModels.txt",
        "runs/cn_definition.json",
        "N",
    ),
    "CF": (
        PROJECT / "code/legacy_walsh_search/Results/C019Results/C0_19_CounterModels.txt",
        "runs/cf_definition.json",
        "0",
    ),
    "CT": (
        PROJECT / "code/legacy_walsh_search/Results/C119Results/C1_19_CounterModels.txt",
        "runs/ct_definition.json",
        "1",
    ),
}


def load_spec(relative_config: str) -> tuple[ModelSpec, dict]:
    config = json.loads((REPO / relative_config).read_text(encoding="utf-8"))
    return (
        ModelSpec(
            PredicateSpec.parse(config["predicate"]),
            tuple(OperationSpec.parse(item) for item in config["operators"]),
            tuple(ConstantSpec.parse(item) for item in config["constants"]),
        ),
        config,
    )


def compact_model(model_string: str, model_type: str):
    order = int(model_string[0])
    position = 1
    designated = np.array(
        [int(value) for value in model_string[position : position + order]],
        dtype=np.bool_,
    )
    position += order
    implication = np.array(
        [int(value) for value in model_string[position : position + order * order]],
        dtype=np.int8,
    ).reshape((order, order))
    position += order * order
    negation = None
    if model_type == "N":
        negation = np.array(
            [int(value) for value in model_string[position : position + order]],
            dtype=np.int8,
        )
        position += order
    if position != len(model_string):
        raise ValueError(f"unparsed compact model suffix: {model_string[position:]}")
    return order, designated, implication, negation


def vampire_model_text(model_string: str, model_type: str, constant_symbol: str | None) -> str:
    order, designated, implication, negation = compact_model(model_string, model_type)
    lines = [
        f"tff('declare_$i{index}',type,'fmb_$i_{index}':$i)."
        for index in range(1, order + 1)
    ]
    lines.append("tff(declare_t,type,t: $i > $o).")
    lines.extend(
        ("" if designated[index - 1] else "~")
        + f"t('fmb_$i_{index}')."
        for index in range(1, order + 1)
    )
    if constant_symbol is not None:
        lines.append(f"tff(declare_{constant_symbol},type,{constant_symbol}:$i).")
        lines.append(
            f"tff({constant_symbol}_definition,axiom,"
            f"{constant_symbol} = 'fmb_$i_1')."
        )
    lines.append("tff(declare_i,type,i: ($i * $i) > $i).")
    implication_rows = []
    for left in range(order):
        for right in range(order):
            implication_rows.append(
                f"i('fmb_$i_{left + 1}','fmb_$i_{right + 1}') = "
                f"'fmb_$i_{int(implication[left, right]) + 1}'"
            )
    lines.append("tff(function_i,axiom,\n  " + "\n& ".join(implication_rows) + "\n).")
    if negation is not None:
        lines.append("tff(declare_n,type,n: ($i) > $i).")
        negation_rows = [
            f"n('fmb_$i_{index + 1}') = 'fmb_$i_{int(value) + 1}'"
            for index, value in enumerate(negation)
        ]
        lines.append("tff(function_n,axiom,\n  " + "\n& ".join(negation_rows) + "\n).")
    return "\n".join(lines) + "\n"


def legacy_polish_to_tptp(formula: str, constant_symbol: str | None) -> str:
    position = 0
    variables: dict[str, str] = {}

    def term() -> str:
        nonlocal position
        symbol = formula[position]
        position += 1
        if symbol == "C":
            return f"i({term()},{term()})"
        if symbol == "N":
            return f"n({term()})"
        if symbol == "O":
            if constant_symbol is None:
                raise ValueError("constant in constant-free formula")
            return constant_symbol
        if symbol not in variables:
            variables[symbol] = chr(ord("A") + len(variables))
        return variables[symbol]

    parsed = term()
    if position != len(formula):
        raise ValueError(f"unparsed Polish suffix: {formula[position:]}")
    return f"t({parsed})"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("signature", choices=sorted(SOURCES))
    parser.add_argument("namespace", help="destination below CounterModels")
    args = parser.parse_args()

    source, relative_config, model_type = SOURCES[args.signature]
    spec, config = load_spec(relative_config)
    constant_symbol = spec.constants[0].tptp_symbol if spec.constants else None
    target = config["counter_modeling_formulas"][0]
    representatives: dict[str, str] = {}
    source_lines = 0
    with source.open(encoding="utf-8") as input_file:
        for line in input_file:
            source_lines += 1
            if ":" not in line:
                continue
            formula, model_string = line.strip().split(":", 1)
            representatives.setdefault(model_string, formula)

    destination = REPO / "CounterModels" / args.namespace
    destination.mkdir(parents=True, exist_ok=True)
    written = 0
    verified = 0
    orders: dict[int, int] = {}
    for model_string, formula in sorted(representatives.items()):
        digest = hashlib.sha256(model_string.encode()).hexdigest()[:16]
        order = int(model_string[0])
        output = destination / f"legacy-countermodel-{order}-{digest}.out"
        if not output.exists():
            output.write_text(
                vampire_model_text(model_string, model_type, constant_symbol),
                encoding="utf-8",
            )
            written += 1
        model = Model(spec, model_filename=str(output))
        candidate = legacy_polish_to_tptp(formula, constant_symbol)
        if not model(candidate):
            raise AssertionError(f"legacy model does not satisfy {candidate}: {output}")
        if model(target):
            raise AssertionError(f"legacy model does not refute target {target}: {output}")
        verified += 1
        orders[order] = orders.get(order, 0) + 1

    report = {
        "signature": args.signature,
        "namespace": args.namespace,
        "source": str(source),
        "source_lines": source_lines,
        "unique_models": len(representatives),
        "written": written,
        "verified": verified,
        "orders": dict(sorted(orders.items())),
        "target_refuted": target,
    }
    report_path = REPO / "data" / f"legacy_model_import_{args.namespace}.json"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
