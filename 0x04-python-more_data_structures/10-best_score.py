#!/usr/bin/python3
"""
This module contains a function that returns the key with the biggest integer
value in a dictionary.
"""


def best_score(a_dictionary):
    """Returns the key with the biggest integer value in a dictionary."""
    if not a_dictionary:
        return None
    max_score = max(a_dictionary.values())
    for key, value in a_dictionary.items():
        if value == max_score:
            return key
