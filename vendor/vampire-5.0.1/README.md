# Vampire 5.0.1 reference release

This directory preserves the exact Vampire release used for the archived
single-axiom screens.

- `source/vampire-release-v5.0.1.tar.gz` is the official release source asset,
  including the CaDiCaL and VIRAS source trees.
- `source/vampire-z3-release-v5.0.1.tar.gz` is the official release source
  asset with the optional Z3 source tree included as well.
- `source/vampire-v5.0.1.tar.gz` is GitHub's automatic source snapshot of the
  official `v5.0.1` tag (release commit `1b13eaf`); it is retained as an
  independent tag-level reference but does not populate submodules.
- `bin/vampire-macOS-ARM64-v5.0.1.zip` is the unmodified official binary
  release asset. `bin/macos-arm64/vampire` is its extracted executable and is
  the reference binary used for the archived searches. Their executable bytes
  have the same SHA-256 digest.
- `LICENCE` and `AUTHORS` are copied without alteration from that source
  release.
- `SHA256SUMS` authenticates every redistributed Vampire file in this
  directory except itself.

On macOS ARM64, `python3 setup.py` installs the vendored executable into the
Git-ignored working path `theorem_provers/vampire`. On another platform the
setup helper downloads the corresponding official 5.0.1 executable, or the
source archive here may be built according to Vampire's own build
instructions included in the source release. A rebuild need not be
byte-identical to the reference binary, but it must report Vampire 5.0.1 and
release commit `1b13eaf` before it is used for a paper-facing reproduction.

Vampire is third-party software governed by the license in `LICENCE`; it is
not covered by this repository's MIT license.
