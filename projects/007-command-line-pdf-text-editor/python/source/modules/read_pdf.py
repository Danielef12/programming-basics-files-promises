import argparse
import os
from typing import List, Optional, Tuple

import fitz


def read_pdf(pdf_path: str) -> fitz.Document:
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"File {pdf_path} does not exist")

    if not pdf_path.lower().endswith(".pdf"):
        raise ValueError(f"File {pdf_path} is not a PDF file")

    try:
        document = fitz.open(pdf_path)
        if document.is_pdf:
            return document
        else:
            raise ValueError(f"File {pdf_path} is not a valid PDF file")
    except Exception as e:
        raise Exception(f"Error while reading {pdf_path}: {e}")


