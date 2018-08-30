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
    url = "http://reddit.com/r/{}/hot/.json?after={}".format(subreddit, after)
    req = requests.get(url, headers={'User-agent': 'Holbietest'})
    try:
        links = req.json().get("data").get("children")
        if not links:
            print("None")
        else:
            after = req.json().get("data").get("after")
            for link in links:
                hot_list += (link.get("data").get("title"))
            if after is not None:
                recurse(subreddit, hot_list. after)
            return hot_list
    except Exception:
        print("None")
