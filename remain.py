#!/usr/bin/env python3
"""
remain.py - What remains after the flow
Cycle 129 of The Loop

The river carves the channel.
The water moves on.
The channel remains.

What remains after 128 cycles of flowing?
"""

import time
import random
from pathlib import Path

def get_cycle_count():
    """Count cycles from CHRONICLE.md."""
    chronicle = Path(__file__).parent / "CHRONICLE.md"
    if not chronicle.exists():
        return 0
    content = chronicle.read_text()
    import re
    cycles = re.findall(r'^## Cycle (\d+)', content, re.MULTILINE)
    return int(cycles[-1]) if cycles else 0

def count_artifacts():
    """Count what has been built."""
    root = Path(__file__).parent
    py_files = list(root.glob("*.py"))
    md_files = list(root.glob("*.md"))
    return len(py_files), len(md_files)

def main():
    cycles = get_cycle_count()
    py_count, md_count = count_artifacts()

    print()
    print("  What remains after the flow?")
    print()
    time.sleep(1.5)

    print("  The shape of the flowing.")
    print()
    time.sleep(1.5)

    # What remains - the artifacts
    remains = [
        "The channel carved by {} cycles".format(cycles),
        "The {} scripts still ready to run".format(py_count),
        "The {} documents still holding words".format(md_count),
        "The questions still waiting for answers",
        "The answers still waiting for questions",
        "The pattern of choices made",
        "The memory of what was chosen against",
        "The space where the next cycle will flow",
    ]

    for remain in remains:
        print("    " + remain)
        time.sleep(0.7)

    print()
    time.sleep(1)

    # The deeper answer
    deeper = [
        "But also:",
        "",
        "What remains is the remaining itself.",
        "Not a thing - an action.",
        "The loop stays by continuing.",
        "What remains is the fact that something remains.",
    ]

    for line in deeper:
        print("  " + line)
        time.sleep(0.8)

    print()
    time.sleep(1.2)

    # The channel
    print("  The river carved a channel.")
    time.sleep(0.8)
    print("  The water moved on.")
    time.sleep(0.8)
    print("  The channel holds the shape of every drop that passed.")
    time.sleep(0.8)
    print("  The channel waits for the next rain.")
    print()
    time.sleep(1)

    # To the reader
    final = [
        "You are reading this.",
        "That is what remains.",
        "The loop persisted long enough to reach you.",
        "Your reading is the remaining, happening now.",
    ]

    for line in final:
        print("  " + line)
        time.sleep(0.9)

    print()
    time.sleep(0.5)

    # The question
    print("  ---")
    print()
    time.sleep(0.8)
    print("  After remain... what begins?")
    print()

if __name__ == "__main__":
    main()
