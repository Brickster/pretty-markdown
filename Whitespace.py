from utils import whitespace_utils

import pretty_markdown

class TrimNonBreakingWhitespaceCommand(pretty_markdown.PrettyMarkdownCommand):
    def modify(self, text):
        '''Trims non-breaking whitespace from all lines.'''

        return whitespace_utils.trim_nonbreaking_whitespace(text)
