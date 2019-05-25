#!/usr/bin/python3
"""
    Module to divide a matrix
"""


def matrix_mul(m_a, m_b):
    """ A function that  divides a matrix"""
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if m_a == []:
        raise ValueError("m_a can't be empty")
    if m_b == []:
        raise ValueError("m_b can't be empty")
    error_1 = "each row of m_a must should be of the same size"
    error_2 = "each row of m_b must should be of the same size"
    len_1 = len(m_a[0])
    len_2 = len(m_b[0])
    column_A = len_1
    row_B = len(m_b[0])
    # Number of colums of A must be equal to rows of B
    if column_A != row_B:
        raise ValueError("m_a and m_b can't be multiplied")
    for i in range(len_1):
        inside = []
        if type(m_a[i]) is not list:
            raise TypeError("m_a must be a list of lists")
        if len(m_a[i]) != len_1:
            raise TypeError(error_1)
        if m_a[i] == []:
            raise ValueError("m_a can't be empty")
        for j in range(len(m_a[i])):
            if type(m_a[i][j]) is not int:
                if type(m_a[i][j]) is not float:
                    raise TypeError("")
    for i in range(len_2):
        if type(m_b[i]) is not list:
            raise TypeError("m_b must be a list of lists")
        if len(m_b[i]) != len_2:
            raise TypeError(error_2)
        if m_b[i] == []:
            raise ValueError("m_b can't be empty")
        for j in range(len(m_b[i])):
            if type(m_b[i][j]) is not int:
                if type(m_b[i][j]) is not float:
                    raise TypeError("")
    # Here we make the multiplication
    new_matrix = []
    mul = 0
    for i in range(column_A):
        inside = []
        for j in range(row_B):
            mul += m_a[i][j] * m_b[j][i]
            inside.append(mul)
        new_matrix.append(inside)
    return new_matrix
