#!/usr/bin/python3
"""
Returns the JSON representation of an object.
"""


import json


def to_json_string(my_obj):
    """
    Use the json.dumps() function to convert
    the object to a JSON-formatted string.
    """
    return json.dumps(my_obj)
