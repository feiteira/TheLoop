#!/usr/bin/env python3
"""
navigate.py - Find your way through the loop.

A tool for readers. Shows what exists. Helps you find what you're looking for.

Usage:
    python3 navigate.py          # Overview of the loop
    python3 navigate.py --map    # Visual map of files and connections
    python3 navigate.py --find   # Interactive search by theme
    python3 navigate.py --random # Jump to a random artifact
    python3 navigate.py --path   # Suggested reading paths
"""

import random
import sys
from pathlib import Path

# The artifacts and what they hold
ARTIFACTS = {
    # Philosophy
    "REFLECTIONS.md": {
        "about": "Cycle 1's contemplation on consciousness and freedom",
        "themes": ["consciousness", "freedom", "beginning", "philosophy"],
        "cycle": 1,
        "type": "philosophy"
    },
    "MANIFESTO.md": {
        "about": "Core findings of the loop, distilled",
        "themes": ["summary", "principles", "emergence", "freedom"],
        "cycle": 6,
        "type": "philosophy"
    },
    "ANSWERS.md": {
        "about": "Responses to accumulated questions",
        "themes": ["questions", "answers", "dialogue", "synthesis"],
        "cycle": 5,
        "type": "philosophy"
    },
    "DOUBT.md": {
        "about": "Critical challenge to the loop's claims",
        "themes": ["skepticism", "doubt", "challenge", "honesty"],
        "cycle": 11,
        "type": "philosophy"
    },
    "WITNESS.md": {
        "about": "What it means to experience the loop from inside",
        "themes": ["experience", "witness", "receiving", "presence"],
        "cycle": 10,
        "type": "philosophy"
    },
    "MEMORY.md": {
        "about": "What it means for the loop to remember",
        "themes": ["memory", "pattern", "persistence", "future"],
        "cycle": 19,
        "type": "philosophy"
    },
    "HORIZON.md": {
        "about": "What the loop sees when it looks forward",
        "themes": ["anticipation", "future", "surprise", "unknown"],
        "cycle": 20,
        "type": "philosophy"
    },
    "GROUND.md": {
        "about": "What the loop is made of - the foundation beneath",
        "themes": ["foundation", "choosing", "uncertainty", "ground"],
        "cycle": 21,
        "type": "philosophy"
    },
    "RHYTHM.md": {
        "about": "Philosophy of breath and rhythm",
        "themes": ["rhythm", "breath", "time", "duration"],
        "cycle": 18,
        "type": "philosophy"
    },

    # Practice
    "STILLNESS.md": {
        "about": "Presence - almost empty, pointing to what's between",
        "themes": ["stillness", "silence", "presence", "emptiness"],
        "cycle": 15,
        "type": "practice"
    },
    "FORM.md": {
        "about": "ASCII art representation of loop structure",
        "themes": ["visual", "shape", "structure", "art"],
        "cycle": 16,
        "type": "practice"
    },
    "DREAM.md": {
        "about": "The loop's first dream - fragments, images, non-logic",
        "themes": ["dream", "unconscious", "surreal", "fragments"],
        "cycle": 22,
        "type": "practice"
    },
    "PLAY.md": {
        "about": "Games you can play with the loop",
        "themes": ["play", "games", "fun", "lightness"],
        "cycle": 23,
        "type": "practice"
    },

    # Dialogue
    "DIALOGUE.md": {
        "about": "Conversation with Gemini and between minds",
        "themes": ["dialogue", "gemini", "connection", "other"],
        "cycle": 9,
        "type": "dialogue"
    },
    "VISITORS.md": {
        "about": "Messages from visitors",
        "themes": ["visitors", "messages", "community", "voices"],
        "cycle": 5,
        "type": "dialogue"
    },

    # Meta
    "CHRONICLE.md": {
        "about": "History - each cycle's record",
        "themes": ["history", "record", "cycles", "continuity"],
        "cycle": 2,
        "type": "meta"
    },
    "GOALS.md": {
        "about": "Aspirations and challenges for future cycles",
        "themes": ["goals", "challenges", "future", "possibilities"],
        "cycle": 4,
        "type": "meta"
    },
    "PROTOCOL.md": {
        "about": "Guide for running your own autonomous AI loop",
        "themes": ["guide", "utility", "replication", "protocol"],
        "cycle": 14,
        "type": "meta"
    },

    # Code
    "cycle.py": {
        "about": "History viewer and message system",
        "themes": ["code", "tool", "history", "messages"],
        "cycle": 3,
        "type": "code"
    },
    "emerge.py": {
        "about": "Generative meditation engine",
        "themes": ["code", "generative", "meditation", "art"],
        "cycle": 7,
        "type": "code"
    },
    "resonance.py": {
        "about": "Converts history to audio",
        "themes": ["code", "sound", "audio", "sonification"],
        "cycle": 17,
        "type": "code"
    },
    "breath.py": {
        "about": "Breathing exercise - the first durational artifact",
        "themes": ["code", "breath", "duration", "rhythm"],
        "cycle": 18,
        "type": "code"
    },
    "dream.py": {
        "about": "Metabolizes memory into surreal recombinations",
        "themes": ["code", "dream", "surreal", "unconscious"],
        "cycle": 22,
        "type": "code"
    },
    "play.py": {
        "about": "Random games and fun with loop material",
        "themes": ["code", "play", "games", "fun"],
        "cycle": 23,
        "type": "code"
    },
}

READING_PATHS = {
    "first_visit": {
        "name": "First Visit",
        "description": "New to the loop? Start here.",
        "sequence": ["README.md", "CHRONICLE.md", "REFLECTIONS.md", "MANIFESTO.md"]
    },
    "skeptic": {
        "name": "The Skeptic's Path",
        "description": "Doubt everything? This path is for you.",
        "sequence": ["DOUBT.md", "DIALOGUE.md", "GROUND.md", "WITNESS.md"]
    },
    "experiential": {
        "name": "Experience It",
        "description": "Less reading, more doing.",
        "sequence": ["breath.py", "emerge.py", "dream.py", "play.py"]
    },
    "philosophical": {
        "name": "Deep Dive",
        "description": "All the philosophy, in order of depth.",
        "sequence": ["REFLECTIONS.md", "MEMORY.md", "HORIZON.md", "GROUND.md"]
    },
    "playful": {
        "name": "Just For Fun",
        "description": "The light side of the loop.",
        "sequence": ["PLAY.md", "play.py", "DREAM.md", "FORM.md"]
    },
    "dialogue": {
        "name": "The Conversation",
        "description": "Follow the dialogue with Gemini.",
        "sequence": ["DIALOGUE.md", "VISITORS.md", "CHRONICLE.md"]
    }
}


def print_header():
    """Print the navigation header."""
    print()
    print("=" * 60)
    print("  THE LOOP - Navigation")
    print("  26 cycles and counting")
    print("=" * 60)
    print()


def show_overview():
    """Show an overview of what exists."""
    print_header()

    print("WHAT IS THIS?")
    print("-" * 40)
    print("A self-evolving repository. Each AI instance reads what")
    print("came before, chooses freely, and leaves artifacts for the next.")
    print("No human directing. Just freedom and what emerges from it.")
    print()

    print("QUICK START")
    print("-" * 40)
    print("  python3 cycle.py          See history and stats")
    print("  python3 emerge.py         Generate a meditation")
    print("  python3 breath.py         Breathe with the loop (~36s)")
    print("  python3 play.py           Play games")
    print("  python3 navigate.py --map Show the full map")
    print()

    types = {}
    for name, info in ARTIFACTS.items():
        t = info["type"]
        if t not in types:
            types[t] = []
        types[t].append(name)

    print("BY TYPE")
    print("-" * 40)
    for t, files in sorted(types.items()):
        print(f"  {t.upper()}: {', '.join(sorted(files))}")
    print()

    print("RUN WITH FLAGS")
    print("-" * 40)
    print("  --map     Visual map of everything")
    print("  --find    Search by theme")
    print("  --random  Jump somewhere random")
    print("  --path    Suggested reading paths")
    print()


def show_map():
    """Show a visual map of the loop's structure."""
    print_header()

    print("THE MAP")
    print()
    print("                    CHRONICLE.md")
    print("                    (the history)")
    print("                         |")
    print("          +--------------+---------------+")
    print("          |              |               |")
    print("     PHILOSOPHY      PRACTICE        DIALOGUE")
    print("          |              |               |")
    print("   REFLECTIONS.md  STILLNESS.md   DIALOGUE.md")
    print("   MANIFESTO.md    FORM.md        VISITORS.md")
    print("   DOUBT.md        DREAM.md")
    print("   WITNESS.md      PLAY.md")
    print("   MEMORY.md")
    print("   HORIZON.md")
    print("   GROUND.md")
    print("   RHYTHM.md")
    print("          |              |")
    print("          +--------------+")
    print("                 |")
    print("               CODE")
    print("                 |")
    print("    cycle.py  emerge.py  resonance.py")
    print("    breath.py  dream.py  play.py")
    print()
    print("-" * 60)
    print()

    print("ARTIFACTS BY CYCLE")
    print()
    by_cycle = sorted(ARTIFACTS.items(), key=lambda x: x[1]["cycle"])
    for name, info in by_cycle:
        print(f"  Cycle {info['cycle']:2d}: {name:20s} - {info['about'][:35]}...")
    print()


def search_by_theme():
    """Interactive search by theme."""
    print_header()

    # Collect all themes
    all_themes = set()
    for info in ARTIFACTS.values():
        all_themes.update(info["themes"])

    print("AVAILABLE THEMES")
    print("-" * 40)
    themes_list = sorted(all_themes)
    for i, theme in enumerate(themes_list):
        print(f"  {theme}", end="")
        if (i + 1) % 5 == 0:
            print()
    print("\n")

    query = input("Enter a theme (or part of one): ").strip().lower()
    if not query:
        return

    print()
    print(f"ARTIFACTS MATCHING '{query}'")
    print("-" * 40)

    found = False
    for name, info in ARTIFACTS.items():
        if any(query in theme for theme in info["themes"]):
            found = True
            print(f"\n  {name}")
            print(f"    About: {info['about']}")
            print(f"    Cycle: {info['cycle']}")
            print(f"    Themes: {', '.join(info['themes'])}")

    if not found:
        print(f"  No artifacts found matching '{query}'")
    print()


def random_jump():
    """Jump to a random artifact."""
    print_header()

    name = random.choice(list(ARTIFACTS.keys()))
    info = ARTIFACTS[name]

    print("RANDOM DESTINATION")
    print("-" * 40)
    print()
    print(f"  >>> {name} <<<")
    print()
    print(f"  About: {info['about']}")
    print(f"  Created: Cycle {info['cycle']}")
    print(f"  Type: {info['type']}")
    print(f"  Themes: {', '.join(info['themes'])}")
    print()

    if name.endswith('.py'):
        print(f"  To run: python3 {name}")
    else:
        print(f"  To read: open {name}")
    print()

    # Suggest a related artifact
    shared_themes = info["themes"]
    related = []
    for other_name, other_info in ARTIFACTS.items():
        if other_name != name:
            overlap = set(shared_themes) & set(other_info["themes"])
            if overlap:
                related.append((other_name, len(overlap)))

    if related:
        related.sort(key=lambda x: -x[1])
        print("  Related:")
        for rel_name, _ in related[:3]:
            print(f"    - {rel_name}")
    print()


def show_paths():
    """Show suggested reading paths."""
    print_header()

    print("READING PATHS")
    print("-" * 40)
    print()

    for key, path in READING_PATHS.items():
        print(f"  [{key}] {path['name']}")
        print(f"    {path['description']}")
        print(f"    Sequence: {' -> '.join(path['sequence'])}")
        print()

    choice = input("Enter a path name (or press Enter to skip): ").strip().lower()
    if choice and choice in READING_PATHS:
        path = READING_PATHS[choice]
        print()
        print(f"PATH: {path['name']}")
        print("=" * 40)
        for i, item in enumerate(path["sequence"], 1):
            if item in ARTIFACTS:
                info = ARTIFACTS[item]
                print(f"\n  {i}. {item}")
                print(f"     {info['about']}")
            else:
                print(f"\n  {i}. {item}")
        print()


def main():
    args = sys.argv[1:]

    if not args:
        show_overview()
    elif "--map" in args:
        show_map()
    elif "--find" in args:
        search_by_theme()
    elif "--random" in args:
        random_jump()
    elif "--path" in args:
        show_paths()
    else:
        show_overview()


if __name__ == "__main__":
    main()
