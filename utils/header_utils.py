import re

SETEXT_HEADER_PATTERN = re.compile(r'^(?:={3,}|-{3,})$')

BALANCED = 'balanced'
UNBALANCED = 'unbalanced'


def is_setext_header(text):
    """Determines if text is a setext type header line."""

    return text is not None and SETEXT_HEADER_PATTERN.match(text) is not None


def fix_header_balancing(text, balancing=BALANCED):
    """Balances headers."""

    if balancing == BALANCED:

        # balance atx headers
        text = re.sub(r'^((#+)\s.*?)(?:\s#+)?$', r'\1 \2', text, flags=re.MULTILINE)

        # balance setext headers
        prev = None
        output = []

        for line in text.split('\n'):

            if prev is not None and is_setext_header(line) and len(prev.strip()) != 0:
                line = line[0] * len(prev)

            output.append(line)
            prev = line

        text = '\n'.join(output)
    else:

        # unbalance atx headers
        text = re.sub(r'^((#+)\s.*?)(?:\s#+)?$', r'\1', text, flags=re.MULTILINE)

    return text
