import csv
from source.validation_modules.input_validation import confirm_input


def save_data(data, filepath):
    if overwrite := confirm_input('Do you want to overwrite existing data? (y/n): '):
        with open(filepath, 'w', newline='', encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
            print(f"Data saved successfully with name '{filepath}'")
    else:
        new_name = input("Enter new filename: ").strip()
        with open(new_name, 'w', newline='', encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
            print(f"Data saved successfully with name '{new_name}'")
