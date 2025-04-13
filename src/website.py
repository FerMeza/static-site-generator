from errno import ENOENT
from os import listdir, mkdir, path, strerror
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