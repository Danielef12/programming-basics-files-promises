def average_length_names_for_year(
    data: list[str, str]
) -> list[tuple[int, float, float]]:
    year_length_name = {}

    for row in data:
        year = int(row["YearOfBirth"])
        name = row["Name"]
        gender = row["Sex"]
        number = int(row["Number"])
        length = len(name)

        if year not in year_length_name:
            year_length_name[year] = {"M": [], "F": []}

        year_length_name[year][gender].extend([length] * number)

    print("Year length name analysis:\n")
    print("Year   Male    Female\n")
    results = []
    for year in sorted(year_length_name.keys()):
        if year_length_name[year]["M"] and year_length_name[year]["F"]:
            avg_male = sum(year_length_name[year]["M"]) / len(
                year_length_name[year]["M"]
            )
            avg_female = sum(year_length_name[year]["F"]) / len(
                year_length_name[year]["F"]
            )

            print(f"{year}:   {avg_male:.2f}    {avg_female:.2f}")
            results.append((year, avg_male, avg_female))
    return results
