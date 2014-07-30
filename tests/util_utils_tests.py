from utils import util_utils

import unittest


class UtilUtilsTests(unittest.TestCase):

    #
    # process_groups
    #

    def test_processGroups(self):

        text = 'This\ncould be\nthe test'

        is_group_lambda = lambda line: line == 'could be'
        process_lambda = lambda lines: ['is'] 

        expected = 'This\nis\nthe test'
        actual = util_utils.process_groups(text, is_group_member=is_group_lambda, process_group=process_lambda)

        self.assertEqual(actual, expected)

    def test_processGroups_noChange(self):

        text = 'This\nis\nthe test'

        is_group_lambda = lambda line: False
        process_lambda = None

        expected = text
        actual = util_utils.process_groups(text, is_group_member=is_group_lambda, process_group=process_lambda)

        self.assertEqual(actual, expected)

    def test_processGroups_multipleGroups(self):

        text = 'This is text.\n\nRemove\nRemove\nWith text that will be removed.\nRemove\nIn multple places.'

        is_group_lambda = lambda line: line == 'Remove'
        process_lambda = lambda lines: ['Changed' for line in lines]

        expected = 'This is text.\n\nChanged\nChanged\nWith text that will be removed.\nChanged\nIn multple places.'
        actual = util_utils.process_groups(text, is_group_member=is_group_lambda, process_group=process_lambda)

        self.assertEqual(actual, expected)

    def test_processGroups_startsWithGroup(self):

        text = 'Remove\nRemove\nWith text that will be removed.'

        is_group_lambda = lambda line: line == 'Remove'
        process_lambda = lambda lines: ['Changed' for line in lines]

        expected = 'Changed\nChanged\nWith text that will be removed.'
        actual = util_utils.process_groups(text, is_group_member=is_group_lambda, process_group=process_lambda)

        self.assertEqual(actual, expected)

    def test_processGroups_endsWithGroup(self):

        text = 'This is text.\n\nRemove\nRemove'

        is_group_lambda = lambda line: line == 'Remove'
        process_lambda = lambda lines: ['Changed' for line in lines]

        expected = 'This is text.\n\nChanged\nChanged'
        actual = util_utils.process_groups(text, is_group_member=is_group_lambda, process_group=process_lambda)

        self.assertEqual(actual, expected)
