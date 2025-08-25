from source.IO_modules.load_csv import load_csv
from source.IO_modules.save_csv import save_data
from source.csv_modules.add_column import add_column
from source.csv_modules.add_row import add_row
from source.csv_modules.data_visualize import data_visualize
from source.csv_modules.delete_column import delete_column
from source.csv_modules.delete_row import delete_row
from source.csv_modules.modify_value import modify_value
from source.csv_modules.order_data import (order_by_filmname,
                                    order_by_year,
                                    order_by_studio)
from source.menu_modules.print_menu import print_main_menu, sorting_menu
from source.validation_modules.input_validation import not_empty_input, validate_input_menu, insert_integer, confirm_input


def main():
    print("Command Line CSV File Editor")
    while (filepath := not_empty_input("\nEnter path to CSV file or type 'quit' to exit: ")) != "quit":

        print("Csv found. Loading...")
        dataset = load_csv(filepath)

        if dataset is None:
            continue

        if not dataset:
            print("No dataset provided")
            continue

        print("Csv loaded successfully.")
        print("\nCSV ANALYSIS")
        print(f"This dataset contains {len(dataset)} rows and {len(dataset[0])} columns.")
        while True:
            print_main_menu()
            selection = validate_input_menu("Select operation: ", 9)
            match selection:
                case "1":
                    data_visualize(dataset)
                case "2":
                    add_row(dataset)
                case "3":
                    add_column(dataset)
                case "4":
                    row_number = insert_integer("Enter row number: ")
                    column_name = not_empty_input("Enter new column name: ")
                    new_value = input("Enter new value: ")
                    modify_value(dataset, row_number, column_name, new_value)
                case "5":
                    row_number = insert_integer("Enter row number to delete: ")
                    delete_row(dataset, row_number)
                case "6":
                    if not dataset:
                        print("No data to delete")
                        continue
                    available_columns = list(dataset[0].keys())
                    print(f"Available columns: {', '.join(available_columns)}")
                    column_name = not_empty_input("Enter column name to delete: ")
                    if column_name not in available_columns:
                        print("Column '{column_name}' does not exist")
                        continue
                    if confirm_input(f"Are you sure you want to delete '{column_name}'? (y/n): "):
                        delete_column(dataset, column_name)
                        print(f"Column '{column_name}' deleted.")
                case "7":
                    sorting_menu()
                    while (selection := validate_input_menu("Select operation:", 4)) != "4":
                        match selection:
                            case "1":
                                order_year = order_by_year(dataset)
                                data_visualize(order_year)
                            case "2":
                                order_by_film = order_by_filmname(dataset)
                                data_visualize(order_by_film)
                            case "3":
                                order_studio = order_by_studio(dataset)
                                data_visualize(order_studio)
                            case "4":
                                print("Back to main menu")
                                break
                case "8":
                    save_data(dataset, filepath)
                case "9":
                    print("Exit")
                    break