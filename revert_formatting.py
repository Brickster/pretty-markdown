from os.path import exists

import sublime
import sublime_plugin


class RevertFormattingCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        """Reverts the text to before the last formatting."""

        backup_directory = sublime.packages_path() + '/PrettyMarkdown/backup'
        backup_path = backup_directory + '/save.backup'

        if exists(backup_path):
            with open(backup_path, 'r') as f:
                text = f.read()

            r = sublime.Region(0, self.view.size())
            self.view.replace(edit, r, text)
