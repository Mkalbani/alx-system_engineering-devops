#!/usr/bin/python3
"""Number of subscribers therre are """
import requests


def number_of_subscribers(subreddit):
	"""
	Returns number of sub
	"""

	url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
	headers = {"User-Agent": "Mkothm"}

	response = requests.get(url, headers=headers, allow_redirects=False)

	if response.status_code == 404:
		return 0
	else:
		res = response.json().get("data")
		return res.get("subscribers")
