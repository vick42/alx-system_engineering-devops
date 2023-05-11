#!/usr/bin/python3
"""
A recursive function that queries the Reddit API
"""
import requests
import sys
after = None
count_dic = []


def count_words(subreddit, world_list):
    """
    parses the title of all hot articles, and prints a sorted list of given
    keywords (delimited by spaces, case-insensitive)
    """
    global after
    global count_dic
    headers = {'User-Agent': 'brave589'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'after': after}
    response = requests.get(url, headers=headers, allow_redirects=False,
                            params=parameters)
