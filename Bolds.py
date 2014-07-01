import sublime, sublime_plugin, re
from . import pretty_markdown

class ConvertBoldCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        '''Converts any bold implementation into the one defined in the settings.'''

        r = sublime.Region(0, self.view.size())
        text = self.view.substr(r)

        bold_character = pretty_markdown.settings().get('bold_character')

        text = re.sub(r'(?<!\\)(\*{2}|_{2})([\S \t]+?)\1', r'{0}{0}\2{0}{0}'.format(bold_character), text)

        self.view.replace(edit, r, text)
