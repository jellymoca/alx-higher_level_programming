#!/usr/bin/python3

"""
Print all integers of a list
"""

def print_list_integer(my_list=[]):
    """
    Print all integers of a list

    Args:
        my_list: list of integers

    Returns:
        None
    """
    for i in my_list:
        print("{:d}".format(i))

