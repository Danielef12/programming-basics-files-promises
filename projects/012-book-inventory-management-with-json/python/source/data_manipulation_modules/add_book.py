from typing import Any, Dict, List


def add_book(data: List[Dict[str, Any]]) -> None:
    """Add a new book to the dataset by following the template of the first entry.

    Args:
        data (List[Dict[str, Any]]): Dataset of books.
    """
    new_book: Dict[str, Any] = {}
    book_template = data[0]
    for key, example_value in book_template.items():
        while True:
            user_input = input(
                f"Insert {key.title()} ({type(example_value).__name__}): "
            ).strip()
            if isinstance(example_value, int):
                try:
                    new_book[key] = int(user_input)
                    break
                except ValueError:
                    print(f"Field {key} must be a positive number")
            elif isinstance(example_value, float):
                try:
                    new_book[key] = float(user_input)
                    break
                except ValueError:
                    print(f"Field {key} must be a decimal number")
            else:
                if user_input:
                    new_book[key] = user_input
                    break
                else:
                    print(f"{key} cannot be empty")
    data.append(new_book)

    print("Book added successfully")
    print("Summary:\n")
    for k, v in new_book.items():
        print(f"- {k.capitalize()}: {v}")
