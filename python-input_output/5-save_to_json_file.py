#!/usr/bin/python3
"""Module that writes an object to text file using JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """Writes object using JSON representation"""

    with open(filename, "w", encoding="utf=8") as f:
        return json.dump(my_obj, f)
