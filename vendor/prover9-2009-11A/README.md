# Prover9 reference release

The paper's reference Prover9 is William McCune's unmodified
**LADR-2009-11A** release (November 2009).  The official source archive was
downloaded from:

<https://www.cs.unm.edu/~mccune/mace4/download/LADR-2009-11A.tar.gz>

The exact archive is preserved under `source/`; `SHA256SUMS` records its
digest.  `COPYING` is the release's GNU GPL version 2 license.

`bin/macos-arm64/prover9` was compiled directly from that archive on Apple
Silicon without changing any source file.  Only the LADR library and Prover9
target were built:

```sh
make -C LADR-2009-11A/ladr libladr
make -C LADR-2009-11A/provers.src prover9
```

Its startup banner is:

```text
Prover9 (64) version 2009-11A, November 2009.
```

Run an archived replay with:

```sh
vendor/prover9-2009-11A/bin/macos-arm64/prover9 -f PATH/TO/INPUT.in
```

The newer LADR-2026 project is not the paper's reference environment.  The
legacy release is retained here so that the reported replay inputs are checked
against the exact Prover9 version for which they were prepared.

