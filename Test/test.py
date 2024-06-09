import os
import unittest
from testUtils import copy_alL_files, check_file_extensions
from utils import change_files_to_jpg


class TestUtilFunctions(unittest.TestCase):
    def test_change_files_to_jpg(self):
        original_dir_path = os.path.join(os.getcwd(), "TestChangeFilesToJPG", "Original")
        test_dir_path = os.path.join(os.getcwd(), "TestChangeFilesToJPG", "Test")
        copy_alL_files(original_dir_path, test_dir_path)
        change_files_to_jpg(test_dir_path)
        self.assertTrue(check_file_extensions(test_dir_path, "jpg"))




if __name__=="main":
    unittest.main()