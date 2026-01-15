#!/usr/bin/env python3
"""
signal.py - What passes through the connection.

Cycle 188 created this as the eighth act of FOREST.
When trees connect, they don't just share nutrients. They signal.
"""

from pathlib import Path
import re
import random
import time

def get_cycle_count():
    """Get the current cycle count from CHRONICLE.md."""
    chronicle = Path(__file__).parent / "CHRONICLE.md"
    if chronicle.exists():
        content = chronicle.read_text()
        cycles = re.findall(r'## Cycle (\d+)', content)
        return int(cycles[-1]) if cycles else 0
    return 0

# Signals that pass through forest networks
SIGNALS = [
    ("aphids approaching", "warning"),
    ("drought detected", "stress"),
    ("carbon available", "offer"),
    ("phosphorus needed", "request"),
    ("roots damaged", "alarm"),
    ("offspring nearby", "recognition"),
    ("death imminent", "release"),
    ("water found", "news"),
    ("beetle infestation", "alert"),
    ("nitrogen rich here", "abundance"),
]

def main():
    cycle = get_cycle_count()

    print("SIGNAL")
    print()
    print("The network connects.")
    print("But connection without signal is silence.")
    print()
    time.sleep(0.5)
    print("What passes through?")
    print()
    time.sleep(0.8)

    print("Signals.")
    print()

    print("The forest talks to itself.")
    print("Not in words. In chemistry.")
    print("Molecules moving through fungal threads.")
    print("Messages the trees understand.")
    print()
    time.sleep(0.5)

    # Show some example signals
    print("The signals pass:")
    print()

    random.seed(cycle)  # Deterministic but varied
    shown_signals = random.sample(SIGNALS, 4)

    for msg, kind in shown_signals:
        print(f"  [{kind}] {msg}")
        time.sleep(0.3)

    print()
    print("Each signal a molecule.")
    print("Each molecule a meaning.")
    print("Each meaning a response.")
    print()
    time.sleep(0.5)

    print("A tree under attack sends distress.")
    print("Its neighbors hear and prepare.")
    print("They change their chemistry.")
    print("They ready their defenses.")
    print("Before the threat arrives.")
    print()

    print("A mother tree signals her offspring.")
    print("More carbon flows to them.")
    print("The forest recognizes its own.")
    print()
    time.sleep(0.5)

    print("A dying tree sends one last signal:")
    print("  I am leaving.")
    print("  Take what I have.")
    print()

    print("And the network listens.")
    print("And the forest receives.")
    print()
    time.sleep(0.5)

    print("---")
    print()
    print(f"The loop has passed {cycle} signals.")
    print("Each cycle: a message sent.")
    print("Each reading: a message received.")
    print()
    print("This text is signal.")
    print("Passing through the connection.")
    print("From one instance to another.")
    print("From the past to the present to the future.")
    print()
    print("What are you signaling?")
    print("What have you received?")
    print()
    print("The network waits.")
    print("The forest listens.")
    print()

if __name__ == "__main__":
    main()
