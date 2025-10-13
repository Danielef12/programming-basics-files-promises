import json
from pathlib import Path
from typing import Any, Dict, List


def load_json(path_file: Path) -> List[Dict[str, Any]]:
    """
    Load tasks from a JSON file.

    Args:
        path_file: Path to the JSON file to load

    Returns:
        List of task dictionaries, or empty list if file is invalid or empty
    """
    with open(path_file, "r", encoding="utf-8") as f:
        try:
            tasks = json.load(f)
            if not isinstance(tasks, list):
                tasks = []
        except json.JSONDecodeError:
            tasks = []
    return tasks
