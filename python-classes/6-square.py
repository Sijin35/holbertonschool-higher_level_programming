#!/usr/bin/python3
"""

Defines a square module.
"""


class Square:
    """

    Represents a square with size validation and printing ability.
    """

    def __init__(self, size=0, position=(0,0)):
        """

        Initializes a square with attribute size which will be made private
        using the setter.
        """

        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """

        Retrieves the position.
        """

        return self.__position

    @position.setter
    def position(self, value):
        """

        Sets the position of the square to be printed.
        """

        self.__position = ()
        if self.__position[0] < 0 and self.__position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """

        Returns the current square area.
        """

        return self.__size * self.__size

    def my_print(self):
        """

        Prints in stdout the square with the character #.
        """
        size = self.__size
        position = self.__position

        if size == 0:
            print()

        for i in range(position[1]):
            print()
        for i in range(size):
            for i in range(position[0]):
                print(" ", end="")
            for i in range(size):
                print("#", end="")
            print()
