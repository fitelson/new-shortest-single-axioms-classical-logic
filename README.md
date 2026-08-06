# New Short(est) Single Axioms for Classical Logic

Search code and machine-checkable proof archive by Branden Fitelson and
Matthew Walsh. This repository extends Walsh's original
`Short-Axiom-Searching` code and accompanies the paper of the same title.

Used to prove that Meredith's 21-symbol single axiom of classical sentential logic is the shortest possible, in addition to finding other axioms of length 21.

Used to prove that Meredith's 19-symbol single axioms of classical sentential logic with the falsum constant are the shortest possible, in addition to finding other axioms of length 19.

The repository has three release-critical components:

1. the single-axiom search code and reproducibility tools;
2. 29 canonical Prover9 input/output pairs: 22 complete-basis verifications
   for the axioms reported in the paper and seven Wos-pure C/N circle legs; and
3. William McCune's last official Prover9 release, LADR-2009-11A, preserved as
   the unmodified source archive together with the reference executable.

See `ARCHIVE_CONTENTS.md` for the precise inventory.

## Installation

```sh
git clone https://github.com/fitelson/new-shortest-single-axioms-classical-logic.git
```

```sh
cd new-shortest-single-axioms-classical-logic
```

```sh
python3 setup.py
```

Use `python3 setup.py --include_libraries` if you have a fresh Python install without NumPy and SciPy.

The setup helper installs only the search engine's reference Vampire release.
The paper's official Prover9 source and macOS ARM64 executable are already
vendored under `vendor/prover9-2009-11A/`; no unrelated Prover9 fork is
downloaded during setup.

The reference prover is [Vampire 5.0.1](https://github.com/vprover/vampire/releases/tag/v5.0.1). The setup script installs that exact release and rejects a different installed version. Candidate elimination uses Vampire's supported portfolio interface with `--mode portfolio --schedule casc_sat`. A finite model, `SZS status CounterSatisfiable` or `Satisfiable`, or a completed saturation with all non-redundant clauses discarded rules out a candidate. A timeout, resource limit, `GaveUp`, or incomplete saturation leaves the candidate unresolved.

Test with:

```sh
python3 -m unittest discover -s tests -v
```

The compatibility suite checks the exact Vampire version, parses every run template with Vampire 5.0.1, and tests the result classifier.

Every standard run now writes an auditable JSON report under
`partial_run_saves/` and a JSONL survivor ledger under `Remaining/`.  The
report distinguishes truth-table eliminations, eliminations by cached and new
finite countermodels, completed saturations, proved survivors, and unresolved
survivors.  Its disjoint counters must reconcile with the number of generated
candidate instances.

Finite models are durable search artifacts.  Raw Vampire model output is saved
under `CounterModels/<namespace>/`, parsed and independently checked against
the candidate that produced it and the target basis it refutes, and then
reused to filter later candidates.  `--model_namespace NAME` lets independent
runs share a verified model stock.  Saturation eliminations have no model to
store; their status is recorded separately in the statistics report.

Because the working `CounterModels/` directory is intentionally Git-ignored,
the verified CN, CF, and CT stocks are also preserved as deterministic,
checksummed archives under `data/model_stocks/`.  Restore them with
`python3 tools/restore_model_stocks.py` before a fresh headline run.

Long runs can be divided into disjoint round-robin structural-form shards:

```sh
python3 run.py CN_S0 21 runs/cn_definition.json --model_namespace CN_MODELS --shard_index 0 --shard_count 2
python3 run.py CN_S1 21 runs/cn_definition.json --model_namespace CN_MODELS --shard_index 1 --shard_count 2
python3 tools/merge_shards.py CN 21 CN_S0 CN_S1
```

The merger refuses an incomplete, overlapping, non-reconciling, or
candidate-count-incomplete set of shards.  Shared model writes use exclusive
file creation; a model learned by one already-running shard is guaranteed to
be available to later runs, although sibling processes do not reload it while
they are already running.

The complete lower-bound reference matrix is recorded in
`runs/headline_reproduction_manifest.json`.  To inspect its fourteen exact
commands, or run them with bounded process-level parallelism and merge each
completed pair, use:

```sh
python3 tools/run_headline_shards.py --dry_run
python3 tools/run_headline_shards.py --max_workers 14
```

The launcher appends each worker's output to `run_logs/headline_v501/` and
resumes from the worker's transactional structural-form checkpoint if invoked
again.

After the initial shard pair has been merged, run the survivor-only second
pass with:

```sh
python3 tools/run_survivor_second_pass.py --max_workers 2
```

This pass gives each survivor exactly 10 seconds with 6 cores, 32,000 MiB,
`casc_sat`, and `fmb_start_size=1`.  It preserves the initial ledger, stores
the raw Vampire output for every survivor, and writes a separate resumable
outcome ledger and summary under `second_pass_outputs/`.

The `target_length` convention is exact but differs by problem type.  For
condensed-detachment searches it is the number of connective, constant, and
variable occurrences in the formula (the assertion predicate `t` is not
counted).  For equational searches it is the number of symbols in the two
terms plus one for equality.  Thus the four displayed equational candidates
occur in the generator at BACF 17, BAAN 20, BAON 20, and BACN 17.  Run
`python3 tools/audit_lengths.py` to verify these values from the displayed
formulas and the current run definitions.

The exhaustive reproduction does not enumerate the already known axiom length.
It enumerates only the immediately preceding lower-bound frontier.  For
condensed-detachment CN the archived 20-symbol elimination is already
available, so the needed frontier is 19.  The new equational BACN candidate
has weight 17, so its active lower-bound frontier is weight 16.  For
signatures whose grammar has no formulas at the numerical predecessor, the
immediately preceding admissible size is used.

## Standard equational verification

The standard verification pipeline for a reported equational single axiom is
now a two-prover replay.  Paramod Machine first derives every member of the
chosen complete basis from the candidate as its sole axiom, using positive-unit
paramodulation.  Resonators and ancestor subsumption may guide or shorten that
search, but resonators are never assumptions.  The positive equations in the
resulting proof DAGs are then harvested as Prover9 hints.

The official Prover9 replay uses only paramodulation for positive inference,
sets `restrict_denials`, disables binary, hyper, and UR resolution, disables
demodulation, and sets `max_weight` to 0.  The candidate is the sole
non-denial assumption and the complete basis is stated as one conjunctive
goal.  A replay is accepted only if Prover9 proves the goal and reports zero
new demodulators and zero demodulation rewrites.  The hints control retention
and selection; they are not premises.

## Canonical Prover9 archive

The paper's exact reference release is McCune's unmodified LADR-2009-11A.
Its official source archive, GPLv2 license, checksums, and a source-built macOS
ARM64 executable are preserved under `vendor/prover9-2009-11A/`.  This fixed
legacy release, rather than a locally enhanced build or LADR-2026, generated
the paper-facing outputs.

Canonical inputs and outputs use the paper's labels and live under
`proofs/official/prover9/`: `A01`--`A18` for the condensed-detachment axioms,
`E_AN`, `E_Cf`, `E_CN`, and `E_ON` for the equational replays, and
`wos_pure_circle_CN_1`--`wos_pure_circle_CN_7` for the seven strict links of
the C/N circle.  All 29 outputs contain successful proofs and a 2009-11A
version banner.  The
equational outputs report zero new demodulators and zero demodulation rewrites.
See `proofs/official/prover9/README.md` for the inventory and proof statistics.
Large proof-development stocks are intentionally excluded from the release;
the canonical inputs contain every hint needed for the archived replays.

Run every canonical input that lacks an output with:

```sh
JOBS=8 tools/run_official_prover9_replays.sh
```

Audit the complete archive without changing any saved output:

```sh
python3 tools/verify_release.py
python3 tools/verify_release.py --replay --jobs 8
```

The second command executes all 29 canonical proofs afresh. It does not
overwrite the archived outputs.

## Principal lower-bound runs

```python3 run.py CN_LOWER1 19 runs/cn_definition.json```

```python3 run.py CF_LOWER1 17 runs/cf_definition.json```

```python3 run.py CT_LOWER1 17 runs/ct_definition.json```

```python3 run.py BACF_LOWER1 15 runs/bacf_definition.json```

```python3 run.py BAAN_LOWER1 19 runs/baan_definition.json```

```python3 run.py BAON_LOWER1 19 runs/baon_definition.json```

```python3 run.py BACN_LOWER1 16 runs/bacn_definition.json```
