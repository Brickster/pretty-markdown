import re

def trim_nonbreaking_whitespace(text):
    """Trims non-breaking whitespace from the end of each line in the given text.

    Non-breaking whitespace refers to the markdown syntax of places two spaces at the end of a line to signify a break.
    """

    pattern = re.compile(r'^.*\S  $')

    text = text.split('\n') # use split(...) since splitlines() doesn't keep trailing blank lines if any are present

    text = [line if pattern.match(line) else line.rstrip() for line in text]
    text = '\n'.join(text)

    return text
