from statistics import mean
from typing import Any, Dict, List


def calculate_average_rating(data: List[Dict[str, Any]]) -> float:
    """Calculate and print the average rating of all the books."""
    average_rate = mean(book["rating"] for book in data)
    print(f"The average rating for all books: {average_rate:.2f}")
    return average_rate
