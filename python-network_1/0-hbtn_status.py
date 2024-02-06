#!/usr/bin/python3
"""
This script fetches https://alu-intranet.hbtn.io/status
and displays the body of the response in a specific format.
"""

import requests

def fetch_status():
    """
    Fetches the URL https://alu-intranet.hbtn.io/status
    and displays the body of the response in the required format.
    """
    url = 'https://alu-intranet.hbtn.io/status'
    response = requests.get(url)
    content_type = "<class '{}'>".format(type(response.text).__name__)
    content = response.text

    print("Body response:")
    print("\t- type: {}".format(content_type))
    print("\t- content: {}".format(content))

if __name__ == "__main__":
    fetch_status()
