#!/usr/bin/python3
"""
This is a Python script that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable found
in the header of the response using the packages urllib and sys
"""

from urllib import request
from sys import argv


if __name__ == "__main__":
    with request.urlopen(argv[1]) as response:
        print(response.getheader("X-Request-Id"))
