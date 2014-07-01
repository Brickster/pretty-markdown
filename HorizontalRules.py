import sublime, sublime_plugin, re
from . import pretty_markdown

class ConvertHorizontalRulesCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        '''Converts any horizontal rule variation to the version defined in the settings file.

        A horizontal rule is defined by three or more hyphens, asterisks, or underscores with optional spaces in between.'''

        horizontal_rule = pretty_markdown.settings().get('horizontal_rule_style')
        # TODO: validate rule style

        r = sublime.Region(0, self.view.size())
        text = self.view.substr(r)

        text = re.sub(r'^[\*-_](?:[^\S\r\n]?[\*-_]){2,}$', horizontal_rule, text, flags=re.MULTILINE)

        self.view.replace(edit, r, text)
