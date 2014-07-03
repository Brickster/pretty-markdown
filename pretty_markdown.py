import sublime, sublime_plugin

def file_extension(path):
    '''Returns the file extension of the file at a given path. If the path isn't for a file, or it doesn't have one, None is returned.'''

    index = path.rfind('.')
    if index != -1:
        return path[index + 1:]
    return None

def command_names():
    '''Returns a list of all command names.'''

    # TODO: rather than have to keep this list in sync with the settings file, make them discoverable.
    return [
        "trim_non_breaking_whitespace",
        "fix_header_balancing",
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
    '''Retrieves the settings file.'''

    return sublime.load_settings("Pretty Markdown.sublime-settings")

class PrettyMarkdownCommand(sublime_plugin.TextCommand):
    '''Parent for all PrettyMarkdown commands.

    Due to my naming convention overlapping with Sublime Text command naming conventions, is_enabled() was defined to return True only
    for subclasses of PrettyMarkdownCommand.'''

    def modify(self, text):
        return text

    def run(self, edit):
        '''Converts any bold implementation into the one defined in the settings.'''

        r = sublime.Region(0, self.view.size())
        text = self.view.substr(r)

        text = self.modify(text)

        self.view.replace(edit, r, text)

    def is_enabled(self):
        return self.__class__.__name__ != 'PrettyMarkdownCommand'
