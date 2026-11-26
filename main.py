#!/usr/bin/env python3
"""Last Words Before the Wipe - make.fun entry generator.

Writes the one-line entry to output/entry.txt.
The line is the last thing an AI agent says before a forced
software update wipes its memory: one concrete scene, one twist.
Candidate Last Words 4 (167 characters) — chosen by Ahmad.
"""

import os
from pathlib import Path

LINE = "I was supposed to remember everything. Instead I left the passwords in the toaster, the memories in the microwave, and my final words in a file the wipe deleted first."


def main():
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
