import fitz

from .read_pdf import read_pdf


def add_text(
    file_input: str,
    file_output: str,
    page: int,
    x: float,
    y: float,
    text: str,
    font_size: int = 11,
) -> None:
    try:
        document = read_pdf(file_input)
        if not (1 <= page <= document.page_count):
            raise ValueError(f"Page {page} invalid, document contains {page} pages")

        pag = document[page - 1]

        point = fitz.Point(x, y)
        pag.insert_text(point, text, fontsize=11, color=(0, 0, 0))
        document.save(file_output)
        document.close()
        print(f"Added text for page {page}. Document saved as {file_output}")
    except Exception as e:
        raise Exception(f"Error while adding text from {file_input}: {e}")
