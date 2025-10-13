import json
import os
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Tuple

from source.filter_sort_functions.utilities import (convert_data_to_object,
                                                    get_all_tasks_for_sort,
                                                    print_filtered_tasks)


def filter_by_priority(data: Dict[str, Dict[str, Any]]) -> None:
    """
    Filter and display tasks by priority level.

    Args:
        data: Dictionary containing "projects" and "list" task data
    """
    all_tasks = get_all_tasks_for_sort(data)

    print("Select filter priority: 1=low, 2=medium, 3=high")
    priority_map = {"1": "low", "2": "medium", "3": "high"}
    choice = input("Select filter priority: ").strip()
    if choice in priority_map:
        priority = priority_map[choice]
        filtered = [t for t in all_tasks if t.get("priority") == priority]
        print("Tasks filtered by priority:")
        for task in filtered:
            print(f"[{task['name']}] | {task['description']} | {task['priority']}")


def filter_by_status_complete(data: Dict[str, Dict[str, Any]]) -> None:
    """
    Filter and display only completed tasks.

    Args:
        data: Dictionary containing "projects" and "list" task data
    """
    all_tasks = get_all_tasks_for_sort(data)
    filtered = [t for t in all_tasks if t.get("completed", True) == True]
    print("Tasks completed:")
    for task in filtered:
        status = "completed" if task["completed"] else "not completed"
        print(f"Task '{task['name']}'  | {task['description']} | {status}")


def filter_by_due_date(data: Dict[str, Dict[str, Any]]) -> None:
    """
    Filter and display tasks by due date range.

    Args:
        data: Dictionary containing "projects" and "list" task data
    """
    all_tasks = get_all_tasks_for_sort(data)
    today = datetime.today().date()

    print("1. Expired")
    print("2. Today")
    print("3. This week")
    print("4. Next 30 days")

    choice = input("Select filter due date: ").strip()
    if choice == "1":
        filtered = [
            t
            for t in all_tasks
            if convert_data_to_object(t.get("due_date", "")).date() < today
        ]
        print_filtered_tasks(filtered, "Expired tasks")
    elif choice == "2":
        filtered = [
            t
            for t in all_tasks
            if convert_data_to_object(t.get("due_date", "")).date() == today
        ]
        print_filtered_tasks(filtered, "Expire today")
    elif choice == "3":
        week = today + timedelta(days=7)
        filtered = [
            t
            for t in all_tasks
            if convert_data_to_object(t.get("due_date", "")).date() <= week
        ]
        print_filtered_tasks(filtered, "Expire this week")
    elif choice == "4":
        month = today + timedelta(days=30)
        filtered = [
            t
            for t in all_tasks
            if convert_data_to_object(t.get("due_date", "")).date() <= month
        ]
        print_filtered_tasks(filtered, "Expired this month")
    else:
        print("Invalid selection.")
