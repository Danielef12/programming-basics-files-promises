from typing import Any, Dict, List


def find_book_in_data(data: List[Dict[str, Any]]) -> Dict[str, Any] | None:
    """Find a book in the dataset by its title.

    Args:
        data (List[Dict[str, Any]]): Dataset of books.

    Returns:
        Dict[str, Any] | None: The found book dictionary if exists, otherwise None.
    """
    while True:
        book_to_search = input("Insert the book name: ").lower().strip()
        if not book_to_search:
            print("Please enter a book name.")
            continue
        book = next((b for b in data if b["title"].lower() == book_to_search), None)
        if book:
            print(f"\n{book['title']} found\n")
            return book
        else:
            print(f"{book_to_search} not found")
