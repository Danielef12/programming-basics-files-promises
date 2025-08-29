import json
import os
from typing import Any, Dict, List


def update_dataset(data: List[Dict[str, Any]], filepath: str) -> None:
    """Save the dataset to a JSON file, with option to overwrite or create a new file.

    Args:
        data (List[Dict[str, Any]]): Dataset of books.
        filepath (str): Original JSON filepath.
    """
    while True:
        overwrite = (
            input("Would you overwrite existent data? (yes/no): ").strip().lower()
        )
        if overwrite in ["y", "yes"]:
            save_name = filepath
            break
        elif overwrite in ["no", "n"]:
            base, ext = os.path.splitext(filepath)
            save_name = f"{base}_new{ext or '.json'}"
            break
    try:
        with open(save_name, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print(f"Data saved in '{save_name}'")
    except Exception as e:
        print(f"Error during the save: {e}")
