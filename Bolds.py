from utils import bold_utils

import pretty_markdown

class ConvertBoldCommand(pretty_markdown.PrettyMarkdownCommand):
    def modify(self, text):
        """Converts any bold implementation into the one defined in the settings."""

        bold_character = pretty_markdown.settings().get('bold_character')
        return bold_utils.convert_bolds(text, bold_character)
