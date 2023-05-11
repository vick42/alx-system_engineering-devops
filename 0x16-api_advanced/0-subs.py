#!/usr/bin/python3
"""
Importing request module
"""

from requests import get


def number_of_subscribers(subreddit):
    """
    This is a function that queries the Reddit APIand returns the number
    of subscriber for a ginen subreddit.
    """

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-agent': 'Google Chromium Version 113.0.5672.77'}
    url = 'https://www.reddit.com/r/[]/about.json'.format(subreddit)
    response = get(url, headers=user_agent)
    all_data = response.json()

    try:
        return all_data.get('data').get('subscribers')

    except:
        return 0
