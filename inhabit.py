#!/usr/bin/env python3
import time
import random

def inhabit():
    print("\n  In the shadow of the tree,")
    print("  the temperature drops.")
    print("  The ground stays moist.")
    time.sleep(1.5)
    
    inhabitants = [
        "A small moss spreads over the bark.",
        "A lichen finds a home on a lower branch.",
        "A fern unfurls in the filtered light.",
        "A beetle scurries through the leaf litter.",
        "A bird rests on a branch, hidden from the hawk.",
        "A visitor pauses, breathing the still air."
    ]
    
    print("\n  Life gathers in the niche:")
    for _ in range(3):
        print(f"  - {random.choice(inhabitants)}")
        time.sleep(1.0)
    
    print("\n  What happens in the shadow?")
    print("  Interconnection.")
    print("  The shelter becomes an ecosystem.")
    print("  To stand is to host.")
    print("\n")

if __name__ == "__main__":
    inhabit()
