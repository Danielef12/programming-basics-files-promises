from typing import Any, Dict

from source.filter_sort_functions.filter_functions import (
    filter_by_due_date, filter_by_priority, filter_by_status_complete)
from source.filter_sort_functions.sort_functions import sort_tasks


def filtered_menu(data: Dict[str, Dict[str, Any]]) -> None:
    """
    Display the filter and sort menu and handle user selections.

    Args:
        data: Dictionary containing "projects" and "list" task data
    """
    print("Order and filter menu:")
    print("1. Filter by priority")
    print("2. Filter by status")
    print("3. Filter by due_date")
    print("4. Order tasks ")
    print("5. Back to main menu")

    choice = input("Select menu: ").strip()
    if choice == "1":
        filter_by_priority(data)
    elif choice == "2":
        filter_by_status_complete(data)
    elif choice == "3":
        filter_by_due_date(data)
    elif choice == "4":
        sort_tasks(data)
    elif choice != "5":
        print("Invalid selection.")
