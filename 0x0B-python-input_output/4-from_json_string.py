#!/usr/bin/python3
"""
Returns an object."""


import json


def from_json_string(my_str):
    """
    Use the json.loads() function to convert the JSON
    string to a Python data structure.
    """
    return json.loads(my_str)
