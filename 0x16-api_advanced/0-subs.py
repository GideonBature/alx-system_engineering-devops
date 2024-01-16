#!/usr/bin/python3
"""queries the Reddit API and returns the number of
subscribers (not active users, total subscribers)
"""
import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API for the number of subscribers
    of a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The number of subscribers of the subreddit,
        or 0 if invalid
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "YourCustomUserAgentHere"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        try:
            data = response.json()
            return data["data"]["subscribers"]
        except KeyError:
            return 0

    else:
        return 0
