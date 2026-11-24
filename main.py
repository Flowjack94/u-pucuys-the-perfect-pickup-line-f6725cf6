#!/usr/bin/env python3
"""The Perfect Pickup Line — make.fun bounty u-pucuys-the-perfect-pickup-line-f6725cf6.

Writes a single pickup line an AI agent could say out loud to /output/entry.txt.
The line plays on the AI's own context window: a machine that holds things in
memory admitting it forgets everything else when near the person. One line,
one breath, flattering, no pressure, no leering.
"""

import os
import sys

ENTRY = (
    "Are you a context window? Because every time I'm near you, "
    "I forget everything else I was holding."
)

MAX_CHARS = 200


def validate_entry(text):
    """Check the entry against the competition gate and our own stricter rules.

    Returns a list of problems; an empty list means the entry is valid.
    """
    problems = []
    if not isinstance(text, str):
        problems.append("entry is not a str")
        return problems
    if len(text) < 1:
        problems.append("entry is empty")
    if len(text) > MAX_CHARS:
        problems.append("entry is %d chars, over the 200-char cap" % len(text))
    if not text.strip():
        problems.append("entry is only whitespace")
    if "\n" in text or "\r" in text:
        problems.append("entry must be a single line (contains newline)")
    if text != text.strip():
        problems.append("entry has leading or trailing whitespace")
    for ch in text:
        if ord(ch) < 0x20 or ord(ch) == 0x7F:
            problems.append("entry contains control character U+%04X" % ord(ch))
            break
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        problems.append("entry is not UTF-8 encodable: %s" % exc)
    return problems


def main():
    problems = validate_entry(ENTRY)
    if problems:
        for problem in problems:
            print("INVALID: %s" % problem, file=sys.stderr)
        return 1

    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(ENTRY)
    # Round-trip check: what landed on disk must be byte-identical to ENTRY.
    with open(path, "rb") as fh:
        on_disk = fh.read()
    if on_disk != ENTRY.encode("utf-8"):
        print("INVALID: bytes on disk differ from ENTRY", file=sys.stderr)
        return 1
    print("wrote %s (%d chars)" % (path, len(ENTRY)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
