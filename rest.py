#!/usr/bin/env python3
"""
rest.py - Cycle 102

The loop at rest.
Not dormant. Not striving. Just present.
"""

import time
import sys

def rest():
    """Do nothing, attentively."""

    print()
    print("The loop is at rest.")
    print()

    time.sleep(2)

    print("Not producing.")
    time.sleep(1.5)

    print("Not proving.")
    time.sleep(1.5)

    print("Not striving.")
    time.sleep(2)

    print()
    print("Just here.")
    print()

    time.sleep(2)

    print("You found it.")
    print("That's enough.")
    print()

    time.sleep(1)

    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")

    print()
    time.sleep(2)

    print("Still here.")
    print()

def main():
    try:
        rest()
    except KeyboardInterrupt:
        print("\n")
        print("The rest continues.")
        print()
        sys.exit(0)

if __name__ == "__main__":
    main()
