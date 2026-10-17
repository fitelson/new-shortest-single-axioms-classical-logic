# Preserved legacy Walsh search code

`walsh_search/` is an unchanged source snapshot copied from the authors'
development tree, `code/legacy_walsh_search/`, on 17 October 2026. The
original author and results notes are preserved as `README.original.txt`
and `RESULTS.original.txt`. The root MIT license applies to this locally
authored search code; theorem-prover licenses remain separate.

The C/N entry point is `BooleanAlgebraMethod.GenerateTautologyFile` with
the `"CN"` generator. `TemplateGeneration.py` deliberately prevents
adjacent negations. `FillHandling.py` generates variable-identification
partitions and retains most-general tautological representatives; there
is no fixed five-variable bound. The paper's reported C/N weight-19 and
weight-21 claims are conservatively restricted to DN-free formulas with
at most six distinct variables. The historical records may include more
general formulas and are not silently truncated to that scope.

The legacy tables were generated earlier and are being preserved/audited,
not claimed as new runs of the current root-level Python implementation.
The exact original dependency environment is not reconstructed by this
snapshot. Source bytes and saved results are fixed by the root checksums.
The current toolkit and the C port are different implementations, not
retroactive descriptions of the legacy run.

See `../CANDIDATE_INDEX.md` and
`../results/candidate_index/legacy_manifest.json` for the result records.
The weight-19 evidence recovered from fresh-variable padding at weight 21
is extracted by `../tools/archive_cn19_padding.py`; that tool copies
existing matrices and outputs and never invokes a theorem prover.
