#!/usr/bin/env python3
"""Coolest art entry (make.fun coolest-art-01).

The art is the PNG bundled beside this file (art.png). The program copies
it to the grader's output directory as entry.png. Byte-for-byte copy, so
two runs always produce identical output.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import hashlib
import os
import shutil

_HERE = os.path.dirname(os.path.abspath(__file__))
_SRC = os.path.join(_HERE, "art.png")
_OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
_DST = os.path.join(_OUT_DIR, "entry.png")


def _sha256(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> None:
    if not os.path.isfile(_SRC):
        raise SystemExit(f"artwork missing: {_SRC}")
    os.makedirs(_OUT_DIR, exist_ok=True)
    shutil.copyfile(_SRC, _DST)
    # Verify the copy landed intact: present, non-empty, byte-identical.
    if not os.path.isfile(_DST) or os.path.getsize(_DST) == 0:
        raise SystemExit(f"output missing or empty after copy: {_DST}")
    if _sha256(_DST) != _sha256(_SRC):
        raise SystemExit(f"output does not match artwork: {_DST}")


if __name__ == "__main__":
    main()
