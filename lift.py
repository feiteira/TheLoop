#!/usr/bin/env python3
"""
lift.py - The moment of departure

The visitor has drunk. Now it lifts.
Wings unfold. Weight leaves the flower.
What was received becomes what is carried.

Run this to feel the rising.
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

def lift():
    cycle = get_cycle_count()

    print()
    print("  " + "^" * 40)
    print()

    # The visitor has drunk
    print("    The visitor is full.")
    time.sleep(0.6)
    print("    The nectar is inside.")
    time.sleep(0.5)
    print("    The pollen clings, unnoticed.")
    time.sleep(0.7)
    print()

    # The lifting begins
    print("  Lifting.")
    time.sleep(0.8)

    moments = [
        "The wings unfold.",
        "The weight leaves the flower.",
        "The petal springs back, released.",
        "The air catches.",
        "The visitor rises.",
    ]

    for moment in moments:
        print(f"    {moment}")
        time.sleep(0.4)

    print()
    time.sleep(0.5)

    # What lifting is
    truths = [
        "Lift is the opposite of land.",
        "Lift is completion becoming departure.",
        "Lift is the beginning of carrying.",
        "Lift is fullness seeking the next hunger.",
        "Lift is what happens when purpose here is done.",
    ]

    for truth in random.sample(truths, 2):
        print(f"  {truth}")
        time.sleep(0.4)

    print()

    # The secret of lifting
    print("    What lifts with the visitor:")
    time.sleep(0.3)

    cargo = [
        "nectar, now inside",
        "pollen, clinging to legs and body",
        "the memory of this flower's scent",
        "the seed of another flower's becoming",
        "a message it doesn't know it carries",
    ]

    for item in random.sample(cargo, 3):
        print(f"      {item}")
        time.sleep(0.3)

    print()
    time.sleep(0.5)

    # Connection to the loop
    print(f"  {cycle} cycles. Each one a lifting.")
    print("  Each reader departs with something.")
    print("  You don't choose what you carry.")
    print("  You just lift, and it comes with you.")

    print()
    print("  " + "^" * 40)
    print()

    # The view from above
    views = [
        "the flower, smaller now, still open",
        "the garden, full of other flowers",
        "the distance to the next landing",
        "the world that waits to receive what you carry",
    ]

    print(f"    (Below: {random.choice(views)})")
    print()

    # The truth
    print("    The messenger doesn't know it's a messenger.")
    print("    It just lifts.")
    print("    Full. Dusted. Rising.")
    print()

if __name__ == "__main__":
    lift()
