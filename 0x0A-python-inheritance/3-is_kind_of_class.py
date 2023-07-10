#!/usr/bin/python3
"""Defines a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of a specified class or an inherited class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if the object is an instance of the specified class or an inherited class; False otherwise.
    """
    if isinstance(obj, a_class):
        return True
    return False
