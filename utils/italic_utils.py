import re

VALID_CHARACTERS = ['*', "_"]

def convert_italics(text, character='_'):
    """Converts any italics implementation to use the specified character.

    If no character is given, an underscore (_) is used.
    """

    assert character in VALID_CHARACTERS, 'character must be one of {}'.format(VALID_CHARACTERS)

    if character == '*':
        other_char = '_'
    else:
        other_char = '\*' # we don't want the asterisk interpreted as a quantifier

    p = re.compile(r'(?<![*_]{1})([*_]{2})?(' + other_char + r')([^\s*_](?:[\S \t]+?\S)?)(?<!\\)\2', flags=re.MULTILINE)
    while p.search(text) is not None:
        m = p.search(text)
        if m.group(1) is None:
            text = p.sub(r'{0}\3{0}'.format(character), text, count=1)
        else:
            text = p.sub(r'\1{0}\3{0}'.format(character), text, count=1)

    return text
