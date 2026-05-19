#!/usr/bin/python3
"""Defines a square module."""


class Square:
    """Represents a square with private attribute size and type/value verification
    which returns the current square area.
    """

    def __init__(self, size=0):
        """Initializes a square with attribute size which will be made private
        using the setter"""

        self.size = size

    @property
    def size(self):
        """Retrieves the size of the square."""

        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square with type/value verification"""

        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area"""

        return self.__size * self.__size
