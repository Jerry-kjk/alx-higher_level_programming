#!/usr/bin/python3
"""
BaseGeometry
"""


class BaseGeometry:
    """
    A base class for geometry-related operations.
    """

    def area(self):
        """
        Calculates the area of the geometry.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates an integer value.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
