from utils import italic_utils

import unittest

class BoldUtilsTests(unittest.TestCase):

    def test_convertItalics_empty(self):

        text = ''
        character = '_'

        expected = ''
        actual = italic_utils.convert_italics(text, character)

        self.assertEqual(actual, expected)

    def test_convertItalics_noChange(self):

        text = '_Italics_'
        character = '_'

        expected = '_Italics_'
        actual = italic_utils.convert_italics(text, character)

        self.assertEqual(actual, expected)

    def test_convertItalics_fromOtherCharacter_asterisk(self):

        text = '*Italics*'
        character = '_'

        expected = '_Italics_'
        actual = italic_utils.convert_italics(text, character)

        self.assertEqual(actual, expected)

    def test_convertItalics_fromOtherCharacter_underscore(self):

        text = '_Bold_'
        character = '*'

        expected = '*Bold*'
        actual = italic_utils.convert_italics(text, character)

        self.assertEqual(actual, expected)

    def test_convertItalics_bold(self):

        text = '**Italics**'
        character = '_'

        expected = '**Italics**'
        actual = italic_utils.convert_italics(text, character)

        self.assertEqual(actual, expected)

    def test_convertItalics_boldAndItalics_sameCharacter(self):

        text = '***BoldAndItalics***'
        character = '_'

        expected = '**_BoldAndItalics_**'
        actual = italic_utils.convert_italics(text, character)

        self.assertEqual(actual, expected)
