import re
import util_utils

LINK_REFERENCE_DEFINITION_REGEX = r'^\[(.*?)\]:\s+(.+?(?:\s+".*")?)$'
LINK_REFERENCE_REGEX = r'!?\[(.+?)\]\[(.*?)\]'


def is_link_reference_definition(text):
    """Determines whether a given string is a link reference definition."""

    return re.match(LINK_REFERENCE_DEFINITION_REGEX, text) is not None


def _format_links(links):
    """Formats a list of links."""

    pairs = [re.match(LINK_REFERENCE_DEFINITION_REGEX, cur).groups() for cur in links]
    longest = len(max([pair[0] for pair in pairs], key=len)) + 4  # 4 accounts for [, ], :, and ' '
    formatted_links = ['[{}]: '.format(definition).ljust(longest) + link for definition, link in pairs]

    return formatted_links


def format_link_reference_definitions(text):
    """Formats groups of link reference definitions so that their links all line up."""

    return util_utils.process_groups(text, is_group_member=is_link_reference_definition, process_group=_format_links)


def _create_link_definitions(link_ids, definition_pairs, default_definition='404'):

    if definition_pairs is None:
        definition_pairs = []

    if link_ids is not None:
        definition_groups_ids = [link_id for link_id, link in definition_pairs]
        missing_links = [link_id for link_id in link_ids if link_id not in definition_groups_ids]

        for missing_link in missing_links:
            definition_pairs.append((missing_link, default_definition))

    new_list = []
    for link_id, link in definition_pairs:
        link_definition = '[{}]: {}'.format(link_id, link)
        new_list.append(link_definition)

    return new_list


def discover_missing_links(text, default_definition='404'):
    """Adds empty link definitions for reference links."""

    text = text.split('\n')

    link_groups = []
    definition_groups = []
    output = []
    line_count = 0

    for line in text:

        is_link_definition = is_link_reference_definition(line)

        if is_link_definition and len(text) - 1 == line_count:

            link_id, link = re.match(LINK_REFERENCE_DEFINITION_REGEX, line).groups()
            definition_groups.append((link_id, link))

            output.extend(_create_link_definitions(link_groups, definition_groups, default_definition))

        elif is_link_definition:

            # we've found a definition, put it in the list
            link_id, link = re.match(LINK_REFERENCE_DEFINITION_REGEX, line).groups()
            definition_groups.append((link_id, link))

        elif definition_groups:

            output.extend(_create_link_definitions(link_groups, definition_groups, default_definition))
            output.append(line)

            link_groups = []
            definition_groups = []

        else:

            # we're not in a link group and it's not a link, so search for links
            links = [m.groups() for m in re.finditer(LINK_REFERENCE_REGEX, line) if m is not None]
            for (link_text, link_id) in links:
                if link_id == '':
                    link_id = link_text  # it's implicit so set the ID to the text value
                link_groups.append(link_id)

            output.append(line)

            if len(text) - 1 == line_count and link_groups:
                output.append('')
                for link in link_groups:
                    output.append('[{}]: {}'.format(link, default_definition))

        line_count += 1

    text = '\n'.join(output)

    return text
