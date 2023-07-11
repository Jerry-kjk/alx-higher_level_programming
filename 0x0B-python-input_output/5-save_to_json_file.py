#!/usr/bin/python3
"""
Writes an Object to a text file.
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Open the file using the specified filename
    in write mode with UTF-8 encoding.
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        json.dump(my_obj, file)
