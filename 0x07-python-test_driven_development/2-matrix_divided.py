#!/usr/bin/python3
"""
Module matrix_divided
Divides each element of a matrix 
"""

def matrix_divided(matrix, div):
    """Return a new divided matrix"""
    if type(matrix) is not list:
        raise TypeError("matrix must be a \
                matrix (list of list) of integers/floats")
    if len(matrix) == 0:
        return []
    for l in matrix:
        if type(l) is not list:
            p
