import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]

    # Retrieve user data
    user_response = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(employee_id))
    user_data = user_response.json()
    username = user_data.get('username')

    # Retrieve todos data
    todos_response = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'.format(employee_id))
    todos_data = todos_response.json()

    # Prepare JSON data
    json_data = {employee_id: []}

    for task in todos_data:
        json_data[employee_id].append({
            'task': task['title'],
            'completed': task['completed'],
            'username': username
        })

    # Write JSON data to file
    filename = '{}.json'.format(employee_id)
    with open(filename, 'w') as json_file:
        json.dump(json_data, json_file)

    print("Data exported to", filename)
