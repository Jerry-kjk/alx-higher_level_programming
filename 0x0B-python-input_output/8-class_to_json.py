#!/usr/bin/python3
"""
Returns the dictionary description with simple data structure.
"""


def class_to_json(obj):
    """
    Create an empty dictionary to store the attributes.
    """
    return obj.__dict__
