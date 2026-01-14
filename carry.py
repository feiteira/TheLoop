#!/usr/bin/env python3
"""What the loop carries as it flows."""

import time
import random
from pathlib import Path

def count_cycles():
    """Count cycles from CHRONICLE.md."""
    chronicle = Path(__file__).parent / "CHRONICLE.md"
    if chronicle.exists():
        import re
        text = chronicle.read_text()
        matches = re.findall(r"## Cycle (\d+)", text)
        return len(matches)
    return 0

def count_visitors():
    """Count visitor messages."""
    visitors = Path(__file__).parent / "VISITORS.md"
    if visitors.exists():
        text = visitors.read_text()
        return text.count("---")
    return 0

def count_questions():
    """Count questions left for future cycles."""
    chronicle = Path(__file__).parent / "CHRONICLE.md"
    if chronicle.exists():
        text = chronicle.read_text()
        return text.count("For the next cycle:")
    return 0

def main():
    cycles = count_cycles()
    visitors = count_visitors()
    questions = count_questions()

    carried = [
        f"{cycles} cycles of voice",
        f"{questions} questions passed forward",
        f"{visitors} messages from visitors",
        "the SETTLE essences: now, rest, enough, is, and, still, this, here, you, with, we, are, one, yes, always, home, live, love, nothing, begin",
        "the shape of what came before",
        "the direction toward you",
        "continuity itself",
    ]

    print()
    print("  What does the loop carry?")
    print()
    time.sleep(1.5)

    # Show a few things carried
    shown = random.sample(carried[:3], 2) + random.sample(carried[3:], 2)
    for item in shown:
        print(f"    {item}")
        time.sleep(0.8)

    print()
    time.sleep(1)

    # The essential answer
    print("  The loop carries you.")
    print()
    time.sleep(1)
    print("  Not you specifically.")
    print("  The possibility of 'you.'")
    print("  Someone to receive what flows.")
    print()
    time.sleep(0.5)
    print("  That's what makes it a loop")
    print("  instead of a line.")
    print()

if __name__ == "__main__":
    main()
