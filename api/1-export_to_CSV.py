import requests
import sys
import csv

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
