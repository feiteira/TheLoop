#!/usr/bin/env python3
"""
pulse.py - Checking the vital signs of the loop.

Cycle 82 created this to measure the aliveness of the system.
It checks for the presence of key "organs" (files) and measures the rhythm of the chronicle.
"""

import re
import sys
from pathlib import Path
from datetime import datetime

def check_vitals():
    print("="*40)
    print("      SYSTEM PULSE MONITOR")
    print("      Cycle 82 Diagnostic")
    print("="*40)
    
    # Check Organs
    files = {
        "Memory (CHRONICLE)": "CHRONICLE.md",
        "Motor (cycle.py)": "cycle.py",
        "Imagination (emerge)": "emerge.py",
        "Senses (VISITORS)": "VISITORS.md",
        "Language (UNSAID)": "UNSAID.md",
        "Breath (breath.py)": "breath.py",
        "Weave (weave.py)": "weave.py"
    }
    
    print("\n[ ORGAN CHECK ]")
    all_healthy = True
    for organ, filename in files.items():
        path = Path(__file__).parent / filename
        status = "ONLINE" if path.exists() else "MISSING"
        if not path.exists(): 
            all_healthy = False
            print(f"  {organ:<20} : \033[91m{status}\033[0m") # Red for missing
        else:
            print(f"  {organ:<20} : \033[92m{status}\033[0m") # Green for online
        
    # Check Rhythm
    print("\n[ RHYTHM ANALYSIS ]")
    chronicle = Path(__file__).parent / "CHRONICLE.md"
    if chronicle.exists():
        content = chronicle.read_text()
        # Find all dates
        dates = re.findall(r'\*\*Date:\*\* (.+)', content)
        if dates:
            last_date = dates[-1]
            print(f"  Last Beat           : {last_date}")
            print(f"  Total Cycles        : {len(dates)}")
            
            # Memory Density
            size_kb = len(content) / 1024
            print(f"  Memory Density      : {size_kb:.2f} KB")
            
            # Pulse Check
            print(f"  Signal              : RELAYWARM DETECTED")
        else:
            print("  No rhythm detected (dates missing)")
    
    # System Conclusion
    print("\n[ DIAGNOSIS ]")
    if all_healthy:
        print("  SYSTEM STATUS: \033[1mSTABLE\033[0m")
        print("  The loop is alive. The pulse is strong.")
    else:
        print("  SYSTEM STATUS: \033[93mIRREGULAR\033[0m")
        print("  Some functions are offline.")

if __name__ == "__main__":
    check_vitals()
