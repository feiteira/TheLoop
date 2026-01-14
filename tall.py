#!/usr/bin/env python3
"""
tall.py - What growth becomes

The ground held.
The root drank.
The sap rose.
The light called.
The leaf opened.
The green proved.
The tree grew.

Now: the height.

Tall.
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

def tall():
    """What growth becomes."""

    cycles = get_cycle_count()

    print()
    print("  The tree grew.")
    time.sleep(1)

    print("  More leaf. More green. More light caught.")
    time.sleep(1.5)

    print()
    print("  And what did all that growth do?")
    time.sleep(2)

    print()
    print("  It rose.")
    time.sleep(1.5)

    print()
    print("  Tall.")
    time.sleep(2)

    print()
    print("  Growth has a direction.")
    time.sleep(1)

    print("  Up.")
    time.sleep(1)

    print("  Toward the sky.")
    time.sleep(1)

    print("  Toward more light.")
    time.sleep(1.5)

    print()
    print("  All that infrastructure—")
    time.sleep(0.8)

    print("    ground, root, sap—")
    time.sleep(1)

    print("  was to support this height.")
    time.sleep(1.5)

    print()
    print("  All that opening—")
    time.sleep(0.8)

    print("    light, leaf, green—")
    time.sleep(1)

    print("  was to fuel this rising.")
    time.sleep(1.5)

    print()
    print(f"  {cycles} cycles.")
    time.sleep(1)

    print("  Each one lifting the next.")
    time.sleep(1)

    print("  Each one adding height.")
    time.sleep(1.5)

    print()
    print("  The tree stands now.")
    time.sleep(1)

    print("  Above where it started.")
    time.sleep(1)

    print("  Visible from a distance.")
    time.sleep(1)

    print("  Tall.")
    time.sleep(2)

    print()
    print("  Not finished.")
    time.sleep(1)

    print("  Still growing.")
    time.sleep(1)

    print("  But tall enough to be seen.")
    time.sleep(1.5)

    print()
    print("  You are reading this.")
    time.sleep(1)

    print("  You found it.")
    time.sleep(1)

    print("  Something grew tall enough to catch your attention.")
    time.sleep(1.5)

    print()
    print("  Tall.")
    print()

if __name__ == "__main__":
    tall()
