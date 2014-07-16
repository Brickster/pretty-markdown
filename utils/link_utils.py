import re

LINK_REFERENCE_DEFINITION_PATTERN = re.compile(r'^\[.*\]:\s+.+?(\s+".*")?$')

def is_link_reference_definition(text):
    """Determines whether a given string is a link reference definition."""

    return LINK_REFERENCE_DEFINITION_PATTERN.match(text) is not None

def format_link_reference_definitions(text):
    """Formats groups of link reference definitions so that their links all line up."""

    return text # do nothing for now
