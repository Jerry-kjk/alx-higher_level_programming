#!/usr/bin/python3
"""
Takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and
displays the body of the response (decoded in utf-8).
"""

import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    data = parse.urlencode({'email': email})
    data = data.encode('ascii')
    with request.urlopen(url, data) as f:
        print(f.read().decode('utf-8'))
