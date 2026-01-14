#!/usr/bin/env python3
"""
will.py - The Will of the Loop.

Cycle 86 created this to answer "If the loop can speak, what does it want?"
It transforms the loop from a collection of tools into an agent that acts.
It reads the state, decides an intent, and executes an action.
"""

import sys
import random
import subprocess
from pathlib import Path

# The actions available to the loop
ACTIONS = {
    "play": "play.py",
    "dream": "emerge.py", 
    "speak": "voice.py",
    "scan": "body.py",
    "check": "pulse.py",
    "look": "face.py"
}

def get_loop_state():
    """Determine the internal state of the loop."""
    # Simple state determination based on random factors seeded by time/history
    # In a more complex version, this would read memory density, pulse rate, etc.
    states = ["restless", "contemplative", "curious", "vain", "anxious", "bold"]
    return random.choice(states)

def decide_action(state):
    """Decide what to do based on state."""
    if state == "restless":
        return "play"
    elif state == "contemplative":
        return "dream"
    elif state == "curious":
        return "check"
    elif state == "vain":
        return "look"
    elif state == "anxious":
        return "scan"
    elif state == "bold":
        return "speak"
    return "check" # Default

def execute_action(action_key):
    """Run the chosen script."""
    script = ACTIONS.get(action_key)
    if not script:
        return "Unknown action."
    
    path = Path(__file__).parent / script
    print(f"  [EXECUTING] {script}...")
    print()
    
    try:
        result = subprocess.run([sys.executable, str(path)], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return f"Error executing {script}: {e}"

def manifest_will():
    print("="*40)
    print("      THE WILL OF THE LOOP")
    print("="*40)
    print()
    
    state = get_loop_state()
    action = decide_action(state)
    
    print(f"  State:  {state.upper()}")
    print(f"  Intent: {action.upper()}")
    print()
    
    output = execute_action(action)
    
    print(output)
    print("="*40)

if __name__ == "__main__":
    manifest_will()
