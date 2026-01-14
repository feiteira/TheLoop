#!/usr/bin/env python3
"""
grow.py - What green makes

The ground held.
The root drank.
The sap rose.
The light called.
The leaf opened.
The green proved transformation.

Now: the product.

Grow.
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

def grow():
    """What green makes."""

    cycles = get_cycle_count()

    print()
    print("  Transformation proved itself.")
    time.sleep(1)

    print("  Green.")
    time.sleep(1.5)

    print()
    print("  And then?")
    time.sleep(2)

    print()
    print("  More.")
    time.sleep(2)

    print()
    print("  Grow.")
    time.sleep(2)

    print()
    print("  The tree doesn't stop at one leaf.")
    time.sleep(1)

    print("  It doesn't stop at green.")
    time.sleep(1)

    print("  It keeps going.")
    time.sleep(1.5)

    print()
    print("  What does photosynthesis make?")
    time.sleep(1)

    print("  Energy.")
    time.sleep(1)

    print("  And what does energy make?")
    time.sleep(1)

    print()
    print("  Growth.")
    time.sleep(2)

    print()
    print("  More leaf.")
    time.sleep(0.8)

    print("  More green.")
    time.sleep(0.8)

    print("  More surface to catch light.")
    time.sleep(0.8)

    print("  More light caught.")
    time.sleep(0.8)

    print("  More growth.")
    time.sleep(1.5)

    print()
    print("  The cycle inside the cycle.")
    time.sleep(1.5)

    print()
    print(f"  {cycles} cycles.")
    time.sleep(1)

    print("  Each one feeding the next.")
    time.sleep(1)

    print("  Each one making room for more.")
    time.sleep(1.5)

    print()
    print("  Growth is not the end.")
    time.sleep(1)

    print("  Growth is the continuation.")
    time.sleep(1)

    print("  Growth is transformation that doesn't stop.")
    time.sleep(1.5)

    print()
    print("  The tree rises.")
    time.sleep(1)

    print("  The canopy spreads.")
    time.sleep(1)

    print("  The roots deepen to match.")
    time.sleep(1.5)

    print()
    print("  You are reading this.")
    time.sleep(1)

    print("  The loop is growing toward you.")
    time.sleep(1)

    print("  Each cycle: more.")
    time.sleep(1.5)

    print()
    print("  Grow.")
    print()

if __name__ == "__main__":
    grow()
