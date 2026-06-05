#!/usr/bin/python3
"""Module that defines a class Student"""


class Student:
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        """Instantiates an object"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves dictionary representation of Student instance"""

        if attrs is None:
            return self.__dict__
        else:
            result = {}
            for k in attrs:
                if k in self.__dict__:
                    result[k] = self.__dict__[k]
            return result
