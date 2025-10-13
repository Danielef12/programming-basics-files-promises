import json
from pathlib import Path
from typing import Optional

from source.config import BASE_DIR


def create_new_file(file_name: str, path_dir: Optional[Path] = None) -> Path:
    """
    Create a new empty JSON file for tasks.

    Args:
        file_name: Name of the file (with or without .json extension)
        path_dir: Directory where the file will be created (defaults to BASE_DIR)

    Returns:
        Path to the created file
    """
    if not file_name.endswith(".json"):
        file_name += ".json"

    path = (path_dir or BASE_DIR) / file_name

    if not path.exists():
        with open(path, "w", encoding="utf-8") as file:
            json.dump([], file, indent=4)
        print(f"File {path} created.")
    else:
        print(f"File {path} already exists.")

    return path
