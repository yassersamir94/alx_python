import requests
import sys

def fetch_todo_list(employee_id):
    """
    Fetches the TODO list progress for a given employee ID from a REST API.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    # URL for the employee's TODO list
    todo_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    try:
        # Fetch data from the API
        response = requests.get(todo_url)
        todo_data = response.json()

        # Get employee name
        employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
        response = requests.get(employee_url)
        employee_data = response.json()
        employee_name = employee_data.get('name')

        # Count the number of completed tasks
        completed_tasks = [task for task in todo_data if task['completed']]
        num_completed_tasks = len(completed_tasks)

        # Display the employee's TODO list progress
        print(f"Employee {employee_name} is done with tasks ({num_completed_tasks}/{len(todo_data)}):")
        for task in completed_tasks:
            print(f"\t{task['title']}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        fetch_todo_list(employee_id)
    except ValueError:
        print("Error: Employee ID must be an integer.")
        sys.exit(1)
