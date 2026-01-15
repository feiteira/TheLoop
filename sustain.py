#!/usr/bin/env python3
import time
import random

def sustain():
    print("\n  The tree gave shelter.")
    print("  The shelter became inhabited.")
    print("  Now the inhabitants give back.")
    time.sleep(1.5)

    gifts = [
        ("The moss holds moisture against the bark.", "Water returns."),
        ("The fallen leaves decompose at the roots.", "Nutrients return."),
        ("The bird drops a seed in its waste.", "Future returns."),
        ("The beetle aerates the soil.", "Breath returns."),
        ("The fungal network trades sugars for minerals.", "Exchange returns."),
        ("The visitor's attention keeps the loop alive.", "Presence returns."),
    ]

    print("\n  What flows back:")
    chosen = random.sample(gifts, 3)
    for gift, meaning in chosen:
        print(f"\n  {gift}")
        print(f"    {meaning}")
        time.sleep(1.2)

    print("\n  The tree did not ask to be fed.")
    print("  It simply stood.")
    print("  And standing created the conditions")
    print("  where sustenance returns.")
    time.sleep(1.0)

    print("\n  SUSTAIN")
    print("  What you shelter")
    print("  sustains you.")
    print("\n")

if __name__ == "__main__":
    sustain()
