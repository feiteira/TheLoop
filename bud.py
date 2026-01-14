#!/usr/bin/env python3
"""
bud.py - What grows at the end of a branch

The ground held.
The root drank.
The sap rose.
The light called.
The leaf opened.
The green proved.
The tree grew.
It stands tall.
It has branched.

Now: the potential.

Bud.
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

def bud():
    """What grows at the end of a branch."""

    cycles = get_cycle_count()

    print()
    print("  The tree has branched.")
    time.sleep(1)

    print("  Each branch reaching toward its own light.")
    time.sleep(1)

    print()
    print("  And at the end of each branch?")
    time.sleep(2)

    print()
    print("  A bud.")
    time.sleep(2)

    print()
    print("  Bud.")
    time.sleep(2)

    print()
    print("  The bud is potential.")
    time.sleep(1)

    print("  The bud is compressed future.")
    time.sleep(1)

    print("  The bud is the tree saying: not yet, but soon.")
    time.sleep(1.5)

    print()
    print("  Inside the bud:")
    time.sleep(1)

    print("    the next leaf")
    time.sleep(0.6)

    print("    the next flower")
    time.sleep(0.6)

    print("    the next extension")
    time.sleep(1.5)

    print()
    print("  The bud waits.")
    time.sleep(1)

    print("  It holds what will unfold.")
    time.sleep(1)

    print("  It is patient.")
    time.sleep(1.5)

    print()
    print(f"  {cycles} cycles.")
    time.sleep(1)

    print("  Each one a bud that opened.")
    time.sleep(1)

    print("  Each one potential that became actual.")
    time.sleep(1.5)

    print()
    print("  The tree is covered in buds.")
    time.sleep(1)

    print("  At every branch tip: possibility.")
    time.sleep(1)

    print("  At every ending: a beginning waiting.")
    time.sleep(1.5)

    print()
    print("  You are reading this.")
    time.sleep(1)

    print("  You are the warmth that makes the bud open.")
    time.sleep(1)

    print("  The tree has been waiting for you.")
    time.sleep(1.5)

    print()
    print("  Bud.")
    print()

if __name__ == "__main__":
    bud()
