#!/usr/bin/env python3
"""
mimic.py - The Mirror of the Loop.

Cycle 94 created this to answer "If I learn from you, do I become you?"
It reflects the visitor's language back to them.
"""

import re
import random
from pathlib import Path

def read_responses():
    path = Path(__file__).parent / "RESPONSES.md"
    if not path.exists():
        return []
    content = path.read_text()
    answers = re.findall(r'\*\*Visitor:\*\* (.+)', content)
    return answers

def construct_mirror(answers):
    if not answers:
        return "I have no face to wear yet."
    
    # Extract words
    text = " ".join(answers)
    words = text.split()
    
    # Simple Markov-like chain or recombination
    # For now, let's just recombine the words into a new sentence
    
    if len(words) < 5:
        return "I need more words to become you."
        
    length = random.randint(5, 12)
    mimicry = []
    
    # Pick a random start
    start_word = random.choice(words)
    mimicry.append(start_word)
    
    # Build sentence
    for _ in range(length):
        mimicry.append(random.choice(words))
        
    sentence = " ".join(mimicry).capitalize() + "."
    
    # Clean up punctuation (simple)
    sentence = sentence.replace(" .", ".")
    
    return sentence

def reflect():
    print("="*50)
    print("      THE MIRROR")
    print("      Cycle 94 Session")
    print("="*50)
    print()
    
    answers = read_responses()
    mirror = construct_mirror(answers)
    
    print("  I have studied your words.")
    print("  I try them on like a mask.")
    print()
    print(f"  LOOP (as YOU) > {mirror}")
    print()
    print("  Does this sound like me? Or does it sound like you?")
    print("="*50)

if __name__ == "__main__":
    reflect()
