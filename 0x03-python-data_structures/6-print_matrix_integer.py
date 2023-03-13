#!/usr/bin/python3

"""
function that will Print a matrix of integers
"""


def print_matrix_integer(matrix=[[]]):
    """
    Print matrix of integers

    Args:
        matrix: matrix of integers

    Returns:
        None
    """
    if not matrix:
        return
    for row in matrix:
        for i in range(len(row)):
            if i == len(row) - 1:
                print("{:d}".format(row[i]), end="")
            else:
                print("{:d}".format(row[i]), end=" ")
        print()
