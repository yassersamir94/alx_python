#!/usr/bin/python3
"""
Script that extends Task 0 to export data in CSV format.
"""

import csv
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} employee_id".format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]

    user_response = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(employee_id))
    user_data = user_response.json()
    employee_name = user_data.get('name')

    todos_response = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'.format(employee_id))
    todos_data = todos_response.json()

    filename = '{}.csv'.format(employee_id)

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            writer.writerow([employee_id, employee_name, task.get('completed'), task.get('title')])
