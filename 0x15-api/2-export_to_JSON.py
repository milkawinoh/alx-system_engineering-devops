#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""

import json
import requests
import sys


if __name__ == '__main__':
    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/users"
    user_url = base_url + "/" + employee_id

    user_response = requests.get(user_url)
    username = user_response.json().get('username')

    todo_url = user_url + "/todos"
    todo_response = requests.get(todo_url)
    tasks = todo_response.json()

    todo_dictionary = {employee_id: []}
    for task in tasks:
        todo_dictionary[employee_id].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
        })
    with open('{}.json'.format(employee_id), 'w') as json_file:
        json.dump(todo_dictionary, json_file)
