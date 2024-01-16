#!/usr/bin/python3
"""Recursive function that queries the Reddit API
and returns a list containing the titles of all
hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recursively fetches all hot article titles from a
    subreddit using the Reddit API.
    Args:
        subreddit (str): The name of the subreddit to query.
        hot_list (list, optional): List to store the titles. Defaults to [].
        after (str, optional): pagination marker for the next page.
        Defaults to None.

    Returns:
    list: List pf article titles, or None if an error occurs or the
    subreddit is invalid
    """

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    if after:
        url += f"?after={after}"

    user_agent = {"User-Agent": "kubuntu:konsole:v23.08.1 (by /u/0x83N3)"}

    response = requests.get(url, headers=user_agent)

    if response.status_code == 200:
        try:
            data = response.json()
            posts = data["data"]["children"]
            hot_list.extend(post["data"]["title"] for post in posts)

            if data["data"]["after"]:
                return recurse(subreddit, hot_list, data["data"]["after"])
            else:
                return hot_list
        except KeyError:
            return None
    else:
        return None
