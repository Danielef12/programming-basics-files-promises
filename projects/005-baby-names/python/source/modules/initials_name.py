from typing import Any, List, Tuple


def name_initial_analysis(
    data: list[str, str], top_n: int = 5
) -> tuple[list[tuple[Any, int | Any]], list[tuple[Any, int | Any]]]:
    initials_male = {}
    initials_female = {}
    for row in data:
        name = row["Name"]
        gender = row["Sex"]
        number = int(row["Number"])
        first_char = name[0].upper()

        if gender == "M":
            initials_male[first_char] = initials_male.get(first_char, 0) + number
        elif gender == "F":
            initials_female[first_char] = initials_female.get(first_char, 0) + number

    top_initials_male = sorted(initials_male.items(), key=lambda x: x[1], reverse=True)[
        :top_n
    ]
    top_initials_female = sorted(
        initials_female.items(), key=lambda x: x[1], reverse=True
    )[:top_n]

    print(f"Top {top_n} initial names analysis (1880-2015):\n")
    print("Male names:")
    for i, (char, freq) in enumerate(top_initials_male, 1):
        print(f"{i}. -{char.upper()}: {freq}")

    print("Female names:")
    for i, (char, freq) in enumerate(top_initials_female, 1):
        print(f"{i}. -{char.upper()}: {freq}")

    return top_initials_male, top_initials_female
