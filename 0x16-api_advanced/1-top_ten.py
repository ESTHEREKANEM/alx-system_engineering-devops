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
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "MyRedditAPI_project"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]
        for post in posts:
            title = post["data"]["title"]
            print(title)
    else:
        print(None)
