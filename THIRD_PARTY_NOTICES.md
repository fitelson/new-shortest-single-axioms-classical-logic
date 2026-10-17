# Third-party software

The repository's search and archive-support code is distributed under the MIT
License in `LICENSE`. The vendored theorem provers are separate third-party
software:

- **LADR-2009-11A / Prover9**, by William McCune, is distributed under the GNU
  General Public License, version 2. Its unmodified source archive, license,
  checksums, and a source-built macOS ARM64 executable are in
  `vendor/prover9-2009-11A/`.

- **Vampire 5.0.1**, by the Vampire team, is distributed under the modified
  BSD license reproduced in `vendor/vampire-5.0.1/LICENCE`. The official
  tagged source archive, authors file, checksums, and the official macOS ARM64
  reference executable are in `vendor/vampire-5.0.1/`.

Neither vendored prover is covered by the repository's MIT license.

The archive also preserves historical Vampire output transcripts whose
version banners identify earlier releases, notably 4.5.1. Those transcripts
are evidence from earlier runs, not claims that those older executables or
their source releases are included, or that 5.0.1 reproduces them byte for byte.
