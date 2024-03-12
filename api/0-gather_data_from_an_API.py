#!/usr/bin/python3
"""
Script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: {} employee_id".format(argv[0]))
        exit(1)

    employee_id = argv[1]

    # Fetching employee information
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)
    todo_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(employee_id)

    user_response = requests.get(user_url)
    todos_response = requests.get(todo_url)

    user_data = user_response.json()
    todos_data = todos_response.json()

    # Extracting required info
    employee_name = user_data.get('name')
    completed_tasks = [task for task in todos_data if task.get('completed')]
    total_tasks = len(todos_data)

    # Printing results
    print("Employee {} is done with tasks({}/{}):".format(employee_name,
                                                           len(completed_tasks),
                                                           total_tasks))

    for task in completed_tasks:
        print("\t {}".format(task.get('title')))
