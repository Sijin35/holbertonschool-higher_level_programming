#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    a = len(argv) - 1

    if a == 1:
        print("{}".format(len(argv) - 1), "argument:")
    elif a > 1:
        print("{}".format(len(argv) - 1), "arguments:")
    elif a == 0:
        print("{}".format(len(argv) - 1), "arguments.")

    for i in range(1, a + 1):
        print("{}: {}".format(i, argv[i]))
