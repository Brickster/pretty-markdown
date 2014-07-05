from utils import header_utils

import unittest


class HeaderUtilsTests(unittest.TestCase):

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
