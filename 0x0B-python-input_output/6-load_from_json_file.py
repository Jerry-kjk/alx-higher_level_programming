#!/usr/bin/python3
"""
Creates an Object from a “JSON file”
"""


import json


def load_from_json_file(filename):
    """
    Open the file using the specified filename
    in read mode with UTF-8 encoding.
    """
    with open(filename, mode="r", encoding="utf-8") as file:
        return json.load(file)
