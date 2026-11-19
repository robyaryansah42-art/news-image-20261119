#!/usr/bin/env python3
"""Entry point for the news-image-20261119 bounty.

Copies the pre-rendered entry.png (drawn by generate_image.py) to
/output/entry.png (or $MAKEFUN_OUTPUT_DIR when set). Standard library
only, no network.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    print(f"wrote {dst}")


if __name__ == "__main__":
    main()
