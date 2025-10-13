from typing import Any, Dict

from source.crud_functions.search_task import search_task
from source.load_functions.load_json import load_json
from source.save_function.save_json import save_json


def mark_as_complete(data: Dict[str, Dict[str, Any]]) -> None:
    """
    Toggle the completion status of a task.

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
        task_idx = int(input("Select task number to mark as complete: ")) - 1
        if not (0 <= task_idx < len(tasks)):
            print("Invalid selection.")
            return
        task = tasks[task_idx]
        task["completed"] = not task.get("completed", False)
        status = "completed" if task["completed"] else "not completed"
        save_json(path_file, tasks)
        print(f"Task '{task['name']}' marked as '{status}'.")
    except ValueError:
        print("Invalid selection.")
