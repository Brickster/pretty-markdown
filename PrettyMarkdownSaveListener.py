import sublime_plugin
from . import pretty_markdown

# TODO: make each file have it's own listener

class PrettyMarkdownSaveListenerCommand(sublime_plugin.EventListener):
    def on_pre_save(self, view):
        '''Runs Pretty Markdown pre-save actions'''

        extension = pretty_markdown.file_extension(view.file_name())
        if extension in pretty_markdown.settings().get('format_files_with_extension'):
            if (pretty_markdown.settings().get("format_on_save")):
                view.run_command("format_markdown")
