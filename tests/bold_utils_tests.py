from utils import bold_utils

import unittest

class BoldUtilsTests(unittest.TestCase):

    def test_convertBolds_empty(self):

        text = ''
        character = '*'

        expected = ''
        actual = bold_utils.convert_bolds(text, character)

        self.assertEqual(actual, expected)

    def test_convertBolds_noChange(self):

        text = '**Bold**'
        character = '*'

        expected = '**Bold**'
        actual = bold_utils.convert_bolds(text, character)

        self.assertEqual(actual, expected)

    def test_convertBolds_fromOtherCharacter_underscore(self):

        text = '__Bold__'
        character = '*'

        expected = '**Bold**'
        actual = bold_utils.convert_bolds(text, character)

        self.assertEqual(actual, expected)

    def test_convertBolds_fromOtherCharacter_asterisk(self):

        text = '**Bold**'
        character = '_'

        expected = '__Bold__'
        actual = bold_utils.convert_bolds(text, character)

        self.assertEqual(actual, expected)

    def test_convertBolds_italics(self):

        text = '_Italics_'
        character = '*'

        expected = '_Italics_'
        actual = bold_utils.convert_bolds(text, character)

        self.assertEqual(actual, expected)

    def test_convertBolds_boldAndItalics_sameCharacter(self):

        text = '___BoldAndItalics___'
        character = '*'

        expected = '_**BoldAndItalics**_'
        actual = bold_utils.convert_bolds(text, character)

        self.assertEqual(actual, expected)

    def test_convertBolds_wrongCharacter(self):

        self.assertRaises(AssertionError, bold_utils.convert_bolds, '', '^')
