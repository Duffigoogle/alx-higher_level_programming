#!/usr/bin/python3
"""Divide a matrix"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.
    Parameters:
        matrix: must be a list of lists of integers or floats
        div: must be a number (integer or float)
    Raises:
        TypeError: If matrix is not a list
        TypeError: If matrix is not a list of lists
        TypeError: If matrix is not a list of lists of numbers (int/float)
        TypeError: If the rows of the matrix are not the same size
        TypeError: If div is not a number
        ZeroDivisionError: If div is 0
    Returns:
        new_matrix: new matrix with all elements divided by div
    """
    err_matrix = "matrix must be a matrix(list of lists) of integers/floats"
    err_matrix2 = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list:
        raise TypeError(err_matrix)
    for li in matrix:
        if type(li) is not list:
            raise TypeError(err_matrix)
        else:
            for num in li:
                if not (type(num) is int or type(num) is float):
                    raise TypeError(err_matrix2)

    len_li = len(matrix[0])
    for li in matrix:
        if len(li) is not len_li:
            raise TypeError(
                "Each row of the matrix must have the same size")

    if not (type(div) is int or type(div) is float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_matrix.append(list(map(lambda num: round(num / div, 2), row)))

    return new_matrix
