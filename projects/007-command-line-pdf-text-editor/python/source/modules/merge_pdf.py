from typing import List

import fitz

from .read_pdf import read_pdf


def merge_pdf(file_list: List[str], file_output: str) -> None:
    try:
        documents = fitz.open()
        for file_name in file_list:
            print(f"Processing: {file_name}")
            current_document = read_pdf(file_name)
            documents.insert_pdf(current_document)
            current_document.close()

        documents.save(file_output)
        documents.close()
        print(f"Merging {len(file_list)} PDF files into {file_output}")
    except Exception as e:
        raise Exception(f"Error while merging {file_list}: {e}")
