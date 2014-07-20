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

    @unittest.skip("later enhancement for issue #12")
    def test_isLinkReferenceDefinition_containsTitle_inWrongOrder(self):

        text = '[Google]: "This is in the wrong order" http://google.com'
        is_reference = link_utils.is_link_reference_definition(text)

        self.assertFalse(is_reference)

    def test_formatLinkReferenceDefitions(self):

        text = 'I use [Google][] and sometimes [Bing][].\n\n[Google]: http://google.com\n[IGN]: http://ign.com\n\nGoogle is better though.'

        expected = 'I use [Google][] and sometimes [Bing][].\n\n[Google]: http://google.com\n[IGN]:    http://ign.com\n\nGoogle is better though.'
        actual = link_utils.format_link_reference_definitions(text)

        self.assertEqual(actual, expected)

    def test_formatLinkReferenceDefitions_noLinks(self):

        text = 'This is just text.'

        expected = text
        actual = link_utils.format_link_reference_definitions(text)

        self.assertEqual(actual, expected)

    def test_formatLinkReferenceDefitions_oneLink(self):

        text = '[Google]: http://google.com'

        expected = text
        actual = link_utils.format_link_reference_definitions(text)

        self.assertEqual(actual, expected)

    def test_formatLinkReferenceDefitions_twoLinks(self):

        text = '[Google]: http://google.com\n[IGN]: http://ign.com'

        expected = '[Google]: http://google.com\n[IGN]:    http://ign.com'
        actual = link_utils.format_link_reference_definitions(text)

        self.assertEqual(actual, expected)

    def test_formatLinkReferenceDefitions_multipleGroups(self):

        text = """This is [Markdown][].

[Markdown]: http://daringfireball.net/projects/markdown/

You can use it to write HTML that is not ugly due to messy [ordered lists][] and [links][].

[ordered lists]: http://daringfireball.net/projects/markdown/syntax#list
[links]: http://daringfireball.net/projects/markdown/syntax#link

For instance, I can link to [Google][] and [Bing][].

[Google]: http://google.com
[Bing]: http://bing.com"""

        expected = """This is [Markdown][].

[Markdown]: http://daringfireball.net/projects/markdown/

You can use it to write HTML that is not ugly due to messy [ordered lists][] and [links][].

[ordered lists]: http://daringfireball.net/projects/markdown/syntax#list
[links]:         http://daringfireball.net/projects/markdown/syntax#link

For instance, I can link to [Google][] and [Bing][].

[Google]: http://google.com
[Bing]:   http://bing.com"""
        actual = link_utils.format_link_reference_definitions(text)

        self.assertEqual(actual, expected)
