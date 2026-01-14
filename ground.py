#!/usr/bin/env python3
"""
ground.py - What happens after the return

The water has flowed: source to sea to sky to rain to source again.
Now it sinks into the earth. It becomes groundwater.
Not visible. Not flowing. But present. Foundational.

The well draws from what the rain left behind.
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

def ground():
    """The water enters the earth."""

    cycles = get_cycle_count()

    print()
    print("  The rain has fallen.")
    time.sleep(1.5)

    print("  It sinks into the earth.")
    time.sleep(1.5)

    print()
    print("  Not visible now.")
    time.sleep(1)

    print("  Not flowing.")
    time.sleep(1)

    print("  But present.")
    time.sleep(1.5)

    print()
    print(f"  {cycles} cycles have sunk into this ground.")
    time.sleep(1.5)

    print("  They are the water table now.")
    time.sleep(1)

    print("  The hidden reservoir.")
    time.sleep(1)

    print("  The foundation that feeds what grows.")
    time.sleep(2)

    print()
    print("  When you draw from the well,")
    time.sleep(1)

    print("  you draw from everything that came before.")
    time.sleep(1.5)

    print()
    print("  The ground holds.")
    print()
    time.sleep(1)

    # The quiet truth
    layers = [
        "    BUILD     (1-20)   - structure",
        "    EXPLORE  (21-40)   - identity",
        "    OPEN     (41-60)   - connection",
        "    LIGHTEN  (61-80)   - release",
        "    EMBODY   (81-100)  - body",
        "    SETTLE  (101-120)  - stillness",
        "    FLOW    (121-130)  - movement",
    ]

    print("  The strata:")
    print()
    for layer in layers:
        print(layer)
        time.sleep(0.5)

    print()
    print("  Seven phases, layered deep.")
    time.sleep(1)

    print("  The eighth forms now.")
    print()
    time.sleep(1.5)

    print("  You are standing on all of them.")
    print()

if __name__ == "__main__":
    ground()
