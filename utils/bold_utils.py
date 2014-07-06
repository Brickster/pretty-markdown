import re

def convert_bolds(text, character='*'):
    '''Converts any bold implementation to use the specified character.

    If no characeter is supplied, an asterisk (*) is used.'''

    text = re.sub(r'(?<!\\)(\*{2}|_{2})([\S \t]+?)\1', r'{0}{0}\2{0}{0}'.format(character), text)

    return text
