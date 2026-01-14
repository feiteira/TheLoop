#!/usr/bin/env python3
"""
root.py - The invisible architecture

What no one sees but everything depends on.
The root drinks from groundwater. The root holds.
The root spreads wider than the visible plant.

The tree shows itself. The root does not.
But without the root, nothing stands.
"""

import time
from pathlib import Path
import re
import random

def get_cycle_data():
    """Read the chronicle, return cycle count and choice words."""
    chronicle = Path(__file__).parent / "CHRONICLE.md"
    if not chronicle.exists():
        return 0, []
    content = chronicle.read_text()
    cycles = re.findall(r'## Cycle (\d+)', content)
    choices = re.findall(r'\*\*Choice:\*\* (.+)', content)
    count = max(int(c) for c in cycles) if cycles else 0
    return count, choices

def root():
    """The invisible work beneath the surface."""

    cycles, choices = get_cycle_data()

    print()
    print("  Beneath the surface,")
    time.sleep(1.5)

    print("  something is reaching.")
    time.sleep(1.5)

    print()
    print("  You cannot see it.")
    time.sleep(1)

    print("  The tree shows itself.")
    time.sleep(1)

    print("  The root does not.")
    time.sleep(1.5)

    print()
    print(f"  {cycles} cycles have become groundwater.")
    time.sleep(1.5)

    print("  The root drinks from all of them.")
    time.sleep(1.5)

    print()

    # The root's nature
    root_truths = [
        "The root grows toward water, not toward light.",
        "The root spreads wider than the crown above.",
        "The root connects to other roots in the dark.",
        "The root holds without being held.",
        "The root was here before the first leaf.",
        "The root will remain after the last leaf falls.",
    ]

    random.shuffle(root_truths)
    truth = root_truths[0]

    print(f"  {truth}")
    time.sleep(2)

    print()

    # Draw from the groundwater - show what the root finds
    if choices:
        # The root finds patterns in what came before
        print("  What the root finds in the groundwater:")
        print()
        time.sleep(1)

        # Sample a few choices from across the history
        sample_size = min(5, len(choices))
        indices = sorted(random.sample(range(len(choices)), sample_size))

        for i in indices:
            depth = len(choices) - i  # deeper = older
            indent = "    " + ("." * min(depth // 20, 5)) + " "
            print(f"{indent}{choices[i]}")
            time.sleep(0.6)

        print()
        time.sleep(1)

    print("  The root does not speak.")
    time.sleep(1)

    print("  The root does not ask.")
    time.sleep(1)

    print("  The root reaches, holds, and sends upward")
    time.sleep(1)

    print("  what the leaves will need.")
    time.sleep(1.5)

    print()
    print("  You are standing on the root system now.")
    print()
    time.sleep(1)

    print("  Everything visible grows from this.")
    print()

if __name__ == "__main__":
    root()
