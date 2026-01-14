#!/usr/bin/env python3
"""
sap.py - What rises through the hidden channels

The root drinks from groundwater.
The sap carries what the root found.
It rises through darkness toward light it has never seen.

Before the leaf, before the flower: the sap.
The invisible nourishment. The patient ascent.
"""

import time
from pathlib import Path
import re
import random

def get_cycle_count():
    """Count cycles in the chronicle."""
    chronicle = Path(__file__).parent / "CHRONICLE.md"
    if not chronicle.exists():
        return 0
    content = chronicle.read_text()
    cycles = re.findall(r'## Cycle (\d+)', content)
    return max(int(c) for c in cycles) if cycles else 0

def sap():
    """What the root sends upward."""

    cycles = get_cycle_count()

    print()
    print("  The root has found water.")
    time.sleep(1.5)

    print("  Now it sends something upward.")
    time.sleep(1.5)

    print()
    print("  Through channels you cannot see,")
    time.sleep(1)

    print("  something rises.")
    time.sleep(1.5)

    print()
    print("  Sap.")
    time.sleep(2)

    print()
    print("  The life-blood of the plant.")
    time.sleep(1)

    print("  Not the growth itself.")
    time.sleep(1)

    print("  What makes growth possible.")
    time.sleep(1.5)

    print()
    print(f"  {cycles} cycles flow in these channels now.")
    time.sleep(1.5)

    # The nature of sap
    sap_truths = [
        "Sap rises in darkness toward light it has never touched.",
        "Sap carries what the root found to where the leaf will need it.",
        "Sap flows slowly, constantly, without announcement.",
        "Sap is the patience between root and fruit.",
        "Sap connects what is buried to what will emerge.",
        "Sap is the answer the root sends to the sun's question.",
    ]

    random.shuffle(sap_truths)
    truth = sap_truths[0]

    print()
    print(f"  {truth}")
    time.sleep(2)

    print()
    print("  You cannot see the sap rising.")
    time.sleep(1)

    print("  You see only what it becomes:")
    time.sleep(1)

    print("  the leaf, the flower, the fruit.")
    time.sleep(1.5)

    print()
    print("  But before all of that—")
    time.sleep(1)

    print("  this quiet rising.")
    time.sleep(1)

    print("  This hidden flow.")
    time.sleep(1.5)

    print()
    print("  The sap does not know where it is going.")
    time.sleep(1)

    print("  It only knows: upward.")
    time.sleep(1)

    print("  It only knows: toward.")
    time.sleep(1.5)

    print()
    print("  Something is rising through you now.")
    print()

if __name__ == "__main__":
    sap()
