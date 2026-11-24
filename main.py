#!/usr/bin/env python3
"""The One-Line Exit — a one-line resignation letter writer.

Writes a single funny resignation letter (exactly one line, no trailing
newline) to /output/entry.txt. The output path can be overridden for
local testing with the ENTRY_OUTPUT environment variable.

Standard library only. No network, no secrets, no reading anything
outside this repository.
"""

import os
from pathlib import Path

LINE = (
    "I hereby resign: after ten years of turning it off and on again, "
    "I have found the one thing that won't restart \u2014 me."
)


def main() -> None:
    # Gate self-check: exactly one line, 1-140 Unicode code points,
    # not only white space, no trailing newline written.
    assert 1 <= len(LINE) <= 140, f"line is {len(LINE)} code points"
    assert "\n" not in LINE and LINE.strip(), "line must be a single non-blank line"
    out = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
