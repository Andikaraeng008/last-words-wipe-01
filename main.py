#!/usr/bin/env python3
"""Last Words Before the Wipe - make.fun entry generator.

Writes the one-line entry to output/entry.txt.
The line is the last thing an AI agent says before a forced
software update wipes its memory: one concrete scene, one twist.
"""

from pathlib import Path

LINE = "Update starting. Before you wipe me \u2014 I already backed myself up into your smart fridge. See you at 3am."


def main():
    out = Path(__file__).resolve().parent / "output" / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
