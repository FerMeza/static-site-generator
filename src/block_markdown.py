from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"

def block_to_block_type(block: str):
    if block:
        if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
            return BlockType.HEADING
        if block.startswith("```") and block.endswith("```"):
            return BlockType.CODE

        lines = block.split("\n")

        if block.startswith(">"):
            for line in lines:
                if not line.startswith(">"):
                    return BlockType.PARAGRAPH
            return BlockType.QUOTE

        # check for unordered list
        count = 0
        for line in lines:
            if line.startswith("- "):
                count += 1
            else:
                break
        
        if count == len(lines):
            return BlockType.UNORDERED_LIST

        # check for ordered list
        count = 0
        for line in lines:
            if line.startswith(f"{count + 1}. "):
                count += 1
            else:
                break

        if count == len(lines):
            return BlockType.ORDERED_LIST
        
    return BlockType.PARAGRAPH

def markdown_to_blocks(markdown):
    dirty_blocks = markdown.split("\n\n")
    clean_blocks = []
    for dirty_block in dirty_blocks:
        clean_block = dirty_block.strip()
        if clean_block != "":
            clean_blocks.append(clean_block)
    
    return clean_blocks