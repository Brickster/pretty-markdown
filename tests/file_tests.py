from utils import bold_utils
from utils import header_utils
from utils import horizontal_rule_utils
from utils import italic_utils
from utils import link_utils
from utils import list_utils
from utils import whitespace_utils

import os.path
import unittest

FILES_DIRECTORY_PATH = os.path.join(os.path.dirname(__file__), 'files')
DIRTY_FILE_PATH = os.path.join(FILES_DIRECTORY_PATH, 'dirty.md')
CLEAN_FILE_PATH = os.path.join(FILES_DIRECTORY_PATH, 'clean.md')
CLEAN_ANY_HEADER_UNBALANCED_FILE_PATH = os.path.join(FILES_DIRECTORY_PATH, 'clean_anyHeader_unbalanced.md')


class FileTests(unittest.TestCase):

    """Tests utils against an actual Markdown file."""

    def test_dirtyToClean(self):

        with open(DIRTY_FILE_PATH) as dirty_file:
            text = dirty_file.read()
        with open(CLEAN_FILE_PATH) as clean_file:
            expected = clean_file.read()

        actual = bold_utils.convert_bolds(text)
        actual = header_utils.fix_header_balancing(actual)
        actual = horizontal_rule_utils.convert_horizontal_rules(actual)
        actual = italic_utils.convert_italics(actual)
        actual = link_utils.discover_missing_links(actual)
        actual = link_utils.format_link_reference_definitions(actual)
        actual = list_utils.alternate_unordered_list_delimiters(actual)
        actual = list_utils.fix_ordered_list_numbering(actual)
        actual = whitespace_utils.trim_nonbreaking_whitespace(actual)

        self.assertEqual(actual, expected)

    def test_dirtyToClean_atx_unbalanced(self):

        with open(DIRTY_FILE_PATH) as dirty_file:
            text = dirty_file.read()
        with open(CLEAN_ANY_HEADER_UNBALANCED_FILE_PATH) as clean_file:
            expected = clean_file.read()

        actual = bold_utils.convert_bolds(text)
        actual = header_utils.fix_header_balancing(actual, balancing=header_utils.UNBALANCED)
        actual = horizontal_rule_utils.convert_horizontal_rules(actual)
        actual = italic_utils.convert_italics(actual)
        actual = link_utils.discover_missing_links(actual)
        actual = link_utils.format_link_reference_definitions(actual)
        actual = list_utils.alternate_unordered_list_delimiters(actual)
        actual = list_utils.fix_ordered_list_numbering(actual)
        actual = whitespace_utils.trim_nonbreaking_whitespace(actual)

        self.assertEqual(actual, expected)

    def test_cleanToClean(self):

        with open(CLEAN_FILE_PATH) as clean_file:
            expected = clean_file.read()

        actual = bold_utils.convert_bolds(expected)
        actual = header_utils.fix_header_balancing(actual)
        actual = horizontal_rule_utils.convert_horizontal_rules(actual)
        actual = italic_utils.convert_italics(actual)
        actual = link_utils.discover_missing_links(actual)
        actual = link_utils.format_link_reference_definitions(actual)
        actual = list_utils.alternate_unordered_list_delimiters(actual)
        actual = list_utils.fix_ordered_list_numbering(actual)
        actual = whitespace_utils.trim_nonbreaking_whitespace(actual)

        self.assertEqual(actual, expected)
