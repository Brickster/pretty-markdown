import re
import util_utils

UNORDERED_LIST_ITEM_PATTERN = re.compile(r'^((?:\s{4}|\t)*)[-*+](\s+.*$)')
ORDERED_LIST_ITEM_PATTERN = re.compile(r'^((?:\s{4}|\t)*)\d+(\.\s+.*$)')

def _is_unordered_list_item(text):
    """Determines if a string is an unordered list item."""

    return text is not None and (UNORDERED_LIST_ITEM_PATTERN.match(text) is not None or len(text.strip()) == 0)

def _tab_count(text):
    """Determines tab count."""

    count = 0

    if text is not None:
        count += text.count('\t')
        count += int(text.count(' ') / 4)

    return count

def _format_unordered_list(list, delimiters = ['-', '+', '*']):
    """Alternates the delimiters in unordered lists according to their indentation."""

    output = []

    for item in list:

        if len(item.strip()) == 0:
            output.append(item)
        else:
            tab_count = _tab_count(UNORDERED_LIST_ITEM_PATTERN.match(item).group(1))
            delimiter_index = tab_count % len(delimiters)
            delimiter = delimiters[delimiter_index]

            new_item = UNORDERED_LIST_ITEM_PATTERN.sub(r'\1{}\2'.format(delimiter), item)
            output.append(new_item)

    return output

def alternate_unordered_list_delimiters(text, delimiters = ['-', '+', '*']):
    """Alternates the delimiters in unordered lists according to their indentation."""

    process_parameters = {'delimiters': delimiters}
    return util_utils.process_groups(text,
                                     is_group_member=_is_unordered_list_item,
                                     process_group=_format_unordered_list,
                                     process_group_parameters=process_parameters)

def _is_ordered_list_item(text):
    """Determines if a string is an ordered list item."""

    return text is not None and (ORDERED_LIST_ITEM_PATTERN.match(text) is not None or len(text.strip()) == 0)

def _format_ordered_list(list):
    """Fixes the number for ordered lists."""

    output = []
    counts = [1]

    for item in list:

        if len(item.strip()) == 0:
            output.append(item)
        else:
            tab_count = _tab_count(ORDERED_LIST_ITEM_PATTERN.match(item).group(1))
            if tab_count == len(counts):
                # add new one level
                counts.append(1)
            elif tab_count < len(counts) - 1:
                # remove all greater tab counts
                counts = counts[:tab_count + 1]

            count = counts[tab_count]

            new_item = ORDERED_LIST_ITEM_PATTERN.sub(r'\g<1>{}\g<2>'.format(count), item) # explicit group definition to not be confused with digit
            output.append(new_item)
        
            count += 1
            counts[tab_count] = count

    return output

def fix_ordered_list_numbering(text):
    """Fixes the number for ordered lists."""

    return util_utils.process_groups(text, is_group_member=_is_ordered_list_item, process_group=_format_ordered_list)
