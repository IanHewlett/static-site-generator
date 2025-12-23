def markdown_to_blocks(markdown):
    split_markdown = markdown.split('\n\n')
    blocks = []
    for block in split_markdown:
        if block == "":
            continue
        blocks.append(block.strip())
    return blocks
