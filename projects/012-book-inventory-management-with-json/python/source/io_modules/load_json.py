import json
from json import JSONDecodeError
from typing import Any, Dict, List


def load_json(filepath: str) -> List[Dict[str, Any]]:
    """Load a JSON file and return its content as a list of dictionaries.

    Args:
        filepath (str): Path to the JSON file.

    Returns:
        List[Dict[str, Any]]: Parsed JSON data.
                              Returns an empty list if file not found or invalid.
    """
    try:
        with open(filepath, encoding="utf-8") as json_file:
            data = json.load(json_file)
            return data
    except FileNotFoundError:
        print(f"File '{filepath}' not found.")
        return []
    except JSONDecodeError as e:
        print(f"Error during load json: {e}")
        return []
