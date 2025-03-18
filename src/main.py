from textnode import TextType, TextNode
from htmlnode import LeafNode

def main():
    my_text_node = TextNode("some link text", TextType.LINK, "https://www.boot.dev")
    print(my_text_node)
    node = LeafNode("p", "Hello, world!", {"class": "test", "id": "dont-care"})
    print(node.to_html())

main()