#!/usr/bin/python3
"""
Writes a string to a text file.
"""


def write_file(filename="", text=""):
    """
    Open the file using the specified filename in
    write mode with UTF-8 encoding.
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        file.write(text)
        return len(text)
