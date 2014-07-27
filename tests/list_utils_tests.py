from unittest.mock import patch
from utils import list_utils

import unittest


class ListUtilsTests(unittest.TestCase):

    #
    # _tab_count
    #

    def test__tabCount_none(self):

        text = None
        tab_count = list_utils._tab_count(text)

        self.assertEqual(tab_count, 0)

    def test__tabCount_empty(self):

        text = ''
        tab_count = list_utils._tab_count(text)

        self.assertEqual(tab_count, 0)

    def test__tabCount_blank(self):

        text = '  '
        tab_count = list_utils._tab_count(text)

        self.assertEqual(tab_count, 0)

    def test__tabCount_zero(self):

        text = 'No tabs'
        tab_count = list_utils._tab_count(text)

        self.assertEqual(tab_count, 0)

    def test__tabCount_one(self):

        text = '\tOne tab'
        tab_count = list_utils._tab_count(text)

        self.assertEqual(tab_count, 1)

    def test__tabCount_two(self):

        text = '\t\tTwo tab'
        tab_count = list_utils._tab_count(text)

        self.assertEqual(tab_count, 2)

    def test__tabCount_many(self):

        text = '\t\t\t\t\t\tMany tabs'
        tab_count = list_utils._tab_count(text)

        self.assertEqual(tab_count, 6)

    def test__tabCount_spaces_one(self):

        text = '    One tab'
        tab_count = list_utils._tab_count(text)

        self.assertEqual(tab_count, 1)

    def test__tabCount_spaces_many(self):

        text = '    ' * 6 + 'Many tab'
        tab_count = list_utils._tab_count(text)

        self.assertEqual(tab_count, 6)

    def test__tabCount_mixed(self):

        text = '\t    \t\t        Mixed tab types'
        tab_count = list_utils._tab_count(text)

        self.assertEqual(tab_count, 6)

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

        self.assertTrue(is_item)

    def test__isUnorderedListItem_blank(self):

        text = '    '
        is_item = list_utils._is_unordered_list_item(text)

        self.assertTrue(is_item)

    def test__isUnorderedListItem_none(self):

        text = None
        is_item = list_utils._is_unordered_list_item(text)

        self.assertFalse(is_item)

    def test__isUnorderedListItem_multipleItems(self):

        text = '- item one\n- item two'
        is_item = list_utils._is_unordered_list_item(text)

        self.assertFalse(is_item)

    #
    # _is_ordered_list_item
    #

    def test__isOrderedListItem(self):

        text = '1. item'
        is_item = list_utils._is_ordered_list_item(text)

        self.assertTrue(is_item)

    def test__isOrderedListItem_multipleDigits(self):

        text = '11. item'
        is_item = list_utils._is_ordered_list_item(text)

        self.assertTrue(is_item)

    def test__isOrderedListItem_subItem_spaces(self):

        text = '    2. item'
        is_item = list_utils._is_ordered_list_item(text)

        self.assertTrue(is_item)

    def test__isOrderedListItem_subItem_tab(self):

        text = '\t3. item'
        is_item = list_utils._is_ordered_list_item(text)

        self.assertTrue(is_item)

    def test__isOrderedListItem_false(self):

        text = 'This is just text.'
        is_item = list_utils._is_ordered_list_item(text)

        self.assertFalse(is_item)

    def test__isOrderedListItem_false_notPeriodDelimited(self):

        text = '1, Item'
        is_item = list_utils._is_ordered_list_item(text)

        self.assertFalse(is_item)

    def test__isOrderedListItem_unorderedItem(self):

        text = '1 This is an unordered item'
        is_item = list_utils._is_ordered_list_item(text)

        self.assertFalse(is_item)

    def test__isOrderedListItem_empty(self):

        text = ''
        is_item = list_utils._is_ordered_list_item(text)

        self.assertTrue(is_item)

    def test__isOrderedListItem_blank(self):

        text = '    '
        is_item = list_utils._is_ordered_list_item(text)

        self.assertTrue(is_item)

    def test__isOrderedListItem_none(self):

        text = None
        is_item = list_utils._is_ordered_list_item(text)

        self.assertFalse(is_item)

    def test__isOrderedListItem_multipleItems(self):

        text = '1. item one\n2. item two'
        is_item = list_utils._is_ordered_list_item(text)

        self.assertFalse(is_item)

    def test__isOrderedListItem_escaped(self):

        text = '\1986. It was a great year.'
        is_item = list_utils._is_ordered_list_item(text)

        self.assertFalse(is_item)

    def test__isOrderedListItem_notAnOrderedList(self):

        text = '+ item one'
        is_item = list_utils._is_ordered_list_item(text)

        self.assertFalse(is_item)

    #
    # _format_unordered_list
    #

    def test__formatUnorderedList(self):

        text = ['- item 1', '    * sub item', '        - sub sub item', '* item 2']
        expected = ['- item 1', '    + sub item', '        * sub sub item', '- item 2']

        actual = list_utils._format_unordered_list(text)

        self.assertEqual(actual, expected)

    def test__formatUnorderedList_withDelimiters(self):

        text = ['- item 1', '    * sub item', '        - sub sub item', '* item 2']
        delimiters = ['+', '*', '-']

        expected = ['+ item 1', '    * sub item', '        - sub sub item', '+ item 2']

        actual = list_utils._format_unordered_list(text, delimiters)

        self.assertEqual(actual, expected)

    def test__formatUnorderedList_spaces(self):

        text = ['- item', '    - subitem', '        - subsubitem']
        delimiters = ['-', '+', '*']

        expected = ['- item', '    + subitem', '        * subsubitem']
        actual = list_utils._format_unordered_list(text, delimiters)

        self.assertEqual(actual, expected)

    def test__formatUnorderedList_tabs(self):

        text = ['- item', '\t- subitem', '\t\t- subsubitem']
        delimiters = ['-', '+', '*']

        expected = ['- item', '\t+ subitem', '\t\t* subsubitem']
        actual = list_utils._format_unordered_list(text, delimiters)

        self.assertEqual(actual, expected)

    def test__formatUnorderedList_tabsAndSpaces(self):

        text = ['- item', '\t- subitem', '\t    - subsubitem', '    \t- subsubitem', '    \t    - subsubsubitem']
        delimiters = ['-', '+', '*']

        expected = ['- item', '\t+ subitem', '\t    * subsubitem', '    \t* subsubitem', '    \t    - subsubsubitem']
        actual = list_utils._format_unordered_list(text, delimiters)

        self.assertEqual(actual, expected)

    def test__formatUnorderedList_rollOver(self):

        text = ['+ item', '\t+ subitem', '\t\t+ subsubitem', '\t\t\t+ subsubsubitem']
        delimiters = ['-', '+', '*']

        expected = ['- item', '\t+ subitem', '\t\t* subsubitem', '\t\t\t- subsubsubitem']
        actual = list_utils._format_unordered_list(text, delimiters)

        self.assertEqual(actual, expected)

    def test__formatUnorderedList_convertToSingleDelimiter(self):

        text = ['* item one', '* item two', '* item three']
        delimiters = ['-']

        expected = ['- item one', '- item two', '- item three']
        actual = list_utils._format_unordered_list(text, delimiters)

        self.assertEqual(actual, expected)

    def test__formatUnorderedList_convertToSingleDelimiter_withSubItems(self):

        text = ['- item', '    * sub item', '        + sub sub item']
        delimiters = ['-']

        expected = ['- item', '    - sub item', '        - sub sub item']
        actual = list_utils._format_unordered_list(text, delimiters)

        self.assertEqual(actual, expected)

    def test__formatUnorderedList_allSameLevel_oneOfEach(self):

        text = ['- item one', '+ item two', '* item three']
        delimiters = ['-', '+', '*']

        expected = ['- item one', '- item two', '- item three']
        actual = list_utils._format_unordered_list(text, delimiters)

        self.assertEqual(actual, expected)

    def test__formatUnorderedList_newLineBetweenItems(self):

        text = ['- Item one', '', '+ Item two', '', '* Item three']
        delimiters = ['-', '*']

        expected = ['- Item one', '', '- Item two', '', '- Item three']

        actual = list_utils._format_unordered_list(text, delimiters)

        self.assertEqual(actual, expected)

    def test__formatUnorderedList_newLineBetweenItems_multipleLevels(self):

        text = ['- Item one', '', '\t+ Sub item one', '', '* Item two']
        delimiters = ['-', '*']

        expected = ['- Item one', '', '\t* Sub item one', '', '- Item two']
        actual = list_utils._format_unordered_list(text, delimiters)

        self.assertEqual(actual, expected)

    def test__formatUnorderedList_lastItemIsDuplicate(self):

        text = ['* item', '* item']
        delimiters = ['-', '+', '*']

        expected = ['- item', '- item']
        actual = list_utils._format_unordered_list(text, delimiters)

        self.assertEqual(actual, expected)

    #
    # _format_ordered_list
    #

    def test__formatOrderedList(self):

        text = ['2. item one']

        expected = ['1. item one']
        actual = list_utils._format_ordered_list(text)

        self.assertEqual(actual, expected)

    def test__formatOrderedList_noChange(self):

        text = ['1. item one']

        expected = text
        actual = list_utils._format_ordered_list(text)

        self.assertEqual(actual, expected)

    def test__formatOrderedList_oneLevel(self):

        text = ['2. item one', '3. item two', '1. item three']

        expected = ['1. item one', '2. item two', '3. item three']
        actual = list_utils._format_ordered_list(text)

        self.assertEqual(actual, expected)

    def test__formatOrderedList_twoLevels(self):

        text = ['2. item one', '\t2. sub item', '3. item two', '1. item three']

        expected = ['1. item one', '\t1. sub item', '2. item two', '3. item three']
        actual = list_utils._format_ordered_list(text)

        self.assertEqual(actual, expected)

    def test__formatOrderedList_twoLevels_spaces(self):

        text = ['2. item one', '    2. sub item', '3. item two', '1. item three']

        expected = ['1. item one', '    1. sub item', '2. item two', '3. item three']
        actual = list_utils._format_ordered_list(text)

        self.assertEqual(actual, expected)

    def test__formatOrderedList_manyLevels(self):

        text = ['2. item one', '\t2. sub item', '3. item two', '\t55. sub item', '\t\t2. sub sub item 1', '\t\t3. sub sub item 2', '1. item three']

        expected = ['1. item one', '\t1. sub item', '2. item two', '\t1. sub item', '\t\t1. sub sub item 1', '\t\t2. sub sub item 2', '3. item three']
        actual = list_utils._format_ordered_list(text)

        self.assertEqual(actual, expected)

    def test__formatOrderedList_manyLevels_tabsAndSpaces(self):

        text = ['2. item one', '\t2. sub item', '3. item two', '    55. sub item', '\t    2. sub sub item 1', '        3. sub sub item 2', '1. item three']

        expected = ['1. item one', '\t1. sub item', '2. item two', '    1. sub item', '\t    1. sub sub item 1', '        2. sub sub item 2', '3. item three']
        actual = list_utils._format_ordered_list(text)

        self.assertEqual(actual, expected)

    def test__formatOrderedList_newLineBetweenItems(self):

        text = ['1. Item one', '', '1. Item two', '', '4. Item three']

        expected = ['1. Item one', '', '2. Item two', '', '3. Item three']
        actual = list_utils._format_ordered_list(text)

        self.assertEqual(actual, expected)

    def test__formatOrderedList_newLineBetweenItems_multipleLevels(self):

        text = ['1. Item one', '', '\t2. Sub item one', '', '3. Item two']

        expected = ['1. Item one', '', '\t1. Sub item one', '', '2. Item two']
        actual = list_utils._format_ordered_list(text)

        self.assertEqual(actual, expected)

    def test__formatOrderedList_newLineAtEnd(self):

        text = ['1. Item one', '1. Item two', '']

        expected = ['1. Item one', '2. Item two', '']
        actual = list_utils._format_ordered_list(text)

        self.assertEqual(actual, expected)

    #
    # alternate_unordered_list_delimiters
    #

    @patch('util_utils.process_groups')
    def test_alternateUnorderedListDelimiters(self, mock_process_groups):

        input_text = 'this is the input'
        delimiters = ['-']
        expected = 'this is the different'

        mock_process_groups.return_value = expected

        actual = list_utils.alternate_unordered_list_delimiters(input_text, delimiters)

        mock_process_groups.assert_called_with(input_text,
                                               is_group_member=list_utils._is_unordered_list_item,
                                               process_group=list_utils._format_unordered_list,
                                               process_group_parameters={'delimiters': delimiters})

        self.assertEqual(actual, expected)

    #
    # fix_ordered_list_numbering
    #

    @patch('util_utils.process_groups')
    def test_fixOrderedListNumbering(self, mock_process_groups):

        input_text = 'this is the input'
        expected = 'this is the different'

        mock_process_groups.return_value = expected

        actual = list_utils.fix_ordered_list_numbering(input_text)

        mock_process_groups.assert_called_with(input_text,
                                               is_group_member=list_utils._is_ordered_list_item,
                                               process_group=list_utils._format_ordered_list)

        self.assertEqual(actual, expected)
