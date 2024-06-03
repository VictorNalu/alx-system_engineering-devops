#!/usr/bin/python3
"""
0-gather_data_from_an_API.py: A script to fetch and display an employee's
TODO list progress.
"""

import requests
import sys


def get_employee_name(employee_id):
    """
    Get the employee's name using the employee ID.

    Args:
        employee_id (int): The employee's ID.

    Returns:
        str: The name of the employee.
    """
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get("name")
    return None


def get_todo_list(employee_id):
    """
    Get the TODO list of an employee using the employee ID.

    Args:
        employee_id (int): The employee's ID.

    Returns:
        list: A list of dictionaries containing TODO items.
    """
    url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return []


def main(employee_id):
    """
    Main function to fetch and display the TODO list progress of an employee.

    Args:
        employee_id (int): The employee's ID.
    """
    employee_name = get_employee_name(employee_id)
    if employee_name is None:
        print(f"Employee with ID {employee_id} not found.")
        return

    todo_list = get_todo_list(employee_id)
    total_tasks = len(todo_list)
    done_tasks = [task for task in todo_list if task.get("completed")]
    done_tasks_count = len(done_tasks)

    print(f"Employee {employee_name} is done with tasks({done_tasks_count}/"
          f"{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    main(employee_id)
