import sublime

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
