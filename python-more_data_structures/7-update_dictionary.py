#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    li = list(a_dictionary.keys())
    for i in li:
        if i == key:
            a_dictionary[i] = value
        else:
            a_dictionary.update({key: value})
    return(a_dictionary)
