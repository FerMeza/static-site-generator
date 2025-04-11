def markdown_to_blocks(markdown):
    dirty_blocks = markdown.split("\n\n")
    clean_blocks = []
    for dirty_block in dirty_blocks:
        clean_block = dirty_block.strip()
        if clean_block != "":
            clean_blocks.append(clean_block)
    
    return clean_blocks