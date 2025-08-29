from source.data_manipulation_modules.add_book import add_book
from source.data_manipulation_modules.search_book_spec import search_book
from source.data_manipulation_modules.update_price import update_price
from source.io_modules.load_json import load_json
from source.io_modules.save_json import update_dataset
from source.menu_utilities.print_menu import print_menu


def main() -> None:
    """Main function to run the program with menu-driven interface."""
    while True:
        try:
            filepath: str = input(
                "Insert the JSON filepath or type 'exit' to close the program: "
            )
            if filepath == "exit":
                print("Thanks for using. Exiting")
                break
            elif not filepath.endswith(".json"):
                print("Please provide a valid json file")
                continue
            else:
                data = load_json(filepath)
        except FileNotFoundError:
            print(f"File {filepath} not found, retry")
            continue

        if not data:
            print("Empty or invalid file, try again.")
            continue

        print("Json load succesfully.")
        print_menu()
        while True:
            option = input("Select an operation: ").strip()
            match option:
                case "1":
                    search_book(data)
                case "2":
                    update_price(data)
                case "3":
                    add_book(data)
                case "4":
                    while True:
                        selection = input("Want save file? (yes/no): ")
                        if selection in ["yes", "y"]:
                            update_dataset(data, filepath)
                            print("Back to file selection...")
                            break
                        elif selection in ["no", "n"]:
                            print("Back to file selection...")
                            break
                        else:
                            print("Invalid selection")
                    break
                case _:
                    print("Invalid option. Try again")
