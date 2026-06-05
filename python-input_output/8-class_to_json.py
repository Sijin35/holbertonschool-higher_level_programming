#!/usr/bin/python3
"""Module that returns dictionary description with simple data structures"""



def class_to_json(obj):
    """Returns the dictionary description"""
    return obj.__dict__
