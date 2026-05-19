#!/usr/bin/python3
"""

Defines a square module.
"""


class Square:
    """

    Represents a square with size validation and printing ability.
    """

    def __init__(self, size=0):
        """

        Initializes a square with attribute size which will be made private
        using the setter.
        """

        self.size = size

    @property
    def size(self):
        """

        Retrieves the current area of the square.
        """

        return self.__size

    @size.setter
    def size(self, value):
        """

        Sets the size of the squre with type/value verification.
        """

        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """

        Returns the current square area.
        """

        return self.__size * self.__size

    def my_print(self):
        """

        Prints in stdout the square with the character #.
        """

        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
