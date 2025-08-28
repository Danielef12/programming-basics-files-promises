import json
from typing import Dict, List


def load_json(filename: str) -> List[Dict[str, str]]:
    """
        Load data from a JSON file.

        Args:
            filename (str): Path to the JSON file.

        Returns:
            List[Dict[str, Any]]: Parsed JSON data as a list of dictionaries.
                Returns an empty list if the file is not found or contains invalid JSON.
        """
    try:
        with open(filename, encoding='utf-8') as json_file:
            data = json.load(json_file)
            return data
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return []
    except json.JSONDecodeError as e:
        print(f"Error parsing json")
        return []
