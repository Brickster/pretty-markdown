from . import pretty_markdown

import re

class ConvertHorizontalRulesCommand(pretty_markdown.PrettyMarkdownCommand):
    def modify(self, text):
        '''Converts any horizontal rule variation to the version defined in the settings file.

        A horizontal rule is defined by three or more hyphens, asterisks, or underscores with optional spaces in between.'''

        horizontal_rule = pretty_markdown.settings().get('horizontal_rule_style')
        text = re.sub(r'^[\*-_](?:[^\S\r\n]?[\*-_]){2,}$', horizontal_rule, text, flags=re.MULTILINE)

        return text
