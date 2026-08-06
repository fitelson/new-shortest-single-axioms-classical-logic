#!/usr/bin/env python3
"""Verify and safely restore packaged finite-model stocks."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import tarfile


REPO = Path(__file__).resolve().parents[1]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def restore(archive_path: Path, destination: Path, expected_digest: str) -> int:
    actual_digest = sha256(archive_path)
    if actual_digest != expected_digest:
        raise RuntimeError(f"checksum mismatch for {archive_path.name}")
    restored = 0
    with tarfile.open(archive_path, mode="r:gz") as archive:
        for member in archive.getmembers():
            parts = PurePosixPath(member.name).parts
            if not member.isfile() or not parts or any(part in ("", ".", "..") for part in parts):
                raise RuntimeError(f"unsafe archive member: {member.name}")
            target = destination.joinpath(*parts)
            source = archive.extractfile(member)
            if source is None:
                raise RuntimeError(f"missing archive data: {member.name}")
            data = source.read()
            if target.exists():
                if target.read_bytes() != data:
                    raise RuntimeError(f"refusing to overwrite different file: {target}")
                continue
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
            restored += 1
    return restored


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--archive_dir", type=Path, default=REPO / "data" / "model_stocks"
    )
    parser.add_argument("--destination", type=Path, default=REPO / "CounterModels")
    parser.add_argument("--only", nargs="*", default=[])
    args = parser.parse_args()

    manifest = json.loads((args.archive_dir / "manifest.json").read_text(encoding="utf-8"))
    selected = set(args.only)
    total = 0
    seen = set()
    for stock in manifest["stocks"]:
        namespace = stock["namespace"]
        if selected and namespace not in selected:
            continue
        seen.add(namespace)
        restored = restore(
            args.archive_dir / stock["archive"], args.destination, stock["sha256"]
        )
        total += restored
        final_count = len(list((args.destination / namespace).glob("*")))
        if final_count != stock["files"]:
            raise RuntimeError(
                f"file-count mismatch for {namespace}: {final_count} != {stock['files']}"
            )
        print(f"{namespace}: restored {restored}, verified {final_count}")
    if selected - seen:
        raise RuntimeError("unknown namespaces: " + ", ".join(sorted(selected - seen)))
    print(f"restored {total} new files")


if __name__ == "__main__":
    main()
