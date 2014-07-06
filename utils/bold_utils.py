import re

valid_characters = ['*', "_"]

def convert_bolds(text, character='*'):
    '''Converts any bold implementation to use the specified character.

    If no characeter is supplied, an asterisk (*) is used.'''

    assert character in valid_characters, "character must be one of {}".format(valid_characters)

    text = re.sub(r'(?<!\\)(\*{2}|_{2})(\S(?:[\S \t]+?\S)?)\1', r'{0}{0}\2{0}{0}'.format(character), text)

    return text
