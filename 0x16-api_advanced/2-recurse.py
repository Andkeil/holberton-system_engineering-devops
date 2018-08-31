#!/usr/bin/python3
"""
Recursively return list
of all titles of hot links
in given subreddit
"""
import json
import requests
import sys


def recurse(subreddit, hot_list=[], after=""):
    url = "https://www.reddit.com/r/{}/hot.json?after={}&limit=100".\
          format(subreddit, after)
    req = requests.get(url, headers={'User-agent': 'Holbietest'})
    try:
        links = req.json().get("data").get("children")
        if not links:
            return None
        after = req.json().get("data").get("after")
        if after is None:
            return hot_list
        for link in links:
            hot_list += (link.get("data").get("title"))
        return recurse(subreddit, hot_list, after)
    except Exception:
        return None
