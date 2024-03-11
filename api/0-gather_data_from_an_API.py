#!/usr/bin/python3
"""
Checks student output for returning info from REST API
"""

import requests
import sys

users_url = "https://jsonplaceholder.typicode.com/users"
todos_url = "https://jsonplaceholder.typicode.com/todos"


def check_tasks(id):
    """ Fetch user name, number of tasks """

    resp = requests.get(todos_url).json()

    filename = 'student_output'
    count = 0
    with open(filename, 'r') as f:
        next(f)
        for line in f:
            count += 1
            # Check if the line starts with a tab followed by a space and ends with a newline
            if line.startswith('\t ') and line.endswith('\n'):
                print("Task {} Formatting: OK".format(count))
            else:
                print("Task {} Formatting: Incorrect".format(count))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <student_id>")
        sys.exit(1)
    check_tasks(int(sys.argv[1]))
