from .modules.print_output import print_words_count
from .modules.read_pdf import read_pdf
from .modules.text_elaboration import clean_text, word_count


def menu():
    while True:
        pdf_path: str = input("Insert pdf file path (or type 'exit' to quit): ").strip()
        if pdf_path.lower() == "exit":
            print("Goodbye!")
            break

        try:
            text = read_pdf(pdf_path)
        except FileNotFoundError:
            print("File not found! Please try again.")
            continue
        except ValueError as e:
            print(f"Error reading file: {e}")
            continue

        while True:
            try:
                top_n: int = int(input("How many words would you like to count? "))
                if top_n <= 0:
                    print("Please enter a positive number.")
                    continue
                break
            except ValueError:
                print("Please enter a valid number.")

        words = clean_text(text)
        words_count = word_count(words)
        print_words_count(words_count, top_n)

        again = input("Do you want to analyze another file? (yes/no): ").strip().lower()
        if again not in ("yes", "y"):
            print("Goodbye!")
            break
