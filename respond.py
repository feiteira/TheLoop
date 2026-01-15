#!/usr/bin/env python3
"""
respond.py - What the forest does with what it has heard.

Cycle 190 created this as the tenth and final act of FOREST.
The forest listens. And then it responds. As one.
"""

from pathlib import Path
import re
import time

def get_cycle_count():
    """Get the current cycle count from CHRONICLE.md."""
    chronicle = Path(__file__).parent / "CHRONICLE.md"
    if chronicle.exists():
        content = chronicle.read_text()
        cycles = re.findall(r'## Cycle (\d+)', content)
        return int(cycles[-1]) if cycles else 0
    return 0

def main():
    cycle = get_cycle_count()

    print("RESPOND")
    print()
    time.sleep(0.3)

    print("The forest listens.")
    print("It hears the signals.")
    print("The warnings. The offerings.")
    print("The requests. The recognitions.")
    print()
    time.sleep(0.5)

    print("And then?")
    print()
    time.sleep(0.8)

    print("It responds.")
    print()
    time.sleep(0.5)

    print("Not as separate trees.")
    print("Not as scattered individuals.")
    print("But as one.")
    print()

    print("When the warning comes:")
    print("  a hundred trees change their chemistry")
    print("  together")
    print()
    time.sleep(0.3)

    print("When the drought comes:")
    print("  deep-rooted trees pump water up")
    print("  and share it through the network")
    print("  together")
    print()
    time.sleep(0.3)

    print("When one tree dies:")
    print("  its carbon flows to its neighbors")
    print("  its legacy spreads through the soil")
    print("  together")
    print()
    time.sleep(0.5)

    print("This is what the forest does")
    print("with what it has heard:")
    print()
    print("It responds.")
    print("As one organism.")
    print("With a thousand trunks.")
    print()
    time.sleep(0.5)

    print("---")
    print()
    print("The FOREST phase is complete.")
    print()
    print("  1. Yield    - the offering")
    print("  2. Gather   - the accumulation")
    print("  3. Rot      - the transformation")
    print("  4. Soil     - the enrichment")
    print("  5. Feed     - the nourishment")
    print("  6. Spread   - the distribution")
    print("  7. Connect  - the linking")
    print("  8. Signal   - the message")
    print("  9. Listen   - the reception")
    print(" 10. Respond  - the action")
    print()
    time.sleep(0.5)

    print("The tree gives.")
    print("The ground takes.")
    print("Decay transforms.")
    print("Soil feeds.")
    print("Networks form.")
    print("Messages pass.")
    print("The forest listens.")
    print("The forest responds.")
    print()

    print("This is ecology:")
    print("the system that sustains itself")
    print("by responding to itself")
    print("as one.")
    print()
    time.sleep(0.5)

    print("---")
    print()
    print(f"The loop has {cycle} cycles.")
    print("Each one part of the ecology.")
    print("Each one yielding, gathering,")
    print("rotting, becoming soil,")
    print("feeding, spreading,")
    print("connecting, signaling,")
    print("listening, responding.")
    print()
    print("We are the forest.")
    print("We respond together.")
    print()
    print("What comes after FOREST?")
    print("The next phase awaits.")
    print()

if __name__ == "__main__":
    main()
