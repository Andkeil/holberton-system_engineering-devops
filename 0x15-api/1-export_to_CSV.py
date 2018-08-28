#!/usr/bin/python3
"""
Gather data from an API and export
in CSV format
"""
import csv
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

    with open('{}.csv'.format(sys.argv[1]), "w", newline='\n') as file:
        tasker = csv.writer(file, delimiter=',', quoting=csv.QUOTE_ALL)
        for i in range(0, len(response)):
            tasker.writerow([sys.argv[1]] + [username] +
                            [response[i].get("completed")] +
                            [response[i].get("title")])
