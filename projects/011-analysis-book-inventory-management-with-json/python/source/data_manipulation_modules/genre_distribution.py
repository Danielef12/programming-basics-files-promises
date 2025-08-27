from typing import Any, Dict, List


def calculate_genre_distribution(data: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Count the number of books in each genre."""
    genre_books = []
    for genre in data:
        genre_books.append(genre["genre"])

    genre_analysis = {}
    for genre in genre_books:
        genre_analysis[genre] = 0
        for book in data:
            if book["genre"] == genre:
                genre_analysis[genre] += 1
    print("Here's the genre analysis.")
    for genre in genre_analysis:
        print("{}: {} books".format(genre, genre_analysis[genre]))

    return genre_analysis
