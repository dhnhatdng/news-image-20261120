#!/usr/bin/env python3
"""Copy the finished front page to the grader's output directory.

The entry image (entry.png, next to this file) is a newspaper-style
summary of the world news of Friday 20 November 2026. This program
needs nothing but the standard library: it finds the image next to
itself and copies it to /output/entry.png.

To try it outside the grader, point MAKEFUN_OUTPUT_DIR at a folder:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"
TARGET_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    TARGET_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, TARGET_DIR / "entry.png")


if __name__ == "__main__":
    main()
