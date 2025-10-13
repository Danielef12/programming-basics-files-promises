from datetime import datetime
from typing import Any, Dict, List


def convert_data_to_object(date_str: str) -> datetime:
    """
    Convert a date string to a datetime object.

    Args:
        date_str: Date string in either "dd-mm-yyyy" or "dd/mm/yyyy" format

    Returns:
        Datetime object, or datetime.max if parsing fails
    """
    try:
        return datetime.strptime(date_str, "%d-%m-%Y")
    except:
        try:
            return datetime.strptime(date_str, "%d/%m/%Y")
        except:
            return datetime.max


def get_all_tasks_for_sort(data: Dict[str, Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Flatten all tasks from projects and lists into a single list with source information.

    Args:
        data: Dictionary containing "projects" and "list" task data

    Returns:
        List of tasks with added "source" field indicating origin
    """
    all_tasks: List[Dict[str, Any]] = []

    for list_name, tasks in data["list"].items():
        for task in tasks:
            task_copy = task.copy()
            task_copy["source"] = f"{list_name}"
            all_tasks.append(task_copy)

    for project_name, files in data["projects"].items():
        for file_name, tasks in files.items():
            for task in tasks:
                task_copy = task.copy()
                task_copy["source"] = f"{project_name}/{file_name}"
                all_tasks.append(task_copy)

    return all_tasks


def print_filtered_tasks(
    tasks: List[Dict[str, Any]], title: str = "Tasks filtered"
) -> None:
    """
    Print a list of tasks with formatting.

    Args:
        tasks: List of task dictionaries to print
        title: Title to display above the task list
    """
    if not tasks:
        print("No task found.")
        return

    print(f"\n{title.upper()} ({len(tasks)} tasks)")
    for idx, task in enumerate(tasks, 1):
        status = "completed" if task.get("completed") else "not completed"
        print(
            f"\n [{idx}]. {task['name']} | {task['description']} | {status} | {task['due_date']}"
        )
        print(f"{task['source']}")
