import re

def convert_bolds(text, character='*'):
    '''Converts any bold implementation into the one defined in the settings.'''

    text = re.sub(r'(?<!\\)(\*{2}|_{2})([\S \t]+?)\1', r'{0}{0}\2{0}{0}'.format(character), text)

    return text
