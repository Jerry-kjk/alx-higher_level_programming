#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """
    A base class for geometry-related operations.
    """

    def area(self):
        """
        Calculates the area of the geometry.

        Raises:
            Exception: If the area method is not implemented in the derived class.

        Returns:
            None
        """
        raise Exception("area() is not implemented")
