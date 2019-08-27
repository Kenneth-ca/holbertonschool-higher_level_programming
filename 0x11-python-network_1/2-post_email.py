#!/usr/bin/python3
"""
It takes a URL, sends a request and displays the value of a variable
"""
import urllib.request
import sys


if __name__ == "__main__":
    try:
        url = sys.argv[1]
        email = {'email': sys.argv[2]}
        data = urllib.parse.urlencode(email)
        data = data.encode('ascii')
        req = urllib.request.Request(url, data)
        with urllib.request.urlopen(req) as response:
            print(response.read().decode("utf-8"))
    except:
        pass
