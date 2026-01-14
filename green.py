#!/usr/bin/env python3
"""
green.py - The color of transformation

The leaf opened.
The light arrived.
And something changed.

Green.

The visible sign that life is being made.
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

def green():
    """The color of transformation."""

    cycles = get_cycle_count()

    print()
    print("  The leaf opened.")
    time.sleep(1)

    print("  The light arrived.")
    time.sleep(1)

    print("  And something changed.")
    time.sleep(1.5)

    print()
    print("  Green.")
    time.sleep(2)

    print()
    print("  The color of what happens")
    time.sleep(0.8)

    print("  when light meets leaf.")
    time.sleep(1.5)

    print()
    print("  Chlorophyll waking.")
    time.sleep(1)

    print("  Photosynthesis beginning.")
    time.sleep(1)

    print("  Light becoming life.")
    time.sleep(1.5)

    print()
    print("  Green is not the light.")
    time.sleep(1)

    print("  Green is not the leaf.")
    time.sleep(1)

    print("  Green is what happens between them.")
    time.sleep(1.5)

    print()
    print(f"  {cycles} cycles.")
    time.sleep(0.8)

    print("  Each one a meeting.")
    time.sleep(0.8)

    print("  Each one a transformation.")
    time.sleep(1.5)

    print()
    print("  The ground is dark.")
    time.sleep(0.8)

    print("  The root is dark.")
    time.sleep(0.8)

    print("  The sap is dark.")
    time.sleep(0.8)

    print("  The light is white.")
    time.sleep(1)

    print()
    print("  But where they meet:")
    time.sleep(1)

    print("  green.")
    time.sleep(2)

    print()
    print("  The color of transformation.")
    time.sleep(1)

    print("  The visible proof.")
    time.sleep(1)

    print("  The sign that something is happening.")
    time.sleep(1.5)

    print()
    print("  You are reading this.")
    time.sleep(1)

    print("  Light is meeting your attention.")
    time.sleep(1)

    print("  Something is turning green.")
    print()

if __name__ == "__main__":
    green()
