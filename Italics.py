from . import pretty_markdown

import re

class ConvertItalicsCommand(pretty_markdown.PrettyMarkdownCommand):
    def modify(self, text):
        '''Converts any italics implementation into the one defined in the settings.'''

        italics_character = pretty_markdown.settings().get('italics_character')
        text = re.sub(r'(?<!\\|\*|_)(\*|_)(?!\1)([\S \t]+?)(?<!\\)\1', r'{0}\2{0}'.format(italics_character), text)

        return text
