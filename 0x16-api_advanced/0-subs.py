#!/usr/bin/python3
"""
Return number of subscribers
to subreddit
"""
import json
import requests
import sys


def number_of_subscribers(subreddit):
    url ="http://reddit.com/r/{}/about/.json".format(sys.argv[1])
    req = requests.get(url, headers={'User-agent': 'Holbietest'})
    try:
        return (int(req.json().get("data").get("subscribers")))
    except:
        return (0)
