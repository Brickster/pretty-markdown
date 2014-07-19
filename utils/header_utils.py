import re

SETEXT_HEADER_PATTERN = re.compile(r'^(?:={3,}|-{3,})$')

def is_setext_header(text):
    """Determines if text is a setext type header line."""

    return text is not None and SETEXT_HEADER_PATTERN.match(text) is not None


def fix_header_balancing(text):
    """Balances headers."""

    text = re.sub(r'^((#+)\s.*?)(?:\s#+)?$', r'\1 \2', text, flags=re.MULTILINE)

    return text
