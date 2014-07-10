import re

horizontal_rule_pattern = re.compile(r'^[*\-_](?:[^\S\r\n]?[*\-_]){2,}$', flags=re.MULTILINE)
setext_header_pattern = re.compile(r'^(?:={3,}|-{3,})$')

def is_valid_horizontal_rule(horizontal_rule):
    """Determines if a given horizontal rule is valid."""

    return horizontal_rule_pattern.match(horizontal_rule) is not None

def convert_horizontal_rules(text, horizontal_rule='---'):
    """Converts any horizontal rule variation to a given version.

    A horizontal rule is defined by three or more hyphens, asterisks, or underscores with optional spaces in between. If one isn't supplied, '---'
    is used.
    """

    assert is_valid_horizontal_rule(horizontal_rule), 'A horizontal rule is defined by three or more hyphens, asterisks, or underscores with optional spaces in between.'

    text = text.split('\n')
    prev = text[0]

    # convert prev if it's a horizontal rule
    prev = horizontal_rule_pattern.sub(horizontal_rule, prev)

    result = [prev]
    for cur in text[1:]:
        # the current line can only be a horizontal rule if the previous line is blank or a rule itself
        if (len(prev.strip()) == 0 or setext_header_pattern.match(prev) is not None or horizontal_rule_pattern.match(prev) is not None):
            cur = horizontal_rule_pattern.sub(horizontal_rule, cur)

        result.append(cur)
        prev = cur

    result = '\n'.join(result)

    return result
