import json
import os
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Tuple

from source.crud_functions.search_task import search_task
from source.load_functions.load_json import load_json
from source.save_function.save_json import save_json


def delete_task(data: Dict[str, Dict[str, Any]]) -> None:
    """
    Delete a task from a file interactively.

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
        task_idx = int(input("Select task number to delete: ")) - 1
        if not (0 <= task_idx < len(tasks)):
            print("Invalid selection.")
            return
        task_name = tasks[task_idx]
        confirm = input(f"Delete task '{task_name['name']}'? [y/N]: ").strip().lower()
        if confirm == "y":
            tasks.pop(task_idx)
            save_json(path_file, tasks)
            print(f"Task '{task_name['name']}' deleted.")
        else:
            print("Delete cancelled.")
    except ValueError:
        print("Invalid selection.")
