import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]

    user_response = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(employee_id))
    user_data = user_response.json()

    todo_response = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'.format(employee_id))
    todo_data = todo_response.json()

    user_todo = {employee_id: [{"task": task['title'], "completed": task['completed'], "username": user_data['username']} for task in todo_data]}

    with open('{}.json'.format(employee_id), 'w') as file:
        json.dump(user_todo, file)
