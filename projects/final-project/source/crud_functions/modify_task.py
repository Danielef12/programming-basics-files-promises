from typing import Any, Dict

from source.crud_functions.search_task import search_task
from source.load_functions.load_json import load_json
from source.save_function.save_json import save_json
from source.validators.input_validators import validate_date, validate_priority


def modify_task(data: Dict[str, Dict[str, Any]]) -> None:
    """
    Modify an existing task interactively.

    Args:
        data: Dictionary containing "projects" and "list" task data
    """
    path_file = search_task(data)
    if not path_file:
        return

    tasks = load_json(path_file)
    if not tasks:
        print("No task found.")
        return

    print("Available task:")
    for idx, task in enumerate(tasks, 1):
        print(f"[{idx}]. {task['name']}  | {task['description']}")

    try:
        task_idx = int(input("Select task number to modify: ")) - 1
        if not (0 <= task_idx < len(tasks)):
            print("Invalid selection.")
            return

        task = tasks[task_idx]
        print(f"\nModifying task '{task['name']}'")
        print("(Press enter to maintenance actual value)")

        new_name = input(f"Name [{task['name']}]: ").strip()
        if new_name:
            task["name"] = new_name

        new_description = input(f"Description [{task['description']}]: ").strip()
        if new_description:
            task["description"] = new_description

        new_priority = input(
            f"Priority [{task['priority']}] (low, medium, high): "
        ).strip()
        if new_priority:
            is_valid, validated = validate_priority(new_priority)
            if is_valid:
                task["priority"] = validated

        new_date = input(f"Due date [{task['due_date']}] (gg-mm-yyyy): ").strip()
        if new_date:
            is_valid, validated = validate_date(new_date)
            if is_valid:
                task["due_date"] = validated

        save_json(path_file, tasks)
        print(f"Task '{task['name']}' updated.")
    except ValueError:
        print("Invalid selection.")
