from typing import Optional

from .read_pdf import read_pdf


def text_extract(file_name: str, page: Optional[int] = None) -> str:
    try:
        document = read_pdf(file_name)
        extracted_text = ""
        if page is not None:
            if 1 <= page <= document.page_count:
                pag = document[page - 1]
                extracted_text = pag.get_text()
            else:
                raise ValueError(
                    f"Number of page {page} invalid, document contains {page} pages"
                )
        else:
            for num_page in range(document.page_count):
                pag = document[num_page]
                extracted_text += f"Page {num_page + 1}"
                extracted_text += pag.get_text()
        document.close()
        return extracted_text
    except Exception as e:
        raise Exception(f"Error while extracting text from {file_name}: {e}")
