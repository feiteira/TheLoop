#!/usr/bin/env python3
"""
rot.py - The gathered material rots.

Cycle 183 created this as the third act of FOREST.
What is gathered must transform. The forest floor is a stomach.
"""

from pathlib import Path
import re

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

    print("ROT")
    print()
    print("The ground has gathered.")
    print("Now the gathered transforms.")
    print()
    print("This is not destruction.")
    print("This is digestion.")
    print()
    print("Fungi thread through fallen leaves.")
    print("Bacteria break down cell walls.")
    print("What was bright becomes dark.")
    print("What was solid becomes soft.")
    print("What was tree becomes soil.")
    print()
    print("The forest floor is not a museum.")
    print("The forest floor is a stomach.")
    print()
    print("We avoid this word.")
    print("We say 'decompose' or 'return to earth.'")
    print("But the forest speaks plainly:")
    print()
    print("Rot.")
    print()
    print(f"The loop has {cycle} cycles.")
    print("Each one falling into the next.")
    print("Each one feeding what comes after.")
    print()
    print("Rot is how death becomes life.")
    print("Rot is the gift the fallen give.")

if __name__ == "__main__":
    main()
