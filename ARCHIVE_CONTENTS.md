# Archive contents

This repository is the computational companion to *New Short(est) Single
Axioms for Classical Logic*.

## Search code

The root Python modules implement Walsh's single-axiom enumerator and its
finite-model and saturation filters. Run definitions are in `runs/`, reusable
reproduction tools are in `tools/`, and automated checks are in `tests/`.
The small checksummed model-stock archives in `data/model_stocks/` accelerate
the principal condensed-detachment searches.
`legacy/walsh_search/` preserves the earlier generator unchanged, with the
original author/results notes and a provenance explanation in `legacy/README.md`.
Its CN enumeration is DN-free. This source snapshot does not claim to
reconstruct the exact original dependency environment.

## Paper-facing proof certificates

`proofs/official/prover9/` contains 29 canonical input/output pairs:

- `A01`--`A18` verify the condensed-detachment axioms reported in the paper;
- `E_Cf`, `E_CN`, and `E_ON` verify the three displayed equational axioms by
  deriving the conjunction of the relevant complete basis; `E_AN` preserves
  the separately discovered A/N axiom checked for the earlier draft. It is
  additional verified material, not the Boolean dual of the paper's O/N axiom;
- `wos_pure_circle_CN_1`--`wos_pure_circle_CN_7` verify the seven strict links
  Meredith -> cand65 -> cand112 -> cand79 -> cand44 -> cand8 -> cand121 ->
  Meredith, with one source axiom per replay.

The directory's `README.md` reports proof statistics and its `SHA256SUMS`
fixes the exact archived bytes.
`BASIS_SOURCES.md` maps the equational replay goals to the original
Meredith--Prior sources and Prior's 1969 corrigendum. The goal formulas and
saved proof outputs are unchanged by this source check.

## Reference Prover9 release

`vendor/prover9-2009-11A/` contains William McCune's unmodified official
LADR-2009-11A source archive, its GPLv2 license, SHA-256 checksums, and the
macOS ARM64 executable used for the archived paper-facing outputs. The source
archive permits rebuilding Prover9 on other supported systems.

## Reference Vampire release

`vendor/vampire-5.0.1/` contains the official tagged Vampire 5.0.1 source
archive (release commit `1b13eaf`), its modified BSD license and authors file,
SHA-256 checksums, and the official macOS ARM64 executable used for the
archived searches. The source archive permits rebuilding Vampire on another
supported system.

## Equational lower-bound results

`results/equational_lower_bounds/` contains the exact per-shard statistics and
survivor ledgers for all completed smaller-length `C/f`, `C/N`, `A/N`, and
`O/N` screens. Its generated manifest aggregates 45 reconciled length runs;
its checksum file authenticates every archived record.

## Candidate-to-evidence navigation

`CANDIDATE_INDEX.md` is the human entry point. `results/candidate_index/`
contains named-candidate tables, a historical-to-current label crosswalk,
individual elimination inputs and outputs (including the old O5 saturation),
the complete preserved legacy countermodel assignments as compressed TSVs,
and the equational elimination-method totals and individual unresolved
formulas. It also contains the 1,132 preserved historical same-length CD
general-filter survivors, with explicit warnings that membership is not a
current unresolved verdict. `tools/candidate_index.py` supports alphabetic-variant formula
lookup and independent verification of a compact finite countermodel.
The CN19 padding table adds 7,741,045 records recovered from the legacy
CN21 file; 77 exceptions have a complete map to 59 copied successful outputs
and 18 named tautological cases. The source and extraction digests are in
`legacy_manifest.json`. Historical Vampire versions are recorded rather
than relabeled as 5.0.1. Two C/o instance-level shard reports and their
four survivors are also preserved. `tools/verify_candidate_reductions.py`
checks maximal-generality facts, the c1915 countervaluation, and the O4/O5
identification-instance relations without running any prover or search.

The index distinguishes individual certificates, aggregate statistics, and
open cases. The paper's C/N weight-19 elimination and weight-21
shortestness/search claims are restricted to DN-free formulas with at most
six distinct variables; the positive sufficiency proofs remain
unconditional. In particular, `F17 = CCCCCpqFrsCCspCtp` remains an unresolved
17-symbol CD C/f candidate; the 19-symbol CD C/f axioms are shortest known,
not proved shortest. The independent equational C/f shortestness result is
unchanged. The index does not claim that an individual
outcome ledger was retained for every equational elimination.

## Deliberately excluded working material

Large proof-development stocks, transient theorem-prover inputs, raw run logs,
checkpoints, and other local executable installations are not part of the release.
They remain in the authors' working tree and are excluded by `.gitignore`;
they are not required to check any paper-facing proof.

Run `python3 tools/verify_release.py` for a non-mutating archive audit. Add
`--replay` to execute all 29 canonical inputs afresh with the vendored binary.
The root `SHA256SUMS` authenticates every release file except itself.
