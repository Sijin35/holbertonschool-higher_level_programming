#!/usr/bin/python3


def fizzbuzz():
    myArray = []
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            myArray.append("FizzBuzz")
        elif i % 3 == 0:
            myArray.append("Fizz")
        elif i % 5 == 0:
            myArray.append("Buzz")
        else:
            myArray.append(i)
    result = " ".join(map(str, myArray))
    print(result)
