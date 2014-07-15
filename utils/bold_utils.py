import re

VALID_CHARACTERS = ['*', "_"]

def convert_bolds(text, character='*'):
    """Converts any bold implementation to use the specified character.

    If no characeter is supplied, an asterisk (*) is used.
    """

    assert character in VALID_CHARACTERS, "character must be one of {}".format(VALID_CHARACTERS)

    text = re.sub(r'(?<!\\)(\*{2}|_{2})(\S(?:[\S \t]+\S)?)\1', r'{0}{0}\2{0}{0}'.format(character), text)

    return text
