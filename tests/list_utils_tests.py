from utils import list_utils

import unittest

class ListUtilsTests(unittest.TestCase):

    def test_doesNothing(self):

        text = '- item one'

        expected = text
        actual = list_utils.alternate_unordered_list_delimiters(text)

        self.assertEqual(actual, expected)
