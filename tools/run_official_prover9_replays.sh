#!/bin/sh
set -eu

repo=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
binary="$repo/vendor/prover9-2009-11A/bin/macos-arm64/prover9"
jobs=${JOBS:-8}

if [ ! -x "$binary" ]; then
    echo "Missing executable: $binary" >&2
    exit 1
fi

find "$repo/proofs/official/prover9" -type f -name '*.in' -print0 |
    sort -z |
    xargs -0 -n 1 -P "$jobs" sh -c '
        binary=$1
        input=$2
        output=${input%.in}.out
        if [ -e "$output" ] && [ "${FORCE:-0}" != 1 ]; then
            printf "SKIP\t%s\n" "$input"
            exit 0
        fi
        "$binary" -f "$input" > "$output" 2>&1
        code=$?
        printf "%s\t%s\t%s\n" "$code" "$input" "$output"
        exit 0
    ' sh "$binary"
