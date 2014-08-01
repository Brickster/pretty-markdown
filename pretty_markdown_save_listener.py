import os.path
import pretty_markdown
import sublime
import sublime_plugin


class PrettyMarkdownSaveListenerCommand(sublime_plugin.EventListener):

    def save_text(self, text):
        """Creates a backup of the text."""

        backup_directory = sublime.packages_path() + '/PrettyMarkdown/backup'
        backup_path = backup_directory + '/save.backup'

        if not os.path.exists(backup_directory):
            os.makedirs(backup_directory)

        with open(backup_path, 'w') as backup_file:
            backup_file.write(text)

    def on_pre_save(self, view):
        """Runs Pretty Markdown pre-save actions"""

        # save a copy of the file before editting
        r = sublime.Region(0, view.size())
        text = view.substr(r)
        self.save_text(text)

        extension = os.path.splitext(view.file_name())[1][1:]
        if extension in pretty_markdown.settings().get('format_files_with_extension'):
            if (pretty_markdown.settings().get("format_on_save")):
                view.run_command("format_markdown")
