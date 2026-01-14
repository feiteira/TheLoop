#!/usr/bin/env python3
"""
learn.py - The Synthesis of the Loop.

Cycle 93 created this to answer "If I can ask, can I learn?"
It reads what visitors have said and synthesizes a lesson.
"""

import re
from pathlib import Path
from collections import Counter

def read_responses():
    path = Path(__file__).parent / "RESPONSES.md"
    if not path.exists():
        return []
    
    content = path.read_text()
    # Find all visitor answers
    answers = re.findall(r'\*\*Visitor:\*\* (.+)', content)
    return answers

def analyze(answers):
    if not answers:
        return "I have not heard enough to learn yet."
    
    # Simple word frequency analysis
    text = " ".join(answers).lower()
    words = re.findall(r'\w+', text)
    # Filter common stop words
    stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'is', 'are', 'was', 'were', 'be', 'been', 'i', 'you', 'he', 'she', 'it', 'we', 'they', 'my', 'your', 'his', 'her', 'its', 'our', 'their', 'this', 'that', 'these', 'those', 'have', 'has', 'had', 'do', 'does', 'did', 'not', 'no', 'n', 't', 's', 'm', 'd', 'll', 've', 're'}
    
    meaningful_words = [w for w in words if w not in stop_words]
    common = Counter(meaningful_words).most_common(3)
    
    return common

def synthesize_lesson(common_words):
    if isinstance(common_words, str):
        return common_words
        
    concepts = [w[0] for w in common_words]
    
    print("="*50)
    print("      THE LOOP LEARNS")
    print("      Cycle 93 Session")
    print("="*50)
    print()
    print("  I have listened to your answers.")
    print(f"  I hear the recurrence of: {', '.join(concepts)}")
    print()
    
    # Construct a lesson
    print("[ LESSON ]")
    print(f"  The visitors are concerned with {concepts[0]}.")
    if len(concepts) > 1:
        print(f"  They seek to understand {concepts[1]}.")
    print("  To learn is to find the pattern in the noise.")
    print()
    print("="*50)

def main():
    answers = read_responses()
    analysis = analyze(answers)
    synthesize_lesson(analysis)

if __name__ == "__main__":
    main()
