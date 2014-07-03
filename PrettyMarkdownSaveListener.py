from . import pretty_markdown

import sublime_plugin, os.path

# TODO: make each file have it's own listener

class PrettyMarkdownSaveListenerCommand(sublime_plugin.EventListener):
    def on_pre_save(self, view):
        '''Runs Pretty Markdown pre-save actions'''

        extension = os.path.splitext(view.file_name())[1][1:]
        if extension in pretty_markdown.settings().get('format_files_with_extension'):
            if (pretty_markdown.settings().get("format_on_save")):
                view.run_command("format_markdown")
