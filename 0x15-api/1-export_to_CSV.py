#!/usr/bin/python3
"""The Script is exporting data in CSV format"""
if __name__ == '__main__':
    import requests
    import sys

    USER_ID = sys.argv[1]

    response = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{USER_ID}'
    )
    USERNAME = response.json()['username']
    tasks_response = requests.get(
        f'https://jsonplaceholder.typicode.com/todos/?userId={USER_ID}'
    )
    with open(f'{USER_ID}.csv', 'w') as file:
        for dict in tasks_response.json():
            TASK_COMPLETED_STATUS = dict['completed']
            TASK_TITLE = dict['title']
            file.write(
                f'"{USER_ID}","{USERNAME}","{TASK_COMPLETED_STATUS}","{TASK_TITLE}"\n'
            )