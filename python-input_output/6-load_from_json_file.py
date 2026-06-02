#!/usr/bin/python3
"""Module that creates an object from a JSON file"""
import json


def load_from_json_file(filename):
    """Creates object from JSON file"""

    with open(filename, "w", encoding="utf-8") as f:
        return json.load(f)
