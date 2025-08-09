import os
import shutil
import sys
import tempfile
import unittest
from unittest.mock import MagicMock, patch

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

from source.modules.add_text import add_text
from source.modules.delete_text import delete_text
from source.modules.merge_pdf import merge_pdf
from source.modules.read_pdf import read_pdf
from source.modules.replace_text import replace_text
from source.modules.split_pdf import split_pdf
from source.modules.text_extract import text_extract


class TestPDFFunctions(unittest.TestCase):

    def setUp(self):
        """Set up test fixtures before each test method."""
        self.temp_dir = tempfile.mkdtemp()
        self.test_pdf_path = os.path.join(self.temp_dir, "test.pdf")
        self.output_pdf_path = os.path.join(self.temp_dir, "output.pdf")

    def tearDown(self):
        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir, ignore_errors=True)

    def create_sample_pdf(self) -> str:
        pdf_path = os.path.join(self.temp_dir, "sample.pdf")
        c = canvas.Canvas(pdf_path, pagesize=letter)
        c.drawString(100, 750, "Hello World")
        c.drawString(100, 700, "This is a test PDF")
        c.drawString(100, 650, "Sample text for testing")
        c.save()
        return pdf_path

    def create_multi_page_pdf(self) -> str:

        pdf_path = os.path.join(self.temp_dir, "multipage.pdf")
        c = canvas.Canvas(pdf_path, pagesize=letter)

        c.drawString(100, 750, "Page 1 Content")
        c.drawString(100, 700, "First page text")
        c.showPage()

        c.drawString(100, 750, "Page 2 Content")
        c.drawString(100, 700, "Second page text")
        c.showPage()

        c.drawString(100, 750, "Page 3 Content")
        c.drawString(100, 700, "Third page text")
        c.save()

        return pdf_path

    def create_empty_file(self, filename: str) -> str:
        file_path = os.path.join(self.temp_dir, filename)
        with open(file_path, "w") as f:
            f.write("")
        return file_path


class TestReadPdf(TestPDFFunctions):
    def setUp(self):
        super().setUp()
        self.sample_pdf = self.create_sample_pdf()

    def test_read_pdf_file_not_exists(self):
        """Test read_pdf raises FileNotFoundError when file doesn't exist."""
        with self.assertRaises(FileNotFoundError) as context:
            read_pdf("nonexistent.pdf")

        self.assertIn("File nonexistent.pdf does not exist", str(context.exception))

    def test_read_pdf_invalid_extension(self):
        txt_file = self.create_empty_file("test.txt")

        with self.assertRaises(ValueError) as context:
            read_pdf(txt_file)

        self.assertIn("is not a PDF file", str(context.exception))

    def test_read_pdf_success(self):
        result = read_pdf(self.sample_pdf)

        self.assertIsNotNone(result)
        self.assertTrue(result.is_pdf)
        self.assertGreater(result.page_count, 0)
        result.close()

    @patch("fitz.open")
    @patch("os.path.exists")
    def test_read_pdf_exception_handling(self, mock_exists, mock_fitz_open):
        mock_exists.return_value = True
        mock_fitz_open.side_effect = Exception("PDF open error")

        with self.assertRaises(Exception) as context:
            read_pdf("test.pdf")

        self.assertIn("Error while reading test.pdf", str(context.exception))


class TestExtractionText(TestPDFFunctions):
    def setUp(self):
        super().setUp()
        self.sample_pdf = self.create_sample_pdf()
        self.multi_page_pdf = self.create_multi_page_pdf()

    def test_text_extract_single_page_integration(self):
        result = text_extract(self.sample_pdf, page=1)

        self.assertIn("Hello World", result)
        self.assertIn("This is a test PDF", result)
        self.assertIn("Sample text for testing", result)

    def test_text_extract_invalid_page(self):
        with self.assertRaises(Exception) as context:
            text_extract(self.sample_pdf, page=10)

        self.assertIn("Error while extracting text", str(context.exception))

    def test_text_extract_all_pages_integration(self):
        result = text_extract(self.multi_page_pdf)

        self.assertIn("Page 1", result)
        self.assertIn("Page 2", result)
        self.assertIn("Page 3", result)
        self.assertIn("First page text", result)
        self.assertIn("Second page text", result)
        self.assertIn("Third page text", result)

    def test_text_extract_nonexistent_file(self):
        with self.assertRaises(Exception) as context:
            text_extract("nonexistent.pdf")

        self.assertIn("Error while extracting text", str(context.exception))


class TestReplaceText(TestPDFFunctions):
    @patch("source.modules.replace_text.read_pdf")
    def test_replace_text_success(self, mock_read_pdf):
        mock_rect = MagicMock()
        mock_rect.tl = (10, 20)

        mock_page = MagicMock()
        mock_page.search_for.return_value = [mock_rect]

        mock_document = MagicMock()
        mock_document.page_count = 1
        mock_document.__getitem__.return_value = mock_page
        mock_read_pdf.return_value = mock_document

        with patch("builtins.print") as mock_print:
            result = replace_text("input.pdf", "output.pdf", "old text", "new text")

        self.assertTrue(result)
        mock_page.add_redact_annot.assert_called_once_with(mock_rect)
        mock_page.apply_redactions.assert_called_once()
        mock_page.insert_text.assert_called_once_with(
            mock_rect.tl, "new text", fontsize=9, color=(0, 0, 0)
        )
        mock_document.save.assert_called_once_with("output.pdf")

    @patch("source.modules.replace_text.read_pdf")
    def test_replace_text_not_found(self, mock_read_pdf):
        mock_page = MagicMock()
        mock_page.search_for.return_value = []

        mock_document = MagicMock()
        mock_document.page_count = 1
        mock_document.__getitem__.return_value = mock_page
        mock_read_pdf.return_value = mock_document

        with patch("builtins.print") as mock_print:
            result = replace_text("input.pdf", "output.pdf", "nonexistent", "new text")

        self.assertFalse(result)
        mock_print.assert_called_with("nonexistent not found in document")


class TestAddText(TestPDFFunctions):
    def setUp(self):
        super().setUp()
        self.sample_pdf = self.create_sample_pdf()

    @patch("source.modules.add_text.read_pdf")
    def test_add_text_success(self, mock_read_pdf):
        mock_page = MagicMock()

        mock_document = MagicMock()
        mock_document.page_count = 3
        mock_document.__getitem__.return_value = mock_page
        mock_read_pdf.return_value = mock_document

        with patch("builtins.print") as mock_print:
            with patch("fitz.Point") as mock_point:
                add_text("input.pdf", "output.pdf", 1, 100.0, 200.0, "New text")

        mock_point.assert_called_once_with(100.0, 200.0)
        mock_page.insert_text.assert_called_once()
        mock_document.save.assert_called_once_with("output.pdf")

    @patch("source.modules.add_text.read_pdf")
    def test_add_text_invalid_page(self, mock_read_pdf):
        mock_document = MagicMock()
        mock_document.page_count = 3
        mock_read_pdf.return_value = mock_document

        with self.assertRaises(Exception) as context:
            add_text("input.pdf", "output.pdf", 5, 100.0, 200.0, "New text")

        self.assertIn("Error while adding text", str(context.exception))

    # Integration Tests for add_text function
    def test_add_text_integration(self):
        output_path = os.path.join(self.temp_dir, "add_text_output.pdf")

        # Add text to the PDF
        with patch("builtins.print"):
            add_text(self.sample_pdf, output_path, 1, 100.0, 600.0, "Added text")

        # Verify the file was created
        self.assertTrue(os.path.exists(output_path))

        # Verify the text was added by extracting text
        extracted_text = text_extract(output_path)
        self.assertIn("Added text", extracted_text)


class TestDeleteText(TestPDFFunctions):
    @patch("source.modules.delete_text.read_pdf")
    def test_delete_text_success(self, mock_read_pdf):
        mock_rect = MagicMock()

        mock_page = MagicMock()
        mock_page.search_for.return_value = [mock_rect]

        mock_document = MagicMock()
        mock_document.page_count = 1
        mock_document.__getitem__.return_value = mock_page
        mock_read_pdf.return_value = mock_document

        with patch("builtins.print") as mock_print:
            result = delete_text("input.pdf", "output.pdf", "text to delete")

        self.assertTrue(result)
        mock_page.add_redact_annot.assert_called_once_with(mock_rect)
        mock_page.apply_redactions.assert_called_once()
        mock_document.save.assert_called_once_with("output.pdf")

    @patch("source.modules.delete_text.read_pdf")
    def test_delete_text_not_found(self, mock_read_pdf):
        """Test delete_text when text is not found."""
        mock_page = MagicMock()
        mock_page.search_for.return_value = []

        mock_document = MagicMock()
        mock_document.page_count = 1
        mock_document.__getitem__.return_value = mock_page
        mock_read_pdf.return_value = mock_document

        with patch("builtins.print") as mock_print:
            result = delete_text("input.pdf", "output.pdf", "nonexistent text")

        self.assertFalse(result)
        mock_print.assert_called_with("nonexistent text not found in document")


class TestMergePdf(TestPDFFunctions):
    def setUp(self):
        super().setUp()
        self.sample_pdf = self.create_sample_pdf()

    def test_merge_pdf_integration(self):
        pdf2_path = os.path.join(self.temp_dir, "sample2.pdf")
        c = canvas.Canvas(pdf2_path, pagesize=letter)
        c.drawString(100, 750, "Second PDF Content")
        c.save()

        output_path = os.path.join(self.temp_dir, "merged.pdf")
        file_list = [self.sample_pdf, pdf2_path]

        with patch("builtins.print"):
            merge_pdf(file_list, output_path)

        # Verify the merged file was created
        self.assertTrue(os.path.exists(output_path))

        # Verify the merged content
        merged_document = read_pdf(output_path)
        self.assertGreaterEqual(merged_document.page_count, 2)
        merged_document.close()

        # Verify content from both files is present
        extracted_text = text_extract(output_path)
        self.assertIn("Hello World", extracted_text)
        self.assertIn("Second PDF Content", extracted_text)


class TestSplitPdf(TestPDFFunctions):
    def setUp(self):
        super().setUp()
        self.multi_page_pdf = self.create_multi_page_pdf()

    def test_split_pdf_integration(self):
        intervals = [(1, 2), (3, 3)]
        output_prefix = os.path.join(self.temp_dir, "split_test")

        with patch("builtins.print"):
            split_pdf(self.multi_page_pdf, intervals, output_prefix)

        expected_files = [
            f"{output_prefix}_pages_1-2.pdf",
            f"{output_prefix}_pages_3-3.pdf",
        ]

        for file_path in expected_files:
            self.assertTrue(
                os.path.exists(file_path), f"Split file {file_path} was not created"
            )

        # Verify the content of the first split file
        first_split_text = text_extract(expected_files[0])
        self.assertIn("Page 1 Content", first_split_text)
        self.assertIn("Page 2 Content", first_split_text)
        self.assertNotIn("Page 3 Content", first_split_text)

        # Verify the content of the second split file
        second_split_text = text_extract(expected_files[1])
        self.assertIn("Page 3 Content", second_split_text)
        self.assertNotIn("Page 1 Content", second_split_text)

    def test_split_pdf_invalid_interval(self):
        intervals = [(1, 10)]  # Invalid: page 10 doesn't exist

        with self.assertRaises(Exception) as context:
            split_pdf(self.multi_page_pdf, intervals)

        self.assertIn("Error while splitting", str(context.exception))

    def test_split_pdf_start_greater_than_end(self):
        intervals = [(3, 1)]  # Invalid: start > end

        with self.assertRaises(Exception) as context:
            split_pdf(self.multi_page_pdf, intervals)

        self.assertIn("Error while splitting", str(context.exception))

    def test_split_pdf_single_page_interval(self):
        intervals = [(1, 1), (2, 2)]
        output_prefix = os.path.join(self.temp_dir, "single_page_split")

        with patch("builtins.print"):
            split_pdf(self.multi_page_pdf, intervals, output_prefix)

        # Verify individual page files were created
        for i in [1, 2]:
            file_path = f"{output_prefix}_pages_{i}-{i}.pdf"
            self.assertTrue(os.path.exists(file_path))

            # Verify each file has only one page
            doc = read_pdf(file_path)
            self.assertEqual(doc.page_count, 1)
            doc.close()


if __name__ == "__main__":
    unittest.main()
