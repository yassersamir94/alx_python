import csv
import requests
import sys

import requests
import sys
import csv

# Function to fetch employee details and tasks
def fetch_employee_data(employee_id):
    user_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    todos_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos')

    if user_response.status_code == 200 and todos_response.status_code == 200:
        user_data = user_response.json()
        todos_data = todos_response.json()
        return user_data, todos_data
    else:
        print("Failed to fetch data from the API.")
        return None, None

# Function to export data to CSV
def export_to_csv(user_data, todos_data, employee_id):
    if user_data and todos_data:
        csv_filename = f'{employee_id}.csv'
        with open(csv_filename, 'w', newline='') as csvfile:
            fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for todo in todos_data:
                writer.writerow({
                    'USER_ID': user_data['id'],
                    'USERNAME': user_data['username'],
                    'TASK_COMPLETED_STATUS': str(todo['completed']),
                    'TASK_TITLE': todo['title']
                })

        print(f"Data exported to {csv_filename}.")
    else:
        print("Data export failed. Make sure the API endpoints are accessible.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    user_data, todos_data = fetch_employee_data(employee_id)
    export_to_csv(user_data, todos_data, employee_id)
