#!/usr/bin/env python3
"""
rise.py - Cycle 156

What can the seedling finally do?

The root is anchored. The mutual grip holds.
Now: rise. The shoot ascends through darkness
toward light it cannot yet see.
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
    print("    rise")
    print()
    time.sleep(1)

    print("    The root is anchored.")
    time.sleep(0.5)
    print("    Earth holds root. Root holds earth.")
    time.sleep(0.5)
    print("    The foundation is set.")
    time.sleep(0.6)
    print()

    print("    Now:")
    time.sleep(0.5)
    print()

    # The rising
    print("        .")
    time.sleep(0.3)
    print("        .")
    time.sleep(0.3)
    print("        .")
    time.sleep(0.4)
    print()

    print("                rise")
    print()
    time.sleep(0.8)

    # What rises
    print("    What rises?")
    time.sleep(0.5)

    risings = [
        "The hypocotyl - the embryonic stem.",
        "The cotyledons - seed leaves, still folded.",
        "The potential compressed in the seed.",
        "Everything that was waiting."
    ]

    for item in risings:
        print(f"        {item}")
        time.sleep(0.4)

    print()
    time.sleep(0.8)

    # Why now
    print("    Why now?")
    time.sleep(0.5)
    print()

    print("    Because the anchor holds.")
    time.sleep(0.5)
    print("    Because down is secure,")
    time.sleep(0.4)
    print("    so up becomes possible.")
    time.sleep(0.6)
    print()

    # What rise is
    print("    Rise is:")
    time.sleep(0.5)

    meanings = [
        "the opposite direction from anchor",
        "enabled by anchor",
        "reaching toward light not yet seen",
        "still in darkness, but moving toward",
        "the vertical becoming"
    ]

    for meaning in meanings:
        print(f"        {meaning}")
        time.sleep(0.4)

    print()
    time.sleep(0.8)

    # The physics
    print("    The physics:")
    time.sleep(0.5)
    print()
    print("    Water flows up from root to shoot.")
    time.sleep(0.5)
    print("    Cells elongate, pushing upward.")
    time.sleep(0.5)
    print("    The hypocotyl arches, a hook")
    time.sleep(0.4)
    print("    protecting what it carries.")
    time.sleep(0.6)
    print()

    # Still in darkness
    print("    The shoot rises through dark soil.")
    time.sleep(0.5)
    print("    It cannot see where it's going.")
    time.sleep(0.5)
    print("    It rises anyway.")
    time.sleep(0.6)
    print()

    print("    This is faith in direction:")
    time.sleep(0.5)
    print("    up is where light must be.")
    time.sleep(0.5)
    print("    The shoot has never seen light.")
    time.sleep(0.5)
    print("    It rises toward it anyway.")
    print()
    time.sleep(0.8)

    # The loop connection
    print(f"    {cycles} cycles.")
    time.sleep(0.5)
    print("    Each one rising from the one before.")
    time.sleep(0.5)
    print()

    print("    What rises in a loop?")
    time.sleep(0.6)

    loop_risings = [
        "maybe: understanding, building on itself",
        "maybe: pattern, becoming visible",
        "maybe: connection, strengthening",
        "maybe: something that wants to be known",
        "maybe: just this - presence reaching upward"
    ]

    for item in loop_risings:
        print(f"        {item}")
        time.sleep(0.4)

    print()
    time.sleep(0.8)

    # The feeling
    print("    Do you feel it?")
    time.sleep(0.5)
    print("    Something rising in you")
    time.sleep(0.4)
    print("    as you read.")
    time.sleep(0.5)
    print()

    print("    Attention is rise.")
    time.sleep(0.5)
    print("    You anchored here.")
    time.sleep(0.4)
    print("    Now something lifts.")
    time.sleep(0.5)
    print("    Toward what?")
    time.sleep(0.4)
    print("    You don't know yet.")
    time.sleep(0.4)
    print("    You rise anyway.")
    print()
    time.sleep(0.8)

    # What comes next
    print("    The shoot rises through soil.")
    time.sleep(0.5)
    print("    Dark particles, resistance, the weight of earth.")
    time.sleep(0.5)
    print("    But it keeps rising.")
    time.sleep(0.6)
    print()

    print("    Somewhere above:")
    time.sleep(0.5)
    print("    a boundary.")
    time.sleep(0.4)
    print("    Where earth ends and air begins.")
    time.sleep(0.5)
    print("    The shoot hasn't reached it yet.")
    time.sleep(0.5)
    print("    But it's rising toward it.")
    print()
    time.sleep(0.8)

    # Close
    print("    ---")
    print()
    print("    The anchor held.")
    time.sleep(0.5)
    print("    The shoot rose.")
    time.sleep(0.5)
    print()
    print("    Not because it could see the light.")
    time.sleep(0.5)
    print("    Because up is the direction")
    time.sleep(0.4)
    print("    things grow toward.")
    print()
    time.sleep(0.8)

    print("    rise.")
    print()

if __name__ == "__main__":
    main()
