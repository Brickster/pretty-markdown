from utils import link_utils

import unittest

class LinkUtilsTests(unittest.TestCase):

    def test_isLinkReferenceDefinition_empty(self):

        text = ''
        is_reference = link_utils.is_link_reference_definition(text)

        self.assertFalse(is_reference)

    def test_isLinkReferenceDefinition_blank(self):

        text = '      '
        is_reference = link_utils.is_link_reference_definition(text)

        self.assertFalse(is_reference)

    def test_isLinkReferenceDefinition_false(self):

        text = 'this is not a reference'
        is_reference = link_utils.is_link_reference_definition(text)

        self.assertFalse(is_reference)

    def test_isLinkReferenceDefinition_true(self):

        text = '[Google]: http://google.com'
        is_reference = link_utils.is_link_reference_definition(text)

        self.assertTrue(is_reference)

    def test_isLinkReferenceDefinition_containsTitle(self):

        text = '[Google]: http://google.com "Google.com"'
        is_reference = link_utils.is_link_reference_definition(text)

        self.assertTrue(is_reference)

    def test_isLinkReferenceDefinition_multipleLines(self):

        text = '[Google]: http://google.com\nThis entire string is not a reference."'
        is_reference = link_utils.is_link_reference_definition(text)

        self.assertFalse(is_reference)

    def test_isLinkReferenceDefinition_idWithoutDefinition(self):

        text = '[Google]: '
        is_reference = link_utils.is_link_reference_definition(text)

        self.assertFalse(is_reference)

    # def test_isLinkReferenceDefinition_containsTitle_inWrongOrder(self):

    #     text = '[Google]: "This is in the wrong order" http://google.com'
    #     is_reference = link_utils.is_link_reference_definition(text)

    #     self.assertFalse(is_reference)

    def test_formatLinkReferenceDefitions(self):

        text = 'This is the text'

        expected = text
        actual = link_utils.format_link_reference_definitions(text)

        self.assertEqual(actual, expected)
