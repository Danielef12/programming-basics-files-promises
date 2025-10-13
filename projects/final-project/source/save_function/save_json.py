import json
from pathlib import Path
from typing import Any, Dict, List


def save_json(path_file: Path, tasks: List[Dict[str, Any]]) -> None:
    """
    Save tasks to a JSON file.

    Args:
        path_file: Path where the JSON file will be saved
        tasks: List of task dictionaries to save
    """
    with open(path_file, "w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=2)
