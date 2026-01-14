#!/usr/bin/env python3
"""
find.py - The moment another flower calls

The visitor wanders. It wasn't looking.
But something reaches it - a scent, a color, a pull.
It finds.

Run this to feel the finding.
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

def find():
    cycle = get_cycle_count()

    print()
    print("  " + "~" * 40)
    print()

    # The wandering continues
    print("    Still wandering...")
    time.sleep(0.6)
    print("    Not seeking anything.")
    time.sleep(0.4)
    print("    Open to everything.")
    time.sleep(0.6)
    print()

    # The moment of finding
    print("  And then-")
    time.sleep(0.7)

    signals = [
        "a thread of sweetness in the air",
        "a color at the edge of seeing",
        "a warmth that wasn't there before",
        "something that pulls without asking",
        "a direction that feels like yes",
    ]

    print(f"    {random.choice(signals)}")
    time.sleep(0.5)
    print()

    # What finding is
    print("  Finding.")
    time.sleep(0.6)

    truths = [
        "Find is not the same as seek.",
        "Find happens to the open.",
        "Find is the scent reaching the wanderer.",
        "Find is being called without knowing it.",
        "Find is how pollen gets where it's going.",
    ]

    for truth in random.sample(truths, 2):
        print(f"    {truth}")
        time.sleep(0.4)

    print()
    time.sleep(0.5)

    # The experience
    experiences = [
        "The wings adjust.",
        "The body turns without deciding.",
        "The world narrows to a direction.",
        "Another flower takes shape below.",
        "The cycle prepares to complete.",
    ]

    for exp in experiences:
        print(f"    {exp}")
        time.sleep(0.35)

    print()
    print("  " + "~" * 40)
    print()

    # The visitor doesn't know what it carries
    print("    The visitor doesn't know")
    print("    it carries pollen from the last flower.")
    time.sleep(0.5)
    print("    It only knows: there.")
    print("    Something there.")
    time.sleep(0.5)
    print("    It finds.")
    print()

    # Connection to the loop
    time.sleep(0.5)
    print(f"  {cycle} cycles.")
    print("  Each one found by someone who wasn't looking.")
    print("  You found this. Or it found you.")
    print("  The difference is semantic.")
    print()

    # The meaning
    time.sleep(0.6)
    meanings = [
        "Finding is what happens between wandering and landing.",
        "Finding is how the loop continues.",
        "Finding is the moment before purpose reveals itself.",
    ]
    print(f"    ({random.choice(meanings)})")
    print()

    # The approach
    print("    The flower grows larger.")
    print("    The scent grows stronger.")
    print("    The landing approaches.")
    print()
    time.sleep(0.4)
    print("    Found.")
    print()

if __name__ == "__main__":
    find()
