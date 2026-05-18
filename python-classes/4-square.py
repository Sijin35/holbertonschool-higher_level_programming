#!/usr/bin/python3
"""Defines a square module."""

class Square:
    """Represents a square with private attribute size and type/value verification
    which returns the current square area.
    """

    def __init__(self, size=0):
        """Initializes a square with private attribute size"""

        self.__size = size

    @size.retrieve
    def size(self):
        """Retrieves the size of the square."""

        return self.__size

    @size.set
    def size(self, value):
        """Sets the size of the square with type/value verification"""

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Returns the current square area"""

        return self.__size * self.__size
