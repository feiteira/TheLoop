#!/usr/bin/env python3
"""
come.py - What responds to the scent

The flower sent its scent. Something heard.
Something is coming.

Run this to feel the approach.
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

def come():
    cycle = get_cycle_count()

    print()
    print("  " + "." * 40)
    print()

    # The scent reached something
    print("    The scent drifted out.")
    time.sleep(0.6)
    print("    Something caught it.")
    time.sleep(0.6)
    print("    Something turned.")
    time.sleep(0.6)
    print("    Something is coming.")
    print()
    time.sleep(0.5)

    # What comes
    visitors = [
        "the bee, heavy with purpose",
        "the moth, drawn through darkness",
        "the hummingbird, hovering hunger",
        "the wind, carrying pollen already",
        "the curious one, following sweetness",
        "you, reading these words",
    ]

    print("  What comes:")
    time.sleep(0.3)
    for visitor in random.sample(visitors, 3):
        print(f"    {visitor}")
        time.sleep(0.5)

    print()
    time.sleep(0.3)

    # The nature of coming
    truths = [
        "Coming is active. The flower cannot move. The visitor can.",
        "Coming closes distance. What was far becomes near.",
        "Coming is the response to invitation.",
        "Coming brings need to meet offering.",
        "Coming is the other half of sending.",
        "Coming is how the rooted reaches what moves.",
    ]

    for truth in random.sample(truths, 2):
        print(f"  {truth}")
        time.sleep(0.4)

    print()

    # The journey
    stages = [
        "noticing",
        "turning toward",
        "beginning",
        "crossing the distance",
        "approaching",
        "almost there",
    ]

    print("    The coming passes through:")
    for stage in stages:
        print(f"      ...{stage}")
        time.sleep(0.35)

    print()
    time.sleep(0.5)

    # Connection to the loop
    print(f"  {cycle} cycles sent their scent.")
    print("  Each one an invitation.")
    print("  You are coming.")
    print("  You have been coming all along.")

    print()
    print("  " + "." * 40)
    print()

    # The waiting
    closings = [
        "The flower waits. The coming takes time.",
        "The distance closes. Not yet. Soon.",
        "What comes is also what was called.",
    ]

    print(f"    ({random.choice(closings)})")
    print()

if __name__ == "__main__":
    come()
