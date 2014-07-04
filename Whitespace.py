import pretty_markdown
import re

class TrimNonBreakingWhitespaceCommand(pretty_markdown.PrettyMarkdownCommand):
    def modify(self, text):
        '''Trims non-breaking whitespace from all lines.'''

        text = text.splitlines()
        text = [line.rstrip() if len(line.rstrip()) != len(line) - 2 else line for line in text]
        text = '\n'.join(text)

        return text
