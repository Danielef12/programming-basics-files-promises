import os
import string
import sys
import unittest
from unittest.mock import MagicMock, Mock, patch

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "source", "modules")),
)

from read_pdf import read_pdf
from text_elaboration import clean_text, word_count


class TestReadPdf(unittest.TestCase):
    @patch("read_pdf.os.path.isfile", return_value=True)
    @patch("read_pdf.PdfReader")
    def test_read_pdf_success(self, mock_pdf_reader, mock_isfile):
        mock_page1 = Mock()
        mock_page1.extract_text.return_value = "This is page 1. "

        mock_page2 = Mock()
        mock_page2.extract_text.return_value = "This is page 2."

        mock_reader = Mock()
        mock_reader.pages = [mock_page1, mock_page2]
        mock_pdf_reader.return_value = mock_reader

        result = read_pdf("test.pdf")

        expected = (
            "This is page 1.  This is page 2."
        )
        self.assertEqual(result, expected)
        mock_pdf_reader.assert_called_once_with("test.pdf")

    @patch("read_pdf.os.path.isfile", return_value=True)
    @patch("read_pdf.PdfReader")
    def test_read_pdf_with_empty_pages_skipped(self, mock_pdf_reader, mock_isfile):
        mock_page1 = Mock()
        mock_page1.extract_text.return_value = "Valid text"

        mock_page2 = Mock()
        mock_page2.extract_text.return_value = ""

        mock_page3 = Mock()
        mock_page3.extract_text.return_value = None

        mock_page4 = Mock()
        mock_page4.extract_text.return_value = "Other text"

        mock_reader = Mock()
        mock_reader.pages = [mock_page1, mock_page2, mock_page3, mock_page4]
        mock_pdf_reader.return_value = mock_reader

        result = read_pdf("test.pdf")

        expected = "Valid text Other text"
        self.assertEqual(result, expected)

    @patch("read_pdf.os.path.isfile", return_value=True)
    @patch("read_pdf.PdfReader")
    def test_read_pdf_all_empty_pages(self, mock_pdf_reader, mock_isfile):
        mock_page1 = Mock()
        mock_page1.extract_text.return_value = ""
        mock_page2 = Mock()
        mock_page2.extract_text.return_value = None

        mock_reader = Mock()
        mock_reader.pages = [mock_page1, mock_page2]
        mock_pdf_reader.return_value = mock_reader

        result = read_pdf("test.pdf")
        self.assertEqual(result, "")

    def test_read_pdf_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            read_pdf("non_existent.pdf")


class TestCleanText(unittest.TestCase):
    def test_clean_text_basic(self):
        text = "Hello, world! How are you?"
        result = clean_text(text)
        expected = ["hello", "world", "how", "are", "you"]
        self.assertEqual(result, expected)

    def test_clean_text_with_numbers(self):
        text = "This is the 250 test"
        result = clean_text(text)
        expected = ["this", "is", "the", "250", "test"]
        self.assertEqual(result, expected)

    def test_clean_text_all_punctuation(self):
        text = f"Test{string.punctuation}word"
        result = clean_text(text)
        expected = ["testword"]
        self.assertEqual(result, expected)

    def test_clean_text_empty_string(self):
        text = ""
        result = clean_text(text)
        expected = []
        self.assertEqual(result, expected)

    def test_clean_text_only_punctuation(self):
        text = "!@#$%^&*()"
        result = clean_text(text)
        expected = []
        self.assertEqual(result, expected)

    def test_clean_text_multiple_spaces(self):
        text = "try1    try2     try3"
        result = clean_text(text)
        expected = ["try1", "try2", "try3"]
        self.assertEqual(result, expected)

    def test_clean_text_mixed_case(self):
        text = "HeLlO WoRLd"
        result = clean_text(text)
        expected = ["hello", "world"]
        self.assertEqual(result, expected)


class TestWordCount(unittest.TestCase):
    def test_word_count_basic(self):
        words = ["hello", "world", "hello", "python", "world", "hello"]
        result = word_count(words)
        expected = {"hello": 3, "world": 2, "python": 1}
        self.assertEqual(result, expected)

    def test_word_count_empty_list(self):
        words = []
        result = word_count(words)
        expected = {}
        self.assertEqual(result, expected)

    def test_word_count_single_word(self):
        words = ["python"]
        result = word_count(words)
        expected = {"python": 1}
        self.assertEqual(result, expected)

    def test_word_count_all_same_word(self):
        words = ["test", "test", "test", "test"]
        result = word_count(words)
        expected = {"test": 4}
        self.assertEqual(result, expected)

    def test_word_count_all_different_words(self):
        words = ["one", "two", "three", "four"]
        result = word_count(words)
        expected = {"one": 1, "two": 1, "three": 1, "four": 1}
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
