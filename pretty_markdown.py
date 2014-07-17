import sublime
import sublime_plugin

def command_names():
    """Returns a list of all command names."""

    return [
        "trim_non_breaking_whitespace",
        "fix_header_balancing",
        "convert_headers",
        "convert_bold",
        "convert_italics",
        "convert_horizontal_rules",
        "discover_missing_links",
        "fix_ordered_list_numbering",
        "alternate_unordered_list_delimiters",
        "create_hanging_list_indents",
        "format_link_reference_definitions"
    ]

def settings():
    """Retrieves the settings file."""

    return sublime.load_settings("Pretty Markdown.sublime-settings")

class PrettyMarkdownCommand(sublime_plugin.TextCommand):

    """Parent for all PrettyMarkdown commands."""

    def modify(self, text):
        return text

    def run(self, edit):
        """Runs the command.

        This method actually doesn't do anything on its own. It delegates to modify(self, text) which will be overridden by child classes.
        """

        r = sublime.Region(0, self.view.size())
        text = self.view.substr(r)

        text = self.modify(text)

        self.view.replace(edit, r, text)

    def is_enabled(self):
        """Determines whether the command is enabled.

        Due to my naming convention overlapping with Sublime Text command naming conventions, is_enabled() was defined to return True only
        for subclasses of PrettyMarkdownCommand.
        """
        return self.__class__.__name__ != 'PrettyMarkdownCommand'
