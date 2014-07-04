import pretty_markdown
import re

class FixHeaderBalancingCommand(pretty_markdown.PrettyMarkdownCommand):
    def modify(self, text):
        '''Balances headers.'''

        text = re.sub(r'^((#+)\s.*?)(?:\s#+)?$', r'\1 \2', text, flags=re.MULTILINE)

        return text

class ConvertHeadersCommand(pretty_markdown.PrettyMarkdownCommand):
    def modify(self, text):
        '''Depending on settings, converts atx to Setext header or vice versa.'''

        return text
