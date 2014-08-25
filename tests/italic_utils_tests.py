from utils import italic_utils

import unittest


class ItalicUtilsTests(unittest.TestCase):

    def test_convertItalics_empty(self):

        text = ''
        character = '_'

        expected = ''
        actual = italic_utils.convert_italics(text, character)

        self.assertEqual(actual, expected)

    def test_convertItalics_italicsEmptyString(self):

        text = '**'
        character = '_'

        expected = '**'
        actual = italic_utils.convert_italics(text, character)

        self.assertEqual(actual, expected)

    def test_convertItalics_italicsBlankString(self):

        text = '* *'
        character = '_'

        expected = '* *'
        actual = italic_utils.convert_italics(text, character)

        self.assertEqual(actual, expected)

    def test_convertItalics_noChange(self):

        text = '_Italics_'
        character = '_'

        expected = '_Italics_'
        actual = italic_utils.convert_italics(text, character)

        self.assertEqual(actual, expected)

    def test_convertItalicss_singleCharacter(self):

        text = '*I*'
        character = '_'

        expected = '_I_'
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

    def test_convertItalics_boldAndItalics_sameCharacter_noChange(self):

        text = '***BoldAndItalics***'
        character = '*'

        expected = '***BoldAndItalics***'
        actual = italic_utils.convert_italics(text, character)

        self.assertEqual(actual, expected)

    def test_convertItalics_boldAndItalics_noChange(self):

        text = '**_BoldAndItalics_**'
        character = '_'

        expected = '**_BoldAndItalics_**'
        actual = italic_utils.convert_italics(text, character)

        self.assertEqual(actual, expected)

    def test_convertItalics_wrappedTextStartsWithSpace(self):

        text = '* starts with space*'
        character = '_'

        expected = '* starts with space*'
        actual = italic_utils.convert_italics(text, character)

        self.assertEqual(actual, expected)

    def test_convertItalics_wrappedTextEndsWithSpace(self):

        text = '*ends with space *'
        character = '_'

        expected = '*ends with space *'
        actual = italic_utils.convert_italics(text, character)

        self.assertEqual(actual, expected)

    def test_convertItalics_tooManyCharacters(self):

        text = '****too many****'
        character = '_'

        expected = '**_*too many*_**'
        actual = italic_utils.convert_italics(text, character)

        self.assertEqual(actual, expected)

    def test_convertItalics_italicsInMiddleOfSentence(self):

        text = 'There are *italics* in this sentence.'
        character = '_'

        expected = 'There are _italics_ in this sentence.'
        actual = italic_utils.convert_italics(text, character)

        self.assertEqual(actual, expected)

    def test_convertItalics_boldInMiddleOfSentence(self):

        text = 'There is **bold** in this sentence.'
        character = '_'

        expected = 'There is **bold** in this sentence.'
        actual = italic_utils.convert_italics(text, character)

        self.assertEqual(actual, expected)

    def test_convertItalics_boldAndItalicsInMiddleOfSentence(self):

        text = 'There is both ***bold and italics*** in this sentence.'
        character = '_'

        expected = 'There is both **_bold and italics_** in this sentence.'
        actual = italic_utils.convert_italics(text, character)

        self.assertEqual(actual, expected)

    def test_convertItalics_twoItalicsInARow_fromAsterisks(self):

        text = '*italics*\n***bold and italics***'
        character = '_'

        expected = '_italics_\n**_bold and italics_**'
        actual = italic_utils.convert_italics(text, character)

        self.assertEqual(actual, expected)

    def test_convertItalics_twoItalicsInARow_fromUnderscores(self):

        text = '_italics_\n___bold and italics___'
        character = '*'

        expected = '*italics*\n__*bold and italics*__'
        actual = italic_utils.convert_italics(text, character)

        self.assertEqual(actual, expected)

    def test_convertItalics_wrongCharacter(self):

        with self.assertRaisesRegex(AssertionError, 'character must be one of *'):
            italic_utils.convert_italics('', '^')
