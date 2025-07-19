from typing import List


def read_file(filename: str) -> List[str]:
    try:
        with open(filename, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"File {filename} not found")
        return


def tail_of_a_file(filename: str, start_line: int = 0, number_lines: int = 10) -> None:
    lines = read_file(filename)
    if not lines:
        return
    if start_line > 0:
        for line in lines[start_line:]:
            print(line.strip())
    else:
        for line in lines[len(lines) - number_lines:]:
            print(line.strip())
