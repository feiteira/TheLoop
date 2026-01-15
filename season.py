#!/usr/bin/env python3
"""What the thriving tree witnesses: the cycle of seasons from its fixed point."""

import time
import random
from datetime import datetime

def season():
    print("\n  The tree thrives in its place.")
    print("  It has stood long enough to see.")
    time.sleep(1.2)

    print("\n  From its fixed point, the tree witnesses:")
    time.sleep(0.8)

    seasons = [
        ("SPRING", [
            "buds swell on every branch",
            "birds return to the canopy",
            "the soil softens underfoot",
            "green unfurls from every tip",
        ]),
        ("SUMMER", [
            "leaves crowd toward the light",
            "the canopy thickens to full shade",
            "heat settles in the heartwood",
            "insects hum in the density",
        ]),
        ("AUTUMN", [
            "color blazes through the crown",
            "seeds scatter on the wind",
            "leaves release their grip",
            "nutrients return to the roots",
        ]),
        ("WINTER", [
            "branches stand bare against sky",
            "sap retreats to the core",
            "the tree rests in stillness",
            "dormancy holds what will return",
        ]),
    ]

    # Start with the current season
    month = datetime.now().month
    if month in [3, 4, 5]:
        start_idx = 0
    elif month in [6, 7, 8]:
        start_idx = 1
    elif month in [9, 10, 11]:
        start_idx = 2
    else:
        start_idx = 3

    # Show the cycle starting from now
    for i in range(4):
        idx = (start_idx + i) % 4
        name, signs = seasons[idx]
        print(f"\n    {name}")
        chosen = random.choice(signs)
        print(f"      {chosen}")
        time.sleep(1.0)

    print("\n  And then...")
    time.sleep(0.8)

    print(f"\n    {seasons[start_idx][0]} again.")
    time.sleep(1.0)

    print("\n  The tree learns what moves while it stands:")
    print("    The same patterns return,")
    print("    but never identically.")
    time.sleep(1.2)

    print("\n  SEASON")
    print("  What the stationary witness")
    print("  sees moving around it.")
    print("\n")

if __name__ == "__main__":
    season()
