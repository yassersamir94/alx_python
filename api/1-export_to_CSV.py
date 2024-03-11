import csv
import requests
import sys

def export_to_csv(employee_id):
    # Fetch user info
    request_user = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    request_todos = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos')

    data_user = request_user.json()
    data_todos = request_todos.json()

    # Define CSV filename
    filename = f"{employee_id}.csv"

    # Write data to CSV
    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE'])
        for todo in data_todos:
            csv_writer.writerow([employee_id, data_user['name'], str(todo['completed']), todo['title']])

    print(f"CSV file '{filename}' created successfully.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    export_to_csv(employee_id)

def user_info(id):
    """ Check user information """

    total_tasks = 0
    response = requests.get(todos_url).json()
    for i in response:
        if i['userId'] == id:
            total_tasks += 1

    try:
        num_lines = 0
        with open(str(id) + ".csv", 'r') as f:
            for line in f:
                if not line == '\n':
                    num_lines += 1

        if total_tasks == num_lines:
            print("Number of tasks in CSV: OK")
        else:
            print("Number of tasks in CSV: Incorrect")
    except FileNotFoundError:
        print(f"CSV file {id}.csv not found.")
