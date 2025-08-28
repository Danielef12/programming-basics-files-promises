from typing import Any, Dict, List


def calculate_genre_distribution(data: List[Dict[str, Any]]) -> Dict[str, int]:
    """
    Count and print the number of books in each genre.

    Args:
        data (List[Dict[str, Any]]): List of books with details (title, author, rating, genre, etc.).

    Returns:
        Dict[str, int]: Dictionary mapping each genre to the number of books in that genre.
    """
    genre_analysis: Dict[str, int] = {}

    for book in data:
        genre = book.get("genre", "Not specific")
        genre_analysis[genre] = genre_analysis.get(genre, 0) + 1

    print("Here's the genre analysis:")
    for genre, count in genre_analysis.items():
        print(f"{genre}: {count} books")

    return genre_analysis
