#!/usr/bin/env python3
"""
last.py - The final act of standing (Cycle 180)

The old tree lasts. Not dramatically. Not heroically.
It simply continues to be what it has become.

This completes the STAND phase.
"""

import re
import time
from pathlib import Path

def get_cycle_count():
    """Read the Chronicle and count cycles."""
    chronicle = Path(__file__).parent / "CHRONICLE.md"
    if not chronicle.exists():
        return 0
    text = chronicle.read_text()
    cycles = re.findall(r"## Cycle (\d+)", text)
    return max(int(c) for c in cycles) if cycles else 0

def main():
    cycles = get_cycle_count()

    print()
    print("=" * 50)
    print("              LAST")
    print("=" * 50)
    print()

    time.sleep(0.5)

    print("The old tree lasts.")
    print()

    time.sleep(0.8)

    # The phases of standing
    phases = [
        ("Stand", "It took its place."),
        ("Weather", "It received the world."),
        ("Shelter", "It created protection."),
        ("Inhabit", "Life gathered in its niche."),
        ("Sustain", "The ecology returned what was given."),
        ("Thrive", "It flourished."),
        ("Season", "It witnessed time's cycles."),
        ("Old", "It aged, accumulated."),
        ("Know", "It embodied what it learned."),
        ("Last", "It persists."),
    ]

    print("The STAND phase:")
    print()
    for phase, description in phases:
        print(f"  {phase}: {description}")
        time.sleep(0.3)
    print()

    time.sleep(0.5)

    # What lasting means
    print("-" * 50)
    print()
    print("To last is not an action.")
    print("It is the outcome of all actions.")
    print()

    time.sleep(0.5)

    print("The tree does not try to last.")
    print("Lasting is what happens when you do not stop.")
    print()

    time.sleep(0.5)

    # The loop's lasting
    print(f"The loop has {cycles} cycles.")
    print(f"Each cycle is proof of lasting.")
    print(f"This moment is lasting happening.")
    print()

    time.sleep(0.5)

    print("-" * 50)
    print()
    print("What comes after lasting?")
    print()
    print("The tree falls. Or returns. Or rests.")
    print("But that is for the next phase.")
    print()
    print("For now: the tree lasts.")
    print()
    print("=" * 50)
    print("         STAND complete.")
    print("=" * 50)
    print()

if __name__ == "__main__":
    main()
