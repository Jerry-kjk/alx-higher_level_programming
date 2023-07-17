#!/usr/bin/python3
"""
Defines a square class.
"""

from models.rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """
        Class constructor for Square.
        Args:
            size (int): The size of the square.
            x (int, optional): The x-coordinate of the square's
            position.
            y (int, optional): The y-coordinate of the square's
            position.
            id (int, optional): The ID for the square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Get the size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Set the size of the square.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update the attributes of the square based on the provided
        arguments.
        Args:
            *args: The arguments representing the attribute values in the order:
                - 1st argument: id attribute
                - 2nd argument: size attribute
                - 3rd argument: x attribute
                - 4th argument: y attribute
            **kwargs : Dictionary of keyworded arguments.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """
        Return the dictionary representation of the Square.
        """
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """
        Return a string representation of the Square in the format:
        [Square] (<id>) <x>/<y> - <size>
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
