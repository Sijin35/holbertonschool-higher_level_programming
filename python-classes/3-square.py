#!/usr/bin/python3
"""

Defines a square module.
"""


class Square:
    """

    Represents a square with private attribute size and public method area.
    """

    def __init__(self, size=0):
        """

        Initializes a square with type/value verification.
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """

        Returns the current area of square.
        """

        return self.__size * self.__size
