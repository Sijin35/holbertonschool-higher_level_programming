#!/usr/bin/python3
"""Module that checks if object is an instance of, or
object is an instance of a class that inherited from specific class"""


def is_kind_of_class(obj, a_class):
    """Returns true if obj is instance of a_class or
    obj is instance of class that inherited from a_class"""

    return isinstance(obj, a_class)
