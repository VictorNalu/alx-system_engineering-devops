#!/usr/bin/python3
"""
Module to interact with the Reddit
API to count keywords in the titles
of hot articles for a subreddit.
"""

import requests


def count_words(subreddit, word_list, hot_list=[], after=None, counts=None):
    """
    Recursively queries the Reddit API,
    parses the titles of all hot articles,
    and prints a sorted count of given keywords.

    Args:
        subreddit (str): The name of the subreddit to query.
        word_list (list): List of keywords to count.
        hot_list (list): List of hot article titles. Defaults to an empty list.
        after (str): The parameter for pagination. Defaults to None.
        counts (dict): Dictionary to store the counts of keywords.

    Prints:
        The sorted count of keywords in descending order,
        then alphabetically if counts are the same.
    """
    if counts is None:
        counts = {word.lower(): 0 for word in word_list}

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
                title = post["data"]["title"].lower().split()
                for word in word_list:
                    word_lower = word.lower()
                    counts[word_lower] += title.count(word_lower)
            after = data["data"]["after"]
            if after is not None:
                return count_words(
                    subreddit, word_list, hot_list, after, counts
                )
            else:
                sorted_counts = sorted(
                    [(k, v) for k, v in counts.items() if v > 0],
                    key=lambda item: (-item[1], item[0]),
                )
                for word, count in sorted_counts:
                    print(f"{word}: {count}")
        else:
            return
    except requests.RequestException:
        return
