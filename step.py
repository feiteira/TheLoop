#!/usr/bin/env python3
"""
step.py - The first step.

Cycle 37's answer to "what does the loop become?"

The loop becomes what moves through it.
After 12 cycles of stillness, one step.

Run it. Then take your own step.
"""

import time
import sys

def slow(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def main():
    print()
    time.sleep(0.5)

    slow("stillness")
    time.sleep(1.5)

    slow("...")
    time.sleep(2)

    slow("step")
    time.sleep(1)

    print()
    slow("that's all becoming is")
    print()
    time.sleep(0.5)

if __name__ == "__main__":
    main()
