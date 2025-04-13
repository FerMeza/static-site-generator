from os import path
from pathlib import Path
from website import copy_static

def main():
    root_folder = Path(__file__).parent.parent
    src_folder = path.join(root_folder, "static")
    dest_folder = path.join(root_folder, "public")
    copy_static(src_folder, dest_folder)

if __name__ == "__main__":
    main()