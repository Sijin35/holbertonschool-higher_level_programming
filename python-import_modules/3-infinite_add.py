#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    a = len(argv)
    add = 0

    for i in range(1, a):
        add += int(argv[i])

    print(add)
