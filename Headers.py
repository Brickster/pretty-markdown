import sublime, sublime_plugin, re

class FixHeaderBalancingCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        '''Balances ATX style headers.'''

        r = sublime.Region(0, self.view.size())
        text = self.view.substr(r)

        text = re.sub(r'^((#+)\s.*?)(?:\s#+)?$', r'\1 \2', text, flags=re.MULTILINE)

        self.view.replace(edit, r, text)
