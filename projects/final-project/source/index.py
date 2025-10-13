from pathlib import Path

from source.config import BASE_DIR
from source.crud_functions.add_task import add_task
from source.crud_functions.delete_task import delete_task
from source.crud_functions.mark_complete import mark_as_complete
from source.crud_functions.modify_task import modify_task
from source.crud_functions.new_list import create_new_file
from source.crud_functions.new_project import create_new_project
from source.filter_sort_functions.filter_menu import filtered_menu
from source.load_functions.load_tasks import load_all_tasks
from source.print_functions.print_all_tasks import print_all_tasks
from source.validators.input_validators import (validate_filename,
                                                validate_input)


def main_menu() -> None:
    """
    Main function that runs the Advanced Task Management System.
    Displays the main menu and handles user interactions.
    """
    print("Welcome to Advanced Task Management System")
    while True:
        print("What would you like to do?")
        print("1. View all tasks")
        print("2. Create new task")
        print("3. Modify existing task")
        print("4. Delete existing task")
        print("5. Mark task as completed")
        print("6. Create new project")
        print("7. Create a simple ToDo List")
        print("8. Filter and order tasks")
        print("9. Exit")
        choice = input("Enter choice: ").strip()
        if choice not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            print("Invalid choice.")
            continue
        data = load_all_tasks()
        match choice:
            case "1":
                print_all_tasks(data)
            case "2":
                selection = input(
                    "Task will be created in a simple list (1) or in a project(2)? "
                )
                if selection == "1":
                    list_name = validate_input(
                        "Enter list name: ", validate_filename, "Invalid file name."
                    )
                    add_task("list", list_name)
                elif selection == "2":
                    project_name = validate_input(
                        "Enter project name: ",
                        validate_filename,
                        "Invalid project name.",
                    )
                    file_name = validate_input(
                        "Enter file name or category: ",
                        validate_filename,
                        "Invalid file name.",
                    )
                    add_task("project", file_name, project_name)
                else:
                    print("Invalid choice.")
                    return

            case "3":
                modify_task(data)

            case "4":
                delete_task(data)

            case "5":
                mark_as_complete(data)
            case "6":
                project_name = input("Enter project name: ")
                directory_project = create_new_project(project_name)
                print("Project created")
                add_file = input("want to add a new task file? (y/n): ")
                if add_file == "y":
                    file_name = input("Enter file name: ")
                    create_new_file(file_name, directory_project)
                    print(f"File {file_name} created in: {directory_project}")

            case "7":
                list_name = validate_input(
                    " Enter ToDo list name: ", validate_filename, "Invalid file name."
                )
                create_new_file(list_name, BASE_DIR)
                print(f"List '{list_name}' created in: {BASE_DIR}")
            case "8":
                filtered_menu(data)

            case "9":
                print("Thank you for using Advanced Task Management System")
                break

            case _:
                print("Invalid choice.")
