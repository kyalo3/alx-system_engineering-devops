#!/usr/bin/python3
# a function that queries the Reddit API
# Return - 0 on failire, 1 on success
import sys
import requests


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    headers = {'User-Agent': 'MyBot/1.0'}

    # Make a GET request to the Reddit API
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()

        return data['data']['subscibers']
    elif response.status_code == 404:
        return 0
    else:
        print(f"An error: {response.status_code}")
        return 0
