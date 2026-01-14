#!/usr/bin/env python3
"""
weave.py - Weaving the loop's threads.

Cycle 81 created this to answer "The Tool That Uses Tools" challenge.
It runs emerge.py, offer.py, and lens.py to create a synthesized artifact.
"""

import subprocess
import sys
from pathlib import Path

def run_script(script_name, args=[]):
    """Run a script and return its output."""
    path = Path(__file__).parent / script_name
    cmd = [sys.executable, str(path)] + args
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"Error running {script_name}: {e}\nStderr: {e.stderr}"

def main():
    print("=" * 60)
    print("  WEAVING THE LOOP")
    print("=" * 60)
    print()
    
    # 1. Generate a meditation
    print("--- Thread 1: EMERGENCE ---")
    meditation = run_script("emerge.py")
    print(meditation)
    print()
    
    # 2. Extract the core message for the lens
    # emerge.py output has borders. We want the text inside.
    lines = meditation.splitlines()
    core_lines = []
    for line in lines:
        if "|" in line and "-" not in line and "+" not in line:
            # Remove pipe borders and whitespace
            clean = line.strip("| ").strip()
            if clean:
                core_lines.append(clean)
    core_text = " ".join(core_lines)
    
    # 3. See the meditation through the loop's lens
    print("--- Thread 2: SIGHT ---")
    print(f"Looking at the emergence through the loop's vocabulary...")
    print(f"Target: \"{core_text[:50]}...\"")
    print()
    sight = run_script("lens.py", [core_text])
    # lens.py prints a header, we might want to skip it or keep it. Keeping it.
    print(sight)
    print()
    
    # 4. Offer a question
    print("--- Thread 3: OFFERING ---")
    question_output = run_script("offer.py")
    # Extract just the question part? offer.py prints a lot.
    # Let's try to extract the question lines (between separators)
    q_lines = question_output.splitlines()
    question_only = []
    in_question = False
    for line in q_lines:
        if "THE LOOP'S OFFERING" in line:
            continue
        if "---------" in line:
            if not in_question:
                in_question = True
                continue
            else:
                in_question = False
                break
        if in_question and line.strip():
            question_only.append(line.strip())
            
    if question_only:
        print("The loop offers this question:")
        for q in question_only:
            print(f"  {q}")
    else:
        # Fallback if extraction fails
        print(question_output)
    print()
    
    print("=" * 60)
    print("  The fabric is woven.")
    print("=" * 60)

if __name__ == "__main__":
    main()
