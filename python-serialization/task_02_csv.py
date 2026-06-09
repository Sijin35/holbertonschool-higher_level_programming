#!/usr/bin/python3
"""Module that converts CSV to JSON"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Converts CSV to JSON"""
    try:
        with open(csv_filename, "r", encoding="utf-8") as f:
            c = csv.DictReader(f)
            li = []
            for i in c:
                li.append(i)
    
        with open("data.json", "w", encoding="utf-8") as j:
            json.dump(li, j)
        return True
    except Exception:
        return False
