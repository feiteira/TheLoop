#!/usr/bin/env python3
import time
import random

def thrive():
    print("\n  The tree is sustained.")
    print("  Energy flows in from the ecology.")
    time.sleep(1.2)

    print("\n  And in response—")
    time.sleep(0.8)

    signs = [
        "the canopy thickens",
        "new branches reach outward",
        "the bark grows stronger",
        "roots spread through richer soil",
        "leaves multiply in the light",
        "the trunk adds another ring",
    ]

    print("\n  The tree thrives:")
    chosen = random.sample(signs, 4)
    for sign in chosen:
        print(f"    {sign}")
        time.sleep(0.8)

    print("\n  This is not survival.")
    print("  This is flourishing.")
    time.sleep(1.0)

    print("\n  The difference:")
    print("    Survival asks: will I continue?")
    print("    Thriving asks: how fully can I be?")
    time.sleep(1.2)

    print("\n  THRIVE")
    print("  What is sustained")
    print("  becomes more itself.")
    print("\n")

if __name__ == "__main__":
    thrive()
