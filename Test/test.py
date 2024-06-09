import os
import unittest
from testUtils import copy_alL_files, check_file_extensions, clear_directory
from utils import change_files_to_jpg, get_files_to_dir

original_dir_path = os.path.join(os.getcwd(), "TestChangeFilesToJPG", "Original")
test_dir_path = os.path.join(os.getcwd(), "TestChangeFilesToJPG", "Test")


class TestUtilFunctions(unittest.TestCase):
    def test_change_files_to_jpg(self):
        clear_directory(test_dir_path)
        copy_alL_files(original_dir_path, test_dir_path)
        change_files_to_jpg(test_dir_path)
        self.assertTrue(check_file_extensions(test_dir_path, "jpg"))

    def test_copy_files_min_size(self):
        clear_directory(test_dir_path)
        min_file_size = 580000
        get_files_to_dir(original_dir_path, test_dir_path, min_file_size)

        file_list = os.listdir(test_dir_path)

        self.assertEqual(len(file_list), 2)

        for f in file_list:
            self.assertTrue(os.path.getsize(f) >= min_file_size)







if __name__=="main":
    unittest.main()