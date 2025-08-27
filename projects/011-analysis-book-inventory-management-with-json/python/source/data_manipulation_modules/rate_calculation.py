from collections import defaultdict
from typing import Any, Dict, List


def calculate_highly_rated_books(data: List[Dict[str, Any]]) -> List[Dict]:
    """Identify and print the titles and authors of books with a rating of 4.5 or higher."""
    high_rated = []
    for book in data:
        if book["rating"] >= 4.5:
            high_rated.append(book)

    print("High rated books:")
    for book in high_rated:
        print(f"\nTitle: {book['title']}\nAuthor: {book['author']}\n")
    return high_rated


def calculate_top_rated_books(data: List[Dict[str, Any]]) -> List[Any]:
    """Find and print the title, author, and rating of the book with the highest rating."""
    max_book_rated = []
    for book in data:
        if book["rating"] >= 4.3:
            max_book_rated.append(book)

    print("\nHere is the list of the most voted books")
    for book in max_book_rated:
        print("\nTitle: {} - Author: {}".format(book["title"], book["author"]))
    return max_book_rated


def calculate_genre_average_rating(
    data: List[Dict[str, Any]],
) -> defaultdict[Any, list]:
    """Calculate and print the average rating for each genre category."""
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
