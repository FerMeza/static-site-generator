from errno import ENOENT
from markdown_to_hmtl_node import markdown_to_html_node
from os import listdir, mkdir, makedirs, path, strerror
from shutil import rmtree
from shutil import copy as scopy

def copy_static(src: str, dest: str) -> None:
    if not path.exists(src):
        raise FileNotFoundError(
            ENOENT,
            strerror(ENOENT),
            src
        )
    # clean dest directory
    if path.exists(dest):
        rmtree(dest)
    mkdir(dest)
    copy_static_recursive(src,dest)

def copy_static_recursive(src : str, dest: str) -> None:
    # and directories !
    src_files = listdir(src)
    for file_or_dir in src_files:
        full_path = path.join(src, file_or_dir)
        if path.isfile(full_path):
            scopy(full_path, dest)
        elif path.isdir(full_path):
            full_dest = path.join(dest, file_or_dir)
            mkdir(full_dest)
            copy_static_recursive(full_path, full_dest)

def extract_title(markdown: str) -> None:
    # Asumming valid and not weird markdown! (si the title is at first!)
    clean_markdown = markdown.lstrip(" \n")
    if not clean_markdown.startswith("# "):
        raise ValueError("Invalid markdown, missing title!")
    title = clean_markdown.split("\n",1)[0].rstrip(" \n")
    if len(title) <= 2:
        raise ValueError("Missing title!")
    return title[2:]

def generate_page(from_path: str, 
                  template_path: str, 
                  dest_path: str) -> None:
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, 'r') as markdown_file, \
        open(template_path, 'r') as template_file:
        markdown_str = markdown_file.read()
        template_str = template_file.read()
        html_str = markdown_to_html_node(markdown_str).to_html()
        title = extract_title(markdown_str)
        webpage = template_str.replace("{{ Title }}", title). \
            replace("{{ Content }}", html_str)
        folder_dest = path.dirname(dest_path)
        if not path.exists(folder_dest):
            makedirs(folder_dest)
        with open(dest_path, "w") as file:
            file.write(webpage)