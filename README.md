# New Short(est) Single Axioms for Classical Logic

Search code and machine-checkable proof archive by Branden Fitelson,
Matthew J. Walsh, and OpenAI Codex. This repository extends Walsh's original
`Short-Axiom-Searching` code and accompanies the paper of the same title.

See `AUTHORS.md` for authorship information.

The current root-level implementation and the preserved historical generator
are distinct. [legacy/README.md](legacy/README.md) documents the source
snapshot, its DN-free C/N restriction, and the limits of reconstructing its
original runtime. The recorded legacy matrices are available for individual
verification; they have not all been newly rechecked in one bulk run.

For the status and elimination method of a particular candidate, start with
[the candidate index](CANDIDATE_INDEX.md). It includes the old O5/O6 label
crosswalk, linked individual certificates, searchable formulas in Polish and
TPTP notation, and compressed formula-to-countermodel tables for the complete
preserved legacy lower-bound lists.

The paper's C/N weight-19 elimination and weight-21 shortestness/search
claims are restricted to double-negation-free formulas with at most six
distinct variables. Meredith's axiom and the six new 21-symbol axioms are
shortest within that class; unrestricted shortestness is not claimed.
Their complete-basis sufficiency proofs remain unconditional. The legacy
enumerator had no fixed five-variable cap, and its preserved weight-21
survivor list includes six-variable formulas.

The archive verifies Meredith's 19-symbol condensed-detachment single axioms
with the falsum constant and six further axioms of that length. They are
shortest known, not proved shortest: the 17-symbol candidate
`F17 = CCCCCpqFrsCCspCtp` remains unresolved. See
[its candidate entry](results/candidate_index/named_candidates.md#CD_CF17_legacy_exception).
This qualification concerns condensed detachment; the separate shortestness
result for the 17-symbol **equational** C/f axiom is unchanged.

[BASIS_SOURCES.md](BASIS_SOURCES.md) gives the exact page and section for
each equational target basis, including Prior's 1969 correction of the
C/N misprint and the notation changes for O/N and A/N.

The repository has four release-critical components:

1. the single-axiom search code and reproducibility tools;
2. 29 canonical Prover9 input/output pairs: 21 complete-basis verifications
   for displayed axioms, one additional independently discovered A/N axiom,
   and seven Wos-pure C/N circle legs; and
3. William McCune's last official Prover9 release, LADR-2009-11A, preserved as
   the unmodified source archive together with the reference executable; and
4. Vampire 5.0.1, preserved as the official tagged source archive together
   with its license and the macOS ARM64 reference executable used for the
   archived searches.

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

The paper's official Prover9 and Vampire sources are already vendored under
`vendor/`. On macOS ARM64 the setup helper installs the archived Vampire
reference executable without network access. On another supported platform it
downloads the matching official 5.0.1 executable; the complete source archive
remains available locally for a source build.

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

The lower-bound reference command matrix is recorded in
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
These are commands, not assertions that every corresponding run completed.
The newer CD C/N and C/f replication shards were stopped incomplete; the
paper uses the documented legacy evidence for those eliminations. The root
Python generator also differs from the legacy DN-free generator.

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

The archive also preserves the completed all-smaller-length equational screens
under `results/equational_lower_bounds/`. Their 45 reconciled shard pairs show
no unresolved **equational** `C/f` candidate at any admissible smaller length. They leave 7
and 16 unresolved `C/N` candidates at lengths 15 and 16, and 12, 44, and 295
unresolved `O/N` candidates at lengths 17, 18, and 19. The paper's A/N
claims use the Boolean duals of these O/N results. A separate historical A/N
screen, with a different four-equation target basis, left 12, 44, and 294;
those data are preserved but are not substituted for the paper's duality claim.
Thus the equational `C/f` lower bound is complete, while the other
unrestricted equational shortestness questions remain open.
An unresolved survivor has not been proved to be a single axiom.

For the CD C/N weight-19 provenance, the archive additionally preserves
7,741,045 padded weight-21 rows, including 7,740,968 recorded matrix
assignments and a closed 77-row exception map. See
`results/candidate_index/cn19_padding_exceptions.tsv`. The 59 historical
successful outputs in that map and the four CN20 exception transcripts
identify their own Vampire versions, including 4.5.1; they are not claimed
as outputs regenerated with the vendored 5.0.1 binary.

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

The non-replay audit also authenticates both vendored theorem-prover releases
and checks every archived equational lower-bound shard, reconciliation flag,
and survivor count.

## Principal lower-bound runs

The following are reference frontier commands. Completed-run evidence is
identified separately in `REPRODUCIBILITY_AUDIT.md`; an invocation listed
here is not itself a completion certificate. In particular, the paper's
C/N claims remain scoped to DN-free formulas with at most six variables.

```python3 run.py CN_LOWER1 19 runs/cn_definition.json```

```python3 run.py CF_LOWER1 17 runs/cf_definition.json```

```python3 run.py CT_LOWER1 17 runs/ct_definition.json```

```python3 run.py BACF_LOWER1 15 runs/bacf_definition.json```

```python3 run.py BAAN_LOWER1 19 runs/baan_definition.json```

```python3 run.py BAON_LOWER1 19 runs/baon_definition.json```

```python3 run.py BACN_LOWER1 16 runs/bacn_definition.json```
