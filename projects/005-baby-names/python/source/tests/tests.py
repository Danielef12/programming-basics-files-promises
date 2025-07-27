import unittest
from unittest.mock import mock_open, patch

from ..modules.average_length import average_length_names_for_year
from ..modules.diversity import name_diversity_analysis
from ..modules.ending_name import name_endings_analysis
from ..modules.initials_name import name_initial_analysis
from ..modules.IO_utility import read_file
from ..modules.popular_names import (popular_name_for_decade,
                                     popular_name_gender)


class TestReadFile(unittest.TestCase):
    def test_read_file_valid(self):
        mock_csv = "Name,Sex,YearOfBirth,Number\nJohn,M,2000,50\nMary,F,2000,60\n"
        with patch("builtins.open", mock_open(read_data=mock_csv)):
            data = read_file("mock.csv")
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]["Name"], "John")
        self.assertEqual(data[1]["Name"], "Mary")

    def test_read_file_empty(self):
        with patch("builtins.open", mock_open(read_data="")):
            data = read_file("mock.csv")
        self.assertEqual(data, [])

    def test_read_file_header_only(self):
        with patch(
            "builtins.open", mock_open(read_data="Name,Sex,YearOfBirth,Number\n")
        ):
            data = read_file("mock.csv")
        self.assertEqual(data, [])

    def test_read_file_file_not_found(self):
        with patch("builtins.open", side_effect=FileNotFoundError):
            data = read_file("nonexistent.csv")
        self.assertEqual(data, [])

    def test_read_file_invalid_encoding(self):
        def raise_unicode_error(*args, **kwargs):
            raise UnicodeDecodeError("utf-8", b"", 0, 1, "invalid start byte")

        with patch("builtins.open", side_effect=raise_unicode_error):
            data = read_file("bad_encoding.csv")
        self.assertEqual(data, [])

    def test_read_file_missing_fields(self):
        mock_csv = "Name,Sex,YearOfBirth,Number\nJohn,M,2000\n"
        with patch("builtins.open", mock_open(read_data=mock_csv)):
            data = read_file("mock.csv")
        self.assertEqual(data[0].get("Number"), None)


class TestPopularNameGender(unittest.TestCase):
    def setUp(self):
        self.data = [
            {"Name": "John", "Sex": "M", "YearOfBirth": "2000", "Number": "50"},
            {"Name": "Mary", "Sex": "F", "YearOfBirth": "2000", "Number": "60"},
            {"Name": "Anna", "Sex": "F", "YearOfBirth": "2000", "Number": "40"},
            {"Name": "John", "Sex": "M", "YearOfBirth": "2000", "Number": "30"},
        ]

    def test_popular_name_gender_normal(self):
        male, female = popular_name_gender(self.data, 2000, top_n=1)
        self.assertEqual(male[0][0], "John")
        self.assertEqual(female[0][0], "Mary")

    def test_popular_name_gender_no_matches(self):
        result = popular_name_gender(self.data, 1990)
        self.assertEqual(result, ([], []))

    def test_popular_name_gender_only_female(self):
        data = [{"Name": "Mary", "Sex": "F", "YearOfBirth": "2000", "Number": "50"}]
        result = popular_name_gender(data, 2000)
        self.assertEqual(len(result[0]), 0)
        self.assertEqual(result[1][0][0], "Mary")


class TestNameDiversityAnalysis(unittest.TestCase):
    def test_diversity_normal(self):
        data = [
            {"Name": "John", "Sex": "M", "YearOfBirth": "2000", "Number": "10"},
            {"Name": "Anna", "Sex": "F", "YearOfBirth": "2000", "Number": "10"},
            {"Name": "Emma", "Sex": "F", "YearOfBirth": "2001", "Number": "10"},
        ]
        result = name_diversity_analysis(data)
        self.assertEqual(result[0][1], 1)
        self.assertEqual(result[0][2], 1)
        self.assertEqual(result[1][2], 1)


class TestAverageLengthNames(unittest.TestCase):
    def test_average_length(self):
        data = [
            {"Name": "A", "Sex": "M", "YearOfBirth": "2000", "Number": "1"},
            {"Name": "Zebediah", "Sex": "M", "YearOfBirth": "2000", "Number": "1"},
            {"Name": "Ana", "Sex": "F", "YearOfBirth": "2000", "Number": "2"},
        ]
        result = average_length_names_for_year(data)
        self.assertAlmostEqual(result[0][1], 4.5, places=1)
        self.assertAlmostEqual(result[0][2], 3.0, places=1)


class TestNameEndingsAnalysis(unittest.TestCase):
    def test_endings_case_insensitivity(self):
        data = [
            {"Name": "Anna", "Sex": "F", "YearOfBirth": "2000", "Number": "10"},
            {"Name": "Maria", "Sex": "F", "YearOfBirth": "2000", "Number": "10"},
        ]
        endings_m, endings_f = name_endings_analysis(data, top_n=1)
        self.assertEqual(endings_f[0][0], "a")


class TestNameInitialAnalysis(unittest.TestCase):
    def test_initials_case_insensitive(self):
        data = [
            {"Name": "alice", "Sex": "F", "YearOfBirth": "2000", "Number": "10"},
            {"Name": "Alice", "Sex": "F", "YearOfBirth": "2000", "Number": "10"},
        ]
        initials_m, initials_f = name_initial_analysis(data, top_n=1)
        self.assertEqual(initials_f[0][0], "A")
        self.assertEqual(initials_f[0][1], 20)


class TestPopularNameForDecade(unittest.TestCase):
    def test_name_across_decade(self):
        data = [
            {"Name": "John", "Sex": "M", "YearOfBirth": "2001", "Number": "20"},
            {"Name": "John", "Sex": "M", "YearOfBirth": "2009", "Number": "30"},
        ]
        result = popular_name_for_decade(data, top_n=1)
        self.assertEqual(result[2000]["M"][0][0], "John")
        self.assertEqual(result[2000]["M"][0][1], 50)


if __name__ == "__main__":
    unittest.main()
