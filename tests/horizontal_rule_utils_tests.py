from utils import horizontal_rule_utils

import unittest


class HorizontalRuleUtilsTests(unittest.TestCase):

    #
    # convert_horizontal_rules
    #

    def test_convertHorizontalRules_empty(self):

        text = ''
        rule = '---'

        expected = ''
        actual = horizontal_rule_utils.convert_horizontal_rules(text, rule)

        self.assertEqual(actual, expected)

    def test_convertHorizontalRules_notARule(self):

        text = '--'
        rule = '---'

        expected = '--'
        actual = horizontal_rule_utils.convert_horizontal_rules(text, rule)

        self.assertEqual(actual, expected)

    def test_convertHorizontalRules_alreadyAsExpected(self):

        text = '---'
        rule = '---'

        expected = '---'
        actual = horizontal_rule_utils.convert_horizontal_rules(text, rule)

        self.assertEqual(actual, expected)

    def test_convertHorizontalRules_shortened(self):

        text = '------'
        rule = '---'

        expected = '---'
        actual = horizontal_rule_utils.convert_horizontal_rules(text, rule)

        self.assertEqual(actual, expected)

    def test_convertHorizontalRules_removeSpaces(self):

        text = '- - - -'
        rule = '---'

        expected = '---'
        actual = horizontal_rule_utils.convert_horizontal_rules(text, rule)

        self.assertEqual(actual, expected)

    def test_convertHorizontalRules_fromAsterisks(self):

        text = '***'
        rule = '---'

        expected = '---'
        actual = horizontal_rule_utils.convert_horizontal_rules(text, rule)

        self.assertEqual(actual, expected)

    def test_convertHorizontalRules_fromAsterisksWithSpaces(self):

        text = '* * *'
        rule = '---'

        expected = '---'
        actual = horizontal_rule_utils.convert_horizontal_rules(text, rule)

        self.assertEqual(actual, expected)

    def test_convertHorizontalRules_fromUnderscores(self):

        text = '___'
        rule = '---'

        expected = '---'
        actual = horizontal_rule_utils.convert_horizontal_rules(text, rule)

        self.assertEqual(actual, expected)

    def test_convertHorizontalRules_fromUnderscoresWithSpaces(self):

        text = '_ _ _'
        rule = '---'

        expected = '---'
        actual = horizontal_rule_utils.convert_horizontal_rules(text, rule)

        self.assertEqual(actual, expected)

    def test_convertHorizontalRules_setextHeader(self):

        text = 'Header\n------'
        rule = '---'

        expected = 'Header\n------'
        actual = horizontal_rule_utils.convert_horizontal_rules(text, rule)

        self.assertEqual(actual, expected)

    def test_convertHorizontalRules_horizontalRuleHasUnevenSpaces(self):

        text = '---'
        rule = '-- --'

        expected = '-- --'
        actual = horizontal_rule_utils.convert_horizontal_rules(text, rule)

        self.assertEqual(actual, expected)

    def test_convertHorizontalRules_invalidHorizontalRule(self):

        with self.assertRaisesRegex(AssertionError, 'A horizontal rule is defined by three or more hyphens, asterisks, or underscores with optional spaces in between.'):
            horizontal_rule_utils.convert_horizontal_rules('', 'mmm')

    def test_convertHorizontalRules_multipleRules(self):

        text = '---\n***\n___\n* * *'
        rule = '***'

        expected = '***\n***\n___\n* * *'
        actual = horizontal_rule_utils.convert_horizontal_rules(text, rule)

        self.assertEqual(actual, expected)

    def test_convertHorizontalRules_multipleRules_allOnNewLines(self):

        text = '---\n\n***\n\n___\n\n* * *'
        rule = '***'

        expected = '***\n\n***\n\n***\n\n***'
        actual = horizontal_rule_utils.convert_horizontal_rules(text, rule)

        self.assertEqual(actual, expected)

    def test_convertHorizontalRules_setextH1HeaderFollowedByMultipleRules(self):

        text = 'Header\n===\n---\n---'
        rule = '***'

        expected = 'Header\n===\n---\n---'
        actual = horizontal_rule_utils.convert_horizontal_rules(text, rule)

        self.assertEqual(actual, expected)

    def test_convertHorizontalRules_setextH1HeaderFollowedByMultipleRules_allOnNewLines(self):

        text = 'Header\n===\n\n---\n\n---'
        rule = '***'

        expected = 'Header\n===\n\n***\n\n***'
        actual = horizontal_rule_utils.convert_horizontal_rules(text, rule)

        self.assertEqual(actual, expected)

    def test_convertHorizontalRules_setextH2HeaderFollowedByMultipleRules(self):

        text = 'Header\n---\n---\n---'
        rule = '***'

        expected = 'Header\n---\n---\n---'
        actual = horizontal_rule_utils.convert_horizontal_rules(text, rule)

        self.assertEqual(actual, expected)

    def test_convertHorizontalRules_setextH2HeaderFollowedByMultipleRules_allOnNewLines(self):

        text = 'Header\n---\n\n---\n\n---'
        rule = '***'

        expected = 'Header\n---\n\n***\n\n***'
        actual = horizontal_rule_utils.convert_horizontal_rules(text, rule)

        self.assertEqual(actual, expected)

    #
    # is_valid_horizontal_rule
    #

    def test_isValidHorizontalRule_true(self):

        self.assertTrue(horizontal_rule_utils.is_valid_horizontal_rule('___'))

    def test_isValidHorizontalRule_false(self):

        self.assertFalse(horizontal_rule_utils.is_valid_horizontal_rule('mmm'))

    def test_isValidHorizontalRule_carrots(self):
        '''Test for issue: 6

        https://github.com/Brickstertwo/pretty-markdown/issues/6'''

        self.assertFalse(horizontal_rule_utils.is_valid_horizontal_rule('^^^'))

    def test_isValidHorizontalRule_backSlashes(self):

        self.assertFalse(horizontal_rule_utils.is_valid_horizontal_rule(r'\\\\'))  # a raw string cannot end in a backslash so "escape" the last one
