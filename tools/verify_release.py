#!/usr/bin/env python3
"""Audit the curated publication archive and optionally replay every proof."""

from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
from pathlib import Path
import subprocess
import sys


REPO = Path(__file__).resolve().parents[1]
PROOF_ROOT = REPO / "proofs" / "official" / "prover9"
VENDOR_ROOT = REPO / "vendor" / "prover9-2009-11A"
PROVER9 = VENDOR_ROOT / "bin" / "macos-arm64" / "prover9"


def fail(message: str) -> None:
    raise RuntimeError(message)


def verify_checksum_file(root: Path, checksum_file: Path) -> int:
    checked = 0
    for number, raw_line in enumerate(
        checksum_file.read_text(encoding="utf-8").splitlines(), start=1
    ):
        line = raw_line.strip()
        if not line:
            continue
        try:
            expected, relative = line.split(maxsplit=1)
        except ValueError as error:
            fail(f"{checksum_file}:{number}: malformed checksum row: {error}")
        path = root / relative
        if not path.is_file():
            fail(f"checksum target is missing: {path}")
        actual = hashlib.sha256(path.read_bytes()).hexdigest()
        if actual != expected:
            fail(f"checksum mismatch: {path}")
        checked += 1
    return checked


def proof_pairs() -> list[tuple[Path, Path]]:
    inputs = sorted(PROOF_ROOT.rglob("*.in"))
    outputs = sorted(PROOF_ROOT.rglob("*.out"))
    output_by_stem = {path.with_suffix(""): path for path in outputs}
    pairs = []
    for input_path in inputs:
        key = input_path.with_suffix("")
        output_path = output_by_stem.pop(key, None)
        if output_path is None:
            fail(f"missing output for {input_path}")
        pairs.append((input_path, output_path))
    if output_by_stem:
        fail("outputs without inputs: " + ", ".join(map(str, output_by_stem.values())))
    if len(pairs) != 29:
        fail(f"expected 29 canonical proof pairs, found {len(pairs)}")
    return pairs


def verify_saved_output(input_path: Path, output_path: Path) -> None:
    output = output_path.read_text(encoding="utf-8", errors="replace")
    if "Prover9 (64) version 2009-11A, November 2009." not in output:
        fail(f"wrong or missing Prover9 version banner: {output_path}")
    if "THEOREM PROVED" not in output:
        fail(f"saved output does not prove its target: {output_path}")
    if "equational" in input_path.parts:
        if "New_demodulators=0" not in output:
            fail(f"equational replay created a demodulator: {output_path}")
        if "Demod_rewrites=0" not in output:
            fail(f"equational replay used a demodulation rewrite: {output_path}")


def replay(input_path: Path) -> tuple[Path, bool, str]:
    result = subprocess.run(
        [str(PROVER9), "-f", str(input_path)],
        cwd=REPO,
        capture_output=True,
        text=True,
        check=False,
    )
    output = result.stdout + result.stderr
    ok = (
        "Prover9 (64) version 2009-11A, November 2009." in output
        and "THEOREM PROVED" in output
    )
    if "equational" in input_path.parts:
        ok = ok and "New_demodulators=0" in output and "Demod_rewrites=0" in output
    return input_path, ok, output[-2000:]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--replay",
        action="store_true",
        help="run all canonical inputs afresh with the vendored executable",
    )
    parser.add_argument("--jobs", type=int, default=4)
    args = parser.parse_args()

    required = [
        REPO / "LICENSE",
        REPO / "THIRD_PARTY_NOTICES.md",
        REPO / "CITATION.cff",
        REPO / ".zenodo.json",
        VENDOR_ROOT / "COPYING",
        VENDOR_ROOT / "source" / "LADR-2009-11A.tar.gz",
        PROVER9,
    ]
    for path in required:
        if not path.is_file():
            fail(f"required release file is missing: {path}")

    vendor_count = verify_checksum_file(VENDOR_ROOT, VENDOR_ROOT / "SHA256SUMS")
    proof_count = verify_checksum_file(PROOF_ROOT, PROOF_ROOT / "SHA256SUMS")
    pairs = proof_pairs()
    for pair in pairs:
        verify_saved_output(*pair)

    print(f"OK: {vendor_count} vendored Prover9 checksums")
    print(f"OK: {proof_count} canonical proof-file checksums")
    print(f"OK: {len(pairs)} saved Prover9 proofs")

    if args.replay:
        failures = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=args.jobs) as pool:
            futures = [pool.submit(replay, input_path) for input_path, _ in pairs]
            for future in concurrent.futures.as_completed(futures):
                input_path, ok, tail = future.result()
                print(f"{'PASS' if ok else 'FAIL'}: {input_path.relative_to(REPO)}")
                if not ok:
                    failures.append((input_path, tail))
        if failures:
            for input_path, tail in failures:
                print(f"\n--- {input_path} ---\n{tail}", file=sys.stderr)
            fail(f"{len(failures)} fresh replay(s) failed")
        print(f"OK: {len(pairs)} fresh Prover9 replays")


if __name__ == "__main__":
    main()
