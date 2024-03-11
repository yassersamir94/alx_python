import requests
import sys
import csv

def export_to_csv(employee_id):
    # Define the API endpoints
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    # Fetch user data
    user_data = requests.get(user_url).json()
    
    # Fetch todos for the user
    todos_data = requests.get(todos_url).json()

    # Prepare the CSV filename
    csv_filename = f"{employee_id}.csv"

    # Write data to CSV file
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
        
        # Write header
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        
        # Write data rows
        for todo in todos_data:
            writer.writerow([
                user_data['id'],
                user_data['username'],
                todo['completed'],
                todo['title']
            ])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)
    
    employee_id = sys.argv[1]
    export_to_csv(employee_id)
