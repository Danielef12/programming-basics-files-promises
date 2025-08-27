import json
from typing import Dict, List


def load_json(filename: str) -> List[Dict[str, str]]:
    try:
        with open(filename) as json_file:
            data = json.load(json_file)
            return data
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return []
    except json.JSONDecodeError as e:
        print(f"Error parsing json")
        return []
