#!/usr/bin/env python3
"""Worst Superpower — make.fun entry.

Writes one line (at most 140 characters) inventing the most useless
superpower imaginable to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Pure standard library, no network, no input files.
"""

import os
import sys

ENTRY = "I can hear what my plants are thinking, but only when they're disappointed in me."

MAX_CHARS = 140


def main() -> int:
    text = ENTRY
    if not (1 <= len(text) <= MAX_CHARS):
        print(f"entry must be 1-{MAX_CHARS} chars, got {len(text)}", file=sys.stderr)
        return 1
    if text.strip() != text or "\n" in text:
        print("entry must be a single line with no surrounding whitespace", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    # Re-read and verify the bytes we just wrote.
    with open(path, "rb") as f:
        raw = f.read()
    written = raw.decode("utf-8")
    if written != text + "\n":
        print("verification failed: entry.txt does not match the entry", file=sys.stderr)
        return 1
    if written.count("\n") != 1:
        print("verification failed: entry.txt must hold exactly one line", file=sys.stderr)
        return 1
    print(f"wrote {len(raw)} bytes to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
