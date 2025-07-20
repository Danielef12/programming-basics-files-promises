import unittest
import os
import tempfile
from ..functions import read_file, concatenate_files, clean_dataset, save_file


class TestReadFile(unittest.TestCase):
    def test_read_file(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            with open(os.path.join(temp_dir, 'test.txt'), 'w') as f:
                f.write('test')

            with open(os.path.join(temp_dir, 'test2.csv'), 'w') as f:
                f.write('test2')

            with open(os.path.join(temp_dir, 'test3.txt'), 'w') as f:
                f.write('test3')

            result = read_file(temp_dir)
            self.assertCountEqual(result, ["test", "test3"])


class TestConcatenateFiles(unittest.TestCase):
    def test_concatenate_files(self):
        content = ["test1", "test2", "test3"]
        expected_result = "test1\ntest2\ntest3"
        result = concatenate_files(content)
        self.assertEqual(result, expected_result)

    def test_concatenate_files_empty(self):
        content = []
        expected_result = ""
        result = concatenate_files(content)
        self.assertEqual(result, expected_result)


class TestCleanDataset(unittest.TestCase):
    def test_clean_dataset_valid_and_invalid(self):
        content = [
            "Name,Category,Price,Quantity\nProd1,Cat1,10.5,5\nInvalidRow\nProd2,Cat2,abc,3\nProd3,Cat3,8.0,2"
        ]

        expected = "Name,Category,Price,Quantity\nProd1,Cat1,10.5,5\nProd3,Cat3,8.0,2"

        result = clean_dataset(content)
        self.assertEqual(result, expected)

    def test_clean_dataset_empty_input(self):
        content = []
        expected = ""
        results = clean_dataset(content)
        self.assertEqual(results, expected)

    def test_clean_dataset_missing_fields(self):
        content = [
            "Name,Category,Price,Quantity\nOnlyThreeFields,Cat1,10.5\n,,,\nProd2,Cat2,5.0,2"
        ]
        expected = "Name,Category,Price,Quantity\nProd2,Cat2,5.0,2"
        result = clean_dataset(content)
        self.assertEqual(result, expected)

    def test_clean_dataset_multiple_files(self):
        content = [
            "Name,Category,Price,Quantity\nProd1,Cat1,10,2",
            "Name,Category,Price,Quantity\nProd2,Cat2,20,3\nInvalid,Row",
            "Name,Category,Price,Quantity\nProd3,Cat3,30.5,5"
        ]
        expected = "Name,Category,Price,Quantity\nProd1,Cat1,10,2\nProd2,Cat2,20,3\nProd3,Cat3,30.5,5"
        risultato = clean_dataset(content)
        self.assertEqual(risultato, expected)


class TestSaveFile(unittest.TestCase):
    def test_save_file_success(self):
        data = "Content for testing function"

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_file = os.path.join(temp_dir, 'output.txt')
            save_file(temp_file, data)

            self.assertTrue(os.path.exists(temp_file))

            with open(temp_file, 'r') as f:
                content = f.read()
            self.assertEqual(content, data)


if __name__ == '__main__':
    unittest.main()
