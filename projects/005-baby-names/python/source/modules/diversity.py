def name_diversity_analysis(data: list[str, str]) -> list[tuple[int, int, int, int]]:
    year_diversity = {}

    for row in data:
        year = int(row["YearOfBirth"])
        name = row["Name"]
        gender = row["Sex"]

        if year not in year_diversity:
            year_diversity[year] = {"M": set(), "F": set()}

        year_diversity[year][gender].add(name)

    print("Year diversity analysis:\n")
    print("Year   Male    Female   Total\n")
    result = []
    for year in sorted(year_diversity.keys()):
        male_unique = len(year_diversity[year]["M"])
        female_unique = len(year_diversity[year]["F"])
        total = male_unique + female_unique

        print(f"{year}:   {male_unique}    {female_unique}     {total}")
        result.append((year, male_unique, female_unique, total))
    return result
