#!/usr/bin/python3
"""Module to serialie Python dict to JSON and vice versa"""
import json


def serialize_and_save_to_file(data, filename):
    """Serizlizes dict to JSON"""

    with open(filename, "w", encoding="utf=8") as f:
        return json.dump(data, f)

def load_and_deserialize(filename):
    """Deserialize JSON to dict"""

    with open(filename, "r", encoding="utf=8") as f:
        return json.load(f)
