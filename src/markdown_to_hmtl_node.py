from block_markdown import markdown_to_blocks, BlockType, block_to_block_type
from functools import reduce
from htmlnode import LeafNode, ParentNode
from inline_markdown import text_to_textnodes
from textnode import TextNode, TextType, text_node_to_html_node

def markdown_to_html_node(markdown: str) -> ParentNode:
    blocks = markdown_to_blocks(markdown)
    children_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        html_node = block_to_html_node(block, block_type)
        children_nodes.append(html_node)
    return ParentNode(
        "div",
        children_nodes
    )

def block_to_html_node(block: str, block_type: BlockType) -> ParentNode:
    match block_type:
        case BlockType.CODE:
            text = block.strip("```").lstrip("\n")
            print(repr(text.splitlines()))
            text_node = TextNode(text, TextType.CODE)
            code = text_node_to_html_node(text_node)
            return ParentNode("pre", [code])
        case BlockType.HEADING:
            splited = block.split(" ", 1)
            return ParentNode(
                f"h{len(splited[0])}",
                text_to_children(splited[1]),
            )
        case BlockType.ORDERED_LIST:
            parent = ParentNode("ol",[])
            for line in block.split("\n"):
                text = line.split(" ", 1)[1]
                parent.children.append(
                    ParentNode(
                        "li",
                        text_to_children(text))
                )
            return parent
        case BlockType.PARAGRAPH:
            return ParentNode(
                "p",
                text_to_children(block),
            )
        case BlockType.QUOTE:
            text = reduce(lambda x, y: x + y + "\n", map(lambda line : line[1:], block.splitlines()), "")
            children = text_to_children(text[:-1])
            parent = ParentNode("blockquote", children)
            return parent
        case BlockType.UNORDERED_LIST:
            parent = ParentNode("ul",[])
            for line in block.split("\n"):
                text = line.split(" ", 1)[1]
                parent.children.append(
                    ParentNode(
                        "li",
                        text_to_children(text))
                )
            return parent
        case _:
            raise ValueError("Not a valid Block Type")

# I'm asumming nothing can be nested!, so it's all inline!
def text_to_children(text: str) -> list[LeafNode]:
    text_nodes = text_to_textnodes(" ".join(text.split()))
    children = list(map(lambda text_node : text_node_to_html_node(text_node), text_nodes))
    return children