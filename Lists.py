from utils import list_utils

import pretty_markdown

class AlternateUnorderedListDelimitersCommand(pretty_markdown.PrettyMarkdownCommand):
    def modify(self, text):
        """Alternates the delimiters in unordered lists according to their indentation."""

        delimiters = pretty_markdown.settings().get('unordered_list_delimiters')
        return list_utils.alternate_unordered_list_delimiters(text, delimiters)

class FixOrderedListNumberingCommand(pretty_markdown.PrettyMarkdownCommand):
    def modify(self, text):
        """Fixes the number for ordered lists."""

        return list_utils.fix_ordered_list_numbering(text)

class CreateHangingListIndentsCommand(pretty_markdown.PrettyMarkdownCommand):
    def modify(self, text):
        """"""

        return text
