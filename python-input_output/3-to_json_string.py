#!/usr/bin/python3
"""Module that returns JSON represenstaion of an object"""
import json


def to_json_string(my_obj):
    """Function that returns JSON reprenestation of string"""

    return json.dumps(my_obj)
