import os

from PyPDF2 import PdfReader


def read_pdf(pdf_path) -> str:
    if not os.path.isfile(pdf_path):
        raise FileNotFoundError("File not found")
    if not pdf_path.lower().endswith(".pdf"):
        raise ValueError("File not a pdf")
    reader = PdfReader(pdf_path)
    base_text = [page.extract_text() for page in reader.pages if page.extract_text()]
    return " ".join(base_text)
