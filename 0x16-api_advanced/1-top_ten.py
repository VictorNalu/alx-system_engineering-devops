#!/usr/bin/python3
"""
Module to interact with the Reddit API
to fetch the top 10 hot posts for a subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of
    the first 10 hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    If not a valid subreddit, prints None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "python:reddit_api:v1.0 (by /u/yourusername)"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data["data"]["children"]
            for post in posts:
                print(post["data"]["title"])
        else:
            print(None)
    except requests.RequestException:
        print(None)
