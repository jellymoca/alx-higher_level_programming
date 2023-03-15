#!/usr/bin/python3
"""
module 100-weight_average

Contains function weight_average
"""


def weight_average(my_list=[]):
    """
    Returns the weighted average of all integers tuple (<score>, <weight>)
    """
    if not my_list:
        return 0
    return sum(score * weight for score, weight in my_list)
    / sum(weight for score, weight in my_list)
