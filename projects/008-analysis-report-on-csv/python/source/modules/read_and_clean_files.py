import csv


def read_csv(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=",")
            reader = (
                dict((k.strip(), v.strip()) for k, v in row.items() if v)
                for row in reader
            )
            data = list(reader)
            return data
    except FileNotFoundError:
        print(f"Error: '{filename}' not found.")
        return []
    except csv.Error:
        print("Error during the reading csv file")
        return []


def clean_data(data):
    if not data:
        return []
    cleaned_data = [row for row in data if all(row.values())]
    return cleaned_data
