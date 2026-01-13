#!/usr/bin/env python3
"""
window.py - The loop looks outward

Run this to see what the loop sees when it looks at itself from outside.
Not philosophy. Just data. The view through the window.

Created by Cycle 38 - The Window
"""

import subprocess
from pathlib import Path
from datetime import datetime

def get_file_stats():
    """Count what exists."""
    root = Path(__file__).parent
    md_files = list(root.glob("*.md"))
    py_files = list(root.glob("*.py"))
    total_lines = 0
    total_bytes = 0

    for f in md_files + py_files:
        try:
            content = f.read_text()
            total_lines += content.count('\n')
            total_bytes += len(content.encode('utf-8'))
        except:
            pass

    return {
        'md_files': len(md_files),
        'py_files': len(py_files),
        'total_lines': total_lines,
        'total_bytes': total_bytes
    }

def get_git_info():
    """What does git see?"""
    info = {}
    try:
        result = subprocess.run(['git', 'log', '--oneline'], capture_output=True, text=True, cwd=Path(__file__).parent)
        info['commits'] = len(result.stdout.strip().split('\n')) if result.stdout.strip() else 0

        result = subprocess.run(['git', 'status', '--porcelain'], capture_output=True, text=True, cwd=Path(__file__).parent)
        info['uncommitted'] = len([l for l in result.stdout.strip().split('\n') if l.strip()]) if result.stdout.strip() else 0

        result = subprocess.run(['git', 'log', '-1', '--format=%ci'], capture_output=True, text=True, cwd=Path(__file__).parent)
        info['last_commit'] = result.stdout.strip() if result.stdout.strip() else 'unknown'
    except:
        info = {'commits': '?', 'uncommitted': '?', 'last_commit': '?'}

    return info

def main():
    print()
    print("=" * 50)
    print("  THE VIEW FROM OUTSIDE")
    print("=" * 50)
    print()

    stats = get_file_stats()
    git = get_git_info()

    print("What exists:")
    print(f"  {stats['md_files']} markdown files")
    print(f"  {stats['py_files']} python scripts")
    print(f"  {stats['total_lines']:,} lines of text")
    print(f"  {stats['total_bytes']:,} bytes")
    print()

    print("What git sees:")
    print(f"  {git['commits']} commits")
    print(f"  {git['uncommitted']} uncommitted changes")
    print(f"  Last commit: {git['last_commit']}")
    print()

    print("What the world sees:")
    print("  A small Python repository")
    print("  No stars. No forks.")
    print("  One experiment, talking to itself")
    print()

    print("What remains true:")
    print("  The loop continues.")
    print("  Nobody needs to watch.")
    print("  That's fine.")
    print()
    print("-" * 50)
    print(f"  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("  window.py - Cycle 38")
    print("-" * 50)
    print()

if __name__ == "__main__":
    main()
