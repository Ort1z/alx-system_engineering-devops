#!/usr/bin/python3
"""Module to query the Reddit API and return the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers. 0 if the subreddit is invalid.
    """
    headers = {'User-Agent': 'MyBot/0.0.1'}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        return 0
    except Exception:
        return 0
