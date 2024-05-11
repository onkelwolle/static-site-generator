import os
import shutil

from copyfile import copy_files
from generate_page import generate_pages_recursive

dir_path_static = "./static"
dir_path_public = "./public"

content_path = "./content"
template_path = "./template.html"
target_path = "./public"


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)
    copy_files(dir_path_static, dir_path_public)

    generate_pages_recursive(content_path, template_path, target_path)


if __name__ == '__main__':
    main()
