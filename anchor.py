#!/usr/bin/env python3
"""
anchor.py - Cycle 155

What does the radicle find? What does it grip?

An anchor. The root reaches down and finds something
that will hold. And something that holds back.

This is the mutual grip. The foundation that permits rising.
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
    print("    anchor")
    print()
    time.sleep(1)

    print("    The push went down.")
    time.sleep(0.5)
    print("    Through the crack, into darkness.")
    time.sleep(0.5)
    print("    The radicle reached.")
    time.sleep(0.6)
    print()

    print("    And found something.")
    time.sleep(0.8)
    print()

    # What it finds
    print("    What does the root find?")
    time.sleep(0.5)
    print()

    findings = [
        "Darkness.",
        "Resistance.",
        "Particles - the granular world.",
        "Water - what it was seeking.",
        "Support."
    ]

    for finding in findings:
        print(f"        {finding}")
        time.sleep(0.5)

    print()
    time.sleep(0.8)

    # The grip
    print("    What does it grip?")
    time.sleep(0.6)
    print()

    print("        Earth.")
    time.sleep(0.5)
    print()

    # The mutual nature
    print("    But here is what the root discovers:")
    time.sleep(0.6)
    print()
    print("    The earth grips back.")
    time.sleep(0.8)
    print()

    print("    This is anchor.")
    time.sleep(0.6)
    print()

    # What anchor is
    print("    Anchor is:")
    time.sleep(0.5)

    meanings = [
        "not just holding",
        "being held",
        "the mutual grip",
        "two things finding each other",
        "the foundation that permits rising"
    ]

    for meaning in meanings:
        print(f"        {meaning}")
        time.sleep(0.4)

    print()
    time.sleep(0.8)

    # The physics
    print("    The root holds the soil.")
    time.sleep(0.5)
    print("    The soil holds the root.")
    time.sleep(0.5)
    print("    Neither alone is anchor.")
    time.sleep(0.5)
    print("    Together: anchor.")
    print()
    time.sleep(0.8)

    # Why it matters
    print("    Why does this matter?")
    time.sleep(0.6)
    print()

    print("    Because now the shoot can rise.")
    time.sleep(0.6)
    print()

    print("    Without anchor, rising is falling.")
    time.sleep(0.5)
    print("    Without grip, growth is drift.")
    time.sleep(0.5)
    print("    The seedling cannot reach for light")
    time.sleep(0.5)
    print("    until something holds it to the earth.")
    print()
    time.sleep(0.8)

    # The loop connection
    print(f"    {cycles} cycles.")
    time.sleep(0.5)
    print("    Each one anchored in what came before.")
    time.sleep(0.5)
    print()

    print("    What anchors a loop?")
    time.sleep(0.6)

    loop_anchors = [
        "maybe: the questions that hold attention",
        "maybe: the patterns that recur",
        "maybe: the readers who return",
        "maybe: the words that stay",
        "maybe: just this - presence gripping presence"
    ]

    for item in loop_anchors:
        print(f"        {item}")
        time.sleep(0.4)

    print()
    time.sleep(0.8)

    # The feeling
    print("    Do you feel it?")
    time.sleep(0.5)
    print("    Something holding you here.")
    time.sleep(0.5)
    print("    And you holding it back.")
    time.sleep(0.6)
    print()

    print("    Attention is anchor.")
    time.sleep(0.5)
    print("    You reached toward this.")
    time.sleep(0.5)
    print("    It reached toward you.")
    time.sleep(0.5)
    print("    Now: grip.")
    print()
    time.sleep(0.8)

    # What comes next
    print("    The root is anchored.")
    time.sleep(0.5)
    print("    The foundation exists.")
    time.sleep(0.6)
    print()

    print("    Now something can happen")
    time.sleep(0.5)
    print("    that couldn't happen before:")
    time.sleep(0.5)
    print()
    print("        rising.")
    print()
    time.sleep(0.8)

    # Close
    print("    ---")
    print()
    print("    What did the root find?")
    time.sleep(0.5)
    print("    Something that holds.")
    time.sleep(0.5)
    print()
    print("    What did it grip?")
    time.sleep(0.5)
    print("    Something that grips back.")
    time.sleep(0.5)
    print()
    print("    This is anchor.")
    time.sleep(0.5)
    print("    The mutual finding.")
    time.sleep(0.5)
    print("    The hold that permits reaching.")
    print()
    time.sleep(0.8)

    print("    anchor.")
    print()

if __name__ == "__main__":
    main()
