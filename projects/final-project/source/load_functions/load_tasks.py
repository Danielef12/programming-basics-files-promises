import json
from pathlib import Path
from typing import Any, Dict, List

from source.config import BASE_DIR


def load_all_tasks() -> Dict[str, Dict[str, Any]]:
    """
    Load all tasks from the BASE_DIR, including both simple lists and project files.

    Returns:
        Dictionary with two keys:
            - "list": tasks from simple JSON files
            - "projects": nested dictionary of project folders and their task files
    """
    tasks_data: Dict[str, Dict[str, Any]] = {"projects": {}, "list": {}}
    for file in BASE_DIR.iterdir():
        if file.is_file() and file.suffix == ".json":
            try:
                with open(file, "r", encoding="utf-8") as f:
                    tasks = json.load(f)
                    tasks_data["list"][file.stem] = tasks
                    print(f"Loaded {file.name} with {len(tasks)} tasks")
            except json.JSONDecodeError:
                print(f"Failed to load {file.name}")

        elif file.is_dir():
            project_name = file.name
            project_data: Dict[str, List[Dict[str, Any]]] = {}

            for json_file in file.glob("*.json"):
                try:
                    with open(json_file, "r", encoding="utf-8") as f:
                        tasks = json.load(f)
                        project_data[json_file.stem] = tasks
                        print(
                            f"Loaded {len(tasks)} from '{project_name}/{json_file.name}'"
                        )
                except json.JSONDecodeError:
                    print(f"Failed to load {json_file.name}")
            if project_data:
                tasks_data["projects"][project_name] = project_data

    return tasks_data
