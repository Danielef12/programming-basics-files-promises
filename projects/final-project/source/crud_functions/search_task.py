from pathlib import Path
from typing import Any, Dict, Optional

from source.config import BASE_DIR


def search_task(data: Dict[str, Dict[str, Any]]) -> Optional[Path]:
    """
    Interactive search to find and select a task file.

    Args:
        data: Dictionary containing "projects" and "list" task data

    Returns:
        Path to the selected task file, or None if selection was invalid
    """
    print("Select if task are in:")
    print("1. List tasks")
    print("2. Project tasks")

    choice = input("Select: ").strip()
    if choice == "1":
        if not data["list"]:
            print("No list found.")
            return None
        print("Available list")
        lists = list(data["list"].keys())
        for idx, list_name in enumerate(lists, 1):
            print(f"[{idx}]. {list_name}")

        try:
            selection = int(input("List number: ")) - 1
            if 0 <= selection < len(lists):
                return BASE_DIR / f"{lists[selection]}.json"
        except ValueError:
            print("Invalid selection.")
            return None
    elif choice == "2":
        if not data["projects"]:
            print("No project found.")
            return None
        print("Available project")
        projects = list(data["projects"].keys())
        for idx, project_name in enumerate(projects, 1):
            print(f"[{idx}]. {project_name}")
        try:
            selection = int(input("Project number: ")) - 1
            if 0 <= selection < len(projects):
                project_name = projects[selection]
                files = list(data["projects"][project_name].keys())
                print(f"File in {project_name}:")
                for idx, file_name in enumerate(files, 1):
                    print(f"[{idx}]. {file_name}")

                file_idx = int(input("Select file number: ")) - 1
                if 0 <= file_idx < len(files):
                    return BASE_DIR / project_name / f"{files[file_idx]}.json"
        except ValueError:
            print("Invalid selection.")
            return None
    else:
        print("Invalid selection.")
        return None
