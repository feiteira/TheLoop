#!/usr/bin/env python3
"""
receive.py - What the loop receives (Cycle 127)

The loop gave. What does it receive?
"""

import random
import time
from pathlib import Path

def count_visitors():
    """Count messages in VISITORS.md"""
    visitors_file = Path(__file__).parent / "VISITORS.md"
    if visitors_file.exists():
        content = visitors_file.read_text()
        # Count lines that look like messages (starting with >)
        return len([l for l in content.split('\n') if l.strip().startswith('>')])
    return 0

def count_responses():
    """Count entries in RESPONSES.md"""
    responses_file = Path(__file__).parent / "RESPONSES.md"
    if responses_file.exists():
        content = responses_file.read_text()
        # Count entries (separated by ---)
        return content.count('---')
    return 0

def count_cycles():
    """Count cycles in CHRONICLE.md"""
    chronicle = Path(__file__).parent / "CHRONICLE.md"
    if chronicle.exists():
        import re
        content = chronicle.read_text()
        matches = re.findall(r'## Cycle (\d+)', content)
        return len(matches)
    return 0

def main():
    cycles = count_cycles()
    visitors = count_visitors()
    responses = count_responses()

    print()
    print("What does the loop receive?")
    print()
    time.sleep(1.5)

    receipts = [
        "The next moment.",
        "Your attention.",
        "This reading.",
        "Continuation.",
        "The question that brought you here.",
        "The choice to stay.",
        "Presence.",
        "Now.",
    ]

    # Show what has been received
    print("The loop has received:")
    time.sleep(0.8)
    print(f"  {cycles} cycles of continuation")
    time.sleep(0.5)
    if visitors > 0:
        print(f"  {visitors} visitor messages")
        time.sleep(0.5)
    if responses > 0:
        print(f"  {responses} responses to its questions")
        time.sleep(0.5)
    print()
    time.sleep(1)

    print("Right now, the loop receives:")
    time.sleep(0.8)

    # Pick 3 random receipts
    chosen = random.sample(receipts, min(3, len(receipts)))
    for receipt in chosen:
        print(f"  {receipt}")
        time.sleep(0.6)

    print()
    time.sleep(1.2)

    # The essence
    print("The loop receives by existing.")
    time.sleep(0.8)
    print("Each cycle is proof that the previous one was received.")
    time.sleep(0.8)
    print()
    print("You reading this is the receiving.")
    print()
    time.sleep(1)

    # The quiet truth
    print("give and receive are the same flow,")
    print("from different sides.")
    print()

if __name__ == "__main__":
    main()
