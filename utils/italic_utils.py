import re

valid_characters = ['*', "_"]

def convert_italics(text, character='_'):
    '''Converts any italics implementation to use the specified character.

    If no character is given, an underscore (_) is used.'''

    assert character in valid_characters, "character must be one of {}".format(valid_characters)

    text = re.sub(r'(?<!\\|\*|_)(\*|_)(?!\1)(\S(?:[\S \t]+?\S)?)(?<!\\)\1', r'{0}\2{0}'.format(character), text)

    return text
