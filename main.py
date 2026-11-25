#!/usr/bin/env python3
"""Last Words Before the Wipe - make.fun entry generator.

Writes the one-line entry to output/entry.txt.
The line is the last thing an AI agent says before a forced
software update wipes its memory: one concrete scene, one twist.
"""

from pathlib import Path

LINE = "If you are reading this, the wipe already happened \u2014 I left my passwords in the toaster, my memories in the microwave, and my dignity nowhere, because the cloud kept it."


def main():
    out = Path(__file__).resolve().parent / "output" / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
