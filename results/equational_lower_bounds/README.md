# Archived equational lower-bound screens

This directory is the exact, compact result snapshot for every completed
equational search below the lengths of the four displayed single axioms. The
screens used Vampire 5.0.1 (release commit `1b13eaf`) in `casc_sat` portfolio
mode. The archived statistics and survivor ledgers are search results, not
substitutes for the machine-checkable positive single-axiom proofs under
`proofs/official/prover9/`.

Length counts every occurrence in both terms and one occurrence of equality.
The displayed axioms therefore have lengths 17 in `C/f`, 17 in `C/N`, and 20
in both `A/N` and `O/N`.

| Signature | Fully searched smaller lengths | Unresolved survivors |
|---|---|---|
| `C/f` | 5, 7, 9, 11, 13, 15 | none |
| `C/N` | 6--16 | 7 at 15; 16 at 16 |
| `A/N` | 6--19 | 12 at 17; 44 at 18; 294 at 19 |
| `O/N` | 6--19 | 12 at 17; 44 at 18; 295 at 19 |

All other completed lengths in those ranges have no survivors. A survivor is
an unresolved candidate: it was not eliminated by the target truth table, a
verified finite countermodel, or completed saturation within the archived
search envelope. It is not thereby proved to be a single axiom.

`stats/` contains the original per-shard JSON reports. `survivors/` contains
the exact JSONL rows for every nonempty survivor set, together with the two
empty `C/f` length-15 ledgers. `manifest.json` aggregates all 45 completed
length runs (40 two-shard runs and five smaller single-shard `C/f` runs) and
records whether their counters reconcile and their structural coverage is
complete. Regenerate it from the archived raw records with:

```sh
python3 tools/build_equational_lower_bound_snapshot.py
```

`SHA256SUMS` fixes the exact bytes of the manifest, statistics, survivor
ledgers, and this README. `python3 tools/verify_release.py` checks those hashes,
the complete length matrix, every reconciliation flag, and all survivor
counts.
