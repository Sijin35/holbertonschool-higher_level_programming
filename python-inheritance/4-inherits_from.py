#!/usr/bin/python3
"""Module that checks if object is instance of class
that inherited from specific class"""


def inherits_from(obj, a_class):
    """Returns True if obj is instnace of class that
    inherited from a_class directly or indirectly"""

    return isinstance(obj, a_class) and type(obj) is not a_class
