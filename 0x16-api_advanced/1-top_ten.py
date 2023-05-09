#!/usr/bin/python3
"""
Prints the titles of the first 10 hot posts
"""
import requests

def top_ten(subreddit):
    """
    This function queries the reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "MyRedditAPI/1.0"}
    params = {"limit": 10}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]

        for post in posts:
            title = post["data"]["title"]
            print(title)

    else:
        print(None)
