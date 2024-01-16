#!/usr/bin/python3
# a function that queries the Reddit API
# Return - 0 on failire, 1 on success
import sys
from api import number_of_subscribers

def number_of_subscribers(subreddit):
    try:
        return number_of_subscribers
    if subreddit == 0:
        print("invalid subreddit")
    else:
        print("valid reddit")
