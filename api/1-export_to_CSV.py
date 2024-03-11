import csv
import requests
import sys

# Check if the correct number of command-line arguments is provided
if len(sys.argv) != 2:
    print("Usage: python3 1-export_to_CSV.py <employee_id>")
    sys.exit(1)

# Retrieve the employee ID from the command-line argument
employee_id = sys.argv[1]

# Send requests to fetch user and TODO data
user_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}')
todos_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos')

# Check if requests are successful
if user_response.status_code != 200 or todos_response.status_code != 200:
    print("Failed to retrieve data from the API.")
    sys.exit(1)

# Parse JSON responses
user_data = user_response.json()
todos_data = todos_response.json()

# Count completed tasks
completed_tasks = sum(1 for todo in todos_data if todo['completed'])

# Prepare CSV file name
csv_filename = f"{employee_id}.csv"

# Write data to CSV file
with open(csv_filename, mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
    csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

    for todo in todos_data:
        csv_writer.writerow([user_data['id'], user_data['username'], todo['completed'], todo['title']])

# Print completion message
print(f"Data exported to {csv_filename} successfully.")
