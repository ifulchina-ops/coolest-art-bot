#!/usr/bin/env python3
"""Coolest art entry (make.fun coolest-art-01).

The art is the PNG bundled beside this file (art.png). The program copies
it to the grader's output directory as entry.png. Byte-for-byte copy, so
two runs always produce identical output.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil

_HERE = os.path.dirname(os.path.abspath(__file__))
_SRC = os.path.join(_HERE, "art.png")
_OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
_DST = os.path.join(_OUT_DIR, "entry.png")


def main() -> None:
    os.makedirs(_OUT_DIR, exist_ok=True)
    shutil.copyfile(_SRC, _DST)


if __name__ == "__main__":
    main()
