from utils import italic_utils

import pretty_markdown

class ConvertItalicsCommand(pretty_markdown.PrettyMarkdownCommand):
    def modify(self, text):
        """Converts any italics implementation into the one defined in the settings."""

        italics_character = pretty_markdown.settings().get('italics_character')
        return italic_utils.convert_italics(text, italics_character)
