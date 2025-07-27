from typing import Any, List, Tuple


def name_endings_analysis(
    data: list[str, str], top_n: int = 5
) -> tuple[list[tuple[Any, int | Any]], list[tuple[Any, int | Any]]]:
    endings_male = {}
    endings_female = {}

    for row in data:
        name = row["Name"]
        gender = row["Sex"]
        number = int(row["Number"])
        last_char = name[-1].lower()

        if gender == "M":
            endings_male[last_char] = endings_male.get(last_char, 0) + number
        elif gender == "F":
            endings_female[last_char] = endings_female.get(last_char, 0) + number

    top_endings_male = sorted(endings_male.items(), key=lambda x: x[1], reverse=True)[
        :top_n
    ]
    top_endings_female = sorted(
        endings_female.items(), key=lambda x: x[1], reverse=True
    )[:top_n]

    print(f"Top {top_n} ending names analysis (1880-2015):\n")
    print("Male names:")
    for i, (char, freq) in enumerate(top_endings_male, 1):
        print(f"{i}. -{char.upper()}: {freq}")

    print("Female names:")
    for i, (char, freq) in enumerate(top_endings_female, 1):
        print(f"{i}. -{char.upper()}: {freq}")

    return top_endings_male, top_endings_female
