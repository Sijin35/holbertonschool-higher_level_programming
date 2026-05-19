#!/usr/bin/python3
"""

Defines a square module.
"""


class Square:
    """

    Represents a square with size validation and printing ability.
    """

    def __init__(self, size=0, position=(0, 0)):

        self.size = size
        self.position = position

    @property
    def size(self):

        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):

        return self.__position

    @position.setter
    def position(self, value):

        if (
            not isinstance(value, tuple) or
            not len(value) == 2 or
            not all(isinstance(i, int) for i in value) or
            not all(i >= 0 for i in value)
         ):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):

        return self.__size * self.__size

    def my_print(self):

        size = self.__size
        position = self.__position

        if size == 0:
            print()
            return

        for i in range(position[1]):
            print()
        for i in range(size):
            for i in range(position[0]):
                print(" ", end="")
            for i in range(size):
                print("#", end="")
            print()
