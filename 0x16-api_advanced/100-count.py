#!/usr/bin/python3
"""a recursive function that queries the Reddit API,
parses the title of all hot articles.
"""
import requests


def count_words(subreddit, word_list, hot_list=[], after=None, word_counts={}):
    """Recursively count keyword occurences in hot article
    titles from a subreddit.
    Args:
        subreddit (str): The name of the subreddit to query.
        word_list (list): List of keywords to count.
        hot_list (list, optional): List to store article titles,
        Defaults to [].
        after (str, optional): Pagination marker for the next page.
        Defaults to {}.
        word_counts (dict, optional): Dictionary to store word counts.
        Defaults to {}.

    Returns:
        None
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

            for title in hot_list:
                for word in word_list:
                    if word.lower() in title.lower():
                        word_counts[word.lower()] = \
                                word_counts.get(word.lower(), 0) + 1

            if data["data"]["after"]:
                count_words(subreddit, word_list, hot_list,
                            data["data"]["after"], word_counts)
            else:
                sorted_counts = sorted(word_counts.items(),
                                       key=lambda item: (-item[1], item[0]))
                for word, count in sorted_counts:
                    if count > 0:
                        print(f"{word}: {count}")
        except KeyError:
            pass
    else:
        pass
