import os
import shutil


def copy_alL_files(src_dir: str, dst_dir: str) -> None:
    """
    Copies the files in the source folder to the destination folder.
    :param src_dir: Path as a String to the source directory.
    :param dst_dir: Path as a String to the destination directory.
    :return: None
    """
    src_files = os.listdir(src_dir)
    for file_name in src_files:
        full_file_name = os.path.join(src_dir, file_name)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, dst_dir)


def clear_directory(dir_to_clear: str) -> None:
    """
    Deletes all files from a directory.
    :param dir_to_clear: Absolute path as a String to the directory.
    :return: None
    """
    for filename in os.listdir(dir_to_clear):
        file_path = os.path.join(dir_to_clear, filename)
        try:
            # if file or directory
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
    

def check_file_extensions(dir_to_check: str, ext: str) -> bool:
    """
    Check that all files in a directory have the given extension.
    :param dir_to_check: Absolute path as a String to the directory.
    :param ext: String, the file extension to check for like "jpg"
    :return: True if all files have the given extension, false otherwise.
    """
    for filename in os.listdir(dir_to_check):
        filepath = os.path.join(dir_to_check, filename)
        name, extension = os.path.splitext(filepath)
        if not extension == ext:
            return False
    return True

