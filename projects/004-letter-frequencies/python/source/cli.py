from .file_manipulate_modules import (reading_input, cleaning_input, frequency_analysis,
                                      graphic_representation_horizontal)
from .utility import confirm_operation


def main() -> None:
    try:
        input_file = input("Enter the path of the file (.txt) or enter the text to analyze").strip()
        text = reading_input(input_file)
        cleaned_file = cleaning_input(text)
        letter_frequencies = frequency_analysis(cleaned_file)
        graphic_representation_horizontal(letter_frequencies)
        print("Done")
        if confirm_operation("would you analyze another file or text?"):
            main()
        else:
            print("Thank you!")

    except (FileNotFoundError, RuntimeError) as e:
        print(f"Error: {e}")
        if confirm_operation("Would you like to try again?"):
            main()
        else:
            print("Thank you!")
    except Exception as e:
        print(f"Fatal error: {e}")
