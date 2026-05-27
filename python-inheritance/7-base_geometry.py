#!/usr/bin/python3
"""Module that creates class BaseGeometry"""


class BaseGeometry:
    """Represents class BaseGeometry with public instance methods"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):

        self.name = name
        self.value = value

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        if isinstance(value, bool):
            raise TypeError(f"{name} must be an integer")
