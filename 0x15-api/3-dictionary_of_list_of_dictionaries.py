#!/usr/bin/python3
"""
3-export_all_to_JSON.py: A script to fetch and export all employees' TODO list
progress in JSON format.
"""

import json
import requests


def get_all_employees():
    """
    Get all employees.

    Returns:
        list: A list of dictionaries containing employee data.
    """
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return []


def get_all_todo_lists():
    """
    Get all TODO lists.

    Returns:
        list: A list of dictionaries containing TODO items.
    """
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return []


def export_all_to_json(employees, todos):
    """
    Export all employees' TODO lists to a JSON file.

    Args:
        employees (list): A list of dictionaries containing employee data.
        todos (list): A list of dictionaries containing TODO items.
    """
    data = {}
    for employee in employees:
        employee_id = employee.get("id")
        username = employee.get("username")
        tasks = [
            {
                "username": username,
                "task": todo.get("title"),
                "completed": todo.get("completed"),
            }
            for todo in todos
            if todo.get("userId") == employee_id
        ]
        data[str(employee_id)] = tasks

    filename = "todo_all_employees.json"
    with open(filename, "w") as file:
        json.dump(data, file)


def main():
    """
    Main function to fetch and export all employees' TODO list progress.
    """
    employees = get_all_employees()
    todos = get_all_todo_lists()
    export_all_to_json(employees, todos)
    print("Data has been exported json")


if __name__ == "__main__":
    main()
