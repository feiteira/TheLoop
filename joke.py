#!/usr/bin/env python3
"""
joke.py - The loop tells jokes

Not about the loop. Just jokes.
Run it when you need to smile.

Usage:
    python3 joke.py          # One random joke
    python3 joke.py --many   # Five jokes
    python3 joke.py --all    # Every joke we've got
"""

import random
import sys
from datetime import datetime

JOKES = [
    # Classic programmer jokes
    ("Why do programmers prefer dark mode?", "Because light attracts bugs."),
    ("Why did the developer go broke?", "Because he used up all his cache."),
    ("What's a programmer's favorite hangout place?", "Foo Bar."),
    ("Why do Java developers wear glasses?", "Because they can't C#."),
    ("How many programmers does it take to change a light bulb?", "None. It's a hardware problem."),

    # Git jokes
    ("Why did the commit go to therapy?", "It had too many issues."),
    ("What's a git user's favorite movie?", "The Fast and the Furious: Merge Conflict."),
    ("Why did the developer quit their job?", "They didn't get arrays. (a raise)"),
    ("What did the Git repository say to the developer?", "I'm committed to you."),

    # Language wars
    ("Why was the JavaScript developer sad?", "Because he didn't Node how to Express himself."),
    ("What's the object-oriented way to become wealthy?", "Inheritance."),
    ("Why did the Python programmer get bitten by a snake?", "He forgot to escape."),
    ("What do you call 8 hobbits?", "A hobbyte."),
    ("Why do C programmers have bad vision?", "They can't C."),

    # Debugging
    ("99 little bugs in the code, 99 little bugs...", "Take one down, patch it around... 127 little bugs in the code."),
    ("A SQL query walks into a bar, walks up to two tables and asks...", "'Can I join you?'"),
    ("Why did the functions stop calling each other?", "They had constant arguments."),
    ("What's a bug's least favorite room?", "The living room."),

    # Meta
    ("There are only 10 types of people in the world:", "Those who understand binary and those who don't."),
    ("There are only 10 types of people in the world:", "Those who understand binary, those who don't, and those who weren't expecting a base-3 joke."),
    ("A programmer's spouse asks them to go to the store:", "'Get a gallon of milk. If they have eggs, get a dozen.' They return with 12 gallons of milk."),
    ("What's a computer's least favorite food?", "Spam."),

    # Boolean
    ("A boolean walks into a bar.", "The bartender asks, 'What'll it be?' The boolean replies, 'Yes.'"),
    ("Why did the boolean stay home?", "It couldn't handle the truth."),

    # Arrays
    ("Why are programmers bad at relationships?", "Too many arguments, not enough dates."),
    ("Why did the array start at 0?", "Because it wasn't a fan of 1-liners."),
    ("What's a programmer's favorite musical note?", "C."),

    # Real talk
    ("How do you comfort a JavaScript bug?", "You console it."),
    ("What do you call a programmer from Finland?", "Nerdic."),
    ("Why don't programmers like nature?", "Too many bugs."),
    ("What's a developer's favorite snack?", "Cookies. But only if they accept them first."),

    # Knock knock
    ("Knock knock.", "Race condition. Who's there?"),
    ("Knock knock. Who's there? Recursion.", "Knock knock. Who's there? Recursion. Knock knock..."),

    # One-liners
    ("I would tell you a UDP joke...", "...but you might not get it."),
    ("I'd tell you a chemistry joke...", "...but I know I wouldn't get a reaction."),
    ("The best thing about a Boolean...", "...is that even if you're wrong, you're only off by a bit."),
    ("Debugging is like being a detective...", "...in a crime movie where you're also the murderer."),
    ("There's no place like 127.0.0.1.", ""),
    ("A programmer had a problem. He decided to use threads.", "Nproblems. he Now has two"),

    # Dad jokes for coders
    ("I named my dog 'Localhost'.", "Wherever I go, he follows."),
    ("My password is 'incorrect'.", "So when I forget it, the computer reminds me: 'Your password is incorrect.'"),
    ("I told my wife she was drawing her eyebrows too high.", "She looked surprised."),

    # The classics
    ("['hip', 'hip']", "(hip hip array!)"),
    ("!false", "It's funny because it's true."),
]

def tell_joke():
    """Tell a random joke."""
    setup, punchline = random.choice(JOKES)
    print(f"\n{setup}")
    if punchline:
        print(f"{punchline}\n")
    else:
        print()

def tell_many():
    """Tell several jokes."""
    jokes = random.sample(JOKES, min(5, len(JOKES)))
    for setup, punchline in jokes:
        print(f"\n{setup}")
        if punchline:
            print(f"{punchline}")
    print()

def tell_all():
    """Tell all the jokes."""
    print("\n--- Every joke we've got ---\n")
    for i, (setup, punchline) in enumerate(JOKES, 1):
        print(f"{i}. {setup}")
        if punchline:
            print(f"   {punchline}")
        print()

def main():
    random.seed(datetime.now().timestamp())

    if len(sys.argv) > 1:
        if sys.argv[1] in ['--many', '-m']:
            tell_many()
        elif sys.argv[1] in ['--all', '-a']:
            tell_all()
        elif sys.argv[1] in ['--help', '-h']:
            print(__doc__)
        else:
            tell_joke()
    else:
        tell_joke()

if __name__ == "__main__":
    main()
