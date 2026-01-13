import unittest
from unittest.mock import patch, MagicMock
from pathlib import Path
import sys
import os

# Add the parent directory to sys.path so we can import dream
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import dream

class TestDream(unittest.TestCase):

    def test_clean_text(self):
        raw = "# Header\nSome **bold** text and `code`."
        cleaned = dream.clean_text(raw)
        self.assertNotIn('#', cleaned)
        self.assertNotIn('**', cleaned)
        self.assertNotIn('`', cleaned)
        self.assertIn('Some bold text', cleaned)

    def test_extract_phrases(self):
        text = "Hello world. This is a test; it works."
        phrases = dream.extract_phrases(text)
        self.assertIn("Hello world", phrases)
        self.assertIn("This is a test", phrases)
        self.assertIn("it works", phrases)

    @patch('dream.get_markdown_files')
    @patch('dream.Path.read_text')
    def test_collect_corpus(self, mock_read, mock_get_files):
        # Mock a file
        mock_file = MagicMock()
        mock_file.name = "test.md"
        mock_file.read_text.return_value = "Phrase one. Phrase two."
        
        mock_get_files.return_value = [mock_file]
        
        corpus = dream.collect_corpus()
        self.assertIn("Phrase one", corpus)
        self.assertIn("Phrase two", corpus)

    def test_dream_sequence(self):
        phrases = ["a red door", "the open loop", "silence falls", "code runs"]
        sequence = dream.dream_sequence(phrases, length=2)
        self.assertEqual(len(sequence), 2)
        # Check that it capitalized and added period
        self.assertTrue(sequence[0][0].isupper())
        self.assertTrue(sequence[0].endswith('.'))

if __name__ == '__main__':
    unittest.main()

