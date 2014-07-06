from utils import horizontal_rule_utils

import pretty_markdown

class ConvertHorizontalRulesCommand(pretty_markdown.PrettyMarkdownCommand):
    def modify(self, text):
        '''Converts any horizontal rule variation to the version defined in the settings file.

        A horizontal rule is defined by three or more hyphens, asterisks, or underscores with optional spaces in between.'''

        horizontal_rule = pretty_markdown.settings().get('horizontal_rule_style')
        return horizontal_rule_utils.convert_horizontal_rules(text, horizontal_rule)
