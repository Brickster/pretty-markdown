import re

LINK_REFERENCE_DEFINITION_PATTERN = re.compile(r'^\[(.*)\]:\s+(.+?(?:\s+".*")?$)')

def is_link_reference_definition(text):
    """Determines whether a given string is a link reference definition."""

    return LINK_REFERENCE_DEFINITION_PATTERN.match(text) is not None

def _format_links(links):
    """Formats a list of links."""

    pairs = [LINK_REFERENCE_DEFINITION_PATTERN.match(cur).groups() for cur in links]
    longest = len(max([pair[0] for pair in pairs], key=len)) + 4 # 4 accounts for [, ], :, and ' '
    formatted_links = ['[{}]: '.format(definition).ljust(longest) + link for definition, link in pairs]

    return formatted_links

def format_link_reference_definitions(text):
    """Formats groups of link reference definitions so that their links all line up."""

    text = text.split('\n')
    link_group = []
    output = []

    for line in text:

        is_link_definition = is_link_reference_definition(line)
        if not is_link_definition and link_group:

            formatted_links = _format_links(link_group)

            output += formatted_links
            output.append(line)
            link_group = []

        elif is_link_definition and text.index(line) == len(text) - 1:

            link_group.append(line)
            output += _format_links(link_group)

        elif is_link_definition:
            link_group.append(line)
        else:
            output.append(line)

    text = '\n'.join(output)

    return text
