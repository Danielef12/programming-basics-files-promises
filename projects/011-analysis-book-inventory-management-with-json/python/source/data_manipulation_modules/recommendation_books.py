from typing import Any, Dict, List


def book_recommendation_by_genre(data: List[Dict[str, Any]]) -> List[Any]:
    """Based on the user's favorite genre (prompted as input), recommend a book from that genre with a rating above 4.0."""
    genre_prefer = input("Insert prefer genre: ").strip().title()
    book_recommend = []
    for book in data:
        if book["genre"] == genre_prefer and book["rating"] >= 4:
            book_recommend.append(book)
            print(
                "\nTitle: {}\nAuthor: {}\nRating: {}\n".format(
                    book["title"], book["author"], book["rating"]
                )
            )
    return book_recommend


def book_recommendation_by_year(data: List[Dict[str, Any]]) -> List[Any]:
    """Prompt the user to enter a year, and then print the titles and authors of books published in or after that year."""
    year = int(input("Insert year of publication: "))
    books_by_year = []
    for book in data:
        if book["publication_year"] >= year and book["rating"] > 4:
            books_by_year.append(book)
    print(f"title of book publicate after {year}:")
    books_by_year = sorted(books_by_year, key=lambda x: x["publication_year"])
    print(books_by_year)
    for book in books_by_year:
        print(
            f"Title: {book['title']}\nAuthor: {book['author']}\nYear: {book['publication_year']}\n"
        )
    return books_by_year
