import os.path
import tempfile
import unittest
from .. import file_manipulate_modules


class TestReadingInput(unittest.TestCase):
    def setUp(self):
        self.temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt')
        self.temp_file.write("Text to test the function")
        self.temp_file.close()
        self.temp_file_path = self.temp_file.name

    def tearDown(self):
        if os.path.exists(self.temp_file_path):
            os.unlink(self.temp_file_path)

    def test_reading_existing_file(self):
        result = file_manipulate_modules.reading_input(self.temp_file_path)
        self.assertEqual(result, "Text to test the function")

    def test_reading_non_existing_file(self):
        with self.assertRaises(FileNotFoundError) as context:
            file_manipulate_modules.reading_input("fake_file.txt")
        self.assertIn("No such file or directory", str(context.exception))

    def test_reading_text_input(self):
        text_input = "Text to test the function"
        result = file_manipulate_modules.reading_input(text_input)
        self.assertEqual(result, text_input)

    def test_reading_empty_text(self):
        text_input = ""
        result = file_manipulate_modules.reading_input(text_input)
        self.assertEqual(result, "")


class TestCleaningInput(unittest.TestCase):

    def test_normal_text_cleaning(self):
        input_text = "this, is the test, number 1543"
        result = file_manipulate_modules.cleaning_input(input_text)
        self.assertEqual(result, "thisisthetestnumber")

    def test_mixed_text_cleaning(self):
        input_text = "ABcDefGHI"
        result = file_manipulate_modules.cleaning_input(input_text)
        self.assertEqual(result, "abcdefghi")

    def test_cleaning_numbers_and_special_characters(self):
        input_text = "ABCd2948EF@!gh12I"
        result = file_manipulate_modules.cleaning_input(input_text)
        self.assertEqual(result, "abcdefghi")

    def test_cleaning_empty_text(self):
        input_text = ""
        result = file_manipulate_modules.cleaning_input(input_text)
        self.assertEqual(result, "")

    def test_cleaning_text_with_no_input(self):
        input_text = None
        result = file_manipulate_modules.cleaning_input(input_text)
        self.assertEqual(result, "")

    def test_cleaning_only_noalpha(self):
        input_text = "195@@1234##1240"
        result = file_manipulate_modules.cleaning_input(input_text)
        self.assertEqual(result, "")


class TestFrequencyAnalysis(unittest.TestCase):
    def test_frequency(self):
        text_input = "Hello"
        result = file_manipulate_modules.frequency_analysis(text_input)
        self.assertEqual(result, {"H": 1, "e": 1, "l": 2, "o": 1})

    def test_frequency_empty_string(self):
        text_input = ""
        result = file_manipulate_modules.frequency_analysis(text_input)
        self.assertEqual(result, {})

    def test_frequency_single_letter(self):
        text_input = "a"
        result = file_manipulate_modules.frequency_analysis(text_input)
        self.assertEqual(result, {"a": 1})

    def test_frequency_repeated_letter(self):
        text_input = "aaaaabbccc"
        result = file_manipulate_modules.frequency_analysis(text_input)
        self.assertEqual(result, {"a": 5, "b": 2, "c": 3})


if __name__ == '__main__':
    unittest.main()
