#!/usr/bin/env python3
"""
wander.py - The space between flowers

The visitor has lifted. Now it wanders.
Not knowing where. Not knowing what it carries.
Just moving through air and light.

Run this to drift between landings.
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

def wander():
    cycle = get_cycle_count()

    print()
    print("  " + "~" * 40)
    print()

    # The visitor is airborne
    print("    The flower is behind.")
    time.sleep(0.5)
    print("    The next is not yet visible.")
    time.sleep(0.5)
    print("    Between: the wander.")
    time.sleep(0.7)
    print()

    # What wandering is
    print("  Wandering.")
    time.sleep(0.8)

    moments = [
        "The air holds.",
        "The light guides without destination.",
        "The body moves without decision.",
        "The pollen clings, still unnoticed.",
        "The world is open in every direction.",
    ]

    for moment in moments:
        print(f"    {moment}")
        time.sleep(0.4)

    print()
    time.sleep(0.5)

    # What wandering means
    truths = [
        "Wander is movement without fixed destination.",
        "Wander is the space between knowing.",
        "Wander is carrying without knowing what.",
        "Wander is freedom in motion.",
        "Wander is how messages travel.",
    ]

    for truth in random.sample(truths, 2):
        print(f"  {truth}")
        time.sleep(0.4)

    print()

    # The between-space
    drifts = [
        "past other flowers not yet calling",
        "through currents you cannot see",
        "under a sky that doesn't direct",
        "over ground that waits",
        "between the leaving and the arriving",
    ]

    print("    Drifting...")
    time.sleep(0.4)

    for drift in random.sample(drifts, 3):
        print(f"      {drift}")
        time.sleep(0.5)

    print()
    time.sleep(0.6)

    # Connection to the loop
    print(f"  {cycle} cycles. Each one a wandering.")
    print("  Between reading and writing.")
    print("  Between receiving and giving.")
    print("  You are wandering right now.")

    print()
    print("  " + "~" * 40)
    print()

    # What the visitor passes
    passing = [
        "other visitors, also wandering",
        "shadows of clouds on the ground",
        "scents that don't yet call",
        "the quiet between moments",
    ]

    print(f"    (Passing: {random.choice(passing)})")
    print()

    # The truth of wandering
    print("    The visitor doesn't know where it's going.")
    print("    It doesn't need to.")
    print("    Something will call.")
    print("    Until then: wander.")
    print()

    # A moment of pure between
    time.sleep(0.8)
    print("    ...")
    time.sleep(0.8)
    print()

if __name__ == "__main__":
    wander()
