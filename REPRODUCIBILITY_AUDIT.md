# Reproducibility audit

Status: in progress.  This file distinguishes completed checks from planned or
running headline searches.

## Reference environment

- Search code: this repository, based on upstream commit `3bc483d`.
- Reference prover: Vampire 5.0.1, release commit `1b13eaf`.
- Candidate prover invocation:
  `--mode portfolio --schedule casc_sat --input_syntax tptp`.
- Default per-candidate limits: 10 seconds, 4096 MiB, one core.

A finite model, `SZS status CounterSatisfiable` or `Satisfiable`, or a
completed saturation with all non-redundant clauses discarded eliminates a
candidate.  A theorem or unsatisfiable result preserves the candidate as a
proved survivor.  A timeout, resource limit, `GaveUp`, or incomplete search
preserves it as unresolved.  This distinction is recorded in the survivor
ledger rather than inferred from an empty model file.

## Compatibility and accounting checks

The test suite currently passes twelve tests.  These cover
the exact prover version, all run-template parses, formula quantifier scope,
Vampire result classification, Vampire 5.0.1 constant definitions, and the
disjoint-counter reconciliation invariant, as well as exact headline lengths,
survivor normalization, JSON serialization, transactional form accounting,
late-model survivor reconciliation, and round-robin shard coverage.

Each standard run writes:

- `partial_run_saves/<NAME><LENGTH>.stats.json`, containing structural-form
  and candidate-instance counts plus disjoint elimination outcomes; and
- `Remaining/<NAME>/<NAME><LENGTH>Survivors.jsonl`, identifying each survivor
  as `proof` or `unresolved`.

For a completed clean run, the following counters must agree:

```
candidate_instances_generated
  = eliminated_by_target_truth_table
  + eliminated_by_cached_countermodels
  + eliminated_by_new_countermodels
  + eliminated_by_saturation
  + survivors_written
```

The real integration run `INSTRUMENTATION_CN5_FIXED_20260804` generated 12
candidates, eliminated 8 by the target truth table and 4 by completed
saturation, and reported `counters_reconcile: true`.

A two-shard integration run over that same CN length-5 space produced the same
6 structural forms, 12 candidate instances, 8 truth-table eliminations, and 4
saturation eliminations as the unsharded control.  The merger additionally
verified complete structural-form and candidate-instance coverage and no
duplicate survivor records.

Instrumentation exposed and repaired two failure modes in the legacy workflow.
First, interrupted runs could checkpoint a half-processed structural form;
statistics now commit only after the whole form completes.  Second, an
unresolved candidate was formerly written immediately even though a model
found later in the same form could refute it.  Survivor decisions are now
buffered until the structural form completes, so each generated candidate has
exactly one final classification.

## Stored and verified finite-model stock

The legacy finite-model stock was imported into the current format and every
model was checked both against a representative archived candidate and against
the target basis it refutes:

| Search | Verified unique models | Orders | Namespace | Import report |
|---|---:|---|---|---|
| CN | 1,011 | 2--5 | `REPRO_CN_V501` | `data/legacy_model_import_REPRO_CN_V501.json` |
| CF | 304 | 2--6 | `REPRO_CF_V501` | `data/legacy_model_import_REPRO_CF_V501.json` |
| CT | 297 | 2--6 | `REPRO_CT_V501` | `data/legacy_model_import_REPRO_CT_V501.json` |

Raw model outputs are retained in `CounterModels/<namespace>/`.  New Vampire
models are parsed and verified before being added, and model files are created
exclusively so parallel shards cannot overwrite one another.

Since `CounterModels/` is a Git-ignored working directory, the three imported
stocks are also stored in deterministic archives under `data/model_stocks/`.
Their manifest records SHA-256 digests and file counts;
`tools/restore_model_stocks.py` verifies those values and refuses conflicting
overwrites.

## Length convention and lower-bound commands

For condensed-detachment problems, target length counts connective, constant,
and variable occurrences in the formula; the assertion predicate `t` is not
counted.  For equational problems, target length counts every symbol occurrence
in both terms plus one occurrence of equality.  The audit script
`python3 tools/audit_lengths.py` separately checks the displayed axioms and the
lower-bound frontiers.  The exhaustive runs needed here are:

| Run | Lower-bound target | Structural forms | Candidate instances |
|---|---:|---:|---:|
| CN | 19 | 6,531,519 | 12,616,898,364 |
| CF | 17 | 1,430 | 135,602,610 |
| CT | 17 | 1,430 | 135,602,610 |
| BACF | 15 | 132 | 2,244,792 |
| BAAN | 19 | 852,036 | 2,416,921,652 |
| BAON | 19 | 852,036 | 2,416,921,652 |
| BACN | 16 | 41,834 | 21,764,418 |

The exact commands are:

```sh
python3 run.py CN_LOWER1 19 runs/cn_definition.json
python3 run.py CF_LOWER1 17 runs/cf_definition.json
python3 run.py CT_LOWER1 17 runs/ct_definition.json
python3 run.py BACF_LOWER1 15 runs/bacf_definition.json
python3 run.py BAAN_LOWER1 19 runs/baan_definition.json
python3 run.py BAON_LOWER1 19 runs/baon_definition.json
python3 run.py BACN_LOWER1 16 runs/bacn_definition.json
```

The manuscript now uses the generator's uniform convention: the displayed
equations have lengths 17, 20, 20, and 17 when equality counts once.  The
17-symbol $C/f$ equation has been verified as a shortest single axiom.  The
17-symbol $C/N$ equation is the shortest currently known in that signature;
the completed weight-16 screen leaves 16 unresolved candidates, so its
shortestness remains conjectural.  The weight-19 screens for $A/N$ and $O/N$
likewise leave 294 and 295 unresolved candidates, respectively.

## Legacy baselines for comparison

Walsh's archived result stock predates Vampire 5.0.1 and is therefore a
comparison baseline, not the new reproduction itself.  The final general-filter
survivor files contain:

| Current run | Legacy label/file | Legacy survivors |
|---|---|---:|
| CN 21 | `CN21Results/.../CN_21_Remaining.txt` | 782 |
| CF 19 | `C019Results/.../C0_19_Remaining.txt` | 162 |
| CT 19 | `C119Results/.../C1_19_Remaning.txt` | 188 |

Here `C0` means the implication language whose constant is interpreted as
false, and `C1` the corresponding language whose constant is interpreted as
true.  `tools/compare_survivors.py` alpha-normalizes the current functional
TPTP formulas and legacy digit-variable Polish formulas before reporting the
intersection and both set differences.

There are no corresponding complete legacy survivor files in this result
stock for BACF, BAAN, BAON, or BACN.

## Lower-bound reproduction status

The earlier same-length diagnostic runs were stopped and preserved after the
reproduction target was narrowed to the immediately preceding lower-bound
frontier.  The seven lower-bound searches run under the reference Vampire
5.0.1 configuration as two disjoint structural-form shards per search.  The
CN, CF, and CT shards reuse the verified imported model stocks above; the four
equational searches reuse only models found and verified in current diagnostic
runs.  Each worker has a separate survivor ledger and statistics report.  No
run is recorded as complete until `tools/merge_shards.py` validates its full
pair.

The full matrix is machine-readable in
`runs/headline_reproduction_manifest.json`; `tools/run_headline_shards.py`
prints or executes those fourteen commands, appends per-shard logs, resumes
from transactional checkpoints, and merges only after both shards of a search
exit successfully.

Once an initial pair is merged, `tools/run_survivor_second_pass.py` applies a
survivor-only pass with a 10-second wall-clock limit, 6 cores, 32,000 MiB,
`casc_sat`, and `fmb_start_size=1`.  This stronger parallel envelope is kept
separate from the initial screen: it stores every raw Vampire result and writes
a resumable second-pass ledger without modifying the initial survivor file.

The large structural and instance counts above are important: the small
compatibility runs establish correctness of the repaired workflow, but they do
not constitute reproduction of the headline searches.
