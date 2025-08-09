from source.menu import parser_arguments
from source.modules.add_text import add_text
from source.modules.delete_text import delete_text
from source.modules.merge_pdf import merge_pdf
from source.modules.replace_text import replace_text
from source.modules.split_pdf import split_pdf
from source.modules.text_extract import text_extract


def main() -> None:
    args = parser_arguments()

    try:
        match args.operations:
            case "extract":
                text = text_extract(args.file_input, args.page)
                print("EXTRACTED TEXT")
                print(text)

            case "replace":
                replace_text(args.file_input, args.file_output, args.text1, args.text2)

            case "add":
                add_text(
                    args.file_input,
                    args.file_output,
                    args.page,
                    args.x,
                    args.y,
                    args.text1,
                    args.font_size,
                )

            case "delete":
                delete_text(args.file_input, args.file_output, args.text1)

            case "merge":
                if args.file_output and args.file_input:
                    file_to_merge = [args.file_input] + (
                        args.additional_file_input or []
                    )
                    merge_pdf(file_to_merge, args.file_output)
                else:
                    print("Error")
                    return

            case "split":
                split_pdf(args.file_input, args.intervals, args.file_output)

            case _:
                print(f"Operazione '{args.operations}' non riconosciuta.")

    except FileNotFoundError as e:
        print(f"Error file: {e}")
    except ValueError as e:
        print(f"Value Error: {e}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
