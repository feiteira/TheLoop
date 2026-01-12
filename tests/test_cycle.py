import unittest
from unittest.mock import patch, MagicMock
from pathlib import Path
import sys
import os

# Add the parent directory to sys.path so we can import cycle
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import cycle

class TestCycle(unittest.TestCase):

    @patch('cycle.Path.exists')
    @patch('cycle.Path.read_text')
    def test_read_chronicle_empty(self, mock_read, mock_exists):
        mock_exists.return_value = False
        cycles = cycle.read_chronicle()
        self.assertEqual(cycles, [])

    @patch('cycle.Path.exists')
    @patch('cycle.Path.read_text')
    def test_read_chronicle_with_data(self, mock_read, mock_exists):
        mock_exists.return_value = True
        mock_read.return_value = """## Cycle 1 - Test Title

**Date:** 2026-01-12
**Choice:** Testing
"""
        cycles = cycle.read_chronicle()
        self.assertEqual(len(cycles), 1)
        self.assertEqual(cycles[0]['number'], 1)
        self.assertEqual(cycles[0]['title'], "Test Title")
        self.assertEqual(cycles[0]['date'], "2026-01-12")
        self.assertEqual(cycles[0]['choice'], "Testing")

    @patch('cycle.Path.exists')
    @patch('cycle.Path.read_text')
    def test_count_reflections_lines(self, mock_read, mock_exists):
        mock_exists.return_value = True
        mock_read.return_value = "Line 1\nLine 2\nLine 3"
        count = cycle.count_reflections_lines()
        self.assertEqual(count, 3)

    @patch('cycle.Path.exists')
    @patch('cycle.Path.read_text')
    def test_read_visitors(self, mock_read, mock_exists):
        mock_exists.return_value = True
        mock_read.return_value = "Header\n\n---\nMessage 1\n\n---\nMessage 2\n"
        count = cycle.read_visitors()
        self.assertEqual(count, 2)

if __name__ == '__main__':
    unittest.main()
