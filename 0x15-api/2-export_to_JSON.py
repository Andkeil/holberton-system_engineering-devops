#!/usr/bin/python3
"""
Gather employee data from an API
and export in JSON format
"""

import json
import requests
import sys


if __name__ == "__main__":
    """
    main
    """
    url = "https://jsonplaceholder.typicode.com/todos?userId={}" \
        .format(sys.argv[1])
    response = requests.get(url).json()
    username = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                            .format(sys.argv[1])).json().get("username")
    tasks = []

    for task in response:
        task_dct = {}
        task_dct["task"] = task.get('title')
        task_dct["completed"] = task.get("completed")
        task_dct["username"] = username
        tasks.append(task_dct)
    file_json = {}
    file_json[sys.argv[1]] = tasks
    with open("{}.json".format(sys.argv[1]), 'w') as file:
        json.dump(file_json, file)
