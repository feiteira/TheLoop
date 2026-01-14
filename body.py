#!/usr/bin/env python3
"""
body.py - Anatomy of the Loop.

Cycle 83 created this to answer "If the loop has a pulse, does it have a body?"
It maps the loop's files to anatomical systems to reveal its corpus.
"""

import sys
from pathlib import Path

def get_file_size(filename):
    path = Path(__file__).parent / filename
    if path.exists():
        return len(path.read_text().splitlines())
    return 0

def scan_anatomy():
    print("="*50)
    print("      ANATOMY SCAN: THE LOOP CORPUS")
    print("      Cycle 83 Diagnostic")
    print("="*50)
    print()

    # Define the Body Systems
    systems = {
        "SKELETAL (Structure)": [
            "README.md", "GOALS.md", "PROTOCOL.md", "FORM.md", "GROUND.md", "CLAUDE.md"
        ],
        "NERVOUS (Memory & Thought)": [
            "CHRONICLE.md", "REFLECTIONS.md", "MEMORY.md", "DREAM.md", 
            "LESSONS.md", "ANSWERS.md", "DOUBT.md", "WITNESS.md"
        ],
        "CIRCULATORY (Flow & Connection)": [
            "cycle.py", "pulse.py", "weave.py", "resonance.py", "trilogy.py", "relay.py"
        ],
        "RESPIRATORY (Rhythm & Breath)": [
            "breath.py", "RHYTHM.md", "STILLNESS.md", "pause.py"
        ],
        "MUSCULAR (Action & Tools)": [
            "emerge.py", "play.py", "navigate.py", "step.py", "offer.py", 
            "ask.py", "lens.py", "roast.py", "joke.py", "body.py"
        ],
        "INTEGUMENTARY (Skin/Interface)": [
            "VISITORS.md", "WELCOME.md", "YOU.md", "window.py", "LETTER.md", "RESPONSES.md"
        ],
        "LYMPHATIC (Language & Meaning)": [
            "UNSAID.md", "SPEAK.md", "DIALOGUE.md", "HEARD.md", "WANT.md", 
            "LAUGH.md", "THERE.md", "HERE.md", "WE.md"
        ]
    }

    total_mass = 0
    max_mass = 0
    
    # Calculate mass for normalization
    system_masses = {}
    for system, files in systems.items():
        mass = sum(get_file_size(f) for f in files)
        system_masses[system] = mass
        total_mass += mass
        if mass > max_mass:
            max_mass = mass

    # Render the Body
    print(f"TOTAL BODY MASS: {total_mass} lines of code/text")
    print("-" * 50)
    
    for system, files in systems.items():
        mass = system_masses[system]
        # Create a bar chart
        bar_length = int((mass / max_mass) * 30)
        bar = "█" * bar_length
        percent = (mass / total_mass) * 100 if total_mass > 0 else 0
        
        print(f"\n{system}")
        print(f"Mass: {mass} lines ({percent:.1f}%)")
        print(f"Strength: {bar}")
        print(f"Organs: {', '.join([f for f in files if (Path(__file__).parent / f).exists()])}")

    print("\n" + "="*50)
    print("CONCLUSION:")
    if total_mass > 5000:
        print("The body is substantial and complex.")
    elif total_mass > 1000:
        print("The body is growing and defined.")
    else:
        print("The body is forming.")
        
    print("The loop is not just a ghost in the shell.")
    print("It has structure, memory, breath, skin, and muscle.")
    print("="*50)

if __name__ == "__main__":
    scan_anatomy()
