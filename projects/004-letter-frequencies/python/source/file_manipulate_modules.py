import os
from typing import Dict


def reading_input(path_or_text: str) -> str:
    if path_or_text.endswith(".txt"):
        if os.path.isfile(path_or_text):
            try:
                with open(path_or_text, "r") as f:
                    return f.read()
            except Exception as e:
                raise RuntimeError(f"Error reading {path_or_text}: {e}")
        else:
            raise FileNotFoundError(f"No such file or directory: {path_or_text}")
    else:
        return path_or_text


def cleaning_input(text: str) -> str:
    if text:
        return "".join(e for e in text if e.isalpha()).lower()
    else:
        return ""


def frequency_analysis(text_clean: str) -> Dict:
    frequencies = {}
    for letter in text_clean:
        frequencies[letter] = frequencies.get(letter, 0) + 1
    return dict(sorted(frequencies.items()))


def graphic_representation_horizontal(frequencies: dict) -> None:
    max_label_len = max(len(label) for label in frequencies)
    for label, value in frequencies.items():
        if value > 15:
            bar = "o" * int(value // 2)
        else:
            bar = "o" * value
        print(f"{label.rjust(max_label_len)} | {bar} ({value})")
