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
    req = requests.get(url, headers={'User-agent': 'Holbietest'})
    if req.json().get("data").get("dist") == 0:
        print("None")

    links = req.json().get("data").get("children")
    for link in links:
        print(link.get("data").get("title"))
