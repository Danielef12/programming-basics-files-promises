import csv


def load_csv(filepath):
    try:
        data = []
        with open(filepath, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
        return data
    except FileNotFoundError:
        print(f"Csv '{filepath}' not found, verify path.")
        return []
    except Exception as e:
        print("Error loading csv:", e)
        return []