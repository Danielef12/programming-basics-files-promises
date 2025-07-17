import unittest
import tempfile
import os
from io import StringIO
from contextlib import redirect_stdout
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ..head import head_of_a_file


class TestHeadOfAFile(unittest.TestCase):

    def setUp(self):
        # Crea un file temporaneo con contenuti di esempio
        self.test_file = tempfile.NamedTemporaryFile(delete=False, mode='w+', encoding='utf-8')
        self.test_lines = [f"Line {i}\n" for i in range(1, 21)]  # 20 righe
        self.test_file.writelines(self.test_lines)
        self.test_file.close()

    def tearDown(self):
        # Cancella il file temporaneo dopo i test
        os.remove(self.test_file.name)

    def test_default_lines(self):
        f = StringIO()
        with redirect_stdout(f):
            head_of_a_file(self.test_file.name)
        output = f.getvalue().strip().split('\n')
        expected = [line.strip() for line in self.test_lines[:10]]
        self.assertEqual(output, expected)

    def test_custom_lines(self):
        f = StringIO()
        with redirect_stdout(f):
            head_of_a_file(self.test_file.name, line_display=5)
        output = f.getvalue().strip().split('\n')
        expected = [line.strip() for line in self.test_lines[:5]]
        self.assertEqual(output, expected)

    def test_show_filename(self):
        f = StringIO()
        with redirect_stdout(f):
            head_of_a_file(self.test_file.name, line_display=3, show_filename=True)
        output = f.getvalue().strip().split('\n')
        filename_line = f"===> {os.path.basename(self.test_file.name)} <==="
        expected = [filename_line] + [line.strip() for line in self.test_lines[:3]]
        self.assertEqual(output, expected)

    def test_file_not_found(self):
        f = StringIO()
        with redirect_stdout(f):
            head_of_a_file("non_esiste.txt")
        output = f.getvalue().strip()
        self.assertIn("File not found", output)


if __name__ == "__main__":
    unittest.main()
