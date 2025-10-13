from datetime import datetime
from typing import Callable, Optional, Tuple


def validate_date(date_string: str) -> Tuple[bool, Optional[str]]:
    """
    Validate that a date string is in the correct format and not in the past.

    Args:
        date_string: Date string in format "dd-mm-yyyy"

    Returns:
        Tuple of (is_valid, formatted_date) where formatted_date is in "dd/mm/yyyy" format
    """
    try:
        date_obj = datetime.strptime(date_string, "%d-%m-%Y")
        if date_obj.date() >= datetime.today().date():
            return True, date_obj.strftime("%d/%m/%Y")
        else:
            print("The expiration date cannot be earlier than today")
            return False, None
    except ValueError:
        return False, None


def validate_priority(priority: str) -> Tuple[bool, Optional[str]]:
    """
    Validate that a priority string is one of the allowed values.

    Args:
        priority: Priority string to validate

    Returns:
        Tuple of (is_valid, normalized_priority) where priority is lowercase
    """
    valid_priority = ["low", "medium", "high"]
    priority_lower = priority.lower().strip()
    if priority_lower in valid_priority:
        return True, priority_lower
    return False, None


def validate_filename(filename: str) -> Tuple[bool, Optional[str]]:
    """
    Validate and sanitize a filename by removing invalid characters.

    Args:
        filename: Raw filename string

    Returns:
        Tuple of (is_valid, sanitized_filename) with spaces replaced by underscores
    """
    if not filename or not filename.strip():
        return False, None
    filename = filename.strip().replace(" ", "_")
    invalid_chars = ["/", "\\", ":", "*", "?", '"', "<", ">", "|"]
    for char in invalid_chars:
        filename = filename.replace(char, "")
    return True, filename


def validate_input(
    prompt: str,
    validator: Optional[Callable[[str], Tuple[bool, Optional[str]]]] = None,
    error_msg: str = "Invalid input, try again",
) -> str:
    """
    Prompt user for input with optional validation.

    Args:
        prompt: Message to display to the user
        validator: Optional validation function that returns (is_valid, validated_value)
        error_msg: Error message to display on validation failure

    Returns:
        Validated user input string
    """
    while True:
        user_input = input(prompt).strip()

        if not user_input:
            print("Empty input. Try again.")
            continue

        if validator:
            is_valid, validate_value = validator(user_input)
            if is_valid:
                return validate_value
            else:
                print(f"{error_msg}")
        else:
            return user_input
