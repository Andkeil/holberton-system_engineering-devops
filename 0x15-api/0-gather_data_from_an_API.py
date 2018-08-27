#!/usr/bin/python3
"""
Gather employee data from an API
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
                            .format(sys.argv[1])).json().get("name")
    task_done = []
    task_count = 0

    for i in range(0, len(response)):
        if (response[i].get("completed")):
            task_done.append(response[i].get("title"))
            task_count += 1

    print("Employee {} is done with tasks({}/{}):".format(username,
                                                          task_count,
                                                          len(response)))
    for task in task_done:
        print("\t {}".format(task))
