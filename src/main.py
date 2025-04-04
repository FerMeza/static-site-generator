from textnode import TextType, TextNode
from inline_markdown import text_to_textnodes

def main():
    text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    print(text_to_textnodes(text))

if __name__ == "__main__":
    main()