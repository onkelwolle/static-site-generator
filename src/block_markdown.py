def markdown_to_blocks(markdown):
    list_of_blocks = markdown.split("\n\n")
    stripped_list_of_blocks = []
    for item in list_of_blocks:
        if item.strip() != "":
            stripped_list_of_blocks.append(item.strip())
    return stripped_list_of_blocks
