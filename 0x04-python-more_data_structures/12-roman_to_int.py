#!/usr/bin/python3
"""
Module for roman_to_int function
"""


def roman_to_int(roman_string):
    """
    Convert a Roman numeral to an integer
    """

    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    a = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
         'C': 100, 'D': 500, 'M': 1000}
    res = 0
    n = len(roman_string)

    for i in range(n):
        if i < n - 1 and a[roman_string[i]] < a[roman_string[i + 1]]:
            res -= a[roman_string[i]]
        else:
            res += a[roman_string[i]]
    return res
