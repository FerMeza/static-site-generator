from markdown_to_hmtl_node import markdown_to_html_node

def main():
    md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

    node = markdown_to_html_node(md)
    html = node.to_html()
    print(repr(html))

if __name__ == "__main__":
    main()