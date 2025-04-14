from sys import argv
from website import copy_static, generate_pages_recursive

def main():
    basepath = "/"
    if len(argv) > 1:
        basepath = argv[1]
        print(basepath)
    static_folder = "./static"
    docs_folder = "./docs"
    content_folder = "./content"
    template_html = "./template.html"
    # Side effect! Deletes dest folder content before!!!
    copy_static(static_folder, docs_folder)
    generate_pages_recursive(content_folder, template_html, docs_folder, basepath)

if __name__ == "__main__":
    main()