from . import pretty_markdown

import re

class FixHeaderBalancingCommand(pretty_markdown.PrettyMarkdownCommand):
    def modify(self, text):
        '''Balances ATX style headers.'''

        text = re.sub(r'^((#+)\s.*?)(?:\s#+)?$', r'\1 \2', text, flags=re.MULTILINE)

        return text
