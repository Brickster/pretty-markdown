import re
import util_utils

LINK_REFERENCE_DEFINITION_REGEX = r'^\[(.*?)\]:\s+(.+?(?:\s+".*")?)$'
LINK_REFERENCE_REGEX = r'\[(.+?)\]\[(.*?)\]'

# TODO remove these and just use re.match, re.finditer, etc since they are cache internally anyway
LINK_REFERENCE_DEFINITION_PATTERN = re.compile(LINK_REFERENCE_DEFINITION_REGEX, flags=re.MULTILINE)
LINK_REFERENCE_PATTERN = re.compile(LINK_REFERENCE_REGEX)


def is_link_reference_definition(text):
    """Determines whether a given string is a link reference definition."""

    return re.match(LINK_REFERENCE_DEFINITION_REGEX, text) is not None


def _format_links(links):
    """Formats a list of links."""

    pairs = [LINK_REFERENCE_DEFINITION_PATTERN.match(cur).groups() for cur in links]
    longest = len(max([pair[0] for pair in pairs], key=len)) + 4  # 4 accounts for [, ], :, and ' '
    formatted_links = ['[{}]: '.format(definition).ljust(longest) + link for definition, link in pairs]

    return formatted_links


def format_link_reference_definitions(text):
    """Formats groups of link reference definitions so that their links all line up."""

    return util_utils.process_groups(text, is_group_member=is_link_reference_definition, process_group=_format_links)


def _append_missing_links(link_definitions, text, default_definition='404'):
    """Appends any missing links that appear before the link definitions."""

    link_definitions_string = '\n'.join(link_definitions)
    link_definitions_start = text.index(link_definitions_string)

    definitions = {m.group(1): m.group(2) for m in LINK_REFERENCE_DEFINITION_PATTERN.finditer(link_definitions_string)}
    links = {m.group(1): m.group(2) for m in LINK_REFERENCE_PATTERN.finditer(text) if m.start() < link_definitions_start}

    missing_links = [key for key in links if key not in definitions]

    for key in missing_links:
        new_def = '[{}]: {}'.format(key, default_definition)
        link_definitions.append(new_def)

    return link_definitions


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

    for line in text:

        is_link_definition = is_link_reference_definition(line)

        if is_link_definition and text[-1] == line:

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

            if text[-1] == line and link_groups:
                output.append('')
                for link in link_groups:
                    output.append('[{}]: {}'.format(link, default_definition))

    text = '\n'.join(output)

    return text
