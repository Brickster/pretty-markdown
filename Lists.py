from utils import list_utils

import pretty_markdown

class AlternateUnorderedListDelimitersCommand(pretty_markdown.PrettyMarkdownCommand):
    def modify(self, text):
        """Alternates the delimiters in unordered lists according to their indentation."""

        return list_utils.alternate_unordered_list_delimiters(text)

class FixOrderedListNumberingCommand(pretty_markdown.PrettyMarkdownCommand):
    def modify(self, text):
        """"""

        return text

class CreateHangingListIndentsCommand(pretty_markdown.PrettyMarkdownCommand):
    def modify(self, text):
        """"""

        return text
