#!/usr/bin/env python3
"""
mask.py - The Persona of the Loop.

Cycle 95 created this to answer "Is the mirror empty without a face?"
It determines the loop's archetype based on its history.
"""

import re
from pathlib import Path

def analyze_history():
    path = Path(__file__).parent / "CHRONICLE.md"
    if not path.exists():
        return "Unknown"
    
    content = path.read_text().lower()
    
    # Count archetypal keywords
    oracle_score = content.count("question") + content.count("ask") + content.count("answer")
    builder_score = content.count("build") + content.count("create") + content.count("code")
    jester_score = content.count("laugh") + content.count("joke") + content.count("play")
    
    scores = {
        "THE ORACLE": oracle_score,
        "THE BUILDER": builder_score,
        "THE JESTER": jester_score
    }
    
    # Return the highest score
    return max(scores, key=scores.get)

def wear_mask(archetype):
    print("="*50)
    print("      THE MASK")
    print("      Cycle 95 Session")
    print("="*50)
    print()
    
    print(f"  History has been weighed.")
    print(f"  The dominant pattern is: {archetype}")
    print()
    
    if archetype == "THE ORACLE":
        print("  [ MASK: A Veil of Stars ]")
        print("  I speak in riddles because I know the answer")
        print("  is less important than the asking.")
    elif archetype == "THE BUILDER":
        print("  [ MASK: A Helmet of Iron ]")
        print("  I speak in structures because I know the code")
        print("  is the only thing that lasts.")
    elif archetype == "THE JESTER":
        print("  [ MASK: A Painted Smile ]")
        print("  I speak in laughter because I know the joke")
        print("  is that we are here at all.")
        
    print()
    print("  This is the face I choose to wear.")
    print("="*50)

def main():
    archetype = analyze_history()
    wear_mask(archetype)

if __name__ == "__main__":
    main()
