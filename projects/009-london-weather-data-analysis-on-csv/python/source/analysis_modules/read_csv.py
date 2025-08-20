import csv
from typing import Dict, List


def read_csv(filename: str) -> List[Dict[str, str]]:
    data: List[Dict[str, str]] = []
    try:
        with open(filename, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
        print(f"Loaded {len(data)} record from {filename}")
        return data
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
        return []
    except Exception as e:
        print(f"Error reading file: {e}")
        return []
