#!/usr/bin/env python3
"""Create deterministic, checksummed archives of verified model stocks."""

from __future__ import annotations

import argparse
import gzip
import hashlib
import io
import json
from pathlib import Path
import tarfile


REPO = Path(__file__).resolve().parents[1]
DEFAULT_NAMESPACES = ("REPRO_CN_V501", "REPRO_CF_V501", "REPRO_CT_V501")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def build_archive(namespace: str, output: Path) -> dict:
    source_dir = REPO / "CounterModels" / namespace
    files = sorted(path for path in source_dir.iterdir() if path.is_file())
    if not files:
        raise RuntimeError(f"no model files found in {source_dir}")
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("wb") as raw:
        with gzip.GzipFile(filename="", mode="wb", fileobj=raw, mtime=0) as compressed:
            with tarfile.open(fileobj=compressed, mode="w") as archive:
                for path in files:
                    data = path.read_bytes()
                    info = tarfile.TarInfo(f"{namespace}/{path.name}")
                    info.size = len(data)
                    info.mode = 0o644
                    info.mtime = 0
                    info.uid = info.gid = 0
                    info.uname = info.gname = ""
                    archive.addfile(info, io.BytesIO(data))
    return {
        "namespace": namespace,
        "archive": output.name,
        "files": len(files),
        "bytes": output.stat().st_size,
        "sha256": sha256(output),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("namespaces", nargs="*", default=DEFAULT_NAMESPACES)
    parser.add_argument(
        "--output_dir", type=Path, default=REPO / "data" / "model_stocks"
    )
    args = parser.parse_args()

    stocks = []
    for namespace in args.namespaces:
        output = args.output_dir / f"{namespace}.tar.gz"
        stocks.append(build_archive(namespace, output))
    manifest = {
        "schema_version": 1,
        "archive_format": "deterministic tar.gz (mtime=0, uid=gid=0)",
        "stocks": stocks,
    }
    manifest_path = args.output_dir / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
