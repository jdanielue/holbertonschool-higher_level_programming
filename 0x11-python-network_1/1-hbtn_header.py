#!/usr/bin/python3
"""sends a request to the URL and displays the value of the X-Request-Id"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as r:
        html = r.info()
    print(html["X-Request-Id"])
