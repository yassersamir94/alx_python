import csv
import requests
import sys

def user_info(id):
    try:
        with open(str(id) + ".csv", 'r') as f:
            # Read CSV file and count the number of rows excluding the header
            num_tasks = sum(1 for _ in f) - 1
            print("Number of tasks in CSV: OK")
    except FileNotFoundError:
        print(f"CSV file for user {id} not found.")
        print("Number of tasks in CSV: Error")

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python3 main_0.py <employee_id>")
        sys.exit(1)

    # Retrieve the employee ID from the command-line argument
    employee_id = sys.argv[1]

    # Call user_info function with the employee ID
    user_info(int(employee_id))
