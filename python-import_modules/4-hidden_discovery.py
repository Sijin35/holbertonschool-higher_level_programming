#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4 as hid

    for i in sorted(dir(hid)):
        if not i.startswith("__"):
            print(i)
