from collections import defaultdict
from typing import Any, Dict, List


def filter_books(data, rate_to_filter, fields_to_print):
    """
        Filter books by minimum rating and print selected fields.

        Args:
            data (List[Dict[str, Any]]): List of books with details (title, author, rating, genre, etc.).
            rate_to_filter (float): Minimum rating threshold for filtering books.
            fields_to_print (List[str]): Fields to display for each filtered book.

        Returns:
            List[Dict[str, Any]]: List of books that meet the filtering condition.
        """
    filtered = []
    for book in data:
        if book['rating'] >= rate_to_filter:
            filtered.append(book)
            for field in fields_to_print:
                print(f"{field.capitalize()}:", book.get(field,'N/A'))
            print()
    return filtered




def calculate_highly_rated_books(data: List[Dict[str, Any]]) -> None:
    """
    Print titles and authors of books with a rating of 4.5 or higher.

    Args:
        data (List[Dict[str, Any]]): List of books with details (title, author, rating, genre, etc.).

    Returns:
        None
    """
    print("High rated books:")
    filter_books(data, 4.5, ['title', 'author'])

def calculate_top_rated_books(data: List[Dict[str, Any]]) -> None:
    """
    Print the titles, authors, and ratings of books with rating >= 4.3.

    Args:
        data (List[Dict[str, Any]]): List of books with details (title, author, rating, genre, etc.).

    Returns:
        None
    """
    print("\nHere is the list of the most voted books")
    filter_books(data, 4.3, ['title', 'author', 'rating'])


def calculate_genre_average_rating(
    data: List[Dict[str, Any]],
) -> defaultdict[Any, list]:
    """
    Calculate and print the average rating for each genre.

    Args:
        data (List[Dict[str, Any]]): List of books with details (title, author, rating, genre, etc.).

    Returns:
        defaultdict[Any, list]: Dictionary mapping each genre to a list of ratings.
    """
    mean_rating = defaultdict(list)

    for book in data:
        genre = book.get("genre", "Not specific")
        rating = book.get("rating", 0)
        mean_rating[genre].append(rating)

    print("Average ratings by category")
    for category, rating in mean_rating.items():
        average = sum(rating) / len(rating)
        print(f"Genre: {category} : {average:.2f}")
    return mean_rating
