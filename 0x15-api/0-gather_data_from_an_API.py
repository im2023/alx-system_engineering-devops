#!/usr/bin/python3
"""returning information about
TODO list progress"""
import sys
import requests

def get_employee_todo_progress(employee_id):
    url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    response = requests.get(url)
    if response.status_code == 200:
        todos = response.json()
        EMPLOYEE_NAME = todos[0]['username']
        TOTAL_NUMBER_OF_TASKS = len(todos)
        done_tasks = [todo['title'] for todo in todos if todo['completed']]
        NUMBER_OF_DONE_TASKS = len(done_tasks)
        
        print(f"Employee {EMPLOYEE_NAME} is done with tasks({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")
        for task in done_tasks:
            print(f"\t{task}")
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    if not employee_id.isdigit():
        print("Employee ID must be an integer.")
        sys.exit(1)

    get_employee_todo_progress(int(employee_id))
