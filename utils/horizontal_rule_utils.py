import re

def convert_horizontal_rules(text, horizontal_rule='---'):
    '''Converts any horizontal rule variation to a given version.

    A horizontal rule is defined by three or more hyphens, asterisks, or underscores with optional spaces in between. If one isn't supplied, "---"
    is used.'''

    rule_pattern = re.compile(r'^[\*-_](?:[^\S\r\n]?[\*-_]){2,}$', flags=re.MULTILINE)

    assert rule_pattern.match(horizontal_rule) is not None, 'A horizontal rule is defined by three or more hyphens, asterisks, or underscores with optional spaces in between.'

    text = rule_pattern.sub(horizontal_rule, text)

    return text
