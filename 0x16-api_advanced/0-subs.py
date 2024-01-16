#!/usr/bin/python3
# a function that queries the Reddit API
# Return - 0 on failire, 1 on success
import sys
from api import number_of_subscribers


def number_of_subscribers(subreddit):
    result = number_of_subscribers(sys.argv[1])
    try:
        return number_of_subscribers
    except Exception as e:
        print(f"An error: {e}")
        return 0
