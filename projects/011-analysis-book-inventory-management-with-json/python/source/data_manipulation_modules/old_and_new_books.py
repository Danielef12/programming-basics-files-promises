from statistics import mean
from typing import Any, Dict, List


def sort_books(list_to_sort, filter_by: str) -> list:
    """
        Sort a list of books by a specified field.

        Args:
            list_to_sort (List[Dict[str, Any]]): List of books with details (title, author, rating, genre, publication_year, etc.).
            filter_by (str): The key to sort the books by (e.g., "publication_year", "rating").

        Returns:
            List[Dict[str, Any]]: The sorted list of books.
        """
    sorted_list = sorted(list_to_sort, key=lambda x: x[filter_by])
    return sorted_list





def calculate_oldest_and_newest_books(
    data: List[Dict[str, Any]],
) -> tuple[list[Any], list[Any]]:
    """
    Determine and print the oldest and newest books in the collection.

    The classification is based on the average publication year:
    - Books with a publication year above the average are considered "new".
    - Books with a publication year equal to or below the average are considered "old".

    Args:
        data (List[Dict[str, Any]]): List of books with details (title, author, rating, genre, publication_year, etc.).

    Returns:
        Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
            A tuple containing:
                - List of newest books (sorted by publication year).
                - List of oldest books (sorted by publication year).
    """
    average_publication_year = round(mean(book["publication_year"] for book in data))
    older_books = []
    new_books = []
    for book in data:
        if book["publication_year"] > average_publication_year:
            new_books.append(book)
        else:
            older_books.append(book)
    sorted_older_books = sort_books(older_books, "publication_year")
    sorted_new_books = sort_books(new_books, "publication_year")

    print("The 5 oldest books are:")
    for book in sorted_older_books[0:5]:
        print(
            f"\nTitle: {book['title']}\nAuthor: {book['author']}\nYear: {book['publication_year']}"
        )

    print("\nThe 5 newest books are:")
    for book in sorted_new_books[0:5]:
        print(
            f"\nTitle: {book['title']}\nAuthor: {book['author']}\nYear: {book['publication_year']}"
        )
    return sorted_new_books, sorted_older_books
