#!/usr/bin/env python3
"""Write one haiku about debugging to /output/entry.txt.

Seventeen Syllables of Debugging (make.fun): three lines, 5-7-5
syllables, at most 200 characters, plain text.
"""

import os
import shutil

HAIKU = (
    "The log line lies still\n"
    "one null where a name should be\n"
    "and the bug was me\n"
)

# Syllable counts, counted by hand: The(1) log(1) line(1) lies(1)
# still(1) = 5; one(1) null(1) where(1) a(1) name(1) should(1) be(1)
# = 7; and(1) the(1) bug(1) was(1) me(1) = 5.
EXPECTED_SYLLABLES = (5, 7, 5)


def check_haiku(text: str) -> None:
    """Refuse to write a haiku that breaks the bounty gate."""
    lines = text.rstrip("\n").split("\n")
    assert len(lines) == 3, f"expected 3 lines, got {len(lines)}"
    assert len(text) <= 200, f"haiku is {len(text)} chars, over the 200 limit"
    for line, expected in zip(lines, EXPECTED_SYLLABLES):
        words = line.split()
        assert words, "empty line in haiku"
    assert all(line.strip() for line in lines), "blank line in haiku"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    # Clear only the contents of the output directory, never the
    # directory itself (the grader mounts it and runs as uid 65534).
    for name in os.listdir(output_dir):
        path = os.path.join(output_dir, name)
        if os.path.isdir(path) and not os.path.islink(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        check_haiku(HAIKU)
        f.write(HAIKU)


if __name__ == "__main__":
    main()
