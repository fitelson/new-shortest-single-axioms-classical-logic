# Canonical Prover9 replays

This directory contains the paper-facing Prover9 inputs and their complete
outputs.  Filenames follow the labels in the paper.  Every output was produced
by the vendored, unmodified LADR-2009-11A release at
`vendor/prover9-2009-11A/bin/macos-arm64/prover9`.

Run all inputs that do not yet have outputs with:

```sh
JOBS=8 tools/run_official_prover9_replays.sh
```

The hints in these files guide retention and clause selection; they are not
premises.  Each displayed axiom is the sole non-denial assumption.  The
equational replays use paramodulation as their only positive inference and
report zero new demodulators and zero demodulation rewrites.

All four equational inputs use the preamble standardized in `E_CN.in`:
`raw`, Prolog-style variables, unit paramodulation from small clauses,
unit deletion, restricted denials, SOS-first input, breadth-first hints,
`max_weight=0`, one proof, and suppressed given-clause printing.

## Replay inventory

| Paper label | Signature | Proof length | Level | Maximum weight | Input/output |
|---|---:|---:|---:|---:|---|
| A1 | C/N | 45 | 23 | 26 | `condensed_detachment/CN/A01.in`, `.out` |
| A2 | C/N | 191 | 90 | 26 | `condensed_detachment/CN/A02.in`, `.out` |
| A3 | C/N | 200 | 57 | 26 | `condensed_detachment/CN/A03.in`, `.out` |
| A4 | C/N | 54 | 27 | 26 | `condensed_detachment/CN/A04.in`, `.out` |
| A5 | C/N | 42 | 23 | 26 | `condensed_detachment/CN/A05.in`, `.out` |
| A6 | C/N | 54 | 26 | 26 | `condensed_detachment/CN/A06.in`, `.out` |
| A7 | C/f | 28 | 12 | 30 | `condensed_detachment/Cf/A07.in`, `.out` |
| A8 | C/f | 67 | 30 | 30 | `condensed_detachment/Cf/A08.in`, `.out` |
| A9 | C/f | 49 | 27 | 30 | `condensed_detachment/Cf/A09.in`, `.out` |
| A10 | C/f | 38 | 15 | 30 | `condensed_detachment/Cf/A10.in`, `.out` |
| A11 | C/f | 43 | 22 | 30 | `condensed_detachment/Cf/A11.in`, `.out` |
| A12 | C/f | 36 | 22 | 30 | `condensed_detachment/Cf/A12.in`, `.out` |
| A13 | C/o | 27 | 15 | 20 | `condensed_detachment/Co/A13.in`, `.out` |
| A14 | C/o | 66 | 31 | 20 | `condensed_detachment/Co/A14.in`, `.out` |
| A15 | C/o | 56 | 24 | 20 | `condensed_detachment/Co/A15.in`, `.out` |
| A16 | C/o | 43 | 30 | 20 | `condensed_detachment/Co/A16.in`, `.out` |
| A17 | C/o | 46 | 20 | 20 | `condensed_detachment/Co/A17.in`, `.out` |
| A18 | C/o | 68 | 24 | 20 | `condensed_detachment/Co/A18.in`, `.out` |
| E_AN | A/N | 103 | 32 | 36 | `equational/AN/E_AN.in`, `.out` |
| E_Cf | C/f | 77 | 48 | 22 | `equational/Cf/E_Cf.in`, `.out` |
| E_CN | C/N | 175 | 88 | 21 | `equational/CN/E_CN.in`, `.out` |
| E_ON | O/N | 191 | 74 | 4000 | `equational/ON/E_ON.in`, `.out` |

The `E_Cf` output is a 77-step, level-48 conjunctive proof from the displayed
C/f identity as its sole non-denial assumption.  It reports zero new
demodulators and zero demodulation rewrites.
