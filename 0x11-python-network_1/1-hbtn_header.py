#!/usr/bin/python3
"""
It takes a URL, sends a request and displays the value of a variable
"""
import urllib.request
from sys import argv


if __name__ == "__main__":
    try:
        url = argv[1]
        with urllib.request.urlopen(url) as response:
            print(response.info()['X-Request-Id'])
    except:
        pass
