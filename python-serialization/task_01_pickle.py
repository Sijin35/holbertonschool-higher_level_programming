#!/usr/bin/python3
"""Module that serializes and deserializes Python objects using pickle"""
import pickle


class CustomObject:
    """Uses pickle module to serialize and deserialize"""

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        output = (
                f"Name: {self.name}\n"
                f"Age: {self.age}\n"
                f"Is Student: {self.is_student}"
            )
        print(output)

    def serialize(self, filename):
        self.filename = filename
        try:
            with open(self.filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, "rb") as f:
                return  pickle.load(f)
        except(FileNotFoundError, EOFError, pickle.UnpicklingError):
            return None
