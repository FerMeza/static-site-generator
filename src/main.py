from os import path
from pathlib import Path
from website import copy_static, generate_page

def main():
    root_folder = Path(__file__).parent.parent
    static_folder = path.join(root_folder, "static")
    public_folder = path.join(root_folder, "public")
    content_folder = path.join(root_folder, "content")
    # Side effect! Deletes dest folder content before >:D
    copy_static(static_folder, public_folder)
    content_md = path.join(content_folder, "index.md")
    template_html = path.join(root_folder, "template.html")
    index_html = path.join(public_folder, "index.html")
    generate_page(content_md, template_html, index_html)

if __name__ == "__main__":
    main()