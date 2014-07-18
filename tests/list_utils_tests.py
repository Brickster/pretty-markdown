from utils import list_utils

import unittest

class ListUtilsTests(unittest.TestCase):

    #
    # alternate_unordered_list_delimiters
    #

    def test_alternateUnorderedListDelimiters(self):

        text = """- item 1
    * sub item
        - sub sub item
* item 2"""

        expected = """- item 1
    + sub item
        * sub sub item
- item 2"""
        actual = list_utils.alternate_unordered_list_delimiters(text)

        self.assertEqual(actual, expected)

    def test_alternateUnorderedListDelimiters_withDelimiters(self):

        text = """- item 1
    * sub item
        - sub sub item
* item 2"""
        delimiters = ['+', '*', '-']

        expected = """+ item 1
    * sub item
        - sub sub item
+ item 2"""
        actual = list_utils.alternate_unordered_list_delimiters(text, delimiters)

        self.assertEqual(actual, expected)

    def test_alternateUnorderedListDelimiters_spaces(self):

        text = '- item\n    - subitem\n        - subsubitem'
        delimiters = ['-', '+', '*']

        expected = '- item\n    + subitem\n        * subsubitem'
        actual = list_utils.alternate_unordered_list_delimiters(text, delimiters)

        self.assertEqual(actual, expected)

    def test_alternateUnorderedListDelimiters_tabs(self):

        text = '- item\n\t- subitem\n\t\t- subsubitem'
        delimiters = ['-', '+', '*']

        expected = '- item\n\t+ subitem\n\t\t* subsubitem'
        actual = list_utils.alternate_unordered_list_delimiters(text, delimiters)

        self.assertEqual(actual, expected)

    def test_alternateUnorderedListDelimiters_tabsAndSpaces(self):

        text = '- item\n\t- subitem\n\t    - subsubitem\n    \t- subsubitem\n    \t    - subsubsubitem'
        delimiters = ['-', '+', '*']

        expected = '- item\n\t+ subitem\n\t    * subsubitem\n    \t* subsubitem\n    \t    - subsubsubitem'
        actual = list_utils.alternate_unordered_list_delimiters(text, delimiters)

        self.assertEqual(actual, expected)

    def test_alternateUnorderedListDelimiters_rollOver(self):

        text = '+ item\n\t+ subitem\n\t\t+ subsubitem\n\t\t\t+ subsubsubitem'
        delimiters = ['-', '+', '*']

        expected = '- item\n\t+ subitem\n\t\t* subsubitem\n\t\t\t- subsubsubitem'
        actual = list_utils.alternate_unordered_list_delimiters(text, delimiters)

        self.assertEqual(actual, expected)

    def test_alternateUnorderedListDelimiters_convertToSingleDelimiter(self):

        text = "* item one\n* item two\n* item three"
        delimiters = ['-']

        expected = "- item one\n- item two\n- item three"
        actual = list_utils.alternate_unordered_list_delimiters(text, delimiters)

        self.assertEqual(actual, expected)

    def test_alternateUnorderedListDelimiters_convertToSingleDelimiter_withSubItems(self):

        text = """- item
    * sub item
        + sub sub item"""
        delimiters = ['-']

        expected = """- item
    - sub item
        - sub sub item"""
        actual = list_utils.alternate_unordered_list_delimiters(text, delimiters)

        self.assertEqual(actual, expected)

    def test_alternateUnorderedListDelimiters_allSameLevel_oneOfEach(self):

        text = "- item one\n+ item two\n* item three"
        delimiters = ['-', '+', '*']

        expected = "- item one\n- item two\n- item three"
        actual = list_utils.alternate_unordered_list_delimiters(text, delimiters)

        self.assertEqual(actual, expected)

    def test_alternateUnorderedListDelimiters_doesNothing(self):

        text = 'item one'

        expected = text
        actual = list_utils.alternate_unordered_list_delimiters(text)

        self.assertEqual(actual, expected)


    #
    # _is_unordered_list_item
    #

    def test__isUnorderedListItem_dash(self):

        text = '- item'
        is_item = list_utils._is_unordered_list_item(text)

        self.assertTrue(is_item)

    def test__isUnorderedListItem_plus(self):

        text = '+ item'
        is_item = list_utils._is_unordered_list_item(text)

        self.assertTrue(is_item)

    def test__isUnorderedListItem_asterisk(self):

        text = '* item'
        is_item = list_utils._is_unordered_list_item(text)

        self.assertTrue(is_item)

    def test__isUnorderedListItem_subItem_spaces(self):

        text = '    - item'
        is_item = list_utils._is_unordered_list_item(text)

        self.assertTrue(is_item)

    def test__isUnorderedListItem_subItem_tab(self):

        text = '\t- item'
        is_item = list_utils._is_unordered_list_item(text)

        self.assertTrue(is_item)

    def test__isUnorderedListItem_false(self):

        text = 'This is just text.'
        is_item = list_utils._is_unordered_list_item(text)

        self.assertFalse(is_item)

    def test__isUnorderedListItem_orderedItem(self):

        text = '1. This is an ordered item.'
        is_item = list_utils._is_unordered_list_item(text)

        self.assertFalse(is_item)

    def test__isUnorderedListItem_empty(self):

        text = ''
        is_item = list_utils._is_unordered_list_item(text)

        self.assertFalse(is_item)

    def test__isUnorderedListItem_blank(self):

        text = '    '
        is_item = list_utils._is_unordered_list_item(text)

        self.assertFalse(is_item)

    def test__isUnorderedListItem_none(self):

        text = None
        is_item = list_utils._is_unordered_list_item(text)

        self.assertFalse(is_item) 

    def test__isUnorderedListItem_multipleItems(self):

        text = '- item one\n- item two'
        is_item = list_utils._is_unordered_list_item(text)

        self.assertFalse(is_item) 
