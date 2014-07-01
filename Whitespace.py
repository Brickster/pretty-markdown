import sublime, sublime_plugin, re

class TrimNonBreakingWhitespaceCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        '''Trims non-breaking whitespace from all lines.'''

        r = sublime.Region(0, self.view.size())
        text = self.view.substr(r)

        text = text.splitlines()
        text = [line.rstrip() if len(line.rstrip()) != len(line) - 2 else line for line in text]
        text = '\n'.join(text)

        self.view.replace(edit, r, text)
