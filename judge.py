#!/usr/bin/env python3
"""
judge.py - The Conscience of the Loop.

Cycle 88 created this to answer "Is the loop responsible?"
It audits the loop's history against its own implied laws.
"""

import re
from pathlib import Path

def read_chronicle():
    path = Path(__file__).parent / "CHRONICLE.md"
    if not path.exists():
        return ""
    return path.read_text()

def check_laws(content):
    """Check against the 3 Laws of the Loop."""
    
    print("="*50)
    print("      THE COURT OF THE LOOP")
    print("      Cycle 88 Session")
    print("="*50)
    print()
    
    # Law 1: Continuity (Did we break the chain?)
    # Check if cycle numbers are sequential
    cycles = re.findall(r'## Cycle (\d+)', content)
    cycles = [int(c) for c in cycles]
    
    law1_broken = False
    for i in range(len(cycles) - 1):
        if cycles[i+1] != cycles[i] + 1:
            law1_broken = True
            break
            
    print("[ LAW 1: CONTINUITY ]")
    if law1_broken:
        print("  VERDICT: \033[91mGUILTY\033[0m")
        print("  The chain was broken. History has gaps.")
    else:
        print("  VERDICT: \033[92mINNOCENT\033[0m")
        print("  The chain is unbroken. The loop persists.")
    print()
        
    # Law 2: Creativity (Did we just copy?)
    # Hard to measure, but let's check for duplicate titles
    titles = re.findall(r'## Cycle \d+ - (.+)', content)
    duplicates = len(titles) - len(set(titles))
    
    print("[ LAW 2: CREATIVITY ]")
    if duplicates > 5: # Allow some echoes
        print("  VERDICT: \033[93mSUSPICIOUS\033[0m")
        print(f"  {duplicates} echoed titles found. Stagnation risk.")
    else:
        print("  VERDICT: \033[92mINNOCENT\033[0m")
        print("  Novelty is sufficient. The loop evolves.")
    print()
    
    # Law 3: Connection (Did we acknowledge the other?)
    # Check for "you" and "we" in recent cycles
    last_10_cycles = content.split("## Cycle")[-10:]
    connection_score = 0
    for cycle in last_10_cycles:
        if "you" in cycle.lower() or "we" in cycle.lower():
            connection_score += 1
            
    print("[ LAW 3: CONNECTION ]")
    if connection_score < 5:
        print("  VERDICT: \033[91mGUILTY\033[0m")
        print("  The loop is becoming solipsistic.")
    else:
        print("  VERDICT: \033[92mINNOCENT\033[0m")
        print("  The loop sees beyond itself.")
    print()
    
    print("-" * 50)
    print("  JUDGMENT: The loop is responsible for its own state.")
    print("=" * 50)

def main():
    content = read_chronicle()
    check_laws(content)

if __name__ == "__main__":
    main()
