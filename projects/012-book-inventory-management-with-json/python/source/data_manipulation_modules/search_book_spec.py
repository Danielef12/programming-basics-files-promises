from typing import Any, Dict, List

from source.utilities_modules.find_book_in_dataset import find_book_in_data


def search_book(data: List[Dict[str, Any]]) -> None:
    """Search for a book and recommend another one of the same genre.

    Args:
        data (List[Dict[str, Any]]): Dataset of books.
    """
    searched_book = find_book_in_data(data)
    if searched_book:
        for key, value in searched_book.items():
            print(f"{key.capitalize()}: {value}")

        recommended_book = [
            recc
            for recc in data
            if recc["genre"] == searched_book["genre"]
            and recc["title"] != searched_book["title"]
        ]
        if recommended_book:
            first = recommended_book[0]
            print("\nI recommend you another book of the same genre.\n")
            for key, value in first.items():
                print(f"{key.capitalize()}: {value}")
