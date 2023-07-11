#!/usr/bin/python3
"""
Appends a string at the end of a text file.
"""


def append_write(filename="", text=""):
    """
    Open the file using the specified filename
    in append mode with UTF-8 encoding.
    """
    with open(filename, mode="a", encoding="utf-8") as file:
        file.write(text)
        return len(text)
