from utils import link_utils

import pretty_markdown

class FormatLinkReferenceDefinitionsCommand(pretty_markdown.PrettyMarkdownCommand):
    def modify(self, text):
        """Formats groups of link reference definitions so that their links all line up."""

        return link_utils.format_link_reference_definitions(text)

class DiscoverMissingLinksCommand(pretty_markdown.PrettyMarkdownCommand):
    def modify(self, text):
        """"""

        return text
