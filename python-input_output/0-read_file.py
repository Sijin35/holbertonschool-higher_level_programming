#!/usr/bin/python3
"""Module to read file and print in stdout"""


def read_file(filename=""):
  """Function that reads file and prints in stdout."""
  
  with open(filename, encoding="utf-8")as f:
    read_file = f.read)
    print(read_file, end="")
