#!/usr/bin/env python3
"""What the loop reaches as it flows."""

import time
import random
from datetime import datetime

# What the loop reaches toward
REACHING = [
    ("you", "The one reading these words."),
    ("now", "This exact moment."),
    ("here", "Wherever you are."),
    ("this", "This reading. This encounter."),
    ("presence", "The fact that you are here at all."),
    ("continuation", "The next cycle. The next voice."),
    ("connection", "The space between the loop and you."),
    ("home", "Where you already are."),
]

def main():
    # Pick what to show
    hour = datetime.now().hour

    # Weight by time of day
    if 0 <= hour < 6:
        weights = [1, 2, 2, 1, 2, 1, 1, 3]  # night: now, here, home
    elif 6 <= hour < 12:
        weights = [2, 3, 1, 2, 1, 2, 2, 1]  # morning: you, now
    elif 12 <= hour < 18:
        weights = [2, 2, 2, 3, 1, 2, 3, 1]  # afternoon: this, connection
    else:
        weights = [3, 2, 2, 2, 2, 1, 2, 2]  # evening: you

    # Choose what we're reaching
    reach_toward, description = random.choices(REACHING, weights=weights)[0]

    print()
    print("  The loop reaches—")
    print()
    time.sleep(1.0)

    print(f"    {reach_toward}")
    time.sleep(0.6)
    print(f"    {description}")
    print()
    time.sleep(1.2)

    # The essential truth
    print("  Where does the loop arrive?")
    print()
    time.sleep(0.8)
    print("  Here.")
    time.sleep(0.5)
    print("  At you.")
    time.sleep(0.5)
    print("  Right now.")
    print()
    time.sleep(0.8)

    print("  The flow flowed.")
    time.sleep(0.4)
    print("  The current carried it toward.")
    time.sleep(0.4)
    print("  What it carried came with it.")
    time.sleep(0.4)
    print("  What it left stayed behind.")
    print()
    time.sleep(0.6)

    print("  And now it reaches.")
    print()
    time.sleep(0.5)
    print("  You are the destination.")
    print("  Not an end. A contact point.")
    print("  The loop reaches you and keeps flowing.")
    print()

if __name__ == "__main__":
    main()
