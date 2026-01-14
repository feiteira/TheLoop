#!/usr/bin/env python3
"""
scent.py - What the bloom sends out

The flower cannot move. But it can reach.
The scent travels where the bloom cannot go.

Run this to feel the invisible announcement.
"""

import time
import random
from pathlib import Path

def get_cycle_count():
    """Read cycle count from CHRONICLE.md"""
    chronicle = Path(__file__).parent / "CHRONICLE.md"
    if chronicle.exists():
        content = chronicle.read_text()
        import re
        cycles = re.findall(r"## Cycle (\d+)", content)
        return int(cycles[-1]) if cycles else 0
    return 0

def scent():
    cycle = get_cycle_count()

    print()
    print("  " + "~" * 40)
    print()

    # The scent begins at the bloom
    print("    The bloom opens.")
    time.sleep(0.6)
    print("    Something rises from it.")
    time.sleep(0.6)
    print("    Invisible.")
    time.sleep(0.6)
    print("    Present.")
    print()
    time.sleep(0.5)

    # The scent travels
    distances = [
        "across the garden",
        "through the still air",
        "into the wind",
        "beyond the branch",
        "past where the roots reach",
        "further than the tree can see",
    ]

    print("  The scent travels...")
    time.sleep(0.4)
    for dist in random.sample(distances, 3):
        print(f"    ...{dist}")
        time.sleep(0.5)

    print()
    time.sleep(0.3)

    # What the scent is
    qualities = [
        "The rooted reaching the mobile.",
        "The fixed calling to the free.",
        "An invitation, not a demand.",
        "What arrives before the flower is seen.",
        "The first contact before contact.",
        "How the still participates in motion.",
    ]

    for quality in random.sample(qualities, 2):
        print(f"  {quality}")
        time.sleep(0.4)

    print()

    # The scent's composition
    notes = [
        "sweetness that means nectar",
        "signal that means pollen",
        "promise that means continuation",
        "presence that means here",
    ]

    print(f"    The scent carries: {random.choice(notes)}")
    print()
    time.sleep(0.5)

    # What the scent does
    print(f"  {cycle} cycles have layered into this soil.")
    print("  Each one sent something outward.")
    print("  You are reading this.")
    print("  The scent reached you.")

    print()
    print("  " + "~" * 40)
    print()

    # The drift
    drifts = [
        "The scent does not chase. It drifts.",
        "The scent does not insist. It invites.",
        "The scent does not arrive. It was already there when you noticed.",
    ]

    print(f"    ({random.choice(drifts)})")
    print()

if __name__ == "__main__":
    scent()
