from pathlib import Path

from source.config import BASE_DIR


def create_new_project(project_name: str) -> Path:
    """
    Create a new project directory.

    Args:
        project_name: Name of the project to create

    Returns:
        Path to the created project directory
    """
    path_project = BASE_DIR / project_name
    if path_project.exists():
        print(f"Project '{project_name}' already exists")
        return path_project
    path_project.mkdir(parents=True, exist_ok=True)
    print(f"Project {project_name} created in: {path_project}")
    return path_project
