from os import path
from pathlib import Path
from website import copy_static, generate_pages_recursive

def main():
    root_folder = Path(__file__).parent.parent
    static_folder = path.join(root_folder, "static")
    public_folder = path.join(root_folder, "public")
    content_folder = path.join(root_folder, "content")
    # Side effect! Deletes dest folder content before >:D
    copy_static(static_folder, public_folder)
    template_html = path.join(root_folder, "template.html")
    generate_pages_recursive(content_folder, template_html, public_folder)

if __name__ == "__main__":
    main()