#!/usr/bin/python3
"""
Defines a class Student.
"""


class Student:
    """
    Student class.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize the public instance attributes.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def to_json(self, attrs=None):
        """
        If attrs is not provided, retrieve all attributes.
        """
        if attrs is None or not isinstance(attrs, list):
            return self.__dict__
        return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
    
    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance
        with the key-value pairs from the JSON dictionary
        """
        for key, value in json.items():
            setattr(self, key, value)
