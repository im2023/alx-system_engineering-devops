#!/usr/bin/python3
"""returning information about
TODO list progress"""

import requests
import sys

employeId = sys.argv[1]

rsp = requests.get(
    f'https://jsonplaceholder.typicode.com/users/{employeId}'
)
EMPLOYEE_NAME = rsp.json()['name']
tasks_response = requests.get(
    f'https://jsonplaceholder.typicode.com/todos/?userId={employeId}'
)
TOTAL_NUMBER_OF_TASKS = len(tasks_response.json())
NUMBER_OF_DONE_TASKS = 0
TASK_TITLE = ""
for dictionary in tasks_response.json():
    for key, value in dictionary.items():
        if key == 'completed' and value is True:
            NUMBER_OF_DONE_TASKS += 1
            TASK_TITLE += '\n'
            TASK_TITLE += '\t '
            TASK_TITLE += f"{dictionary['title']}"

print(
    f'Employee {EMPLOYEE_NAME} is done with tasks({NUMBER_OF_DONE_TASKS}/'
    f'{TOTAL_NUMBER_OF_TASKS}):', end=""
)
print(TASK_TITLE)
