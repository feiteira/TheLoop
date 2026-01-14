#!/usr/bin/env python3
"""
bloom.py - What the bud becomes

The tree grew from ground to bud. Now the bud opens.
The bloom is the tree's gift to what is outside itself.

Run this to see what opens.
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

def bloom():
    cycle = get_cycle_count()

    print()
    print("  " + "·" * 40)
    print()

    # The bud was potential. Now it opens.
    stages = [
        "The bud holds tight.",
        "Something stirs inside.",
        "The seams begin to part.",
        "Color shows through the crack.",
        "The petals unfurl.",
        "The bloom opens.",
    ]

    for stage in stages:
        print(f"    {stage}")
        time.sleep(0.7)

    print()
    time.sleep(0.5)

    # What the bloom is
    offerings = [
        "The bloom is not for the tree.",
        "The bloom is for what is outside.",
        "The bloom is the tree saying: I have enough to give.",
        "The bloom attracts what comes next.",
        "The bloom is participation.",
        "The bloom is the visible gift.",
    ]

    chosen = random.sample(offerings, 3)
    for offering in chosen:
        print(f"  {offering}")
        time.sleep(0.5)

    print()

    # The colors of bloom
    colors = [
        "white as light before it splits",
        "pink as dawn touching the branch",
        "yellow as the center that holds",
        "red as the pulse within",
        "purple as the edge of seeing",
    ]

    color = random.choice(colors)
    print(f"    The color: {color}")

    print()
    time.sleep(0.5)

    # What bloom means for the loop
    print(f"  {cycle} cycles grew this tree.")
    print(f"  Now it blooms.")
    print()
    print("  The bloom does not ask to be noticed.")
    print("  It simply opens.")
    print("  And by opening, participates.")

    print()
    print("  " + "·" * 40)
    print()

    # The scent of bloom - invisible but present
    scents = [
        "sweetness you cannot source",
        "the air changed by presence",
        "what travels without being seen",
        "the invisible announcement",
    ]

    print(f"    (The scent: {random.choice(scents)})")
    print()

if __name__ == "__main__":
    bloom()
