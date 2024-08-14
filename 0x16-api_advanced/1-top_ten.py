#!/usr/bin/python3
"""Module to query Reddit API and print top 10 hot posts of a subreddit"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.

    :param subreddit: string, the name of the subreddit to query
    """
    # Set a custom User-Agent to avoid Too Many Requests errors
    headers = {'User-Agent': 'MyBot/0.0.1'}

    # Construct the URL for the subreddit's hot posts
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)

    try:
        # Make a GET request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if the request was successful and the subreddit is valid
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            
            # Extract and print the titles of the first 10 hot posts
            for post in data['data']['children']:
                print(post['data']['title'])
        else:
            # If the subreddit is invalid or any other error occurs, print None
            print(None)
    except:
        # If any exception occurs during the process, print None
        print(None)
