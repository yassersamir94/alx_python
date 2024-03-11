import csv
import requests
import sys

id = sys.argv[1]

request_user = requests.get('https://jsonplaceholder.typicode.com/users/'+id)
request_todos = requests.get('https://jsonplaceholder.typicode.com/users/'+id+'/todos')

data_user = request_user.json()
data_todos = request_todos.json()

completed_tasks = []

for item in data_todos:
    if item.get('completed') == True:
        completed_tasks.append(item)

csv_filename = f"{id}.csv"

with open(csv_filename, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
    
    for task in completed_tasks:
        csv_writer.writerow([id, data_user.get('name'), str(task.get('completed')), task.get('title')])

print(f"Data exported to {csv_filename}")
