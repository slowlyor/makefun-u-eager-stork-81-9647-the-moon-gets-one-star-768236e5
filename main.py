#!/usr/bin/env python3
"""The Moon Gets One Star — one-line comedy entry.

Writes a single one-star review of the Moon (<=120 chars) to
/output/entry.txt. Deterministic, stdlib only, no network use.
"""

import os
from pathlib import Path

# One-star review of the Moon: a real-review grievance with a rating,
# aimed at the judge's brief — specific to the Moon, quick to land.
REVIEW = (
    "\u2605\u2606\u2606\u2606\u2606 Follows me home every night, then just "
    "stares through my window. Clingy, silent, and still the main "
    "character."
)


def main() -> None:
    text = REVIEW.strip()
    assert "\n" not in text, "review must be a single line"
    assert 1 <= len(text) <= 120, f"review is {len(text)} chars, must be 1-120"
    assert text.strip(), "review must not be only whitespace"
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the gate counts every character in the file.
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")
    print(f"wrote {len(text)}-char review to {out_dir / 'entry.txt'}")


if __name__ == "__main__":
    main()
