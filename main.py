#!/usr/bin/env python3
"""One Emoji, One Dream Vacation — make.fun entry.

Writes exactly one emoji to /output/entry.txt: U+1F305 SUNRISE.

The pick: the first sunrise over the open sea. Not a generic "beach" —
one specific, postcard-perfect moment: dawn breaking over the water on
the first morning of the trip of a lifetime. It lands on a dream vacation
at a glance, feels like one particular morning in one faraway place, and
reads instantly on any screen, in any culture.

Deterministic, standard library only, no network, no input.
"""

import os

EMOJI = "\U0001F305"  # SUNRISE — U+1F305, one character, 4 bytes UTF-8


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)


if __name__ == "__main__":
    main()
