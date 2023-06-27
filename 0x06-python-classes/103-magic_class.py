#!/usr/bin/python3
"""MagicClass that does exactly Python bytecode"""

import math


class MagicClass:
     """Represent a circle."""

    def __init__(self, radius=0):
        # Private attribute to store the radius
        self.__radius = 0
        
        # Check if the radius argument is a number
        if type(radius) is not int and type(radius) is not float:
            # Raise a TypeError if the radius is not a number
            raise TypeError('radius must be a number')
        
        # Set the radius value
        self.__radius = radius
    
    def area(self):
        # Calculate and return the area of the circle
        return math.pi * (self.__radius ** 2)
    
    def circumference(self):
        # Calculate and return the circumference of the circle
        return 2 * math.pi * self.__radius

