#!/usr/bin/env python3
"""Exhaustively verify the seven-element matrix countermodel for O6."""

from collections import Counter
from itertools import product


DOMAIN = tuple(range(1, 8))
DESIGNATED = frozenset({3, 6})
O = 3

# Padding at index 0 lets the displayed values 1,...,7 serve as indices.
IMP = (
    (),
    (None, 3, 3, 3, 3, 3, 3, 3),
    (None, 7, 6, 6, 6, 6, 6, 7),
    (None, 1, 4, 6, 1, 4, 3, 7),
    (None, 3, 3, 3, 3, 3, 3, 3),
    (None, 6, 6, 6, 6, 6, 6, 7),
    (None, 4, 2, 6, 5, 4, 6, 7),
    (None, 2, 2, 6, 2, 2, 6, 6),
)


def i(x: int, y: int) -> int:
    return IMP[x][y]


def o6(p: int, q: int, r: int, s: int, t: int) -> int:
    """CCpqCrCCCqsCopCtq."""
    return i(i(p, q), i(r, i(i(i(q, s), i(O, p)), i(t, q))))


def lukasiewicz_l4(p: int, q: int, r: int, s: int) -> int:
    """CCCpqrCCrpCsp."""
    return i(i(i(p, q), r), i(i(r, p), i(s, p)))


def main() -> None:
    assert O in DESIGNATED
    assert all(i(x, y) in DOMAIN for x, y in product(DOMAIN, repeat=2))

    # Soundness of condensed detachment (semantic modus ponens):
    # if x and Cxy are designated, then y is designated.
    mp_violations = [
        (x, y, i(x, y))
        for x, y in product(DOMAIN, repeat=2)
        if x in DESIGNATED and i(x, y) in DESIGNATED and y not in DESIGNATED
    ]
    assert not mp_violations

    o6_values = Counter(o6(*valuation) for valuation in product(DOMAIN, repeat=5))
    assert sum(o6_values.values()) == 7**5
    assert set(o6_values) <= DESIGNATED

    l4_assignment = (2, 1, 1, 3)
    l4_value = lukasiewicz_l4(*l4_assignment)
    assert l4_value == 7
    assert l4_value not in DESIGNATED

    print(f"domain: {DOMAIN}")
    print(f"designated values: {sorted(DESIGNATED)}")
    print("condensed-detachment violations: 0")
    print(f"O6 valuations checked: {7**5}")
    print(f"O6 output counts: {dict(sorted(o6_values.items()))}")
    print(f"L4 at (P,Q,R,S)={l4_assignment}: {l4_value} (undesignated)")
    print(f"L5=o: {O} (designated)")
    print("VERIFIED: O6 does not derive the Lukasiewicz basis under CD.")


if __name__ == "__main__":
    main()
