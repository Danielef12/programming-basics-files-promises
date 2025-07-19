import unittest
from unittest.mock import patch
from io import StringIO
import tempfile
import os
from source.modules import tail_of_a_file


class TestTailOfAFile(unittest.TestCase):
    def setUp(self):
        # Crea un file temporaneo con contenuto di esempio
        self.temp_file = tempfile.NamedTemporaryFile(mode='w+', delete=False)
        self.temp_file.writelines([f"Line {i}\n" for i in range(1, 21)])  # 20 righe
        self.temp_file.close()
        self.filename = self.temp_file.name

    def tearDown(self):

        os.unlink(self.filename)

    @patch('sys.stdout', new_callable=StringIO)
    def test_tail_default(self, mock_stdout):
        tail_of_a_file(self.filename)
        output = mock_stdout.getvalue().strip().split('\n')
        expected = [f"Line {i}" for i in range(11, 21)]  # Ultime 10 righe
        self.assertEqual(output, expected)

    @patch('sys.stdout', new_callable=StringIO)
    def test_tail_with_start_line(self, mock_stdout):
        tail_of_a_file(self.filename, start_line=15)
        output = mock_stdout.getvalue().strip().split('\n')
        expected = [f"Line {i}" for i in range(16, 21)]
        self.assertEqual(output, expected)

    @patch('sys.stdout', new_callable=StringIO)
    def test_file_not_found(self, mock_stdout):
        tail_of_a_file("non_existent_file.txt")
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "File non_existent_file.txt not found")


if __name__ == '__main__':
    unittest.main()
