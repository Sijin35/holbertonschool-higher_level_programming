#!/usr/bin/python3

def multiple_returns(sentence):
    c = 0
    if sentence == "":
        return 0, None
    for i in sentence:
        c += 1
    return c, sentence[0]
