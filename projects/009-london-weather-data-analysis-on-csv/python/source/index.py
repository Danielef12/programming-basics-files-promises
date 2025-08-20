from source.analysis_modules.analysis_generator import print_analysis
from source.analysis_modules.read_csv import read_csv


def main() -> None:
    filename = input("Enter the csv filename:")
    if not filename:
        filename = "../london_weather.csv"

    data = read_csv(filename)
    if not data:
        print("No data to analize. Exiting")
        return

    print(f"Dataset contain {len(data)} records")

    try:
        print_analysis(data)
    except Exception as e:
        print(f"Error: {e}")
