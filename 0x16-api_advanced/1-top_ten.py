#!/usr/bin/python3

"""
importing request module
"""

from requests import get


def top_ten(subreddit):
    """
    This is a function that queries the Reddit API and prints the titles of the
    first 10 hot posts listed for a given subreddit
    """

    if subreddit is None or not isinstance(subreddit, str):
        print("None")

    user_agent = {'User-agent': 'Chromium Version 113.0.5672.77'}
    params = {'limit': 10}
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)

    response = get(url, headers=user_agent, params=params)
    all_data = response.json()

    try:
        raw1 = all_data.get('data').get('children')

        for i in raw1:
            print(i.get('data').get('title'))

    except:
        print("None")
