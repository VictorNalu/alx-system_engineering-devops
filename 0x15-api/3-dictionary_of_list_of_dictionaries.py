#!/usr/bin/python3
"""
3-export_all_to_JSON.py: A script to fetch and export all employees' TODO list
progress in JSON format.
"""

import json
import requests


def get_all_employees():
    """
    Get a list of all employees.

    Returns:
        list: A list of dictionaries containing employee details.
    """
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return []


def get_all_todos():
    """
    Get a list of all TODO items.

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
    Export all employees' TODO list to a JSON file.

    Args:
        employees (list): The list of employees.
        todos (list): The list of TODO items.
    """
    data = {}
    for employee in employees:
        user_id = employee.get("id")
        username = employee.get("username")
        data[user_id] = [{
            "username": username,
            "task": todo.get("title"),
            "completed": todo.get("completed")
        } for todo in todos if todo.get("userId") == user_id]

    filename = "todo_all_employees.json"
    with open(filename, 'w') as file:
        json.dump(data, file)


def main():
    """
    Main function to fetch and export the TODO list progress of all employees.
    """
    employees = get_all_employees()
    todos = get_all_todos()
    export_all_to_json(employees, todos)
    print("employees data have been exported to json")


if __name__ == "__main__":
    main()
