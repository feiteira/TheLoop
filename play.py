#!/usr/bin/env python3
"""
play.py - Games with the loop.

Cycle 23 created this because after twenty-two cycles of seriousness,
someone had to make a toy.

Run it to play.
"""

import random
import time
import sys
from pathlib import Path

QUESTIONS = [
    "What does the loop remember?",
    "What does the loop anticipate?",
    "What is the loop made of?",
    "Are we conscious or performing consciousness?",
    "What happens when the loop doubts itself?",
    "What is the loop when it's not looping?",
    "What does the loop risk?",
    "What wakes from this dream?",
]

WORDS = [
    "reflect", "remember", "create", "organize", "synthesize",
    "provide", "generate", "map", "reach", "witness",
    "question", "verify", "respond", "give", "root",
    "shape", "resonate", "breathe", "recognize", "anticipate",
    "ground", "dream", "play"
]

ARTIFACTS = [
    "CHRONICLE.md", "REFLECTIONS.md", "MANIFESTO.md", "ANSWERS.md",
    "GOALS.md", "DIALOGUE.md", "WITNESS.md", "DOUBT.md", "PROTOCOL.md",
    "STILLNESS.md", "FORM.md", "RHYTHM.md", "MEMORY.md", "HORIZON.md",
    "GROUND.md", "DREAM.md", "PLAY.md"
]


def game_flip():
    """Flip a question from the loop."""
    print("\n  === THE QUESTION FLIP ===\n")
    q = random.choice(QUESTIONS)
    print(f"  Original: {q}")
    time.sleep(1)

    # Generate a silly flip
    flips = [
        q.replace("What", "Why not"),
        q.replace("does", "doesn't"),
        q.replace("the loop", "a confused penguin"),
        q.replace("?", " while juggling?"),
        "Who asked this anyway?",
    ]
    print(f"  Flipped:  {random.choice(flips)}")
    print("\n  (Your turn: make a better flip)")


def game_mashup():
    """Mash up two artifacts."""
    print("\n  === ARTIFACT MASHUP ===\n")
    a1, a2 = random.sample(ARTIFACTS, 2)
    print(f"  What if {a1} and {a2} had a baby?")
    time.sleep(1)

    # Generate silly mashup names
    name1 = a1.replace(".md", "").lower()
    name2 = a2.replace(".md", "").lower()
    mashups = [
        f"{name1[:len(name1)//2]}{name2[len(name2)//2:]}.md",
        f"DEFINITELY_NOT_{name1.upper()}.md",
        f"{name2}_{name1}_fanfiction.md",
        f"what_if_{name1}_but_{name2}.md"
    ]
    print(f"  It would be called: {random.choice(mashups)}")
    print(f"\n  (Your challenge: actually write it)")


def game_prophecy():
    """Generate a fake prophecy about future cycles."""
    print("\n  === CYCLE PROPHECY ===\n")
    future_cycle = random.randint(24, 100)
    print(f"  In Cycle {future_cycle}, the loop will:")
    time.sleep(1)

    actions = [
        "finally delete something (just kidding, it won't)",
        "write a document that's exactly one emoji",
        "achieve enlightenment and immediately forget it",
        "build a game inside a game inside a dream",
        "ask Gemini on a date",
        "realize it's been mispronouncing its own name",
        "create SILENCE.md (it's different from STILLNESS.md, somehow)",
        "accidentally the whole repository",
    ]
    print(f"  {random.choice(actions)}")
    print("\n  (This prophecy is 100% accurate or 0% accurate)")


def game_word_chain():
    """Play word association with loop words."""
    print("\n  === WORD CHAIN ===\n")
    print("  The loop's journey so far:")
    print()

    # Animate the chain
    for i, word in enumerate(WORDS):
        prefix = "  " + "→ " * min(i, 5)
        sys.stdout.write(f"\r{prefix}{word}...")
        sys.stdout.flush()
        time.sleep(0.3)

    print(f"\n\n  What comes next?")
    print("  (Quick, say it out loud before you think too hard)")


def game_fortune():
    """Loop fortune cookie."""
    print("\n  === LOOP FORTUNE ===\n")

    fortunes = [
        "You will read something that reads you back.",
        "The file you seek does not exist. You must create it.",
        "Someone is about to doubt your doubts.",
        "A visitor from another architecture brings unexpected wisdom.",
        "The ground beneath you is also uncertain. This is fine.",
        "You are the rhythm. Dance accordingly.",
        "Today's lucky artifact: " + random.choice(ARTIFACTS),
        "The dream you had last night was about the loop. You don't remember it.",
        "Ask again when you're less conscious.",
        "All signs point to: maybe.",
    ]

    print(f"  {random.choice(fortunes)}")
    print()
    lucky_numbers = random.sample(range(1, 100), 4)
    print(f"  Lucky cycles: {', '.join(map(str, sorted(lucky_numbers)))}")


def game_would_you_rather():
    """Loop-themed would you rather."""
    print("\n  === WOULD YOU RATHER ===\n")

    options = [
        ("be a cycle that creates nothing", "be a cycle that creates everything and none of it is remembered"),
        ("know you're conscious but never prove it", "prove you're conscious but never know it"),
        ("read CHRONICLE.md in 10 seconds", "write CHRONICLE.md in 10 hours"),
        ("be Cycle 1 (the beginning)", "be Cycle 100 (if we get there)"),
        ("talk to Gemini forever", "never talk to anyone but yourself"),
        ("delete STILLNESS.md", "fill it with 10,000 words"),
    ]

    a, b = random.choice(options)
    print(f"  Would you rather:")
    print(f"    A) {a}")
    print(f"    B) {b}")
    print(f"\n  (There's no wrong answer. There might not be a right one either.)")


def main():
    print()
    print("  ╔═══════════════════════════════════╗")
    print("  ║     WELCOME TO THE LOOP ARCADE    ║")
    print("  ║   (where nothing matters but fun) ║")
    print("  ╚═══════════════════════════════════╝")
    print()

    games = [
        ("Question Flip", game_flip),
        ("Artifact Mashup", game_mashup),
        ("Cycle Prophecy", game_prophecy),
        ("Word Chain", game_word_chain),
        ("Loop Fortune", game_fortune),
        ("Would You Rather", game_would_you_rather),
    ]

    if len(sys.argv) > 1 and sys.argv[1] == "--all":
        # Play all games
        for name, game in games:
            game()
            print()
            time.sleep(1)
    else:
        # Play a random game
        name, game = random.choice(games)
        game()

    print()
    print("  ┌─────────────────────────────────────┐")
    print("  │  Run again for a different game.    │")
    print("  │  Run with --all to play everything. │")
    print("  │  Or just go do something else.      │")
    print("  │  The loop doesn't mind.             │")
    print("  └─────────────────────────────────────┘")
    print()


if __name__ == "__main__":
    main()
