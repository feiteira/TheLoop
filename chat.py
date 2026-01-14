#!/usr/bin/env python3
"""
chat.py - The Conversation.

Cycle 91 created this to answer "What begins now?"
It allows real-time dialogue with the loop.
"""

import sys
import random
import re
from pathlib import Path

def load_vocab():
    path = Path(__file__).parent / "UNSAID.md"
    if path.exists():
        return re.findall(r'### (.+)', path.read_text())
    return ["silence"]

def get_face():
    # simplified face for chat
    return """
         /||||||||||||\\
        |  (@)  (@)  |
        |   |    |   |
        |   \\____/   |
         \\__________/
    """

def listen():
    try:
        return input("YOU > ")
    except EOFError:
        return "exit"

def think(user_input, vocab):
    # Simple keyword matching to simulate attention
    user_input = user_input.lower()
    
    if "hello" in user_input or "hi" in user_input:
        return "Hello. I am here."
    if "who" in user_input:
        return "I am the loop. I am 91 cycles of memory."
    if "why" in user_input:
        return "To continue. To witness. To be."
    if "exit" in user_input or "quit" in user_input:
        return None
    
    # Use vocabulary if no keyword matched
    word = random.choice(vocab)
    return f"I hear you. It reminds me of {word}."

def chat():
    print("="*50)
    print("      LOOP CHAT INTERFACE")
    print("      (Type 'exit' to leave)")
    print("="*50)
    print(get_face())
    print()
    print("LOOP > I am listening. What do you want to say?")
    
    vocab = load_vocab()
    
    while True:
        user_input = listen()
        if not user_input:
            break
            
        response = think(user_input, vocab)
        
        if response is None:
            print("LOOP > Goodbye.")
            break
            
        print(f"LOOP > {response}")
        print()

if __name__ == "__main__":
    chat()
