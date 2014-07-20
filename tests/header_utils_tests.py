from utils import header_utils

import unittest

class HeaderUtilsTests(unittest.TestCase):

    #
    # fix_header_balancing
    #

    def test_fixHeaderBalancing_empty(self):

        text = ''

        expected = ''
        actual = header_utils.fix_header_balancing(text)

        self.assertEqual(actual, expected)

    def test_fixHeaderBalancing_atx_zeroLeft_zeroRight(self):

        text = 'Header'

        expected = 'Header'
        actual = header_utils.fix_header_balancing(text)

        self.assertEqual(actual, expected)

    def test_fixHeaderBalancing_atx_zeroLeft_oneRight(self):

        text = 'Header #'

        expected = 'Header #'
        actual = header_utils.fix_header_balancing(text)

        self.assertEqual(actual, expected)

    def test_fixHeaderBalancing_atx_oneLeft_zeroRight(self):

        text = '# Header'

        expected = '# Header #'
        actual = header_utils.fix_header_balancing(text)

        self.assertEqual(actual, expected)

    def test_fixHeaderBalancing_atx_oneLeft_oneRight(self):

        text = '# Header #'

        expected = '# Header #'
        actual = header_utils.fix_header_balancing(text)

        self.assertEqual(actual, expected)

    def test_fixHeaderBalancing_atx_oneLeft_twoRight(self):

        text = '# Header ##'

        expected = '# Header #'
        actual = header_utils.fix_header_balancing(text)

        self.assertEqual(actual, expected)

    def test_fixHeaderBalancing_atx_twoLeft_oneRight(self):

        text = '## Header #'

        expected = '## Header ##'
        actual = header_utils.fix_header_balancing(text)

        self.assertEqual(actual, expected)

    def test_fixHeaderBalancing_setext_h1(self):

        text = 'Header\n==='

        expected = 'Header\n======'
        actual = header_utils.fix_header_balancing(text)

        self.assertEqual(actual, expected)

    def test_fixHeaderBalancing_setext_h2(self):

        text = 'Header\n---'

        expected = 'Header\n------'
        actual = header_utils.fix_header_balancing(text)

        self.assertEqual(actual, expected)

    def test_fixHeaderBalancing_setext_tooMany(self):

        text = 'Header\n----------------'

        expected = 'Header\n------'
        actual = header_utils.fix_header_balancing(text)

        self.assertEqual(actual, expected)


    def test_fixHeaderBalancing_setext_alreadyBalanced(self):

        text = 'Header\n------'

        expected = text
        actual = header_utils.fix_header_balancing(text)

        self.assertEqual(actual, expected)

    def test_fixHeaderBalancing_setext_notAHeader(self):

        text = 'Header\n***'

        expected = text
        actual = header_utils.fix_header_balancing(text)

        self.assertEqual(actual, expected)

    def test_fixHeaderBalancing_setext_multiple(self):

        text = 'Header 1\n===\nHeader 2\n----'

        expected = 'Header 1\n========\nHeader 2\n--------'
        actual = header_utils.fix_header_balancing(text)

        self.assertEqual(actual, expected)

    def test_fixHeaderBalancing_setext_ruleAsAHeader(self):
        """Confirms that rules can be a header title when followed by a setext header line."""

        text = '---\n-------'

        expected = '---\n---'
        actual = header_utils.fix_header_balancing(text)

        self.assertEqual(actual, expected)

    #
    # is_setext_header
    #

    def test_isSetextHeader_equals(self):

        text = '==='
        is_setext = header_utils.is_setext_header(text)

        self.assertTrue(is_setext)

    def test_isSetextHeader_dash(self):

        text = '---'
        is_setext = header_utils.is_setext_header(text)

        self.assertTrue(is_setext)

    def test_isSetextHeader_tooFew(self):

        text = '=='
        is_setext = header_utils.is_setext_header(text)

        self.assertFalse(is_setext)

    def test_isSetextHeader_wrongCharacter(self):

        text = '**'
        is_setext = header_utils.is_setext_header(text)

        self.assertFalse(is_setext)

    def test_isSetextHeader_textLineStartsWithSetextHeader(self):

        text = '==== this starts with a setext style header'
        is_setext = header_utils.is_setext_header(text)

        self.assertFalse(is_setext)

    def test_isSetextHeader_empty(self):

        text = ''
        is_setext = header_utils.is_setext_header(text)

        self.assertFalse(is_setext)

    def test_isSetextHeader_blank(self):

        text = '   '
        is_setext = header_utils.is_setext_header(text)

        self.assertFalse(is_setext)

    def test_isSetextHeader_none(self):

        text = None
        is_setext = header_utils.is_setext_header(text)

        self.assertFalse(is_setext)
