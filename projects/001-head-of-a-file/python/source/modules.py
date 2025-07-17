import os
from typing import List


def reading_file(filepath) -> List[str]:
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"\n[ERROR] File not found: {filepath}")


def head_of_a_file(filepath, line_display=10, show_filename=False):
    lines = reading_file(filepath)
    if not lines:
        return

    if show_filename:
        print(f"\n===> {os.path.basename(filepath)} <===")

    for line in lines[:line_display]:
        print(line.strip())
