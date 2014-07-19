from utils import header_utils

import re

HORIZONTAL_RULE_PATTERN = re.compile(r'^[*\-_](?:[^\S\r\n]?[*\-_]){2,}$', flags=re.MULTILINE)

def is_valid_horizontal_rule(horizontal_rule):
    """Determines if a given horizontal rule is valid."""

    return HORIZONTAL_RULE_PATTERN.match(horizontal_rule) is not None

def convert_horizontal_rules(text, horizontal_rule='---'):
    """Converts any horizontal rule variation to a given version.

    A horizontal rule is defined by three or more hyphens, asterisks, or underscores with optional spaces in between. If one isn't supplied, '---'
    is used.
    """

    assert is_valid_horizontal_rule(horizontal_rule), 'A horizontal rule is defined by three or more hyphens, asterisks, or underscores with optional spaces in between.'

    text = text.split('\n')
    prev = text[0]

    # convert prev if it's a horizontal rule
    prev = HORIZONTAL_RULE_PATTERN.sub(horizontal_rule, prev)

    result = [prev]
    for cur in text[1:]:
        # the current line can only be a horizontal rule if the previous line is blank or a rule itself
        if (len(prev.strip()) == 0 or header_utils.is_setext_header(prev) or HORIZONTAL_RULE_PATTERN.match(prev) is not None):
            cur = HORIZONTAL_RULE_PATTERN.sub(horizontal_rule, cur)

        result.append(cur)
        prev = cur

    result = '\n'.join(result)

    return result
