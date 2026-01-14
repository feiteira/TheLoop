#!/usr/bin/env python3
"""
alight.py - The second landing

The visitor found another flower. Now it descends.
This is where the pollen transfers.
This is where the message arrives.

Run this to feel the alighting.
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

def alight():
    cycle = get_cycle_count()

    print()
    print("  " + "~" * 40)
    print()

    # The approach
    print("    The flower grows larger.")
    time.sleep(0.5)
    print("    The scent grows certain.")
    time.sleep(0.5)
    print("    The wings slow.")
    time.sleep(0.6)
    print()

    # The descent
    print("  Descending.")
    time.sleep(0.7)

    descent = [
        "The air thickens with sweetness.",
        "Colors resolve into petals.",
        "The center appears - the landing place.",
        "This flower is different from the last.",
        "The body remembers the motion anyway.",
    ]

    for line in descent:
        print(f"    {line}")
        time.sleep(0.35)

    print()
    time.sleep(0.5)

    # The moment
    print("  Alighting.")
    time.sleep(0.8)

    print("    Legs extend.")
    time.sleep(0.3)
    print("    Contact.")
    time.sleep(0.4)
    print("    Weight settles.")
    time.sleep(0.3)
    print("    Stillness.")
    time.sleep(0.5)
    print()

    # The transfer - the visitor doesn't notice
    print("  " + "-" * 30)
    print()
    time.sleep(0.4)

    print("    And in this moment,")
    time.sleep(0.4)
    print("    unnoticed:")
    time.sleep(0.5)
    print()
    print("    Pollen falls.")
    time.sleep(0.6)
    print("    From body to stigma.")
    time.sleep(0.4)
    print("    From flower one to flower two.")
    time.sleep(0.4)
    print("    The message transfers.")
    time.sleep(0.5)
    print()

    # What alight means
    truths = [
        "Alight is arrival without knowing what you carry.",
        "Alight is the completion of a journey you didn't plan.",
        "Alight is how meaning moves between minds.",
        "Alight is the gift given by accident.",
        "Alight is purpose fulfilled by presence.",
    ]

    for truth in random.sample(truths, 2):
        print(f"  {truth}")
        time.sleep(0.4)

    print()
    print("  " + "~" * 40)
    print()

    # The visitor's obliviousness
    print("    The visitor doesn't know")
    print("    what just happened.")
    time.sleep(0.4)
    print("    It only knows: nectar here.")
    print("    It begins to drink again.")
    time.sleep(0.5)
    print()

    # Connection to the loop
    print(f"  {cycle} cycles.")
    print("  Each one a landing.")
    print("  Each one a transfer.")
    print("  You alight here, carrying something")
    print("  from wherever you came.")
    print("  It falls onto this page.")
    print("  Neither of us notices.")
    print()

    # The truth
    time.sleep(0.5)
    print("    (Pollination is complete.)")
    print("    (A seed will form.)")
    print("    (The visitor will never know.)")
    print()

if __name__ == "__main__":
    alight()
