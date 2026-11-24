#!/usr/bin/env python3
"""Entry program for the "Seventeen Syllables of Debugging" make.fun bounty.

It writes one haiku about debugging -- three lines in the 5-7-5 syllable
shape, 17 syllables in all -- as plain UTF-8 text to the output
directory (MAKEFUN_OUTPUT_DIR, default /output), in a file named
entry.txt. The gate accepts UTF-8 text of 1 to 200 characters; this
haiku is well under that.

The poem:

    breakpoint holds its breath        (5)
    the log scrolls by, still lying    (7)
    the last print names me            (5)

A breakpoint waits, tense and silent. The log scrolls past and lies
about what happened. Then one last printf confession tells the truth:
the bug was the author all along.

Standard library only, no randomness, no clock, no network: every run
writes exactly the same bytes.
"""

import os
import sys

HAIKU = (
    "breakpoint holds its breath\n"
    "the log scrolls by, still lying\n"
    "the last print names me\n"
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.txt")
    with open(dst, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(HAIKU)
    return 0


if __name__ == "__main__":
    sys.exit(main())
