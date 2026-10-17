# Individual elimination evidence

Use the methods and links in [the named-candidate table](../named_candidates.md)
to select a successful certificate. In particular:

- `legacy_O5.in` with `legacy_O5_vampire501.out` verifies elimination of
  **2021 O5**, `CCCpqrCCrCoCrpCsp`, by completed saturation. The output has
  a successful `CounterSatisfiable` status under the official Vampire 5.0.1.
- `O5_AJL_legacy_O6_countermodel_verification.py` exhaustively checks the
  seven-element certificate for **AJL O5 / 2021 O6**. These are two labels
  for `CCpqCrCCCqsCopCtq`, not for the preceding formula.
- `CN19_chain_verification.py` checks the recurrence and finite examples
  used in the Appendix A proof. The induction in the paper supplies the
  infinite-closure argument; this finite script is not its substitute.
- The `*_countermodel.out` files are individual finite matrices selected
  from the already archived stocks. Candidate validity, modus ponens, and
  a refuted classical target are independently checked by
  `python3 tools/candidate_index.py check`; the witnesses are recorded in
  `../finite_model_verifications.json` (zero-based domain numbering).
- The fresh `CD_CN19_c1914_constrained` run supplies an eight-element
  countermodel. Its auxiliary equations narrow the model search; the model
  is independently checked against the candidate and CD alone, without
  requiring those equations as extra assumptions of the insufficiency claim.
- The four `CN20_exception_*_vampire451.out` files preserve successful
  historical Vampire 4.5.1 outputs. Earlier timed-out slices in those same
  transcripts are not their elimination certificates; the later successful
  `CounterSatisfiable` result is.

`CN19_development_notes.in` is a historical working-file snapshot, preserving
the original labels and comments. It is not the reference replay input for
every row. The index's canonical TPTP columns quantify all variables by the
usual convention; in particular they do not reproduce incomplete binder
lists from commented historical examples.

The old seven-clause O5 saturation is retained as
`legacy_O5_historical_saturation.in`. The adjacent fresh input/output pair
records its current official-release confirmation.

Other reconstruction inputs and transcripts may contain `Timeout` results.
They are retained to document those bounded attempts and are not certificates
of elimination. The named-candidate table links the successful evidence for
each settled row and explicitly marks F17, the weight-17 C/f formula
`CCCCCpqFrsCCspCtp`, as unresolved. The earlier assumption that this formula
had been eliminated is not retained. Neither the failed reconstruction
attempts nor the historical blanket claim supply an elimination certificate.

The oversized domain-8 SAT diagnostic log is stored as
`CD_CF17_legacy_exception_satsuma_ae_kissat_mab/domain_8.cnf.satsuma_ae_proof.1792274584009567000.out.gz`.
Decompression reproduces the original log byte for byte (SHA-256
`e7ae02360d13db19a4dde7f7324d954dc9dea24d923cd31b953a956ee8725b84`).
This diagnostic log is not an elimination certificate for F17.

To repeat that successful test from the repository root:

```sh
vendor/vampire-5.0.1/bin/macos-arm64/vampire \
  --mode portfolio --schedule casc_sat --cores 2 --time_limit 30 --proof tptp \
  results/candidate_index/evidence/legacy_O5.in
```
