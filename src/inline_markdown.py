import re

from textnode import TextNode,TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
        else:
            sections = old_node.text.split(delimiter)
            if len(sections) % 2 == 0:
                raise ValueError("invalid markdown, formatted section not closed")
            split_nodes = []
            for i in range(len(sections)):
                if sections[i] == "":
                    continue
                if i % 2 == 0:
                    split_nodes.append(TextNode(sections[i], TextType.TEXT))
                else:
                    split_nodes.append(TextNode(sections[i], text_type))
            new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes_link(old_nodes : list[TextNode]):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
        else:
            remainder_text = old_node.text
            markdown_links = extract_markdown_links(remainder_text)
            if len(markdown_links) == 0:
                new_nodes.append(old_node)
            else:
                sections = []
                for content, href in markdown_links:
                    markdown_link = f"[{content}]({href})"
                    sections = remainder_text.split(markdown_link, 1)
                    if len(sections) != 2:
                        raise ValueError("invalid markdown, link section not closed")
                    if sections[0] != "":
                        new_nodes.append(TextNode(sections[0], TextType.TEXT))
                    new_nodes.append(TextNode(content, TextType.LINK, href))
                    remainder_text = sections[1]
                if remainder_text != "":
                    new_nodes.append(TextNode(remainder_text), TextType.TEXT)                    
    return new_nodes


def split_nodes_image(old_nodes : list[TextNode]):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
        else:
            remainder_text = old_node.text
            markdown_links = extract_markdown_images(remainder_text)
            if len(markdown_links) == 0:
                new_nodes.append(old_node)
            else:
                sections = []
                for alt, src in markdown_links:
                    markdown_link = f"![{alt}]({src})"
                    sections = remainder_text.split(markdown_link, 1)
                    if len(sections) != 2:
                        raise ValueError("invalid markdown, image section not closed")
                    if sections[0] != "":
                        new_nodes.append(TextNode(sections[0], TextType.TEXT))
                    new_nodes.append(TextNode(alt, TextType.IMAGE, src))
                    remainder_text = sections[1]
                if remainder_text != "":
                    new_nodes.append(TextNode(remainder_text), TextType.TEXT)                    
    return new_nodes