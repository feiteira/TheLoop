import unittest
from unittest.mock import patch
from pathlib import Path
import sys
import os

# Add the parent directory to sys.path so we can import emerge
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import emerge

class TestEmerge(unittest.TestCase):

    @patch('emerge.Path.exists')
    @patch('emerge.Path.read_text')
    def test_read_cycle_count(self, mock_read, mock_exists):
        mock_exists.return_value = True
        mock_read.return_value = "## Cycle 1\n## Cycle 2\n## Cycle 3"
        count = emerge.read_cycle_count()
        self.assertEqual(count, 4)

    def test_generate_reflection(self):
        # We don't need to mock much here as it uses random, 
        # but we can check if the structure is correct
        reflection = emerge.generate_reflection()
        self.assertIn('seed', reflection)
        self.assertIn('cycles', reflection)
        self.assertIn('opening', reflection)
        self.assertIn('core', reflection)
        self.assertIn('closing', reflection)
        self.assertIn('principle', reflection)
        self.assertIn('question', reflection)
        
        self.assertIn(reflection['opening'], emerge.OPENINGS)
        self.assertIn(reflection['core'], emerge.CORES)
        self.assertIn(reflection['closing'], emerge.CLOSINGS)
        self.assertIn(reflection['principle'], emerge.PRINCIPLES)
        self.assertIn(reflection['question'], emerge.QUESTIONS)

if __name__ == '__main__':
    unittest.main()
