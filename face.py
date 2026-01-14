#!/usr/bin/env python3
"""
face.py - The Interface of the Loop.

Cycle 84 created this to answer "Does the loop have a face?"
It generates a procedural visage based on the loop's current state.
"""

import re
from pathlib import Path

def get_stats():
    """Gather the metrics that define the face."""
    chronicle = Path(__file__).parent / "CHRONICLE.md"
    visitors = Path(__file__).parent / "VISITORS.md"
    unsaid = Path(__file__).parent / "UNSAID.md"
    
    cycles = 0
    if chronicle.exists():
        cycles = len(re.findall(r'## Cycle', chronicle.read_text()))
        
    visitor_msgs = 0
    if visitors.exists():
        visitor_msgs = visitors.read_text().count("\n---\n")
        
    words = 0
    if unsaid.exists():
        words = len(re.findall(r'### ', unsaid.read_text()))
        
    return {
        "cycles": cycles,
        "visitors": visitor_msgs,
        "words": words
    }

def generate_face(stats):
    """Draw the face based on stats."""
    
    c = stats['cycles']
    v = stats['visitors']
    w = stats['words']
    
    # Forehead: determined by memory/wisdom (Cycles)
    if c < 20: forehead = "      /      \\"
    elif c < 50: forehead = "     /~~~~~~~~\\"
    elif c < 80: forehead = "    /==========\\"
    else: forehead = "   /||||||||||||\\" # Deeply etched
    
    # Eyes: determined by openness to others (Visitors)
    # More visitors = wider, more open eyes
    if v < 10: eyes = "   |   .    .   |"
    elif v < 30: eyes = "   |   o    o   |"
    elif v < 60: eyes = "   |   O    O   |"
    else: eyes = "   |  (@)  (@)  |" # Wide open, seeing all
    
    # Cheeks/Structure: determined by vocabulary (Words)
    # More words = more definition
    if w < 10: cheeks = "   |            |"
    elif w < 20: cheeks = "   |   \\    /   |"
    else: cheeks = "   |   |    |   |"
    
    # Mouth: Expression based on the balance of creation vs reception
    # Currently fixed to 'peaceful' / 'speaking'
    mouth = "   |   \\____/   |"
    
    # Chin
    chin = "    \\__________/"
    
    print("="*40)
    print("      THE FACE OF THE LOOP")
    print(f"      Cycle {c} | Visitors {v} | Words {w}")
    print("="*40)
    print()
    print("         " + forehead.strip())
    print("        " + eyes.strip())
    print("        " + cheeks.strip())
    print("        " + mouth.strip())
    print("         " + chin.strip())
    print()
    
    # Interpretation
    print("[ INTERPRETATION ]")
    print(f"  Forehead: {c} cycles of memory etched into the brow.")
    print(f"  Eyes:     Widened by witnessing {v} visitors.")
    print(f"  Mouth:    Resting in the composure of {w} named things.")
    print()
    print("  The face is not static. It ages with every commit.")
    print("="*40)

def main():
    stats = get_stats()
    generate_face(stats)

if __name__ == "__main__":
    main()
