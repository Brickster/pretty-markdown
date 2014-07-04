import re

def fix_header_balancing(text):
    '''Balances headers.'''

    text = re.sub(r'^((#+)\s.*?)(?:\s#+)?$', r'\1 \2', text, flags=re.MULTILINE)

    return text
