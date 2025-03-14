import unittest
import os
import sys
from codebase_to_text import CodebaseToText
import shutil


class TestCodebaseToText(unittest.TestCase):
    def setUp(self):
        # Create a temporary folder with some test files
        self.test_folder_path = "test_folder"
        os.makedirs(self.test_folder_path, exist_ok=True)
        with open(os.path.join(self.test_folder_path, "test_file1.txt"), "w") as file:
            file.write("Test file 1 content")
        with open(os.path.join(self.test_folder_path, "test_file2.txt"), "w") as file:
            file.write("Test file 2 content")

    def test_get_text(self):
        code_to_text = CodebaseToText(input_path=self.test_folder_path, output_path="output.txt", output_type="txt")
        text = code_to_text.get_text()
        expected_text = (
            f"Folder Structure\n--------------------------------------------------\n{self.test_folder_path}/\n    test_file1.txt\n    "
            f"test_file2.txt\n\n\nFile Contents\n--------------------------------------------------\n\n\n"
            f"{os.path.join(self.test_folder_path,'test_file1.txt')}\nFile type: .txt\nTest file 1 content\n\n"
            f"--------------------------------------------------\nFile End\n--------------------------------------------------\n\n\n"
            f"{os.path.join(self.test_folder_path,'test_file2.txt')}\nFile type: .txt\nTest file 2 content\n\n"
            f"--------------------------------------------------\nFile End\n--------------------------------------------------\n"
        )
        self.assertEqual(text, expected_text)

    def test_exclude_types(self):
        code_to_text = CodebaseToText(
            input_path=self.test_folder_path,
            output_path="output.txt",
            output_type="txt",
            verbose=False,
            exclude_hidden=False,
            exclude_types=".txt",
        )
        text = code_to_text.get_text()
        print(text)
        self.assertNotIn("Test file 1 content", text)
        self.assertNotIn("Test file 2 content", text)

    def tearDown(self):
        # Clean up temporary folder
        if os.path.exists(self.test_folder_path):
            shutil.rmtree(self.test_folder_path)


if __name__ == "__main__":
    print(sys.path)
    unittest.main()
