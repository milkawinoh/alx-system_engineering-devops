import requests
import sys
import csv

def get_employee_info(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com'

    # Fetch user details
    user_response = requests.get(f'{base_url}/users/{employee_id}')
    user_data = user_response.json()
    employee_name = user_data['username']

    # Fetch todos
    todos_response = requests.get(f'{base_url}/todos?userId={employee_id}')
    todos_data = todos_response.json()

    # Write data to CSV file
    with open(f'{employee_id}.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for todo in todos_data:
            writer.writerow([employee_id, employee_name, todo["completed"], todo["title"]])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    try:
        employee_id = int(employee_id)
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    get_employee_info(employee_id)
