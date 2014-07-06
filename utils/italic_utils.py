import re

def convert_italics(text, character='_'):
    '''Converts any italics implementation to use the specified character.

    If no character is given, an underscore (_) is used.'''

    text = re.sub(r'(?<!\\|\*|_)(\*|_)(?!\1)([\S \t]+?)(?<!\\)\1', r'{0}\2{0}'.format(character), text)

    return text
