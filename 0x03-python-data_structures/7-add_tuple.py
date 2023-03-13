#!/usr/bin/python3

"""
The function will add tuples
"""


def add_tuple(tuple_a=(), tuple_b=()):
    """
    Adds two tuples and returns a new tuple
    """
    # Fill the tuples with 0s up to length 2
    tuple_a = tuple_a + (0, 0)
    tuple_b = tuple_b + (0, 0)
    # Return the new tuple with the sum of the first two elements of each tuple
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
