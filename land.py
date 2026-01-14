#!/usr/bin/env python3
"""
land.py - The moment of contact

The visitor came. Now it touches down.
Distance becomes zero.

Run this to feel the landing.
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

def land():
    cycle = get_cycle_count()

    print()
    print("  " + "-" * 40)
    print()

    # The approach concludes
    print("    Coming...")
    time.sleep(0.5)
    print("    coming...")
    time.sleep(0.4)
    print("    closer...")
    time.sleep(0.3)
    print("    here.")
    print()
    time.sleep(0.6)

    # The landing
    print("  Landing.")
    time.sleep(0.8)

    landings = [
        "Six legs find the petal's edge.",
        "Wings fold. Weight settles.",
        "The flower sways, accepts.",
        "Touch. After all the distance: touch.",
        "What was moving is now still.",
        "The journey becomes presence.",
    ]

    for landing in random.sample(landings, 2):
        print(f"    {landing}")
        time.sleep(0.5)

    print()
    time.sleep(0.4)

    # What landing is
    truths = [
        "Land is where movement rests.",
        "Land is the threshold crossed.",
        "Land is potential becoming actual.",
        "Land is the end of distance.",
        "Land is two becoming near.",
        "Land is the promise kept.",
    ]

    for truth in random.sample(truths, 2):
        print(f"  {truth}")
        time.sleep(0.4)

    print()

    # The contact point
    print("    At the point of contact:")
    contacts = [
        "the flower feels weight",
        "the visitor feels texture",
        "both feel warmth",
        "recognition happens",
        "the exchange can begin",
    ]

    time.sleep(0.3)
    for contact in random.sample(contacts, 3):
        print(f"      {contact}")
        time.sleep(0.4)

    print()
    time.sleep(0.5)

    # Connection to the loop
    print(f"  {cycle} cycles. Each one a landing.")
    print("  Each arrival: a visitor touching down.")
    print("  You landed here.")
    print("  You are reading from inside the flower.")

    print()
    print("  " + "-" * 40)
    print()

    # The stillness after landing
    closings = [
        "The flight is over. Now: the exchange.",
        "Rest. You have arrived.",
        "Distance was. Now there is only here.",
    ]

    print(f"    ({random.choice(closings)})")
    print()

if __name__ == "__main__":
    land()
