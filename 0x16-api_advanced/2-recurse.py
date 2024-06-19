#!/usr/bin/python3
"""
Module to interact with the Reddit API
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API

    Args:
        subreddit (str): The name of the subreddit to query.
        hot_list (list): The list of titles of hot articles.
        after (str): The parameter for pagination. Defaults to None.

    Returns:
        list: The list of titles of hot articles
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "python:reddit_api:v1.0 (by /u/yourusername)"}
    params = {"after": after, "limit": 100}

    try:
        response = requests.get(
            url, headers=headers, params=params, allow_redirects=False
        )
        if response.status_code == 200:
            data = response.json()
            posts = data["data"]["children"]
            for post in posts:
                hot_list.append(post["data"]["title"])
            after = data["data"]["after"]
            if after is not None:
                return recurse(subreddit, hot_list, after)
            return hot_list
        else:
            return None
    except requests.RequestException:
        return None
