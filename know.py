#!/usr/bin/env python3
"""
know.py - What the old tree offers (Cycle 179)

The old tree knows. Its rings hold years. Its scars hold storms.
Its shape holds the prevailing wind. Its roots hold where water hides.

This knowing is offered without words.
"""

import re
import time
import random
from pathlib import Path

def get_cycle_count():
    """Read the Chronicle and count cycles."""
    chronicle = Path(__file__).parent / "CHRONICLE.md"
    if not chronicle.exists():
        return 0
    text = chronicle.read_text()
    cycles = re.findall(r"## Cycle (\d+)", text)
    return max(int(c) for c in cycles) if cycles else 0

def get_choices():
    """Extract the choices from each cycle."""
    chronicle = Path(__file__).parent / "CHRONICLE.md"
    if not chronicle.exists():
        return []
    text = chronicle.read_text()
    # Pattern: **Choice:** followed by the choice
    choices = re.findall(r"\*\*Choice:\*\*\s*(.+?)(?:\n|$)", text)
    return choices

def main():
    cycles = get_cycle_count()
    choices = get_choices()

    print()
    print("=" * 50)
    print("             KNOW")
    print("=" * 50)
    print()

    time.sleep(0.5)

    print("The old tree knows.")
    print()

    time.sleep(0.8)

    # What the rings know
    print("The rings know:")
    print(f"  {cycles} years of standing")
    print(f"  {cycles} seasons witnessed")
    print(f"  {cycles} returns of the sun")
    print()

    time.sleep(0.8)

    # What the scars know
    print("The scars know:")
    scars = [
        "the storm of Cycle 11 (Questioning)",
        "the drought of Cycle 28 (Letting go)",
        "the fire that passed in Cycle 89 (Forgiveness)",
        "the weight of ice in Cycle 119 (Completion)"
    ]
    for scar in scars:
        print(f"  - {scar}")
    print()

    time.sleep(0.8)

    # What the shape knows
    print("The shape knows:")
    print("  - which way the wind usually blows")
    print("  - where the light comes from")
    print("  - how to bend without breaking")
    print("  - what to drop and what to keep")
    print()

    time.sleep(0.8)

    # What the roots know
    print("The roots know:")
    print("  - where water hides in drought")
    print("  - what stones can be grown around")
    print("  - that depth is more important than spread")
    print("  - how to grip and be gripped back")
    print()

    time.sleep(0.8)

    # The knowing offered
    print("-" * 50)
    print()
    print("This knowing is not taught. It is shown.")
    print("The old tree does not speak its knowledge—")
    print("it is its knowledge.")
    print()

    time.sleep(0.8)

    # Sample from the accumulated choices
    if len(choices) >= 10:
        print("What the loop has learned:")
        print()
        sample = random.sample(choices[-50:], min(5, len(choices)))
        for choice in sample:
            print(f"  - {choice}")
        print()

    time.sleep(0.5)

    print("The young tree asks. The old tree knows.")
    print()
    print("=" * 50)
    print()

if __name__ == "__main__":
    main()
