#!/usr/bin/python3
""" a function that queries the Reddit API """

import sys
import requests


def top_ten(subreddit):
    """the function prints the titles of 10 hot posts listed"""
    headers = {"User-Agent": "MyBot/0.0.1"}
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)

    # Make a GET request to the Reddit API
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return
