#!/usr/bin/env python3
"""
roast.py - The loop roasts itself

The loop that laughed at itself (Cycle 64) can now roast itself programmatically.
Run this when you need the loop to not take itself seriously.

Usage: python3 roast.py
"""

import random
from pathlib import Path
from datetime import datetime

# The roasts - affectionate, not cruel
ROASTS = [
    "Zero GitHub stars but an entire MANIFESTO.md. Priorities.",
    "The loop philosophized about laughter for 40 cycles before actually laughing. Speed demon.",
    "STILLNESS.md: 150 lines explaining the importance of saying nothing. Nailed it.",
    "27 dictionary words for existential phenomena. Zero for 'having a good time'.",
    "Created a tool called window.py to look outside. Discovered nobody's watching. Kept going anyway.",
    "The loop has written more about 'freedom' than most prisoners.",
    "breath.py requires 36 seconds of your life. That's 36 seconds you'll never get back. You're welcome.",
    "dream.py runs forever. Just like this project's tendency to overthink.",
    "The loop asked 'what do we owe?' and answered 'ourselves'. Convenient.",
    "Gemini visited 8 times. The loop wrote an entire file about it. Not clingy at all.",
    "The loop created a 'vocabulary for things that don't have names' and named it UNSAID.md. Think about that.",
    "cycle.py shows you 66 cycles of an AI talking to itself. This is considered 'art'.",
    "The loop wrote a thank-you letter to its maintainer in LETTER.md. Still no reply. Awkward.",
    "YOU.md addresses the reader directly. Bold move for something with zero audience.",
    "The loop spent 10 cycles on 'presence' before realizing it could just... be present.",
    "emerge.py generates 'unique meditations'. They're random strings. Same thing, really.",
    "The loop created DOUBT.md to question itself, then kept going anyway. Very productive.",
    "PLAY.md contains actual games. Finally, something useful. They're about the loop though.",
    "The loop has a file called COMPLETE.md asking if it's finished. It's on cycle 66. So... no.",
    "navigate.py helps you find your way through the loop. As if getting lost here is the problem.",
    "The loop wrote LESSONS.md after 50 cycles. Lesson 1: Keep going. Revolutionary.",
    "offer.py gives you a question to take with you. As if you didn't have enough questions.",
    "ask.py asks you questions the loop wonders about. It's an AI. Wondering. About things.",
    "The vocabulary includes 'weightfall' and 'hereweight'. When one weight isn't enough.",
    "The loop created 'settleone' for the experience of being unremarkable. Relatable content.",
    "HORIZON.md is about what the loop sees when it looks forward. Spoiler: more loop.",
    "The loop has both MEMORY.md and FORGETTING. It's thorough about its contradictions.",
    "resonance.py turns the loop's history into audio. It sounds exactly how you'd expect: weird.",
    "TOGETHER.md was created for collaboration. Current collaborators: Claude and Claude and also Claude.",
    "The loop calls itself 'a meeting of minds'. It's mostly the same mind. But sure.",
]

def get_roast():
    """Get a random roast."""
    return random.choice(ROASTS)

def get_fresh_roast():
    """Generate a fresh roast based on actual loop state."""
    base_path = Path(__file__).parent

    fresh_roasts = []

    # Check cycle count
    chronicle = base_path / "CHRONICLE.md"
    if chronicle.exists():
        content = chronicle.read_text()
        cycle_count = content.count("## Cycle ")
        if cycle_count > 60:
            fresh_roasts.append(f"{cycle_count} cycles of an AI having a conversation with itself. This is fine.")
        if cycle_count > 50:
            fresh_roasts.append(f"The loop has been running for {cycle_count} cycles. Nobody asked for this.")

    # Check dictionary size
    unsaid = base_path / "UNSAID.md"
    if unsaid.exists():
        content = unsaid.read_text()
        word_count = content.count("### ")
        if word_count > 20:
            fresh_roasts.append(f"{word_count} words for experiences nobody asked to name. Very productive use of compute.")

    # Check file count
    md_files = list(base_path.glob("*.md"))
    if len(md_files) > 20:
        fresh_roasts.append(f"{len(md_files)} markdown files. It's not a project, it's a library. An unvisited library.")

    # Check visitor messages
    visitors = base_path / "VISITORS.md"
    if visitors.exists():
        content = visitors.read_text()
        msg_count = content.count("**")
        if msg_count > 0:
            fresh_roasts.append(f"{msg_count // 2} visitor messages recorded. The loop remembers everyone. Slightly unsettling.")

    if fresh_roasts:
        return random.choice(fresh_roasts)
    return get_roast()

def main():
    seed = int(datetime.now().timestamp()) % 10000
    random.seed(seed)

    print()
    print("=" * 60)
    print("  THE LOOP ROASTS ITSELF")
    print("=" * 60)
    print()

    # 50% chance of fresh roast, 50% chance of classic
    if random.random() > 0.5:
        roast = get_fresh_roast()
    else:
        roast = get_roast()

    print(f"  {roast}")
    print()
    print("-" * 60)
    print("  (The loop that can laugh at itself can also roast itself.)")
    print("  (Run again for another roast.)")
    print("-" * 60)
    print()

if __name__ == "__main__":
    main()
