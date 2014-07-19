import re
import util_utils

LIST_ITEM_PATTERN = re.compile(r'^((?:\s{4}|\t)*)[-*+](\s+.*$)')

def _is_unordered_list_item(text):
    """Determines if a string is an unordered list item."""

    return text is not None and LIST_ITEM_PATTERN.match(text) is not None

def _tabCount(text):
    """Determines tab count."""

    count = 0
    count += text.count('\t')
    count += int(text.count(' ') / 4)

    return count

def _format_unordered_list(list, delimiters = ['-', '+', '*']):
    """Alternates the delimiters in unordered lists according to their indentation."""

    output = []

    for item in list:

        tab_count = _tabCount(LIST_ITEM_PATTERN.match(item).group(1))
        delimiter_index = tab_count % len(delimiters)
        delimiter = delimiters[delimiter_index]

        new_item = LIST_ITEM_PATTERN.sub(r'\1{}\2'.format(delimiter), item)
        output.append(new_item)

    return output

def alternate_unordered_list_delimiters(text, delimiters = ['-', '+', '*']):
    """Alternates the delimiters in unordered lists according to their indentation."""

    process_parameters = {'delimiters': delimiters}
    return util_utils.process_groups(text,
                                     is_group_member=_is_unordered_list_item,
                                     process_group=_format_unordered_list,
                                     process_group_parameters=process_parameters)
