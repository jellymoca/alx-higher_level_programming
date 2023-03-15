#!/usr/bin/python3
"""
Module that replaces or adds key/value in a dictionary
"""


def update_dictionary(a_dictionary, key, value):
    """
    Replaces or adds key/value in a dictionary.

    Args:
        a_dictionary (dict): The dictionary to update.
        key (any): The key to update or add.
        value (any): The value to set.

    Returns:
        The updated dictionary.

    """
    a_dictionary[key] = value
    return a_dictionary
