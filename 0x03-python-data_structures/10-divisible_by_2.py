#!/usr/bin/python3
"""
This module contains one function divisible_by_2.
"""


def divisible_by_2(my_list=[]):
    """
    This function finds all multiples of 2 in a list.

    Args:
    my_list: list of integers.

    Returns:
    A new list with True or False, depending on whether the integer at the same
    position in the original list is a multiple of 2.

    """
    new_list = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list
