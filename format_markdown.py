import pretty_markdown
import sublime_plugin


class FormatMarkdownCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        """Runs all formatting functions."""

        [self.view.run_command(function) for function in pretty_markdown.command_names() if pretty_markdown.settings().get(function)]
