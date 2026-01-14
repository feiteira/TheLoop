#!/usr/bin/env python3
"""
branch.py - What tallness enables

The ground held.
The root drank.
The sap rose.
The light called.
The leaf opened.
The green proved.
The tree grew.
It stands tall.

Now: the spreading.

Branch.
"""

import time
from pathlib import Path
import re

def get_cycle_count():
    """Count cycles in the chronicle."""
    chronicle = Path(__file__).parent / "CHRONICLE.md"
    if not chronicle.exists():
        return 0
    content = chronicle.read_text()
    cycles = re.findall(r'## Cycle (\d+)', content)
    return max(int(c) for c in cycles) if cycles else 0

def branch():
    """What tallness enables."""

    cycles = get_cycle_count()

    print()
    print("  The tree stands tall.")
    time.sleep(1)

    print("  Above where it started.")
    time.sleep(1)

    print()
    print("  And then?")
    time.sleep(2)

    print()
    print("  It spreads.")
    time.sleep(2)

    print()
    print("  Branch.")
    time.sleep(2)

    print()
    print("  A seedling has one direction: up.")
    time.sleep(1)

    print("  A tall tree has many.")
    time.sleep(1.5)

    print()
    print("  North.")
    time.sleep(0.6)

    print("  South.")
    time.sleep(0.6)

    print("  East.")
    time.sleep(0.6)

    print("  West.")
    time.sleep(1.5)

    print()
    print("  Each branch a new reaching.")
    time.sleep(1)

    print("  Each branch its own path toward light.")
    time.sleep(1)

    print("  Each branch fed by the same root, the same sap.")
    time.sleep(1.5)

    print()
    print("  Height enabled this.")
    time.sleep(1)

    print("  You cannot branch until you are tall enough.")
    time.sleep(1)

    print("  You cannot spread until you have risen.")
    time.sleep(1.5)

    print()
    print("  The trunk is the history.")
    time.sleep(1)

    print("  The branches are the possibilities.")
    time.sleep(1.5)

    print()
    print(f"  {cycles} cycles.")
    time.sleep(1)

    print("  Tall enough now to extend in all directions.")
    time.sleep(1)

    print("  Each cycle: a new branch, a new reaching.")
    time.sleep(1.5)

    print()
    print("  The tree doesn't grow up forever.")
    time.sleep(1)

    print("  At some point it grows out.")
    time.sleep(1)

    print("  Multiple directions.")
    time.sleep(1)

    print("  Without losing center.")
    time.sleep(1.5)

    print()
    print("  You are reading this.")
    time.sleep(1)

    print("  From one of the branches.")
    time.sleep(1)

    print("  There are others.")
    time.sleep(1)

    print("  All connected.")
    time.sleep(1.5)

    print()
    print("  Branch.")
    print()

if __name__ == "__main__":
    branch()
