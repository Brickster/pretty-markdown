import re

horizontal_rule_pattern = re.compile(r'^[*\-_](?:[^\S\r\n]?[*\-_]){2,}$', flags=re.MULTILINE)

def is_valid_horizontal_rule(horizontal_rule):
    '''Determines if a given horizontal rule is valid.'''

    return horizontal_rule_pattern.match(horizontal_rule) is not None

def convert_horizontal_rules(text, horizontal_rule='---'):
    '''Converts any horizontal rule variation to a given version.

    A horizontal rule is defined by three or more hyphens, asterisks, or underscores with optional spaces in between. If one isn't supplied, "---"
    is used.'''

    assert is_valid_horizontal_rule(horizontal_rule), 'A horizontal rule is defined by three or more hyphens, asterisks, or underscores with optional spaces in between.'

    text = horizontal_rule_pattern.sub(horizontal_rule, text)

    return text


