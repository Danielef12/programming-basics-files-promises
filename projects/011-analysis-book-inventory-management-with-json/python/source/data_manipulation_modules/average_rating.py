from statistics import mean
from typing import Any, Dict, List


def calculate_average_rating(data: List[Dict[str, Any]]) -> float:
    """
    Calculate and print the average rating of all books in the collection.

    Args:
        data (List[Dict[str, Any]]): List of books with details
            (title, author, rating, genre, publication_year, etc.).

    Returns:
        float: The average rating of all books.
    """
    average_rate = mean(book["rating"] for book in data)
    print(f"The average rating for all books: {average_rate:.2f}")
    return average_rate
