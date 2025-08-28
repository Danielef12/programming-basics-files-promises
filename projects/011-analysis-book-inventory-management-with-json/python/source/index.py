import typing

from source.data_manipulation_modules.average_rating import \
    calculate_average_rating
from source.data_manipulation_modules.genre_distribution import \
    calculate_genre_distribution
from source.data_manipulation_modules.old_and_new_books import \
    calculate_oldest_and_newest_books
from source.data_manipulation_modules.rate_calculation import (
    calculate_genre_average_rating, calculate_highly_rated_books,
    calculate_top_rated_books)
from source.data_manipulation_modules.recommendation_books import (
    book_recommendation_by_genre, book_recommendation_by_year)
from source.input_modules.load_json import load_json
from source.menu_modules.print_menu import print_menu


def main() -> None:
    while True:
        try:
            filepath: str = input("Insert the JSON filepath: ")
            if not filepath.endswith(".json"):
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
            option: str = input("Select an option: ").strip()
            match option:
                case "1":
                    calculate_average_rating(data)
                case "2":
                    calculate_oldest_and_newest_books(data)
                case "3":
                    calculate_genre_distribution(data)
                case "4":
                    calculate_highly_rated_books(data)
                case "5":
                    calculate_top_rated_books(data)
                case "6":
                    calculate_genre_average_rating(data)
                case "7":
                    selection = input(
                        "Do you want to be recommended based on a category [1] or based on a specific year[2]?"
                    )
                    while not selection in ["1", "2"]:
                        selection = input("Invalid selection, select 1 or 2")
                    if selection == "1":
                        book_recommendation_by_genre(data)
                    else:
                        book_recommendation_by_year(data)
                case "0":
                    break
                case _:
                    print("Invalid option, try again")
