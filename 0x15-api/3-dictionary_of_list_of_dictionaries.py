#!/usr/bin/python3
"""
Gather all employee data from an API
and export dictionary list of
dictionaries in JSON
"""

import json
import requests
import sys


if __name__ == "__main__":
    """
    main
    """
    todo = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    dct_users = {}
    dct_usrnames = {}

    for user in users:
        ID = user.get("id")
        dct_users[ID] = []
        dct_usrnames[ID] = user.get('username')

    for task in todo:
        task_dct = {}
        ID = task.get("userId")
        task_dct["username"] = dct_usrnames.get(ID)
        task_dct["task"] = task.get('title')
        task_dct["completed"] = task.get("completed")
        dct_users.get(ID).append(task_dct)

    with open("todo_all_employees.json", 'w') as file:
        json.dump(dct_users, file)
