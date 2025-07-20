import os
from typing import List


def read_file(directory_file_to_process: str) -> List[str]:
    try:
        content: List[str] = []
        for filename in os.listdir(directory_file_to_process):

            if filename.endswith(".txt"):
                file_path = os.path.join(directory_file_to_process, filename)
                try:
                    with open(file_path, "r") as file:
                        content.append(file.read())
                except FileNotFoundError:
                    print(f"File {filename} not found.")
                except Exception as e:
                    print(f"Error reading {filename}: {e}")
        return content
    except FileNotFoundError:
        print(f"File {directory_file_to_process} not found.")
    except Exception as e:
        print(f"Error reading {directory_file_to_process}: {e}")


def concatenate_files(content: List[str]) -> str:
    return "\n".join(content)


def clean_dataset(content_list: List[str]) -> str:
    clean_row = []
    set_header = False

    for argument in content_list:
        row = argument.strip().split("\n")

        for one_line in row:
            fields = [field.strip() for field in one_line.split(",")]

            if len(fields) != 4:
                continue

            if any(not f for f in fields):
                continue

            if not set_header:
                clean_row.append(",".join(fields))
                set_header = True
                continue

            name, category, price, quantity = fields

            try:
                float(price)
                int(quantity)
            except ValueError:
                continue

            clean_row.append(",".join([name, category, price, quantity]))
    return "\n".join(clean_row)


def save_file(file_name: str, data: str) -> None:
    try:
        with open(file_name, "w") as file:
            file.write(data)
        print(f"File {file_name} saved successfully.")
    except Exception as e:
        print(f"Error saving {file_name}: {e}")
