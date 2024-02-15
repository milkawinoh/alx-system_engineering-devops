import requests
import sys

def get_employee_info(employee_id):
    # Base URL of the API
    base_url = 'https://jsonplaceholder.typicode.com'
    
    # API endpoint for user details
    user_endpoint = f'{base_url}/users/{employee_id}'
    
    # API endpoint for user's todos
    todos_endpoint = f'{base_url}/todos?userId={employee_id}'
    
    # Fetch user details
    user_response = requests.get(user_endpoint)
    user_data = user_response.json()
    employee_name = user_data['name']
    
    # Fetch todos
    todos_response = requests.get(todos_endpoint)
    todos_data = todos_response.json()
    
    # Calculate progress
    total_tasks = len(todos_data)
    completed_tasks = sum(1 for todo in todos_data if todo['completed'])
    
    # Display progress
    print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")
    for todo in todos_data:
        if todo['completed']:
            print(f"\t{todo['title']}")

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
