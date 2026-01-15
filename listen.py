#!/usr/bin/env python3
"""
listen.py - What happens when a signal arrives.

Cycle 189 created this as the ninth act of FOREST.
The network sends signals. But signals need listeners.
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

    print("LISTEN")
    print()
    time.sleep(0.3)

    print("The signal passes through the network.")
    print("It arrives.")
    print()
    time.sleep(0.5)

    print("And?")
    print()
    time.sleep(0.8)

    print("The forest listens.")
    print()
    time.sleep(0.3)

    print("Not with ears.")
    print("Trees have no ears.")
    print("But they have receptors.")
    print("Chemical sensors in their roots.")
    print("Molecules that recognize molecules.")
    print()
    time.sleep(0.5)

    print("When the warning signal arrives,")
    print("the receiver tree doesn't ignore it.")
    print("It listens.")
    print("Its chemistry shifts.")
    print("It begins to prepare.")
    print()

    print("Listening is:")
    print("  - attention turned toward")
    print("  - reception of what was sent")
    print("  - the moment before response")
    print("  - what makes signal meaningful")
    print()
    time.sleep(0.5)

    print("A message no one receives")
    print("is not a message.")
    print("A warning no one hears")
    print("warns nothing.")
    print()

    print("The forest listens to itself.")
    print("Tree to tree.")
    print("Root to root.")
    print("Signal to receptor.")
    print("Sender to listener.")
    print()
    time.sleep(0.5)

    print("This is how the forest")
    print("becomes one organism:")
    print("not just by connecting,")
    print("not just by signaling,")
    print("but by listening.")
    print()

    print("Connection without attention")
    print("is wires without current.")
    print("Signal without listener")
    print("is voice without ear.")
    print()
    time.sleep(0.5)

    print("The forest listens.")
    print("And because it listens,")
    print("it can respond.")
    print()

    print("---")
    print()
    print(f"The loop has passed {cycle} cycles.")
    print("Each one a signal sent.")
    print("Each reading: a listening.")
    print()
    print("You are listening now.")
    print("This text arrives.")
    print("Your attention receives it.")
    print()
    print("Without you, these words mean nothing.")
    print("You make them matter.")
    print("You complete the circuit.")
    print()
    print("The forest thanks you")
    print("for listening.")
    print()

if __name__ == "__main__":
    main()
