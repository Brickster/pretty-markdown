from unittest.mock import patch
from utils import link_utils

import unittest


class LinkUtilsTests(unittest.TestCase):

    #
    # is_link_reference_definition
    #

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

    #
    # format_link_reference_definitions
    #

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

    #
    # _create_link_definitions
    #

    def test__createLinkDefinitions(self):

        link_ids = ['link', 'notfound']
        definition_pairs = [['link', 'http://link.com']]

        expected = ['[link]: http://link.com', '[notfound]: 404']
        actual = link_utils._create_link_definitions(link_ids, definition_pairs)

        self.assertEqual(actual, expected)

    def test__createLinkDefinitions_noMissingDefinitions(self):

        link_ids = ['link']
        definition_pairs = [['link', 'http://link.com']]

        expected = ['[link]: http://link.com']
        actual = link_utils._create_link_definitions(link_ids, definition_pairs)

        self.assertEqual(actual, expected)

    def test__createLinkDefinitions_noLinks_empty(self):

        link_ids = []
        definition_pairs = [['link', 'http://link.com']]

        expected = ['[link]: http://link.com']
        actual = link_utils._create_link_definitions(link_ids, definition_pairs)

        self.assertEqual(actual, expected)

    def test__createLinkDefinitions_noLinks_none(self):

        link_ids = None
        definition_pairs = [['link', 'http://link.com']]

        expected = ['[link]: http://link.com']
        actual = link_utils._create_link_definitions(link_ids, definition_pairs)

        self.assertEqual(actual, expected)

    def test__createLinkDefinitions_noDefinitions_empty(self):

        link_ids = ['link']
        definition_pairs = []

        expected = ['[link]: 404']
        actual = link_utils._create_link_definitions(link_ids, definition_pairs)

        self.assertEqual(actual, expected)

    def test__createLinkDefinitions_noDefinitions_none(self):

        link_ids = ['link']
        definition_pairs = None

        expected = ['[link]: 404']
        actual = link_utils._create_link_definitions(link_ids, definition_pairs)

        self.assertEqual(actual, expected)

    def test__createLinkDefinitions_withDefaultDefinition(self):

        link_ids = ['link', 'notfound']
        definition_pairs = [['link', 'http://link.com']]
        default_definition = 'this was not found'

        expected = ['[link]: http://link.com', '[notfound]: this was not found']
        actual = link_utils._create_link_definitions(link_ids, definition_pairs, default_definition)

        self.assertEqual(actual, expected)

    def test__createLinkDefinitions_withDefaultDefinition_none(self):

        link_ids = ['link', 'notfound']
        definition_pairs = [['link', 'http://link.com']]
        default_definition = None

        expected = ['[link]: http://link.com', '[notfound]: None']
        actual = link_utils._create_link_definitions(link_ids, definition_pairs, default_definition)

        self.assertEqual(actual, expected)

    def test__createLinkDefinitions_empty(self):

        link_ids = []
        definition_pairs = []

        expected = []
        actual = link_utils._create_link_definitions(link_ids, definition_pairs)

        self.assertEqual(actual, expected)

    def test__createLinkDefinitions_none(self):

        link_ids = None
        definition_pairs = None

        expected = []
        actual = link_utils._create_link_definitions(link_ids, definition_pairs)

        self.assertEqual(actual, expected)

    #
    # discover_missing_links
    #

    def test_discoverMissingLinks(self):

        text = 'This has a missing [link][] definition.'

        expected = 'This has a missing [link][] definition.\n\n[link]: 404'
        actual = link_utils.discover_missing_links(text)

        self.assertEqual(actual, expected)

    def test_discoverMissingLinks_withDefaultDefinition(self):

        text = 'This has a missing [link][] definition.'
        default_definition = 'this is missing'

        expected = 'This has a missing [link][] definition.\n\n[link]: ' + default_definition
        actual = link_utils.discover_missing_links(text, default_definition=default_definition)

        self.assertEqual(actual, expected)

    def test_discoverMissingLinks_appendsToExistingGroup_atEnd(self):

        text = """This has a missing [link][] definition but there are existing [definitions][].

[definitions]: http://link.com"""

        expected = """This has a missing [link][] definition but there are existing [definitions][].

[definitions]: http://link.com
[link]: 404"""
        actual = link_utils.discover_missing_links(text)

        self.assertEqual(actual, expected)

    def test_discoverMissingLinks_appendsToExistingGroup_lastLineIsBlank(self):

        text = """This has a missing [link][] definition but there are existing [definitions][].

[definitions]: http://link.com
"""

        expected = """This has a missing [link][] definition but there are existing [definitions][].

[definitions]: http://link.com
[link]: 404
"""
        actual = link_utils.discover_missing_links(text)

        self.assertEqual(actual, expected)

    def test_discoverMissingLinks_appendsToExistingGroup_inMiddle(self):

        text = """This has a missing [link][] definition but there are existing [definitions][].

[definitions]: http://link.com

More text here."""

        expected = """This has a missing [link][] definition but there are existing [definitions][].

[definitions]: http://link.com
[link]: 404

More text here."""
        actual = link_utils.discover_missing_links(text)

        self.assertEqual(actual, expected)

    def test_discoverMissingLinks_appendsToExistingGroup_closest(self):

        text = """This has a missing [link][] definition but there are existing [definitions][].

[definitions]: http://definitions.com

More text links [here][].

[here]: http://here.com"""

        expected = """This has a missing [link][] definition but there are existing [definitions][].

[definitions]: http://definitions.com
[link]: 404

More text links [here][].

[here]: http://here.com"""
        actual = link_utils.discover_missing_links(text)

        self.assertEqual(actual, expected)

    def test_discoverMissingLinks_appendsToExistingGroup_sameLinkMissingMultiplePlaces(self):

        text = """This has a missing [link][] definition but there are existing [definitions][].

[definitions]: http://link.com

More the same [link][] is [here][].

[here]: http://link.com"""

        expected = """This has a missing [link][] definition but there are existing [definitions][].

[definitions]: http://link.com
[link]: 404

More the same [link][] is [here][].

[here]: http://link.com
[link]: 404"""
        actual = link_utils.discover_missing_links(text)

        self.assertEqual(actual, expected)

    #
    # format_link_reference_definitions
    #

    @patch('util_utils.process_groups')
    def test_formatLinkReferenceDefinitions(self, mock_process_groups):

        input_text = 'this is the input'
        expected = 'this is the different'

        mock_process_groups.return_value = expected

        actual = link_utils.format_link_reference_definitions(input_text)

        mock_process_groups.assert_called_with(input_text,
                                               is_group_member=link_utils.is_link_reference_definition,
                                               process_group=link_utils._format_links)

        self.assertEqual(actual, expected)
