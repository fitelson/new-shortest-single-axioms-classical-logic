# Archive contents

This repository is the computational companion to *New Short(est) Single
Axioms for Classical Logic*.

## Search code

The root Python modules implement Walsh's single-axiom enumerator and its
finite-model and saturation filters. Run definitions are in `runs/`, reusable
reproduction tools are in `tools/`, and automated checks are in `tests/`.
The small checksummed model-stock archives in `data/model_stocks/` accelerate
the principal condensed-detachment searches.

## Paper-facing proof certificates

`proofs/official/prover9/` contains 22 canonical input/output pairs:

- `A01`--`A18` verify the condensed-detachment axioms reported in the paper;
- `E_AN`, `E_Cf`, `E_CN`, and `E_ON` verify the four equational axioms by
  deriving the conjunction of the relevant complete basis.

The directory's `README.md` reports proof statistics and its `SHA256SUMS`
fixes the exact archived bytes.

## Reference Prover9 release

`vendor/prover9-2009-11A/` contains William McCune's unmodified official
LADR-2009-11A source archive, its GPLv2 license, SHA-256 checksums, and the
macOS ARM64 executable used for the archived paper-facing outputs. The source
archive permits rebuilding Prover9 on other supported systems.

## Deliberately excluded working material

Large proof-development stocks, transient theorem-prover inputs, raw run logs,
checkpoints, and local executable installations are not part of the release.
They remain in the authors' working tree and are excluded by `.gitignore`;
they are not required to check any paper-facing proof.

Run `python3 tools/verify_release.py` for a non-mutating archive audit. Add
`--replay` to execute all 22 canonical inputs afresh with the vendored binary.
