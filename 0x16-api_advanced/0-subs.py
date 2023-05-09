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
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {"User-Agent": "MyRedditAPI/1.0"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data.get('data').get('subscribers')
    else:
        return 0
