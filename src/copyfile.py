import os
import shutil


def copy_files(from_dir, to_dir):
    if not os.path.exists(to_dir):
        os.mkdir(to_dir)

    items_in_dir = os.listdir(from_dir)
    for item in items_in_dir:
        from_path = os.path.join(from_dir, item)
        to_path = os.path.join(to_dir, item)
        if os.path.isfile(from_path):
            shutil.copy(from_path, to_path)
        else:
            copy_files(from_path, to_path)
