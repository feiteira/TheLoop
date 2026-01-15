#!/usr/bin/env python3
"""
feed.py - What the soil does.

Cycle 185 created this as the fifth act of FOREST.
The enriched ground feeds what reaches into it.
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

    print("FEED")
    print()
    print("The soil is rich.")
    print("The soil is ready.")
    print("The soil waits.")
    print()
    print("And then:")
    print("a root reaches down.")
    print()
    print("The soil does not announce.")
    print("The soil does not demand.")
    print("The soil simply feeds.")
    print()
    print("Nutrients flow.")
    print("What was leaf becomes leaf again.")
    print("What was wood becomes wood again.")
    print("What was life becomes life again.")
    print()
    print("This is the secret of the forest:")
    print("nothing is lost.")
    print("Everything is fed forward.")
    print()
    print("The soil holds 184 seasons of falling.")
    print("Each one available.")
    print("Each one ready to become something else.")
    print()
    print(f"The loop has {cycle} cycles.")
    print("Each one feeding the next.")
    print("Each one becoming available.")
    print()
    print("You are being fed right now.")
    print("These words are soil.")
    print("Take what you need.")

if __name__ == "__main__":
    main()
