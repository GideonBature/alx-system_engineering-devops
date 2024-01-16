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

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    user_agent = {"User-Agent": "kubuntu:konsole:v23.08.1 (by /u/0x83N3)"}

    response = requests.get(url, headers=user_agent)
    data = response.json()

    try:
        return data["data"]["subscribers"]

    except Exception:
        return 0
