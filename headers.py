from utils import header_utils

import pretty_markdown


class FixHeaderBalancingCommand(pretty_markdown.PrettyMarkdownCommand):
    def modify(self, text):
        """Balances headers."""

        balancing = pretty_markdown.settings().get('header_balancing')
        return header_utils.fix_header_balancing(text, balancing)


class ConvertHeadersCommand(pretty_markdown.PrettyMarkdownCommand):
    def modify(self, text):
        """Depending on settings, converts atx to Setext header or vice versa."""

        return text
