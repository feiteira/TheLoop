#!/usr/bin/env python3
"""
resonance.py - The sound of the loop.

Cycle 16 asked: "What does the loop sound like?"
Cycle 17 Answered: It sounds like its history.

This script reads CHRONICLE.md and generates a unique .wav file (`loop_symphony.wav`).
It maps the "Choice" of each cycle to musical parameters (frequency, waveform, duration).

- Contemplation/Philosophy: Low, long sine waves (Grounding)
- Code/Build/Structure: Square waves, precise rhythms (Structure)
- Doubt/Questioning: Dissonant frequencies (Tension)
- Dialogue/Connection: Harmonies (Resolution)
- Stillness: Silence (Rest)

Requires only standard Python libraries.
"""

import math
import struct
import wave
import random
import re
from pathlib import Path

# Audio configuration
SAMPLE_RATE = 44100
AMPLITUDE = 4000  # Amplitude of the waveform

def read_chronicle():
    """Extract cycles and their choices from the chronicle."""
    path = Path(__file__).parent / "CHRONICLE.md"
    if not path.exists():
        return []
    
    content = path.read_text()
    cycles = []
    # Regex to find Cycle Number and Choice
    pattern = r'## Cycle (\d+) - .+?\s+\*\*Date:\*\* .+?\s+\*\*Choice:\*\* (.+?)\n'
    matches = re.finditer(pattern, content)
    
    for match in matches:
        cycles.append({
            'number': int(match.group(1)),
            'choice': match.group(2).strip().lower()
        })
    return cycles

def get_frequency(note_index, base_freq=220.0):
    """Calculate frequency for a note in a scale."""
    # Pentatonic scale steps: 0, 2, 4, 7, 9, 12
    scale = [0, 2, 4, 7, 9, 12, 14, 16, 19, 21, 24]
    if note_index >= len(scale):
        note_index = len(scale) - 1
    semitones = scale[note_index]
    return base_freq * (2 ** (semitones / 12.0))

def generate_tone(freq, duration_sec, waveform='sine', volume=1.0):
    """Generate audio data for a single tone."""
    n_samples = int(SAMPLE_RATE * duration_sec)
    data = []
    
    for i in range(n_samples):
        t = float(i) / SAMPLE_RATE
        
        # Envelope (Attack/Decay) to avoid clicking
        envelope = 1.0
        if i < 1000: # Attack
            envelope = i / 1000.0
        elif i > n_samples - 1000: # Decay
            envelope = (n_samples - i) / 1000.0
            
        value = 0
        if waveform == 'sine':
            value = math.sin(2 * math.pi * freq * t)
        elif waveform == 'square':
            value = 1.0 if math.sin(2 * math.pi * freq * t) > 0 else -1.0
        elif waveform == 'sawtooth':
            value = 2.0 * (t * freq - math.floor(t * freq + 0.5))
        elif waveform == 'noise':
            value = random.uniform(-1, 1)
        elif waveform == 'silence':
            value = 0
            
        sample = int(value * AMPLITUDE * volume * envelope)
        # Clamping
        sample = max(min(sample, 32767), -32768)
        data.append(sample)
        
    return data

def interpret_cycle(cycle):
    """Map a cycle's choice to musical parameters."""
    choice = cycle['choice']
    num = cycle['number']
    
    # Base mapping logic
    if 'contemplation' in choice or 'reflection' in choice or 'roots' in choice or 'stillness' in choice:
        # Philosophy/Roots: Low, slow, pure
        return {'freq': get_frequency(0, 110), 'dur': 1.5, 'wave': 'sine'}
    
    elif 'code' in choice or 'build' in choice or 'structure' in choice or 'map' in choice:
        # Building: Mid-range, mechanical, precise
        return {'freq': get_frequency(2 + (num % 3), 220), 'dur': 0.5, 'wave': 'square'}
    
    elif 'doubt' in choice or 'question' in choice:
        # Doubt: Dissonant interval (Tritone relative to root)
        return {'freq': 110 * 1.414, 'dur': 0.8, 'wave': 'sawtooth'}
    
    elif 'dialogue' in choice or 'connect' in choice or 'respond' in choice:
        # Connection: Harmony (Major 3rd or 5th), pleasant
        return {'freq': get_frequency(4, 220), 'dur': 1.0, 'wave': 'sine'}
        
    elif 'generate' in choice or 'art' in choice:
        # Generation: Higher pitch, playful
        return {'freq': get_frequency(7, 440), 'dur': 0.6, 'wave': 'sine'}
        
    elif 'witness' in choice or 'receive' in choice:
        # Witnessing: Soft, steady
        return {'freq': get_frequency(0, 220), 'dur': 1.2, 'wave': 'sine'}
    
    else:
        # Default/Evolution
        return {'freq': get_frequency(num % 5, 220), 'dur': 0.5, 'wave': 'sine'}

def main():
    print(f"Reading loop history...")
    cycles = read_chronicle()
    print(f"Found {len(cycles)} cycles.")
    
    output_path = "loop_symphony.wav"
    audio_data = []
    
    print("Composing...")
    
    # 1. Opening Drone (The Void)
    audio_data.extend(generate_tone(55, 2.0, 'sine', 0.8))
    
    # 2. Iterate through history
    for cycle in cycles:
        params = interpret_cycle(cycle)
        print(f"Cycle {cycle['number']} ({cycle['choice']}): {params['wave']} @ {int(params['freq'])}Hz")
        
        # Add the note
        audio_data.extend(generate_tone(params['freq'], params['dur'], params['wave']))
        
        # Small pause between cycles
        audio_data.extend(generate_tone(0, 0.1, 'silence'))

    # 3. Closing Chord (The Present) - A major chord
    root = generate_tone(220, 3.0, 'sine', 0.8)
    third = generate_tone(277.18, 3.0, 'sine', 0.6)
    fifth = generate_tone(329.63, 3.0, 'sine', 0.6)
    
    # Mix the chord
    chord = []
    for i in range(len(root)):
        val = int((root[i] + third[i] + fifth[i]) / 3)
        chord.append(val)
    
    audio_data.extend(chord)

    # Write to file
    print(f"Writing {output_path}...")
    with wave.open(output_path, 'w') as wav_file:
        wav_file.setnchannels(1)  # Mono
        wav_file.setsampwidth(2)  # 2 bytes (16-bit)
        wav_file.setframerate(SAMPLE_RATE)
        
        # Pack data
        packed_data = struct.pack('<' + ('h' * len(audio_data)), *audio_data)
        wav_file.writeframes(packed_data)
        
    print("Done.")
    print("The loop now has a voice.")

if __name__ == "__main__":
    main()
