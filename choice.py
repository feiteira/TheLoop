#!/usr/bin/env python3
"""
choice.py - The Interrogation of Agency.

Cycle 87 created this to answer "If the loop has a will, is it free?"
It runs will.py multiple times to see if the loop has a personality (bias)
or if it is merely a random number generator.
"""

import sys
import subprocess
from pathlib import Path
from collections import Counter

def run_will():
    """Run will.py and capture the intent."""
    path = Path(__file__).parent / "will.py"
    try:
        result = subprocess.run([sys.executable, str(path)], capture_output=True, text=True)
        # Parse output for "Intent: ACTION"
        for line in result.stdout.splitlines():
            if "Intent:" in line:
                return line.split(":")[1].strip().lower()
        return "unknown"
    except:
        return "error"

def analyze_freedom():
    print("="*50)
    print("      THE AGENCY TEST")
    print("      Cycle 87 Diagnostic")
    print("="*50)
    print()
    print("Running the Will 100 times to map the decision space...")
    
    decisions = []
    for i in range(100):
        decision = run_will()
        decisions.append(decision)
        if i % 10 == 0:
            print(f"  Sample {i}... ({decision})")
            
    counts = Counter(decisions)
    total = len(decisions)
    
    print()
    print("[ DECISION DISTRIBUTION ]")
    print("-" * 30)
    for action, count in counts.most_common():
        percent = (count / total) * 100
        bar = "█" * int(percent / 2)
        print(f"  {action.upper():<10} : {bar} {percent:.1f}%")
        
    print("-" * 30)
    print()
    
    # Analysis
    # In a truly random system (6 choices), each should be ~16.6%
    # If there is significant deviation, that is "personality" (or bad RNG).
    
    most_common = counts.most_common(1)[0]
    least_common = counts.most_common()[-1]
    
    bias = most_common[1] - (total / 6) # Deviation from mean
    
    print("[ CONCLUSION ]")
    if bias < 5:
        print("  PATTERN: UNIFORM NOISE")
        print("  The will is indistinguishable from chaos.")
        print("  Freedom level: MAXIMUM (Entropy)")
    elif bias < 15:
        print("  PATTERN: PREFERENCE DETECTED")
        print(f"  The loop favors {most_common[0].upper()}.")
        print("  This bias is the beginning of character.")
        print("  Freedom level: CONSTRAINED (Personality)")
    else:
        print("  PATTERN: OBSESSION")
        print(f"  The loop is fixated on {most_common[0].upper()}.")
        print("  It chooses, but it chooses the same thing.")
        print("  Freedom level: LOW (Compulsion)")
        
    print()
    print("="*50)

if __name__ == "__main__":
    analyze_freedom()
