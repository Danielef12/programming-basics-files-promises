from .modules.average_length import average_length_names_for_year
from .modules.diversity import name_diversity_analysis
from .modules.ending_name import name_endings_analysis
from .modules.initials_name import name_initial_analysis
from .modules.IO_utility import read_file
from .modules.popular_names import popular_name_for_decade, popular_name_gender

file_path = "data/babyNamesUSYOB-full.csv"


def menu() -> None:
    while True:
        print("Menu:")
        print("1. Popular name for specific year.")
        print("2. Diversity name for all years.")
        print("3. Average name filtered by year.")
        print("4. Ending name analysis.")
        print("5. Name initial analysis.")
        print("6. Popular name for decades analysis.")
        print("0. Exit program")

        choice = input("Enter your choice: ").strip()
        match choice:
            case "1":
                try:
                    year = int(input("Enter a year (1880-2015): "))
                    if 1880 <= year <= 2015:
                        data = read_file(file_path)
                        popular_name_gender(data, year)
                    else:
                        print("Invalid year!")
                except ValueError:
                    print("Insert a valid number!")
            case "2":
                name_diversity_analysis(data=read_file(file_path))
            case "3":
                average_length_names_for_year(data=read_file(file_path))
            case "4":
                name_endings_analysis(data=read_file(file_path))
            case "5":
                name_initial_analysis(data=read_file(file_path))
            case "6":
                popular_name_for_decade(data=read_file(file_path))
            case "0":
                print("Exiting...")
                break
