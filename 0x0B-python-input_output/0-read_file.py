#!/usr/bin/python3
"""
Reads a text file-reading function.
"""


def read_file(filename=""):
    """
    Open the file using the specified filename and UTF-8 encoding.
    """
    with open(filename, encoding="utf-8") as file:
        for line in file:
            print(line, end="")
