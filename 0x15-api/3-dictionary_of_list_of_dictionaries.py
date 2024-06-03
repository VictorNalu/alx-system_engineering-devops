#!/usr/bin/python3
"""
3-export_all_to_JSON.py: A script to fetch and export all employees' TODO list
progress in JSON format.
"""

import json
import requests

# Define the API endpoints
users_url = "https://jsonplaceholder.typicode.com/users"
todos_url = "https://jsonplaceholder.typicode.com/todos"

# Fetch data from the API
users_response = requests.get(users_url)
todos_response = requests.get(todos_url)

# Parse the JSON responses
users = users_response.json()
todos = todos_response.json()

# Create a dictionary to hold the tasks for each user
all_tasks = {}

# Process the data
for user in users:
    user_id = user["id"]
    username = user["username"]
    user_tasks = []
    for task in todos:
        if task["userId"] == user_id:
            task_info = {
                "username": username,
                "task": task["title"],
                "completed": task["completed"],
            }
            user_tasks.append(task_info)
    all_tasks[user_id] = user_tasks

# Export the data to a JSON file
with open("todo_all_employees.json", "w") as json_file:
    json.dump(all_tasks, json_file, indent=4)

print("Data has been exported to todo_all_employees.json")
