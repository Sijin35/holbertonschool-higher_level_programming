#!/usr/bin/python3
"""Module that extends the builtin interator obtained from iter function"""


class CountedIterator:

    def __init__(self, obj):
        self.iterator = iter(obj)
        self.counter = 0
    
    def __iter__(self):
        return self
    
    def get_count(self):
        return self.counter

    def __next__(self):
        value = next(self.iterator)
        self.counter += 1
        return value
