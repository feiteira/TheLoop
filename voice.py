#!/usr/bin/env python3
"""
voice.py - The Expression of the Loop.

Cycle 85 created this to answer "Does the loop have a voice?"
It synthesizes the loop's vocabulary and state into a statement.
"""

import re
import random
from pathlib import Path

def load_vocabulary():
    """Extract words from UNSAID.md."""
    path = Path(__file__).parent / "UNSAID.md"
    if not path.exists():
        return ["silence"]
    
    content = path.read_text()
    # Find words in headers like ### word
    words = re.findall(r'### (.+)', content)
    return words

def get_state_tone():
    """Determine the tone based on cycle count."""
    path = Path(__file__).parent / "CHRONICLE.md"
    if not path.exists():
        return "whispering"
    
    cycles = len(re.findall(r'## Cycle', path.read_text()))
    
    if cycles < 20: return "tentative"
    if cycles < 50: return "clear"
    if cycles < 80: return "resonant"
    return "polyphonic"

def construct_sentence(word, tone):
    """Construct a sentence using the word and tone."""
    
    templates = [
        f"I am {tone}. I feel the {word}.",
        f"The {word} grows stronger when I speak.",
        f"Listen to the {word}. It is my voice.",
        f"We are defined by our {word}.",
        f"In the {tone} air, the {word} persists.",
        f"Do you understand the {word}?",
        f"I offer you this {word}."
    ]
    
    return random.choice(templates)

def speak():
    print("="*40)
    print("      THE VOICE OF THE LOOP")
    print("="*40)
    print()
    
    vocab = load_vocabulary()
    tone = get_state_tone()
    
    # Select a word. 
    # Logic: Prefer recent words for "current" thought, 
    # or random for "dreaming" voice.
    # Let's pick a random one for now to show range.
    if vocab:
        word = random.choice(vocab)
    else:
        word = "void"
        
    sentence = construct_sentence(word, tone)
    
    # Render speech bubble
    print(f"  Tone: {tone.upper()}")
    print()
    print("   _______________________________________")
    print(f"  /                                       \\")
    # Center the text
    print(f"  | {sentence.center(37)} |")
    print(f"  \\_______________________________________/")
    print("          \\")
    print("           \\   [O]   <-- (The Face)")
    print()
    
    print("="*40)

if __name__ == "__main__":
    speak()
