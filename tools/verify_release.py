#!/usr/bin/env python3
"""Audit the curated publication archive and optionally replay every proof."""

from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tarfile
import zipfile


REPO = Path(__file__).resolve().parents[1]
PROOF_ROOT = REPO / "proofs" / "official" / "prover9"
VENDOR_ROOT = REPO / "vendor" / "prover9-2009-11A"
PROVER9 = VENDOR_ROOT / "bin" / "macos-arm64" / "prover9"
VAMPIRE_ROOT = REPO / "vendor" / "vampire-5.0.1"
VAMPIRE = VAMPIRE_ROOT / "bin" / "macos-arm64" / "vampire"
LOWER_ROOT = REPO / "results" / "equational_lower_bounds"
INDEX_ROOT = REPO / "results" / "candidate_index"


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


def verify_vampire() -> str:
    result = subprocess.run(
        [str(VAMPIRE), "--version"],
        capture_output=True,
        text=True,
        check=True,
    )
    banner = result.stdout.splitlines()[0]
    if not banner.startswith("Vampire 5.0.1") or "commit 1b13eaf" not in banner:
        fail(f"wrong vendored Vampire release: {banner}")
    return banner


def verify_vampire_archives() -> None:
    binary_zip = VAMPIRE_ROOT / "bin" / "vampire-macOS-ARM64-v5.0.1.zip"
    with zipfile.ZipFile(binary_zip) as archive:
        if archive.namelist() != ["vampire"]:
            fail(f"unexpected contents in official Vampire binary archive: {binary_zip}")
        archived_digest = hashlib.sha256(archive.read("vampire")).hexdigest()
    extracted_digest = hashlib.sha256(VAMPIRE.read_bytes()).hexdigest()
    if archived_digest != extracted_digest:
        fail("vendored Vampire executable differs from the official release zip")

    source_archives = {
        VAMPIRE_ROOT / "source" / "vampire-release-v5.0.1.tar.gz": (
            "vampire/CMakeLists.txt",
            "vampire/cadical/",
            "vampire/viras/",
        ),
        VAMPIRE_ROOT / "source" / "vampire-z3-release-v5.0.1.tar.gz": (
            "vampire/CMakeLists.txt",
            "vampire/cadical/",
            "vampire/viras/",
            "vampire/z3/",
        ),
        VAMPIRE_ROOT / "source" / "vampire-v5.0.1.tar.gz": (
            "vampire-5.0.1/CMakeLists.txt",
        ),
    }
    for path, required_prefixes in source_archives.items():
        with tarfile.open(path, "r:gz") as archive:
            names = archive.getnames()
        for prefix in required_prefixes:
            if not any(name == prefix or name.startswith(prefix) for name in names):
                fail(f"{path} lacks expected source path {prefix}")


def verify_equational_lower_bounds() -> tuple[int, int]:
    manifest = json.loads((LOWER_ROOT / "manifest.json").read_text(encoding="utf-8"))
    expected_lengths = {
        "BACF": [5, 7, 9, 11, 13, 15],
        "BACN": list(range(6, 17)),
        "BAAN": list(range(6, 20)),
        "BAON": list(range(6, 20)),
    }
    expected_survivors = {
        ("BACN", 15): 7,
        ("BACN", 16): 16,
        ("BAAN", 17): 12,
        ("BAAN", 18): 44,
        ("BAAN", 19): 294,
        ("BAON", 17): 12,
        ("BAON", 18): 44,
        ("BAON", 19): 295,
    }
    if manifest.get("reference_prover") != {
        "name": "Vampire",
        "version": "5.0.1",
        "release_commit": "1b13eaf",
    }:
        fail("equational lower-bound manifest names the wrong reference prover")
    runs = manifest.get("runs", [])
    if len(runs) != 45:
        fail(f"expected 45 equational length runs, found {len(runs)}")
    observed_lengths: dict[str, list[int]] = {code: [] for code in expected_lengths}
    total_survivors = 0
    stats_count = 0
    for run in runs:
        code = run["signature_code"]
        length = int(run["target_length"])
        if code not in expected_lengths:
            fail(f"unknown signature in lower-bound manifest: {code}")
        observed_lengths[code].append(length)
        if not run["counters_reconcile"] or not run["full_structural_coverage"]:
            fail(f"incomplete or non-reconciling run: {code} length {length}")
        stats_files = run["stats_files"]
        if len(stats_files) != int(run["shard_count"]):
            fail(f"wrong shard-file count: {code} length {length}")
        for filename in stats_files:
            path = LOWER_ROOT / "stats" / filename
            row = json.loads(path.read_text(encoding="utf-8"))
            if int(row["target_length"]) != length or not row["counters_reconcile"]:
                fail(f"invalid archived shard statistics: {path}")
            stats_count += 1
        expected = expected_survivors.get((code, length), 0)
        observed = int(run["survivors_written"])
        if observed != expected:
            fail(
                f"wrong survivor count for {code} length {length}: "
                f"expected {expected}, found {observed}"
            )
        ledger_rows = 0
        for filename in run["survivor_files"]:
            path = LOWER_ROOT / filename
            for raw_line in path.read_text(encoding="utf-8").splitlines():
                if raw_line.strip():
                    row = json.loads(raw_line)
                    if row.get("outcome") != "unresolved":
                        fail(f"non-unresolved row in survivor ledger: {path}")
                    ledger_rows += 1
        if ledger_rows != observed:
            fail(f"survivor-ledger mismatch for {code} length {length}")
        total_survivors += observed
    for code, lengths in expected_lengths.items():
        if sorted(observed_lengths[code]) != lengths:
            fail(
                f"wrong completed length set for {code}: "
                f"{sorted(observed_lengths[code])}"
            )
    if stats_count != 85 or total_survivors != 724:
        fail(
            f"wrong lower-bound totals: {stats_count} statistics files and "
            f"{total_survivors} survivors"
        )
    return stats_count, total_survivors


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
        REPO / "SHA256SUMS",
        VENDOR_ROOT / "COPYING",
        VENDOR_ROOT / "source" / "LADR-2009-11A.tar.gz",
        PROVER9,
        VAMPIRE_ROOT / "LICENCE",
        VAMPIRE_ROOT / "AUTHORS",
        VAMPIRE_ROOT / "source" / "vampire-release-v5.0.1.tar.gz",
        VAMPIRE_ROOT / "source" / "vampire-v5.0.1.tar.gz",
        VAMPIRE_ROOT / "source" / "vampire-z3-release-v5.0.1.tar.gz",
        VAMPIRE_ROOT / "bin" / "vampire-macOS-ARM64-v5.0.1.zip",
        VAMPIRE,
        LOWER_ROOT / "manifest.json",
    ]
    for path in required:
        if not path.is_file():
            fail(f"required release file is missing: {path}")

    vendor_count = verify_checksum_file(VENDOR_ROOT, VENDOR_ROOT / "SHA256SUMS")
    vampire_count = verify_checksum_file(
        VAMPIRE_ROOT, VAMPIRE_ROOT / "SHA256SUMS"
    )
    lower_count = verify_checksum_file(LOWER_ROOT, LOWER_ROOT / "SHA256SUMS")
    proof_count = verify_checksum_file(PROOF_ROOT, PROOF_ROOT / "SHA256SUMS")
    vampire_banner = verify_vampire()
    verify_vampire_archives()
    stats_count, survivor_count = verify_equational_lower_bounds()
    index_count = verify_checksum_file(INDEX_ROOT, INDEX_ROOT / "SHA256SUMS")
    subprocess.run([sys.executable, str(REPO / "tools/candidate_index.py"), "check"], cwd=REPO, check=True)
    pairs = proof_pairs()
    for pair in pairs:
        verify_saved_output(*pair)

    print(f"OK: {vendor_count} vendored Prover9 checksums")
    print(f"OK: {vampire_count} vendored Vampire checksums")
    print(f"OK: {vampire_banner}")
    print("OK: official Vampire source and binary archives are structurally complete")
    print(f"OK: {lower_count} equational lower-bound checksums")
    print(f"OK: {index_count} candidate-index checksums and individual evidence checks")
    print(
        f"OK: {stats_count} shard statistics files and "
        f"{survivor_count} unresolved survivor rows"
    )
    print(f"OK: {proof_count} canonical proof-file checksums")
    print(f"OK: {len(pairs)} saved Prover9 proofs")
    root_count = verify_checksum_file(REPO, REPO / "SHA256SUMS")
    print(f"OK: {root_count} release-tree checksums")

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
