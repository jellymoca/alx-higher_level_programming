#!/usr/bin/python3
"""
returns the weighted average of all integers tuple (<score>, <weight>)
"""


def weight_average(my_list=[]):
    """
    Return the weighted average of all integers tuple (<score>, <weight>)
    """
    if not my_list:
        return 0
    numerator = sum(score * weight for score, weight in my_list)
    denominator = sum(weight for score, weight in my_list)
    return numerator / denominator
