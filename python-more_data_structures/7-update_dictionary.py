#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    li = list(a_dictionary.keys())
    for i in li:
        if li[i] == key:
            a_dicitionary[li] = key
        else:
            a_dictionary.update({k: v})
    return(a_dictionary)
