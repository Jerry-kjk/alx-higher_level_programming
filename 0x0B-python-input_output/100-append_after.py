#!/usr/bin/python3
"""
Defines a text file insertion function.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Open the file in read mode
    """
    with open(filename, 'r') as file:
        lines = file.readlines()
    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)