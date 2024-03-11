import sys
import json
import urllib.request

def fetch_todo_list(employee_id):
    # Construct the URL for employee details and todo list
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todo_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    # Fetch data from the API
    try:
        with urllib.request.urlopen(user_url) as response:
            user_data = json.loads(response.read())
        
        with urllib.request.urlopen(todo_url) as response:
            todo_data = json.loads(response.read())
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None, None
    
    return user_data, todo_data

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    # Fetch data from the API
    user_data, todo_data = fetch_todo_list(employee_id)
    if not user_data or not todo_data:
        sys.exit(1)

    # Process the data
    employee_name = user_data.get('name')
    total_tasks = len(todo_data)
    done_tasks = sum(1 for task in todo_data if task.get('completed'))

    # Display the output
    print(f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")
    for task in todo_data:
        if task.get('completed'):
            print(f"\t{task.get('title')}")

if __name__ == "__main__":
    main()
