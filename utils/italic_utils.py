import re

VALID_CHARACTERS = ['*', "_"]


def convert_italics(text, character='_'):
    """Converts any italics implementation to use the specified character.

    If no character is given, an underscore (_) is used.
    """

    assert character in VALID_CHARACTERS, 'character must be one of {}'.format(VALID_CHARACTERS)

    p = re.compile(r'(?<![*_])((?:\*{2}|_{2})?)([*_])([*_]*)((?<!(?<![*_])[*_][*_])[^\s*_](?:[\S \t]+?\S)?)\3\2\1')
    text = p.sub(r'\1{0}\3\4\3{0}\1'.format(character), text)

    return text
