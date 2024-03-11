#!/usr/bin/python3
"""
Script that, using a REST API, for a given employee ID, returns information about his/her TODO list progress.
"""

import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} employee_id".format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]

    # Fetching user data
    user_response = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(employee_id))
    user_data = user_response.json()
    employee_name = user_data.get('name')

    # Fetching todos data
    todos_response = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'.format(employee_id))
    todos_data = todos_response.json()

    # Calculating progress
    total_tasks = len(todos_data)
    completed_tasks = [task for task in todos_data if task.get('completed')]
    total_completed_tasks = len(completed_tasks)

    print("Employee {} is done with tasks({}/{}):".format(employee_name, total_completed_tasks, total_tasks))
    for task in completed_tasks:
        print("\t{}".format(task.get('title')))
