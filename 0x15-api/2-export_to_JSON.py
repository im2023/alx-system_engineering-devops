#!/usr/bin/python3
"""the script is exporting data in JSON format"""
if __name__ == '__main__':
    import json
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
    with open(f'{USER_ID}.json', 'w') as file:
        json_string = {
            str(USER_ID): [
                {
                    "task": dictionary['title'],
                    "completed": dictionary['completed'],
                    "username": USERNAME,
                }
                for dictionary in tasks_response.json()
            ]
        }
        file.write(json.dumps(json_string))
