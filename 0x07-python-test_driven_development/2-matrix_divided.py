#!/usr/bin/python3
"""
    Module to divide a matrix
"""


def matrix_divided(matrix, div):
    """ A function that  divides a matrix"""
    text = "matrix must be a matrix (list of lists) of integers/floats"
    text_2 = "Each row of the matrix must have the same size"
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) is not list:
        raise TypeError(text)
    n = len(matrix[0])
    matrix_2 = []
    for m in matrix:
        inside = []
        if type(m) is not list:
            raise TypeError(text)
        if len(m) != n:
            raise TypeError(text_2)
        for i in m:
            if type(i) is not int and type(i) is not float:
                raise TypeError(text)
            inside.append(round((i / div), 2))
        matrix_2.append(inside)
    return matrix_2
