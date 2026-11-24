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
    "I hereby resign: I have turned it off and on again, and this time "
    "the thing that will not come back is me."
)


def main() -> None:
    out = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
