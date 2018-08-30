#!/usr/bin/python3
"""
Return first 10 hot posts
from a subreddit
"""
import json
import requests
import sys


def top_ten(subreddit):
    url = "http://reddit.com/r/{}/hot/.json?limit=10".format(subreddit)
    req = requests.get(url, headers={'User-agent': 'Holbietest'},
                       allow_redirects=False)
    try:
        print(req.json.get("data").get("children").get("data").get("title"))
    except:
        print("None")
