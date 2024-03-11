import requests
import sys

def gather_data(employee_id):
    # Construct the URLs for employee details and todo list
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    # Fetch employee details
    response_user = requests.get(user_url)
    response_todos = requests.get(todos_url)

    # Check if requests were successful
    if response_user.status_code != 200 or response_todos.status_code != 200:
        print("Failed to fetch data from the API")
        return

    # Extract JSON data
    user_data = response_user.json()
    todos_data = response_todos.json()

    # Calculate the number of completed tasks
    completed_tasks = [task for task in todos_data if task['completed']]
    num_completed_tasks = len(completed_tasks)

    # Display employee information
    print(f"Employee {user_data['name']} is done with tasks({num_completed_tasks}/{len(todos_data)}):")

    # Display titles of completed tasks
    for task in completed_tasks:
        print(f"\t {task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    gather_data(employee_id)
