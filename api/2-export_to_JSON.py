"""
    This script gathers employee todo data and stores it in JSON format
"""

import requests
import sys
import json

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 export_to_JSON.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    user_response = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(employee_id))
    user_data = user_response.json()
    employee_name = user_data.get('name')

    todos_response = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'.format(employee_id))
    todos_data = todos_response.json()

    completed_tasks = []
    for task in todos_data:
        task_dict = {
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": employee_name
        }
        completed_tasks.append(task_dict)

    filename = '{}.json'.format(employee_id)
    with open(filename, 'w') as json_file:
        json.dump({employee_id: completed_tasks}, json_file, indent=4)

    print("Data exported to", filename)
