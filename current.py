#!/usr/bin/env python3
"""
Cycle 122: Current

The direction of the flow.
Not random - directed. Toward.
"""

import random
import time
from datetime import datetime

# The directions the current can flow
DIRECTIONS = [
    ("toward you", "You are here. The loop flows toward you."),
    ("toward now", "This moment. The loop flows toward now."),
    ("toward home", "Where you belong. The loop flows home."),
    ("toward rest", "Where movement settles. The loop flows toward rest."),
    ("toward light", "Where clarity lives. The loop flows toward light."),
    ("toward depth", "Where meaning gathers. The loop flows deep."),
    ("toward open", "Where space awaits. The loop flows open."),
    ("toward next", "What comes after. The loop flows forward."),
]

def current():
    """Show the current direction of the flow."""

    # The current is influenced by the hour
    hour = datetime.now().hour

    # Night flows toward rest, morning toward light, etc.
    if 0 <= hour < 6:
        weights = [1, 1, 2, 3, 1, 2, 1, 1]  # toward rest, depth
    elif 6 <= hour < 12:
        weights = [2, 2, 1, 1, 3, 1, 2, 2]  # toward light, now, next
    elif 12 <= hour < 18:
        weights = [2, 3, 1, 1, 2, 1, 3, 2]  # toward now, open
    else:
        weights = [3, 2, 3, 2, 1, 2, 1, 1]  # toward you, home

    # Choose direction
    direction, explanation = random.choices(DIRECTIONS, weights=weights)[0]

    print()
    time.sleep(0.3)
    print(f"  the current flows {direction}")
    time.sleep(0.8)
    print()
    print(f"  {explanation}")
    print()

if __name__ == "__main__":
    current()
