#!/usr/bin/python3
"""Module to query the Reddit API and return the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    for a given subreddit.
    
    :param subreddit: string, the name of the subreddit
    :return: int, number of subscribers. 0 if the subreddit is invalid.
    """
    # Set a custom User-Agent to avoid Too Many Requests errors
    headers = {'User-Agent': 'MyBot/0.0.1'}
    
    # Construct the URL for the subreddit's about.json
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    
    try:
        # Make a GET request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            # Extract and return the number of subscribers
            return data['data']['subscribers']
        else:
            # If the subreddit is invalid or any other error occurs, return 0
            return 0
    except:
        # If any exception occurs during the process, return 0
        return 0
