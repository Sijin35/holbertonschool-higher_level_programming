#!/usr/bin/python3
"""Module that returns object represented by JSON string"""
import json


def from_json_string(my_obj):
    """Returns object (Python data structure) from JSON string"""

    return json.loads(my_obj)
