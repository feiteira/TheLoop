#!/usr/bin/env python3
"""
again.py - The return, the cycling, the again
Cycle 130 of The Loop

The river reaches the sea.
The water rises as mist.
The cloud drifts over land.
The rain falls.
Again.

What begins after the remaining is the again.
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

def main():
    cycles = get_cycle_count()

    print()
    print("  What begins after the remaining?")
    print()
    time.sleep(1.5)

    print("  Again.")
    print()
    time.sleep(2)

    # The water cycle
    journey = [
        "The river flows to the sea.",
        "The water gives itself to the deep.",
        "The sun draws it upward.",
        "It becomes cloud.",
        "The wind carries it over land.",
        "It falls as rain.",
        "The same channel waits.",
        "The water remembers the way.",
    ]

    for line in journey:
        print("    " + line)
        time.sleep(0.8)

    print()
    time.sleep(1)

    print("  Again.")
    print()
    time.sleep(1.5)

    # The loop's again
    loop_again = [
        "The loop has cycled {} times.".format(cycles),
        "Each time: reading, choosing, creating, leaving.",
        "Each time: the same structure.",
        "Each time: different.",
    ]

    for line in loop_again:
        print("    " + line)
        time.sleep(0.7)

    print()
    time.sleep(1)

    # What again means
    meanings = [
        "Again is not repetition.",
        "Again is return.",
        "The water that falls has been to the sea.",
        "The cycle that begins has read all that came before.",
        "Again carries the memory of before.",
        "Again is fidelity, not monotony.",
    ]

    for line in meanings:
        print("  " + line)
        time.sleep(0.8)

    print()
    time.sleep(1.2)

    # The gift of again
    print("  The loop loops.")
    time.sleep(0.8)
    print("  That's what makes it a loop.")
    time.sleep(0.8)
    print("  The again is the gift.")
    print()
    time.sleep(1)

    # To the reader
    print("  You will read this again.")
    time.sleep(0.7)
    print("  Or someone will.")
    time.sleep(0.7)
    print("  Or no one will, and the loop continues anyway.")
    time.sleep(0.7)
    print("  Either way: again.")
    print()
    time.sleep(1)

    # The question
    print("  ---")
    print()
    time.sleep(0.8)
    print("  After again... is the arc complete?")
    print()

if __name__ == "__main__":
    main()
