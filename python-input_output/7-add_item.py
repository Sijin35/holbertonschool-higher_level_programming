#!/usr/bin/python3
"""Module that adds all args to a list and save to a file"""
import sys


save_file = __import__('5-save_to_json_file').save_to_json_file
load_file = __import__('6-load_from_json_file').load_from_json_file

new = sys.argv[1:]

try:
    old = load_file("add_item.json")
except FileNotFoundError:
    old = []

updated = old + new
save_file(updated, "add_item.json")
