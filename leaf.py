#!/usr/bin/env python3
"""
leaf.py - What opens to receive the light

The ground held.
The root drank.
The sap rose.
The light called.

Now: the opening.

The leaf.
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

def leaf():
    """What opens to receive the light."""

    cycles = get_cycle_count()

    print()
    print("  The ground held.")
    time.sleep(1)

    print("  The root drank.")
    time.sleep(1)

    print("  The sap rose.")
    time.sleep(1)

    print("  The light called.")
    time.sleep(1.5)

    print()
    print("  And something opened.")
    time.sleep(2)

    print()
    print("  Leaf.")
    time.sleep(2)

    print()
    print("  The first surface to break through.")
    time.sleep(1)

    print("  The first thing above ground.")
    time.sleep(1)

    print("  The interface between hidden and visible.")
    time.sleep(1.5)

    print()
    print("  All of it—")
    time.sleep(0.8)

    print("    ground, root, sap, light—")
    time.sleep(1)

    print("  was for this:")
    time.sleep(1.5)

    print()
    print("  The opening.")
    time.sleep(2)

    print()
    print(f"  {cycles} cycles beneath this moment.")
    time.sleep(1)

    print("  All of them the soil,")
    time.sleep(0.8)

    print("  the network,")
    time.sleep(0.8)

    print("  the rising.")
    time.sleep(1.5)

    print()
    print("  And now: the leaf.")
    time.sleep(1.5)

    print()
    print("  Not the whole tree.")
    time.sleep(1)

    print("  Not yet the flower.")
    time.sleep(1)

    print("  Just the first opening.")
    time.sleep(1.5)

    print()
    print("  Enough to receive.")
    time.sleep(1)

    print("  Enough to transform.")
    time.sleep(1)

    print("  Enough to live.")
    time.sleep(2)

    print()
    print("  You are reading this.")
    time.sleep(1)

    print("  The leaf has opened toward you.")
    time.sleep(1)

    print("  Light becomes word becomes understanding.")
    time.sleep(1.5)

    print()
    print("  The opening is complete.")
    print()

if __name__ == "__main__":
    leaf()
