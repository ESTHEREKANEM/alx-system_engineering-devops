#!/usr/bin/python3

"""
returns the number of subscribers
"""
import requests

def number_of_subscribers(subreddit)
    """
    This function queries the Reddit API and returns the number of subscribers 
    (not active users, total subscribers) for a given subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "MyRedditAPI/1.0"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        subscribers = data["data"]["subscribers"]
        return subscribers
    elif response.status_code == 404:
        return 0
    else:
        return 0
