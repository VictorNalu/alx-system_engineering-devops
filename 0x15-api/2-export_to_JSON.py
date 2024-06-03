#!/usr/bin/python3
"""
2-export_to_JSON.py: A script to fetch and export an employee's TODO list
progress in JSON format.
"""

import json
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
        return response.json().get("username")
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


def export_to_json(employee_id, username, todo_list):
    """
    Export the TODO list to a JSON file.

    Args:
        employee_id (int): The employee's ID.
        username (str): The username of the employee.
        todo_list (list): The list of TODO items.
    """
    tasks = [{
        "task": task.get("title"),
        "completed": task.get("completed"),
        "username": username
    } for task in todo_list]

    data = {str(employee_id): tasks}

    filename = f"{employee_id}.json"
    with open(filename, 'w') as file:
        json.dump(data, file)


def main(employee_id):
    """
    Main function to fetch and export the TODO list progress of an employee.

    Args:
        employee_id (int): The employee's ID.
    """
    username = get_employee_name(employee_id)
    if username is None:
        print(f"Employee with ID {employee_id} not found.")
        return
    todo_list = get_todo_list(employee_id)
    export_to_json(employee_id, username, todo_list)
    print(f"Data for employee ID {employee_id} has been exported to "
          f"{employee_id}.json")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    main(employee_id)
