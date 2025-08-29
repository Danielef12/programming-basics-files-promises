from typing import Any, Dict, List

from source.utilities_modules.find_book_in_dataset import find_book_in_data


def update_price(data: List[Dict[str, Any]]) -> None:
    """Update the price of a book given its title.

    Args:
        data (List[Dict[str, Any]]): Dataset of books.
    """
    searched_book = find_book_in_data(data)
    if searched_book:
        for key, value in searched_book.items():
            print(f"{key.capitalize()}: {value}")
    if searched_book:
        old_price = searched_book["price"]
        new_price = float(input(f"The price is: {old_price}. Insert the new price: "))
        searched_book["price"] = new_price
        print("Price modified successfully.")
