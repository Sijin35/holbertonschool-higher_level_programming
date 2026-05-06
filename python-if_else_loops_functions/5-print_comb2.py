#!/usr/bin/python3

for i in range(100):
    if i > 0:
        print(", ", end="")
    print("{:02d}".format(i), end="")
    
