from .read_pdf import read_pdf


def delete_text(file_input: str, file_output: str, text_to_delete: str) -> bool:
    try:
        document = read_pdf(file_input)
        deleted = 0
        for num_page in range(document.page_count):
            page = document[num_page]

            instance_text = page.search_for(text_to_delete)

            for inst in instance_text:
                page.add_redact_annot(inst)
                deleted += 1

            if instance_text:
                page.apply_redactions()
        if deleted > 0:
            document.save(file_output)
            print(f"Deleted {deleted} text. File saved as {file_output}")
            result = True
        else:
            print(f"{text_to_delete} not found in document")
            result = False

        document.close()
        return result

    except Exception as e:
        raise Exception(f"Error while deleting text from {file_input}: {e}")
