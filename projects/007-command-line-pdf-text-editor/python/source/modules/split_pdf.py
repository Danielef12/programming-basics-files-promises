from typing import List, Tuple

import fitz

from .read_pdf import read_pdf


def split_pdf(
    file_input: str, intervals: List[Tuple[int, int]], output_prefix: str = "split"
) -> None:
    try:
        document = read_pdf(file_input)

        for i, (start, end) in enumerate(intervals):

            if not (
                1 <= start <= document.page_count and 1 <= end <= document.page_count
            ):
                raise ValueError(
                    f"Interval of pages {start}-{end} invalid, document contains {document.page_count} pages"
                )

            if start > end:
                raise ValueError(f"Starting page greater than end page.")

            new_document = fitz.open()
            new_document.insert_pdf(document, from_page=start - 1, to_page=end - 1)

            output_name = f"{output_prefix}_pages_{start}-{end}.pdf"
            new_document.save(output_name)
            new_document.close()
            print(f"created:{output_name}")
        document.close()

    except Exception as e:
        raise Exception(f"Error while splitting {file_input}: {e}")
