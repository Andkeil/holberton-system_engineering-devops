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
    url = "https://www.reddit.com/r/{}/hot.json?after={}".format(subreddit,
                                                                 after)
    req = requests.get(url, headers={'User-agent': 'Holbietest'})
    try:
        links = req.json().get("data").get("children")
        if not links:
            return None
        after = req.json().get("data").get("after")
        for link in links:
            hot_list.append(link.get("data").get("title"))
        if not after:
            return hot_list
        return recurse(subreddit, hot_list, after)
    except Exception:
        return None
