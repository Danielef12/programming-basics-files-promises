import typing
from typing import Any, Dict, List, Tuple


def popular_name_gender(
    data: list[str, str], year: int, top_n: int = 10
) -> tuple[list[tuple[Any, int | Any]], list[tuple[Any, int | Any]]]:
    male_names: dict[str, int] = {}
    female_names: dict[str, int] = {}
    year_str = str(year)

    for row in data:
        if row["YearOfBirth"] == year_str:
            name = row["Name"]
            gender = row["Sex"]
            number = int(row["Number"])

            if gender == "M":
                male_names[name] = male_names.get(name, 0) + number
            elif gender == "F":
                female_names[name] = female_names.get(name, 0) + number

    top_male_names = sorted(male_names.items(), key=lambda x: x[1], reverse=True)[
        :top_n
    ]
    top_female_names = sorted(female_names.items(), key=lambda x: x[1], reverse=True)[
        :top_n
    ]

    print(f"Top {top_n} popular name of {year}\n")
    print("Male names:")
    for i, (name, freq) in enumerate(top_male_names, 1):
        print(f"{i}. {name}: {freq}")

    print("\nFemale names:")
    for i, (name, freq) in enumerate(top_female_names, 1):
        print(f"{i}. {name}: {freq}")

    return top_male_names, top_female_names


def popular_name_for_decade(
    data: list[str, str], top_n: int = 5
) -> dict[int, dict[str, list[tuple[Any, Any]]]]:
    decades = {}

    for row in data:
        year = int(row["YearOfBirth"])
        decade = (year // 10) * 10
        name = row["Name"]
        gender = row["Sex"]
        number = int(row["Number"])

        if decade not in decades:
            decades[decade] = {"M": {}, "F": {}}

        if name not in decades[decade][gender]:
            decades[decade][gender][name] = 0
        decades[decade][gender][name] += number

    print("Popular decades analysis:\n")

    results = {}
    for decade in sorted(decades.keys()):
        top_male = sorted(
            decades[decade]["M"].items(), key=lambda x: x[1], reverse=True
        )[:top_n]
        top_female = sorted(
            decades[decade]["F"].items(), key=lambda x: x[1], reverse=True
        )[:top_n]

        print(f" Year {decade}:")
        print("Male names:", end=" ")
        for name, freq in top_male:
            print(f"{name}({freq})", end=", ")

        print("\nFemale names:", end=" ")
        for name, freq in top_female:
            print(f"{name}({freq})", end=", ")
        print("\n")
        results[decade] = {"M": top_male, "F": top_female}
    return results
