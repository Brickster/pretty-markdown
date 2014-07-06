from utils import whitespace_utils

import unittest

class WhitespaceUtilsTests(unittest.TestCase):

    def test_trimNonBreakingWhitespace_empty(self):

        text = ''

        expected = ''
        actual = whitespace_utils.trim_nonbreaking_whitespace(text)

        self.assertEqual(actual, expected)

    def test_trimNonBreakingWhitespace_blank_singleSpace(self):

        text = ' '

        expected = ''
        actual = whitespace_utils.trim_nonbreaking_whitespace(text)

        self.assertEqual(actual, expected)

    def test_trimNonBreakingWhitespace_blank_breakingSpace(self):

        text = '  '

        expected = ''
        actual = whitespace_utils.trim_nonbreaking_whitespace(text)

        self.assertEqual(actual, expected)

    def test_trimNonBreakingWhitespace_blank_multipleSpaces(self):

        text = '   '

        expected = ''
        actual = whitespace_utils.trim_nonbreaking_whitespace(text)

        self.assertEqual(actual, expected)

    def test_trimNonBreakingWhitespace_line_noSpacesAtEnd(self):

        text = 'This line has no spaces at the end.'

        expected = 'This line has no spaces at the end.'
        actual = whitespace_utils.trim_nonbreaking_whitespace(text)

        self.assertEqual(actual, expected)

    def test_trimNonBreakingWhitespace_line_breakingSpacesAtEnd(self):

        text = 'This line has a break at the end.  '

        expected = 'This line has a break at the end.  '
        actual = whitespace_utils.trim_nonbreaking_whitespace(text)

        self.assertEqual(actual, expected)

    def test_trimNonBreakingWhitespace_line_multipleSpacesAtEnd(self):

        text = 'This line has multiple spaces at the end.   '

        expected = 'This line has multiple spaces at the end.'
        actual = whitespace_utils.trim_nonbreaking_whitespace(text)

        self.assertEqual(actual, expected)

    def test_trimNonBreakingWhitespace_line_tabAtEnd(self):

        text = 'This line has a tab at the end.\t'

        expected = 'This line has a tab at the end.'
        actual = whitespace_utils.trim_nonbreaking_whitespace(text)

        self.assertEqual(actual, expected)

    def test_trimNonBreakingWhitespace_line_twoTabsAtEnd(self):

        text = 'This line has two tabs at the end.\t\t'

        expected = 'This line has two tabs at the end.'
        actual = whitespace_utils.trim_nonbreaking_whitespace(text)

        self.assertEqual(actual, expected)

    def test_trimNonBreakingWhitespace_block_trailingBlankLine(self):

        text = '''This block has a trailing blank line.\n'''

        expected = '''This block has a trailing blank line.\n'''
        actual = whitespace_utils.trim_nonbreaking_whitespace(text)

        self.assertEqual(actual, expected)

    def test_trimNonBreakingWhitespace_block_leadingBlankLine(self):

        text = '''\nThis block has a leading blank line.'''

        expected = '''\nThis block has a leading blank line.'''
        actual = whitespace_utils.trim_nonbreaking_whitespace(text)

        self.assertEqual(actual, expected)
