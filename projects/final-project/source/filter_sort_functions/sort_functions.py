from typing import Any, Dict

from source.filter_sort_functions.utilities import (convert_data_to_object,
                                                    get_all_tasks_for_sort,
                                                    print_filtered_tasks)


def sort_tasks(data: Dict[str, Dict[str, Any]]) -> None:
    """
    Sort and display all tasks by various criteria.

    Args:
        data: Dictionary containing "projects" and "list" task data
    """
    all_tasks = get_all_tasks_for_sort(data)

    print("\n1. Sort by priority (high to low)")
    print("2. Due date (before -> after)")
    print("3. By name (A-Z)")
    print("4. By status (not completed)")
    choice = input("Select: ").strip()

    priority_order = {"high": 1, "medium": 2, "low": 3}
    if choice == "1":
        sorted_task = sorted(
            all_tasks, key=lambda t: priority_order.get(t.get("priority", "low"), 3)
        )
        print_filtered_tasks(sorted_task, "Sort by priority")
    elif choice == "2":
        sorted_task = sorted(
            all_tasks, key=lambda t: convert_data_to_object(t.get("due_date", ""))
        )
        print_filtered_tasks(sorted_task, "Sort by due_date")
    elif choice == "3":
        sorted_task = sorted(all_tasks, key=lambda t: t.get("name", "").lower())
        print_filtered_tasks(sorted_task, "Sort by name")
    elif choice == "4":
        sorted_task = sorted(
            all_tasks, key=lambda t: (t.get("completed", False), t.get("name", ""))
        )
        print_filtered_tasks(sorted_task, "Sort by status")
    else:
        print("Invalid selection.")
