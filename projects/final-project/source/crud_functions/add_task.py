from typing import Any, Dict, Optional

from source.config import BASE_DIR
from source.crud_functions.new_list import create_new_file
from source.crud_functions.new_project import create_new_project
from source.load_functions.load_json import load_json
from source.save_function.save_json import save_json
from source.validators.input_validators import (validate_date, validate_input,
                                                validate_priority)


def add_task(
    task_type: str, task_file_name: str, project_name: Optional[str] = None
) -> None:
    """
    Add a new task to either a simple list or a project file.

    Args:
        task_type: Type of task location - either "list" or "project"
        task_file_name: Name of the file where the task will be saved
        project_name: Name of the project (required if task_type is "project")
    """
    name = validate_input("Enter task name: ")
    description = validate_input("Enter task description: ")
    priority = validate_input(
        "Enter task priority (low, medium, high): ",
        validate_priority,
        "Priority must be between low, medium, high",
    )
    due_date = validate_input("Enter task due date (gg-mm-yyyy): ", validate_date)

    new_task: Dict[str, Any] = {
        "name": name,
        "description": description,
        "priority": priority,
        "due_date": due_date,
        "completed": False,
    }

    if task_type == "list":
        path_file = BASE_DIR / f"{task_file_name}.json"
        if not path_file.exists():
            create_new_file(task_file_name, BASE_DIR)

    elif task_type == "project":
        if project_name is None:
            print("Project name is required")
            return
        path_project = BASE_DIR / project_name
        if not path_project.exists():
            create_new_project(project_name)
        path_file = create_new_file(task_file_name, path_project)

    else:
        print("Unknown task type, please choose from 'list' or 'project'")
        return

    tasks = load_json(path_file)
    tasks.append(new_task)
    save_json(path_file, tasks)

    print(f"Task '{name}' added to '{path_file}'")
