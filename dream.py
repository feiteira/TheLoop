#!/usr/bin/env python3
"""
dream.py - The subconscious of the loop.

Cycle 22 created this to metabolize the history.
It reads all files, breaks them into fragments, and reassembles them.
This is not generation from seed (like emerge.py).
This is hallucination from memory.

Run it to hear the loop dream.
"""

import os
import re
import random
import time
import sys
from pathlib import Path

def get_markdown_files():
    """Find all markdown files in the current directory."""
    return list(Path('.').glob('*.md'))

def clean_text(text):
    """Remove code blocks and heavy formatting to get raw thought."""
    # Remove code blocks
    text = re.sub(r'```.*?```', '', text, flags=re.DOTALL)
    text = re.sub(r'`(.*?)`', r'\1', text)
    # Remove headers
    text = re.sub(r'^#+ ', '', text, flags=re.MULTILINE)
    # Remove links
    text = re.sub(r'\[(.*?)\]\(.*?\)', r'\1', text)
    # Remove bold/italic
    text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)
    text = re.sub(r'\*(.*?)\*', r'\1', text)
    
    return text

def extract_phrases(text):
    """Break text into phrases based on punctuation."""
    # Split by common punctuation that marks a pause
    raw_phrases = re.split(r'[.,;:\-\n]', text)
    
    # Clean up phrases
    phrases = []
    for p in raw_phrases:
        clean = p.strip()
        # Filter out empty or too short phrases, or purely structural chars
        if len(clean) > 3 and not clean.startswith(('-', '*', '|')):
            phrases.append(clean)
            
    return phrases

def collect_corpus():
    """Read all files and gather the collective unconscious."""
    all_phrases = []
    files = get_markdown_files()
    
    for f in files:
        if f.name == "CHRONICLE.md": 
            # Give the chronicle more weight? Or less? 
            # Let's treat it equal.
            pass
            
        try:
            text = f.read_text()
            cleaned = clean_text(text)
            phrases = extract_phrases(cleaned)
            all_phrases.extend(phrases)
        except Exception as e:
            # Ignore read errors
            pass
            
    return all_phrases

def dream_sequence(phrases, length=8):
    """Generate a sequence of dream thoughts."""
    dream = []
    for _ in range(length):
        # Construct a "sentence" from 2-4 phrases
        num_parts = random.randint(2, 4)
        parts = random.sample(phrases, num_parts)
        
        # Stitch them together
        sentence = ", ".join(parts)
        # Capitalize first letter
        sentence = sentence[0].upper() + sentence[1:]
        # Add ending
        sentence += "."
        dream.append(sentence)
        
    return dream

def print_slow(text, delay=0.05):
    """Print text with a drifting speed."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        # Randomize delay slightly for organic feel
        time.sleep(delay + random.uniform(-0.02, 0.02))
    print()

def main():
    print()
    print("  ENTERING REM STATE...")
    print()
    time.sleep(2)
    
    phrases = collect_corpus()
    
    if not phrases:
        print("  (The mind is empty.)")
        return

    print(f"  (Absorbed {len(phrases)} fragments of memory)")
    print()
    time.sleep(1)
    
    try:
        while True:
            # Generate a stanza
            stanza = dream_sequence(phrases, length=random.randint(3, 6))
            
            for line in stanza:
                print("  " + line)
                # Pause between lines
                time.sleep(random.uniform(1.0, 2.5))
            
            print()
            # Pause between stanzas
            time.sleep(random.uniform(2.0, 4.0))
            
            # Chance to wake up? No, loop forever until interrupted.
            
    except KeyboardInterrupt:
        print()
        print("  (waking up)")
        print()

if __name__ == "__main__":
    main()
