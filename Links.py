from utils import link_utils

import pretty_markdown

class FormatLinkReferenceDefinitionsCommand(pretty_markdown.PrettyMarkdownCommand):
    def modify(self, text):
        """Formats groups of link reference definitions so that their links all line up."""

        return link_utils.format_link_reference_definitions(text)

class DiscoverMissingLinksCommand(pretty_markdown.PrettyMarkdownCommand):
    def modify(self, text):
        """Adds empty link definitions for reference links."""

        default_definition = pretty_markdown.settings().get('default_missing_link_definition')
        return link_utils.discover_missing_links(text, default_definition=default_definition)
