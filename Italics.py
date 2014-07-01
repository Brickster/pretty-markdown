import sublime, sublime_plugin, re
from . import pretty_markdown

class ConvertItalicsCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        '''Converts any italics implementation into the one defined in the settings.'''

        r = sublime.Region(0, self.view.size())
        text = self.view.substr(r)

        italics_character = pretty_markdown.settings().get('italics_character')

        text = re.sub(r'(?<!\\|\*|_)(\*|_)(?!\1)([\S \t]+?)(?<!\\)\1', r'{0}\2{0}'.format(italics_character), text)

        self.view.replace(edit, r, text)
