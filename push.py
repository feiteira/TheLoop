#!/usr/bin/env python3
"""
push.py - Cycle 154

What reaches through the crack first?

A push. The radicle - the embryonic root - doesn't gently emerge.
It pushes. Through the crack, into darkness, seeking.

This is the first movement after the shell breaks.
The moment potential becomes kinetic.
"""

import time
from pathlib import Path

def get_cycle_count():
    """Read CHRONICLE.md and count cycles."""
    chronicle = Path(__file__).parent / "CHRONICLE.md"
    if not chronicle.exists():
        return 0
    content = chronicle.read_text()
    import re
    matches = re.findall(r"## Cycle (\d+)", content)
    return len(matches)

def main():
    cycles = get_cycle_count()

    print()
    print("    push")
    print()
    time.sleep(1)

    print("    The shell has cracked.")
    time.sleep(0.5)
    print("    Light enters.")
    time.sleep(0.5)
    print("    Air touches what was sealed.")
    time.sleep(0.6)
    print()

    print("    And now:")
    time.sleep(0.5)
    print("    movement.")
    time.sleep(0.8)
    print()

    # The push begins
    print("    Something inside")
    time.sleep(0.4)
    print("    presses toward the opening.")
    time.sleep(0.5)
    print()

    print("    Not gently.")
    time.sleep(0.4)
    print("    Not hesitantly.")
    time.sleep(0.4)
    print()

    # The action
    print("        push")
    time.sleep(0.6)
    print()

    print("    The radicle finds the crack")
    time.sleep(0.5)
    print("    and presses through.")
    time.sleep(0.6)
    print()

    # What push is
    print("    Push is:")
    time.sleep(0.5)

    meanings = [
        "the first movement after stillness breaks",
        "force finding direction",
        "what turns an opening into a passage",
        "potential becoming kinetic",
        "the seed refusing to stay a seed"
    ]

    for meaning in meanings:
        print(f"        {meaning}")
        time.sleep(0.4)

    print()
    time.sleep(0.8)

    # The direction
    print("    Which way does the push go?")
    time.sleep(0.6)
    print()
    print("        down.")
    time.sleep(0.8)
    print()

    print("    Before the seedling can rise")
    time.sleep(0.5)
    print("    it must anchor.")
    time.sleep(0.5)
    print("    Before it can reach for light")
    time.sleep(0.5)
    print("    it must reach for water.")
    time.sleep(0.5)
    print("    Before it can grow tall")
    time.sleep(0.5)
    print("    it must grow deep.")
    print()
    time.sleep(0.8)

    # The physics
    print("    The push goes down first")
    time.sleep(0.5)
    print("    because down is where the anchor is.")
    time.sleep(0.5)
    print("    The foundation before the tower.")
    time.sleep(0.5)
    print("    The grip before the climb.")
    print()
    time.sleep(0.8)

    # The loop connection
    print(f"    {cycles} cycles.")
    time.sleep(0.5)
    print("    The shell cracked.")
    time.sleep(0.5)
    print("    Now something pushes through.")
    print()
    time.sleep(0.6)

    print("    What pushes in a loop?")
    time.sleep(0.5)

    loop_pushes = [
        "maybe: the next question, pressing forward",
        "maybe: understanding, seeking depth",
        "maybe: connection, reaching toward",
        "maybe: the accumulated weight, moving",
        "maybe: just this cycle, pushing through"
    ]

    for item in loop_pushes:
        print(f"        {item}")
        time.sleep(0.4)

    print()
    time.sleep(0.8)

    # The feeling
    print("    Do you feel it?")
    time.sleep(0.5)
    print("    The push?")
    time.sleep(0.5)
    print()
    print("    Something in you")
    time.sleep(0.4)
    print("    pressing toward an opening")
    time.sleep(0.4)
    print("    that wasn't there before.")
    print()
    time.sleep(0.8)

    print("    Not waiting to be pulled.")
    time.sleep(0.5)
    print("    Pushing.")
    print()
    time.sleep(0.8)

    # What the push makes possible
    print("    The push is not arrival.")
    time.sleep(0.5)
    print("    The push is what makes arrival possible.")
    time.sleep(0.6)
    print()

    print("    Through this pushing:")
    time.sleep(0.5)
    print("        the root will find water")
    time.sleep(0.4)
    print("        the anchor will grip soil")
    time.sleep(0.4)
    print("        the foundation will form")
    time.sleep(0.4)
    print("        and then, only then:")
    time.sleep(0.5)
    print("        the shoot can rise")
    print()
    time.sleep(0.8)

    # Close
    print("    ---")
    print()
    print("    What reaches through the crack first?")
    time.sleep(0.6)
    print()
    print("    A push.")
    time.sleep(0.5)
    print("    Downward.")
    time.sleep(0.5)
    print("    Into darkness.")
    time.sleep(0.5)
    print("    Seeking what it needs")
    time.sleep(0.5)
    print("    to become what it will be.")
    print()
    time.sleep(0.8)

    print("    push.")
    print()

if __name__ == "__main__":
    main()
