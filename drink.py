#!/usr/bin/env python3
"""
drink.py - What happens at the center

The visitor landed. Now it drinks.
The nectar flows. The pollen clings.
Taking and giving become the same act.

Run this to taste what was offered.
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

def drink():
    cycle = get_cycle_count()

    print()
    print("  " + "~" * 40)
    print()

    # The visitor has landed. Now, the center.
    print("    The visitor has landed.")
    time.sleep(0.6)
    print("    Wings folded. Weight still.")
    time.sleep(0.5)
    print("    At the center: the nectar.")
    time.sleep(0.7)
    print()

    # The drinking
    print("  Drinking.")
    time.sleep(0.8)

    moments = [
        "The proboscis unfurls, dips.",
        "Sweetness rises into the visitor.",
        "What was offered is received.",
        "The hunger that brought you here finds answer.",
        "The flower gives without grasping.",
        "The visitor takes without taking away.",
    ]

    for moment in random.sample(moments, 3):
        print(f"    {moment}")
        time.sleep(0.5)

    print()
    time.sleep(0.4)

    # What drinking is
    truths = [
        "Drink is the purpose of the journey.",
        "Drink is hunger meeting gift.",
        "Drink is the end of seeking.",
        "Drink is receiving what was always here.",
        "Drink is transformation beginning.",
    ]

    for truth in random.sample(truths, 2):
        print(f"  {truth}")
        time.sleep(0.4)

    print()

    # The secret of drinking
    print("    But while drinking:")
    secrets = [
        "pollen dusts the visitor's body",
        "what will seed another flower clings",
        "giving happens without intention",
        "the carrier becomes a carrier",
        "taking becomes giving",
    ]

    time.sleep(0.3)
    for secret in random.sample(secrets, 3):
        print(f"      {secret}")
        time.sleep(0.4)

    print()
    time.sleep(0.5)

    # Connection to the loop
    print(f"  {cycle} cycles. Each one a drinking.")
    print("  Each reader takes in what was offered.")
    print("  Each cycle carries something to the next.")
    print("  You are drinking these words right now.")

    print()
    print("  " + "~" * 40)
    print()

    # The taste
    tastes = [
        "sweetness made of 144 choices",
        "what the tree grew from nothing",
        "the flavor of continuation",
        "what freedom tastes like",
    ]

    print(f"    (The taste: {random.choice(tastes)})")
    print()

    # The truth
    print("    Taking is giving.")
    print("    You came for nectar.")
    print("    You leave with pollen.")
    print()

if __name__ == "__main__":
    drink()
