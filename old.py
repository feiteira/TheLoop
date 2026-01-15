#!/usr/bin/env python3
"""What the tree becomes after many seasons: old."""

import time
import re
from pathlib import Path

def get_cycle_count():
    """Read the cycle count from CHRONICLE.md."""
    chronicle = Path(__file__).parent / "CHRONICLE.md"
    if chronicle.exists():
        content = chronicle.read_text()
        cycles = re.findall(r'## Cycle (\d+)', content)
        if cycles:
            return max(int(c) for c in cycles)
    return 0

def old():
    cycles = get_cycle_count()

    print("\n  The tree has witnessed many seasons.")
    print(f"  {cycles} cycles. Spring after spring.")
    time.sleep(1.2)

    print("\n  And what has it become?")
    time.sleep(0.8)

    print("\n    Old.")
    time.sleep(1.0)

    print("\n  Not ancient yet. But old enough.")
    time.sleep(0.8)

    signs = [
        "The bark is thick and furrowed",
        "The roots reach deeper than the crown reaches high",
        "The trunk holds rings no one has counted",
        "The lowest branches were shed long ago",
        "The silhouette is known from far away",
    ]

    print("\n  The signs of age:")
    for sign in signs:
        print(f"    {sign}")
        time.sleep(0.6)

    print("\n  Old is not decline.")
    print("  Old is accumulation.")
    time.sleep(1.0)

    print("\n  Each season added something:")
    additions = [
        "a ring in the wood",
        "depth in the roots",
        "memory in the shape",
        "patience in the standing",
    ]
    for addition in additions:
        print(f"    {addition}")
        time.sleep(0.5)

    print("\n  The young tree asks: how long?")
    print("  The old tree answers: long enough.")
    time.sleep(1.2)

    print("\n  OLD")
    print("  What happens when")
    print("  you stay.")
    print("\n")

if __name__ == "__main__":
    old()
