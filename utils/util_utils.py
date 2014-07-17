def process_groups(text, is_group_member, process_group):
    """Processes groups with a block of text.

    Determining whether a line in the input text is a group member and processing said groups is delegated to the supplied functions.
    """

    text = text.split('\n')
    group = []
    output = []

    for line in text:

        is_member = is_group_member(line)
        if not is_member and group:

            processed_group = process_group(group)

            output += processed_group
            output.append(line)
            group = []

        elif is_member and text.index(line) == len(text) - 1:

            group.append(line)
            output += process_group(group)

        elif is_member:
            group.append(line)
        else:
            output.append(line)

    text = '\n'.join(output)

    return text
