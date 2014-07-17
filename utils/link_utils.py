import re
import util_utils

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

    return util_utils.process_groups(text, is_group_member=is_link_reference_definition, process_group=_format_links)
