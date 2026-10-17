# Candidate elimination index

Start here to find what happened to a candidate, rather than inferring its
status from its absence from the list of new axioms. Condensed-detachment
formulas and equational identities have separate tables and search spaces.

The paper reports its C/N weight-19 elimination and weight-21
shortestness/search claims only for **DN-free formulas with at most six
distinct variables**. These qualifications do not limit the positive
complete-basis proof certificates. The underlying legacy enumeration
excluded adjacent negations but had no fixed five-variable cap; its
weight-21 survivor list contains 66 six-variable formulas. Historical
records beyond the reported class are preserved rather than removed.

## The old O5 and the paper's O5

The two labels denote different formulas. In ASCII Polish notation below,
`o` is the verum constant and `F` is the falsum constant.

| 2021 label | AJL label | Polish formula | Current status | Individual evidence |
|---|---|---|---|---|
| O1 | O1, same-length C/N question | `CCCpqCCrNsCtNtCCtpCrp` | Open | [Candidate entry](results/candidate_index/named_candidates.md#legacy_O1) |
| O2 | O2, same-length C/f question | `CCCpqrCCCCsFtCrpCsp` | Open | [Candidate entry](results/candidate_index/named_candidates.md#legacy_O2) |
| O3 | O3, same-length C/o question | `CCpCqrCCCrsCoqCtCpr` | Open | [Candidate entry](results/candidate_index/named_candidates.md#legacy_O3) |
| O4 | O4 | `CCCpqCorCsCCrpCtp` | Open, weight 17 | [Candidate entry](results/candidate_index/named_candidates.md#O4) |
| Identification instance | O4[t:=s] | `CCCpqCorCsCCrpCsp` | Open; sufficiency reduces to O4 | [Candidate entry](results/candidate_index/named_candidates.md#O4_ident_t_s) |
| **O5** | **No current O-number** | **`CCCpqrCCrCoCrpCsp`** | **Eliminated by completed saturation** | [Input](results/candidate_index/evidence/legacy_O5.in), [official Vampire 5.0.1 output](results/candidate_index/evidence/legacy_O5_vampire501.out) |
| O6 | O5, Appendix B | `CCpqCrCCCqsCopCtq` | Eliminated by a seven-element matrix | [Exhaustive matrix verifier](results/candidate_index/evidence/O5_AJL_legacy_O6_countermodel_verification.py) |
| Identification instance | O5[t:=r] | `CCpqCrCCCqsCopCrq` | Eliminated by the same matrix | [Candidate entry](results/candidate_index/named_candidates.md#O5_ident_t_r) |
| Unnumbered C/f candidate | F17 | `CCCCCpqFrsCCspCtp` | **Open**, weight 17 | [Candidate entry](results/candidate_index/named_candidates.md#CD_CF17_legacy_exception) |

The old O5 replay states the candidate and condensed detachment as axioms,
with Meredith's classical C/o single axiom M2 as conjecture. Vampire returns
`SZS status CounterSatisfiable` and a finite saturation. Its failure to derive
M2 therefore establishes insufficiency. The retained seven-clause
[historical saturation](results/candidate_index/evidence/legacy_O5_historical_saturation.in)
is also included; the fresh 5.0.1 replay produces a smaller saturation.

The matrix for **AJL O5 / old O6** is a separate certificate. Its designated
set is `{3,6}`, `o=3`, and it refutes L4. Neither bounded failed proof searches
nor timed-out finite-model searches count as eliminations of **O4**.
The complete instance-level C/o weight-17 screen retained four formulas,
O4, O4[t:=s], O5, and O5[t:=r]. Its two
[shard reports](results/candidate_index/evidence/CO17_instance_stats_shard0.json)
and [second shard](results/candidate_index/evidence/CO17_instance_stats_shard1.json)
and the adjacent survivor JSONLs are preserved. Thus O4 is the only
remaining **representative family**, not the only unresolved formula up to
renaming. No O4-to-o derivation is claimed.

## Individual candidate tables

| Table | What it contains |
|---|---|
| [Named candidates](results/candidate_index/named_candidates.md) | The 19 named C/N weight-19 working-file entries (one is not a tautology as transcribed), the four exceptional C/N weight-20 candidates, the exceptional constant-language cases and their retained identification instances, the old O1--O6 labels, and `cand102`. Each row identifies evidence or an open case. |
| [C/N weight-19 padding exception map](results/candidate_index/cn19_padding_exceptions.tsv) | All 77 exceptional padded weight-21 rows: 59 saved successful historical outputs and 18 links to named tautological weight-19 cases. |
| [Named candidates, TSV](results/candidate_index/named_candidates.tsv) | The same rows with ASCII Polish, numeric-variable legacy Polish, and parenthesized TPTP using both A,B,C and X,Y,Z variable names. |
| [Equational tables](results/candidate_index/equational_candidates.md) | Elimination-method totals at every searched smaller weight, followed by every unresolved C/N and O/N identity. |
| [Equational survivors, TSV](results/candidate_index/equational_survivors.tsv) | All 23 C/N and 351 O/N survivor formulas, their weights, stable IDs, and precise source-ledger locations. These rows are unresolved, not eliminated. A/N follows by duality. |
| [Preserved same-length lists](results/candidate_index/same_length/README.md) | The original CD general-filter lists at C/N weight 21 (782 rows), C/f weight 19 (162), and C/o weight 19 (188). They include subsequently verified axioms and do not assert that every row is still unresolved. |
| [Same-length candidates, TSV](results/candidate_index/same_length_candidates.tsv) | All 1,132 historical rows with ordinary Polish, digit-variable Polish, TPTP notation, and exact source-list locations. Current named verdicts take precedence in formula lookup. |

The development notes accidentally used `c1918` for two different weight-19
formulas. The index keeps that historical label but assigns distinct stable
IDs ending in `c1918` and `c1918b`. Formula identity, rather than a bare number,
resolves this ambiguity. The paper's `c_{19,13}` is the row
`CD_CN19_c1913`, with Polish formula `CCpCCqrCNsNrCCrpCrs`; its elimination is
the induction in Appendix A, not the finite audit performed by its helper
script.

The historical `c1915` entry, `CCpCCqrCsNrCCNtpCrt`, is false at
(p,q,r,s,t)=(1,0,1,0,0). It is retained as provenance, not counted as a
post-tautology survivor. Its additional old matrix certificate is also
preserved. The lifting targets' maximal generality, this countervaluation,
and O5[t:=r]'s 2,401 matrix valuations are checked by
`tools/verify_candidate_reductions.py`, with results in
`results/candidate_index/reduction_checks.json`.

**Unresolved C/f lower-bound candidate:** `F17 = CCCCCpqFrsCCspCtp`, stable
ID `CD_CF17_legacy_exception`. Its row in the legacy weight-17 file has no
attached countermodel, and no definitive elimination certificate has been
recovered. The reconstruction attempts did not establish axiomhood or
insufficiency. We therefore classify the candidate as **open**, rather than
presuming that a missing elimination certificate exists. The earlier blanket
claim that all weight-17 C/f candidates were eliminated is withdrawn.
The verified 19-symbol CD C/f axioms are **shortest known**, with shortestness
conditional on eliminating F17. The separate **equational** C/f lower bound
and its 17-symbol single axiom are unaffected.

## Preserved legacy countermodel assignments

These compressed TSVs preserve every row of the corresponding legacy
post-tautology-filter file, including rows subsequently handled separately.
They identify the compact finite countermodel assigned to each eliminated
formula. Exceptions link to the named-candidate table by stable ID.

| System / weight | Candidate rows | Rows with recorded finite countermodels | Exceptional rows | Download |
|---|---:|---:|---:|---|
| CD C/N, 20 | 24,616,789 | 24,616,785 | 4 | [CD_CN20.tsv.gz](results/candidate_index/legacy/CD_CN20.tsv.gz) |
| CD C/f, 17 | 723,665 | 723,664 | 1 | [CD_CF17.tsv.gz](results/candidate_index/legacy/CD_CF17.tsv.gz) |
| CD C/o, 17 | 926,821 | 926,816 | 5 | [CD_CO17.tsv.gz](results/candidate_index/legacy/CD_CO17.tsv.gz) |
| CD C/N, 19 via padding to 21 | 7,741,045 | 7,740,968 | 77 | [CD_CN19_from_CN21.tsv.gz](results/candidate_index/legacy/CD_CN19_from_CN21.tsv.gz) |

The first three tables contain **26,267,275 preserved candidate rows**, not the much larger number
of all raw variable-identification instances. The legacy enumerator first
removed nontautologies and subsumed instances. The
[legacy manifest](results/candidate_index/legacy_manifest.json) records the
original source filenames, source SHA-256 digests, counts, and exception row
numbers. The compressed tables retain the original variable-numbering
convention: digits are variables; `O` is the relevant constant in a
constant-language dataset. The lookup tool translates ordinary variable
letters and TPTP notation to that convention.

The fourth table is a static extraction from all 82,301,488 rows of the
legacy CN21 countermodel file. It keeps exactly formulas Cz-alpha with z
fresh, alongside the normalized weight-19 alpha, original padded formula,
source line, and recorded matrix or exception-map ID. Eliminating the
padded axiom eliminates alpha by the pure-CD padding argument. The 77
exceptions have a complete [mapping](results/candidate_index/cn19_padding_exceptions.json):
59 copied successful outputs (55 saturations, four finite models) and 18
named cases, including the Appendix A chain. This covers the legacy
NN-free representatives without imposing a new variable cap. It does not
turn the optional independent C rerun into a completed result. That rerun
was stopped at the authors' request after this legacy evidence was recovered;
its partial output is not used as an elimination certificate.

The source snapshot is under [legacy/walsh_search](legacy/README.md).
The four CN20 exceptional outputs explicitly identify **Vampire 4.5.1**;
the padding map records the version banners in each historical output.
These are not described as 5.0.1 replays. Neither the copied generator nor
the current 5.0.1 sources assert a reconstruction of the exact 2021 runtime.

The compact model format is: one digit for domain size, its designation bits,
the implication table in row-major order, and (for C/N) its negation table.
Values and matrix indices are zero-based; a constant is interpreted as 0.
These assignments are preserved historical evidence. An individual lookup
with `--verify` independently exhausts its candidate valuations, checks modus
ponens, and exhibits a valuation refuting the classical target.

## Search by label or formula

Run from the repository root:

```sh
python3 tools/candidate_index.py find legacy_O5
python3 tools/candidate_index.py find O5
python3 tools/candidate_index.py find c1913
python3 tools/candidate_index.py find 'CCCpqrCCrCoCrpCsp' --system CD_CO
python3 tools/candidate_index.py find 'i(i(i(X,Y),Z),i(i(Z,i(o,i(Z,X))),i(U,X)))' --system CD_CO
```

`O5` selects the AJL label; use `legacy_O5` or `'old O5'` for the earlier
formula. Formula lookup accepts alphabetic variants. For an unnamed legacy
formula, the tool streams the appropriate compressed table, so it does not
load millions of rows into memory. Add `--verify` to check its recorded
finite countermodel. A lookup miss does not establish elimination or
axiomhood.

## What each outcome means

- **Truth-table elimination:** the candidate fails in the intended classical
  two-element interpretation and hence is not a theorem of the target logic.
- **Finite countermodel:** every candidate instance is designated, modus
  ponens preserves designation, and some target theorem is undesignated
  (or, for equations, the candidate holds while the target basis fails).
- **Completed saturation:** the candidate-plus-counterexample problem is
  satisfiable, as certified by a successful complete saturation result.
- **Syntactic elimination:** a mathematical argument shows a required theorem
  absent from the entire closure; Appendix A is the example here.
- **Open:** no proof of axiomhood or definitive elimination is claimed.

The newer equational instrumentation preserved aggregate counts by
elimination method and individual **survivor** rows. It did not preserve a
formula-by-formula ledger for all eliminated identities. Its aggregate
method counts are provided exactly as recorded; the index does not assign
invented individual methods to those billions of generated identities.
The older independent A/N screen is retained for provenance under
`results/equational_lower_bounds/`, but uses a different basis and is not
the paper's A/N classification, which is the Boolean dual of O/N.

## Rebuild and check

```sh
python3 tools/candidate_index.py build
python3 tools/candidate_index.py check
python3 results/candidate_index/evidence/O5_AJL_legacy_O6_countermodel_verification.py
```

The optional `import-project /path/to/walsh_meredith` command reconstructs
the compact legacy tables from the preserved development tree. It does not
launch a proof or model search. `replay_candidate_eliminations.py` documents
the bounded Vampire replays used to reconstruct individual missing records;
its successful outputs, rather than its timeouts, supply table evidence.
