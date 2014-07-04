import re
import pretty_markdown

class ConvertBoldCommand(pretty_markdown.PrettyMarkdownCommand):
    def modify(self, text):
        '''Converts any bold implementation into the one defined in the settings.'''

        bold_character = pretty_markdown.settings().get('bold_character')
        text = re.sub(r'(?<!\\)(\*{2}|_{2})([\S \t]+?)\1', r'{0}{0}\2{0}{0}'.format(bold_character), text)

        return text
