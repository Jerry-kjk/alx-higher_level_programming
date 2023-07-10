#!/usr/bin/python3
"""
Defines a Rectangle subclass Square.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class representing a square.
    """
    def __init__(self, size):
        """
        Initializes a Square instance with size.
        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is not a positive integer.
        """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
