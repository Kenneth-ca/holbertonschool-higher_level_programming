#!/usr/bin/python3
"""
It takes a URL, sends a request and displays the value of a variable
"""
import urllib.request
from sys import argv


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(argv[1]) as response:
            print(response.headers.get('X-Request-Id'))
    except:
        pass
