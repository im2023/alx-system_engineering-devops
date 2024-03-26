#!/usr/bin/python3
"""The script is exporting data in JSON format"""
if __name__ == '__main__':
    import json
    import requests

    rsp_fil = requests.get(
        f'https://jsonplaceholder.typicode.com/users/'
    )
    json_string = {}
    for user_count in rsp_fil.json():
        USER_ID = user_count['id']
        USERNAME = user_count['username']
        rsp_task = requests.get(
            f'https://jsonplaceholder.typicode.com/todos/?userId={USER_ID}'
        )

        json_string[str(USER_ID)] = [
            {
                "username": USERNAME,
                "task": dict['title'],
                "completed": dict['completed'],
            }
            for dict in rsp_task.json()
        ]
    with open('todo_all_employees.json', 'w') as w:
        w.write(json.dumps(json_string))
