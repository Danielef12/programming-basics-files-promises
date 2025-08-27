from statistics import mean
from typing import Any, Dict, List


def calculate_oldest_and_newest_books(
    data: List[Dict[str, Any]],
) -> tuple[list[Any], list[Any]]:
    """Determine and print the title, author, and publication year of the oldest and newest books in the collection."""
    average_publication_year = round(mean(book["publication_year"] for book in data))
    older_books = []
    new_books = []
    for book in data:
        if book["publication_year"] > average_publication_year:
            new_books.append(book)
        else:
            older_books.append(book)
    sorted_older_books = sorted(older_books, key=lambda book: book["publication_year"])
    sorted_new_books = sorted(
        new_books, key=lambda book: book["publication_year"], reverse=True
    )

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
