#!/usr/bin/python3
""" a function that queries the Reddit API """

import sys
import requests


def top_ten(subreddit):
    """the function prints the titles of 10 hot posts listed"""
    headers = {"User-Agent": "Kyalo3"}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    # Make a GET request to the Reddit API
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for i in range(10):
            print(posts[i]['data']['subscribers'])
    else:
        print(None)
