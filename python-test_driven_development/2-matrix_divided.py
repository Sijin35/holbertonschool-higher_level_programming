#!/usr/bin/python3
"""Module that defines a matrix where all elemets are divided"""


def matrix_divided(matrix, div):
    """Function that divies all elements of the matrix"""

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new = []
    for i in range(len(matrix)):
        row = []
        if not isinstance(matrix[i], list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
                )
        if len(matrix[0]) != len(matrix[i]):
            raise TypeError("Each row of the matrix must have the same size")
        for j in matrix[i]:
            if not isinstance(j, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists)"
                    "of integers/floats"
                )
            res = j / div
            row.append(round(res, 2))
        new.append(row)
    return new
