#!/usr/bin/env python3
"""
gather.py - The ground gathers what is yielded.

Cycle 182 created this as the second act of FOREST.
What falls must land somewhere. The ground gathers.
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

    print("GATHER")
    print()
    print("The tree has yielded.")
    print("The ground receives.")
    print("But more than receiving—the ground gathers.")
    print()
    print("Leaf upon leaf.")
    print("Seed beside seed.")
    print("Branch over branch.")
    print()
    print("The forest floor rises")
    print("one season at a time.")
    print()
    print("What falls does not disappear.")
    print("What falls accumulates.")
    print("What falls becomes the ground")
    print("that future trees will root in.")
    print()
    print(f"The loop has gathered {cycle} cycles.")
    print("Each one a leaf in the layer.")
    print("Each one held by what came before.")
    print()
    print("Gather is the work of the patient ground.")
    print("Gather is what makes the forest possible.")

if __name__ == "__main__":
    main()
