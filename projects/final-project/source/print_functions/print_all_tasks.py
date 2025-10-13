from typing import Any, Dict


def print_all_tasks(data: Dict[str, Dict[str, Any]]) -> None:
    """
    Print all tasks from both projects and simple lists.

    Args:
        data: Dictionary containing "projects" and "list" task data
    """
    print("Print all project tasks")
    if not data["projects"]:
        print("No projects found")
    else:
        for project_name, files in data["projects"].items():
            print(f"{project_name.upper()}:")
            for file_name, tasks in files.items():
                print(f"    {file_name}.json ({len(tasks)} tasks)")
                for idx, task in enumerate(tasks, 1):
                    status = "completed" if task["completed"] else "in_progress"
                    print(
                        f"    [{idx}] {task['name']} | {task['description']} | {task['priority']} | {task['due_date']} | {status}"
                    )

    print("Simple list:")
    if not data["list"]:
        print("No list found.")
    else:
        for list_name, tasks in data["list"].items():
            print(f"\n {list_name}.json ({len(tasks)} tasks)")
            for idx, task in enumerate(tasks, 1):
                status = "completed" if task["completed"] else "in_progress"
                print(
                    f"    [{idx}] {task['name']} | {task['description']} | {task['priority']} | {task['due_date']} | {status}"
                )
