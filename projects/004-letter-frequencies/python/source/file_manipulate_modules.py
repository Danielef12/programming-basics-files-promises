import os
from typing import Dict


def reading_input(path_or_text: str) -> str:
    if not path_or_text.endswith(".txt"):
        return path_or_text
    if not os.path.isfile(path_or_text):
        raise FileNotFoundError(f"'{path_or_text}' not found")
    try:
        with open(path_or_text, "r", encoding="utf-8") as file:
            return file.read()
    except Exception as e:
        raise RuntimeError(f"Error reading {path_or_text}: {e}")


def cleaning_input(text: str) -> str:
    if text:
        return "".join(e for e in text if e.isalpha()).lower()
    else:
        return ""


def frequency_analysis(text_clean: str) -> Dict[str, int]:
    frequencies = {}
    for letter in text_clean:
        frequencies[letter] = frequencies.get(letter, 0) + 1
    return dict(sorted(frequencies.items()))


def graphic_representation_horizontal(frequencies: dict) -> None:
    max_label_len = max(len(label) for label in frequencies)
    for label, value in frequencies.items():
        if value > 15:
            bar = "o" * (value // 2)
        else:
            bar = "o" * value
        print(f"{label.rjust(max_label_len)} | {bar} ({value})")
