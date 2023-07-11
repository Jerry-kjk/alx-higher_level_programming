#!/usr/bin/python3
"""
Defines a class Student.
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
        if isinstance(attrs, list):
            if all(isinstance(attr, str) for attr in attrs):
                res = {}
                for i in attrs:
                    if i in self.__dict__:
                        res[i] = self.__dict__[i]
                return res
        return self.__dict__
    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance
        with the key-value pairs from the JSON dictionary
        """
        for attr in json:
            self.__dict__[attr] = json[attr]
