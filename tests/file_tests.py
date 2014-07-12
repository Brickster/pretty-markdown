from utils import bold_utils
from utils import header_utils
from utils import italic_utils

import os.path
import unittest

files_directory_path = os.path.join(os.path.dirname(__file__), 'files')
dirty_file_path = os.path.join(files_directory_path, 'dirty.md')
clean_file_path = os.path.join(files_directory_path, 'clean.md')

class FileTests(unittest.TestCase):

    """Tests utils against an actual Markdown file."""

    def test_dirtyToClean(self):

        with open(dirty_file_path) as dirty_file:
            text = dirty_file.read()
        with open(clean_file_path) as clean_file:
            expected = clean_file.read()

        actual = bold_utils.convert_bolds(text)
        actual = header_utils.fix_header_balancing(actual)
        actual = italic_utils.convert_italics(actual)

        self.assertEqual(actual, expected)

    def test_cleanToClean(self):

        with open(clean_file_path) as clean_file:
            expected = clean_file.read()

        actual = bold_utils.convert_bolds(expected)
        actual = header_utils.fix_header_balancing(actual)
        actual = italic_utils.convert_italics(actual)

        self.assertEqual(actual, expected)
