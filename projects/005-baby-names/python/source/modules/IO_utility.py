import csv
import typing
from typing import List


def read_file(path: str) -> list[str]:
    data: list[str] = []
    try:
        with open(path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        print("File not found")
    except UnicodeDecodeError:
        print("Error: could not decode file")
    return data
