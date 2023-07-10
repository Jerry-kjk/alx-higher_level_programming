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

        Raises:
            Exception: If the area method is not implemented in the derived class.

        Returns:
            None
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates an integer value.

        Args:
            name (str): The name of the value.
            value: The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.

        Returns:
            None
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
