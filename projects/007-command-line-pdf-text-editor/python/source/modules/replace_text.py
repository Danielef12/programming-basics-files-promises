from .read_pdf import read_pdf


def replace_text(
    file_input: str, file_output: str, search_text: str, text_to_replace: str
) -> bool:
    try:
        document = read_pdf(file_input)
        replaced = 0

        for num_page in range(document.page_count):
            page = document[num_page]

            instance_text = page.search_for(search_text)

            for inst in instance_text:
                page.add_redact_annot(inst)
                page.apply_redactions()

                page.insert_text(inst.tl, text_to_replace, fontsize=9, color=(0, 0, 0))
                replaced += 1

        if replaced > 0:
            document.save(file_output)
            print(f"{replaced} substitutions made. File saved as {file_output}")
            result = True
        else:
            print(f"{search_text} not found in document")
            result = False

        document.close()
        return result
    except Exception as e:
        raise Exception(f"Error while replacing text from {file_input}: {e}")
