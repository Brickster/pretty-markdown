def process_groups(text, is_group_member, process_group, is_group_member_parameters = {}, process_group_parameters = {}):
    """Processes groups with a block of text.

    Determining whether a line in the input text is a group member and processing said groups is delegated to the supplied functions.
    """

    text = text.split('\n')
    group = []
    output = []

    count = 0

    for line in text:

        is_member = is_group_member(line, **is_group_member_parameters)
        if not is_member and group:

            processed_group = process_group(group, **process_group_parameters)

            output += processed_group
            output.append(line)
            group = []

        elif is_member and len(text) - 1 == count:

            group.append(line)
            output += process_group(group, **process_group_parameters)

        elif is_member:
            group.append(line)
        else:
            output.append(line)

        count += 1

    text = '\n'.join(output)

    return text
