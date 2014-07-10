import re

link_reference_definition_pattern = re.compile(r'^\[.*\]:\s+.+?(\s+".*")?$')

def is_link_reference_definition(text):
    """Determines whether a given string is a link reference definition."""

    return link_reference_definition_pattern.match(text) is not None
