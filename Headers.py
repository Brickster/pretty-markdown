from utils import header_utils

import pretty_markdown

class FixHeaderBalancingCommand(pretty_markdown.PrettyMarkdownCommand):
    def modify(self, text):
        """Balances headers."""

        return header_utils.fix_header_balancing(text)

class ConvertHeadersCommand(pretty_markdown.PrettyMarkdownCommand):
    def modify(self, text):
        """Depending on settings, converts atx to Setext header or vice versa."""

        return text
