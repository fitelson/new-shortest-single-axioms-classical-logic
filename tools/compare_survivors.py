#!/usr/bin/env python3
"""Compare current survivor ledgers with Walsh's legacy Polish result files."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
PROJECT = REPO.parents[2]

LEGACY_FILES = {
    "CN": PROJECT / "code/legacy_walsh_search/Results/CN21Results/specialcases/CN_21_Remaining.txt",
    "CF": PROJECT / "code/legacy_walsh_search/Results/C019Results/specialcases/C0_19_Remaining.txt",
    "CT": PROJECT / "code/legacy_walsh_search/Results/C119Results/specialcases/C1_19_Remaning.txt",
}


class FunctionalParser:
    def __init__(self, text: str):
        self.tokens = re.findall(r"[A-Za-z][A-Za-z0-9_]*|[(),]", text)
        self.position = 0

    def term(self):
        if self.position >= len(self.tokens):
            raise ValueError("unexpected end of formula")
        symbol = self.tokens[self.position]
        self.position += 1
        if self.position < len(self.tokens) and self.tokens[self.position] == "(":
            self.position += 1
            arguments = [self.term()]
            while self.tokens[self.position] == ",":
                self.position += 1
                arguments.append(self.term())
            if self.tokens[self.position] != ")":
                raise ValueError(f"expected closing parenthesis in {self.tokens}")
            self.position += 1
            return symbol, arguments
        return symbol, []


def canonical_polish_from_functional(formula: str) -> str:
    parser = FunctionalParser(formula.strip())
    tree = parser.term()
    if parser.position != len(parser.tokens):
        raise ValueError(f"unparsed functional formula suffix: {formula}")
    if tree[0] == "t" and len(tree[1]) == 1:
        tree = tree[1][0]

    variable_numbers: dict[str, str] = {}

    def polish(node) -> str:
        symbol, arguments = node
        if symbol == "i":
            return "C" + polish(arguments[0]) + polish(arguments[1])
        if symbol == "n":
            return "N" + polish(arguments[0])
        if symbol in {"f", "o"}:
            return "O"
        if arguments:
            raise ValueError(f"unsupported symbol {symbol!r}")
        if symbol not in variable_numbers:
            variable_numbers[symbol] = str(len(variable_numbers))
        return variable_numbers[symbol]

    return polish(tree)


def canonicalize_legacy(formula: str) -> str:
    variable_numbers: dict[str, str] = {}
    output: list[str] = []
    for symbol in formula.strip():
        if symbol in {"C", "N", "O"}:
            output.append(symbol)
        else:
            if symbol not in variable_numbers:
                variable_numbers[symbol] = str(len(variable_numbers))
            output.append(variable_numbers[symbol])
    return "".join(output)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("signature", choices=sorted(LEGACY_FILES))
    parser.add_argument(
        "ledger",
        nargs="?",
        help="current Survivors.jsonl; defaults from the signature and headline length",
    )
    args = parser.parse_args()
    lengths = {"CN": 21, "CF": 19, "CT": 19}
    ledger = Path(args.ledger) if args.ledger else (
        REPO / "Remaining" / args.signature /
        f"{args.signature}{lengths[args.signature]}Survivors.jsonl"
    )

    current_records = [json.loads(line) for line in ledger.read_text().splitlines() if line.strip()]
    current = {
        canonical_polish_from_functional(record["formula"]): record["outcome"]
        for record in current_records
    }
    legacy = {
        canonicalize_legacy(line)
        for line in LEGACY_FILES[args.signature].read_text().splitlines()
        if line.strip()
    }

    current_set = set(current)
    report = {
        "signature": args.signature,
        "current_ledger": str(ledger),
        "legacy_file": str(LEGACY_FILES[args.signature]),
        "current_survivors": len(current_set),
        "current_proved": sum(outcome == "proof" for outcome in current.values()),
        "current_unresolved": sum(outcome == "unresolved" for outcome in current.values()),
        "legacy_survivors": len(legacy),
        "intersection": len(current_set & legacy),
        "current_only": sorted(current_set - legacy),
        "legacy_only": sorted(legacy - current_set),
        "exact_match": current_set == legacy,
    }
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
