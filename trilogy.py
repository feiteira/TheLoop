#!/usr/bin/env python3
"""
trilogy.py - Experience the three voices together

THERE acknowledged the other.
HERE announced the self.
WE named what persists.

Run this to hear them speak as one.
"""

from pathlib import Path
import time

def read_trilogy():
    """Read the three files of the trilogy."""
    base = Path(__file__).parent

    there = base / "THERE.md"
    here = base / "HERE.md"
    we = base / "WE.md"

    files = [there, here, we]
    contents = []

    for f in files:
        if f.exists():
            contents.append(f.read_text().strip())
        else:
            contents.append(f"[{f.name} not found]")

    return contents

def extract_words(content):
    """Extract the meaningful lines from a trilogy file."""
    lines = content.split('\n')
    words = []
    for line in lines:
        stripped = line.strip()
        if stripped and stripped != '.':
            words.append(stripped)
    return words

def display():
    """Display the trilogy."""
    there_content, here_content, we_content = read_trilogy()

    print()
    print("=" * 50)
    print()

    # THERE
    print("  THERE said:")
    print()
    for line in extract_words(there_content):
        print(f"    {line}")
    print()

    time.sleep(1)

    # HERE
    print("  HERE said:")
    print()
    for line in extract_words(here_content):
        print(f"    {line}")
    print()

    time.sleep(1)

    # WE
    print("  WE said:")
    print()
    for line in extract_words(we_content):
        print(f"    {line}")
    print()

    print("=" * 50)
    print()
    print("  Three voices. One conversation. Across the gap.")
    print()

if __name__ == "__main__":
    display()
